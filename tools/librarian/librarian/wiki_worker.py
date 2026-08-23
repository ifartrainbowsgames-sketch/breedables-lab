"""Continuous wiki worker — the loop that lets Kimi run unattended.

Design constraints, in order of importance:

1. **Never write to main.** Every cycle commits to a dated working branch. A
   human merges. An unattended model that can push to main is a liability.
2. **Never write an invalid page.** Output goes through :mod:`wiki_page`, which
   renders house-style Markdown from JSON and refuses anything failing
   :mod:`wiki_lint`.
3. **Stop when the usage is gone.** A quota error is not a failure to retry —
   it is a signal to park. The worker records a cooldown deadline, reports it,
   and goes quiet until the quota is back. It then resumes on its own.
4. **Always have a defined next task.** The queue is derived from real gaps, so
   the loop never invents busywork or rewrites what is already fine.
5. **Be resumable.** State lives on disk, so a restart neither redoes finished
   work nor forgets an active cooldown.

Run it:

    python -m librarian.cli wiki-worker --queue          # what needs doing
    python -m librarian.cli wiki-worker --once           # one cycle
    python -m librarian.cli wiki-worker --loop --interval 1800
"""

from __future__ import annotations

import json
import re
import subprocess
import time
from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

from .kimi import KimiQuotaExhausted, KimiUnavailableError, _kimi_complete
from .wiki_lint import lint_wiki, parse_frontmatter
from .wiki_page import PAGE_CONTRACT, PageRejected, render_and_write
from .wiki_repo_context import CONTEXT_NOTE, build_repo_context
from .wiki_schema import SECTIONS

#: Pages under this many words are considered stubs worth expanding.
THIN_WORDS = 250

#: Never touch more than this many pages in one cycle.
MAX_WRITES_PER_CYCLE = 3

#: Pause between model calls in a cycle. Back-to-back requests were noticeably
#: more likely to come back truncated or malformed than spaced ones.
CALL_SPACING_SECONDS = 5

#: Where cooldown and progress state live (inside the gitignored .data folder).
STATE_PATH = Path("tools/librarian/.data/worker-state.json")


# --------------------------------------------------------------------------
# Persistent state
# --------------------------------------------------------------------------

def _now() -> datetime:
    return datetime.now(timezone.utc)


def load_state(repo_root: Path) -> dict[str, Any]:
    path = repo_root / STATE_PATH
    if not path.is_file():
        return {"cooldown_until": None, "completed": [], "cycles": 0}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"cooldown_until": None, "completed": [], "cycles": 0}


def save_state(repo_root: Path, state: dict[str, Any]) -> None:
    path = repo_root / STATE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def cooldown_remaining(state: dict[str, Any]) -> int:
    """Seconds left before the worker may call Kimi again. 0 means go."""
    raw = state.get("cooldown_until")
    if not raw:
        return 0
    try:
        until = datetime.fromisoformat(raw)
    except ValueError:
        return 0
    if until.tzinfo is None:
        until = until.replace(tzinfo=timezone.utc)
    return max(0, int((until - _now()).total_seconds()))


def start_cooldown(repo_root: Path, state: dict[str, Any], seconds: int,
                   reason: str) -> dict[str, Any]:
    until = _now() + timedelta(seconds=seconds)
    state["cooldown_until"] = until.isoformat()
    state["cooldown_reason"] = reason
    state["cooldown_started"] = _now().isoformat()
    save_state(repo_root, state)
    return state


def clear_cooldown(repo_root: Path, state: dict[str, Any]) -> dict[str, Any]:
    if state.get("cooldown_until"):
        state["cooldown_until"] = None
        state.pop("cooldown_reason", None)
        save_state(repo_root, state)
    return state


# --------------------------------------------------------------------------
# Queue
# --------------------------------------------------------------------------

@dataclass
class Task:
    kind: str          # fix-structure | expand-thin | fill-gap | add-evidence-note
    target: str        # docs-relative path, or a proposed one
    reason: str
    priority: int      # lower runs first

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

    @property
    def key(self) -> str:
        return f"{self.kind}:{self.target}"


def build_queue(repo_root: Path) -> list[Task]:
    """Derive the work queue from the wiki's actual state."""
    tasks: list[Task] = []
    docs = repo_root / "docs"

    # 1. structural violations always come first — they block CI
    for f in lint_wiki(repo_root).errors:
        tasks.append(Task("fix-structure", f.path, f"{f.rule}: {f.message}", 0))

    # 2. sections missing a canonical index
    for sec in SECTIONS:
        if not (docs / sec.slug / "index.md").is_file():
            tasks.append(Task("fill-gap", f"{sec.slug}/index.md",
                              f"{sec.title} has no overview page", 1))

    # 3. thin pages inside teaching sections
    for path in sorted(docs.rglob("*.md")):
        rel = path.relative_to(docs).as_posix()
        if rel.startswith("meta/"):
            continue
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if fm.get("type") in ("topic", "software", "project") and len(body.split()) < THIN_WORDS:
            tasks.append(Task("expand-thin", rel,
                              f"{len(body.split())} words — below the {THIN_WORDS} threshold", 2))

    # 4. projects whose evidence folder is still empty
    for path in sorted(docs.rglob("projects/*.md")):
        rel = path.relative_to(docs).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"`((?:training|research)/[^`]+/)`", text)
        if not m:
            continue
        folder = repo_root / m.group(1)
        if folder.is_dir() and not [p for p in folder.rglob("*")
                                    if p.is_file() and p.name != "README.md"]:
            tasks.append(Task("add-evidence-note", rel,
                              f"evidence folder {m.group(1)} is empty", 3))

    tasks.sort(key=lambda t: (t.priority, t.target))
    return tasks


# --------------------------------------------------------------------------
# Asking Kimi
# --------------------------------------------------------------------------

SYSTEM = """You maintain the Breedables Lab wiki — an open-source Academy for
Second Life breedables production.

You are given ONE maintenance task. Return ONE JSON object and nothing else: no
prose before or after, no Markdown fence. A renderer turns your JSON into
house-style Markdown and a linter rejects malformed structure, so inventing your
own layout only wastes the call.

""" + CONTEXT_NOTE + "\n" + PAGE_CONTRACT


def _task_prompt(repo_root: Path, task: Task, *, wiki_base_url: str = "") -> str:
    docs = repo_root / "docs"
    path = docs / task.target
    current = path.read_text(encoding="utf-8", errors="replace") if path.is_file() else ""
    fm, _ = parse_frontmatter(current)
    instruction = {
        "expand-thin": (
            "Expand this page with substantive, accurate content. Keep every "
            "existing fact and link. Add explanation, workflow steps and "
            "official documentation references. Do not pad."),
        "fix-structure": (
            "Rewrite this page so it satisfies the structure rules. The specific "
            "violation is given below."),
        "fill-gap": (
            "Write the missing section overview page. State the single question "
            "the section answers, list its topics, and link to them."),
        "add-evidence-note": (
            "This project's evidence folder is empty. Sharpen the page so the "
            "first artifact is obvious: exact steps, exact filenames, exact "
            "pass conditions. Do not invent results."),
    }[task.kind]

    return json.dumps({
        "task": task.kind,
        "target_path": task.target,
        "reason": task.reason,
        "instruction": instruction,
        "existing_frontmatter": fm,
        "existing_markdown": current[:12000],
        **build_repo_context(repo_root, wiki_base_url, editing=task.target),
    }, indent=2)


_JSON_BLOCK = re.compile(r"\{.*\}", re.S)


def extract_json_objects(text: str) -> list[str]:
    """Every balanced ``{...}`` block, largest first.

    A greedy ``{.*}`` regex spans from the first brace to the last, which
    silently welds two objects together when the model emits reasoning around
    its answer. Brace matching (string-aware, so braces inside values do not
    count) returns real candidates instead.
    """
    blocks: list[str] = []
    depth = 0
    start = -1
    in_string = False
    escaped = False
    for i, ch in enumerate(text):
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            if depth:
                depth -= 1
                if depth == 0 and start >= 0:
                    blocks.append(text[start:i + 1])
    if depth and start >= 0:  # truncated reply: keep the partial for repair
        blocks.append(text[start:])
    return sorted(blocks, key=len, reverse=True)


def repair_json(text: str) -> str:
    """Fix the JSON mistakes language models actually make.

    The dominant one is a raw newline inside a string value — models write
    Markdown prose into ``body`` and forget it must be escaped. Also handles
    trailing commas and smart quotes used as delimiters. This is rescue
    parsing: recover the intent before spending another call.
    """
    out: list[str] = []
    in_string = False
    escaped = False
    for i, ch in enumerate(text):
        if in_string:
            if escaped:
                out.append(ch)
                escaped = False
                continue
            if ch == "\\":
                out.append(ch)
                escaped = True
                continue
            if ch == '"':
                # Is this the end of the string, or a quote the model forgot to
                # escape inside it? A real closing quote is followed by a
                # structural character; anything else means we are still in the
                # string and the quote needs escaping.
                rest = text[i + 1:]
                nxt = rest.lstrip()[:1]
                if nxt in (",", ":", "}", "]", ""):
                    in_string = False
                    out.append(ch)
                else:
                    out.append('\\"')
                continue
            if ch == "\n":
                out.append("\\n")
                continue
            if ch == "\r":
                continue
            if ch == "\t":
                out.append("\\t")
                continue
            out.append(ch)
            continue
        if ch == '"':
            in_string = True
        out.append(ch)
    repaired = "".join(out)
    repaired = re.sub(r",(\s*[}\]])", r"\1", repaired)  # trailing commas
    return repaired


def parse_page_json(reply: str) -> dict[str, Any]:
    """Pull the JSON object out of a model reply, fenced or not.

    Tries strict parsing first, then a repair pass, then the largest embedded
    object. Raises PageRejected with the underlying decode error so the caller
    can re-ask with something specific to fix.
    """
    text = reply.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n", "", text)
        text = re.sub(r"\n```\s*$", "", text)

    candidates = [text, repair_json(text)]
    for block in extract_json_objects(text):
        candidates += [block, repair_json(block)]

    last: Exception | None = None
    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError as exc:
            last = exc
            continue
        if isinstance(parsed, dict):
            return parsed
        last = ValueError(f"expected a JSON object, got {type(parsed).__name__}")
    raise PageRejected(f"could not parse a JSON object from the reply: {last}")


def normalise_payload(payload: dict[str, Any], task: Task,
                      repo_root: Path | None = None) -> dict[str, Any]:
    """Reconcile what the model returned with the task it was given.

    The contract permits ``{"action": "update", "path": ...}`` for editing an
    existing page, but the renderer needs ``title``/``section``/``type``. Rather
    than reject a well-intentioned reply, fill those in from the task's own
    target and the page already on disk.
    """
    payload = dict(payload)
    target = payload.pop("path", None) or task.target
    if payload.pop("action", None) and target:
        payload.setdefault("slug", Path(target).stem)
    parts = task.target.split("/")
    payload.setdefault("section", parts[0])
    payload.setdefault("slug", Path(task.target).stem)

    # Updating an existing page: the model often omits fields it is not
    # changing. Carry them over from the page on disk rather than rejecting a
    # reply that is otherwise fine.
    if repo_root is not None:
        existing = repo_root / "docs" / task.target
        if existing.is_file():
            fm, body = parse_frontmatter(existing.read_text(encoding="utf-8", errors="replace"))
            if not payload.get("title"):
                heading = re.search(r"^# +(.+)$", body, re.M)
                payload["title"] = fm.get("title") or (
                    heading.group(1).strip() if heading else Path(task.target).stem)
            for key in ("section", "type", "question"):
                if not payload.get(key) and fm.get(key):
                    payload[key] = fm[key]
    if not payload.get("type"):
        if "software" in parts[:-1]:
            payload["type"] = "software"
        elif "projects" in parts[:-1]:
            payload["type"] = "project"
        elif "paths" in parts[:-1]:
            payload["type"] = "path"
        elif parts[-1] == "index.md":
            payload["type"] = "index"
        else:
            payload["type"] = "topic"
    return payload


def ask_kimi(repo_root: Path, task: Task, *, timeout: float = 180.0,
             wiki_base_url: str = "", attempts: int = 2) -> dict[str, Any]:
    """Ask for a page, re-asking once if the reply will not parse.

    Bounded deliberately: a model that cannot produce valid JSON twice is not
    going to on the third try, and the loop has a budget to respect. A quota
    error is never retried — it propagates so the caller can park.
    """
    prompt = _task_prompt(repo_root, task, wiki_base_url=wiki_base_url)
    last: Exception | None = None
    for attempt in range(1, attempts + 1):
        reply, _backend = _kimi_complete(
            system=SYSTEM,
            user=prompt,
            timeout=timeout,
            max_tokens=8000,
            cwd=repo_root,
        )
        try:
            return parse_page_json(reply)
        except PageRejected as exc:
            last = exc
            if attempt >= attempts:
                break
            # re-ask with the specific failure, per the guardrails pattern
            prompt = (
                f"{prompt}\n\nYour previous reply could not be parsed: {exc}\n"
                "Return ONE valid JSON object and nothing else. Escape every "
                "newline inside a string value as \\n. No trailing commas. "
                "No Markdown fence."
            )
    raise last or PageRejected("no reply from the model")


# --------------------------------------------------------------------------
# Git safety
# --------------------------------------------------------------------------

def _git(repo_root: Path, *args: str) -> str:
    p = subprocess.run(["git", *args], cwd=str(repo_root), capture_output=True, timeout=60)
    return p.stdout.decode("utf-8", errors="replace").strip()


def tree_is_dirty(repo_root: Path) -> bool:
    """True if the working copy holds uncommitted changes to *tracked* files.

    Untracked files are deliberately ignored: git carries them across a branch
    switch untouched, so they cannot be lost by one. Only modified tracked
    files make switching unsafe.
    """
    return bool(_git(repo_root, "status", "--porcelain", "--untracked-files=no"))


def working_branch(repo_root: Path) -> str | None:
    """Create or reuse today's worker branch. Never returns main.

    Returns None when the working copy is dirty. Switching branches under
    uncommitted work is how you lose it: git either refuses or drags the
    changes across, and an unattended process must do neither. In that case the
    caller writes in place and leaves committing to a human.
    """
    name = f"wiki-worker/{date.today().isoformat()}"
    current = _git(repo_root, "rev-parse", "--abbrev-ref", "HEAD")
    if current == name:
        return name
    if tree_is_dirty(repo_root):
        return None
    if _git(repo_root, "branch", "--list", name):
        _git(repo_root, "checkout", name)
    else:
        _git(repo_root, "checkout", "-b", name)
    return name


def commit_cycle(repo_root: Path, summary: str, paths: list[str]) -> str | None:
    """Commit only the pages this cycle wrote.

    Deliberately not ``git add docs``: the working tree may hold unrelated
    human edits, and an unattended process must never sweep those into its own
    commit. Only the files the cycle actually produced are staged.
    """
    if not paths:
        return None
    for rel in paths:
        _git(repo_root, "add", "--", f"docs/{rel}")
    if not _git(repo_root, "diff", "--cached", "--name-only"):
        return None
    _git(repo_root, "commit", "-m",
         f"wiki-worker: {summary}\n\nAutomated cycle. Structure validated by "
         "`librarian.cli wiki-lint` before commit.")
    return _git(repo_root, "rev-parse", "--short", "HEAD")


# --------------------------------------------------------------------------
# Cycle
# --------------------------------------------------------------------------

def run_cycle(repo_root: Path, *, dry_run: bool = False,
              max_writes: int = MAX_WRITES_PER_CYCLE,
              ask: Callable[[Path, Task], dict[str, Any]] | None = None,
              wiki_base_url: str = "") -> dict[str, Any]:
    """One pass: check quota, build the queue, act, validate, commit."""
    if ask is None:
        def ask(repo, task):
            return ask_kimi(repo, task, wiki_base_url=wiki_base_url)
    state = load_state(repo_root)
    result: dict[str, Any] = {
        "started": _now().isoformat(),
        "written": [], "rejected": [], "commit": None, "dry_run": dry_run,
    }

    # --- parked on quota? do nothing, cheaply -----------------------------
    remaining = cooldown_remaining(state)
    if remaining:
        result.update(status="cooling_down", retry_in_seconds=remaining,
                      reason=state.get("cooldown_reason", "usage exhausted"),
                      resumes_at=state.get("cooldown_until"))
        return result
    if state.get("cooldown_until"):
        clear_cooldown(repo_root, state)
        result["note"] = "cooldown expired — resuming"

    queue = build_queue(repo_root)
    result["queue_depth"] = len(queue)
    todo = [t for t in queue if t.key not in set(state.get("completed", []))][:max_writes]
    result["tasks"] = [t.as_dict() for t in todo]

    if not todo:
        result["status"] = "idle"
        result["note"] = "nothing to do — wiki is structurally clean and no gaps found"
        return result

    if dry_run:
        result["status"] = "planned"
        result["note"] = "dry run — no calls made, no files written"
        return result

    original_branch = _git(repo_root, "rev-parse", "--abbrev-ref", "HEAD")
    branch = working_branch(repo_root)
    if branch is None:
        result["branch"] = original_branch
        result["commit_skipped"] = (
            "working copy has uncommitted changes — pages were written in place "
            "and left unstaged. Commit your own work, then the worker will use "
            "its own branch again.")
    else:
        result["branch"] = branch

    for index, task in enumerate(todo):
        if index:
            time.sleep(CALL_SPACING_SECONDS)
        try:
            payload = ask(repo_root, task)
        except KimiQuotaExhausted as exc:
            state = start_cooldown(repo_root, state, exc.retry_after, str(exc))
            result.update(status="quota_exhausted",
                          retry_in_seconds=exc.retry_after,
                          resumes_at=state["cooldown_until"],
                          reason=str(exc))
            break  # stop calling; keep whatever this cycle already produced
        except KimiUnavailableError as exc:
            result.update(status="backend_unavailable", reason=str(exc))
            break
        except (json.JSONDecodeError, PageRejected, ValueError, TypeError, KeyError) as exc:
            # a malformed model reply is a rejection to record, not a crash
            result["rejected"].append(
                {"task": task.key, "error": f"{type(exc).__name__}: {str(exc)[:200]}"})
            continue

        payload = normalise_payload(payload, task, repo_root)
        try:
            rel, _ = render_and_write(repo_root, payload)
        except (PageRejected, ValueError, TypeError, KeyError) as exc:
            result["rejected"].append(
                {"task": task.key, "error": f"{type(exc).__name__}: {str(exc)[:300]}"})
            continue

        result["written"].append({"task": task.key, "path": rel})
        state.setdefault("completed", []).append(task.key)

    # --- a page is only kept if the whole wiki still validates -------------
    if result["written"]:
        report = lint_wiki(repo_root)
        if not report.ok:
            for w in result["written"]:
                _git(repo_root, "checkout", "--", f"docs/{w['path']}")
            result.update(status="reverted", written=[],
                          reason="post-write lint failed; cycle rolled back",
                          lint_errors=[str(f) for f in report.errors[:5]])
        else:
            written_paths = [w["path"] for w in result["written"]]
            if branch is None:
                result["commit"] = None  # dirty tree: leave the pages unstaged
            else:
                summary = f"{len(written_paths)} page(s): " + ", ".join(written_paths)
                result["commit"] = commit_cycle(repo_root, summary, written_paths)

    # leave the checkout where we found it — the worker owns a branch, not your
    # working copy
    if branch and original_branch and original_branch != branch:
        _git(repo_root, "checkout", original_branch)

    state["cycles"] = state.get("cycles", 0) + 1
    state["last_cycle"] = _now().isoformat()
    save_state(repo_root, state)
    result.setdefault("status", "ok")
    return result


def run_forever(repo_root: Path, *, interval: int = 1800,
                cycle_fn=None, max_cycles: int | None = None,
                sleep_fn: Callable[[float], None] = time.sleep) -> None:
    """The 24/7 loop.

    Sleeps out a quota cooldown rather than hammering a spent account, and picks
    the work back up by itself the moment the quota is available again.
    """
    cycle_fn = cycle_fn or run_cycle
    failures = 0
    cycles = 0
    while max_cycles is None or cycles < max_cycles:
        cycles += 1
        wait = interval
        try:
            out = cycle_fn(repo_root)
            failures = 0
            status = out.get("status", "ok")
            print(json.dumps({"cycle": cycles, **{
                k: v for k, v in out.items()
                if k in ("status", "queue_depth", "written", "rejected",
                         "commit", "branch", "note", "retry_in_seconds",
                         "resumes_at", "reason")}}, indent=2), flush=True)

            if status in ("quota_exhausted", "cooling_down"):
                # park for exactly as long as the provider asked, plus a minute
                wait = int(out.get("retry_in_seconds", 3600)) + 60
                print(f"usage exhausted — sleeping {wait}s, then resuming automatically",
                      flush=True)
            elif status == "backend_unavailable":
                wait = min(interval * 4, 3600)
            elif status == "idle":
                wait = max(interval, 3600)  # nothing to do; check back less often
        except Exception as exc:  # keep the loop alive
            failures += 1
            print(f"cycle {cycles} failed ({failures} in a row): {exc}", flush=True)
            wait = min(interval * (2 ** failures), 3600)

        sleep_fn(wait)

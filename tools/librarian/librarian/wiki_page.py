"""Structured page authoring — the only sanctioned way to write a wiki page.

Kimi does not write Markdown. It returns **JSON** describing a page, and this
module renders it into house-style Markdown, in the correct folder, with front
matter. The renderer owns the layout, so a model cannot invent headings, repeat
sections, bury the answer, or drop a page in the wrong place.

This is the "rules engine has veto power" pattern: generate, validate, then
write — and refuse the write if validation fails.

    payload = {
        "title": "Baking high to low",
        "section": "texturing",
        "type": "topic",
        "summary": "...",
        "studio_pick": "...",
        "sections": [{"heading": "How it works", "body": "..."}],
        "watch": [{"title": "...", "url": "...", "why": "..."}],
        "read":  [{"title": "...", "url": "..."}],
        "evidence_folder": "training/texturing/baking/",
    }
    render_and_write(repo_root, payload)
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .wiki_lint import lint_page
from .wiki_schema import SECTIONS_BY_SLUG, TYPE_FOLDERS, LintReport


class PageRejected(Exception):
    """The proposed page violates the information architecture."""


def slugify(title: str) -> str:
    s = re.sub(r"[^\w\s-]", "", title.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)


#: Keys a payload must carry before it is worth rendering. A model can omit
#: anything, so this is checked rather than assumed — a malformed reply must be
#: a rejection the cycle records, never an exception that kills the run.
REQUIRED_KEYS = ("title", "section", "type")


def target_path(payload: dict[str, Any]) -> str:
    """Where this page is allowed to live. Not negotiable by the model."""
    if not isinstance(payload, dict):
        raise PageRejected(f"expected a JSON object, got {type(payload).__name__}")
    missing = [k for k in REQUIRED_KEYS if not str(payload.get(k, "")).strip()]
    if missing:
        raise PageRejected("payload is missing required key(s): " + ", ".join(missing))
    section = payload.get("section", "")
    ptype = payload.get("type", "topic")
    if section not in SECTIONS_BY_SLUG:
        raise PageRejected(
            f"unknown section '{section}'. Valid: {', '.join(SECTIONS_BY_SLUG)}"
        )
    sec = SECTIONS_BY_SLUG[section]
    if ptype not in sec.allows:
        raise PageRejected(
            f"type '{ptype}' is not allowed in {sec.title}. "
            f"Allowed: {', '.join(sec.allows)}"
        )
    folder = TYPE_FOLDERS.get(ptype)
    slug = payload.get("slug") or slugify(payload["title"])
    parts = [section] + ([folder] if folder else []) + [f"{slug}.md"]
    return "/".join(parts)


def _table(rows: list[dict[str, str]], cols: list[tuple[str, str]]) -> list[str]:
    out = ["| " + " | ".join(h for h, _ in cols) + " |",
           "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        cells = []
        for _, key in cols:
            v = str(r.get(key, "") or "")
            if key == "url" and v:
                v = f"[{r.get('title', 'link')}]({v})"
            cells.append(v.replace("|", "\\|"))
        out.append("| " + " | ".join(cells) + " |")
    return out


def render(payload: dict[str, Any]) -> str:
    """Render house-style Markdown. The model supplies content, never layout."""
    title = payload["title"].strip()
    section = payload.get("section", "")
    ptype = payload.get("type", "topic")

    fm = ["---", f'title: "{title}"']
    if section:
        fm.append(f"section: {section}")
    fm.append(f"type: {ptype}")
    if payload.get("question"):
        fm.append(f'question: "{payload["question"]}"')
    fm.append("---")

    out = fm + ["", f"# {title}", ""]

    # metadata card — never loose bold lines, which render as one run-on blob
    meta = []
    if payload.get("prerequisites"):
        meta.append(f"    **Prerequisites** — {payload['prerequisites']}")
    if payload.get("evidence_folder"):
        meta.append(f"    **Evidence folder** — `{payload['evidence_folder']}`")
    if payload.get("canonical_note"):
        meta.append(f"    **Canonical home** — {payload['canonical_note']}")
    if meta:
        out += ['!!! info "About this page"']
        out += [m + "  " for m in meta[:-1]] + [meta[-1], ""]

    if payload.get("summary"):
        out += [payload["summary"].strip(), ""]

    # answer first
    if payload.get("studio_pick"):
        out += ['!!! tip "Studio pick"',
                "    " + payload["studio_pick"].strip().replace("\n", "\n    "), ""]

    # free vs paid always as tabs, never two stacked tables
    if payload.get("tools_free") or payload.get("tools_paid"):
        cols = [("Tool", "title"), ("Link", "url"), ("Best for", "best_for")]
        if payload.get("tools_free"):
            out += ['=== "Free tools"', ""]
            out += ["    " + l for l in _table(payload["tools_free"], cols)] + [""]
        if payload.get("tools_paid"):
            out += ['=== "Paid tools"', ""]
            out += ["    " + l for l in _table(payload["tools_paid"], cols)] + [""]

    if payload.get("watch"):
        out += ["## Watch", ""]
        out += _table(payload["watch"], [("Topic", "topic"), ("Video", "url"), ("Why this one", "why")]) + [""]

    if payload.get("read"):
        out += ["## Read", ""]
        out += _table(payload["read"], [("Source", "url"), ("Covers", "covers")]) + [""]

    for sec in payload.get("sections", []):
        out += [f"## {sec['heading'].strip()}", "", sec["body"].strip(), ""]

    if payload.get("steps"):
        out += ["## Do", ""]
        out += [f"{i}. {s}" for i, s in enumerate(payload["steps"], 1)] + [""]

    if payload.get("artifacts"):
        out += ["## Produce", "", "| Artifact | Path |", "|----------|------|"]
        out += [f"| {a['artifact']} | `{a['path']}` |" for a in payload["artifacts"]] + [""]

    if payload.get("checklist"):
        out += ["## Done when", ""]
        out += [f"- [ ] {c}" for c in payload["checklist"]] + [""]

    if payload.get("related"):
        out += ["## Related", ""]
        out += [f"- [{r['title']}]({r['path']})" for r in payload["related"]] + [""]

    return "\n".join(out).rstrip() + "\n"


def validate(rel: str, markdown: str,
             known_pages: set[str] | None = None) -> LintReport:
    report = LintReport()
    lint_page(rel, markdown, report, known_pages=known_pages)
    return report


def _known_pages(repo_root: Path, incoming: str) -> set[str]:
    """Every page that will exist once this one lands."""
    docs = repo_root / "docs"
    pages = {p.relative_to(docs).as_posix() for p in docs.rglob("*.md")} if docs.is_dir() else set()
    pages.add(incoming)
    return pages


#: A rendered page carrying less than this much prose is a failed generation,
#: not a short page. Seen in practice: a model answered an "expand this page"
#: task with a title and nothing else, and the write replaced 243 words with 6.
MIN_BODY_WORDS = 60

#: A rewrite may not drop below this fraction of what it replaces. Expanding a
#: page must never be able to shrink it.
MIN_RETAINED_FRACTION = 0.6


def _body_words(markdown: str) -> int:
    from .wiki_lint import parse_frontmatter

    _, body = parse_frontmatter(markdown)
    return len(body.split())


def check_not_destructive(repo_root: Path, rel: str, markdown: str) -> None:
    """Refuse a write that would gut the page it replaces.

    Structure validation cannot catch this: a near-empty page is perfectly
    well-formed. Only comparing against what is already there does.
    """
    new_words = _body_words(markdown)
    if new_words < MIN_BODY_WORDS:
        raise PageRejected(
            f"rendered page has only {new_words} words of body content "
            f"(minimum {MIN_BODY_WORDS}) — the generation produced no substance")

    existing = repo_root / "docs" / rel
    if not existing.is_file():
        return
    old_words = _body_words(existing.read_text(encoding="utf-8", errors="replace"))
    floor = int(old_words * MIN_RETAINED_FRACTION)
    if old_words and new_words < floor:
        raise PageRejected(
            f"rewrite would shrink the page from {old_words} to {new_words} words "
            f"(floor {floor}) — refusing to discard existing content")


def render_and_write(repo_root: Path, payload: dict[str, Any], *,
                     dry_run: bool = False) -> tuple[str, LintReport]:
    """Render, validate, then write. Refuses to write an invalid page.

    Link targets are resolved against the real docs tree, so a model that
    invents a path or writes one repo-relative is rejected before the file is
    created rather than surfacing later as a broken build.
    """
    rel = target_path(payload)
    markdown = render(payload)
    check_not_destructive(repo_root, rel, markdown)
    report = validate(rel, markdown, known_pages=_known_pages(repo_root, rel))
    if not report.ok:
        raise PageRejected(
            f"generated page failed structure validation:\n"
            + "\n".join(str(f) for f in report.errors)
        )
    if not dry_run:
        out = repo_root / "docs" / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(markdown, encoding="utf-8")
    return rel, report


#: Handed to Kimi verbatim. It describes the JSON contract, not Markdown, so the
#: model never gets the chance to invent layout.
PAGE_CONTRACT = """Return ONE JSON object describing a wiki page. Do not return Markdown.
The renderer owns all formatting — you supply content only.

{
  "title":     "Sentence case. Never an internal code like B05 or A03.",
  "section":   "one of: modeling | texturing | rigging-animation | second-life | engineering | academy | research",
  "type":      "topic | software | project | path | reference | candidate",
  "slug":      "optional-kebab-case-filename",
  "summary":   "One paragraph. What this page is for.",
  "question":  "index pages only: the single question the page answers",
  "prerequisites": "optional, e.g. 'Retopology'",
  "evidence_folder": "optional repo path, e.g. training/texturing/a01/",
  "studio_pick": "optional: what we chose and WHY, with evidence",
  "tools_free": [{"title": "", "url": "", "best_for": ""}],
  "tools_paid": [{"title": "", "url": "", "best_for": ""}],
  "watch":     [{"topic": "", "title": "", "url": "", "why": ""}],
  "read":      [{"title": "", "url": "", "covers": ""}],
  "sections":  [{"heading": "Unique heading", "body": "Markdown prose"}],
  "steps":     ["hands-on step"],
  "artifacts": [{"artifact": "", "path": ""}],
  "checklist": ["pass condition"],
  "related":   [{"title": "", "path": "relative/path.md"}]
}

HARD RULES — the write is rejected if you break them:
1. Every heading in "sections" must be UNIQUE on the page. Recurring labels go
   in the body as **bold text**, never as a heading.
2. At most 25 headings total.
3. No internal codes (A01, B07) in "title" or in any link text.
4. type "path" pages link only — no Watch/Read/Do/Produce content. They point at
   the canonical subject page.
5. Every topic has exactly ONE canonical page. If the topic already exists, return
   {"action": "update", "path": "existing/path.md", ...} instead of a new page.
6. Do not invent URLs.
"""

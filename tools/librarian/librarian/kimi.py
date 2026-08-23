"""Kimi briefings — Kimi Code CLI (subscription OAuth) or Open Platform API."""

from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path
from typing import Any

import httpx

from .academy_manifest import code_glossary, humanize_codes
from .wiki_context import WIKI_MISSION

from .wiki_page import PAGE_CONTRACT

DEFAULT_BASE_URL = "https://api.moonshot.ai/v1"
DEFAULT_API_MODEL = "kimi-k3"
DEFAULT_CLI_MODEL = "kimi-code/kimi-for-coding"
KIMI_CODE_API_BASE = "https://api.kimi.ai/coding/v1"
KIMI_CODE_TOKEN_URL = "https://auth.kimi.ai/api/oauth/token"
KIMI_CODE_CLIENT_ID = "17e5f671-d194-4dfb-9706-5516cb48c098"
WIKI_BREEDABLES_INVENTORY = "docs/research/breedables-inventory-and-software.md"


class KimiUnavailableError(RuntimeError):
    """No Kimi backend configured or authenticated."""


class KimiQuotaExhausted(KimiUnavailableError):
    """Usage is spent or rate-limited — stop calling and try again later.

    Distinct from KimiUnavailableError because the response is different: an
    unauthenticated backend needs a human, whereas an exhausted quota just needs
    time. ``retry_after`` is seconds, taken from the Retry-After header when the
    server sends one and otherwise a conservative default.
    """

    def __init__(self, message: str, retry_after: int = 3600) -> None:
        super().__init__(message)
        self.retry_after = max(60, int(retry_after))


#: Substrings that mean "out of usage", not "broken". Matched case-insensitively
#: against the provider's error body.
_QUOTA_MARKERS = (
    "quota",
    "insufficient balance",
    "insufficient_quota",
    "exceeded_current_quota",
    "rate_limit",
    "rate limit",
    "too many requests",
    "billing",
    "credit",
)


def _quota_error_from(status_code: int, body: str, headers: Any = None) -> "KimiQuotaExhausted | None":
    """Classify a failed response as a quota/rate-limit condition, or not."""
    lowered = (body or "").lower()
    hit = status_code in (402, 429) or any(m in lowered for m in _QUOTA_MARKERS)
    if not hit:
        return None
    retry_after = 3600
    try:
        if headers is not None:
            raw = headers.get("Retry-After") or headers.get("retry-after")
            if raw:
                retry_after = int(float(raw))
    except (TypeError, ValueError):
        pass
    # a plain 429 with no hint usually clears quickly; a 402 needs real time
    if retry_after == 3600 and status_code == 429:
        retry_after = 300
    return KimiQuotaExhausted(
        f"Kimi usage exhausted (HTTP {status_code}): {(body or '')[:200]}",
        retry_after=retry_after,
    )


def _glossary_block() -> str:
    lines = [f"- {code} → {label}" for code, label in sorted(code_glossary().items())]
    return "\n".join(lines)


def kimi_cli_exe() -> Path | None:
    override = os.getenv("KIMI_CLI_EXE", "").strip()
    if override:
        path = Path(override)
        return path if path.is_file() else None
    home = Path.home() / ".kimi-code" / "bin"
    for name in ("kimi.exe", "kimi"):
        candidate = home / name
        if candidate.is_file():
            return candidate
    return None


def kimi_code_cred_path() -> Path | None:
    cred_dir = Path.home() / ".kimi-code" / "credentials"
    matches = sorted(cred_dir.glob("kimi-code-env-*.json"))
    return matches[0] if matches else None


def kimi_cli_logged_in() -> bool:
    return kimi_code_cred_path() is not None


def kimi_cli_ready() -> bool:
    return kimi_cli_logged_in()


def resolve_kimi_backend() -> str:
    """Return ``cli``, ``api``, or ``off``. Default auto: CLI (subscription) then API."""
    explicit = os.getenv("KIMI_BACKEND", "").strip().lower()
    if explicit in {"off", "local", "none", "false", "0"}:
        return "off"
    if explicit == "api":
        return "api" if os.getenv("MOONSHOT_API_KEY") else "off"
    if explicit == "cli":
        return "cli" if kimi_cli_ready() else "off"
    if kimi_cli_ready():
        return "cli"
    if os.getenv("MOONSHOT_API_KEY"):
        return "api"
    return "off"


def _cli_model_to_api(model: str) -> str:
    if model.startswith("kimi-code/"):
        return model.split("/", 1)[1]
    return model


def _load_kimi_code_creds() -> dict[str, Any]:
    path = kimi_code_cred_path()
    if path is None:
        raise KimiUnavailableError("Kimi Code not logged in — run: kimi login --region global")
    return json.loads(path.read_text(encoding="utf-8"))


def _save_kimi_code_creds(creds: dict[str, Any]) -> None:
    path = kimi_code_cred_path()
    if path is None:
        raise KimiUnavailableError("Kimi Code credential file missing")
    path.write_text(json.dumps(creds, indent=2) + "\n", encoding="utf-8")


def _ensure_kimi_code_access_token() -> str:
    creds = _load_kimi_code_creds()
    access = creds.get("access_token")
    expires_at = float(creds.get("expires_at") or 0)
    if access and expires_at > time.time() + 120:
        return str(access)

    refresh = creds.get("refresh_token")
    if not refresh:
        raise KimiUnavailableError("Kimi Code refresh token missing — run: kimi login --region global")

    resp = httpx.post(
        KIMI_CODE_TOKEN_URL,
        data={
            "client_id": KIMI_CODE_CLIENT_ID,
            "grant_type": "refresh_token",
            "refresh_token": refresh,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30.0,
    )
    resp.raise_for_status()
    body = resp.json()
    creds["access_token"] = body["access_token"]
    creds["refresh_token"] = body["refresh_token"]
    creds["expires_in"] = body.get("expires_in", 900)
    creds["expires_at"] = int(time.time()) + int(creds["expires_in"])
    creds["scope"] = body.get("scope", creds.get("scope", "kimi-code"))
    creds["token_type"] = body.get("token_type", "Bearer")
    _save_kimi_code_creds(creds)
    return str(body["access_token"])


def _kimi_code_api_chat(
    *,
    system: str,
    user: str,
    model: str | None = None,
    timeout: float = 180.0,
    temperature: float = 0.4,
    max_tokens: int | None = 4096,
) -> str:
    """Kimi Code subscription API (OAuth) — no Open Platform balance required."""
    token = _ensure_kimi_code_access_token()
    api_model = _cli_model_to_api(model or os.getenv("KIMI_CLI_MODEL", DEFAULT_CLI_MODEL))
    body: dict[str, Any] = {
        "model": api_model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    }
    # Kimi Code coding models only accept the default temperature — do not send the field.
    if max_tokens is not None:
        body["max_tokens"] = max_tokens
    resp = httpx.post(
        f"{KIMI_CODE_API_BASE.rstrip('/')}/chat/completions",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=body,
        timeout=timeout,
    )
    if resp.status_code >= 400:
        quota = _quota_error_from(resp.status_code, resp.text, resp.headers)
        if quota:
            raise quota
    resp.raise_for_status()
    message = resp.json()["choices"][0]["message"]
    content = message.get("content") or message.get("reasoning_content") or ""
    if not content.endswith("\n"):
        content += "\n"
    return content


def _parse_kimi_cli_stream_json(stdout: str) -> str:
    parts: list[str] = []
    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if obj.get("role") == "assistant" and obj.get("content"):
            parts.append(str(obj["content"]))
    if not parts:
        raise ValueError("no assistant content in Kimi CLI output")
    text = "".join(parts)
    if not text.endswith("\n"):
        text += "\n"
    return text


def _kimi_cli_chat(
    *,
    system: str,
    user: str,
    model: str | None = None,
    cwd: Path | None = None,
    timeout: float = 180.0,
) -> str:
    exe = kimi_cli_exe()
    if exe is None:
        raise KimiUnavailableError("Kimi CLI executable not found")
    if not kimi_cli_logged_in():
        raise KimiUnavailableError("Kimi CLI not logged in — run: kimi login --region global")

    mdl = model or os.getenv("KIMI_CLI_MODEL", DEFAULT_CLI_MODEL)
    prompt = (
        f"{system.strip()}\n\n---\n\n{user.strip()}\n\n"
        "Reply in markdown only. Do not run tools or shell commands."
    )
    cmd = [str(exe), "-p", prompt, "--output-format", "stream-json", "-m", mdl]
    if cwd is not None:
        cmd.extend(["--add-dir", str(cwd)])

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(cwd) if cwd else None,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "")[:800]
        raise RuntimeError(f"kimi cli exit {result.returncode}: {detail}")
    stdout = result.stdout or ""
    if not stdout.strip():
        detail = (result.stderr or "")[:800]
        raise RuntimeError(f"kimi cli produced no output: {detail}")
    return _parse_kimi_cli_stream_json(stdout)


def _kimi_complete(
    *,
    system: str,
    user: str,
    timeout: float = 120.0,
    temperature: float = 0.4,
    max_tokens: int | None = 4096,
    api_model: str | None = None,
    cli_model: str | None = None,
    cwd: Path | None = None,
) -> tuple[str, str]:
    backend = resolve_kimi_backend()
    if backend == "cli":
        text = _kimi_code_api_chat(
            system=system,
            user=user,
            model=cli_model,
            timeout=timeout,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return text, "kimi-cli"
    if backend == "api":
        key = os.getenv("MOONSHOT_API_KEY", "")
        text = _kimi_chat_api(
            system=system,
            user=user,
            api_key=key,
            base_url=os.getenv("MOONSHOT_BASE_URL", DEFAULT_BASE_URL),
            model=api_model or os.getenv("MOONSHOT_MODEL", DEFAULT_API_MODEL),
            timeout=timeout,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return text, "kimi-api"
    raise KimiUnavailableError(
        "No Kimi backend — run `kimi login --region global` or set MOONSHOT_API_KEY"
    )


def _kimi_chat_api(
    *,
    system: str,
    user: str,
    api_key: str,
    base_url: str = DEFAULT_BASE_URL,
    model: str = DEFAULT_API_MODEL,
    timeout: float = 120.0,
    temperature: float = 0.4,
    max_tokens: int | None = 4096,
) -> str:
    body: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
    }
    if max_tokens is not None:
        body["max_tokens"] = max_tokens
    resp = httpx.post(
        f"{base_url.rstrip('/')}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=body,
        timeout=timeout,
    )
    if resp.status_code >= 400:
        quota = _quota_error_from(resp.status_code, resp.text, resp.headers)
        if quota:
            raise quota
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    if not content.endswith("\n"):
        content += "\n"
    return content


def humanize_report_local(payload: dict[str, Any]) -> str:
    """Deterministic plain-English report (no API)."""
    s = payload.get("summary", {})
    lines = [
        f"# Wiki morning briefing — {payload.get('generated_at', '')[:10]}",
        "",
        "## In plain English",
        "",
        f"- Checked **{s.get('wiki_links_checked', 0)}** tutorial and doc links in the wiki.",
    ]
    failed = s.get("wiki_links_failed", 0)
    if failed:
        lines.append(f"- **{failed}** link(s) are broken and need fixing.")
    else:
        lines.append("- All checked links responded OK.")

    if payload.get("academy_gaps"):
        lines.extend(["", "## Academy — what learners are missing", ""])
        for g in payload["academy_gaps"]:
            label = g.get("name") or humanize_codes(str(g.get("id", "?")))
            issues = [humanize_codes(i) for i in g.get("issues", [])]
            lines.append(f"- **{label}**: {'; '.join(issues)}")

    if payload.get("registry_gaps"):
        lines.extend(["", "## Tool registry — reviewer tasks", ""])
        for g in payload["registry_gaps"]:
            name = g.get("name", "?")
            issues = [humanize_codes(i) for i in g.get("issues", [])]
            lines.append(f"- **{name}**: {'; '.join(issues)}")

    if payload.get("next_actions"):
        lines.extend(["", "## Do this next", ""])
        for i, action in enumerate(payload["next_actions"], 1):
            lines.append(f"{i}. {humanize_codes(action)}")

    lines.extend(
        [
            "",
            "---",
            "",
            "Auto-generated (local). Learner guide: `docs/academy/index.md`",
        ]
    )
    return "\n".join(lines) + "\n"


def humanize_report_kimi(
    payload: dict[str, Any],
    *,
    timeout: float = 90.0,
) -> tuple[str, str]:
    """Kimi CLI (subscription) or Open Platform API for a morning briefing."""
    system = f"""You write morning briefings for a breedables studio wiki team.
Rules:
- Use plain English. Never use internal codes like A01 or B07 unless quoting a folder path.
- Use the glossary below when translating ids.
- Be concise: summary, then numbered next steps for a human (not an engineer).
- Link learners to docs/academy/index.md if they seem lost in naming.

Glossary:
{_glossary_block()}
"""
    user = (
        "Turn this daily wiki JSON into a markdown morning briefing.\n\n"
        f"```json\n{json.dumps(payload, indent=2)[:120000]}\n```"
    )
    return _kimi_complete(
        system=system,
        user=user,
        timeout=timeout,
        temperature=0.3,
    )


def write_human_report(
    payload: dict[str, Any],
    out_path,
    *,
    use_kimi: bool = True,
) -> dict[str, Any]:
    """Write report-human.md; Kimi CLI/API if available, else local humanizer."""
    source = "local"

    if use_kimi and resolve_kimi_backend() != "off":
        try:
            text, source = humanize_report_kimi(payload)
        except (httpx.HTTPError, KeyError, IndexError, RuntimeError, KimiUnavailableError, ValueError, subprocess.TimeoutExpired, AttributeError) as exc:
            text = humanize_report_local(payload)
            source = f"local (kimi failed: {exc})"
    else:
        text = humanize_report_local(payload)

    out_path.write_text(text, encoding="utf-8")
    return {"ok": True, "source": source, "path": str(out_path)}


def wiki_evolution_local(context: dict[str, Any]) -> str:
    """Structured improvement brief without API."""
    daily = context.get("daily_report", {})
    s = daily.get("summary", {})
    lines = [
        f"# Wiki evolution brief — {daily.get('generated_at', '')[:10]}",
        "",
        "## Mission check",
        "",
        "Open-source Academy for **Second Life breedables**: learn Blender step-by-step,",
        "use OSS tools, commit evidence in `training/`, ship in-world.",
        "",
        "## Today's health",
        "",
        f"- Links checked: {s.get('wiki_links_checked', 0)} · failed: {s.get('wiki_links_failed', 0)}",
        f"- Academy gaps: {s.get('academy_gaps', 0)} · Registry gaps: {s.get('registry_gaps', 0)}",
        "",
    ]

    if daily.get("academy_gaps"):
        lines.extend(["## Top wiki improvements (from gaps)", ""])
        for g in daily["academy_gaps"][:8]:
            label = g.get("name") or humanize_codes(str(g.get("id", "?")))
            lines.append(f"- **{label}**: {'; '.join(g.get('issues', []))}")
        lines.append("")

    if daily.get("registry_gaps"):
        lines.extend(["## Open-source tools to research", ""])
        for g in daily["registry_gaps"][:5]:
            lines.append(f"- **{g.get('name', '?')}**: {'; '.join(g.get('issues', []))}")
        lines.append("")

    lines.extend(
        [
            "## One lesson/lab to prioritize today",
            "",
            "Pick the first Blender lesson or studio lab with **empty** `training/` evidence.",
            "",
            "## Daily task list",
            "",
            "| Who | Task |",
            "|-----|------|",
            "| **Automated** | Link check, gap export, optional webscreen on failures |",
            "| **AI (Kimi)** | Draft lesson improvements, OSS tool notes — `kimi login` or API |",
            "| **Human** | Review AI drafts, commit evidence, approve wiki edits |",
            "",
            "---",
            "",
            "Auto-generated (local). Run `kimi login --region global` for full research brief.",
        ]
    )
    return "\n".join(lines) + "\n"


def wiki_evolution_kimi(
    context: dict[str, Any],
    *,
    repo_root: Path | None = None,
) -> tuple[str, str]:
    """Kimi researches how to evolve the wiki toward the breedables Academy goal."""
    system = f"""You are the research editor for Breedables Lab — an open-source Academy wiki for Second Life breedables.

Mission:
{WIKI_MISSION.strip()}

Each day you propose how to **evolve and improve** the wiki. Rules:
1. Teach step-by-step with the best **open-source** software (Blender, Material Maker, Ucupaint, Poly Haven, etc.).
2. Every suggestion must be actionable — name specific wiki pages or `training/` folders.
3. Split work: **human must do** / **AI can draft** / **already automated**.
4. Plain English for learners — no A01/B07 in headings or link text; codes are for folder paths only.
4a. STRUCTURE IS MACHINE-ENFORCED. Do not write Markdown for new pages.
   When you propose a page, emit a JSON object per the page contract below. A
   renderer turns it into house-style Markdown and a linter rejects it if the
   structure is wrong, so inventing your own layout only wastes a cycle.

{PAGE_CONTRACT}

5. Do not invent URLs. Prefer official Blender manual, SL wiki, GitHub, CC0 asset sites.
6. Output markdown with exactly these sections:
   ## Mission check
   ## Top 3 wiki improvements (specific pages)
   ## Wiki UX upgrades (from Outlands/Fandom/Material patterns)
   ## Images to find (slug + where to use)
   ## Open-source tools to research
   ## One lesson/lab to prioritize today
   ## Daily task list (human / AI / automated)
   ## Optional: breedables market angle

For **Wiki UX upgrades**, reference: hub card grids, sticky quick nav, Ctrl+K search, featured banners, infoboxes on case studies.
For **Images to find**, list slugs (e.g. kittycats, blender) and suggest official/Wikimedia URLs — these feed `wiki-images` CLI.

Glossary:
{_glossary_block()}
"""
    bundle = {
        "mission": context.get("mission", WIKI_MISSION),
        "blender_lessons": context.get("blender_lessons"),
        "studio_labs": context.get("studio_labs"),
        "registry_tools": context.get("registry_tools"),
        "daily_report_summary": context.get("daily_report", {}).get("summary"),
        "daily_gaps": {
            "academy": context.get("daily_report", {}).get("academy_gaps"),
            "registry": context.get("daily_report", {}).get("registry_gaps"),
            "failures": context.get("daily_report", {}).get("failures"),
            "next_actions": context.get("daily_report", {}).get("next_actions"),
        },
        "wiki_pages": context.get("wiki_pages"),
        "mkdocs_warnings": context.get("mkdocs_warnings"),
        "wiki_excerpts": context.get("doc_snippets"),
    }
    user = (
        "Write today's **wiki evolution brief**: how should we improve the Academy to better "
        "teach SL breedables with open-source tools, based on this state?\n\n"
        f"```json\n{json.dumps(bundle, indent=2)[:100000]}\n```"
    )
    return _kimi_complete(
        system=system,
        user=user,
        timeout=180.0,
        temperature=0.5,
        cwd=repo_root,
    )


def write_wiki_evolution_report(
    context: dict[str, Any],
    out_path,
    *,
    use_kimi: bool = True,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    source = "local"

    if use_kimi and resolve_kimi_backend() != "off":
        try:
            text, source = wiki_evolution_kimi(context, repo_root=repo_root)
        except (httpx.HTTPError, KeyError, IndexError, RuntimeError, KimiUnavailableError, ValueError, subprocess.TimeoutExpired, AttributeError) as exc:
            text = wiki_evolution_local(context)
            source = f"local (kimi failed: {exc})"
    else:
        text = wiki_evolution_local(context)

    out_path.write_text(text, encoding="utf-8")
    return {"ok": True, "source": source, "path": str(out_path)}


def _strip_markdown_fence(text: str) -> str:
    """Remove optional ```markdown wrapper from model output."""
    stripped = text.strip()
    if not stripped.startswith("```"):
        return text if text.endswith("\n") else text + "\n"
    lines = stripped.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    out = "\n".join(lines)
    return out if out.endswith("\n") else out + "\n"


def build_breedables_research_context(repo_root: Path) -> str:
    """Load wiki + research sources for Kimi to update the live inventory page."""
    pieces: list[str] = []
    for rel in (
        WIKI_BREEDABLES_INVENTORY,
        "docs/research/breedables-case-studies.md",
        "docs/research/breedables-market-study.md",
    ):
        path = repo_root / rel
        if path.exists():
            pieces.append(f"## {rel}\n\n{path.read_text(encoding='utf-8')[:50000]}")
    return "\n\n".join(pieces)


def breedables_research_local(*, wiki_excerpt: str = "") -> str:
    """Structured breedables inventory brief without API (seed for Kimi refresh)."""
    lines = [
        "# Breedables inventory & software — research brief",
        "",
        "**Status:** Local fallback (Kimi CLI/API unavailable — run `kimi login --region global`).",
        "",
        "See the full wiki page: `docs/research/breedables-inventory-and-software.md`.",
        "",
        "## What Kimi should expand when API is live",
        "",
        "1. Cross-check each line's **active/discontinued** status against official sites.",
        "2. Hunt forum posts / creator blogs for **documented 3D software** (Blender, Maya, ZBrush).",
        "3. Flag **species/theme gaps** not covered by active lines.",
        "4. Never invent URLs or claim a tool was used without a source.",
        "",
    ]
    if wiki_excerpt:
        lines.extend(["## Context excerpt", "", wiki_excerpt[:8000], ""])
    return "\n".join(lines) + "\n"


def breedables_research_kimi(
    *,
    context: str,
    repo_root: Path | None = None,
) -> tuple[str, str]:
    """Kimi updates the live wiki breedables inventory page."""
    from datetime import date

    today = date.today().isoformat()
    system = f"""You are the research editor for Breedables Lab — an open-source Academy wiki for Second Life breedables.

You are updating the **live wiki page** `docs/research/breedables-inventory-and-software.md`.

Write a complete, publish-ready markdown document (MkDocs Material) covering:

1. **Master inventory** — all documented SL breedable producers/lines from the context (do not drop Wild Kajaera, oYo, Foxtrot, Nixsy, PlantPets, DFS, etc. if present in context).
2. **Software & pipeline** — DOCUMENTED vs INFERRED 3D tools (Blender, Avastar, Maya, ZBrush, Substance, LSL); be explicit when unknown.
3. **What is still available to make** — species/mechanics/tech gaps with saturation caveats.
4. **Recommended OSS plugin shortlist** for making a new breedable (link to addon catalog conceptually).
5. **References** — real URLs only.

Rules:
- **Update and improve** the existing inventory page from context — do not shrink coverage.
- Front matter line: `**Kimi updated:** {today}` and `**Status:** RESEARCH — not a product plan`.
- Link companions: case studies, market study, platform baseline, addon catalog (relative paths).
- Use `!!! note` admonitions where appropriate (MkDocs).
- Do **not** wrap output in code fences. Output raw markdown only.
- Do not invent URLs or products. Mark unverified items clearly.
- Distinguish marketplaces (Sweetflowers) from producers.
"""
    user = (
        "Update the breedables inventory wiki page. Context (existing wiki + research):\n\n"
        f"{context[:120000]}"
    )
    text, source = _kimi_complete(
        system=system,
        user=user,
        timeout=300.0,
        max_tokens=12000,
        cwd=repo_root,
    )
    return _strip_markdown_fence(text), source


def write_breedables_research(
    out_path,
    *,
    context: str = "",
    use_kimi: bool = True,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Write breedables inventory to wiki (default) via Kimi subscription."""
    out = Path(out_path)
    source = "local"
    wiki_target = bool(
        repo_root
        and str(out).replace("\\", "/").endswith(WIKI_BREEDABLES_INVENTORY)
    )

    if use_kimi and resolve_kimi_backend() != "off":
        try:
            text, source = breedables_research_kimi(context=context, repo_root=repo_root)
        except (httpx.HTTPError, KeyError, IndexError, RuntimeError, KimiUnavailableError, ValueError, subprocess.TimeoutExpired, AttributeError) as exc:
            if wiki_target and out.exists():
                return {
                    "ok": False,
                    "source": f"local (kimi failed: {exc})",
                    "path": str(out),
                    "error": "Kimi failed; existing wiki page left unchanged",
                }
            text = breedables_research_local(wiki_excerpt=context)
            source = f"local (kimi failed: {exc})"
    else:
        if wiki_target and out.exists():
            return {
                "ok": False,
                "source": "off",
                "path": str(out),
                "error": "No Kimi backend; existing wiki page left unchanged",
            }
        text = breedables_research_local(wiki_excerpt=context)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")

    audit: dict[str, Any] | None = None
    if repo_root and source.startswith("kimi") and wiki_target:
        from datetime import date

        audit_dir = repo_root / "research" / "discoveries" / f"daily-{date.today().isoformat()}"
        audit_dir.mkdir(parents=True, exist_ok=True)
        audit_path = audit_dir / "breedables-inventory-kimi.md"
        audit_path.write_text(text, encoding="utf-8")
        audit = str(audit_path.relative_to(repo_root))

    result: dict[str, Any] = {"ok": True, "source": source, "path": str(out)}
    if audit:
        result["audit_copy"] = audit
    return result


def test_kimi_connection(
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    model: str | None = None,
) -> dict[str, Any]:
    """Smoke test — prefers Kimi CLI (subscription), then Open Platform API."""
    backend = resolve_kimi_backend()
    if backend == "cli":
        try:
            text = _kimi_code_api_chat(
                system="Reply with exactly one token.",
                user="Reply with exactly: kimi-ok",
                model=os.getenv("KIMI_CLI_MODEL", DEFAULT_CLI_MODEL),
                timeout=90.0,
                max_tokens=32,
            )
            return {
                "ok": True,
                "backend": "cli",
                "api": KIMI_CODE_API_BASE,
                "reply": text.strip(),
            }
        except (httpx.HTTPError, KimiUnavailableError, KeyError, IndexError) as exc:
            return {"ok": False, "backend": "cli", "error": str(exc)}

    key = api_key or os.getenv("MOONSHOT_API_KEY")
    if not key:
        return {
            "ok": False,
            "backend": "off",
            "error": "No Kimi backend — run `kimi login --region global` or set MOONSHOT_API_KEY",
        }
    base = base_url or os.getenv("MOONSHOT_BASE_URL", DEFAULT_BASE_URL)
    mdl = model or os.getenv("MOONSHOT_MODEL", DEFAULT_API_MODEL)
    try:
        resp = httpx.post(
            f"{base.rstrip('/')}/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={
                "model": mdl,
                "messages": [{"role": "user", "content": "Reply with exactly: kimi-ok"}],
                "max_tokens": 16,
                "temperature": 0,
            },
            timeout=60.0,
        )
        resp.raise_for_status()
        reply = resp.json()["choices"][0]["message"]["content"]
        return {"ok": True, "backend": "api", "model": mdl, "reply": reply.strip()}
    except httpx.HTTPStatusError as exc:
        body = exc.response.text[:500]
        return {"ok": False, "backend": "api", "error": f"HTTP {exc.response.status_code}", "detail": body}
    except (httpx.HTTPError, KeyError, IndexError) as exc:
        return {"ok": False, "backend": "api", "error": str(exc)}

"""Full wiki inventory and Kimi whole-wiki audit."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

from .kimi import KimiUnavailableError, WIKI_MISSION, _kimi_complete, resolve_kimi_backend

# Top-level information architecture. Every wiki page belongs to exactly one
# subject section; see docs/meta/wiki-style-guide.md.
SECTION_PREFIXES = {
    "docs/modeling/": "3D Modeling",
    "docs/texturing/": "Texturing & Materials",
    "docs/rigging-animation/": "Rigging & Animation",
    "docs/second-life/": "Second Life Production",
    "docs/engineering/": "Breedables Engineering",
    "docs/academy/": "Academy",
    "docs/research/": "Research & Tools",
    "docs/meta/": "Meta",
}


MKDOCS_NAV_SECTIONS = tuple(SECTION_PREFIXES.values())


def _first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "(no title)"


def inventory_wiki_pages(repo_root: Path) -> list[dict[str, Any]]:
    """List every published MkDocs page under docs/."""
    docs = repo_root / "docs"
    pages: list[dict[str, Any]] = []
    for path in sorted(docs.rglob("*.md")):
        rel = path.relative_to(repo_root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        section = "Other"
        for prefix, name in SECTION_PREFIXES.items():
            if rel.startswith(prefix):
                section = name
                break
        else:
            if rel in ("docs/index.md", "docs/pipeline.md", "docs/roadmap.md"):
                section = "Home"

        issues: list[str] = []
        if len(text.strip()) < 400:
            issues.append("thin content (<400 chars)")
        if "TODO" in text or "TBD" in text:
            issues.append("contains TODO/TBD")
        if rel.startswith("docs/modeling/blender/") and "Watch" not in text and "Video" not in text:
            issues.append("lesson may lack training links")
        if "/projects/" in rel and len(text.strip()) < 800:
            issues.append("studio lab likely skeleton")

        pages.append(
            {
                "path": rel,
                "title": _first_heading(text),
                "section": section,
                "chars": len(text),
                "has_images": "![" in text,
                "issues": issues,
            }
        )
    return pages


def mkdocs_build_warnings(repo_root: Path) -> list[str]:
    """Run mkdocs build and collect WARNING lines (broken internal links)."""
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
        )
        combined = (proc.stdout or "") + (proc.stderr or "")
    except (subprocess.TimeoutExpired, OSError) as exc:
        return [f"mkdocs build failed: {exc}"]

    warnings: list[str] = []
    for line in combined.splitlines():
        if "WARNING" in line and "Doc file" in line:
            warnings.append(line.strip())
    return warnings


def wiki_audit_local(context: dict[str, Any]) -> str:
    today = date.today().isoformat()
    pages = context.get("wiki_pages", [])
    warnings = context.get("mkdocs_warnings", [])
    thin = [p for p in pages if p.get("issues")]
    no_img = [p for p in pages if not p.get("has_images")
              and p["path"].split("/")[1] in ("modeling", "texturing", "rigging-animation")]

    lines = [
        f"# Wiki audit — {today}",
        "",
        "**Status:** Local fallback (run with Kimi for deeper review)",
        "",
        "## Summary",
        "",
        f"- **Pages in docs/:** {len(pages)}",
        f"- **MkDocs link warnings:** {len(warnings)}",
        f"- **Pages flagged:** {len(thin)}",
        f"- **Subject pages without images:** {len(no_img)}",
        "",
    ]

    if warnings:
        lines.extend(["## Broken internal links (fix these)", ""])
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")

    if thin:
        lines.extend(["## Pages needing content", ""])
        for p in thin[:25]:
            issues = "; ".join(p.get("issues", []))
            lines.append(f"- `{p['path']}` — {issues}")
        lines.append("")

    lines.extend(
        [
            "## Kimi commands",
            "",
            "- `python -m librarian.cli wiki-audit` — full AI review",
            "- `python -m librarian.cli wiki-images` — refresh card logos",
            "- `python -m librarian.cli breedables-research` — update inventory",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def wiki_audit_kimi(context: dict[str, Any], *, repo_root: Path | None = None) -> tuple[str, str]:
    today = date.today().isoformat()
    system = f"""You are the **whole-wiki editor** for Breedables Lab.

Mission:
{WIKI_MISSION.strip()}

You audit ALL MkDocs pages under docs/ — not just breedables research.

Output markdown with exactly these sections:
## Executive summary
## Wiki setup health (nav, hub, images, search UX)
## Broken or stale documentation (file path + fix)
## Academy gaps (lessons/labs missing Watch/Read/Do)
## Image gaps (slug + suggested source)
## Top 5 fixes for today (human / AI / automated)
## Optional: breedables research angle

Rules:
- Name specific file paths (docs/…)
- Prioritize broken MkDocs links and outdated instructions (wrong ports, removed tools like Wails)
- Reference wiki-design-benchmarks patterns (Outlands hub, card grids, sticky nav)
- Do not invent URLs
- Plain English for learners in suggested copy
"""
    bundle = {
        "date": today,
        "nav_sections": list(MKDOCS_NAV_SECTIONS),
        "mkdocs_warnings": context.get("mkdocs_warnings"),
        "wiki_pages": context.get("wiki_pages"),
        "pages_with_issues": [p for p in context.get("wiki_pages", []) if p.get("issues")],
        "doc_snippets": context.get("doc_snippets"),
        "daily_gaps": context.get("daily_report", {}).get("academy_gaps"),
        "design_benchmarks_excerpt": context.get("doc_snippets", {}).get("docs/meta/wiki-style-guide.md", "")[:3000],
    }
    user = (
        "Audit the entire wiki setup and content. Propose concrete fixes.\n\n"
        f"```json\n{json.dumps(bundle, indent=2)[:95000]}\n```"
    )
    return _kimi_complete(
        system=system,
        user=user,
        timeout=300.0,
        max_tokens=12000,
        cwd=repo_root,
    )


def build_wiki_audit_context(repo_root: Path, daily_payload: dict | None = None) -> dict[str, Any]:
    from .wiki_context import CONTEXT_FILES, _read_snippet

    repo_root = repo_root.resolve()
    snippets = {rel: _read_snippet(repo_root, rel, max_chars=2500) for rel in CONTEXT_FILES}
    snippets["docs/meta/wiki-style-guide.md"] = _read_snippet(
        repo_root, "docs/meta/wiki-style-guide.md", max_chars=2500
    )
    snippets["docs/meta/system-build-summary.md"] = _read_snippet(
        repo_root, "docs/meta/system-build-summary.md", max_chars=2500
    )
    return {
        "daily_report": daily_payload or {},
        "wiki_pages": inventory_wiki_pages(repo_root),
        "mkdocs_warnings": mkdocs_build_warnings(repo_root),
        "doc_snippets": snippets,
    }


def write_wiki_audit(
    out_path: Path,
    *,
    context: dict[str, Any],
    use_kimi: bool = True,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    source = "local"
    if use_kimi and resolve_kimi_backend() != "off":
        try:
            text, source = wiki_audit_kimi(context, repo_root=repo_root)
        except (
            KimiUnavailableError,
            RuntimeError,
            json.JSONDecodeError,
            KeyError,
            IndexError,
        ) as exc:
            text = wiki_audit_local(context)
            source = f"local (kimi failed: {exc})"
    else:
        text = wiki_audit_local(context)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return {"ok": True, "source": source, "path": str(out_path)}

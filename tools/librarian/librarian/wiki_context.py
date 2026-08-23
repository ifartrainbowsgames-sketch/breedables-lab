"""Collect wiki mission + structure for Kimi evolution briefings."""

from __future__ import annotations

from pathlib import Path

from .academy_manifest import BLENDER_LESSONS, TRACKS
from .db import LibrarianDB

WIKI_MISSION = """
Breedables Lab has TWO equally important outputs:

1. Build a real Second Life breedables production pipeline (Reference Creature).
2. Build a professional 3D/creature Academy that answers:
   "How do professional artists work, what software do they use, what is free,
   and where do I learn the entire workflow?"

Academy rules:
- Mirror REAL professional pipelines (Gnomon-style: Maya/ZBrush/Substance + free OSS route via Blender).
- Three routes per stage: Professional / Free-OSS / Breedables recommended.
- Every software page needs verified training URLs, exercises, artifacts, PASS/FAIL — not vague advice.
- Teach correct general 3D FIRST, then Second Life adaptation.
- Use existing Librarian/daily-wiki/webscreen/Kimi to POPULATE pages — no new meta-frameworks.
- Reference Creature experiments update the Academy with evidence.

Key docs: docs/academy/mission.md, professional-workflow/, software/packages/, start-here.md
"""

CONTEXT_FILES: tuple[str, ...] = (
    "docs/index.md",
    "docs/academy/mission.md",
    "docs/academy/start-here.md",
    "docs/academy/overview.md",
    "docs/academy/professional-workflow/index.md",
    "docs/academy/professional-workflow/software-map.md",
    "docs/studio/wiki-design-benchmarks.md",
    "docs/studio/system-build-summary.md",
    "docs/research/wiki-concept-audit.md",
)


def _read_snippet(repo_root: Path, rel: str, max_chars: int = 4000) -> str:
    path = repo_root / rel
    if not path.is_file():
        return f"(missing: {rel})"
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text) > max_chars:
        return text[:max_chars] + "\n\n…(truncated)…"
    return text


def build_wiki_context(
    repo_root: Path,
    db: LibrarianDB,
    daily_payload: dict,
) -> dict:
    repo_root = repo_root.resolve()
    tools = [
        {
            "name": r.name,
            "status": r.status,
            "commercial_type": r.commercial_type,
            "code_license": r.code_license or r.github_license,
            "url": r.canonical_url,
        }
        for r in db.list(limit=50)
    ]
    lessons = [
        {
            "number": L.number,
            "title": L.title,
            "path": L.lesson_wiki_path,
            "evidence": L.evidence_path,
        }
        for L in BLENDER_LESSONS
    ]
    labs = [
        {
            "title": t.title,
            "stage": t.production_stage,
            "path": t.lesson_wiki_path,
            "evidence": t.evidence_path,
        }
        for t in TRACKS
    ]
    doc_snippets = {rel: _read_snippet(repo_root, rel) for rel in CONTEXT_FILES}
    from .wiki_audit import inventory_wiki_pages, mkdocs_build_warnings

    return {
        "mission": WIKI_MISSION.strip(),
        "blender_lessons": lessons,
        "studio_labs": labs,
        "registry_tools": tools,
        "daily_report": daily_payload,
        "doc_snippets": doc_snippets,
        "wiki_pages": inventory_wiki_pages(repo_root),
        "mkdocs_warnings": mkdocs_build_warnings(repo_root),
    }

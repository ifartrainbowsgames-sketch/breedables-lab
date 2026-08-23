from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AcademyTrack:
    id: str
    title: str
    lesson_wiki_path: str
    evidence_path: str
    production_stage: str


TRACKS: tuple[AcademyTrack, ...] = (
    AcademyTrack(
        id="A01",
        title="Organic PBR Material",
        lesson_wiki_path="docs/academy/tracks/a01-organic-pbr.md",
        evidence_path="training/texturing/a01/",
        production_stage="Texturing & PBR",
    ),
    AcademyTrack(
        id="A02",
        title="Layered Texture Refinement",
        lesson_wiki_path="docs/academy/tracks/a02-layered-textures.md",
        evidence_path="training/texturing/a02/",
        production_stage="Texturing",
    ),
    AcademyTrack(
        id="A03",
        title="Organic Retopology",
        lesson_wiki_path="docs/academy/tracks/a03-retopology.md",
        evidence_path="training/modeling/a03/",
        production_stage="Retopology",
    ),
    AcademyTrack(
        id="A04",
        title="Rig + Two Animations",
        lesson_wiki_path="docs/academy/tracks/a04-rig-animation.md",
        evidence_path="training/rigging/a04/",
        production_stage="Rigging & animation",
    ),
    AcademyTrack(
        id="A05",
        title="SL Creature Fixture",
        lesson_wiki_path="docs/academy/tracks/a05-sl-fixture.md",
        evidence_path="training/lsl/a05/",
        production_stage="LSL & in-world test",
    ),
)

WIKI_INDEX_FILES: tuple[str, ...] = (
    "docs/academy/resources/videos.md",
    "docs/academy/resources/official-docs.md",
)


def academy_content_gaps(repo_root: Path) -> list[dict]:
    gaps: list[dict] = []
    root = repo_root.resolve()

    for rel in WIKI_INDEX_FILES:
        path = root / rel
        issues = []
        if not path.is_file():
            issues.append(f"missing wiki file: {rel}")
        elif path.stat().st_size < 200:
            issues.append(f"wiki file too thin: {rel}")
        if issues:
            gaps.append({"kind": "wiki", "id": rel, "name": rel, "issues": issues})

    for track in TRACKS:
        issues = []
        lesson = root / track.lesson_wiki_path
        evidence = root / track.evidence_path
        if not lesson.is_file():
            issues.append(f"missing lesson: {track.lesson_wiki_path}")
        elif lesson.stat().st_size < 500:
            issues.append(f"lesson incomplete: {track.lesson_wiki_path}")
        if not evidence.is_dir():
            issues.append(f"missing evidence folder: {track.evidence_path}")
        else:
            has_files = any(evidence.iterdir())
            if not has_files:
                issues.append(f"evidence folder empty: {track.evidence_path}")
        if issues:
            gaps.append(
                {
                    "kind": "academy_track",
                    "id": track.id,
                    "name": track.title,
                    "issues": issues,
                }
            )
    return gaps

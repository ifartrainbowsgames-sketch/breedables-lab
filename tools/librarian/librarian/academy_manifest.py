from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BlenderLesson:
    id: str
    number: int
    title: str
    lesson_wiki_path: str
    evidence_path: str


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


BLENDER_LESSONS: tuple[BlenderLesson, ...] = (
    BlenderLesson("B01", 1, "Install & setup", "docs/academy/software/blender/b01-install-setup.md", "training/blender/b01/"),
    BlenderLesson("B02", 2, "Interface & navigation", "docs/academy/software/blender/b02-interface-navigation.md", "training/blender/b02/"),
    BlenderLesson("B03", 3, "Mesh modeling", "docs/academy/software/blender/b03-mesh-modeling.md", "training/blender/b03/"),
    BlenderLesson("B04", 4, "Sculpting basics", "docs/academy/software/blender/b04-sculpting.md", "training/blender/b04/"),
    BlenderLesson("B05", 5, "Retopology", "docs/academy/software/blender/b05-retopology.md", "training/blender/b05/"),
    BlenderLesson("B06", 6, "UV unwrapping", "docs/academy/software/blender/b06-uv-unwrapping.md", "training/blender/b06/"),
    BlenderLesson("B07", 7, "Texture painting & PBR", "docs/academy/software/blender/b07-texture-painting-pbr.md", "training/blender/b07/"),
    BlenderLesson("B08", 8, "Rigging & weight painting", "docs/academy/software/blender/b08-rigging-weight-painting.md", "training/blender/b08/"),
    BlenderLesson("B09", 9, "Basic animation", "docs/academy/software/blender/b09-animation.md", "training/blender/b09/"),
    BlenderLesson("B10", 10, "Export to Second Life", "docs/academy/software/blender/b10-export-to-sl.md", "training/blender/b10/"),
)

WIKI_INDEX_FILES: tuple[str, ...] = (
    "docs/academy/resources/videos.md",
    "docs/academy/resources/official-docs.md",
)


def code_glossary() -> dict[str, str]:
    """Internal id → plain English (for reports and Kimi prompts)."""
    out: dict[str, str] = {}
    for lesson in BLENDER_LESSONS:
        out[lesson.id] = f"Blender lesson {lesson.number} ({lesson.title})"
    for track in TRACKS:
        out[track.id] = track.title
    out["A-model"] = "Modeling stage (general)"
    return out


def humanize_codes(text: str) -> str:
    """Replace B01/A01-style codes with plain names in free text."""
    result = text
    # Longer ids first so B10 replaces before B1 substring issues.
    for code, label in sorted(code_glossary().items(), key=lambda x: -len(x[0])):
        result = result.replace(code, label)
    return result


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

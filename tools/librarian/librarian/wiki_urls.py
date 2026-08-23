from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

# Markdown links and bare https URLs
_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
_BARE_RE = re.compile(r"(?<![(\[])(https?://[^\s<>\"')]+)")


@dataclass(frozen=True)
class WikiLink:
    url: str
    source: str  # relative path from repo root


# Pages that carry curated external URLs. Tutorial and video links now live on
# the subject page that owns the topic, so these are the section entry points
# plus the two cross-cutting indexes.
DEFAULT_WIKI_SOURCES: tuple[str, ...] = (
    "docs/research/software-database.md",
    "docs/academy/complete-courses.md",
    "docs/modeling/index.md",
    "docs/modeling/mesh-modeling.md",
    "docs/modeling/sculpting.md",
    "docs/modeling/retopology.md",
    "docs/modeling/uv-mapping.md",
    "docs/texturing/index.md",
    "docs/texturing/pbr-materials.md",
    "docs/rigging-animation/index.md",
    "docs/rigging-animation/rigging-and-skinning.md",
    "docs/rigging-animation/animation.md",
    "docs/second-life/index.md",
    "docs/second-life/export-and-upload.md",
    "docs/second-life/platform-baseline.md",
    "docs/engineering/index.md",
    "docs/pipeline.md",
    "docs/index.md",
)


def _package_card_sources(repo_root: Path) -> list[str]:
    """Software cards, which now live under each subject section."""
    out: list[str] = []
    for section in ("modeling", "texturing", "second-life"):
        pkg_dir = repo_root / "docs" / section / "software"
        if not pkg_dir.is_dir():
            continue
        out += [
            p.relative_to(repo_root).as_posix()
            for p in pkg_dir.glob("*.md")
            if p.name != "index.md"
        ]
    blender = repo_root / "docs" / "modeling" / "blender" / "index.md"
    if blender.is_file():
        out.append(blender.relative_to(repo_root).as_posix())
    return sorted(out)


def extract_links(text: str, source: str) -> list[WikiLink]:
    seen: set[str] = set()
    out: list[WikiLink] = []
    for pattern in (_LINK_RE, _BARE_RE):
        for match in pattern.finditer(text):
            url = match.group(1).rstrip(".,;")
            if url in seen:
                continue
            seen.add(url)
            out.append(WikiLink(url=url, source=source))
    return out


def collect_wiki_links(repo_root: Path, sources: tuple[str, ...] | None = None) -> list[WikiLink]:
    if sources is None:
        paths = list(DEFAULT_WIKI_SOURCES) + _package_card_sources(repo_root)
    else:
        paths = list(sources)
    links: list[WikiLink] = []
    seen: set[str] = set()
    for rel in paths:
        path = repo_root / rel
        if not path.is_file():
            continue
        for item in extract_links(path.read_text(encoding="utf-8"), rel):
            if item.url in seen:
                continue
            seen.add(item.url)
            links.append(item)
    return links

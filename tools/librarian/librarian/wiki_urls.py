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


DEFAULT_WIKI_SOURCES: tuple[str, ...] = (
    "docs/academy/resources/tutorials.md",
    "docs/academy/resources/training-videos-by-stage.md",
    "docs/academy/resources/complete-courses.md",
    "docs/academy/resources/videos.md",
    "docs/academy/resources/official-docs.md",
    "docs/academy/start-here.md",
    "docs/academy/overview.md",
    "docs/index.md",
)


def _package_card_sources(repo_root: Path) -> list[str]:
    pkg_dir = repo_root / "docs" / "academy" / "software" / "packages"
    if not pkg_dir.is_dir():
        return []
    return sorted(
        str(p.relative_to(repo_root)).replace("\\", "/")
        for p in pkg_dir.glob("*.md")
        if p.name != "index.md"
    )


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

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VIDEO_INDEX = Path("docs/academy/resources/videos.md")
TUTORIAL_ARSENAL = Path("docs/academy/resources/tutorials.md")

_TABLE_SEP = re.compile(r"^[\s|:-]+$")
_URL = re.compile(r"https?://[^\s)>\]]+")


def parse_video_index(path: Path) -> list[dict[str, str]]:
    """Return curated rows from the Academy video library (skip TBD placeholders)."""
    if not path.is_file():
        return []

    videos: list[dict[str, str]] = []
    section = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if not line.startswith("|"):
            continue
        cols = [col.strip() for col in line.strip("|").split("|")]
        if len(cols) < 2:
            continue
        title, url = cols[0], cols[1]
        if title.casefold() == "title" or _TABLE_SEP.match(title) or _TABLE_SEP.match(url):
            continue
        if not url.startswith("http"):
            continue
        videos.append({"title": title.strip("* "), "url": url, "section": section})
    return videos


def count_arsenal_links(path: Path) -> int:
    if not path.is_file():
        return 0
    return len({match.group(0).rstrip(".,);") for match in _URL.finditer(path.read_text(encoding="utf-8"))})


def inventory_wiki_videos(repo_root: Path, *, no_kimi: bool = False) -> dict:
    root = repo_root.resolve()
    videos = parse_video_index(root / VIDEO_INDEX)
    payload = {
        "total": len(videos),
        "video_library": str(VIDEO_INDEX),
        "videos": videos,
        "arsenal_links": count_arsenal_links(root / TUTORIAL_ARSENAL),
        "kimi": "skipped" if no_kimi else "not_configured",
    }
    if not no_kimi:
        payload["kimi_note"] = (
            "Kimi enrichment is not configured in V1. "
            "Pass --no-kimi to inventory the wiki index only."
        )
    return payload


def breedwiki_reply(
    wiki_base_url: str,
    *,
    query: str = "",
    inventory: dict | None = None,
) -> str:
    base = wiki_base_url.rstrip("/")
    library = f"{base}/academy/resources/videos/"
    lines = [
        "*Breedables Academy video library*",
        library,
    ]
    if inventory is not None:
        lines.append(f"Curated videos: {inventory['total']}")
        videos = inventory.get("videos") or []
        needle = query.casefold().strip()
        matches = [
            item
            for item in videos
            if not needle
            or needle in item["title"].casefold()
            or needle in item.get("section", "").casefold()
        ]
        if needle and not matches:
            lines.append(f"No curated video matched `{query}`.")
        elif needle:
            for item in matches[:5]:
                lines.append(f"• {item['title']}: {item['url']}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wiki-videos",
        description="Inventory curated Academy wiki videos.",
    )
    parser.add_argument(
        "--no-kimi",
        action="store_true",
        help="Skip Kimi enrichment and count wiki-index videos only.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        help="Repository root (defaults to BREEDABLES_REPO_ROOT / mkdocs root).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    from .config import Settings

    args = build_parser().parse_args(argv)
    settings = Settings.from_env()
    repo_root = args.repo_root or settings.repo_root
    payload = inventory_wiki_videos(repo_root, no_kimi=args.no_kimi)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

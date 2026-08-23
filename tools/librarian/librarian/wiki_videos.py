"""Build comprehensive video tutorial library with in-wiki YouTube embeds."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .kimi import KimiUnavailableError, _kimi_complete, _strip_markdown_fence, resolve_kimi_backend

VIDEO_LIBRARY_PATH = "docs/academy/resources/video-library.md"
VIDEO_MANIFEST_PATH = "docs/academy/resources/video-manifest.json"

# Kimi expands this list — every production software in the pipeline
SOFTWARE_VIDEO_TARGETS: list[dict[str, str]] = [
    {"slug": "blender", "title": "Blender", "category": "core"},
    {"slug": "maya", "title": "Autodesk Maya", "category": "modeling-rig"},
    {"slug": "zbrush", "title": "ZBrush", "category": "sculpt"},
    {"slug": "substance-painter", "title": "Substance 3D Painter", "category": "texture"},
    {"slug": "mari", "title": "Foundry Mari", "category": "texture"},
    {"slug": "material-maker", "title": "Material Maker", "category": "texture"},
    {"slug": "krita", "title": "Krita", "category": "2d"},
    {"slug": "photoshop", "title": "Adobe Photoshop", "category": "2d"},
    {"slug": "topogun", "title": "TopoGun", "category": "retopo"},
    {"slug": "marvelous-designer", "title": "Marvelous Designer", "category": "cloth"},
    {"slug": "marmoset-toolbag", "title": "Marmoset Toolbag", "category": "lookdev"},
    {"slug": "pureref", "title": "PureRef", "category": "reference"},
    {"slug": "second-life", "title": "Second Life creator", "category": "delivery"},
    {"slug": "hard-ops", "title": "Hard Ops / Boxcutter (Blender add-ons)", "category": "addon"},
    {"slug": "retopoflow", "title": "RetopoFlow (Blender add-on)", "category": "addon"},
    {"slug": "ucupaint", "title": "Ucupaint (Blender add-on)", "category": "addon"},
    {"slug": "avastar", "title": "Avastar (Second Life rigging)", "category": "addon"},
]


def youtube_id_from_url(url: str) -> str | None:
    url = url.strip()
    if "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0].split("&")[0]
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    if "embed/" in url:
        return url.split("embed/")[-1].split("?")[0]
    if "playlist?list=" in url:
        return None
    if re.fullmatch(r"[\w-]{11}", url):
        return url
    return None


def embed_block(youtube_id: str, title: str) -> str:
    safe = title.replace('"', "'")
    return (
        f'<div class="wiki-video" markdown="0">\n'
        f'<iframe src="https://www.youtube-nocookie.com/embed/{youtube_id}" '
        f'title="{safe}" loading="lazy" '
        f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
        f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>\n'
        f"</div>\n"
    )


def _parse_video_json(text: str) -> list[dict[str, Any]]:
    stripped = _strip_markdown_fence(text).strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", stripped)
    if fence:
        stripped = fence.group(1).strip()
    if not stripped.startswith("["):
        start, end = stripped.find("["), stripped.rfind("]")
        if start >= 0 and end > start:
            stripped = stripped[start : end + 1]
    data = json.loads(stripped)
    if not isinstance(data, list):
        raise ValueError("expected JSON array")
    return data


def _normalize_video_entry(entry: dict[str, Any]) -> dict[str, Any]:
    slug = str(entry.get("software", "")).strip().lower().replace(" ", "-")
    aliases = {
        "autodesk-maya": "maya",
        "adobe-substance-3d-painter": "substance-painter",
        "substance-3d-painter": "substance-painter",
        "maxon-zbrush": "zbrush",
        "hard-ops-/-boxcutter-(blender-add-ons)": "hard-ops",
    }
    slug = aliases.get(slug, slug)
    entry = {**entry, "software": slug}
    if not entry.get("youtube_id") and entry.get("url"):
        yid = youtube_id_from_url(str(entry["url"]))
        if yid:
            entry["youtube_id"] = yid
    return entry


def discover_videos_kimi(
    *,
    repo_root: Path,
    targets: list[dict[str, str]] | None = None,
) -> tuple[list[dict[str, Any]], str]:
    """Discover videos one software at a time — avoids truncated JSON from huge responses."""
    items = targets or SOFTWARE_VIDEO_TARGETS
    major = {"blender", "maya", "zbrush", "substance-painter"}
    system = """You are the video curator for Breedables Lab Academy — 3D production software for creature/game/SL workflows.

Output **only** a JSON array (no markdown prose). Each object:
{
  "software": "blender",
  "title": "Human-readable video title",
  "youtube_id": "11-char id OR null if playlist/channel only",
  "url": "full https://youtube.com/... or official course URL",
  "stage": "modeling|sculpt|retopo|uv|texture|rig|anim|lookdev|sl|reference",
  "level": "beginner|intermediate|advanced",
  "why": "one sentence"
}

Rules:
- Prefer stable tutorials: Blender Official, Grant Abbitt, FlippedNormals, Adobe, Autodesk, Maxon, Marmoset, Foundry
- youtube_id required when url is a single video; null ok for playlists/channels
- Do not invent video IDs — real videos only
- Use the exact software slug from the request in every object
"""
    all_videos: list[dict[str, Any]] = []
    source = "kimi-cli"
    errors: list[str] = []

    for target in items:
        slug = target["slug"]
        count = 12 if slug in major else 6
        user = (
            f"Build **{count}** video entries for this software only:\n\n"
            f"```json\n{json.dumps([target], indent=2)}\n```"
        )
        try:
            text, batch_source = _kimi_complete(
                system=system,
                user=user,
                timeout=180.0,
                max_tokens=8000,
                cwd=repo_root,
            )
            source = batch_source
            batch = [_normalize_video_entry(v) for v in _parse_video_json(text)]
            all_videos.extend(batch)
        except (
            KimiUnavailableError,
            RuntimeError,
            json.JSONDecodeError,
            ValueError,
            KeyError,
        ) as exc:
            errors.append(f"{slug}: {exc}")

    if not all_videos and errors:
        raise ValueError("; ".join(errors))
    if errors:
        source = f"{source} ({len(errors)} batch failures)"
    return all_videos, source


def seed_videos_local() -> list[dict[str, Any]]:
    """Curated seed from verified wiki links — used when Kimi unavailable or to merge."""
    seed_path = Path(__file__).resolve().parent / "data" / "video-seed.json"
    if seed_path.is_file():
        try:
            data = json.loads(seed_path.read_text(encoding="utf-8"))
            if isinstance(data, list) and data:
                return data
        except (json.JSONDecodeError, OSError):
            pass
    return [
        {"software": "pureref", "title": "PureRef intro workflow", "youtube_id": "9YQTXN9nT0E", "url": "https://www.youtube.com/watch?v=9YQTXN9nT0E", "stage": "reference", "level": "beginner", "why": "Reference board setup"},
        {"software": "blender", "title": "Blender Guru — Donut (modeling)", "youtube_id": "nIoXOplUvAw", "url": "https://www.youtube.com/watch?v=nIoXOplUvAw", "stage": "modeling", "level": "beginner", "why": "Canonical beginner modeling"},
        {"software": "blender", "title": "Grant Abbitt — low-poly creatures", "youtube_id": None, "url": "https://www.youtube.com/@grabbitt", "stage": "modeling", "level": "beginner", "why": "Creature base meshes"},
        {"software": "blender", "title": "Royal Skies — retopology beginner", "youtube_id": "h6E9N10rN5s", "url": "https://www.youtube.com/watch?v=h6E9N10rN5s", "stage": "retopo", "level": "beginner", "why": "Manual retopo over sculpt"},
        {"software": "blender", "title": "Blender Official — UV basics", "youtube_id": "mLuhL_vgGUE", "url": "https://www.youtube.com/watch?v=mLuhL_vgGUE", "stage": "uv", "level": "beginner", "why": "UV unwrapping fundamentals"},
        {"software": "blender", "title": "Ryan King Art — PBR texturing", "youtube_id": "4_xYiw1nL5M", "url": "https://www.youtube.com/watch?v=4_xYiw1nL5M", "stage": "texture", "level": "intermediate", "why": "Metallic/roughness workflow"},
        {"software": "blender", "title": "Darkfall — quadruped rigging intro", "youtube_id": "6Km2tRFTxvs", "url": "https://www.youtube.com/watch?v=6Km2tRFTxvs", "stage": "rig", "level": "intermediate", "why": "Creature rigging"},
        {"software": "maya", "title": "Autodesk Maya Quick Start", "youtube_id": None, "url": "https://www.autodesk.com/learn/ondemand/collection/maya-quick-start", "stage": "modeling", "level": "beginner", "why": "Official Maya onboarding"},
        {"software": "maya", "title": "FlippedNormals — Quad Draw retopo", "youtube_id": "7T_yQ62jMTY", "url": "https://www.youtube.com/watch?v=7T_yQ62jMTY", "stage": "retopo", "level": "intermediate", "why": "Industry retopo tool"},
        {"software": "zbrush", "title": "FlippedNormals — creature head sculpt", "youtube_id": "UdT6ekB_IAE", "url": "https://www.youtube.com/watch?v=UdT6ekB_IAE", "stage": "sculpt", "level": "intermediate", "why": "ZBrush creature workflow"},
        {"software": "zbrush", "title": "Maxon ZClassroom", "youtube_id": None, "url": "https://www.maxon.net/en/zbrush/zclassroom", "stage": "sculpt", "level": "beginner", "why": "Official ZBrush training"},
        {"software": "substance-painter", "title": "Adobe Substance tutorials hub", "youtube_id": None, "url": "https://helpx.adobe.com/substance-3d-tutorials.html", "stage": "texture", "level": "beginner", "why": "Official texture authoring"},
        {"software": "substance-painter", "title": "Creature skin texturing", "youtube_id": "0yOKG8G2ae8", "url": "https://www.youtube.com/watch?v=0yOKG8G2ae8", "stage": "texture", "level": "intermediate", "why": "Painter creature workflow"},
        {"software": "material-maker", "title": "Material Maker intro", "youtube_id": "8MMSS2F5vtc", "url": "https://www.youtube.com/watch?v=8MMSS2F5vtc", "stage": "texture", "level": "beginner", "why": "OSS procedural PBR"},
        {"software": "mari", "title": "Foundry Mari learn hub", "youtube_id": None, "url": "https://www.foundry.com/products/mari/learn", "stage": "texture", "level": "intermediate", "why": "Film/VFX texture painting"},
        {"software": "krita", "title": "Krita hand-painted textures", "youtube_id": "1v24b1nNBJE", "url": "https://www.youtube.com/watch?v=1v24b1nNBJE", "stage": "texture", "level": "beginner", "why": "Free 2D paint finish"},
        {"software": "topogun", "title": "TopoGun 3 workflow", "youtube_id": "wg8S4n5lGQ8", "url": "https://www.youtube.com/watch?v=wg8S4n5lGQ8", "stage": "retopo", "level": "intermediate", "why": "Standalone retopo"},
        {"software": "marvelous-designer", "title": "Marvelous Designer official channel", "youtube_id": None, "url": "https://www.youtube.com/user/MarvelousDesigner", "stage": "cloth", "level": "beginner", "why": "Cloth simulation"},
        {"software": "marmoset-toolbag", "title": "Baking props in Toolbag", "youtube_id": None, "url": "https://marmoset.co/posts/baking-props-in-marmoset-toolbag/", "stage": "lookdev", "level": "intermediate", "why": "Bake + lookdev"},
        {"software": "second-life", "title": "Gaia Clift — mesh upload", "youtube_id": "uZ5KyLvivkw", "url": "https://www.youtube.com/watch?v=uZ5KyLvivkw", "stage": "sl", "level": "beginner", "why": "SL upload walkthrough"},
        {"software": "retopoflow", "title": "CG Cookie — RetopoFlow", "youtube_id": None, "url": "https://www.youtube.com/cgcookie", "stage": "retopo", "level": "intermediate", "why": "Blender retopo add-on"},
    ]


def merge_videos(*lists: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str]] = set()
    out: list[dict[str, Any]] = []
    for lst in lists:
        for v in lst:
            key = (v.get("software", ""), v.get("url") or v.get("youtube_id") or v.get("title", ""))
            if key in seen:
                continue
            seen.add(key)
            if not v.get("youtube_id") and v.get("url"):
                v = {**v, "youtube_id": youtube_id_from_url(str(v["url"]))}
            v = _normalize_video_entry(v)
            out.append(v)
    return out


def render_video_library(videos: list[dict[str, Any]]) -> str:
    from datetime import date

    by_soft: dict[str, list[dict[str, Any]]] = {}
    for v in videos:
        by_soft.setdefault(str(v.get("software", "other")), []).append(v)

    slug_titles = {t["slug"]: t["title"] for t in SOFTWARE_VIDEO_TARGETS}
    order = [t["slug"] for t in SOFTWARE_VIDEO_TARGETS] + sorted(
        s for s in by_soft if s not in {t["slug"] for t in SOFTWARE_VIDEO_TARGETS}
    )

    lines = [
        "# Video library — watch in the wiki",
        "",
        f"**Updated:** {date.today().isoformat()} · **Videos:** {len(videos)}",
        "",
        "Press **play** below or open the YouTube link. Covers **all pipeline software** — not just Blender.",
        "",
        "Also see: [Training videos by stage](training-videos-by-stage.md) · [Tutorial arsenal](tutorials.md) · [Software packages](../software/packages/index.md)",
        "",
        "!!! tip \"How to add more\"",
        "    Run `python -m librarian.cli wiki-videos` (Kimi expands this page). "
        "    Or add rows to [training-videos-by-stage.md](training-videos-by-stage.md).",
        "",
    ]

    for slug in order:
        entries = by_soft.get(slug, [])
        if not entries:
            continue
        title = slug_titles.get(slug, slug.replace("-", " ").title())
        lines.extend([f"## {title} {{#{slug}}}", ""])
        by_level: dict[str, list] = {"beginner": [], "intermediate": [], "advanced": [], "other": []}
        for e in entries:
            lvl = str(e.get("level", "other")).lower()
            by_level.get(lvl, by_level["other"]).append(e)

        for lvl in ("beginner", "intermediate", "advanced", "other"):
            batch = by_level[lvl]
            if not batch:
                continue
            if lvl != "other":
                # Bold label, not a heading: these repeat under every software
                # section, and as headings they flood the page table of contents.
                lines.append(f"**{lvl.capitalize()}**")
                lines.append("")
            for v in batch:
                vid_title = v.get("title", "Video")
                yid = v.get("youtube_id")
                url = v.get("url", "")
                why = v.get("why", "")
                if yid:
                    lines.append(embed_block(str(yid), str(vid_title)))
                lines.append(f"**[{vid_title}]({url})** — {why}")
                lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Regenerate with Kimi")
    lines.append("")
    lines.append("```powershell")
    lines.append("cd tools/librarian")
    lines.append("python -m librarian.cli wiki-videos")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def load_video_manifest(repo_root: Path) -> list[dict[str, Any]]:
    path = repo_root / VIDEO_MANIFEST_PATH
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_video_manifest(repo_root: Path, videos: list[dict[str, Any]]) -> None:
    path = repo_root / VIDEO_MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(videos, indent=2), encoding="utf-8")


def write_wiki_videos(
    repo_root: Path,
    *,
    use_kimi: bool = True,
    merge_seed: bool = True,
) -> dict[str, Any]:
    source = "local"
    cached = load_video_manifest(repo_root)
    videos: list[dict[str, Any]] = merge_videos(seed_videos_local(), cached) if merge_seed else list(cached)

    if use_kimi and resolve_kimi_backend() != "off":
        try:
            kimi_videos, source = discover_videos_kimi(repo_root=repo_root)
            videos = merge_videos(videos, kimi_videos) if merge_seed else kimi_videos
        except (
            KimiUnavailableError,
            RuntimeError,
            json.JSONDecodeError,
            ValueError,
            KeyError,
        ) as exc:
            if not videos:
                videos = seed_videos_local()
            source = f"local (kimi failed: {exc})"
            if cached:
                source = f"manifest (kimi failed: {exc})"
    elif not videos:
        videos = seed_videos_local()

    md = render_video_library(videos)
    out = repo_root / VIDEO_LIBRARY_PATH
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    save_video_manifest(repo_root, videos)

    embed_count = sum(1 for v in videos if v.get("youtube_id"))
    return {
        "ok": True,
        "source": source,
        "path": str(out),
        "total": len(videos),
        "embeddable": embed_count,
    }

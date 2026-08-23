"""Discover, download, and optimize wiki card/inline images via Kimi."""

from __future__ import annotations

import io
import json
import re
import time
from pathlib import Path
from typing import Any

import httpx

from .kimi import KimiUnavailableError, _kimi_complete, resolve_kimi_backend

MANIFEST_PATH = "docs/assets/manifest.json"
CARD_SIZE = 200
INLINE_MAX = 400
PAD = 18
BG = (42, 42, 46)

# Slugs map to docs/assets/cards/{slug}.png and inline/{slug}.png
IMAGE_TARGETS: list[dict[str, str]] = [
    {"slug": "blender", "title": "Blender", "category": "software"},
    {"slug": "maya", "title": "Autodesk Maya", "category": "software"},
    {"slug": "zbrush", "title": "ZBrush", "category": "software"},
    {"slug": "substance-painter", "title": "Adobe Substance 3D Painter", "category": "software"},
    {"slug": "krita", "title": "Krita", "category": "software"},
    {"slug": "photoshop", "title": "Adobe Photoshop", "category": "software"},
    {"slug": "material-maker", "title": "Material Maker", "category": "software"},
    {"slug": "second-life", "title": "Second Life", "category": "software"},
    {"slug": "marvelous-designer", "title": "Marvelous Designer", "category": "software"},
    {"slug": "mari", "title": "Foundry Mari", "category": "software"},
    {"slug": "topogun", "title": "TopoGun", "category": "software"},
    {"slug": "pureref", "title": "PureRef", "category": "software"},
    {"slug": "marmoset-toolbag", "title": "Marmoset Toolbag", "category": "software"},
    {"slug": "start-here", "title": "Academy start here", "category": "hub"},
    {"slug": "breedables-research", "title": "Breedables research hub", "category": "hub"},
    {"slug": "workflow", "title": "Professional workflow", "category": "hub"},
    {"slug": "studio-labs", "title": "Studio labs", "category": "hub"},
    {"slug": "tutorials", "title": "Tutorial arsenal", "category": "hub"},
    {"slug": "kittycats", "title": "KittyCats (SL breedables)", "category": "breedables"},
    {"slug": "meeroos", "title": "Meeroos (SL breedables)", "category": "breedables"},
    {"slug": "abc-horses", "title": "ABC Awesome Breed Creation horses", "category": "breedables"},
]

HUB_ALIASES: dict[str, str] = {
    "start-here": "pureref",
    "breedables-research": "second-life",
    "addons": "blender",
    "production-line": "marvelous-designer",
    "workflow": "maya",
    "blender-path": "blender",
    "studio-labs": "zbrush",
    "tutorials": "krita",
    "tools-registry": "material-maker",
    "software-packages": "substance-painter",
    "second-life": "second-life",
    "blender": "blender",
}


def _parse_json_array(text: str) -> list[dict[str, Any]]:
    stripped = text.strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", stripped)
    if fence:
        stripped = fence.group(1).strip()
    if not stripped.startswith("["):
        start = stripped.find("[")
        end = stripped.rfind("]")
        if start >= 0 and end > start:
            stripped = stripped[start : end + 1]
    data = json.loads(stripped)
    if not isinstance(data, list):
        raise ValueError("expected JSON array")
    return data


def discover_images_kimi(
    *,
    repo_root: Path,
    targets: list[dict[str, str]] | None = None,
) -> tuple[list[dict[str, Any]], str]:
    """Ask Kimi for direct HTTPS image URLs (logos, official art, Wikimedia thumbs)."""
    items = targets or IMAGE_TARGETS
    system = """You are the visual editor for Breedables Lab wiki (Second Life breedables Academy).

Find **direct HTTPS image URLs** for wiki card thumbnails. Prefer in order:
1. Google favicon CDN: `https://www.google.com/s2/favicons?domain=DOMAIN&sz=128` (most reliable for software)
2. GitHub avatars for OSS projects (material-maker)
3. Official vendor PNG/JPG logos on vendor CDNs (not Wikimedia — bot-blocked)
4. For breedables: official marketplace/blog header images ONLY if clearly public promotional art

Output **only** a JSON array (no markdown prose). Each object:
{"slug": "...", "url": "https://...", "license": "...", "alt": "..."}

Rules:
- url must be https and end in .png, .jpg, .jpeg, .webp, or .gif OR be a known CDN thumb URL
- Do not invent URLs — use real links you are confident exist
- license: e.g. "trademark/fair use logo", "CC BY-SA Wikimedia", "official promo"
- If unsure, omit that slug rather than guess
"""
    user = (
        "Find images for these wiki targets:\n\n"
        f"```json\n{json.dumps(items, indent=2)}\n```"
    )
    text, source = _kimi_complete(
        system=system,
        user=user,
        timeout=240.0,
        max_tokens=8000,
        cwd=repo_root,
    )
    return _parse_json_array(text), source


def discover_images_local(targets: list[dict[str, str]] | None = None) -> list[dict[str, Any]]:
    """Fallback: Google favicon CDN for software slugs."""
    favicon_domains = {
        "blender": "blender.org",
        "maya": "autodesk.com",
        "zbrush": "maxon.net",
        "substance-painter": "adobe.com",
        "krita": "krita.org",
        "photoshop": "adobe.com",
        "material-maker": "github.com",
        "second-life": "secondlife.com",
        "marvelous-designer": "marvelousdesigner.com",
        "mari": "foundry.com",
        "topogun": "topogun.com",
        "pureref": "pureref.com",
        "marmoset-toolbag": "marmoset.co",
        "kittycats": "kittycats.ws",
        "meeroos": "secondlife.com",
    }
    out: list[dict[str, Any]] = []
    for item in targets or IMAGE_TARGETS:
        slug = item["slug"]
        domain = favicon_domains.get(slug)
        if domain:
            out.append(
                {
                    "slug": slug,
                    "url": f"https://www.google.com/s2/favicons?domain={domain}&sz=128",
                    "license": "favicon/fair use",
                    "alt": item["title"],
                }
            )
    return out


def _fetch_image(url: str) -> tuple[bytes, str]:
    resp = httpx.get(
        url,
        headers={"User-Agent": "breedables-lab-wiki/1.0"},
        follow_redirects=True,
        timeout=45.0,
    )
    resp.raise_for_status()
    ctype = resp.headers.get("content-type", "image/png").split(";")[0].strip()
    return resp.content, ctype


def _ext_for(ctype: str, url: str) -> str:
    mapping = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/webp": ".webp",
        "image/gif": ".gif",
    }
    if ctype in mapping:
        return mapping[ctype]
    for ext in (".png", ".jpg", ".jpeg", ".webp", ".gif"):
        if url.lower().split("?")[0].endswith(ext):
            return ext if ext != ".jpeg" else ".jpg"
    return ".png"


def _optimize_bytes(raw: bytes, slug: str, cards_dir: Path, inline_dir: Path) -> dict[str, Any]:
    try:
        from PIL import Image, ImageOps
    except ImportError as exc:
        raise RuntimeError("Install Pillow: pip install Pillow") from exc

    im = Image.open(io.BytesIO(raw))
    im = ImageOps.exif_transpose(im)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGBA")

    def fit_card(image: Image.Image) -> Image.Image:
        inner = CARD_SIZE - PAD * 2
        img = image.copy()
        if img.mode == "RGBA":
            flat = Image.new("RGB", img.size, BG)
            flat.paste(img, mask=img.split()[3])
            img = flat
        else:
            img = img.convert("RGB")
        img.thumbnail((inner, inner), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (CARD_SIZE, CARD_SIZE), BG)
        ox = (CARD_SIZE - img.width) // 2
        oy = (CARD_SIZE - img.height) // 2
        canvas.paste(img, (ox, oy))
        return canvas

    def fit_inline(image: Image.Image) -> Image.Image:
        img = image.copy()
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, BG)
            bg.paste(img, mask=img.split()[3])
            img = bg
        else:
            img = img.convert("RGB")
        if img.width > INLINE_MAX:
            ratio = INLINE_MAX / img.width
            img = img.resize((INLINE_MAX, max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)
        return img

    card_path = cards_dir / f"{slug}.png"
    inline_path = inline_dir / f"{slug}.png"
    fit_card(im).save(card_path, format="PNG", optimize=True)
    fit_inline(im).save(inline_path, format="PNG", optimize=True)
    return {
        "card": str(card_path),
        "inline": str(inline_path),
        "card_kb": round(card_path.stat().st_size / 1024, 1),
        "inline_kb": round(inline_path.stat().st_size / 1024, 1),
    }


def apply_manifest(
    repo_root: Path,
    entries: list[dict[str, Any]],
    *,
    delay_s: float = 0.8,
) -> dict[str, Any]:
    """Download URLs from manifest entries and write optimized card/inline PNGs."""
    inbox = repo_root / "docs" / "assets" / "inbox"
    cards = repo_root / "docs" / "assets" / "cards"
    inline = repo_root / "docs" / "assets" / "inline"
    for d in (inbox, cards, inline):
        d.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    for entry in entries:
        slug = str(entry.get("slug", "")).strip()
        url = str(entry.get("url", "")).strip()
        if not slug or not url.startswith("https://"):
            results.append({"slug": slug, "ok": False, "error": "missing slug or https url"})
            continue
        try:
            raw, ctype = _fetch_image(url)
            ext = _ext_for(ctype, url)
            inbox_path = inbox / f"{slug}{ext}"
            inbox_path.write_bytes(raw)
            opt = _optimize_bytes(raw, slug, cards, inline)
            results.append({"slug": slug, "ok": True, "url": url, **opt})
            time.sleep(delay_s)
        except (httpx.HTTPError, OSError, ValueError) as exc:
            results.append({"slug": slug, "ok": False, "url": url, "error": str(exc)})

    ok = sum(1 for r in results if r.get("ok"))
    failed_slugs = {r["slug"] for r in results if not r.get("ok") and r.get("slug")}
    if failed_slugs:
        fallback = discover_images_local(
            [t for t in IMAGE_TARGETS if t["slug"] in failed_slugs]
        )
        for entry in fallback:
            slug = entry["slug"]
            if slug not in failed_slugs:
                continue
            url = str(entry.get("url", ""))
            try:
                raw, _ctype = _fetch_image(url)
                opt = _optimize_bytes(raw, slug, cards, inline)
                results.append({"slug": slug, "ok": True, "url": url, "fallback": True, **opt})
                failed_slugs.discard(slug)
                time.sleep(delay_s)
            except (httpx.HTTPError, OSError, ValueError):
                pass
        ok = sum(1 for r in results if r.get("ok"))

    for hub, source in HUB_ALIASES.items():
        src = cards / f"{source}.png"
        dst = cards / f"{hub}.png"
        if src.exists() and hub != source:
            dst.write_bytes(src.read_bytes())

    manifest_path = repo_root / MANIFEST_PATH
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "entries": entries,
        "results": results,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    return {"ok": True, "manifest": str(manifest_path), "downloaded": ok, "total": len(entries), "results": results}


def write_wiki_images(
    repo_root: Path,
    *,
    use_kimi: bool = True,
    targets: list[dict[str, str]] | None = None,
) -> dict[str, Any]:
    source = "local"
    entries: list[dict[str, Any]]

    if use_kimi and resolve_kimi_backend() != "off":
        try:
            entries, source = discover_images_kimi(repo_root=repo_root, targets=targets)
        except (
            httpx.HTTPError,
            KeyError,
            IndexError,
            RuntimeError,
            KimiUnavailableError,
            ValueError,
            json.JSONDecodeError,
        ) as exc:
            entries = discover_images_local(targets)
            source = f"local (kimi failed: {exc})"
    else:
        entries = discover_images_local(targets)

    apply_result = apply_manifest(repo_root, entries)
    return {"source": source, **apply_result}

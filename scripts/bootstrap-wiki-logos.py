#!/usr/bin/env python3
"""Download official logos and build wiki card + inline assets.

    python scripts/bootstrap-wiki-logos.py

Writes docs/assets/cards/*.png and docs/assets/inline/*.png
"""

from __future__ import annotations

import io
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Install Pillow: pip install Pillow", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "docs" / "assets" / "cards"
INLINE = ROOT / "docs" / "assets" / "inline"
CARD_SIZE = 200
INLINE_MAX = 400
PAD = 18
BG = (42, 42, 46)  # matches Material dark surface

def favicon(domain: str) -> str:
    return f"https://www.google.com/s2/favicons?domain={domain}&sz=128"


LOGOS: dict[str, str] = {
    "blender": favicon("blender.org"),
    "maya": favicon("autodesk.com"),
    "zbrush": favicon("maxon.net"),
    "substance-painter": favicon("adobe.com"),
    "krita": favicon("krita.org"),
    "photoshop": favicon("adobe.com"),
    "material-maker": "https://avatars.githubusercontent.com/u/56296542?s=120&v=4",
    "second-life": favicon("secondlife.com"),
    "marvelous-designer": favicon("marvelousdesigner.com"),
    "mari": favicon("foundry.com"),
    "topogun": favicon("topogun.com"),
    "pureref": favicon("pureref.com"),
    "marmoset-toolbag": favicon("marmoset.co"),
}

# Home-page card filenames → source logo key
HUB_ALIASES: dict[str, str] = {
    "start-here": "pureref",
    "blender": "blender",
    "breedables-research": "second-life",
    "second-life": "second-life",
    "addons": "blender",
    "production-line": "marvelous-designer",
    "workflow": "maya",
    "blender-path": "blender",
    "studio-labs": "zbrush",
    "tutorials": "krita",
    "tools-registry": "material-maker",
    "software-packages": "substance-painter",
}


def fetch(url: str, retries: int = 4) -> Image.Image:
    req = urllib.request.Request(url, headers={"User-Agent": "breedables-lab-wiki/1.0"})
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            im = Image.open(io.BytesIO(data))
            im = ImageOps.exif_transpose(im)
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGBA")
            return im
        except urllib.error.HTTPError as exc:
            last_err = exc
            if exc.code in (429, 503) and attempt + 1 < retries:
                time.sleep(2 ** attempt)
                continue
            raise
    raise last_err or RuntimeError(f"fetch failed: {url}")


def text_fallback(label: str) -> Image.Image:
    im = Image.new("RGB", (120, 120), BG)
    from PIL import ImageDraw, ImageFont

    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()
    words = label.replace("-", " ").split()
    line = words[0] if len(words) == 1 else words[0][:4]
    bbox = d.textbbox((0, 0), line, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((120 - tw) // 2, (120 - th) // 2), line, fill=(255, 180, 60), font=font)
    return im


def fit_on_canvas(im: Image.Image, size: int, background: tuple[int, int, int]) -> Image.Image:
    inner = size - PAD * 2
    im = im.copy()
    if im.mode == "RGBA":
        flat = Image.new("RGB", im.size, background)
        flat.paste(im, mask=im.split()[3])
        im = flat
    else:
        im = im.convert("RGB")
    im.thumbnail((inner, inner), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (size, size), background)
    ox = (size - im.width) // 2
    oy = (size - im.height) // 2
    canvas.paste(im, (ox, oy))
    return canvas


def fit_inline(im: Image.Image, max_width: int) -> Image.Image:
    im = im.copy()
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, BG)
        bg.paste(im, mask=im.split()[3])
        im = bg
    else:
        im = im.convert("RGB")
    if im.width > max_width:
        ratio = max_width / im.width
        im = im.resize((max_width, max(1, int(im.height * ratio))), Image.Resampling.LANCZOS)
    return im


def save_logo(name: str, url: str) -> None:
    try:
        im = fetch(url)
    except Exception as exc:
        print(f"WARN {name}: {exc} — text fallback", file=sys.stderr)
        im = text_fallback(name)
    time.sleep(1.2)
    card = fit_on_canvas(im, CARD_SIZE, BG)
    card_path = CARDS / f"{name}.png"
    card.save(card_path, format="PNG", optimize=True)

    inline = fit_inline(im, INLINE_MAX)
    inline_path = INLINE / f"{name}.png"
    inline.save(inline_path, format="PNG", optimize=True)

    card_kb = card_path.stat().st_size / 1024
    inline_kb = inline_path.stat().st_size / 1024
    print(f"{name}: card {card_kb:.0f} KB, inline {inline_kb:.0f} KB")


def main() -> int:
    CARDS.mkdir(parents=True, exist_ok=True)
    INLINE.mkdir(parents=True, exist_ok=True)

    for name, url in LOGOS.items():
        try:
            save_logo(name, url)
        except Exception as exc:
            print(f"WARN {name}: {exc}", file=sys.stderr)

    for hub_name, source in HUB_ALIASES.items():
        src = CARDS / f"{source}.png"
        dst = CARDS / f"{hub_name}.png"
        if src.exists() and hub_name != source:
            dst.write_bytes(src.read_bytes())
            print(f"hub alias: {hub_name} <- {source}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

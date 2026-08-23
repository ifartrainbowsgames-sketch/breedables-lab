#!/usr/bin/env python3
"""Crop and compress large wiki images for card thumbnails and inline use.

Drop multi-MB PNG/JPG/WebP files into docs/assets/inbox/. Run:

    python scripts/optimize-wiki-images.py

Outputs:
  docs/assets/cards/   — 200×200 center-crop PNG (~20–80 KB)
  docs/assets/inline/  — max width 800 px JPEG (~50–150 KB)

Requires: pip install Pillow
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Install Pillow: pip install Pillow", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "docs" / "assets" / "inbox"
CARDS = ROOT / "docs" / "assets" / "cards"
INLINE = ROOT / "docs" / "assets" / "inline"

CARD_SIZE = 200
INLINE_MAX_WIDTH = 800
SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tiff"}


def optimize_one(src: Path) -> tuple[Path, Path]:
    stem = src.stem
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        rgb = im.convert("RGB") if im.mode not in ("RGB", "RGBA") else im

        card = ImageOps.fit(rgb, (CARD_SIZE, CARD_SIZE), method=Image.Resampling.LANCZOS)
        card_path = CARDS / f"{stem}.png"
        card.save(card_path, format="PNG", optimize=True)

        inline = rgb.copy()
        if inline.width > INLINE_MAX_WIDTH:
            ratio = INLINE_MAX_WIDTH / inline.width
            inline = inline.resize(
                (INLINE_MAX_WIDTH, max(1, int(inline.height * ratio))),
                Image.Resampling.LANCZOS,
            )
        inline_path = INLINE / f"{stem}.jpg"
        inline.save(inline_path, format="JPEG", quality=82, optimize=True)

    return card_path, inline_path


def main() -> int:
    for d in (INBOX, CARDS, INLINE):
        d.mkdir(parents=True, exist_ok=True)

    sources = sorted(p for p in INBOX.iterdir() if p.suffix.lower() in SUPPORTED)
    if not sources:
        print(f"No images in {INBOX}. Drop PNG/JPG/WebP files there and re-run.")
        return 0

    for src in sources:
        card, inline = optimize_one(src)
        card_kb = card.stat().st_size / 1024
        inline_kb = inline.stat().st_size / 1024
        print(f"{src.name}: card {card_kb:.0f} KB, inline {inline_kb:.0f} KB")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

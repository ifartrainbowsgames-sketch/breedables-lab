"""Post-process webscreen discovery bundles with trafilatura (HTML → clean markdown)."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def extract_discovery_dir(discovery_dir: Path) -> dict:
    """Rewrite content.md from page.html using trafilatura. Returns status dict."""
    discovery_dir = discovery_dir.resolve()
    html_path = discovery_dir / "page.html"
    meta_path = discovery_dir / "meta.json"
    out_path = discovery_dir / "content.md"

    if not html_path.is_file():
        return {"ok": False, "error": "page.html missing — run webscreen screen first"}

    try:
        import trafilatura
    except ImportError as exc:
        return {
            "ok": False,
            "error": "trafilatura not installed — pip install -e '.[research]'",
            "detail": str(exc),
        }

    html = html_path.read_text(encoding="utf-8", errors="replace")
    meta: dict = {}
    if meta_path.is_file():
        import json

        meta = json.loads(meta_path.read_text(encoding="utf-8"))

    final_url = meta.get("final_url") or meta.get("url") or ""
    title = meta.get("title") or discovery_dir.name

    text = trafilatura.extract(
        html,
        url=final_url or None,
        include_comments=False,
        include_tables=True,
        output_format="markdown",
    )
    if not text or not text.strip():
        return {"ok": False, "error": "trafilatura returned empty text"}

    header = f"# {title}\n\n> Source: {final_url}\n"
    header += f"> Extracted: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} (trafilatura)\n\n"
    out_path.write_text(header + text.strip() + "\n", encoding="utf-8")
    return {"ok": True, "path": str(out_path.relative_to(discovery_dir)), "chars": len(text)}


def extract_after_screen(repo_root: Path, slug: str) -> dict:
    discovery_dir = repo_root / "research" / "discoveries" / slug
    result = extract_discovery_dir(discovery_dir)
    result["slug"] = slug
    return result

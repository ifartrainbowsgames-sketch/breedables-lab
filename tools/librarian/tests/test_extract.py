from pathlib import Path

import pytest

trafilatura = pytest.importorskip("trafilatura")

from librarian.extract import extract_discovery_dir


def test_extract_discovery_dir(tmp_path: Path) -> None:
    discovery = tmp_path / "test-slug"
    discovery.mkdir()
    (discovery / "meta.json").write_text(
        '{"title": "Example", "final_url": "https://example.com/page"}',
        encoding="utf-8",
    )
    html = """<!DOCTYPE html><html><head><title>Example</title></head>
    <body><article><h1>Hello</h1><p>World content here.</p></article></body></html>"""
    (discovery / "page.html").write_text(html, encoding="utf-8")

    result = extract_discovery_dir(discovery)
    assert result["ok"] is True
    content = (discovery / "content.md").read_text(encoding="utf-8")
    assert "Hello" in content or "World" in content
    assert "example.com" in content

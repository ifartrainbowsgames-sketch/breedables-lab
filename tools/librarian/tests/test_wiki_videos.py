from librarian.wiki_videos import breedwiki_reply, inventory_wiki_videos, parse_video_index


def test_parse_video_index_skips_placeholders(tmp_path):
    path = tmp_path / "videos.md"
    path.write_text(
        """# Videos

## A01 — Organic PBR

| Title | URL | Notes |
|-------|-----|-------|
| Real tutorial | https://www.youtube.com/watch?v=abc123 | official |
| *TBD — later* | — | Add when reviewed |
""",
        encoding="utf-8",
    )
    videos = parse_video_index(path)
    assert len(videos) == 1
    assert videos[0]["title"] == "Real tutorial"
    assert videos[0]["url"].endswith("abc123")


def test_inventory_counts_curated_wiki_videos():
    from pathlib import Path

    root = Path(__file__).resolve().parents[3]
    payload = inventory_wiki_videos(root, no_kimi=True)
    assert payload["total"] == 3
    assert payload["kimi"] == "skipped"
    assert payload["video_library"] == "docs/academy/resources/videos.md"
    titles = {item["title"] for item in payload["videos"]}
    assert "Material Maker intro" in titles


def test_breedwiki_reply_links_to_video_library():
    inventory = {
        "total": 2,
        "videos": [
            {"title": "Material Maker intro", "url": "https://example.com/mm", "section": "A01"},
            {"title": "PBR Texturing", "url": "https://example.com/pbr", "section": "A01"},
        ],
    }
    text = breedwiki_reply(
        "https://ifartrainbowsgames-sketch.github.io/breedables-lab",
        query="material",
        inventory=inventory,
    )
    assert "academy/resources/videos/" in text
    assert "Curated videos: 2" in text
    assert "Material Maker intro" in text
    assert "PBR Texturing" not in text

from librarian.wiki_videos import (
    embed_block,
    merge_videos,
    render_video_library,
    seed_videos_local,
    youtube_id_from_url,
)


def test_youtube_id_from_watch_url() -> None:
    assert youtube_id_from_url("https://www.youtube.com/watch?v=h6E9N10rN5s") == "h6E9N10rN5s"


def test_embed_block_contains_iframe() -> None:
    html = embed_block("abc123xyz01", "Test title")
    assert "youtube-nocookie.com/embed/abc123xyz01" in html
    assert "wiki-video" in html


def test_render_video_library_has_sections() -> None:
    md = render_video_library(seed_videos_local())
    assert "## Blender" in md
    assert "wiki-video" in md
    assert "#blender" in md


def test_merge_videos_dedupes() -> None:
    a = [{"software": "blender", "title": "A", "url": "https://youtube.com/watch?v=aaa", "youtube_id": "aaa"}]
    b = [{"software": "blender", "title": "A dup", "url": "https://youtube.com/watch?v=aaa", "youtube_id": "aaa"}]
    assert len(merge_videos(a, b)) == 1

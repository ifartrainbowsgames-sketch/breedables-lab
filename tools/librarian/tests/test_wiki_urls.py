from librarian.wiki_urls import extract_links


def test_extract_markdown_links():
    text = """
    See [Donut](https://www.youtube.com/playlist?list=abc) and
    [Manual](https://docs.blender.org/manual/en/latest/).
    Bare: https://wiki.secondlife.com/wiki/Ozimals
    """
    links = extract_links(text, "docs/academy/resources/tutorials.md")
    urls = {l.url for l in links}
    assert "https://www.youtube.com/playlist?list=abc" in urls
    assert "https://docs.blender.org/manual/en/latest/" in urls
    assert "https://wiki.secondlife.com/wiki/Ozimals" in urls

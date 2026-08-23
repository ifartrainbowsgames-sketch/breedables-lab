from librarian.ingest import parse_feed


def test_parse_rss():
    xml = """<rss><channel><item><title>Tool A</title><link>https://example.com/a</link></item></channel></rss>"""
    items = parse_feed(xml)
    assert [(i.title, i.url) for i in items] == [("Tool A", "https://example.com/a")]


def test_parse_atom():
    xml = """<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Tool B</title><link rel="alternate" href="https://example.com/b" /></entry></feed>"""
    items = parse_feed(xml)
    assert [(i.title, i.url) for i in items] == [("Tool B", "https://example.com/b")]

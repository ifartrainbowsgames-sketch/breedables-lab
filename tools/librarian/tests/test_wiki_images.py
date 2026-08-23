from librarian.wiki_images import HUB_ALIASES, _parse_json_array, discover_images_local


def test_parse_json_array_from_fence() -> None:
    raw = """Here are images:
```json
[{"slug": "blender", "url": "https://example.com/b.png", "license": "test", "alt": "Blender"}]
```
"""
    data = _parse_json_array(raw)
    assert len(data) == 1
    assert data[0]["slug"] == "blender"


def test_discover_images_local_has_software_slugs() -> None:
    entries = discover_images_local()
    slugs = {e["slug"] for e in entries}
    assert "blender" in slugs
    assert "second-life" in slugs


def test_hub_aliases_reference_existing_sources() -> None:
    software = {e["slug"] for e in discover_images_local()}
    for hub, source in HUB_ALIASES.items():
        assert source in software or hub in software

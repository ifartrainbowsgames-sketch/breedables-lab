from librarian.db import LibrarianDB


def test_add_and_merge_duplicate(tmp_path):
    db = LibrarianDB(tmp_path / "test.sqlite3")
    db.init()

    first, created = db.add(
        name="Material Maker",
        url="https://github.com/RodZill4/material-maker?utm_source=test",
        category="textures",
        commercial_type="OPEN_SOURCE",
        code_license="MIT",
        status="EXPERIMENTAL",
    )
    assert created is True

    second, created = db.add(
        name="material-maker",
        url="https://www.github.com/RodZill4/material-maker/tree/main",
        category="textures",
    )
    assert created is False
    assert second.id == first.id
    assert second.code_license == "MIT"
    assert second.commercial_type == "OPEN_SOURCE"
    assert len(db.list()) == 1


def test_gaps_flags_unchecked_and_unknown(tmp_path):
    db = LibrarianDB(tmp_path / "test.sqlite3")
    db.init()
    db.add(name="Mystery Tool", url="https://example.com")
    gaps = db.gaps()
    assert gaps
    assert "link not checked" in gaps[0]["issues"]
    assert "commercial type unknown" in gaps[0]["issues"]

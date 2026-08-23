from pathlib import Path

from librarian.academy_manifest import academy_content_gaps
from librarian.db import LibrarianDB


def test_gaps_flags_missing_evidence(tmp_path):
    db = LibrarianDB(tmp_path / "test.sqlite3")
    db.init()
    db.add(name="Mystery Tool", url="https://example.com")
    gaps = db.gaps()
    assert gaps
    assert "missing primary video" in gaps[0]["issues"]
    assert "missing official doc links" in gaps[0]["issues"]


def test_set_evidence_clears_gaps(tmp_path):
    repo_root = tmp_path / "repo"
    lesson = repo_root / "docs/academy/tracks/a01-organic-pbr.md"
    lesson.parent.mkdir(parents=True)
    lesson.write_text("# lesson\n" + ("x" * 600), encoding="utf-8")
    evidence = repo_root / "training/texturing/a01"
    evidence.mkdir(parents=True)
    (evidence / "notes.md").write_text("done", encoding="utf-8")

    db = LibrarianDB(tmp_path / "test.sqlite3")
    db.init()
    resource, _ = db.add(
        name="Material Maker",
        url="https://github.com/RodZill4/material-maker",
        commercial_type="OPEN_SOURCE",
        code_license="MIT",
    )
    db.update_evidence(
        resource.id,
        primary_video_url="https://www.youtube.com/watch?v=example",
        doc_urls=["https://github.com/RodZill4/material-maker/wiki"],
        lesson_wiki_path="docs/academy/tracks/a01-organic-pbr.md",
        evidence_path="training/texturing/a01/",
        academy_track="A01",
    )
    gaps = db.evidence_gaps(repo_root=repo_root)
    names = [g["name"] for g in gaps]
    assert "Material Maker" not in names


def test_academy_content_gaps_detects_missing_track(tmp_path):
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    gaps = academy_content_gaps(repo_root)
    assert gaps
    assert any(g["kind"] == "academy_track" for g in gaps)

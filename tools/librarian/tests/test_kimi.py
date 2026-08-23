from librarian.academy_manifest import humanize_codes
from librarian.kimi import (
    _parse_kimi_cli_stream_json,
    _strip_markdown_fence,
    humanize_report_local,
    resolve_kimi_backend,
    wiki_evolution_local,
)
from librarian.wiki_context import build_wiki_context, WIKI_MISSION


def test_humanize_codes_replaces_track_and_lesson_ids() -> None:
    text = "Complete B06 and B07 before A01; see A03 retopo."
    out = humanize_codes(text)
    assert "B06" not in out
    assert "B07" not in out
    assert "A01" not in out
    assert "Blender lesson 6" in out
    assert "Organic PBR" in out


def test_humanize_report_local_plain_english() -> None:
    payload = {
        "generated_at": "2026-08-23T12:00:00+00:00",
        "summary": {"wiki_links_checked": 90, "wiki_links_failed": 0},
        "registry_gaps": [{"name": "RetopoFlow", "issues": ["commercial type unknown"]}],
        "next_actions": ["Registry: RetopoFlow — commercial type unknown"],
    }
    md = humanize_report_local(payload)
    assert "plain English" in md.lower() or "In plain English" in md
    assert "RetopoFlow" in md
    assert "A01" not in md


def test_wiki_evolution_local_includes_mission() -> None:
    context = {
        "daily_report": {
            "generated_at": "2026-08-23T12:00:00+00:00",
            "summary": {"wiki_links_checked": 90, "wiki_links_failed": 0, "academy_gaps": 0, "registry_gaps": 1},
            "registry_gaps": [{"name": "RetopoFlow", "issues": ["commercial type unknown"]}],
        }
    }
    md = wiki_evolution_local(context)
    assert "Mission check" in md
    assert "Second Life breedables" in md
    assert "Daily task list" in md


def test_build_wiki_context_has_mission(tmp_path) -> None:
    from librarian.db import LibrarianDB

    repo = tmp_path
    (repo / "docs" / "academy").mkdir(parents=True)
    (repo / "docs" / "academy" / "start-here.md").write_text("# Start", encoding="utf-8")
    (repo / "mkdocs.yml").write_text("site_name: test\n", encoding="utf-8")
    db = LibrarianDB(repo / "test.sqlite3")
    db.init()
    ctx = build_wiki_context(repo, db, {"summary": {}, "generated_at": "2026-08-23"})
    assert "breedables" in ctx["mission"].lower()
    assert len(ctx["blender_lessons"]) == 10
    assert WIKI_MISSION.strip()


def test_parse_kimi_cli_stream_json() -> None:
    stdout = (
        '{"role":"meta","type":"system.version","version":"0.38.0"}\n'
        '{"role":"assistant","content":"# Hello\\n\\nWorld"}\n'
    )
    text = _parse_kimi_cli_stream_json(stdout)
    assert text == "# Hello\n\nWorld\n"


def test_strip_markdown_fence() -> None:
    wrapped = "```markdown\n# Title\n\nBody\n```"
    assert _strip_markdown_fence(wrapped) == "# Title\n\nBody\n"


def test_resolve_kimi_backend_off_without_cli_or_api(monkeypatch) -> None:
    monkeypatch.delenv("MOONSHOT_API_KEY", raising=False)
    monkeypatch.setenv("KIMI_BACKEND", "off")
    assert resolve_kimi_backend() == "off"

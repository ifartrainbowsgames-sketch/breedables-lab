import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from librarian.kimi import KimiQuotaExhausted, KimiUnavailableError, _quota_error_from
from librarian.wiki_worker import (
    Task,
    build_queue,
    clear_cooldown,
    cooldown_remaining,
    load_state,
    parse_page_json,
    run_cycle,
    run_forever,
    save_state,
    start_cooldown,
)

FM = '---\ntitle: "T"\nsection: modeling\ntype: topic\n---\n'


def make_wiki(tmp_path: Path, pages: dict[str, str]) -> Path:
    for rel, text in pages.items():
        p = tmp_path / "docs" / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return tmp_path


# ------------------------------------------------------------------ quota

@pytest.mark.parametrize("status,body", [
    (429, "rate limit reached"),
    (402, "insufficient balance"),
    (400, "exceeded_current_quota_error"),
    (403, "billing not active"),
])
def test_quota_conditions_are_classified(status, body):
    assert _quota_error_from(status, body) is not None


@pytest.mark.parametrize("status,body", [
    (500, "internal server error"),
    (404, "model not found"),
    (400, "invalid request: bad parameter"),
])
def test_non_quota_errors_are_not_misread_as_quota(status, body):
    assert _quota_error_from(status, body) is None


def test_retry_after_header_is_honoured():
    err = _quota_error_from(429, "slow down", {"Retry-After": "120"})
    assert err.retry_after == 120


def test_quota_error_has_a_floor():
    assert KimiQuotaExhausted("x", retry_after=1).retry_after == 60


def test_quota_error_is_an_unavailable_error():
    # so existing handlers keep working
    assert issubclass(KimiQuotaExhausted, KimiUnavailableError)


# ------------------------------------------------------------- cooldown

def test_cooldown_roundtrip(tmp_path):
    state = load_state(tmp_path)
    assert cooldown_remaining(state) == 0
    state = start_cooldown(tmp_path, state, 600, "usage spent")
    assert 500 < cooldown_remaining(load_state(tmp_path)) <= 600
    clear_cooldown(tmp_path, load_state(tmp_path))
    assert cooldown_remaining(load_state(tmp_path)) == 0


def test_expired_cooldown_reports_zero(tmp_path):
    state = load_state(tmp_path)
    state["cooldown_until"] = (datetime.now(timezone.utc) - timedelta(minutes=5)).isoformat()
    save_state(tmp_path, state)
    assert cooldown_remaining(load_state(tmp_path)) == 0


def test_corrupt_state_does_not_crash(tmp_path):
    p = tmp_path / "tools/librarian/.data/worker-state.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("{not json", encoding="utf-8")
    assert cooldown_remaining(load_state(tmp_path)) == 0


# ------------------------------------------------------------------ queue

def test_thin_pages_are_queued(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\nshort.\n"})
    kinds = {t.kind for t in build_queue(tmp_path)}
    assert "expand-thin" in kinds


def test_substantial_page_is_not_queued_as_thin(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\n" + ("word " * 400)})
    assert not [t for t in build_queue(tmp_path)
                if t.kind == "expand-thin" and t.target == "modeling/x.md"]


def test_structure_errors_outrank_everything(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\n## A\n\na\n\n## A\n\nb\n"})
    q = build_queue(tmp_path)
    assert q[0].kind == "fix-structure"
    assert q[0].priority == 0


# ------------------------------------------------------------------ cycle

def test_cycle_parked_on_cooldown_makes_no_calls(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\nshort.\n"})
    start_cooldown(tmp_path, load_state(tmp_path), 900, "usage spent")

    def explode(_repo, _task):
        raise AssertionError("model must not be called while cooling down")

    out = run_cycle(tmp_path, ask=explode)
    assert out["status"] == "cooling_down"
    assert out["retry_in_seconds"] > 0


def test_quota_mid_cycle_starts_cooldown_and_stops(tmp_path):
    make_wiki(tmp_path, {
        "modeling/a.md": FM + "# A\n\nshort.\n",
        "modeling/b.md": FM + "# B\n\nshort.\n",
    })
    calls = []

    def quota(_repo, task):
        calls.append(task.key)
        raise KimiQuotaExhausted("usage spent", retry_after=1800)

    out = run_cycle(tmp_path, ask=quota)
    assert out["status"] == "quota_exhausted"
    assert out["retry_in_seconds"] == 1800
    assert len(calls) == 1, "must stop after the first quota error, not keep trying"
    assert cooldown_remaining(load_state(tmp_path)) > 0


def test_cycle_resumes_after_cooldown_expires(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\nshort.\n"})
    state = load_state(tmp_path)
    state["cooldown_until"] = (datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat()
    state["cooldown_reason"] = "usage spent"
    save_state(tmp_path, state)

    called = []

    def ask(_repo, task):
        called.append(task.key)
        raise KimiQuotaExhausted("spent again", retry_after=60)

    out = run_cycle(tmp_path, ask=ask)
    assert called, "expired cooldown must let the worker try again"
    assert out.get("note") == "cooldown expired — resuming"


def test_dry_run_makes_no_calls(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\nshort.\n"})

    def explode(_repo, _task):
        raise AssertionError("dry run must not call the model")

    out = run_cycle(tmp_path, dry_run=True, ask=explode)
    assert out["status"] == "planned"


def test_invalid_model_output_is_rejected_not_written(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\nshort.\n"})

    def bad(_repo, _task):
        return {"title": "B07 Bad Title", "section": "modeling", "type": "topic",
                "summary": "s", "sections": [{"heading": "H", "body": "b"}]}

    out = run_cycle(tmp_path, ask=bad)
    assert out["written"] == []
    assert out["rejected"]


def test_idle_when_nothing_to_do(tmp_path):
    make_wiki(tmp_path, {"modeling/x.md": FM + "# T\n\n" + ("word " * 400)})
    out = run_cycle(tmp_path, ask=lambda *_: {})
    assert out["status"] in ("idle", "ok")


# ------------------------------------------------------------------- loop

def test_loop_sleeps_out_the_cooldown_then_continues():
    slept: list[float] = []
    seq = [
        {"status": "quota_exhausted", "retry_in_seconds": 1800},
        {"status": "ok", "written": [], "queue_depth": 1},
    ]

    def cycle(_repo):
        return seq.pop(0)

    run_forever(Path("."), interval=60, cycle_fn=cycle, max_cycles=2,
                sleep_fn=slept.append)
    assert slept[0] == 1860, "must wait the provider's retry window, not the poll interval"
    assert slept[1] == 60, "must return to normal cadence once usage is back"


def test_loop_survives_an_exception_and_backs_off():
    slept: list[float] = []

    def cycle(_repo):
        raise RuntimeError("network down")

    run_forever(Path("."), interval=60, cycle_fn=cycle, max_cycles=3,
                sleep_fn=slept.append)
    assert slept == [120, 240, 480], "exponential backoff on repeated failure"


def test_loop_idles_less_often_when_there_is_no_work():
    slept: list[float] = []
    run_forever(Path("."), interval=60, cycle_fn=lambda _r: {"status": "idle"},
                max_cycles=1, sleep_fn=slept.append)
    assert slept[0] >= 3600


# -------------------------------------------------------------- json parse

def test_parse_plain_json():
    assert parse_page_json('{"title": "x"}')["title"] == "x"


def test_parse_fenced_json():
    assert parse_page_json('```json\n{"title": "x"}\n```')["title"] == "x"


def test_parse_json_with_surrounding_prose():
    reply = 'Here you go:\n\n{"title": "x"}\n\nHope that helps.'
    assert parse_page_json(reply)["title"] == "x"


# ------------------------------------------------------ json repair / re-ask

def test_repair_escapes_raw_newlines_in_strings():
    from librarian.wiki_worker import repair_json
    broken = '{"body": "line one\nline two"}'
    assert json.loads(repair_json(broken))["body"] == "line one\nline two"


def test_repair_strips_trailing_commas():
    from librarian.wiki_worker import repair_json
    assert json.loads(repair_json('{"a": 1, "b": [1, 2,],}'))["b"] == [1, 2]


def test_repair_leaves_valid_json_untouched():
    from librarian.wiki_worker import repair_json
    # already-escaped newline: repair must not double-escape it
    good = json.dumps({"a": "already\nescaped", "b": [1, 2]})
    assert json.loads(repair_json(good)) == json.loads(good)


def test_parse_recovers_unescaped_newline_reply():
    reply = '{"title": "X", "sections": [{"heading": "H", "body": "para one\npara two"}]}'
    assert parse_page_json(reply)["sections"][0]["body"] == "para one\npara two"


def test_parse_rejects_non_object_json():
    from librarian.wiki_page import PageRejected
    with pytest.raises(PageRejected):
        parse_page_json('["not", "an", "object"]')


def test_ask_reasks_once_on_unparseable_reply(monkeypatch, tmp_path):
    import librarian.wiki_worker as w

    prompts, replies = [], ['not json at all', '{"title": "X"}']

    def fake(**kw):
        prompts.append(kw["user"])
        return replies.pop(0), "test"

    monkeypatch.setattr(w, "_kimi_complete", fake)
    monkeypatch.setattr(w, "_task_prompt", lambda *a, **k: "base prompt")
    out = w.ask_kimi(tmp_path, Task("expand-thin", "modeling/x.md", "r", 2))
    assert out["title"] == "X"
    assert len(prompts) == 2
    assert "could not be parsed" in prompts[1], "the retry must say what went wrong"


def test_ask_gives_up_after_the_bound(monkeypatch, tmp_path):
    import librarian.wiki_worker as w
    from librarian.wiki_page import PageRejected

    calls = []

    def fake(**kw):
        calls.append(1)
        return "still not json", "test"

    monkeypatch.setattr(w, "_kimi_complete", fake)
    monkeypatch.setattr(w, "_task_prompt", lambda *a, **k: "base prompt")
    with pytest.raises(PageRejected):
        w.ask_kimi(tmp_path, Task("expand-thin", "modeling/x.md", "r", 2))
    assert len(calls) == 2, "must not retry forever"


def test_quota_error_is_not_retried(monkeypatch, tmp_path):
    import librarian.wiki_worker as w

    calls = []

    def fake(**kw):
        calls.append(1)
        raise KimiQuotaExhausted("spent", retry_after=600)

    monkeypatch.setattr(w, "_kimi_complete", fake)
    monkeypatch.setattr(w, "_task_prompt", lambda *a, **k: "base prompt")
    with pytest.raises(KimiQuotaExhausted):
        w.ask_kimi(tmp_path, Task("expand-thin", "modeling/x.md", "r", 2))
    assert len(calls) == 1, "a spent quota must not burn the retry budget"


def test_worker_will_not_switch_branches_under_a_dirty_tree(monkeypatch, tmp_path):
    import librarian.wiki_worker as w

    monkeypatch.setattr(w, "tree_is_dirty", lambda _r: True)
    monkeypatch.setattr(w, "_git", lambda _r, *a: "feature/x" if a[:1] == ("rev-parse",) else "")
    assert w.working_branch(tmp_path) is None


def test_worker_uses_its_branch_when_the_tree_is_clean(monkeypatch, tmp_path):
    import librarian.wiki_worker as w

    monkeypatch.setattr(w, "tree_is_dirty", lambda _r: False)
    monkeypatch.setattr(w, "_git", lambda _r, *a: "main" if a[:1] == ("rev-parse",) else "")
    assert w.working_branch(tmp_path).startswith("wiki-worker/")


def test_repair_escapes_unescaped_inner_quotes():
    from librarian.wiki_worker import repair_json
    # model wrote a quoted phrase inside a value without escaping it
    broken = '{"body": "the so-called "cage" errors", "n": 1}'
    assert json.loads(repair_json(broken))["body"] == 'the so-called "cage" errors'


def test_repair_keeps_real_string_boundaries():
    from librarian.wiki_worker import repair_json
    ok = '{"a": "one", "b": "two", "c": ["x", "y"]}'
    assert json.loads(repair_json(ok)) == json.loads(ok)


def test_repair_handles_quote_before_closing_brace():
    from librarian.wiki_worker import repair_json
    assert json.loads(repair_json('{"a": "value"}'))["a"] == "value"


# --------------------------------------------------- json extraction / shapes

def test_extract_returns_balanced_objects_not_a_greedy_span():
    from librarian.wiki_worker import extract_json_objects
    text = 'thinking {"a": 1} then {"b": {"c": 2}} done'
    blocks = extract_json_objects(text)
    assert '{"b": {"c": 2}}' in blocks
    assert '{"a": 1}' in blocks
    assert not any(b.startswith('{"a": 1} then') for b in blocks)


def test_extract_ignores_braces_inside_strings():
    from librarian.wiki_worker import extract_json_objects
    blocks = extract_json_objects('{"body": "use {curly} braces"}')
    assert blocks == ['{"body": "use {curly} braces"}']


def test_parse_picks_the_object_from_surrounding_reasoning():
    reply = 'We should update it. {"title": "X", "section": "modeling"}'
    assert parse_page_json(reply)["title"] == "X"


def test_update_action_shape_is_normalised(tmp_path):
    from librarian.wiki_worker import normalise_payload
    task = Task("expand-thin", "modeling/software/retopoflow.md", "thin", 2)
    out = normalise_payload({"action": "update", "path": "modeling/software/retopoflow.md",
                             "title": "RetopoFlow", "summary": "s"}, task)
    assert out["section"] == "modeling"
    assert out["type"] == "software"
    assert out["slug"] == "retopoflow"
    assert "action" not in out and "path" not in out


def test_normalise_infers_type_from_the_target_folder():
    from librarian.wiki_worker import normalise_payload
    cases = {
        "modeling/software/x.md": "software",
        "texturing/projects/x.md": "project",
        "academy/paths/x.md": "path",
        "research/index.md": "index",
        "modeling/x.md": "topic",
    }
    for target, expected in cases.items():
        out = normalise_payload({"title": "T"}, Task("expand-thin", target, "r", 2))
        assert out["type"] == expected, target


def test_normalise_does_not_override_what_the_model_stated():
    from librarian.wiki_worker import normalise_payload
    out = normalise_payload({"title": "T", "type": "reference", "section": "research"},
                            Task("expand-thin", "modeling/x.md", "r", 2))
    assert out["type"] == "reference" and out["section"] == "research"


def test_update_without_title_inherits_it_from_the_page(tmp_path):
    from librarian.wiki_worker import normalise_payload
    make_wiki(tmp_path, {"modeling/software/retopoflow.md":
                         '---\ntitle: "RetopoFlow"\nsection: modeling\ntype: software\n---\n'
                         "# RetopoFlow\n\nshort.\n"})
    task = Task("expand-thin", "modeling/software/retopoflow.md", "thin", 2)
    out = normalise_payload({"action": "update", "sections": [{"heading": "H", "body": "b"}]},
                            task, tmp_path)
    assert out["title"] == "RetopoFlow"
    assert out["type"] == "software"
    assert out["section"] == "modeling"


def test_title_falls_back_to_the_h1_when_frontmatter_lacks_one(tmp_path):
    from librarian.wiki_worker import normalise_payload
    make_wiki(tmp_path, {"modeling/x.md": "# Mesh modeling\n\nshort.\n"})
    out = normalise_payload({}, Task("expand-thin", "modeling/x.md", "r", 2), tmp_path)
    assert out["title"] == "Mesh modeling"


def test_model_supplied_title_wins_over_the_existing_one(tmp_path):
    from librarian.wiki_worker import normalise_payload
    make_wiki(tmp_path, {"modeling/x.md": '---\ntitle: "Old"\n---\n# Old\n'})
    out = normalise_payload({"title": "New"}, Task("expand-thin", "modeling/x.md", "r", 2), tmp_path)
    assert out["title"] == "New"

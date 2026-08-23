from librarian.config import Settings
from librarian.notify import (
    NotifyUnavailableError,
    apprise_urls_from_env,
    format_daily_slack_body,
    send_notification,
)


def test_apprise_urls_from_bot_and_channel(monkeypatch) -> None:
    monkeypatch.setenv("SLACK_BOT_TOKEN", "xoxb-test-token")
    monkeypatch.setenv("SLACK_NOTIFY_CHANNEL", "breedables-knowledge")
    monkeypatch.delenv("APPRISE_URLS", raising=False)
    monkeypatch.delenv("SLACK_WEBHOOK_URL", raising=False)
    urls = apprise_urls_from_env()
    assert len(urls) == 1
    assert urls[0].startswith("slackb://xoxb-test-token/#breedables-knowledge")


def test_format_daily_slack_body_includes_summary() -> None:
    payload = {
        "generated_at": "2026-08-24T00:00:00+00:00",
        "summary": {
            "wiki_links_checked": 80,
            "wiki_links_failed": 2,
            "academy_gaps": 3,
            "registry_gaps": 1,
        },
        "next_actions": ["Fix broken links", "Fill B04 lesson"],
        "paths": {"human": "research/discoveries/daily-2026-08-24/report-human.md"},
    }
    body = format_daily_slack_body(payload, wiki_base_url="https://example.com/wiki")
    assert "Daily wiki" in body
    assert "failed:* 2" in body
    assert "Fix broken links" in body
    assert "example.com/wiki" in body


def test_send_notification_requires_urls(monkeypatch) -> None:
    monkeypatch.delenv("APPRISE_URLS", raising=False)
    monkeypatch.delenv("SLACK_WEBHOOK_URL", raising=False)
    monkeypatch.delenv("SLACK_BOT_TOKEN", raising=False)
    monkeypatch.delenv("SLACK_NOTIFY_CHANNEL", raising=False)
    try:
        send_notification("test", settings=Settings.from_env())
        assert False, "expected NotifyUnavailableError"
    except NotifyUnavailableError:
        pass

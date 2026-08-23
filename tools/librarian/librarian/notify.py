"""Post Librarian reports to Slack (and other channels) via Apprise."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .config import Settings


class NotifyUnavailableError(RuntimeError):
    """No notification URLs configured or apprise not installed."""


def apprise_urls_from_env(settings: Settings | None = None) -> list[str]:
    """Build Apprise URL list from environment."""
    urls: list[str] = []
    raw = os.getenv("APPRISE_URLS", "").strip()
    if raw:
        urls.extend(part.strip() for part in raw.split(",") if part.strip())

    webhook = os.getenv("SLACK_WEBHOOK_URL", "").strip()
    if webhook:
        urls.append(webhook if webhook.startswith("http") else f"slack://{webhook}")

    bot = (settings.slack_bot_token if settings else None) or os.getenv("SLACK_BOT_TOKEN", "")
    bot = bot.strip()
    channel = os.getenv("SLACK_NOTIFY_CHANNEL", "").strip()
    if bot and channel and not _has_slack_url(urls):
        target = channel if channel.startswith("#") or channel.startswith("@") else f"#{channel}"
        urls.append(f"slackb://{bot}/{target}")

    return urls


def _has_slack_url(urls: list[str]) -> bool:
    return any(u.startswith("slack") for u in urls)


def format_daily_slack_body(payload: dict[str, Any], *, wiki_base_url: str) -> str:
    """Short Slack-friendly summary of a daily-wiki payload."""
    s = payload["summary"]
    day = payload["generated_at"][:10]
    lines = [
        f"*Daily wiki — {day}*",
        f"• Links checked: {s['wiki_links_checked']} · *failed:* {s['wiki_links_failed']}",
        f"• Academy gaps: {s['academy_gaps']} · Registry gaps: {s['registry_gaps']}",
        "",
        "*Next actions*",
    ]
    for action in payload.get("next_actions", [])[:5]:
        lines.append(f"• {action}")

    paths = payload.get("paths") or {}
    if paths.get("human"):
        lines.extend(["", f"Human briefing: `{paths['human']}`"])
    if paths.get("evolution"):
        lines.append(f"Wiki evolution: `{paths['evolution']}`")
    lines.extend(["", f"<{wiki_base_url}|Open wiki>"])
    return "\n".join(lines)


def send_notification(
    body: str,
    *,
    title: str = "Breedables Librarian",
    urls: list[str] | None = None,
    settings: Settings | None = None,
) -> dict[str, Any]:
    """Send a notification through Apprise. Returns result metadata."""
    targets = urls if urls is not None else apprise_urls_from_env(settings)
    if not targets:
        raise NotifyUnavailableError(
            "Set APPRISE_URLS, SLACK_WEBHOOK_URL, or SLACK_BOT_TOKEN + SLACK_NOTIFY_CHANNEL"
        )

    try:
        import apprise
    except ImportError as exc:
        raise NotifyUnavailableError(
            "Install notify extras: pip install -e \".[notify]\""
        ) from exc

    app = apprise.Apprise()
    for url in targets:
        app.add(url)

    ok = app.notify(body=body, title=title, body_format=apprise.NotifyFormat.MARKDOWN)
    if ok:
        return {"ok": True, "targets": len(targets), "via": "apprise"}

    # Apprise slackb:// can fail on some workspaces — fall back to slack-sdk bot post.
    bot = (settings.slack_bot_token if settings else None) or os.getenv("SLACK_BOT_TOKEN", "")
    channel = os.getenv("SLACK_NOTIFY_CHANNEL", "").strip()
    if bot.strip() and channel:
        try:
            from slack_sdk import WebClient
            from slack_sdk.errors import SlackApiError

            client = WebClient(token=bot.strip())
            target = channel if channel.startswith("#") or channel.startswith("@") else f"#{channel}"
            resp = client.chat_postMessage(channel=target, text=f"*{title}*\n{body}", mrkdwn=True)
            return {"ok": bool(resp.get("ok")), "targets": 1, "via": "slack_sdk"}
        except SlackApiError as exc:
            return {"ok": False, "targets": len(targets), "via": "slack_sdk", "error": str(exc)}

    return {"ok": False, "targets": len(targets), "via": "apprise"}


def notify_daily_wiki(
    payload: dict[str, Any],
    *,
    settings: Settings,
) -> dict[str, Any]:
    """Post daily-wiki summary to configured Slack/notification channels."""
    body = format_daily_slack_body(payload, wiki_base_url=settings.wiki_base_url)
    day = payload["generated_at"][:10]
    return send_notification(
        body,
        title=f"Breedables wiki — {day}",
        settings=settings,
    )


def notify_test(settings: Settings) -> dict[str, Any]:
    """Smoke test notification delivery."""
    body = (
        "*Breedables Librarian* — Apprise connection test\n"
        f"• Repo: `{settings.repo_root}`\n"
        f"• Wiki: {settings.wiki_base_url}"
    )
    return send_notification(body, title="Librarian notify test", settings=settings)

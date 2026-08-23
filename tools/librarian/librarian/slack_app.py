from __future__ import annotations

import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from .config import Settings
from .db import LibrarianDB


def _format_resource(r) -> str:
    license_value = r.code_license or r.github_license or "unknown"
    return (
        f"*{r.name}*\n"
        f"Type: `{r.commercial_type}` | Status: `{r.status}` | License: `{license_value}`\n"
        f"Category: `{r.category}`\n"
        f"Official: {r.url}\n"
        f"HTTP: `{r.http_status if r.http_status is not None else 'unchecked'}`"
    )


def _open_db(settings: Settings) -> LibrarianDB:
    db = LibrarianDB(settings.db_path)
    db.init()
    return db


def build_app(settings: Settings) -> App:
    if not settings.slack_bot_token:
        raise RuntimeError("SLACK_BOT_TOKEN is required")

    app = App(token=settings.slack_bot_token)

    @app.command("/breedtool")
    def breedtool(ack, respond, command):
        ack()
        query = (command.get("text") or "").strip()
        if not query:
            respond("Usage: `/breedtool material maker`")
            return
        db = _open_db(settings)
        matches = db.search(query, limit=5)
        if not matches:
            respond(f"No Librarian record matched `{query}`.")
            return
        respond("\n\n".join(_format_resource(r) for r in matches))

    @app.command("/breedstatus")
    def breedstatus(ack, respond):
        ack()
        db = _open_db(settings)
        counts = db.status_counts()
        if not counts:
            respond("The Librarian registry is empty.")
            return
        respond("*Breedables Librarian status*\n" + "\n".join(f"• `{k}`: {v}" for k, v in counts.items()))

    @app.command("/breedgaps")
    def breedgaps(ack, respond):
        ack()
        db = _open_db(settings)
        gaps = db.gaps(limit=10)
        if not gaps:
            respond("No obvious registry gaps found.")
            return
        lines = ["*Top registry gaps*"]
        for item in gaps:
            lines.append(f"• #{item['id']} *{item['name']}*: {', '.join(item['issues'])}")
        respond("\n".join(lines))

    @app.event("app_mention")
    def on_mention(event, say):
        text = re.sub(r"<@[^>]+>", "", event.get("text", "")).strip()
        if not text:
            say("Try `tool <name>`, `status`, or `gaps`.")
            return
        db = _open_db(settings)
        lowered = text.casefold()
        if lowered == "status":
            counts = db.status_counts()
            say(" ".join(f"{k}:{v}" for k, v in counts.items()) or "Registry empty.")
        elif lowered == "gaps":
            gaps = db.gaps(limit=5)
            say("\n".join(f"#{g['id']} {g['name']}: {', '.join(g['issues'])}" for g in gaps) or "No obvious gaps.")
        elif lowered.startswith("tool "):
            matches = db.search(text[5:].strip(), limit=3)
            say("\n\n".join(_format_resource(r) for r in matches) if matches else "No matching tool.")
        else:
            say("I keep structured studio records. Try `tool <name>`, `status`, or `gaps`. Deep research stays in ChatGPT.")

    return app


def main() -> None:
    settings = Settings.from_env()
    if not settings.slack_app_token:
        raise RuntimeError("SLACK_APP_TOKEN is required for Socket Mode")
    app = build_app(settings)
    SocketModeHandler(app, settings.slack_app_token).start()


if __name__ == "__main__":
    main()

from __future__ import annotations

import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from .config import Settings
from .db import LibrarianDB


def _wiki_link(settings: Settings, wiki_path: str | None) -> str | None:
    if not wiki_path:
        return None
    rel = wiki_path.removeprefix("docs/").removesuffix(".md")
    return f"{settings.wiki_base_url}/{rel}/"


def _format_resource(settings: Settings, r) -> str:
    license_value = r.code_license or r.github_license or "unknown"
    lines = [
        f"*{r.name}*",
        f"License: `{license_value}` | Category: `{r.category}`",
        f"Official: {r.url}",
    ]
    if r.primary_video_url:
        lines.append(f"Video: {r.primary_video_url}")
    docs = r.doc_url_list()
    if docs:
        lines.append("Docs: " + ", ".join(docs[:3]))
    lesson = _wiki_link(settings, r.lesson_wiki_path)
    if lesson:
        lines.append(f"Lesson: {lesson}")
    if r.evidence_path:
        lines.append(f"Evidence folder: `{r.evidence_path}`")
    if r.academy_track:
        lines.append(f"Academy track: `{r.academy_track}`")
    return "\n".join(lines)


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
        respond("\n\n".join(_format_resource(settings, r) for r in matches))

    @app.command("/breedstatus")
    def breedstatus(ack, respond):
        ack()
        db = _open_db(settings)
        resources = db.list(limit=500)
        if not resources:
            respond("The Librarian registry is empty.")
            return
        with_video = sum(1 for r in resources if r.primary_video_url)
        with_docs = sum(1 for r in resources if r.doc_url_list())
        with_lesson = sum(1 for r in resources if r.lesson_wiki_path)
        respond(
            "*Breedables Librarian evidence status*\n"
            f"• Tools registered: {len(resources)}\n"
            f"• With video: {with_video}\n"
            f"• With official docs: {with_docs}\n"
            f"• With wiki lesson: {with_lesson}\n"
            f"• Wiki: {settings.wiki_base_url}/"
        )

    @app.command("/breedgaps")
    def breedgaps(ack, respond):
        ack()
        db = _open_db(settings)
        gaps = db.evidence_gaps(repo_root=settings.repo_root, limit=10)
        if not gaps:
            respond("No evidence gaps found in the registry.")
            return
        lines = ["*Top evidence gaps* (wiki-first)"]
        for item in gaps:
            lesson = _wiki_link(settings, item.get("lesson_wiki_path"))
            suffix = f" → {lesson}" if lesson else ""
            lines.append(f"• #{item['id']} *{item['name']}*: {', '.join(item['issues'])}{suffix}")
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
            resources = db.list(limit=500)
            with_lesson = sum(1 for r in resources if r.lesson_wiki_path)
            say(f"tools:{len(resources)} with_lesson:{with_lesson} wiki:{settings.wiki_base_url}/")
        elif lowered == "gaps":
            gaps = db.evidence_gaps(repo_root=settings.repo_root, limit=5)
            say(
                "\n".join(
                    f"#{g['id']} {g['name']}: {', '.join(g['issues'])}"
                    for g in gaps
                )
                or "No evidence gaps."
            )
        elif lowered.startswith("tool "):
            matches = db.search(text[5:].strip(), limit=3)
            say(
                "\n\n".join(_format_resource(settings, r) for r in matches)
                if matches
                else "No matching tool."
            )
        else:
            say(
                "I link tools to wiki lessons and evidence folders. "
                f"Try `tool <name>`, `status`, or `gaps`. Full wiki: {settings.wiki_base_url}/"
            )

    return app


def main() -> None:
    settings = Settings.from_env()
    if not settings.slack_app_token:
        raise RuntimeError("SLACK_APP_TOKEN is required for Socket Mode")
    app = build_app(settings)
    SocketModeHandler(app, settings.slack_app_token).start()


if __name__ == "__main__":
    main()

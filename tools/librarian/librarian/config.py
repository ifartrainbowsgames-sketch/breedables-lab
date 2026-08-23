from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    db_path: Path
    github_token: str | None
    slack_bot_token: str | None
    slack_app_token: str | None

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        return cls(
            db_path=Path(os.getenv("LIBRARIAN_DB_PATH", ".data/librarian.sqlite3")),
            github_token=os.getenv("GITHUB_TOKEN") or None,
            slack_bot_token=os.getenv("SLACK_BOT_TOKEN") or None,
            slack_app_token=os.getenv("SLACK_APP_TOKEN") or None,
        )

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _default_repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "mkdocs.yml").is_file():
            return parent
    return Path.cwd()


@dataclass(frozen=True)
class Settings:
    db_path: Path
    github_token: str | None
    slack_bot_token: str | None
    slack_app_token: str | None
    repo_root: Path
    wiki_base_url: str

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        return cls(
            db_path=Path(os.getenv("LIBRARIAN_DB_PATH", ".data/librarian.sqlite3")),
            github_token=os.getenv("GITHUB_TOKEN") or None,
            slack_bot_token=os.getenv("SLACK_BOT_TOKEN") or None,
            slack_app_token=os.getenv("SLACK_APP_TOKEN") or None,
            repo_root=Path(os.getenv("BREEDABLES_REPO_ROOT", _default_repo_root())),
            wiki_base_url=os.getenv(
                "WIKI_BASE_URL",
                "https://ifartrainbowsgames-sketch.github.io/breedables-lab",
            ).rstrip("/"),
        )

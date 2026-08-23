from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from .normalize import canonical_name, canonical_url, github_repo_from_url

COMMERCIAL_TYPES = {
    "OPEN_SOURCE",
    "FREE_CLOSED_SOURCE",
    "FREEMIUM",
    "PAID_COMMERCIAL",
    "RESEARCH_ONLY",
    "OPEN_CONTENT_CC0",
    "UNKNOWN",
}

STATUSES = {
    "DISCOVERED",
    "REVIEWING",
    "EXPERIMENTAL",
    "USE_NOW",
    "USE_LATER",
    "APPROVED",
    "REJECTED",
    "SUPERSEDED",
}


@dataclass
class Resource:
    id: int
    name: str
    canonical_name: str
    url: str
    canonical_url: str
    category: str
    commercial_type: str
    code_license: str | None
    model_license: str | None
    asset_license: str | None
    output_rights: str | None
    dependency_risk: str | None
    status: str
    notes: str | None
    source_type: str | None
    http_status: int | None
    last_checked_at: str | None
    github_full_name: str | None
    github_archived: int | None
    github_stars: int | None
    github_pushed_at: str | None
    github_license: str | None
    primary_video_url: str | None
    doc_urls: str | None
    lesson_wiki_path: str | None
    evidence_path: str | None
    license_note_path: str | None
    academy_track: str | None
    last_evidence_review: str | None
    created_at: str
    updated_at: str

    def as_dict(self) -> dict:
        data = asdict(self)
        if data["github_archived"] is not None:
            data["github_archived"] = bool(data["github_archived"])
        if data["doc_urls"]:
            try:
                data["doc_urls"] = json.loads(data["doc_urls"])
            except json.JSONDecodeError:
                pass
        return data

    def doc_url_list(self) -> list[str]:
        if not self.doc_urls:
            return []
        try:
            parsed = json.loads(self.doc_urls)
        except json.JSONDecodeError:
            return [u.strip() for u in self.doc_urls.split(",") if u.strip()]
        return parsed if isinstance(parsed, list) else []


class LibrarianDB:
    def __init__(self, path: Path | str):
        self.path = Path(path)

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def init(self) -> None:
        with self.connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS resources (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    canonical_name TEXT NOT NULL,
                    url TEXT NOT NULL,
                    canonical_url TEXT NOT NULL UNIQUE,
                    category TEXT NOT NULL DEFAULT 'other',
                    commercial_type TEXT NOT NULL DEFAULT 'UNKNOWN',
                    code_license TEXT,
                    model_license TEXT,
                    asset_license TEXT,
                    output_rights TEXT,
                    dependency_risk TEXT,
                    status TEXT NOT NULL DEFAULT 'DISCOVERED',
                    notes TEXT,
                    source_type TEXT,
                    http_status INTEGER,
                    last_checked_at TEXT,
                    github_full_name TEXT,
                    github_archived INTEGER,
                    github_stars INTEGER,
                    github_pushed_at TEXT,
                    github_license TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );

                CREATE INDEX IF NOT EXISTS idx_resources_name
                ON resources(canonical_name);

                CREATE INDEX IF NOT EXISTS idx_resources_status
                ON resources(status);

                CREATE INDEX IF NOT EXISTS idx_resources_category
                ON resources(category);

                CREATE INDEX IF NOT EXISTS idx_resources_github_full_name
                ON resources(github_full_name);
                """
            )
            self._migrate_evidence_columns(conn)

    _EVIDENCE_COLUMNS: tuple[tuple[str, str], ...] = (
        ("primary_video_url", "TEXT"),
        ("doc_urls", "TEXT"),
        ("lesson_wiki_path", "TEXT"),
        ("evidence_path", "TEXT"),
        ("license_note_path", "TEXT"),
        ("academy_track", "TEXT"),
        ("last_evidence_review", "TEXT"),
    )

    def _migrate_evidence_columns(self, conn: sqlite3.Connection) -> None:
        existing = {row[1] for row in conn.execute("PRAGMA table_info(resources)").fetchall()}
        for name, typedef in self._EVIDENCE_COLUMNS:
            if name not in existing:
                conn.execute(f"ALTER TABLE resources ADD COLUMN {name} {typedef}")

    def add(
        self,
        *,
        name: str,
        url: str,
        category: str = "other",
        commercial_type: str = "UNKNOWN",
        code_license: str | None = None,
        model_license: str | None = None,
        asset_license: str | None = None,
        output_rights: str | None = None,
        dependency_risk: str | None = None,
        status: str = "DISCOVERED",
        notes: str | None = None,
        source_type: str | None = None,
    ) -> tuple[Resource, bool]:
        commercial_type = commercial_type.upper()
        status = status.upper()
        if commercial_type not in COMMERCIAL_TYPES:
            raise ValueError(f"Unknown commercial_type: {commercial_type}")
        if status not in STATUSES:
            raise ValueError(f"Unknown status: {status}")

        cname = canonical_name(name)
        curl = canonical_url(url)
        now = datetime.now(timezone.utc).isoformat()
        github_full_name = github_repo_from_url(curl)

        with self.connect() as conn:
            existing = conn.execute(
                "SELECT * FROM resources WHERE canonical_url = ? ORDER BY id LIMIT 1",
                (curl,),
            ).fetchone()

            if not existing and github_full_name:
                existing = conn.execute(
                    "SELECT * FROM resources WHERE github_full_name = ? ORDER BY id LIMIT 1",
                    (github_full_name,),
                ).fetchone()

            if existing:
                updates = {
                    "url": url,
                    "canonical_url": curl,
                    "category": category or existing["category"],
                    "commercial_type": commercial_type if commercial_type != "UNKNOWN" else existing["commercial_type"],
                    "code_license": code_license or existing["code_license"],
                    "model_license": model_license or existing["model_license"],
                    "asset_license": asset_license or existing["asset_license"],
                    "output_rights": output_rights or existing["output_rights"],
                    "dependency_risk": dependency_risk or existing["dependency_risk"],
                    "status": status if status != "DISCOVERED" else existing["status"],
                    "notes": notes or existing["notes"],
                    "source_type": source_type or existing["source_type"],
                    "github_full_name": github_full_name or existing["github_full_name"],
                    "updated_at": now,
                }
                conn.execute(
                    """
                    UPDATE resources
                    SET url=:url, canonical_url=:canonical_url, category=:category,
                        commercial_type=:commercial_type, code_license=:code_license,
                        model_license=:model_license, asset_license=:asset_license,
                        output_rights=:output_rights, dependency_risk=:dependency_risk,
                        status=:status, notes=:notes, source_type=:source_type,
                        github_full_name=:github_full_name, updated_at=:updated_at
                    WHERE id=:id
                    """,
                    {**updates, "id": existing["id"]},
                )
                row = conn.execute("SELECT * FROM resources WHERE id = ?", (existing["id"],)).fetchone()
                return self._row(row), False

            cur = conn.execute(
                """
                INSERT INTO resources (
                    name, canonical_name, url, canonical_url, category,
                    commercial_type, code_license, model_license, asset_license,
                    output_rights, dependency_risk, status, notes, source_type,
                    github_full_name, created_at, updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    name.strip(),
                    cname,
                    url.strip(),
                    curl,
                    category,
                    commercial_type,
                    code_license,
                    model_license,
                    asset_license,
                    output_rights,
                    dependency_risk,
                    status,
                    notes,
                    source_type,
                    github_full_name,
                    now,
                    now,
                ),
            )
            row = conn.execute("SELECT * FROM resources WHERE id = ?", (cur.lastrowid,)).fetchone()
            return self._row(row), True

    def list(self, *, status: str | None = None, category: str | None = None, limit: int = 100) -> list[Resource]:
        clauses, params = [], []
        if status:
            clauses.append("status = ?")
            params.append(status.upper())
        if category:
            clauses.append("category = ?")
            params.append(category)
        where = f" WHERE {' AND '.join(clauses)}" if clauses else ""
        sql = f"SELECT * FROM resources{where} ORDER BY updated_at DESC LIMIT ?"
        params.append(limit)
        with self.connect() as conn:
            rows = conn.execute(sql, params).fetchall()
        return [self._row(row) for row in rows]

    def get(self, resource_id: int) -> Resource | None:
        with self.connect() as conn:
            row = conn.execute("SELECT * FROM resources WHERE id = ?", (resource_id,)).fetchone()
        return self._row(row) if row else None

    def search(self, query: str, limit: int = 10) -> list[Resource]:
        q = f"%{canonical_name(query)}%"
        with self.connect() as conn:
            rows = conn.execute(
                """
                SELECT * FROM resources
                WHERE canonical_name LIKE ? OR lower(category) LIKE lower(?) OR lower(notes) LIKE lower(?)
                ORDER BY updated_at DESC LIMIT ?
                """,
                (q, f"%{query}%", f"%{query}%", limit),
            ).fetchall()
        return [self._row(row) for row in rows]

    def update_check(self, resource_id: int, **fields) -> Resource:
        allowed = {
            "http_status",
            "last_checked_at",
            "github_full_name",
            "github_archived",
            "github_stars",
            "github_pushed_at",
            "github_license",
        }
        unknown = set(fields) - allowed
        if unknown:
            raise ValueError(f"Unsupported fields: {sorted(unknown)}")
        fields["updated_at"] = datetime.now(timezone.utc).isoformat()
        assignments = ", ".join(f"{key} = :{key}" for key in fields)
        with self.connect() as conn:
            conn.execute(
                f"UPDATE resources SET {assignments} WHERE id = :id",
                {**fields, "id": resource_id},
            )
            row = conn.execute("SELECT * FROM resources WHERE id = ?", (resource_id,)).fetchone()
        if not row:
            raise KeyError(resource_id)
        return self._row(row)

    def update_evidence(
        self,
        resource_id: int,
        *,
        primary_video_url: str | None = None,
        doc_urls: list[str] | str | None = None,
        lesson_wiki_path: str | None = None,
        evidence_path: str | None = None,
        license_note_path: str | None = None,
        academy_track: str | None = None,
        last_evidence_review: str | None = None,
        clear_missing: bool = False,
    ) -> Resource:
        fields: dict[str, object] = {}
        if clear_missing or primary_video_url is not None:
            fields["primary_video_url"] = primary_video_url
        if clear_missing or doc_urls is not None:
            if doc_urls is None:
                fields["doc_urls"] = None
            elif isinstance(doc_urls, list):
                fields["doc_urls"] = json.dumps(doc_urls)
            else:
                fields["doc_urls"] = doc_urls
        if clear_missing or lesson_wiki_path is not None:
            fields["lesson_wiki_path"] = lesson_wiki_path
        if clear_missing or evidence_path is not None:
            fields["evidence_path"] = evidence_path
        if clear_missing or license_note_path is not None:
            fields["license_note_path"] = license_note_path
        if clear_missing or academy_track is not None:
            fields["academy_track"] = academy_track
        if clear_missing or last_evidence_review is not None:
            fields["last_evidence_review"] = last_evidence_review
        if not fields:
            raise ValueError("No evidence fields provided")
        fields["updated_at"] = datetime.now(timezone.utc).isoformat()
        assignments = ", ".join(f"{key} = :{key}" for key in fields)
        with self.connect() as conn:
            conn.execute(
                f"UPDATE resources SET {assignments} WHERE id = :id",
                {**fields, "id": resource_id},
            )
            row = conn.execute("SELECT * FROM resources WHERE id = ?", (resource_id,)).fetchone()
        if not row:
            raise KeyError(resource_id)
        return self._row(row)

    def _resource_evidence_issues(self, resource: Resource, repo_root: Path | None) -> list[str]:
        issues: list[str] = []
        if not resource.primary_video_url:
            issues.append("missing primary video")
        if not resource.doc_url_list():
            issues.append("missing official doc links")
        if not resource.lesson_wiki_path:
            issues.append("missing wiki lesson link")
        elif repo_root is not None:
            lesson = repo_root / resource.lesson_wiki_path
            if not lesson.is_file():
                issues.append(f"wiki lesson missing on disk: {resource.lesson_wiki_path}")
        if not resource.evidence_path:
            issues.append("missing evidence folder path")
        elif repo_root is not None:
            evidence = repo_root / resource.evidence_path
            if not evidence.is_dir():
                issues.append(f"evidence folder missing: {resource.evidence_path}")
            elif not any(evidence.iterdir()):
                issues.append(f"evidence folder empty: {resource.evidence_path}")
        if resource.commercial_type in {"UNKNOWN", "PAID_COMMERCIAL", "FREEMIUM"} and not resource.license_note_path:
            issues.append("license note path recommended")
        return issues

    def evidence_gaps(self, *, repo_root: Path | None = None, limit: int = 25) -> list[dict]:
        gaps: list[dict] = []
        for resource in self.list(limit=500):
            issues = self._resource_evidence_issues(resource, repo_root)
            if issues:
                gaps.append(
                    {
                        "kind": "resource",
                        "id": resource.id,
                        "name": resource.name,
                        "academy_track": resource.academy_track,
                        "lesson_wiki_path": resource.lesson_wiki_path,
                        "issues": issues,
                    }
                )
            if len(gaps) >= limit:
                break
        return gaps

    def registry_gaps(self, limit: int = 25) -> list[dict]:
        rows = self.list(limit=500)
        gaps = []
        for r in rows:
            issues = []
            if r.http_status is None:
                issues.append("link not checked")
            elif r.http_status >= 400:
                issues.append(f"link HTTP {r.http_status}")
            if r.commercial_type == "UNKNOWN":
                issues.append("commercial type unknown")
            if r.commercial_type == "OPEN_SOURCE" and not (r.code_license or r.github_license):
                issues.append("open-source license missing")
            if issues:
                gaps.append({"kind": "registry", "id": r.id, "name": r.name, "issues": issues})
            if len(gaps) >= limit:
                break
        return gaps

    def gaps(self, limit: int = 25, repo_root: Path | None = None) -> list[dict]:
        return self.evidence_gaps(repo_root=repo_root, limit=limit)

    def status_counts(self) -> dict[str, int]:
        with self.connect() as conn:
            rows = conn.execute("SELECT status, COUNT(*) AS n FROM resources GROUP BY status ORDER BY status").fetchall()
        return {row["status"]: row["n"] for row in rows}

    def export_json(self) -> str:
        return json.dumps([r.as_dict() for r in self.list(limit=100000)], indent=2, sort_keys=True)

    @staticmethod
    def _row(row: sqlite3.Row | None) -> Resource:
        if row is None:
            raise ValueError("row is None")
        data = dict(row)
        for key in (
            "primary_video_url",
            "doc_urls",
            "lesson_wiki_path",
            "evidence_path",
            "license_note_path",
            "academy_track",
            "last_evidence_review",
        ):
            data.setdefault(key, None)
        return Resource(**data)

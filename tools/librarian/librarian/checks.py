from __future__ import annotations

from datetime import datetime, timezone

import httpx

from .db import LibrarianDB, Resource
from .normalize import github_repo_from_url


DEFAULT_TIMEOUT = 12.0


def check_http(url: str, timeout: float = DEFAULT_TIMEOUT) -> int:
    headers = {"User-Agent": "BreedablesStudioLibrarian/0.1"}
    with httpx.Client(follow_redirects=True, timeout=timeout, headers=headers) as client:
        try:
            response = client.head(url)
            if response.status_code in {405, 403}:
                response = client.get(url)
        except httpx.HTTPError:
            return 0
    return response.status_code


def github_metadata(full_name: str, token: str | None = None, timeout: float = DEFAULT_TIMEOUT) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "BreedablesStudioLibrarian/0.1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = f"https://api.github.com/repos/{full_name}"
    with httpx.Client(timeout=timeout, headers=headers) as client:
        response = client.get(url)
        response.raise_for_status()
        data = response.json()

    license_obj = data.get("license") or {}
    return {
        "github_full_name": data.get("full_name") or full_name,
        "github_archived": bool(data.get("archived")),
        "github_stars": int(data.get("stargazers_count") or 0),
        "github_pushed_at": data.get("pushed_at"),
        "github_license": license_obj.get("spdx_id") or license_obj.get("name"),
    }


def check_resource(db: LibrarianDB, resource: Resource, github_token: str | None = None) -> Resource:
    status = check_http(resource.url)
    update = {
        "http_status": status,
        "last_checked_at": datetime.now(timezone.utc).isoformat(),
    }

    full_name = resource.github_full_name or github_repo_from_url(resource.url)
    if full_name:
        try:
            update.update(github_metadata(full_name, github_token))
        except httpx.HTTPError:
            update["github_full_name"] = full_name

    return db.update_check(resource.id, **update)

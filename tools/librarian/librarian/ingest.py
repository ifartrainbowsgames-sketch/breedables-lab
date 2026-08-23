from __future__ import annotations

import xml.etree.ElementTree as ET
from dataclasses import dataclass

import httpx

from .db import LibrarianDB


@dataclass(frozen=True)
class FeedItem:
    title: str
    url: str


def parse_feed(xml_text: str) -> list[FeedItem]:
    root = ET.fromstring(xml_text)
    items: list[FeedItem] = []

    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if title and link:
            items.append(FeedItem(title, link))

    if items:
        return items

    ns = {"a": "http://www.w3.org/2005/Atom"}
    for entry in root.findall(".//a:entry", ns):
        title = (entry.findtext("a:title", default="", namespaces=ns) or "").strip()
        link = ""
        for node in entry.findall("a:link", ns):
            href = (node.attrib.get("href") or "").strip()
            rel = (node.attrib.get("rel") or "alternate").strip()
            if href and rel == "alternate":
                link = href
                break
            if href and not link:
                link = href
        if title and link:
            items.append(FeedItem(title, link))

    return items


def ingest_feed(
    db: LibrarianDB,
    feed_url: str,
    *,
    category: str = "research",
    limit: int = 25,
    timeout: float = 15.0,
) -> dict:
    headers = {"User-Agent": "BreedablesStudioLibrarian/0.1"}
    with httpx.Client(follow_redirects=True, timeout=timeout, headers=headers) as client:
        response = client.get(feed_url)
        response.raise_for_status()
        items = parse_feed(response.text)[:limit]

    created = 0
    merged = 0
    for item in items:
        _, was_created = db.add(
            name=item.title,
            url=item.url,
            category=category,
            commercial_type="UNKNOWN",
            status="DISCOVERED",
            source_type=f"feed:{feed_url}",
            notes="Discovered from RSS/Atom feed. Requires research/verification before recommendation.",
        )
        created += int(was_created)
        merged += int(not was_created)
    return {"seen": len(items), "created": created, "merged": merged}


def github_search(
    db: LibrarianDB,
    query: str,
    *,
    token: str | None = None,
    category: str = "github-discovery",
    limit: int = 10,
    timeout: float = 15.0,
) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "BreedablesStudioLibrarian/0.1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": min(max(limit, 1), 100),
    }
    with httpx.Client(timeout=timeout, headers=headers) as client:
        response = client.get("https://api.github.com/search/repositories", params=params)
        response.raise_for_status()
        data = response.json()

    created = 0
    merged = 0
    for repo in data.get("items", [])[:limit]:
        license_obj = repo.get("license") or {}
        license_id = license_obj.get("spdx_id")
        description = (repo.get("description") or "").strip()
        notes = "Discovered via GitHub search; review project scope, full license/dependencies, model/assets, and commercial fit."
        if description:
            notes += f" Description: {description}"
        _, was_created = db.add(
            name=repo.get("name") or repo.get("full_name") or "GitHub repository",
            url=repo["html_url"],
            category=category,
            commercial_type="UNKNOWN",
            code_license=license_id if license_id and license_id != "NOASSERTION" else None,
            status="DISCOVERED",
            source_type=f"github-search:{query}",
            notes=notes,
        )
        created += int(was_created)
        merged += int(not was_created)

    return {
        "total_count": int(data.get("total_count") or 0),
        "seen": min(len(data.get("items", [])), limit),
        "created": created,
        "merged": merged,
    }

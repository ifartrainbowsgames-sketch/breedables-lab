"""What the wiki currently looks like, in a form a model can act on.

Before this existed, Kimi was handed one page and asked to improve it — blind to
everything around it. That is why it invented link targets and why nothing
stopped it proposing a topic that already had a home elsewhere.

This module gives it three things:

* **The page index** — every page that exists, its title, type and the exact
  relative link to reach it *from the page being edited*. A model cannot invent
  a path when the correct one is in front of it.
* **The public URLs** — the GitHub blob and the published GitHub Pages address
  for the page, so its output is traceable to something real.
* **The architecture** — the sections and what each is for, so a page lands in
  the right place by construction.
"""

from __future__ import annotations

import posixpath
import re
import subprocess
from pathlib import Path
from typing import Any

from .wiki_lint import parse_frontmatter
from .wiki_schema import SECTIONS

#: Keep the index affordable in tokens; the wiki is ~85 pages so this is ample.
MAX_INDEXED_PAGES = 200


def git_remote_url(repo_root: Path) -> str:
    try:
        out = subprocess.run(["git", "remote", "get-url", "origin"],
                             cwd=str(repo_root), capture_output=True, timeout=15)
        url = out.stdout.decode("utf-8", errors="replace").strip()
    except (OSError, subprocess.SubprocessError):
        return ""
    if url.startswith("git@github.com:"):
        url = "https://github.com/" + url.split(":", 1)[1]
    return re.sub(r"\.git$", "", url)


def current_branch(repo_root: Path) -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                             cwd=str(repo_root), capture_output=True, timeout=15)
        return out.stdout.decode("utf-8", errors="replace").strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def published_url(wiki_base_url: str, rel: str) -> str:
    """The GitHub Pages address a docs-relative page is served at."""
    slug = rel[:-3]  # drop .md
    if slug.endswith("/index"):
        slug = slug[: -len("/index")]
    elif slug == "index":
        slug = ""
    return f"{wiki_base_url.rstrip('/')}/{slug}/".replace("//", "/").replace(":/", "://")


def source_url(repo_url: str, branch: str, rel: str) -> str:
    if not repo_url:
        return ""
    return f"{repo_url}/blob/{branch or 'main'}/docs/{rel}"


def page_index(repo_root: Path, *, relative_to: str = "") -> list[dict[str, str]]:
    """Every page, with the link text that reaches it from ``relative_to``."""
    docs = repo_root / "docs"
    if not docs.is_dir():
        return []
    from_dir = posixpath.dirname(relative_to)
    rows: list[dict[str, str]] = []
    for path in sorted(docs.rglob("*.md")):
        rel = path.relative_to(docs).as_posix()
        if rel.startswith("meta/"):
            continue
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        title = fm.get("title") or (
            m.group(1) if (m := re.search(r"^# +(.+)$", body, re.M)) else rel)
        rows.append({
            "path": rel,
            "title": title,
            "type": fm.get("type", ""),
            "section": fm.get("section", ""),
            "link_from_here": posixpath.relpath(rel, from_dir if from_dir else "."),
        })
    return rows[:MAX_INDEXED_PAGES]


def architecture() -> list[dict[str, str]]:
    return [{"folder": f"{s.slug}/", "section": s.title, "answers": s.question}
            for s in SECTIONS if s.slug != "meta"]


def build_repo_context(repo_root: Path, wiki_base_url: str, *,
                       editing: str = "") -> dict[str, Any]:
    """The full picture handed to the model alongside a task."""
    repo_url = git_remote_url(repo_root)
    branch = current_branch(repo_root)
    ctx: dict[str, Any] = {
        "repository": repo_url,
        "published_site": wiki_base_url,
        "branch": branch,
        "architecture": architecture(),
        "existing_pages": page_index(repo_root, relative_to=editing),
    }
    if editing:
        ctx["editing"] = {
            "path": f"docs/{editing}",
            "source_url": source_url(repo_url, branch, editing),
            "published_url": published_url(wiki_base_url, editing),
        }
    return ctx


CONTEXT_NOTE = """You are editing a real, published wiki. The context includes:

* `repository` and `published_site` — where this page will actually appear.
* `editing.published_url` — the live address of the page you are changing.
* `existing_pages` — EVERY page that already exists. Two rules follow from it:
  1. To link to a page, copy its `link_from_here` value verbatim. Do not
     construct a path yourself and do not invent one; a link that does not
     resolve is rejected and the whole call is wasted.
  2. If a topic already has a page in this list, do NOT create a second one.
     Link to the existing page instead. Every topic has exactly one home.
* `architecture` — which folder owns which subject, and the question it answers.
"""

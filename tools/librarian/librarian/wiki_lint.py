"""Structural linter for the wiki.

Enforces the information architecture defined in :mod:`wiki_schema`. Runs in CI
and before any automated page write, so neither a human nor Kimi can put a page
in the wrong place or reintroduce the layout problems this wiki has already had.

Every rule here exists because the wiki actually broke that way once.
"""

from __future__ import annotations

import collections
import posixpath
import re
from pathlib import Path
from typing import Any

from .wiki_schema import (
    FORBIDDEN_LINK_TEXT,
    LintReport,
    MAX_TOC_ENTRIES,
    PATH_FORBIDDEN_HEADINGS,
    QUESTION_REQUIRED_TYPES,
    REQUIRED_FRONTMATTER,
    ROOT_PAGES,
    SECTIONS_BY_SLUG,
    TYPE_FOLDERS,
)

_FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)
_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter dict, body). Deliberately tiny — no YAML dependency."""
    m = _FM.match(text)
    if not m:
        return {}, text
    data: dict[str, str] = {}
    for line in m.group(1).split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data, text[m.end():]


def headings(body: str, levels: tuple[int, ...] = (2, 3)) -> list[tuple[int, str]]:
    """H2/H3 headings, skipping fenced code blocks."""
    out: list[tuple[int, str]] = []
    fence = False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6}) +(.+?)\s*(?:\{#[^}]*\})?\s*$", line)
        if m and len(m.group(1)) in levels:
            out.append((len(m.group(1)), m.group(2).strip()))
    return out


def lint_page(rel: str, text: str, report: LintReport,
              known_pages: set[str] | None = None) -> None:
    """Validate one page.

    ``known_pages`` is the set of docs-relative page paths that exist. When
    supplied, every relative link is resolved and a dangling target is an
    error — this is the check that stops a generated page shipping a link the
    model invented or wrote root-relative instead of page-relative.
    """
    fm, body = parse_frontmatter(text)
    parts = rel.split("/")

    is_root = rel in ROOT_PAGES
    is_meta = parts[0] == "meta"

    # ---- front matter ----------------------------------------------------
    for key in REQUIRED_FRONTMATTER:
        # root pages sit outside the section tree, so they declare no section
        if key == "section" and is_root:
            continue
        if key not in fm:
            report.add(rel, "frontmatter", f"missing required key '{key}'")
    ptype = fm.get("type", "")
    section = fm.get("section", "")

    # ---- placement -------------------------------------------------------
    if is_root:
        pass  # root pages are exempt from section placement
    elif not parts[:-1]:
        report.add(rel, "placement",
                   "page sits at docs/ root but is not a declared root page")
    else:
        folder_section = parts[0]
        if section and section != folder_section:
            report.add(rel, "placement",
                       f"declares section '{section}' but lives in '{folder_section}/'")
        if folder_section not in SECTIONS_BY_SLUG:
            report.add(rel, "placement",
                       f"'{folder_section}/' is not a section in wiki_schema.SECTIONS")
        else:
            sec = SECTIONS_BY_SLUG[folder_section]
            if ptype and ptype not in sec.allows:
                report.add(rel, "placement",
                           f"type '{ptype}' is not allowed in {sec.title} "
                           f"(allowed: {', '.join(sec.allows)})")

    # ---- type must match its folder -------------------------------------
    if ptype in TYPE_FOLDERS:
        required = TYPE_FOLDERS[ptype]
        if required and required not in parts[:-1]:
            report.add(rel, "type-folder",
                       f"type '{ptype}' must live in a '{required}/' folder")
    elif ptype:
        report.add(rel, "type-folder", f"unknown page type '{ptype}'")

    # ---- one question per index page ------------------------------------
    if ptype in QUESTION_REQUIRED_TYPES and "question" not in fm:
        report.add(rel, "frontmatter",
                   "index pages must declare the single question they answer",
                   severity="warning")

    hs = headings(body)

    # ---- duplicate headings ---------------------------------------------
    dupes = [h for h, n in collections.Counter(t for _, t in hs).items() if n > 1]
    if dupes:
        report.add(rel, "duplicate-heading",
                   "repeated headings flood the table of contents: "
                   + ", ".join(sorted(dupes)[:4])
                   + " — use **bold labels** instead")

    # ---- table of contents size -----------------------------------------
    # meta/ holds archived records; they are out of the nav and not read linearly
    if len(hs) > MAX_TOC_ENTRIES and not is_meta:
        report.add(rel, "toc-size",
                   f"{len(hs)} table-of-contents entries (max {MAX_TOC_ENTRIES}) "
                   "— split the page or demote headings to bold labels")

    # ---- internal codes in reader-facing text ---------------------------
    title = fm.get("title") or (
        re.search(r"^# +(.+)$", body, re.M).group(1) if re.search(r"^# +(.+)$", body, re.M) else "")
    if re.match(r"^[AB]\d{2}\b", title.strip()):
        report.add(rel, "internal-code",
                   f"title '{title}' leads with an internal code — codes are folder names only")
    for m in re.finditer(FORBIDDEN_LINK_TEXT, body):
        report.add(rel, "internal-code",
                   f"link text '{m.group(0)}' uses an internal code — use the page's real name")
        break

    # ---- Academy paths link, they do not teach --------------------------
    if ptype == "path":
        for _, h in hs:
            if h.strip().lower().split()[0].rstrip(":—-") in PATH_FORBIDDEN_HEADINGS:
                report.add(rel, "path-duplication",
                           f"path page has a teaching heading '{h}' — paths link to the "
                           "canonical subject page, they never duplicate its content")
                break

    # ---- internal links must actually resolve ---------------------------
    if known_pages is not None:
        page_dir = posixpath.dirname(rel)
        for m in _LINK.finditer(body):
            target = m.group(2)
            if re.match(r"^(https?:|mailto:|#|/)", target):
                continue
            target = target.split("#", 1)[0]
            if not target or not target.endswith(".md"):
                continue
            resolved = posixpath.normpath(posixpath.join(page_dir, target))
            if resolved not in known_pages:
                report.add(rel, "dead-link",
                           f"link '{m.group(2)}' resolves to '{resolved}', which does "
                           "not exist — use a path relative to this page")

    # ---- run-on metadata blocks -----------------------------------------
    lines = body.split("\n")
    for i, line in enumerate(lines[:12]):
        if (line.strip().startswith("**") and not line.endswith("  ")
                and not line.endswith("\\")
                and i + 1 < len(lines) and lines[i + 1].strip().startswith("**")):
            report.add(rel, "run-on-metadata",
                       "bold metadata lines without a trailing double-space collapse "
                       "into one paragraph — use an '!!! info' card",
                       severity="warning")
            break


def find_duplicate_topics(pages: dict[str, str]) -> list[tuple[str, list[str]]]:
    """Same H1 in two places means a topic has two canonical homes."""
    by_title: dict[str, list[str]] = collections.defaultdict(list)
    for rel, text in pages.items():
        _, body = parse_frontmatter(text)
        m = re.search(r"^# +(.+)$", body, re.M)
        if m:
            by_title[m.group(1).strip().lower()].append(rel)
    return [(t, ps) for t, ps in sorted(by_title.items()) if len(ps) > 1]


def lint_wiki(repo_root: Path) -> LintReport:
    docs = repo_root / "docs"
    report = LintReport()
    pages: dict[str, str] = {}
    for path in sorted(docs.rglob("*.md")):
        pages[path.relative_to(docs).as_posix()] = path.read_text(
            encoding="utf-8", errors="replace")
    known = set(pages)
    for rel, text in pages.items():
        lint_page(rel, text, report, known_pages=known)

    for title, paths in find_duplicate_topics(pages):
        report.add(paths[0], "duplicate-topic",
                   f"'{title}' is also the title of {', '.join(paths[1:])} — "
                   "every topic needs exactly one canonical home; link instead")

    return report


def format_report(report: LintReport) -> str:
    if not report.findings:
        return "wiki-lint: clean — architecture, headings and placement all valid\n"
    lines = [str(f) for f in report.findings]
    lines.append("")
    lines.append(f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return "\n".join(lines) + "\n"


def lint_summary(repo_root: Path) -> dict[str, Any]:
    """Machine-readable form, for the daily wiki payload and Kimi context."""
    r = lint_wiki(repo_root)
    by_rule: dict[str, int] = collections.Counter(f.rule for f in r.findings)
    return {
        "ok": r.ok,
        "errors": len(r.errors),
        "warnings": len(r.warnings),
        "by_rule": dict(by_rule),
        "findings": [
            {"path": f.path, "rule": f.rule, "message": f.message, "severity": f.severity}
            for f in r.findings[:100]
        ],
    }

"""The wiki's information architecture, as data.

This module is the single source of truth for where a page is allowed to live
and what it must contain. Everything else — the linter, the Kimi page renderer,
the audit — reads from here, so the structure cannot drift by being described
differently in two places.

If you want to change the architecture, change it here first.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Section:
    slug: str
    title: str
    question: str
    #: page types allowed anywhere in this section
    allows: tuple[str, ...]


#: Top-level information architecture. Order matters — it is the nav order.
#:
#: The wiki is organised by *tool*, not by pipeline stage. A pipeline stage is a
#: reading order, and `pipeline.md` already provides it; splitting the pages
#: themselves across stages only scattered each tool over several sections.
SECTIONS: tuple[Section, ...] = (
    Section("academy", "Academy",
            "What should I learn next?",
            ("index", "path", "reference")),
    Section("tools", "Tools",
            "Which tool do I use, and how do I learn it?",
            ("index", "topic", "software")),
    Section("projects", "Studio labs",
            "What do I build to prove I can do it?",
            ("index", "project")),
    Section("second-life", "Second Life Production",
            "How do I get the finished asset into Second Life correctly?",
            ("index", "topic")),
    Section("engineering", "Breedables Engineering",
            "How does the breedable system actually work?",
            ("index", "topic")),
    Section("research", "Research & Tools",
            "What are we currently evaluating?",
            ("index", "reference", "candidate", "software")),
    Section("meta", "Meta",
            "How is this wiki maintained?",
            ("index", "meta")),
)

SECTIONS_BY_SLUG = {s.slug: s for s in SECTIONS}

#: Pages allowed to sit at docs/ root, outside any section.
ROOT_PAGES = ("index.md", "pipeline.md", "roadmap.md")

#: Page types and the folder each must live in, relative to its section.
#: None means "anywhere in the section".
TYPE_FOLDERS: dict[str, str | None] = {
    "index": None,        # a section or sub-folder landing page
    "topic":  None,       # canonical teaching page for one subject
    "software": None,     # a tool hub; the Tools section already scopes it
    "project": "projects",    # hands-on lab ending in committed evidence
    "path": "paths",          # Academy: an ordered reading list, links only
    "reference": None,        # tables and indexes, no teaching
    "candidate": "candidates",  # under evaluation, not approved
    "meta": None,             # about the wiki itself
}

# --------------------------------------------------------------------------
# House style rules. Each is enforced by wiki_lint; the message is what an
# author (human or Kimi) sees when they break it.
# --------------------------------------------------------------------------

#: A page's table of contents must stay scannable.
MAX_TOC_ENTRIES = 25

#: Headings must not repeat within a page — repeated headings flood the TOC.
FORBID_DUPLICATE_HEADINGS = True

#: Internal codes are folder names, never reader-facing text.
FORBIDDEN_TITLE_PATTERNS = (
    (r"^[AB]\d{2}\b", "internal code in the page title — use plain words"),
    (r"^\w+ — .*[A-Z]{2,}.*$", None),  # informational only, not enforced
)

#: Link text must not lead with an internal code either.
FORBIDDEN_LINK_TEXT = r"\[(?:A|B)\d{2}(?:\s|\]|—)"

#: Academy paths link; they never teach. These headings signal teaching content
#: and are not allowed on a `type: path` page.
PATH_FORBIDDEN_HEADINGS = ("watch", "read", "explain", "do", "produce",
                           "outcome", "exercise", "tutorials", "videos")

#: Every page needs these front matter keys.
REQUIRED_FRONTMATTER = ("title", "section", "type")

#: Page types that must additionally declare the one question they answer.
QUESTION_REQUIRED_TYPES = ("index",)


@dataclass
class Finding:
    path: str
    rule: str
    message: str
    severity: str = "error"  # error | warning

    def __str__(self) -> str:
        mark = "ERROR" if self.severity == "error" else "warn "
        return f"{mark}  {self.path}  [{self.rule}] {self.message}"


@dataclass
class LintReport:
    findings: list[Finding] = field(default_factory=list)

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warning"]

    @property
    def ok(self) -> bool:
        return not self.errors

    def add(self, path: str, rule: str, message: str, severity: str = "error") -> None:
        self.findings.append(Finding(path, rule, message, severity))

from pathlib import Path

import pytest

from librarian.wiki_lint import (
    find_duplicate_topics,
    headings,
    lint_page,
    parse_frontmatter,
)
from librarian.wiki_page import PageRejected, render, render_and_write, target_path
from librarian.wiki_schema import LintReport

FM = '---\ntitle: "T"\nsection: modeling\ntype: topic\n---\n'


def rules(rel: str, text: str) -> set[str]:
    r = LintReport()
    lint_page(rel, text, r)
    return {f.rule for f in r.findings}


def test_frontmatter_parsed_without_yaml_dependency():
    fm, body = parse_frontmatter(FM + "# T\n\nbody\n")
    assert fm == {"title": "T", "section": "modeling", "type": "topic"}
    assert body.startswith("# T")


def test_headings_ignore_fenced_code():
    body = "## Real\n\n```markdown\n## Not a heading\n```\n\n### Also real\n"
    assert headings(body) == [(2, "Real"), (3, "Also real")]


def test_duplicate_headings_rejected():
    text = FM + "# T\n\n## Videos\n\na\n\n## Videos\n\nb\n"
    assert "duplicate-heading" in rules("modeling/x.md", text)


def test_clean_page_has_no_findings():
    text = FM + "# T\n\n## One\n\na\n\n## Two\n\nb\n"
    assert rules("modeling/x.md", text) == set()


def test_page_in_wrong_section_rejected():
    text = FM.replace("section: modeling", "section: texturing") + "# T\n"
    assert "placement" in rules("modeling/x.md", text)


def test_software_page_must_live_in_software_folder():
    text = FM.replace("type: topic", "type: software") + "# T\n"
    assert "type-folder" in rules("modeling/blender.md", text)
    assert "type-folder" not in rules("modeling/software/blender.md", text)


def test_unknown_section_folder_rejected():
    text = '---\ntitle: "T"\nsection: tutorials\ntype: topic\n---\n# T\n'
    assert "placement" in rules("tutorials/x.md", text)


def test_internal_code_in_title_rejected():
    text = FM.replace('title: "T"', 'title: "B07 Texture Painting"') + "# B07 Texture Painting\n"
    assert "internal-code" in rules("modeling/x.md", text)


def test_internal_code_in_link_text_rejected():
    text = FM + "# T\n\nSee [A03](../x.md) for detail.\n"
    assert "internal-code" in rules("modeling/x.md", text)


def test_toc_size_limit():
    body = "".join(f"## H{i}\n\ntext\n\n" for i in range(30))
    assert "toc-size" in rules("modeling/x.md", FM + "# T\n\n" + body)


def test_meta_pages_exempt_from_toc_limit():
    body = "".join(f"## H{i}\n\ntext\n\n" for i in range(30))
    text = '---\ntitle: "T"\nsection: meta\ntype: meta\n---\n# T\n\n' + body
    assert "toc-size" not in rules("meta/x.md", text)


def test_root_pages_need_no_section():
    text = ('---\ntitle: "Home"\ntype: index\nquestion: "Where do I start?"\n---\n'
            "# Home\n")
    assert rules("index.md", text) == set()


def test_index_page_without_its_question_is_flagged():
    text = '---\ntitle: "Home"\ntype: index\n---\n# Home\n'
    assert "frontmatter" in rules("index.md", text)


def test_academy_path_may_not_duplicate_teaching_content():
    text = ('---\ntitle: "P"\nsection: academy\ntype: path\n---\n'
            "# P\n\n## Watch\n\nvideos here\n")
    assert "path-duplication" in rules("academy/paths/p.md", text)


def test_run_on_metadata_warned():
    text = FM + "# T\n\n**Stage:** one\n**Prereq:** two\n"
    assert "run-on-metadata" in rules("modeling/x.md", text)


def test_duplicate_topic_across_pages():
    pages = {
        "modeling/retopology.md": FM + "# Retopology\n",
        "research/retopology.md": FM + "# Retopology\n",
    }
    dupes = find_duplicate_topics(pages)
    assert dupes and dupes[0][0] == "retopology"
    assert len(dupes[0][1]) == 2


# ---------------------------------------------------------------- wiki_page

BASE = {
    "title": "Baking high to low",
    "section": "texturing",
    "type": "topic",
    "summary": "Transfer detail from high poly to low poly.",
    "sections": [{"heading": "Why", "body": "because"}],
}


def test_target_path_is_derived_not_chosen():
    assert target_path(BASE) == "texturing/baking-high-to-low.md"
    assert target_path({**BASE, "type": "software"}) == "texturing/software/baking-high-to-low.md"


def test_render_emits_frontmatter_and_house_style():
    md = render({**BASE, "studio_pick": "Blender", "evidence_folder": "training/x/"})
    assert md.startswith("---\n")
    assert "section: texturing" in md
    assert '!!! tip "Studio pick"' in md
    assert '!!! info "About this page"' in md


def test_free_and_paid_tools_render_as_tabs():
    md = render({**BASE,
                 "tools_free": [{"title": "Blender", "url": "u", "best_for": "b"}],
                 "tools_paid": [{"title": "Painter", "url": "u", "best_for": "b"}]})
    assert '=== "Free tools"' in md and '=== "Paid tools"' in md


def test_unknown_section_refused():
    with pytest.raises(PageRejected):
        target_path({**BASE, "section": "tutorials"})


def test_type_not_allowed_in_section_refused():
    with pytest.raises(PageRejected):
        target_path({**BASE, "type": "candidate"})


def test_write_refused_when_generated_page_is_invalid(tmp_path):
    bad = {**BASE, "sections": [{"heading": "Same", "body": "a"},
                                {"heading": "Same", "body": "b"}]}
    with pytest.raises(PageRejected):
        render_and_write(tmp_path, bad, dry_run=True)


def test_valid_page_writes_to_derived_path(tmp_path):
    # body must clear MIN_BODY_WORDS — a stub is a failed generation, not a page
    payload = {**BASE, "sections": [{"heading": "Why", "body": "word " * 200}]}
    rel, report = render_and_write(tmp_path, payload)
    assert rel == "texturing/baking-high-to-low.md"
    assert report.ok
    assert (tmp_path / "docs" / rel).is_file()


# ------------------------------------------------------- link resolution

def test_dead_relative_link_rejected():
    text = FM + "# T\n\nSee [x](research/experiments.md).\n"
    r = LintReport()
    lint_page("second-life/platform-baseline.md", text, r,
              known_pages={"second-life/platform-baseline.md", "research/experiments.md"})
    assert "dead-link" in {f.rule for f in r.findings}


def test_correct_relative_link_accepted():
    text = FM + "# T\n\nSee [x](../research/experiments.md).\n"
    r = LintReport()
    lint_page("second-life/platform-baseline.md", text, r,
              known_pages={"second-life/platform-baseline.md", "research/experiments.md"})
    assert "dead-link" not in {f.rule for f in r.findings}


def test_external_and_anchor_links_ignored():
    text = FM + "# T\n\n[a](https://x.com) [b](#frag) [c](../research/experiments.md#e01)\n"
    r = LintReport()
    lint_page("second-life/p.md", text, r,
              known_pages={"second-life/p.md", "research/experiments.md"})
    assert "dead-link" not in {f.rule for f in r.findings}


def test_write_refused_when_model_invents_a_link(tmp_path):
    (tmp_path / "docs").mkdir(parents=True)
    bad = {**BASE, "related": [{"title": "Nope", "path": "does/not/exist.md"}]}
    with pytest.raises(PageRejected):
        render_and_write(tmp_path, bad)


# --------------------------------------------------- destructive-write guard

MEATY = {**BASE, "sections": [{"heading": "Why", "body": "word " * 200}]}


def test_near_empty_render_is_refused(tmp_path):
    (tmp_path / "docs").mkdir(parents=True)
    thin = {"title": "RetopoFlow", "section": "modeling", "type": "software"}
    with pytest.raises(PageRejected, match="no substance"):
        render_and_write(tmp_path, thin)


def test_rewrite_may_not_gut_an_existing_page(tmp_path):
    target = tmp_path / "docs" / "texturing" / "baking-high-to-low.md"
    target.parent.mkdir(parents=True)
    target.write_text('---\ntitle: "T"\n---\n# T\n\n' + ("word " * 400), encoding="utf-8")
    small = {**BASE, "sections": [{"heading": "Why", "body": "word " * 70}]}
    with pytest.raises(PageRejected, match="shrink the page"):
        render_and_write(tmp_path, small)


def test_expansion_of_an_existing_page_is_allowed(tmp_path):
    target = tmp_path / "docs" / "texturing" / "baking-high-to-low.md"
    target.parent.mkdir(parents=True)
    target.write_text('---\ntitle: "T"\n---\n# T\n\n' + ("word " * 100), encoding="utf-8")
    rel, report = render_and_write(tmp_path, MEATY)
    assert report.ok and rel.endswith("baking-high-to-low.md")


def test_new_page_only_needs_the_minimum(tmp_path):
    (tmp_path / "docs").mkdir(parents=True)
    rel, report = render_and_write(tmp_path, MEATY)
    assert report.ok

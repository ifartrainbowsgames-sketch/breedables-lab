from __future__ import annotations

import json
import subprocess
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .academy_manifest import academy_content_gaps
from .checks import check_http
from .db import LibrarianDB
from .extract import extract_after_screen
from .kimi import write_human_report, write_wiki_evolution_report
from .wiki_audit import build_wiki_audit_context, write_wiki_audit
from .wiki_context import build_wiki_context
from .wiki_urls import collect_wiki_links


def _daily_dir(repo_root: Path) -> Path:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return repo_root / "research" / "discoveries" / f"daily-{day}"


def run_daily_wiki(
    db: LibrarianDB,
    repo_root: Path,
    *,
    url_limit: int = 80,
    screen_failures: bool = False,
    humanize: bool = False,
    wiki_evolve: bool = False,
    wiki_audit: bool = False,
    webscreen_dir: Path | None = None,
) -> dict:
    """Morning wiki health pass: gaps + external link checks + report file."""
    repo_root = repo_root.resolve()
    out_dir = _daily_dir(repo_root)
    out_dir.mkdir(parents=True, exist_ok=True)

    academy_gaps = academy_content_gaps(repo_root)
    registry_gaps = db.registry_gaps(limit=25)
    resource_gaps = db.evidence_gaps(repo_root=repo_root, limit=25)

    links = collect_wiki_links(repo_root)
    if url_limit > 0:
        links = links[:url_limit]

    checked: list[dict] = []
    failures: list[dict] = []
    for link in links:
        status = check_http(link.url)
        row = {
            "url": link.url,
            "source": link.source,
            "http_status": status,
            "ok": status in {200, 301, 302, 303, 307, 308},
        }
        checked.append(row)
        if not row["ok"]:
            failures.append(row)

    screened: list[dict] = []
    if screen_failures and failures:
        screened = _screen_with_webscreen(
            repo_root, failures, webscreen_dir or (repo_root / "tools" / "webscreen")
        )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "report_dir": str(out_dir.relative_to(repo_root)).replace("\\", "/"),
        "summary": {
            "wiki_links_checked": len(checked),
            "wiki_links_failed": len(failures),
            "academy_gaps": len(academy_gaps),
            "registry_gaps": len(registry_gaps),
            "resource_evidence_gaps": len(resource_gaps),
            "browser_rescreens": len(screened),
        },
        "academy_gaps": academy_gaps,
        "registry_gaps": registry_gaps,
        "resource_evidence_gaps": resource_gaps,
        "link_checks": checked,
        "failures": failures,
        "browser_rescreens": screened,
        "next_actions": _next_actions(academy_gaps, failures, registry_gaps),
    }

    json_path = out_dir / "report.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_path = out_dir / "report.md"
    md_path.write_text(_render_markdown(payload), encoding="utf-8")

    payload["paths"] = {
        "json": str(json_path.relative_to(repo_root)).replace("\\", "/"),
        "markdown": str(md_path.relative_to(repo_root)).replace("\\", "/"),
    }
    if humanize:
        human_path = out_dir / "report-human.md"
        meta = write_human_report(payload, human_path)
        payload["human_report"] = meta
        payload["paths"]["human"] = str(human_path.relative_to(repo_root)).replace("\\", "/")
    if wiki_evolve:
        context = build_wiki_context(repo_root, db, payload)
        evolve_path = out_dir / "wiki-evolution.md"
        meta = write_wiki_evolution_report(context, evolve_path, repo_root=repo_root)
        payload["wiki_evolution"] = meta
        payload["paths"]["evolution"] = str(evolve_path.relative_to(repo_root)).replace("\\", "/")
    if wiki_audit:
        audit_context = build_wiki_audit_context(repo_root, payload)
        audit_path = out_dir / "wiki-audit-kimi.md"
        meta = write_wiki_audit(audit_path, context=audit_context, repo_root=repo_root)
        payload["wiki_audit"] = meta
        payload["paths"]["audit"] = str(audit_path.relative_to(repo_root)).replace("\\", "/")
    return payload


def _next_actions(academy_gaps: list, failures: list, registry_gaps: list) -> list[str]:
    actions: list[str] = []
    if failures:
        actions.append(f"Fix or replace {len(failures)} failing wiki URL(s) — see failures in this report.")
    for gap in academy_gaps[:5]:
        label = gap.get("name") or gap.get("id", "?")
        actions.append(f"Academy: {label} — {', '.join(gap.get('issues', []))}")
    for gap in registry_gaps[:3]:
        actions.append(f"Registry: {gap.get('name', '?')} — {', '.join(gap.get('issues', []))}")
    if not actions:
        actions.append("No critical gaps detected in this pass. Consider running webscreen hunt on a research topic.")
    return actions


def _render_markdown(payload: dict) -> str:
    s = payload["summary"]
    lines = [
        f"# Daily wiki report — {payload['generated_at'][:10]}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|------:|",
        f"| Wiki links checked | {s['wiki_links_checked']} |",
        f"| Wiki links failed | {s['wiki_links_failed']} |",
        f"| Academy gaps | {s['academy_gaps']} |",
        f"| Registry gaps | {s['registry_gaps']} |",
        f"| Resource evidence gaps | {s['resource_evidence_gaps']} |",
        f"| Browser re-screens (failures) | {s['browser_rescreens']} |",
        "",
    ]

    if payload["failures"]:
        lines.extend(["## Failed links", ""])
        for f in payload["failures"]:
            lines.append(f"- **{f['http_status']}** [{f['url']}]({f['url']}) — `{f['source']}`")
        lines.append("")

    if payload["academy_gaps"]:
        lines.extend(["## Academy gaps", ""])
        for g in payload["academy_gaps"]:
            label = g.get("name") or g.get("id", "?")
            lines.append(f"- **{label}**: {', '.join(g.get('issues', []))}")
        lines.append("")

    if payload["registry_gaps"]:
        lines.extend(["## Registry gaps", ""])
        for g in payload["registry_gaps"]:
            lines.append(f"- **{g.get('name', '?')}**: {', '.join(g.get('issues', []))}")
        lines.append("")

    lines.extend(["## Next actions", ""])
    for i, action in enumerate(payload["next_actions"], 1):
        lines.append(f"{i}. {action}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Generated by `python -m librarian.cli daily-wiki`.")
    lines.append("Learner guide: `docs/academy/start-here.md`")
    lines.append("Re-run with `--screen-failures` when Go + Chrome + webscreen are available.")
    return "\n".join(lines)


def _screen_with_webscreen(
    repo_root: Path, failures: list[dict], webscreen_dir: Path, limit: int = 5
) -> list[dict]:
    if not shutil.which("go"):
        return [{"error": "go not installed — skip browser rescreen"}]
    main_go = webscreen_dir / "cmd" / "webscreen" / "main.go"
    if not main_go.is_file():
        return [{"error": f"webscreen not found at {webscreen_dir}"}]

    out: list[dict] = []
    for row in failures[:limit]:
        slug = f"daily-fail-{row['http_status']}"
        try:
            proc = subprocess.run(
                [
                    "go",
                    "run",
                    "./cmd/webscreen",
                    "screen",
                    "--url",
                    row["url"],
                    "--slug",
                    slug,
                ],
                cwd=str(webscreen_dir),
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
            entry: dict = {
                "url": row["url"],
                "exit_code": proc.returncode,
                "stdout": proc.stdout.strip(),
                "stderr": proc.stderr.strip()[:500],
            }
            if proc.returncode == 0:
                first_line = proc.stdout.strip().split("\n")[0]
                parts = first_line.split()
                if len(parts) >= 2 and parts[0] == "saved":
                    entry["extract"] = extract_after_screen(repo_root, parts[1])
            out.append(entry)
        except subprocess.TimeoutExpired:
            out.append({"url": row["url"], "error": "timeout"})
        except OSError as exc:
            out.append({"url": row["url"], "error": str(exc)})
    return out

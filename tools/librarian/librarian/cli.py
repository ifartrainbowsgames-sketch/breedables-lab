from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from .checks import check_resource
from .config import Settings
from .db import LibrarianDB
from .ingest import github_search, ingest_feed
from .seed import seed_baseline
from .academy_manifest import academy_content_gaps
from .daily_wiki import run_daily_wiki
from .extract import extract_discovery_dir
from .kimi import (
    build_breedables_research_context,
    test_kimi_connection,
    write_breedables_research,
    WIKI_BREEDABLES_INVENTORY,
)
from .wiki_audit import build_wiki_audit_context, write_wiki_audit
from .wiki_images import write_wiki_images
from .wiki_videos import write_wiki_videos


def _db() -> tuple[LibrarianDB, Settings]:
    settings = Settings.from_env()
    db = LibrarianDB(settings.db_path)
    db.init()
    return db, settings


def cmd_init_db(_args) -> int:
    db, settings = _db()
    print(f"Initialized {settings.db_path}")
    return 0


def cmd_add(args) -> int:
    db, _ = _db()
    resource, created = db.add(
        name=args.name,
        url=args.url,
        category=args.category,
        commercial_type=args.commercial_type,
        code_license=args.code_license,
        model_license=args.model_license,
        asset_license=args.asset_license,
        output_rights=args.output_rights,
        dependency_risk=args.dependency_risk,
        status=args.status,
        notes=args.notes,
        source_type=args.source_type,
    )
    print(("CREATED" if created else "MERGED") + f" #{resource.id} {resource.name}")
    print(json.dumps(resource.as_dict(), indent=2))
    return 0


def cmd_list(args) -> int:
    db, _ = _db()
    rows = db.list(status=args.status, category=args.category, limit=args.limit)
    for r in rows:
        license_value = r.code_license or r.github_license or "?"
        print(f"#{r.id:<4} {r.status:<12} {r.commercial_type:<20} {license_value:<12} {r.name} -> {r.canonical_url}")
    return 0


def cmd_show(args) -> int:
    db, _ = _db()
    if args.id:
        resource = db.get(args.id)
        if not resource:
            print("Not found", file=sys.stderr)
            return 1
        print(json.dumps(resource.as_dict(), indent=2))
        return 0

    matches = db.search(args.query, limit=args.limit)
    if not matches:
        print("No matches")
        return 1
    print(json.dumps([m.as_dict() for m in matches], indent=2))
    return 0


def cmd_check(args) -> int:
    db, settings = _db()
    if args.id:
        rows = [db.get(args.id)]
        rows = [r for r in rows if r]
    else:
        rows = db.list(limit=args.limit)

    for row in rows:
        checked = check_resource(db, row, settings.github_token)
        print(
            f"#{checked.id} HTTP={checked.http_status} "
            f"github={checked.github_full_name or '-'} "
            f"license={checked.github_license or checked.code_license or '?'} "
            f"{checked.name}"
        )
    return 0


def cmd_gaps(args) -> int:
    db, settings = _db()
    print(json.dumps(db.gaps(limit=args.limit, repo_root=settings.repo_root), indent=2))
    return 0


def cmd_registry_gaps(args) -> int:
    db, _ = _db()
    print(json.dumps(db.registry_gaps(limit=args.limit), indent=2))
    return 0


def cmd_content_gaps(args) -> int:
    db, settings = _db()
    payload = {
        "resources": db.evidence_gaps(repo_root=settings.repo_root, limit=args.limit),
        "academy": academy_content_gaps(settings.repo_root),
    }
    print(json.dumps(payload, indent=2))
    return 0


def cmd_daily_wiki(args) -> int:
    db, settings = _db()
    payload = run_daily_wiki(
        db,
        settings.repo_root,
        url_limit=args.url_limit,
        screen_failures=args.screen_failures,
        humanize=args.humanize,
        wiki_evolve=args.wiki_evolve,
        wiki_audit=args.wiki_audit,
    )
    print(json.dumps(payload["summary"], indent=2))
    print(f"\nReport: {payload['paths']['markdown']}")
    if payload.get("human_report"):
        hr = payload["human_report"]
        print(f"Human briefing: {payload['paths'].get('human')} ({hr.get('source')})")
    if payload.get("wiki_evolution"):
        ev = payload["wiki_evolution"]
        print(f"Wiki evolution: {payload['paths'].get('evolution')} ({ev.get('source')})")
    if payload.get("wiki_audit"):
        au = payload["wiki_audit"]
        print(f"Wiki audit: {payload['paths'].get('audit')} ({au.get('source')})")
    for action in payload["next_actions"][:5]:
        print(f"  → {action}")
    return 0


def cmd_kimi_test(_args) -> int:
    _db()  # loads repo-root .env via Settings
    result = test_kimi_connection()
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


def cmd_breedables_research(args) -> int:
    _, settings = _db()
    repo = settings.repo_root
    context = build_breedables_research_context(repo)
    out = repo / (args.out or WIKI_BREEDABLES_INVENTORY)
    if Path(args.out).is_absolute():
        out = Path(args.out)
    result = write_breedables_research(
        out,
        context=context,
        use_kimi=not args.no_kimi,
        repo_root=repo,
    )
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


def cmd_wiki_audit(args) -> int:
    _, settings = _db()
    repo = settings.repo_root
    from datetime import date

    out_dir = repo / "research" / "discoveries" / f"daily-{date.today().isoformat()}"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "wiki-audit-kimi.md"
    context = build_wiki_audit_context(repo)
    result = write_wiki_audit(out, context=context, use_kimi=not args.no_kimi, repo_root=repo)
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


def cmd_wiki_videos(args) -> int:
    _, settings = _db()
    result = write_wiki_videos(
        settings.repo_root,
        use_kimi=not args.no_kimi,
        merge_seed=not args.no_seed,
    )
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


def cmd_wiki_images(args) -> int:
    _, settings = _db()
    result = write_wiki_images(
        settings.repo_root,
        use_kimi=not args.no_kimi,
    )
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


def cmd_extract(args) -> int:
    _, settings = _db()
    discovery_dir = settings.repo_root / "research" / "discoveries" / args.slug
    result = extract_discovery_dir(discovery_dir)
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


def cmd_research_queue(args) -> int:
    db, settings = _db()
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "wiki_base_url": settings.wiki_base_url,
        "resources": db.evidence_gaps(repo_root=settings.repo_root, limit=args.limit),
        "academy": academy_content_gaps(settings.repo_root),
        "registry": db.registry_gaps(limit=args.limit),
    }
    print(json.dumps(payload, indent=2))
    return 0


def cmd_set_evidence(args) -> int:
    db, _ = _db()
    doc_urls = None
    if args.docs:
        doc_urls = [part.strip() for part in args.docs.split(",") if part.strip()]
    resource = db.update_evidence(
        args.id,
        primary_video_url=args.video,
        doc_urls=doc_urls,
        lesson_wiki_path=args.lesson,
        evidence_path=args.evidence,
        license_note_path=args.license_note,
        academy_track=args.track,
        last_evidence_review=args.reviewed,
    )
    print(json.dumps(resource.as_dict(), indent=2))
    return 0


def cmd_status(_args) -> int:
    db, _ = _db()
    print(json.dumps(db.status_counts(), indent=2, sort_keys=True))
    return 0


def cmd_export(_args) -> int:
    db, _ = _db()
    print(db.export_json())
    return 0


def cmd_seed(_args) -> int:
    db, _ = _db()
    print(json.dumps(seed_baseline(db), indent=2))
    return 0


def cmd_ingest_feed(args) -> int:
    db, _ = _db()
    result = ingest_feed(db, args.url, category=args.category, limit=args.limit)
    print(json.dumps(result, indent=2))
    return 0


def cmd_discover_github(args) -> int:
    db, settings = _db()
    result = github_search(
        db,
        args.query,
        token=settings.github_token,
        category=args.category,
        limit=args.limit,
    )
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="breedables-librarian")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init-db")
    p.set_defaults(func=cmd_init_db)

    p = sub.add_parser("add")
    p.add_argument("name")
    p.add_argument("url")
    p.add_argument("--category", default="other")
    p.add_argument("--commercial-type", default="UNKNOWN")
    p.add_argument("--code-license")
    p.add_argument("--model-license")
    p.add_argument("--asset-license")
    p.add_argument("--output-rights")
    p.add_argument("--dependency-risk")
    p.add_argument("--status", default="DISCOVERED")
    p.add_argument("--notes")
    p.add_argument("--source-type")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("list")
    p.add_argument("--status")
    p.add_argument("--category")
    p.add_argument("--limit", type=int, default=100)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("show")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", type=int)
    group.add_argument("--query")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("check")
    p.add_argument("--id", type=int)
    p.add_argument("--limit", type=int, default=100)
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("gaps")
    p.add_argument("--limit", type=int, default=25)
    p.set_defaults(func=cmd_gaps)

    p = sub.add_parser("registry-gaps")
    p.add_argument("--limit", type=int, default=25)
    p.set_defaults(func=cmd_registry_gaps)

    p = sub.add_parser("content-gaps")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_content_gaps)

    p = sub.add_parser("research-queue")
    p.add_argument("--limit", type=int, default=50)
    p.set_defaults(func=cmd_research_queue)

    p = sub.add_parser("daily-wiki")
    p.add_argument("--url-limit", type=int, default=80, help="Max external URLs to HTTP-check")
    p.add_argument(
        "--screen-failures",
        action="store_true",
        help="Re-screen failed URLs with Go webscreen (requires go + Chrome)",
    )
    p.add_argument(
        "--humanize",
        action="store_true",
        help="Write report-human.md (Kimi if MOONSHOT_API_KEY set, else local glossary)",
    )
    p.add_argument(
        "--wiki-evolve",
        action="store_true",
        help="Write wiki-evolution.md — Kimi researches how to improve the Academy wiki",
    )
    p.add_argument(
        "--wiki-audit",
        action="store_true",
        help="Write wiki-audit-kimi.md — Kimi audits all docs/ pages and setup",
    )
    p.set_defaults(func=cmd_daily_wiki)

    p = sub.add_parser("kimi-test", help="Verify Kimi CLI (subscription) or Open Platform API")
    p.set_defaults(func=cmd_kimi_test)

    p = sub.add_parser(
        "breedables-research",
        help="Kimi updates docs/research/breedables-inventory-and-software.md (wiki)",
    )
    p.add_argument(
        "--out",
        default=WIKI_BREEDABLES_INVENTORY,
        help="Wiki path relative to repo root (default: live inventory page)",
    )
    p.add_argument(
        "--no-kimi",
        action="store_true",
        help="Skip Kimi even if logged in",
    )
    p.set_defaults(func=cmd_breedables_research)

    p = sub.add_parser(
        "wiki-images",
        help="Kimi finds image URLs; downloads and optimizes docs/assets/cards/",
    )
    p.add_argument(
        "--no-kimi",
        action="store_true",
        help="Use favicon fallback only (no Kimi)",
    )
    p.set_defaults(func=cmd_wiki_images)

    p = sub.add_parser(
        "wiki-audit",
        help="Kimi audits entire docs/ wiki — stale links, gaps, UX",
    )
    p.add_argument(
        "--no-kimi",
        action="store_true",
        help="Local audit only (no Kimi)",
    )
    p.set_defaults(func=cmd_wiki_audit)

    p = sub.add_parser(
        "wiki-videos",
        help="Kimi builds video-library.md with in-wiki YouTube embeds for all software",
    )
    p.add_argument("--no-kimi", action="store_true", help="Use local seed only")
    p.add_argument("--no-seed", action="store_true", help="Kimi only, do not merge seed videos")
    p.set_defaults(func=cmd_wiki_videos)

    p = sub.add_parser("extract")
    p.add_argument("slug", help="Discovery folder name under research/discoveries/")
    p.set_defaults(func=cmd_extract)

    p = sub.add_parser("set-evidence")
    p.add_argument("id", type=int)
    p.add_argument("--video")
    p.add_argument("--docs", help="Comma-separated official doc URLs")
    p.add_argument("--lesson", help="Wiki lesson path, e.g. docs/academy/tracks/a01-organic-pbr.md")
    p.add_argument("--evidence", help="Evidence folder path, e.g. training/texturing/a01/")
    p.add_argument("--license-note")
    p.add_argument("--track", help="Academy track id, e.g. A01")
    p.add_argument("--reviewed", help="ISO date of last evidence review")
    p.set_defaults(func=cmd_set_evidence)

    p = sub.add_parser("status")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("export-json")
    p.set_defaults(func=cmd_export)

    p = sub.add_parser("seed-baseline")
    p.set_defaults(func=cmd_seed)

    p = sub.add_parser("ingest-feed")
    p.add_argument("url")
    p.add_argument("--category", default="research")
    p.add_argument("--limit", type=int, default=25)
    p.set_defaults(func=cmd_ingest_feed)

    p = sub.add_parser("discover-github")
    p.add_argument("query")
    p.add_argument("--category", default="github-discovery")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_discover_github)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()

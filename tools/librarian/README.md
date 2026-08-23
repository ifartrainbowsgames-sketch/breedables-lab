# Breedables Studio Librarian

Python automation layer for Breedables Studio.

**V1 purpose:** collect, normalize, deduplicate, validate, and expose structured research/tool records without pretending to replace deep ChatGPT research.

## Responsibility split

- **Python Librarian:** deterministic collection, link checks, GitHub metadata, indexing, duplicate control, lookup, routing.
- **ChatGPT:** deep web research, comparisons, license interpretation, recommendations, synthesis.
- **Slack:** interface + living wiki.
- **GitHub:** source of truth for code/specs/tests.
- **Claude/Cursor:** architecture review and implementation work when assigned.

The Librarian must never decide that a workflow is commercially safe from one license field alone. Code, model weights, bundled assets, dependencies, and output rights are separate concerns.

## V1 features

- SQLite resource registry
- URL/name normalization
- duplicate merge behavior
- tool/status/commercial-type taxonomy
- HTTP link-health checks
- GitHub repository metadata enrichment
- GitHub repository discovery into a review queue
- RSS/Atom feed ingestion into a review queue
- curated baseline seeding
- separate fields for code/model/assets/output/dependency risk
- CLI
- Slack Bolt app with Socket Mode
- `/breedtool`, `/breedstatus`, `/breedgaps`
- app mentions: `tool <name>`, `status`, `gaps`
- pytest coverage for normalization and dedupe

## Install

Requires **Python 3.11+**.

```bash
cd tools/librarian
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install:

```bash
pip install -e ".[dev]"
```

Create configuration:

```bash
cp .env.example .env
```

Environment loading is intentionally left to your shell/process manager in V1; no dotenv package is required.

## CLI quick start

```bash
export LIBRARIAN_DB_PATH=.data/librarian.sqlite3
python -m librarian.cli init-db
```

Add a known tool:

```bash
python -m librarian.cli add \
  "Material Maker" \
  "https://github.com/RodZill4/material-maker" \
  --category textures \
  --commercial-type OPEN_SOURCE \
  --code-license MIT \
  --status EXPERIMENTAL \
  --notes "Procedural PBR authoring candidate"
```

List:

```bash
python -m librarian.cli list
```

Search:

```bash
python -m librarian.cli show --query "material"
```

Check links + GitHub metadata:

```bash
python -m librarian.cli check
```

See obvious registry gaps:

```bash
python -m librarian.cli gaps
```

Export:

```bash
python -m librarian.cli export-json > librarian-export.json
```

Seed the currently researched baseline:

```bash
python -m librarian.cli seed-baseline
```

Discover recently updated GitHub candidates:

```bash
python -m librarian.cli discover-github "blender retopology"
python -m librarian.cli discover-github "second life lsl breedable" --limit 20
```

Ingest an RSS or Atom feed:

```bash
python -m librarian.cli ingest-feed "https://example.com/feed.xml" --category blender-news
```

Discovery commands deliberately store new candidates as `DISCOVERED` with `UNKNOWN` commercial classification unless we already have curated evidence. Discovery is not approval.

## Taxonomy

Commercial type:

- `OPEN_SOURCE`
- `FREE_CLOSED_SOURCE`
- `FREEMIUM`
- `PAID_COMMERCIAL`
- `RESEARCH_ONLY`
- `OPEN_CONTENT_CC0`
- `UNKNOWN`

Workflow status:

- `DISCOVERED`
- `REVIEWING`
- `EXPERIMENTAL`
- `USE_NOW`
- `USE_LATER`
- `APPROVED`
- `REJECTED`
- `SUPERSEDED`

These are intentionally separate. A project can be open source while still being experimental for our production workflow.

## GitHub metadata

If a resource points at a GitHub repository, `check` tries to record:

- full repo name
- archived status
- star count
- last push time
- GitHub-reported license identifier

Optional:

```bash
export GITHUB_TOKEN=...
```

A GitHub API license field is **evidence**, not a complete commercial-rights audit.

## Slack setup

The Slack bot uses **Slack Bolt for Python** in **Socket Mode**, so local development does not require exposing a public HTTP endpoint.

Create/configure a Slack app with:

Bot scopes:

- `commands`
- `chat:write`
- `app_mentions:read`

Enable **Socket Mode**, generate an app-level token with `connections:write`, and create these slash commands:

- `/breedtool`
- `/breedstatus`
- `/breedgaps`

Set:

```bash
export SLACK_BOT_TOKEN=xoxb-...
export SLACK_APP_TOKEN=xapp-...
```

Run:

```bash
python -m librarian.slack_app
```

The bot is intentionally read-oriented in V1. It does **not** silently rewrite Slack Canvases.

### Daily digests — Apprise

**[Apprise](https://github.com/caronc/apprise)** posts `daily-wiki` summaries to a channel (no 24/7 bot process needed for digests).

```bash
pip install -e ".[notify]"
```

Repo-root `.env`:

```bash
SLACK_BOT_TOKEN=xoxb-...
SLACK_NOTIFY_CHANNEL=#breedables-knowledge
```

```bash
python -m librarian.cli notify-test
.\scripts\daily-wiki.ps1   # includes --notify-slack when configured
```

## Suggested first records

Seed only tools we have actually researched, for example:

- Blender
- Material Maker
- Ucupaint
- TripoSR
- RetopoFlow
- Poly Haven
- ambientCG

Do not mass-import random search results. The point is a curated registry.

## What comes next

See the full phased plan and recommended open source stack:

**[docs/studio-roadmap.md](../../docs/studio-roadmap.md)**

### Librarian V1.1 (build in-repo)

1. YouTube resource registry and duplicate detection
2. Structured research-request queue for ChatGPT
3. Scheduled link/version checks
4. GitHub release-watch subscriptions
5. Slack Canvas sync with review/approval gates
6. Experiment evidence + benchmark records
7. Asset provenance records
8. Weekly compact change report

### Companion OSS by phase (adopt, don't fork)

| Phase | Focus | Recommended OSS |
|-------|-------|-----------------|
| 1 | Readable wiki | [MkDocs Material](https://github.com/squidfunk/mkdocs-material), [Wiki.js](https://github.com/requarks/wiki) |
| 2 | Schedules + link depth | [linkchecker](https://github.com/linkchecker/linkchecker) |
| 3 | Cursor / IDE search | [self-docs](https://github.com/AdamRussak/self-doc), [OmniDocs-RAG](https://github.com/ElvinBayramov/OmniDocs-RAG) |
| 4 | Papers & academy | [ResearchShelf](https://pypi.org/project/researchshelf/), [GROBID](https://github.com/kermitt2/grobid) |
| 5 | Slack living wiki | [Beever Atlas](https://github.com/Beever-AI/beever-atlas), [Outline](https://github.com/outline/outline) |

## Security

- Never commit Slack or GitHub tokens.
- Use least-privilege Slack scopes.
- Do not run arbitrary code from discovered repositories.
- Treat fetched web content as untrusted input.
- Do not auto-classify commercial safety from README text alone.

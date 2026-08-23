# Web research stack — Go CLI & Chromium

**Status:** ACTIVE — CLI in `tools/webscreen/`, Librarian integration in `tools/librarian/`  
**Role:** Website **screening** (load JS pages, capture evidence) and **web search** (meta-search → discovery queue) for breedables R&D and Academy link verification.

No desktop UI shell — operators use **PowerShell scripts + CLI** (`scripts/daily-wiki.ps1`, `webscreen hunt`). Evidence lands in git under `research/discoveries/`.

This stack sits **beside** the Python [Librarian](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/tools/librarian): Librarian owns the registry and gaps; this tool owns **browser-grade fetch** and **search ingestion**.

---

## Why not Python-only?

The Librarian already uses **httpx** for HTTP checks and RSS/GitHub APIs. That is enough for:

- Link alive/dead
- GitHub metadata
- Feed discovery

It is **not** enough when a page needs JavaScript, login walls, or you want screenshots + readable main text for research reports (SL wiki, forums, marketplace listings). For that you need a **real browser engine**.

---

## Tier 1 stack (what we run)

```text
┌─────────────────────────────────────────────────────────────┐
│  scripts/daily-wiki.ps1  ·  webscreen CLI  ·  Cursor/AI   │
└───────────────────────────┬─────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│  Go webscreen (tools/webscreen/)                            │
│  · screen  — chromedp load + screenshot + HTML              │
│  · search  — SearXNG meta-search                            │
│  · hunt    — search then screen each hit                    │
└───────────────┬─────────────────────────┬───────────────────┘
                │                         │
     ┌──────────▼──────────┐   ┌──────────▼──────────┐
     │ chromedp (Chrome)   │   │ SearXNG (Docker)    │
     └──────────┬──────────┘   └─────────────────────┘
                │
     ┌──────────▼──────────────────────────────────┐
     │ Python Librarian                              │
     │ daily-wiki · extract (trafilatura) · gaps   │
     └─────────────────────────────────────────────┘
                │
     ┌──────────▼──────────────────────────────────┐
     │ CI: lychee (docs link check) + mkdocs strict│
     └─────────────────────────────────────────────┘
```

| Layer | Project | Role |
|-------|---------|------|
| **Headless screening** | [chromedp](https://github.com/chromedp/chromedp) | Load JS pages via Chrome/Edge DevTools — screenshot + HTML |
| **Article extract** | [trafilatura](https://github.com/adbar/trafilatura) | Python post-step: `page.html` → clean `content.md` |
| **Fallback extract** | [go-readability](https://github.com/go-shiori/go-readability) | Used when trafilatura not installed |
| **Web search** | [SearXNG](https://github.com/searxng/searxng) | Self-hosted meta-search JSON API |
| **Link CI** | [lychee](https://github.com/lycheeverse/lychee) | Weekly + PR link checks on `docs/**/*.md` |
| **Registry** | Breedables Librarian | `daily-wiki`, `research-queue`, `extract` |

**Not in Tier 1:** Wails desktop UI (removed — CLI + scripts are enough). Energy CEF embed (only if you later need an in-process browser panel).

---

## Ollama — needed?

**No, not for Tier 1.** Screening, link checks, search, and markdown extraction are deterministic — no LLM required.

**Kimi K3 (Moonshot API)** — optional for **plain-English morning briefings** when internal codes (A01, B07) leak into automation:

```powershell
# .env — optional
MOONSHOT_API_KEY=your-key

python -m librarian.cli daily-wiki --humanize
# → research/discoveries/daily-YYYY-MM-DD/report-human.md
```

Without an API key, `--humanize` still runs using a local glossary (`academy_manifest.code_glossary`).

| Use | Kimi K3 | Ollama (local) |
|-----|---------|----------------|
| Humanize daily gap report | **Yes** — best fit | Possible but weaker at following glossary rules |
| Summarize discovery bundle | Yes | `qwen2.5:7b` |
| Local wiki embeddings | Overkill | `nomic-embed-text` |

**Not for Tier 1:** link checks, chromedp, trafilatura, SearXNG.

---

## Screening outputs

Each screened URL produces a discovery bundle under `research/discoveries/`:

```text
research/discoveries/2026-08-23-sl-wiki-ozimals/
  meta.json          # url, fetched_at, http_status, title, final_url
  page.png           # viewport screenshot
  page.html          # full DOM (for trafilatura)
  content.md         # extracted readable text + source URL header
```

After screening, run trafilatura (automatic with `--screen-failures` when `[research]` extras installed):

```powershell
cd tools/librarian
pip install -e ".[research]"
python -m librarian.cli extract <slug>
```

These feed human + AI synthesis into `docs/research/*.md`. **Screening ≠ approval** — same rule as Librarian `DISCOVERED`.

---

## Daily workflow

```powershell
# From repo root — HTTP checks + gap report
.\scripts\daily-wiki.ps1

# With browser re-screen on failures + trafilatura extract
.\scripts\daily-wiki.ps1 --screen-failures
```

Report: `research/discoveries/daily-YYYY-MM-DD/report.md`

Manual hunt:

```powershell
cd tools/webscreen
go run ./cmd/webscreen hunt --query "Second Life breedables genetics" --limit 3
cd ../librarian
python -m librarian.cli extract <slug-from-output>
```

---

## Web search (SearXNG)

```powershell
cd tools/webscreen/docker/searxng
docker compose up -d
```

API: `http://127.0.0.1:8080/search?q=...&format=json`

---

## Install (Windows)

### Prerequisites

1. [Go 1.22+](https://go.dev/dl/)
2. Google Chrome or Microsoft Edge (chromedp)
3. Python 3.11+ with Librarian `[research]` extras (trafilatura)
4. Optional: Docker Desktop for SearXNG

### CLI

```powershell
cd tools/webscreen
go mod download
go run ./cmd/webscreen screen --url "https://wiki.secondlife.com/wiki/Ozimals"

cd ../librarian
pip install -e ".[dev,research]"
python -m librarian.cli extract 2026-08-23-wiki-secondlife-com-wiki-ozimals
```

---

## CI

| Workflow | What it checks |
|----------|----------------|
| `.github/workflows/wiki-links.yml` | **lychee** on all `docs/**/*.md` |
| `.github/workflows/docs.yml` | `mkdocs build --strict` |
| `.github/workflows/librarian-weekly.yml` | Librarian tests + `daily-wiki` gap export |

Bot-blocked domains (CG Cookie, SL community) are excluded in `.lychee.toml` — verify those locally with `webscreen screen`.

---

## Integration with Librarian

| Step | Tool |
|------|------|
| Morning health pass | `scripts/daily-wiki.ps1` |
| Search + screen | `webscreen hunt` |
| Clean extract | `python -m librarian.cli extract <slug>` |
| Human approves | move summary into `docs/research/` |
| Publish wiki | `mkdocs build --strict` |

---

## Related

- [Studio roadmap — Phase 2 research automation](../../studio-roadmap.md)
- [Librarian README](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/tools/librarian) (repo)
- [Research README](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/research) (repo)

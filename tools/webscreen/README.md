# Breedables Webscreen — Go CLI + Chromium

Website **screening** and **web search** for breedables R&D. Pairs with the Python [Librarian](../librarian/README.md).

**Wiki:** [docs/production/tools/web-research-stack.md](../../docs/production/tools/web-research-stack.md)

## Stack (Tier 1)

| Piece | Library | Purpose |
|-------|---------|---------|
| Headless screening | [chromedp](https://github.com/chromedp/chromedp) | Load JS pages, screenshot, save HTML |
| Article extract | [trafilatura](https://github.com/adbar/trafilatura) | Via Librarian `extract` — `page.html` → `content.md` |
| Fallback extract | [go-readability](https://github.com/go-shiori/go-readability) | Inline in `screen` when trafilatura not run |
| Meta search | [SearXNG](https://github.com/searxng/searxng) | Self-hosted web search API |
| Link CI | [lychee](https://github.com/lycheeverse/lychee) | PR + weekly checks on `docs/` |

**No Wails** — CLI + `scripts/daily-wiki.ps1` is the operator interface.

## Prerequisites

- Go 1.22+
- Chrome or Edge (chromedp)
- Python 3.11+ with Librarian `[research]` for trafilatura
- Docker (optional, for SearXNG)

## Quick start

```powershell
cd tools/webscreen
go mod download

go run ./cmd/webscreen screen --url "https://wiki.secondlife.com/wiki/Ozimals"

cd ../librarian
pip install -e ".[research]"
python -m librarian.cli extract 2026-08-23-wiki-secondlife-com-wiki-ozimals

go run ./cmd/webscreen search --query "Second Life breedables" --limit 5
go run ./cmd/webscreen hunt --query "KittyCatS breedables" --limit 3
```

## SearXNG

```powershell
cd docker/searxng
docker compose up -d
```

API default: `http://127.0.0.1:8080` — override with `WEBSCREEN_SEARXNG_URL`.

## Output layout

```
research/discoveries/<slug>/
  meta.json
  page.png
  page.html
  content.md
```

Repo root is auto-detected by walking up for `mkdocs.yml`.

## Environment

| Variable | Default | Meaning |
|----------|---------|---------|
| `WEBSCREEN_SEARXNG_URL` | `http://127.0.0.1:8080` | SearXNG base URL |
| `WEBSCREEN_CHROME_PATH` | *(auto)* | Path to Chrome/Edge executable |
| `WEBSCREEN_TIMEOUT` | `30s` | Page load timeout |

## Tests

```powershell
go test ./...
```

Screening tests are skipped in CI unless `WEBSCREEN_INTEGRATION=1` and Chrome is present.

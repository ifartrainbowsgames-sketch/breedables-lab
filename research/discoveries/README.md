# Discoveries — webscreen captures + daily wiki reports

## Daily folder (`daily-YYYY-MM-DD/`)

Produced by `scripts/daily-wiki.ps1`:

| File | Purpose |
|------|---------|
| `report.json` / `report.md` | Link checks, academy/registry gaps |
| `report-human.md` | Plain-English morning briefing (Kimi or local) |
| `wiki-evolution.md` | Kimi research: how to improve the Academy wiki |

## URL bundles (webscreen)

Each screened-page subfolder contains:

- `meta.json` — URL, title, fetch time
- `page.png` — viewport screenshot
- `page.html` — full DOM (input for trafilatura)
- `content.md` — extracted text for AI/human synthesis

**Not approved research** until reviewed and promoted to `docs/research/`.

```powershell
cd tools/webscreen
go run ./cmd/webscreen screen --url "https://example.com"

cd ../librarian
python -m librarian.cli extract <slug>
```

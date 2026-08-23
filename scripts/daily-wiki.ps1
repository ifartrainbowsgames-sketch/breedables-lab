# On-demand wiki health check — run from repo root (no scheduled cadence).
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location (Join-Path $Root "tools\librarian")
$env:BREEDABLES_REPO_ROOT = $Root

if (-not (Test-Path ".venv\Scripts\python.exe")) {
    python -m venv .venv
    .\.venv\Scripts\pip.exe install -e ".[dev,research,notify]" -q
}

.\.venv\Scripts\python.exe -m librarian.cli init-db 2>$null
.\.venv\Scripts\python.exe -m librarian.cli seed-baseline 2>$null

.\.venv\Scripts\python.exe -m librarian.cli daily-wiki @args

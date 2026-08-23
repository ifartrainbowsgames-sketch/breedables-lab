# Daily wiki health check — run from repo root
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

# Always write human + evolution briefs (Kimi CLI subscription or optional Open Platform API)
$humanize = $true
$wikiEvolve = $true
$wikiAudit = $true
$notifySlack = $true
foreach ($arg in $args) {
    if ($arg -eq "--no-humanize") { $humanize = $false }
    if ($arg -eq "--no-wiki-evolve") { $wikiEvolve = $false }
    if ($arg -eq "--no-wiki-audit") { $wikiAudit = $false }
    if ($arg -eq "--no-notify-slack") { $notifySlack = $false }
}
$extra = @()
if ($humanize -and ($args -notcontains "--humanize")) { $extra += "--humanize" }
if ($wikiEvolve -and ($args -notcontains "--wiki-evolve")) { $extra += "--wiki-evolve" }
if ($wikiAudit -and ($args -notcontains "--wiki-audit")) { $extra += "--wiki-audit" }
if ($notifySlack -and ($args -notcontains "--notify-slack") -and ($args -notcontains "--no-notify-slack")) {
    $extra += "--notify-slack"
}
$args = $extra + ($args | Where-Object { $_ -notin @("--no-humanize", "--no-wiki-evolve", "--no-wiki-audit", "--no-notify-slack") })

.\.venv\Scripts\python.exe -m librarian.cli daily-wiki @args

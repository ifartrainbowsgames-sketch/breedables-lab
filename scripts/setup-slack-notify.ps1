# Create #breedables-knowledge, verify bot can post, set GitHub Actions secrets.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$EnvFile = Join-Path $Root ".env"
if (-not (Test-Path $EnvFile)) {
    Write-Error "Missing $EnvFile — copy .env.example first."
}

Get-Content $EnvFile | ForEach-Object {
    if ($_ -match '^\s*([^#=]+)=(.*)$') {
        [Environment]::SetEnvironmentVariable($matches[1].Trim(), $matches[2].Trim(), "Process")
    }
}

$Librarian = Join-Path $Root "tools\librarian"
Set-Location $Librarian
if (-not (Test-Path ".venv\Scripts\python.exe")) {
    python -m venv .venv
    .\.venv\Scripts\pip.exe install -e ".[notify]" -q
}

Write-Host "`n=== Slack bot scopes (add in api.slack.com → Breedables app → OAuth) ===" -ForegroundColor Cyan
Write-Host "  channels:read  channels:join  channels:manage  (optional, for auto-create)"
Write-Host "  chat:write  commands  app_mentions:read  (already required)`n"

Write-Host "=== Manual (if channel missing) ===" -ForegroundColor Cyan
Write-Host "  1. In Slack: Create channel #breedables-knowledge"
Write-Host "  2. /invite @breedables_librarian"
Write-Host "  3. Optional: Incoming Webhook → copy URL for SLACK_WEBHOOK_URL`n"

$env:BREEDABLES_REPO_ROOT = $Root
.\.venv\Scripts\python.exe -m librarian.cli notify-test
if ($LASTEXITCODE -ne 0) {
    Write-Host "notify-test failed — complete manual steps above, then re-run this script." -ForegroundColor Yellow
}

if (Get-Command gh -ErrorAction SilentlyContinue) {
    Write-Host "`n=== GitHub Actions secrets ===" -ForegroundColor Cyan
    $bot = $env:SLACK_BOT_TOKEN
    if ($bot) {
        $bot | gh secret set SLACK_BOT_TOKEN --repo ifartrainbowsgames-sketch/breedables-lab
        Write-Host "  Set SLACK_BOT_TOKEN"
    }
    $channel = if ($env:SLACK_NOTIFY_CHANNEL) { $env:SLACK_NOTIFY_CHANNEL } else { "#breedables-knowledge" }
    $channel | gh secret set SLACK_NOTIFY_CHANNEL --repo ifartrainbowsgames-sketch/breedables-lab
    Write-Host "  Set SLACK_NOTIFY_CHANNEL = $channel"
    if ($env:SLACK_WEBHOOK_URL) {
        $env:SLACK_WEBHOOK_URL | gh secret set SLACK_WEBHOOK_URL --repo ifartrainbowsgames-sketch/breedables-lab
        Write-Host "  Set SLACK_WEBHOOK_URL"
    } else {
        Write-Host "  (Skip SLACK_WEBHOOK_URL — not in .env; CI will use bot token)"
    }
} else {
    Write-Host "gh CLI not found — set GitHub secrets manually." -ForegroundColor Yellow
}

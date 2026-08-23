# Run Kimi Code CLI (subscription OAuth — not Open Platform API).
# Usage: .\scripts\kimi.ps1
#        .\scripts\kimi.ps1 -p "your prompt here"

$KimiExe = Join-Path $env:USERPROFILE ".kimi-code\bin\kimi.exe"
if (-not (Test-Path $KimiExe)) {
    Write-Error "Kimi CLI not found at $KimiExe. Install: irm https://code.kimi.com/kimi-code/install.ps1 | iex"
    exit 1
}
& $KimiExe @args

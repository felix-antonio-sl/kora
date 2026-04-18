# kora CLI wrapper for PowerShell (Windows/macOS/Linux)
# Usage: ./kora.ps1 [command] [args]
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
python "$scriptDir/kora" @args

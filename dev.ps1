param(
    [ValidateSet('check', 'bibliography')][string]$Task = 'check',
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$TaskArgs
)
$ErrorActionPreference = 'Stop'
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
$pythonBinary = if ($pythonCommand -and $pythonCommand.Source -notmatch 'WindowsApps') { $pythonCommand.Source } else { $null }
if (-not $pythonBinary) {
    $bundledPython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
    if (Test-Path -LiteralPath $bundledPython) { $pythonBinary = $bundledPython }
}
if (-not $pythonBinary) { throw 'Python 3.11+ requis. Installer Python ou utiliser son chemin explicite ; aucune configuration globale modifiée.' }
$entrypoint = if ($Task -eq 'check') { 'tools/check.py' } else { 'tools/bibliography.py' }
Push-Location $PSScriptRoot
try {
    & $pythonBinary $entrypoint @TaskArgs
    $resultCode = $LASTEXITCODE
} finally { Pop-Location }
exit $resultCode

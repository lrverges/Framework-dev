<#
.SYNOPSIS
    verify.ps1 - Aduana Determinista de Calidad y Cobertura (LIDR & Superpowers)
#>

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

python (Join-Path $RepoRoot "scripts\gatekeeper\gatekeeper.py") @args
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

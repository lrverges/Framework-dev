<#
.SYNOPSIS
    finish-feature.ps1 - Verificación y Cierre Seguro de Feature (Superpowers)
.DESCRIPTION
    Ejecuta scripts/verify.ps1 dentro del worktree y facilita la finalización de la feature.
.PARAMETER FeatureName
    Nombre de la característica o funcionalidad (ej. user-auth)
#>
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$FeatureName
)

$ErrorActionPreference = "Stop"

$BranchName = "feat/$FeatureName"
$WorktreeDir = ".worktrees/$FeatureName"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$WorktreeFullDir = Join-Path $RepoRoot $WorktreeDir

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " 🏁 Verificando y Finalizando Feature: $FeatureName" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Ejecutar aduana determinista de verificación
Write-Host "---> Ejecutando verificación obligatoria (Linter + Tests + Cobertura 85%+)..." -ForegroundColor Yellow

$VerifyScript = Join-Path $RepoRoot "scripts\verify.ps1"
if (Test-Path $WorktreeFullDir) {
    Push-Location $WorktreeFullDir
    try {
        & $VerifyScript
    } finally {
        Pop-Location
    }
} else {
    & $VerifyScript
}

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] La verificación ha fallado. Corrige los problemas antes de cerrar la feature." -ForegroundColor Red
    exit 1
}

Write-Host "`n================================================================================" -ForegroundColor Green
Write-Host " [EXITO] Verificación superada con éxito." -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Instrucciones de integración:" -ForegroundColor White
Write-Host " 1. Realiza el push de tu rama: git push origin $BranchName" -ForegroundColor Gray
Write-Host " 2. Crea el Pull Request hacia 'main'." -ForegroundColor Gray
Write-Host ""

$Confirm = Read-Host "¿Deseas remover el worktree local $WorktreeDir? (s/N)"
if ($Confirm -match "^[sSyY]$") {
    git worktree remove $WorktreeFullDir --force
    Write-Host "[OK] Worktree $WorktreeDir removido de forma segura." -ForegroundColor Green
}

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " Feature $FeatureName completada satisfactoriamente." -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

<#
.SYNOPSIS
    start-feature.ps1 - Aislamiento Físico con Git Worktrees (Superpowers)
.DESCRIPTION
    Crea un worktree aislado para desarrollar una feature sin tocar la rama principal.
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

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " 🚀 Creando Git Worktree Aislado: $FeatureName" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

$WorktreeFullDir = Join-Path $RepoRoot $WorktreeDir
if (Test-Path $WorktreeFullDir) {
    Write-Host "[AVISO] El worktree en $WorktreeDir ya existe." -ForegroundColor Yellow
} else {
    git worktree add -b $BranchName $WorktreeFullDir main
    Write-Host "[OK] Worktree creado en $WorktreeDir apuntando a $BranchName" -ForegroundColor Green
}

$EnvExample = Join-Path $RepoRoot ".env.example"
$TargetEnv = Join-Path $WorktreeFullDir ".env"
if ((Test-Path $EnvExample) -and -not (Test-Path $TargetEnv)) {
    Copy-Item $EnvExample $TargetEnv
    Write-Host "[OK] Archivo .env copiado en el worktree." -ForegroundColor Green
}

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host " ✅ Entorno aislado listo. Para comenzar a trabajar ejecuta:" -ForegroundColor Green
Write-Host "    cd $WorktreeDir" -ForegroundColor White
Write-Host " La rama 'main' permanece protegida e intacta en la raíz." -ForegroundColor Gray
Write-Host "================================================================================" -ForegroundColor Cyan

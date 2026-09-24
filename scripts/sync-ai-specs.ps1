<#
.SYNOPSIS
    Sincroniza especificaciones desde ai-specs/ hacia los agentes
#>

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$SourceDir = Join-Path $RepoRoot "ai-specs"

if (-not (Test-Path $SourceDir)) {
    Write-Host "[ERROR] Directorio de origen no encontrado: $SourceDir" -ForegroundColor Red
    exit 1
}

Write-Host "Iniciando verificacion y sincronizacion de especificaciones..." -ForegroundColor Cyan

function Test-IsJunction ($path) {
    if (-not (Test-Path $path)) { return $false }
    $item = Get-Item $path -Force
    return ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -eq [System.IO.FileAttributes]::ReparsePoint
}

# 1. .claude/ai-specs/
$ClaudeDest = Join-Path $RepoRoot ".claude\ai-specs"
if (Test-IsJunction $ClaudeDest) {
    Write-Host "  -> $ClaudeDest ya esta vinculado como Junction a ai-specs [OK]" -ForegroundColor Green
} else {
    if (-not (Test-Path $ClaudeDest)) {
        New-Item -ItemType Junction -Path $ClaudeDest -Target $SourceDir -Force | Out-Null
        Write-Host "  -> Creado Junction en $ClaudeDest -> $SourceDir" -ForegroundColor Green
    }
}

# 2. .cursor/rules/
$CursorDest = Join-Path $RepoRoot ".cursor\rules"
if (Test-IsJunction $CursorDest) {
    Write-Host "  -> $CursorDest ya esta vinculado como Junction a ai-specs [OK]" -ForegroundColor Green
} else {
    if (-not (Test-Path $CursorDest)) {
        New-Item -ItemType Junction -Path $CursorDest -Target $SourceDir -Force | Out-Null
        Write-Host "  -> Creado Junction en $CursorDest -> $SourceDir" -ForegroundColor Green
    }
}

# 3. .antigravity/rules/
$AntiDest = Join-Path $RepoRoot ".antigravity\rules"
if (Test-IsJunction $AntiDest) {
    Write-Host "  -> $AntiDest ya esta vinculado como Junction a ai-specs [OK]" -ForegroundColor Green
} else {
    if (-not (Test-Path $AntiDest)) {
        New-Item -ItemType Junction -Path $AntiDest -Target $SourceDir -Force | Out-Null
        Write-Host "  -> Creado Junction en $AntiDest -> $SourceDir" -ForegroundColor Green
    }
}

# 4. .agents/skills/ (sincronizar habilidades para Antigravity)
$SkillsDest = Join-Path $RepoRoot ".agents\skills"
if (-not (Test-Path $SkillsDest)) { New-Item -ItemType Directory -Path $SkillsDest -Force | Out-Null }
$SkillSource = Join-Path $SourceDir "skills"
if (Test-Path $SkillSource) {
    # Skills en archivo .md plano (convertir a dir/SKILL.md)
    Get-ChildItem -Path $SkillSource -Filter "*.md" -File | ForEach-Object {
        $skillDir = Join-Path $SkillsDest $_.BaseName
        if (-not (Test-Path $skillDir)) { New-Item -ItemType Directory -Path $skillDir -Force | Out-Null }
        Copy-Item -Path $_.FullName -Destination (Join-Path $skillDir "SKILL.md") -Force
    }
    # Skills estructuradas en carpetas
    Get-ChildItem -Path $SkillSource -Directory | ForEach-Object {
        $destDir = Join-Path $SkillsDest $_.Name
        if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
        Copy-Item -Path (Join-Path $_.FullName "*") -Destination $destDir -Recurse -Force
    }
    Write-Host "  -> Habilidades (Skills) sincronizadas en $SkillsDest" -ForegroundColor Green
}

Write-Host "[OK] Verificacion y sincronizacion completada exitosamente." -ForegroundColor Green

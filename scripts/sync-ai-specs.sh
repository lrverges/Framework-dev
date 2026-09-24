#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="${REPO_ROOT}/ai-specs"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "[ERROR] Directorio de origen no encontrado: $SOURCE_DIR"
    exit 1
fi

echo "Iniciando sincronizacion de especificaciones..."

# 1. .claude/ai-specs/
CLAUDE_DEST="${REPO_ROOT}/.claude/ai-specs"
mkdir -p "$CLAUDE_DEST"
cp -r "${SOURCE_DIR}/"* "$CLAUDE_DEST/" 2>/dev/null || true
echo "  -> Copiado a $CLAUDE_DEST"

# 2. .cursor/rules/
CURSOR_DEST="${REPO_ROOT}/.cursor/rules"
mkdir -p "$CURSOR_DEST"
cp -r "${SOURCE_DIR}/"* "$CURSOR_DEST/" 2>/dev/null || true
echo "  -> Copiado a $CURSOR_DEST"

# 3. .antigravity/rules/
ANTI_DEST="${REPO_ROOT}/.antigravity/rules"
mkdir -p "$ANTI_DEST"
cp -r "${SOURCE_DIR}/"* "$ANTI_DEST/" 2>/dev/null || true
echo "  -> Copiado a $ANTI_DEST"

# 4. .agents/skills/ (asegurar formato <name>/SKILL.md)
SKILLS_DEST="${REPO_ROOT}/.agents/skills"
mkdir -p "$SKILLS_DEST"
SKILL_SOURCE="${SOURCE_DIR}/skills"
if [ -d "$SKILL_SOURCE" ]; then
    # Copiar archivos .md planos como <name>/SKILL.md
    find "$SKILL_SOURCE" -maxdepth 1 -type f -name "*.md" | while read -r FILE; do
        SKILL_NAME=$(basename "$FILE" .md)
        SKILL_DIR="$SKILLS_DEST/$SKILL_NAME"
        mkdir -p "$SKILL_DIR"
        cp "$FILE" "$SKILL_DIR/SKILL.md"
    done
    # Copiar directorios de skills
    find "$SKILL_SOURCE" -maxdepth 1 -mindepth 1 -type d | while read -r DIR; do
        DIR_NAME=$(basename "$DIR")
        mkdir -p "$SKILLS_DEST/$DIR_NAME"
        cp -r "$DIR/"* "$SKILLS_DEST/$DIR_NAME/" 2>/dev/null || true
    done
fi
echo "  -> Habilidades (Skills) convertidas y copiadas a $SKILLS_DEST"

echo "[OK] Sincronizacion completada."

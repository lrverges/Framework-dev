#!/usr/bin/env bash
set -euo pipefail

# ==============================================================================
# start-feature.sh - Aislamiento Físico con Git Worktrees (Superpowers)
# ==============================================================================

if [ -z "${1:-}" ]; then
  echo "[ERROR] Debes proporcionar el nombre de la feature."
  echo "Uso: ./scripts/start-feature.sh <feature-name>"
  echo "Ejemplo: ./scripts/start-feature.sh user-auth"
  exit 1
fi

FEATURE_NAME="$1"
BRANCH_NAME="feat/${FEATURE_NAME}"
WORKTREE_DIR=".worktrees/${FEATURE_NAME}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "================================================================================"
echo " 🚀 Creando Git Worktree Aislado: ${FEATURE_NAME}"
echo "================================================================================"

mkdir -p "${REPO_ROOT}/.worktrees"

# Verificar si el worktree o rama ya existen
if [ -d "${REPO_ROOT}/${WORKTREE_DIR}" ]; then
  echo "[AVISO] El worktree en ${WORKTREE_DIR} ya existe."
else
  # Crear rama y worktree
  git worktree add -b "${BRANCH_NAME}" "${REPO_ROOT}/${WORKTREE_DIR}" main
  echo "[OK] Worktree creado en ${WORKTREE_DIR} apuntando a la rama ${BRANCH_NAME}"
fi

# Copiar variables de entorno si existe .env.example
if [ -f "${REPO_ROOT}/.env.example" ] && [ ! -f "${REPO_ROOT}/${WORKTREE_DIR}/.env" ]; then
  cp "${REPO_ROOT}/.env.example" "${REPO_ROOT}/${WORKTREE_DIR}/.env"
  echo "[OK] Archivo .env inicializado desde .env.example dentro del worktree."
fi

echo "================================================================================"
echo " ✅ Entorno aislado listo. Para comenzar a trabajar en la feature ejecuta:"
echo ""
echo "    cd ${WORKTREE_DIR}"
echo ""
echo " La rama 'main' permanece 100% protegida e intacta en la raíz."
echo "================================================================================"

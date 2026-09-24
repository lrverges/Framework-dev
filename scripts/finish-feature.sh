#!/usr/bin/env bash
set -euo pipefail

# ==============================================================================
# finish-feature.sh - Verificación y Cierre Seguro de Feature (Superpowers)
# ==============================================================================

if [ -z "${1:-}" ]; then
  echo "[ERROR] Debes proporcionar el nombre de la feature."
  echo "Uso: ./scripts/finish-feature.sh <feature-name>"
  echo "Ejemplo: ./scripts/finish-feature.sh user-auth"
  exit 1
fi

FEATURE_NAME="$1"
BRANCH_NAME="feat/${FEATURE_NAME}"
WORKTREE_DIR=".worktrees/${FEATURE_NAME}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "================================================================================"
echo " 🏁 Verificando y Finalizando Feature: ${FEATURE_NAME}"
echo "================================================================================"

# 1. Ejecutar aduana determinista de verificación
echo "---> Ejecutando verificación obligatoria (Linter + Tests + Cobertura 85%+)..."
if [ -d "${REPO_ROOT}/${WORKTREE_DIR}" ]; then
  (cd "${REPO_ROOT}/${WORKTREE_DIR}" && bash "${REPO_ROOT}/scripts/verify.sh")
else
  bash "${REPO_ROOT}/scripts/verify.sh"
fi

echo "================================================================================"
echo " ✅ Verificación superada con éxito."
echo "================================================================================"
echo ""
echo "Instrucciones de integración:"
echo " 1. Realiza el push de tu rama si utilizas repositorio remoto:"
echo "    git push origin ${BRANCH_NAME}"
echo " 2. Crea el Pull Request hacia 'main'."
echo ""
read -p "¿Deseas limpiar y remover el worktree local ${WORKTREE_DIR}? (s/N): " -r CONFIRM
if [[ $CONFIRM =~ ^[sSyY]$ ]]; then
  git worktree remove "${REPO_ROOT}/${WORKTREE_DIR}" --force || true
  echo "[OK] Worktree ${WORKTREE_DIR} removido de forma segura."
fi

echo "================================================================================"
echo " Feature ${FEATURE_NAME} completada satisfactoriamente."
echo "================================================================================"

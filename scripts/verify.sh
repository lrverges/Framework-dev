#!/usr/bin/env bash
set -euo pipefail

# ==============================================================================
# scripts/verify.sh - Aduana Determinista de Calidad y Cobertura (LIDR & Superpowers)
# ==============================================================================

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if command -v python3 &>/dev/null; then
    python3 "${REPO_ROOT}/scripts/gatekeeper/gatekeeper.py" "$@"
else
    python "${REPO_ROOT}/scripts/gatekeeper/gatekeeper.py" "$@"
fi

#!/usr/bin/env python3
"""
Validador de estado de STACK.md.
Asegura que el stack tecnológico esté configurado antes de permitir compilación, pruebas o código.
"""

import sys
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def check_stack():
    repo_root = Path(__file__).resolve().parent.parent.parent
    stack_file = repo_root / "STACK.md"

    if not stack_file.exists():
        print("[ERROR CRÍTICO] No se encontró el archivo STACK.md en la raíz del proyecto.")
        sys.exit(1)

    content = stack_file.read_text(encoding="utf-8")

    # Verificar estado de configuración
    status_match = re.search(r"^\s*STATUS:\s*([A-Za-z_-]+)", content, re.MULTILINE)
    if not status_match:
        print("[ERROR] Formato inválido en STACK.md: Falta la directiva 'STATUS: <ESTADO>'.")
        sys.exit(1)

    status = status_match.group(1).strip().upper()

    if status == "UNCONFIGURED":
        print("\n================================================================================")
        print(" [GATEKEEPER BLOQUEO] STACK NO CONFIGURADO (STATUS: UNCONFIGURED)")
        print("================================================================================")
        print(" Queda terminantemente prohibido generar código en src/, pruebas en tests/ o")
        print(" contratos en contracts/ hasta que STACK.md sea completado y su estado cambie a:")
        print(" STATUS: CONFIGURED")
        print("================================================================================\n")
        sys.exit(1)

    if status != "CONFIGURED":
        print(f"[ERROR] Estado desconocido en STACK.md: '{status}'. Debe ser 'UNCONFIGURED' o 'CONFIGURED'.")
        sys.exit(1)

    # Si está CONFIGURED, verificar que no queden marcadores [PENDIENTE]
    pendientes = re.findall(r"\[PENDIENTE\]", content, re.IGNORECASE)
    if pendientes:
        print(f"\n[ADVERTENCIA] STACK.md está marcado como CONFIGURED pero contiene {len(pendientes)} campo(s) [PENDIENTE].")
        print("Por favor complete todas las secciones antes de pasar a producción.")

    print(f"[OK] STACK.md validado correctamente. Estado: {status}")
    sys.exit(0)

if __name__ == "__main__":
    check_stack()

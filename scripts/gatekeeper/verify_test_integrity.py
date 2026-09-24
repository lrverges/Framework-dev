#!/usr/bin/env python3
"""
Verificador de integridad criptográfica de pruebas (Agentic TDD).
Previene que agentes de implementación modifiquen o relajen pruebas para forzar el aprobado.
"""

import sys
import os
import json
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def compute_sha256(filepath: Path) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_test_files(tests_dir: Path):
    ignored_names = {"test_manifest.json", ".gitkeep"}
    test_files = []
    for root, _, files in os.walk(tests_dir):
        for f in files:
            if f in ignored_names or f.endswith(".pyc") or f.endswith(".swp"):
                continue
            test_files.append(Path(root) / f)
    return sorted(test_files)

def seal_manifest(tests_dir: Path, manifest_path: Path):
    test_files = find_test_files(tests_dir)
    records = {}

    for file_path in test_files:
        rel_path = file_path.relative_to(tests_dir).as_posix()
        records[rel_path] = compute_sha256(file_path)

    manifest_data = {
        "version": "1.0",
        "description": "Registro criptográfico de inmutabilidad de pruebas (Agentic TDD). Generado y sellado por el Test Engineer.",
        "sealed_at": datetime.now(timezone.utc).isoformat(),
        "files": records
    }

    manifest_path.write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK] Manifiesto de pruebas SELLADO exitosamente ({len(records)} archivo(s) registrados en {manifest_path.name}).")
    for path, digest in records.items():
        print(f"  - {path}: {digest[:12]}...")

def check_manifest(tests_dir: Path, manifest_path: Path) -> bool:
    if not manifest_path.exists():
        print("[ERROR] No se encontró tests/test_manifest.json.")
        return False

    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Error al leer test_manifest.json: {e}")
        return False

    registered_files = manifest_data.get("files", {})
    current_files = find_test_files(tests_dir)

    if not registered_files and not current_files:
        print("[OK] No hay pruebas registradas aún en el repositorio.")
        return True

    if not registered_files and current_files:
        print("[ERROR] Existen archivos de prueba pero el manifiesto no ha sido sellado.")
        print("El Test Engineer debe ejecutar: python scripts/gatekeeper/verify_test_integrity.py --seal")
        return False

    violations = []
    current_rel_paths = set()

    for file_path in current_files:
        rel_path = file_path.relative_to(tests_dir).as_posix()
        current_rel_paths.add(rel_path)

        if rel_path not in registered_files:
            violations.append(f"ARCHIVO NO REGISTRADO / AÑADIDO: {rel_path}")
            continue

        current_hash = compute_sha256(file_path)
        expected_hash = registered_files[rel_path]

        if current_hash != expected_hash:
            violations.append(
                f"MODIFICACIÓN NO AUTORIZADA DE TEST: {rel_path} (esperado {expected_hash[:10]}..., actual {current_hash[:10]}...)"
            )

    for registered_path in registered_files:
        if registered_path not in current_rel_paths:
            violations.append(f"ARCHIVO DE TEST ELIMINADO: {registered_path}")

    if violations:
        print("\n================================================================================")
        print(" [CRITICAL GATEKEEPER VIOLATION] FALLO DE INMUTABILIDAD EN AGENTIC TDD")
        print("================================================================================")
        print(" Se detectaron alteraciones no autorizadas en las pruebas unitarias/integración:")
        for v in violations:
            print(f"   [!] {v}")
        print("\n LEY: El Coder tiene estrictamente prohibido alterar tests para hacerlos pasar.")
        print(" Solo el 'Test Engineer' está autorizado a modificar pruebas y re-sellar el manifest.")
        print("================================================================================\n")
        return False

    print(f"[OK] Integridad de pruebas verificada. Todos los {len(registered_files)} tests se mantienen inmutables.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Verificador de integridad de pruebas Agentic TDD.")
    parser.add_argument("--seal", "--init", action="store_true", help="Sellar el manifiesto con los hashes actuales de tests.")
    parser.add_argument("--check", action="store_true", default=True, help="Verificar la inmutabilidad de los tests contra el manifiesto.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    tests_dir = repo_root / "tests"
    manifest_path = tests_dir / "test_manifest.json"

    if args.seal:
        seal_manifest(tests_dir, manifest_path)
        sys.exit(0)
    else:
        success = check_manifest(tests_dir, manifest_path)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

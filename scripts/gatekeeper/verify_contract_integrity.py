#!/usr/bin/env python3
"""
Verificador de integridad criptográfica de contratos y especificaciones.
Previene que se modifiquen los contratos sin autorización.
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

def find_contract_files(contracts_dir: Path):
    ignored_names = {"contract_manifest.json", ".gitkeep"}
    contract_files = []
    if not contracts_dir.exists():
        return contract_files
    for root, _, files in os.walk(contracts_dir):
        for f in files:
            if f in ignored_names or f.endswith(".pyc") or f.endswith(".swp"):
                continue
            contract_files.append(Path(root) / f)
    return sorted(contract_files)

def seal_manifest(contracts_dir: Path, manifest_path: Path):
    if not contracts_dir.exists():
        contracts_dir.mkdir(parents=True, exist_ok=True)
        
    contract_files = find_contract_files(contracts_dir)
    records = {}

    for file_path in contract_files:
        rel_path = file_path.relative_to(contracts_dir).as_posix()
        records[rel_path] = compute_sha256(file_path)

    manifest_data = {
        "version": "1.0",
        "description": "Registro criptográfico de inmutabilidad de contratos. Generado y sellado por el Arquitecto.",
        "sealed_at": datetime.now(timezone.utc).isoformat(),
        "files": records
    }

    manifest_path.write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[OK] Manifiesto de contratos SELLADO exitosamente ({len(records)} archivo(s) registrados en {manifest_path.name}).")
    for path, digest in records.items():
        print(f"  - {path}: {digest[:12]}...")

def check_manifest(contracts_dir: Path, manifest_path: Path) -> bool:
    if not manifest_path.exists():
        print("[ERROR] No se encontró contracts/contract_manifest.json.")
        return False

    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[ERROR] Error al leer contract_manifest.json: {e}")
        return False

    registered_files = manifest_data.get("files", {})
    current_files = find_contract_files(contracts_dir)

    if not registered_files and not current_files:
        print("[OK] No hay contratos registrados aún en el repositorio.")
        return True

    if not registered_files and current_files:
        print("[ERROR] Existen archivos de contratos pero el manifiesto no ha sido sellado.")
        print("Debes ejecutar: python scripts/gatekeeper/verify_contract_integrity.py --seal")
        return False

    violations = []
    current_rel_paths = set()

    for file_path in current_files:
        rel_path = file_path.relative_to(contracts_dir).as_posix()
        current_rel_paths.add(rel_path)

        if rel_path not in registered_files:
            violations.append(f"ARCHIVO NO REGISTRADO / AÑADIDO: {rel_path}")
            continue

        current_hash = compute_sha256(file_path)
        expected_hash = registered_files[rel_path]

        if current_hash != expected_hash:
            violations.append(
                f"MODIFICACIÓN NO AUTORIZADA DE CONTRATO: {rel_path} (esperado {expected_hash[:10]}..., actual {current_hash[:10]}...)"
            )

    for registered_path in registered_files:
        if registered_path not in current_rel_paths:
            violations.append(f"ARCHIVO DE CONTRATO ELIMINADO: {registered_path}")

    if violations:
        print("\n================================================================================")
        print(" [CRITICAL GATEKEEPER VIOLATION] FALLO DE INMUTABILIDAD EN CONTRATOS")
        print("================================================================================")
        print(" Se detectaron alteraciones no autorizadas en los contratos:")
        for v in violations:
            print(f"   [!] {v}")
        print("\n LEY: El Coder tiene estrictamente prohibido alterar contratos.")
        print(" Solo el 'Arquitecto' o el 'Lead' está autorizado a modificarlos y re-sellar el manifest.")
        print("================================================================================\n")
        return False

    print(f"[OK] Integridad de contratos verificada. Todos los {len(registered_files)} contratos se mantienen inmutables.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Verificador de integridad de contratos.")
    parser.add_argument("--seal", action="store_true", help="Sellar el manifiesto con los hashes actuales de contratos.")
    parser.add_argument("--check", action="store_true", default=True, help="Verificar la inmutabilidad de los contratos contra el manifiesto.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    contracts_dir = repo_root / "contracts"
    manifest_path = contracts_dir / "contract_manifest.json"

    if args.seal:
        seal_manifest(contracts_dir, manifest_path)
        sys.exit(0)
    else:
        success = check_manifest(contracts_dir, manifest_path)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

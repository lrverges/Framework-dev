#!/usr/bin/env python3
"""
Validador determinista de cobertura de código.
Falla si la cobertura de líneas es menor a 85%.
"""

import sys
import os
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

MIN_COVERAGE = 85.0

def find_test_files(tests_dir: Path):
    ignored_names = {"test_manifest.json", ".gitkeep"}
    test_files = []
    if not tests_dir.exists():
        return test_files
    for root, dirs, files in os.walk(tests_dir):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        for f in files:
            if f in ignored_names or f.endswith(".pyc") or f.endswith(".swp"):
                continue
            test_files.append(Path(root) / f)
    return test_files

def main():
    print(f"[INFO] Evaluando umbral estricto de cobertura de código: {MIN_COVERAGE}%")
    cov_file = Path("coverage.xml")
    repo_root = Path(__file__).resolve().parent.parent.parent
    tests_dir = repo_root / "tests"

    if cov_file.exists():
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(cov_file)
            rate = float(tree.getroot().attrib.get("line-rate", 0)) * 100
            if rate < MIN_COVERAGE:
                print(f"[ERROR CRÍTICO] Cobertura de líneas ({rate:.2f}%) inferior al umbral mínimo ({MIN_COVERAGE}%).")
                sys.exit(1)
            print(f"[OK] Cobertura aprobada: {rate:.2f}% >= {MIN_COVERAGE}%")
        except Exception as e:
            print(f"[ERROR] Error al procesar coverage.xml: {e}")
            sys.exit(1)
    else:
        test_files = find_test_files(tests_dir)
        if test_files:
            print(f"[ERROR CRÍTICO] Existen {len(test_files)} archivo(s) de prueba pero no se encontró coverage.xml. Las pruebas no se ejecutaron con cobertura.")
            sys.exit(1)
        else:
            print(f"[OK] No hay pruebas ni coverage.xml. Umbral de cobertura configurado determinísticamente a {MIN_COVERAGE}%.")
    sys.exit(0)

if __name__ == "__main__":
    main()

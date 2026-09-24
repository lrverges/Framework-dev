#!/usr/bin/env python3
"""
Orquestador Determinista del Gatekeeper (Aduana de Calidad Anti-Vibecoding).
Ejecuta la secuencia de verificación completa:
1. Validación de STACK.md
2. Verificación de inmutabilidad criptográfica de tests (Agentic TDD)
3. Verificación de inmutabilidad de contratos
4. Análisis estático (Linter + Type Checker)
5. Ejecución de tests + Coverage
"""

import sys
import subprocess
import argparse
from pathlib import Path

# Asegurar codificación UTF-8 en Windows y cualquier entorno
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def run_step(step_name: str, cmd: list) -> bool:
    print(f"\n---> [GATEKEEPER STEP] {step_name}")
    print(f"     [CMD] {' '.join(cmd)}")
    try:
        res = subprocess.run(cmd, capture_output=False, text=True)
        if res.returncode == 0:
            print(f" [PASSED] {step_name}")
            return True
        else:
            print(f" [FAILED] {step_name} (Codigo de salida: {res.returncode})")
            return False
    except Exception as e:
        print(f" [ERROR] Excepcion ejecutando {step_name}: {e}")
        return False

def read_stack_config(repo_root: Path) -> dict:
    import re
    stack_path = repo_root / "STACK.md"
    config = {
        "status": "UNCONFIGURED",
        "linter": None,
        "type_checker": None,
        "test_runner": None
    }
    
    if not stack_path.exists():
        return config

    content = stack_path.read_text(encoding="utf-8")
    # Buscar la línea canónica "STATUS: <VALOR>" (no texto instructivo)
    status_match = re.search(r"^\s*STATUS:\s*([A-Za-z_-]+)", content, re.MULTILINE)
    if status_match:
        config["status"] = status_match.group(1).strip().upper()

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("- Formateador y Linter:"):
            val = line.split(":", 1)[1].strip()
            if "[PENDIENTE]" not in val:
                config["linter"] = val
        elif stripped.startswith("- Verificador Estático de Tipos"):
            val = line.split(":", 1)[1].strip()
            if "[PENDIENTE]" not in val:
                config["type_checker"] = val
        elif stripped.startswith("- Framework de Pruebas"):
            val = line.split(":", 1)[1].strip()
            if "[PENDIENTE]" not in val:
                config["test_runner"] = val

    return config

def main():
    parser = argparse.ArgumentParser(description="Orquestador Determinista del Gatekeeper")
    parser.add_argument("--strict", action="store_true", help="Falla si las herramientas en STACK.md no están configuradas.")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent.parent
    scripts_dir = repo_root / "scripts" / "gatekeeper"
    python_bin = sys.executable

    print("\n================================================================================")
    print(" [GATEKEEPER] INICIANDO ADUANA DETERMINISTA (DETERMINISTIC GATEKEEPER)")
    print("================================================================================")

    stack_config = read_stack_config(repo_root)
    all_passed = True

    # Paso 1: Validación de STACK.md (informativo — determina si los pasos dinámicos corren)
    stack_ok = run_step("Validacion de STACK.md", [python_bin, str(scripts_dir / "check_stack.py")])
    if not stack_ok and stack_config["status"] == "UNCONFIGURED":
        print(" [INFO] STACK.md esta UNCONFIGURED — estado legítimo para un proyecto nuevo.")
        print("        Los pasos de linter, type checker y test runner se omitirán.")
    elif not stack_ok:
        all_passed = False

    # Pasos 2-3: Integridad criptográfica (siempre corren, sin detenerse en fallo)
    integrity_steps = [
        ("Inmutabilidad de Pruebas (Agentic TDD)", [python_bin, str(scripts_dir / "verify_test_integrity.py")]),
        ("Inmutabilidad de Contratos", [python_bin, str(scripts_dir / "verify_contract_integrity.py")]),
    ]

    for name, cmd in integrity_steps:
        if not run_step(name, cmd):
            all_passed = False

    # Paso 4: Análisis Estático (Linter + Type Checker)
    print(f"\n---> [GATEKEEPER STEP] Analisis Estatico (Linter + Type Checker)")
    if stack_config["status"] == "UNCONFIGURED" and not args.strict:
        print(" [SKIPPED] STACK.md esta UNCONFIGURED. Saltando analisis estatico.")
    else:
        # Linter
        if stack_config["linter"]:
            print(f"     [RUN] Linter: {stack_config['linter']}")
            try:
                res = subprocess.run(stack_config['linter'], shell=True, cwd=str(repo_root), capture_output=False, text=True)
                if res.returncode != 0:
                    print(f" [FAILED] Linter (Codigo de salida: {res.returncode})")
                    all_passed = False
                else:
                    print(f" [PASSED] Linter")
            except Exception as e:
                print(f" [ERROR] Excepcion ejecutando Linter: {e}")
                all_passed = False
        else:
            msg = " [ADVERTENCIA] Comando de Linter no configurado o [PENDIENTE]."
            print(msg)
            if args.strict:
                all_passed = False

        # Type Checker
        if stack_config["type_checker"]:
            print(f"     [RUN] Type Checker: {stack_config['type_checker']}")
            try:
                res = subprocess.run(stack_config['type_checker'], shell=True, cwd=str(repo_root), capture_output=False, text=True)
                if res.returncode != 0:
                    print(f" [FAILED] Type Checker (Codigo de salida: {res.returncode})")
                    all_passed = False
                else:
                    print(f" [PASSED] Type Checker")
            except Exception as e:
                print(f" [ERROR] Excepcion ejecutando Type Checker: {e}")
                all_passed = False
        else:
            msg = " [ADVERTENCIA] Comando de Type Checker no configurado o [PENDIENTE]."
            print(msg)
            if args.strict:
                all_passed = False

    # Paso 5: Ejecución de tests + Coverage
    print(f"\n---> [GATEKEEPER STEP] Ejecucion de Tests + Coverage")
    if stack_config["status"] == "UNCONFIGURED" and not args.strict:
        print(" [SKIPPED] STACK.md esta UNCONFIGURED. Saltando tests y coverage.")
    else:
        if stack_config["test_runner"]:
            print(f"     [RUN] Tests: {stack_config['test_runner']}")
            try:
                res = subprocess.run(stack_config['test_runner'], shell=True, cwd=str(repo_root), capture_output=False, text=True)
                if res.returncode != 0:
                    print(f" [FAILED] Tests (Codigo de salida: {res.returncode})")
                    all_passed = False
                else:
                    print(f" [PASSED] Tests")
            except Exception as e:
                print(f" [ERROR] Excepcion ejecutando Tests: {e}")
                all_passed = False
                
            if not run_step("Check Coverage", [python_bin, str(scripts_dir / "check_coverage.py")]):
                all_passed = False
        else:
            msg = " [ADVERTENCIA] Comando de Tests no configurado o [PENDIENTE]."
            print(msg)
            if args.strict:
                all_passed = False

    print("\n================================================================================")
    if all_passed:
        print(" [EXITO] TODAS LAS ADUANAS SUPERADAS: El proyecto cumple las normas del sistema.")
        print("================================================================================\n")
        sys.exit(0)
    else:
        print(" [FALLO] ADUANA RECHAZADA: Corrige los errores antes de continuar o desplegar.")
        print("================================================================================\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

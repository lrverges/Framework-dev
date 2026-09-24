# AGENTS.md - Protocolo y Leyes del Repositorio (Anti-Vibecoding)

Este repositorio opera bajo un modelo de ingeniería de software de alta fidelidad, diseñado para evitar el "vibecoding" (programar por intuición sin pruebas, especificaciones ni contratos).

Todo agente de IA (Antigravity, subagentes o sistemas automatizados) DEBE cumplir estrictamente estas leyes.

> [!NOTE]
> **Ley de Redirección de specs**: Si cualquier documento, script o agente hace referencia a `specs/` (sin punto), debe interpretarse como `.specs/`. El directorio `specs/` ha sido eliminado; la ubicación canónica es `.specs/` con el ciclo `active/` -> `approved/`.

---

## Leyes Inmutables de los Agentes

1. **Ley del Stack (`STACK.md`)**:
   - Si `STACK.md` indica `STATUS: UNCONFIGURED`, está TERMINANTEMENTE PROHIBIDO escribir código en `src/`, pruebas en `tests/` o contratos en `contracts/`.
   - La única acción permitida es colaborar con el usuario para definir el stack y cambiar el estado a `STATUS: CONFIGURED`.

2. **Ley del Desarrollo Dirigido por Especificaciones (Spec-Driven Development - SDD)**:
   - Ninguna funcionalidad se implementa sin un documento de especificación formal en `.specs/` y un contrato de datos/interfaz en `contracts/` (los cuales incluyen `contracts/api-spec.yml` y `contracts/data-model.md`).
   - Las especificaciones deben incluir criterios de aceptación verificables (Given-When-Then / Gherkin).

3. **Ley de Inmutabilidad de Pruebas (Agentic TDD Inmutable)**:
   - Las pruebas unitarias e integración se escriben primero (fase RED) y reflejan la especificación.
   - Una vez escritas y registradas en `tests/test_manifest.json`, **EL AGENTE IMPLEMENTADOR TIENE ESTRICTAMENTE PROHIBIDO MODIFICAR LAS PRUEBAS**.
   - Si una prueba falla durante la fase GREEN, el error está en la implementación (`src/`), NUNCA en la prueba. Alterar pruebas para "hacerlas pasar" se considera una violación crítica de protocolo.

4. **Ley de Verificación de Documentación Oficial (Anti-Alucinación)**:
   - Prohibido adivinar firmas de métodos, flags de CLI o compatibilidades de versiones.
   - Antes de usar una biblioteca, API o sintaxis externa, el agente debe consultar la documentación oficial mediante web search o la skill `official-doc-verifier`.

5. **Ley del Deterministic Gatekeeping**:
   - Todo cambio debe pasar por el filtro determinista:
     1. Formateo y linter con cero warnings tolerados.
     2. Verificador estático de tipos (type checker) en modo estricto.
     3. Comprobación de integridad de pruebas (`verify_test_integrity.py`).
     4. Comprobación de integridad de contratos (`verify_contract_integrity.py`).
     5. Suite completa de pruebas en verde.
   - Ejecutar el Gatekeeper (`python scripts/gatekeeper/gatekeeper.py`) antes de dar una tarea por completada.

---

## Flujo Operativo de Subagentes (SOPs)

> [!NOTE]
> `ai-specs/` es la fuente canónica para los SOPs y skills de este proyecto.

1. **Spec Architect**: Define `.specs/*.md` y `contracts/*`.
2. **Test Engineer**: Desarrolla pruebas contra los contratos y genera el `test_manifest.json` (fase RED).
3. **Implementation Coder**: Escribe código en `src/` hasta que los tests pasen (fase GREEN), sin tocar `tests/`.
4. **Security Auditor**: Audita seguridad, fugas de recursos, sincronización documental y performance (`deep-code-auditor`).
5. **Adversarial Reviewer**: Ejecuta auditoría adversaria en dos etapas: Spec Compliance y Red Team Security (ver `ai-specs/agents/adversarial-reviewer.md`).
6. **Gatekeeper**: Ejecuta la suite de verificación determinista en el sandbox.

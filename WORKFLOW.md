# Flujo de Trabajo Operativo Integral (Anti-Vibecoding Workflow)

Este documento detalla el ciclo de vida de desarrollo de extremo a extremo que rige este repositorio, combinando **Spec-Driven Development (SDD)**, **Agentic TDD con Inmutabilidad Criptográfica**, **Aislamiento Físico por Worktrees (Superpowers)** y **Verificación Adversaria (LIDR-Academy)**.

---

## 🔄 El Ciclo de 8 Pasos

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 1. Idea o Ticket (Jira / GitHub Issues)                                      │
 │    └──> Skill `enrich-us` -> Guarda en `.specs/active/SPEC-XXX.md`           │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 2. Aprobación Humana de la Especificación                                   │
 │    └──> Mover a `.specs/approved/SPEC-XXX.md`                                │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 3. Inicio de Rama Aislada (Git Worktree - Superpowers)                      │
 │    └──> Ejecutar: `./scripts/start-feature.sh <nombre>`                     │
 │    └──> Trabajar en `.worktrees/<nombre>/` protegiendo `main`               │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 4. QA Agent: Desarrollo de Pruebas (Fase RED Inmutable)                     │
 │    └──> Tests en `tests/unit/` y `tests/integration/`                       │
 │    └──> Sellado criptográfico: `python scripts/gatekeeper/verify_test_integrity.py --seal`
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 5. Dev Agent: Implementación en `src/` (Fase GREEN)                         │
 │    └──> Código en `src/` hasta que los tests pasen (prohibido tocar tests)  │
 │    └──> Si surgen bugs o regresiones: Activar skill `systematic-debugging`  │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 6. Aduana Local Determinista                                                │
 │    └──> Ejecutar: `python scripts/gatekeeper/gatekeeper.py`                 │
 │    └──> Linter, Type checker, Integridad de Contratos y Cobertura >= 85%    │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 7. Auditoría Adversaria de Dos Etapas (Rol: `adversarial-reviewer`)         │
 │    ├── Etapa 1: Spec Compliance Review (Detección de Scope Creep)           │
 │    └── Etapa 2: Red Team Security Review (Inyección, Concurrencia, Memoria) │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 8. Cierre y Pull Request                                                    │
 │    └──> Ejecutar: `./scripts/finish-feature.sh <nombre>`                    │
 │    └──> Limpieza del worktree y merge a `main` tras aprobación              │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Descripción Detallada de los Pasos

### Paso 1: Idea o Ticket -> Skill `enrich-us` -> `.specs/active/`
- Cualquier necesidad, bug report o iniciativa informal se procesa a través de la habilidad [ai-specs/skills/enrich-us.md](file:///c:/Finance/ai-specs/skills/enrich-us.md).
- Produce un documento de especificación formal con criterios de aceptación `Given-When-Then`, casos de borde, validaciones y análisis de impacto en [contracts/data-model.md](file:///c:/Finance/contracts/data-model.md) y [contracts/api-spec.yml](file:///c:/Finance/contracts/api-spec.yml).
- El archivo se guarda en `.specs/active/`.

### Paso 2: Aprobación Humana -> `.specs/approved/`
- El desarrollador principal o tech lead revisa la especificación generada en `.specs/active/`.
- Una vez validada y sin dudas pendientes, se mueve a `.specs/approved/`.
- **Regla inmutable**: Ningún agente puede implementar código de una spec que no esté en `.specs/approved/`.

### Paso 3: Inicio de Rama Aislada -> `./scripts/start-feature.sh <nombre>`
- Se utiliza el script de Git Worktrees para crear un espacio de trabajo físicamente aislado en `.worktrees/<nombre>`.
- Esto garantiza que la rama `main` en la raíz se mantenga limpia e intocada.

### Paso 4: QA Agent -> Tests en `tests/` (Fase RED Inmutable)
- El rol de Test Engineer escribe las pruebas unitarias y de integración exclusivamente a partir de los escenarios aprobados en la spec y los contratos en `contracts/`.
- Las pruebas **deben fallar** (fase RED).
- Se sella el manifiesto con `python scripts/gatekeeper/verify_test_integrity.py --seal` generando los hashes SHA-256 en `tests/test_manifest.json`.

### Paso 5: Dev Agent -> Código en `src/` (Fase GREEN)
- El agente de desarrollo escribe el código mínimo necesario dentro de `src/` para hacer pasar las pruebas.
- **Prohibición crítica**: El Dev Agent tiene estrictamente prohibido alterar o eliminar pruebas de `tests/`.
- **Depuración Científica**: Si se producen bugs inesperados, se prohíbe el "shotgun debugging" y se debe aplicar obligatoriamente el protocolo de 4 pasos de [ai-specs/skills/systematic-debugging.md](file:///c:/Finance/ai-specs/skills/systematic-debugging.md).

### Paso 6: Aduana Local -> `python scripts/gatekeeper/gatekeeper.py`
- Ejecución determinista del script de verificación.
- Filtra linter, formato y type checker estricto con tolerancia cero a warnings y errores.
- Valida la integridad de contratos usando `verify_contract_integrity.py`.
- Ejecuta los tests evaluando la cobertura de código (coverage): si la cobertura total de líneas es inferior al **85%**, la aduana rechaza el commit inmediatamente.

### Paso 7: Auditoría -> Rol `adversarial-reviewer`
- El agente independiente ejecuta la auditoría en dos etapas:
  1. **Spec Compliance**: Verifica que no exista *scope creep* (funciones, endpoints o lógicas no solicitadas en la spec aprobada).
  2. **Adversarial Red Team**: Intenta romper activamente la solución probando condiciones de carrera, inputs maliciosos o cargas concurrentes.

### Paso 8: Cierre -> `./scripts/finish-feature.sh` -> PR Final
- Ejecuta la verificación final en el worktree.
- Tras la confirmación, asiste en la creación del pull request y limpia el worktree local de forma segura.

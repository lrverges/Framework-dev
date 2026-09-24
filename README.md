# Universal Anti-Vibecoding Framework 🛡️

Marco de trabajo universal de ingeniería de software de alta fidelidad asistido por IA. Diseñado para erradicar el *"vibecoding"* (desarrollo por intuición sin pruebas ni especificaciones) mediante **desarrollo guiado por especificaciones (SDD)**, **pruebas inmutables (Agentic TDD)**, **pruebas E2E de navegador**, **diseño de módulos profundos** y **aduanas de calidad deterministas**.

---

## 🏛️ Los Pilares Metodológicos

| Pilar | Mecanismo | Propósito |
| :--- | :--- | :--- |
| **1. Ley del Stack** | [STACK.md](file:///c:/Finance/STACK.md) | Bloqueo absoluto de generación de código/tests hasta definir y acordar formalmente el stack (`STATUS: CONFIGURED`). |
| **2. Spec-Driven Development (SDD)** | `.specs/` y `contracts/` | Cero ambigüedad: toda funcionalidad parte de especificaciones Gherkin (`Dado-Cuando-Entonces`) y contratos de interfaz. |
| **3. Agentic TDD Inmutable** | `tests/` y `test_manifest.json` | Pruebas escritas primero (Fase RED) y selladas criptográficamente con SHA-256. El agente implementador tiene prohibido alterar las pruebas. |
| **4. Pruebas E2E de Navegador** | `tests/e2e/` (Playwright) | Verificación end-to-end de flujos de usuario, modo offline, Service Worker y sincronización en navegador real. |
| **5. Diseño de Módulos Profundos** | Skills `codebase-design` y `domain-modeling` | Arquitectura desacoplada, lenguaje ubicuo en `CONTEXT.md` y módulos con interfaces pequeñas que ocultan alta complejidad. |
| **6. Deterministic Gatekeeping** | [scripts/gatekeeper/gatekeeper.py](file:///c:/Finance/scripts/gatekeeper/gatekeeper.py) | Aduana automatizada de linter, type-checker estricto, verificación de integridad y cobertura $\ge 85\%$. |

---

## 🔄 El Ciclo Completo de Desarrollo (End-to-End)

El flujo operativo se estructura en **8 fases deterministas**:

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 0. Acuerdo del Stack Tecnológico (STACK.md)                                 │
 │    └──> Humano y Agente definen runtime, frameworks, DB y gatekeeping       │
 │    └──> STATUS: CONFIGURED (Habilita el inicio del proyecto)                │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 1. Captura de Requisitos y Dominio                                          │
 │    └──> Skill `enrich-us` -> Redacción de `.specs/active/SPEC-XXX.md`        │
 │    └──> Skill `domain-modeling` -> Glosario ubicuo en `CONTEXT.md`          │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 2. Aprobación Humana de la Especificación & Contratos                       │
 │    └──> Humano valida y promueve a `.specs/approved/SPEC-XXX.md`            │
 │    └──> Formalización y sellado criptográfico de `contracts/`               │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 3. Aislamiento Físico del Entorno (Git Worktree / Sandbox)                  │
 │    └──> Ejecutar: `./scripts/start-feature.sh <nombre>`                     │
 │    └──> Rama de trabajo aislada en `.worktrees/<nombre>/`                   │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 4. Fase RED: Ingeniería de Pruebas Inmutables (Test Engineer)               │
 │    ├── Pruebas Unitarias/Componentes: Vitest + `react-testing`              │
 │    ├── Pruebas End-to-End (E2E): Playwright + `e2e-testing` (Offline/Sync)  │
 │    └── Sellado Criptográfico: `verify_test_integrity.py --seal`             │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 5. Fase GREEN: Implementación (Implementation Coder)                        │
 │    └──> Código en `src/` aplicando `codebase-design` (módulos profundos)    │
 │    └──> Ley Inmutable: Prohibido modificar o relajar los tests en `tests/`  │
 │    └──> Depuración científica con `systematic-debugging` ante errores       │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 6. Aduana Determinista Local (Deterministic Gatekeeper)                     │
 │    └──> Ejecutar: `python scripts/gatekeeper/gatekeeper.py`                 │
 │    └──> Linter (0 warnings) + Typecheck estricto + Cobertura >= 85%         │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 7. Auditoría Adversaria y de Seguridad                                      │
 │    ├── Skill `deep-code-auditor`: OWASP, fugas de recursos, sincronización  │
 │    └── Rol `adversarial-reviewer`: Spec compliance review y Red Teaming     │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ 8. Revisión Final Humana y Cierre (Merge a main)                            │
 │    └──> Humano revisa reporte del Gatekeeper y funcionamiento visual        │
 │    └──> Ejecutar: `./scripts/finish-feature.sh <nombre>`                    │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 👤 Puntos Críticos de Intervención Humana (Human-in-the-Loop)

Los agentes de IA operan con alta autonomía técnica, pero el control arquitectónico, funcional y de negocio permanece siempre en manos del humano a través de **5 Aduanas Humanas (Human Gates)**:

```text
  [Idea / Problema]
          │
          ▼
   ┌─────────────┐
   │ HITL GATE 1 │  ---> Validación y Acuerdo del Stack Tecnológico (STACK.md)
   └─────────────┘
          │
          ▼
   ┌─────────────┐
   │ HITL GATE 2 │  ---> Aprobación Formal de Especificaciones (.specs/approved/)
   └─────────────┘
          │
          ▼
   ┌─────────────┐
   │ HITL GATE 3 │  ---> Arbitraje del Lenguaje Ubicuo y Decisiones Clave (CONTEXT.md / ADRs)
   └─────────────┘
          │
          ▼
  [Fase RED / GREEN / Gatekeeper]
          │
          ▼
   ┌─────────────┐
   │ HITL GATE 4 │  ---> Resolución de Cuellos de Botella o Casos de Borde Inesperados
   └─────────────┘
          │
          ▼
   ┌─────────────┐
   │ HITL GATE 5 │  ---> Aprobación Final de Despliegue y Merge (Pull Request Sign-off)
   └─────────────┘
          │
          ▼
     [Producción]
```

### Detalle de las Intervenciones Humanas:

| Punto de Intervención | Momento del Ciclo | Responsabilidad del Humano | Herramientas / Artefactos |
| :--- | :--- | :--- | :--- |
| **1. Definición del Stack** | Inicio del proyecto | Valida que las tecnologías elegidas (frontend, persistencia, runtime, testing) sean las correctas antes de autorizar `STATUS: CONFIGURED`. | [STACK.md](file:///c:/Finance/STACK.md) |
| **2. Aprobación de Especificación** | Antes de escribir tests o código | Lee la especificación generada en `.specs/active/`, verifica los criterios Gherkin, asegura que no falten casos de uso de negocio y la traslada a `.specs/approved/`. | `.specs/active/` -> `.specs/approved/` |
| **3. Lenguaje de Dominio y ADRs** | Durante el diseño de arquitectura | Resuelve discrepancias terminológicas del negocio (ej. *"¿qué entendemos exactamente por alquiler eventual?"*) y valida las decisiones difíciles de revertir en los ADRs. | [CONTEXT.md](file:///c:/Finance/CONTEXT.md), `docs/adr/` |
| **4. Supervisión de Pruebas** | Tras la fase RED | Verifica que las costuras públicas (*seams*) y los flujos críticos testeados (especialmente flujos monetarios y de sincronización) reflejen el comportamiento deseado. | `tests/`, `test_manifest.json` |
| **5. Visto Bueno Final (Merge Gate)** | Antes de integrar a `main` | Revisa el reporte determinista del Gatekeeper, los artefactos E2E (capturas/videos de Playwright), y aprueba el Pull Request final. | Reporte Gatekeeper, PR Review |

---

## 🧰 Catálogo de Skills Integradas en el Repositorio

Ubicadas en [.agents/skills/](file:///c:/Finance/.agents/skills/) y [ai-specs/skills/](file:///c:/Finance/ai-specs/skills/):

* **`idea-refine`**: Refinamiento y cuestionamiento socrático de ideas vagas, delimitación de alcance de MVP, premisas críticas y lista explícita de "No Hacer" (*Not Doing*).
* **`planning-and-task-breakdown`**: Desglose sistemático de requerimientos en "Vertical Slices" con dimensionamiento de tareas (XS, S, M, L) y puntos de control/verificación con el humano.
* **`enrich-us`**: Transformación de requerimientos informales en especificaciones formales con escenarios Gherkin.
* **`domain-modeling`**: Construcción activa del modelo de dominio y glosario en `CONTEXT.md`, junto con registros de arquitectura en `docs/adr/`.
* **`codebase-design`**: Diseño de módulos profundos (*deep modules*) con interfaces pequeñas y alta cohesión interna (*Design It Twice*).
* **`api-and-interface-design`**: Diseño canónico de contratos de interfaz y APIs REST/OpenAPI, claves de idempotencia para flujos financieros y tipos de TypeScript seguros (*Branded Types* y *Discriminated Unions*).
* **`code-simplification`**: Principio de *Chesterton's Fence* para simplificar y refactorizar código sin romper invariantes, eliminando complejidad y abstracciones innecesarias sin tocar pruebas.
* **`official-doc-verifier`**: Protocolo anti-alucinación que consulta documentación oficial antes de utilizar APIs externas.
* **`deep-code-auditor`**: Auditoría profunda de código para seguridad (OWASP), detección de fugas de recursos y trazabilidad documental.
* **`systematic-debugging`**: Depuración científica en 4 pasos (formulación de hipótesis, reproducción mínima en test, diagnóstico y corrección quirúrgica).
* **`react-testing`**: Pruebas de componentes y hooks en React con React Testing Library y Vitest, incluyendo mocking de APIs con MSW y límites de error.
* **`e2e-testing`**: Automatización end-to-end con Playwright, Page Object Model (POM), manejo anti-flakiness, captura de videos/trazas y pruebas de flujos críticos.
* **`a11y-playwright-testing`**: Verificación automatizada de accesibilidad WCAG 2.2 AA en Playwright con `axe-core`, incluyendo gestión de foco y navegación por teclado.
* **`performance-optimization`**: Optimización estricta de rendimiento y Core Web Vitals (LCP, CLS, INP) con enfoque de medición antes/después y matrices anti-racionalización.

---

## 📁 Estructura del Repositorio

```text
.
├── .agents/                          # Configuración del entorno de agentes
│   └── skills/                       # Skills operativas para los agentes de IA
├── ai-specs/                         # Fuente canónica para SOPs y skills
│   ├── agents/                       # Procedimientos Operativos Estandarizados (SOP-01 al SOP-05)
│   └── skills/                       # Espejo documental de skills
├── contracts/                        # Contratos ejecutables
│   ├── api-spec.yml                  # Especificación OpenAPI canónica
│   ├── contract_manifest.json        # Sellado criptográfico de contratos
│   └── data-model.md                 # Diagrama ERD y entidades del dominio
├── docs/
│   └── adr/                          # Architectural Decision Records (ADRs)
├── scripts/
│   └── gatekeeper/                   # Orquestador y aduanas deterministas
│       ├── gatekeeper.py             # Aduana central determinista
│       ├── verify_contract_integrity.py  # Verificador de inmutabilidad de contratos
│       ├── verify_test_integrity.py  # Verificador de inmutabilidad de tests
│       └── check_coverage.py         # Validador de umbral de cobertura (>= 85%)
├── .specs/                           # Especificaciones formales del sistema
│   ├── active/                       # Especificaciones en redacción/revisión
│   └── approved/                     # Especificaciones aprobadas por el humano
├── src/                              # Código fuente de producción (protegido por aduana)
├── tests/                            # Suites de pruebas automatizadas
│   ├── unit/                         # Pruebas unitarias y de dominio (Vitest)
│   ├── integration/                  # Pruebas de integración y componentes
│   ├── e2e/                          # Pruebas End-to-End en navegador real (Playwright)
│   └── test_manifest.json            # Manifiesto criptográfico SHA-256 de pruebas
├── AGENTS.md                         # Leyes inmutables y protocolo de agentes
├── CONTEXT.md                        # Lenguaje ubicuo del negocio (Domain Modeling)
├── GEMINI.md                         # Directivas del workspace
├── STACK.md                          # Definición formal del stack tecnológico
├── WORKFLOW.md                       # Protocolo operativo detallado de 8 pasos
└── README.md                         # Documento principal del repositorio
```

---

## ⚡ Comandos Clave del Desarrollador

```bash
# Validar el estado del stack tecnológico
python scripts/gatekeeper/check_stack.py

# Sellar contratos tras cambios autorizados por el Arquitecto
python scripts/gatekeeper/verify_contract_integrity.py --seal

# Sellar pruebas tras la Fase RED (Test Engineer)
python scripts/gatekeeper/verify_test_integrity.py --seal

# Ejecutar la Aduana Determinista Completa (Gatekeeper)
python scripts/gatekeeper/gatekeeper.py
```

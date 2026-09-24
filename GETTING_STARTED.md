# Guía de Inicio Rápido y Flujo de Desarrollo Paso a Paso (Getting Started)

Esta guía explica de forma práctica y orientada al desarrollador cómo utilizar este framework para construir una aplicación web completa desde cero interactuando con el agente de IA (Antigravity, Cursor, Claude o Gemini).

La interacción es **conversacional y guiada por protocolos**. No necesitas orquestar scripts complejos manualmente: el agente detecta tus intenciones, activa las habilidades (*skills*) adecuadas y solicita tu confirmación en los puntos de control humano clave (**Human-in-the-Loop / HITL**).

---

## 🚀 Flujo de 8 Pasos Desde Cero

```text
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 0: Preparación inicial (Descomprimir, `git init`, abrir IDE)          │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 1: Ideación y Refinamiento (Skill `idea-refine` + `/grill-me`)         │
 │         └──> Define Core Loop del MVP, público y lista "Not Doing"          │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 2: Desglose y Especificación (`planning-and-task-breakdown` + `enrich`)│
 │         └──> Tareas XS-L y Spec Gherkin en `.specs/active/SPEC-XXX.md`      │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 3: Configuración del Stack Tecnológico (`STACK.md`) [HITL]             │
 │         └──> Selección de herramientas y cambio a `STATUS: CONFIGURED`      │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 4: Modelado de Dominio y Contratos (`domain-modeling` + `api-design`)  │
 │         └──> `CONTEXT.md`, `contracts/api-spec.yml` y sellado SHA-256       │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 5: Fase RED (Agentic TDD Inmutable)                                    │
 │         └──> Tests unitarios/integración en `tests/` y sellado SHA-256      │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 6: Fase GREEN (Implementación en `src/`)                               │
 │         └──> Código mínimo en `src/` (prohibido alterar pruebas de `tests/`)│
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 7: Auditoría y Aduana Determinista (Gatekeeper)                        │
 │         └──> `deep-code-auditor`, OWASP y `python gatekeeper.py` (0 warnings│
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        ▼
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ Paso 8: Aprobación Humana y Cierre [HITL]                                   │
 │         └──> Mover especificación a `.specs/approved/`                      │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

### Paso 0: Preparación Inicial

1. Descomprime el paquete del framework en la carpeta de tu nuevo proyecto:
   ```powershell
   Expand-Archive -Path "anti-vibecoding-framework.zip" -DestinationPath "c:\MiProyecto"
   ```
2. Inicializa el repositorio Git:
   ```bash
   cd c:\MiProyecto
   git init
   ```
3. Abre la carpeta en tu editor y abre el chat del agente.

---

### Paso 1: Ideación y Refinamiento (`idea-refine`)

Para iniciar un proyecto no necesitas comandos complejos: basta con plantear la idea general y solicitar la activación de `idea-refine`.

> 💬 **Prompt que tú escribes:**
> *"Hola, quiero construir una plataforma para gestión de presupuestos personales y recordatorios de vencimiento de servicios. Ayúdame a refinar la idea con `idea-refine` antes de escribir código."*
>
> *(Opcional: Si quieres que el agente te haga preguntas desafiantes sobre viabilidad y modelo de negocio, puedes usar el comando `/grill-me`).*

#### ¿Qué hace el agente?
- Activa la habilidad `idea-refine`.
- Define el problema real, usuarios clave y supuestos de mayor riesgo.
- Formula el **Core Loop del MVP** y la lista **Not Doing** (lo que queda expresamente fuera para no inflar el alcance).
- **Intervención Humana (HITL 1):** Te presenta el resumen del concepto. Tú respondes aprobando o ajustando (ej. *"Me parece bien, pero quitemos la integración bancaria en el MVP y enfoquémonos en carga manual y alertas"*).

---

### Paso 2: Desglose y Especificación Formal (`planning-and-task-breakdown` + `enrich-us`)

Una vez validada la idea, el agente la transforma en un plan de tareas y una especificación con criterios ejecutables.

> 💬 **Prompt que tú escribes:**
> *"Excelente. Ahora desglosa el MVP en tareas y redacta la primera especificación funcional para la carga y consulta de gastos."*

#### ¿Qué hace el agente?
- **`planning-and-task-breakdown`**: Divide el trabajo en rebanadas verticales (*vertical slices*) ordenadas y dimensionadas (XS, S, M, L).
- **`enrich-us`**: Redacta el archivo [`.specs/active/SPEC-001-gastos.md`](file:///c:/Finance/.specs/SPEC_TEMPLATE.md) con criterios de aceptación en formato **Gherkin** (`Given-When-Then`), análisis de impacto y casos de borde.
- **Intervención Humana (HITL 2):** Revisas y apruebas los escenarios funcionales antes de tocar una sola línea de código.

---

### Paso 3: Configuración del Stack Tecnológico ([`STACK.md`](file:///c:/Finance/STACK.md))

Como el stack inicial está en `STATUS: UNCONFIGURED`, la Ley 1 prohíbe escribir código o pruebas.

> 💬 **Prompt que tú escribes:**
> *"Recomiéndame y configuremos el stack tecnológico para este proyecto. Quiero una SPA web moderna y ligera."*

#### ¿Qué hace el agente?
- Te propone el stack óptimo (por ejemplo: React + TypeScript + Vite, Tailwind CSS, Vitest, Playwright, ESLint/Prettier).
- Tras tu visto bueno, actualiza [`STACK.md`](file:///c:/Finance/STACK.md) definiendo los comandos de validación y cambia el estado a:
  ```markdown
  STATUS: CONFIGURED
  ```
- **Intervención Humana (HITL 3):** Confirmación del stack técnico y sus herramientas de calidad.

---

### Paso 4: Modelado de Dominio y Contratos de Datos

Antes de escribir lógica, se formalizan las entidades y las interfaces públicas.

> 💬 **Prompt que tú escribes:**
> *"Define el modelo de dominio en CONTEXT.md y los contratos de datos/API para la SPEC-001."*

#### ¿Qué hace el agente?
- **`domain-modeling`**: Genera o actualiza `docs/CONTEXT.md` con el lenguaje ubicuo del negocio (evita ambigüedades de nomenclatura).
- **`api-and-interface-design`**: Define los endpoints y esquemas en [`contracts/api-spec.yml`](file:///c:/Finance/contracts/api-spec.yml) y [`contracts/data-model.md`](file:///c:/Finance/contracts/data-model.md).
- **Sellado Criptográfico**: El agente ejecuta:
  ```bash
  python scripts/gatekeeper/verify_contract_integrity.py --seal
  ```
  Esto calcula los hashes SHA-256 en [`contracts/contract_manifest.json`](file:///c:/Finance/contracts/contract_manifest.json). A partir de este momento, las interfaces quedan blindadas contra cambios silenciosos.

---

### Paso 5: Fase RED (Agentic TDD Inmutable)

El rol de **Test Engineer** genera las pruebas antes de que exista código.

> 💬 **Prompt que tú escribes:**
> *"Procede con la fase de pruebas (RED) para la SPEC-001 según los contratos sellados."*

#### ¿Qué hace el agente?
- Escribe las pruebas unitarias y de integración en [`tests/`](file:///c:/Finance/tests/) traduciendo directamente los escenarios Gherkin de la spec.
- Ejecuta las pruebas: **fallan (fase RED)** porque aún no hay código implementado en `src/`.
- Sella criptográficamente las pruebas en [`tests/test_manifest.json`](file:///c:/Finance/tests/test_manifest.json) con:
  ```bash
  python scripts/gatekeeper/verify_test_integrity.py --seal
  ```
- **Ley de Inmutabilidad:** Queda estrictamente prohibido alterar estas pruebas durante la fase de desarrollo para "hacerlas pasar".

---

### Paso 6: Fase GREEN (Implementación en `src/`)

> 💬 **Prompt que tú escribes:**
> *"Implementa el código necesario en src/ para hacer pasar todas las pruebas."*

#### ¿Qué hace el agente?
- Escribe la lógica, componentes y servicios exclusivamente dentro de `src/`.
- Consulta la documentación oficial mediante `official-doc-verifier` ante APIs externas (cero alucinación).
- Si surge un fallo complejo, aplica el protocolo de 4 pasos de `systematic-debugging`.
- Ejecuta la suite de pruebas localmente hasta alcanzar el 100% de tests en verde (**fase GREEN**), sin tocar ningún archivo en `tests/`.

---

### Paso 7: Auditoría y Aduana Determinista (Gatekeeper)

Antes de dar la tarea por concluida, el código pasa por una revisión estricta.

> 💬 **Prompt que tú escribes:**
> *"Audita la implementación y ejecuta el Gatekeeper."*

#### ¿Qué hace el agente?
- **`deep-code-auditor` / `adversarial-reviewer`**: Audita OWASP Top 10, sanitización, fugas de memoria y sincronización con las especificaciones.
- **`code-simplification`**: Refactoriza código innecesariamente complejo respetando la cerca de Chesterton.
- **Gatekeeper Determinista**: Ejecuta:
  ```bash
  python scripts/gatekeeper/gatekeeper.py
  ```
  La aduana valida en orden:
  1. Integridad de contratos (SHA-256 intacto).
  2. Inmutabilidad de pruebas (SHA-256 intacto).
  3. Linter y formateo con 0 warnings tolerados.
  4. Type Checker en modo estricto (0 errores de tipos).
  5. 100% de la suite de pruebas en verde y cobertura mínima alcanzada.

---

### Paso 8: Aprobación Humana y Cierre de la Especificación

1. El agente te entrega el resumen del ticket con los resultados del Gatekeeper.
2. **Intervención Humana (HITL 4 & 5):** Pruebas la funcionalidad o revisas el diff.
3. Al dar tu aprobación, la spec se traslada de [`.specs/active/`](file:///c:/Finance/.specs/) a [`.specs/approved/`](file:///c:/Finance/.specs/).
4. El ciclo se repite para la siguiente funcionalidad.

---

## 📑 Cheat Sheet de Prompts Rápidos

| Fase | Lo que tú le dices al agente en el chat | Qué habilidad se activa |
| :--- | :--- | :--- |
| **1. Idea** | *"Tengo esta idea... refinémosla con `idea-refine`"* | `idea-refine` (MVP scope & Not Doing) |
| **2. Tareas/Spec** | *"Genera el desglose y la spec en Gherkin"* | `planning-and-task-breakdown` + `enrich-us` |
| **3. Stack** | *"Definamos el stack técnico en STACK.md"* | Configura runtime, linter, tests y pasa a `CONFIGURED` |
| **4. Contratos** | *"Diseña los contratos y séllalos"* | `domain-modeling` + `api-and-interface-design` + seal |
| **5. Tests (RED)** | *"Escribe y sella las pruebas contra la spec"* | TDD inmutable + seal en `test_manifest.json` |
| **6. Código (GREEN)** | *"Implementa en src/ hasta tener verde"* | Codificación estricta sin tocar `tests/` |
| **7. Gatekeeper** | *"Pasa el Gatekeeper y audita el código"* | `deep-code-auditor` + `scripts/gatekeeper/gatekeeper.py` |

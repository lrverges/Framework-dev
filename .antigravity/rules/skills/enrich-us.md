---
name: enrich-us
description: Analiza y enriquece ideas vagas o tickets informales (Jira/GitHub Issues) transformándolos en especificaciones de ingeniería rigurosas guardadas en .specs/active/.
---

# Skill: User Story & Requirements Enrichment (LIDR-Academy Specboot)

Esta habilidad formaliza el proceso de "User Story Enrichment" para erradicar requerimientos ambiguos y asegurar que el equipo de ingeniería disponga de todos los detalles técnicos antes de escribir código o pruebas.

---

## Misión y Entradas
- **Entrada**: Una idea de producto, requerimiento informal de usuario o ticket proveniente de Jira / GitHub Issues (a través de MCP o entrada directa).
- **Salida**: Un documento formal de especificación ubicado en `.specs/active/SPEC-XXX-<slug>.md`.

---

## Protocolo de Ejecución

Al invocar esta habilidad sobre un requerimiento informal, el agente debe seguir estos pasos:

### 1. Descomposición y Clarificación
- Identificar el objetivo principal y el usuario beneficiario (Persona / Actor).
- Clarificar ambigüedades técnicas y supuestos tácitos.

### 2. Formulación de Criterios de Aceptación (Gherkin)
- Redactar escenarios estrictos en formato `Given-When-Then`:
  - **Happy Path**: Flujo exitoso primario.
  - **Edge Cases**: Límites numéricos, cadenas vacías, valores nulos, caracteres especiales, concurrencia.
  - **Failure Modes**: Respuestas ante caídas de dependencias, timeouts y rechazo de autenticación/permisos.

### 3. Análisis de Impacto Arquitectónico
- **Modelo de Datos**: Verificar si introduce o muta entidades en [contracts/data-model.md](file:///c:/Finance/contracts/data-model.md).
- **Contratos de API**: Especificar nuevos endpoints o mutaciones de esquemas en [contracts/api-spec.yml](file:///c:/Finance/contracts/api-spec.yml).
- **Dependencias**: Confirmar si requiere nuevos paquetes verificados en [STACK.md](file:///c:/Finance/STACK.md).

### 4. Persistencia en `.specs/active/`
- Guardar el documento en `.specs/active/SPEC-XXX-<nombre-feature>.md` utilizando la estructura:
  ```markdown
  # SPEC-XXX: [Título de la Feature]
  - Estado: PENDIENTE DE REVISIÓN HUMANA
  - Origen: [Issue / Requerimiento]
  - Criterios Given-When-Then: [...]
  - Impacto en Data Model: [...]
  - Impacto en API Spec: [...]
  ```
- **Aviso al Usuario**: Detenerse y solicitar la aprobación explícita humana para mover el archivo a `.specs/approved/`.

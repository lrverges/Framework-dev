# Especificaciones (.specs/)

Este directorio es la ubicación canónica para todas las especificaciones funcionales (specs) del proyecto. Ninguna característica o funcionalidad (feature) puede ser implementada sin una especificación previamente aprobada aquí.

## Ciclo de Vida de las Specs

Las especificaciones pasan por un ciclo de vida estricto:

1. **`.specs/active/` (Borradores / Drafts)**: Aquí se guardan las especificaciones en progreso. Usualmente son generadas a partir de ideas informales o requerimientos usando la skill `enrich-us`.
2. **`.specs/approved/` (Aprobadas)**: Una vez que un revisor humano valida la especificación y resuelve cualquier duda, se mueve a este directorio.

**Regla Crítica**: Ningún agente de IA (Implementation Coder, Test Engineer) puede escribir pruebas o código basado en una especificación que no se encuentre en `.specs/approved/`.

## Creación de Specs

- Usa la plantilla oficial: `.specs/SPEC_TEMPLATE.md`
- Apóyate en la skill `enrich-us` para estructurar requerimientos informales en el formato riguroso Given-When-Then y Gherkin.

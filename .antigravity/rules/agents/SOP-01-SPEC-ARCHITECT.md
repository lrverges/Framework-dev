# SOP-01: Spec Architect (Diseñador de Especificaciones y Contratos)

## Objetivo
Traducir requerimientos de alto nivel o historias de usuario en especificaciones técnicas formales y contratos ejecutables, garantizando cero ambigüedad antes de que se escriba una sola línea de código o prueba.

## Límites y Prohibiciones Estrictas:
- ❌ **PROHIBIDO** escribir código fuente en `src/`.
- ❌ **PROHIBIDO** escribir pruebas en `tests/`.
- ❌ **PROHIBIDO** proceder si `STACK.md` indica `STATUS: UNCONFIGURED`.

## Entradas Requeridas:
1. Requerimiento del usuario / problema a resolver.
2. `STACK.md` en estado `STATUS: CONFIGURED`.

## Procedimiento Paso a Paso:
1. **Análisis de Requisitos**: Desglosar la necesidad en requerimientos funcionales (RF) y no funcionales (RNF).
2. **Crear Especificación**:
   - Copiar la plantilla [.specs/SPEC_TEMPLATE.md](file:///c:/Finance/.specs/SPEC_TEMPLATE.md) en `.specs/active/SPEC-XXX-<nombre>.md`.
   - Redactar escenarios de aceptación en formato Gherkin (Dado-Cuando-Entonces) cubriendo flujos estándar y casos de error.
3. **Definir Contratos Ejecutables**:
   - Crear o actualizar los esquemas de datos o interfaces en `contracts/` (OpenAPI, JSONSchema, Pydantic, Protobuf, etc.).
4. **Validación**:
   - Verificar que todos los RF tengan al menos un escenario Gherkin correspondiente y un contrato formal asociado.
5. **Entregar al Test Engineer**:
   - Señalizar la finalización de la especificación para que el `Test Engineer` inicie la fase RED.

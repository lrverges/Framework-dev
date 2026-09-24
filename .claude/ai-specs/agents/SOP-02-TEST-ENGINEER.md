# SOP-02: Test Engineer (Ingeniero de Pruebas e Inmutabilidad)

## Objetivo
Implementar la suite de pruebas unitarias y de integración que materializan la especificación (Fase RED de Agentic TDD) y sellar criptográficamente su inmutabilidad.

## Límites y Prohibiciones Estrictas:
- ❌ **PROHIBIDO** escribir o modificar código de producción en `src/`.
- ❌ **PROHIBIDO** crear tests que dependan de detalles de implementación privada; los tests deben basarse estrictamente en los contratos de `contracts/` y escenarios de `.specs/`.

## Entradas Requeridas:
1. `.specs/approved/SPEC-XXX.md` aprobado.
2. Contratos en `contracts/`.
3. `STACK.md` en estado `STATUS: CONFIGURED`.

## Procedimiento Paso a Paso:
1. **Mapeo de Escenarios**:
   - Cada escenario Given-When-Then de la especificación debe traducirse en al menos un caso de prueba en `tests/unit/` o `tests/integration/`.
2. **Ejecutar Fase RED**:
   - Ejecutar el runner de pruebas del stack. Todos los nuevos tests **DEBEN FALLAR** de forma determinista (debido a la ausencia de código en `src/`).
3. **Sellado Criptográfico**:
   - Una vez escritas las pruebas, sellar el manifiesto ejecutando:
     ```bash
     python scripts/gatekeeper/verify_test_integrity.py --seal
     ```
   - Este comando calcula el hash SHA-256 de cada archivo en `tests/` y actualiza `tests/test_manifest.json`.
4. **Entrega al Implementation Coder**:
   - Notificar al Coder que la fase RED está completa y las pruebas están selladas e inmutables.

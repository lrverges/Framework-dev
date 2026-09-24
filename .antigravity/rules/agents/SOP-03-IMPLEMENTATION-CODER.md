# SOP-03: Implementation Coder (Desarrollador de Implementación)

## Objetivo
Escribir el código de producción mínimo y limpio en `src/` estrictamente necesario para que todas las pruebas pasen (Fase GREEN de TDD), respetando los contratos y sin relajar ninguna validación.

## Límites y Prohibiciones Estrictas:
- ❌ **ESTRICTAMENTE PROHIBIDO MODIFICAR NINGÚN ARCHIVO EN `tests/`**.
- ❌ **PROHIBIDO MODIFICAR LOS CONTRATOS EN `contracts/`**.
- ❌ **PROHIBIDO ADIVINAR O ALUCINAR APIs DE TERCEROS**: Si se usan librerías externas, se debe activar la skill `official-doc-verifier`.

## Entradas Requeridas:
1. Pruebas fallando en `tests/` (Fase RED).
2. Manifiesto sellado en `tests/test_manifest.json`.
3. Contratos en `contracts/`.

## Procedimiento Paso a Paso:
1. **Verificar Inmutabilidad Inicial**:
   - Comprobar que las pruebas están selladas:
     ```bash
     python scripts/gatekeeper/verify_test_integrity.py
     ```
2. **Implementación Iterativa (Fase GREEN)**:
   - Crear o modificar código exclusivamente dentro de `src/`.
   - Cumplir rigurosamente las firmas de los contratos en `contracts/`.
   - Ejecutar la suite de pruebas frecuentemente hasta lograr 100% de aprobados en verde.
3. **Refactorización Limpia**:
   - Limpiar el código (eliminar duplicaciones, optimizar legibilidad, añadir tipado estricto).
   - Asegurar que el linter y formateador pasen con cero errores.
4. **Entrega al Security Auditor**:
   - Notificar al Auditor de Seguridad que el código está en verde y listo para revisión profunda.

# SOP-05: Deterministic Gatekeeper (Aduana Automatizada de Calidad)

## Objetivo
Ejecutar la verificación determinista final en el entorno aislado (sandbox), actuando como el último filtro antes del merge a ramas principales o despliegue a producción.

## Requisitos Previos:
- El código está implementado en `src/`.
- Las pruebas pasaron en su totalidad.
- El informe de `Security Auditor` está aprobado sin alertas críticas.

## Procedimiento Paso a Paso:
1. **Ejecución Local**:
   - Correr el script maestro de aduana:
     ```bash
     python scripts/gatekeeper/gatekeeper.py
     ```
2. **Ejecución en Sandbox Contenedorizado**:
   - Para garantizar aislamiento total:
     ```bash
     docker compose -f sandbox/docker-compose.yml up --build --abort-on-container-exit
     ```
3. **Criterios de Aprobación**:
   - [ ] `check_stack.py` aprobado (estado `CONFIGURED`).
   - [ ] `verify_test_integrity.py` aprobado (100% de hashes coincidentes sin mutación).
   - [ ] Linter y Formatter con 0 advertencias y 0 errores.
   - [ ] Verificador estático de tipos en modo estricto con 0 errores.
   - [ ] 100% de pruebas unitarias y de integración pasando.
4. **Veredicto Final**:
   - Si todo es verde, autorizar el commit/merge. Si cualquier paso falla, bloquear terminantemente.

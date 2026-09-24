# contracts/ - Contratos Ejecutables de Interfaz y Datos

Este directorio alberga las definiciones formales de datos e interfaces antes de cualquier implementación. También incluye el `api-spec.yml` y el `data-model.md`.

## Tipos de Contratos Admitidos:
- **APIs REST / HTTP**: OpenAPI 3.x / Swagger (`openapi.yaml` o `openapi.json`), o `api-spec.yml`.
- **Esquemas de Datos**: `data-model.md`, JSON Schema, Pydantic, Zod o Protocol Buffers (`.proto`).
- **Interfaces de Dominio**: Interfaces TypeScript (`.ts`), Protocolos Python (`.py`), o Traits / Interfaces en el lenguaje elegido en `STACK.md`.

## Reglas de Gobernanza:
1. **Los contratos son inmutables durante el ciclo de implementación**: Si se requiere un cambio en el contrato, debe regresar a la fase de diseño con el Spec Architect.
2. **Validación automática**: Los contratos deben ser verificables sintácticamente mediante herramientas del stack.
3. **Sellado Criptográfico**: Los contratos cuentan con inmutabilidad mediante sellado criptográfico usando hashes en `contract_manifest.json` (análogo a `test_manifest.json`).

## Comandos Útiles:
- Para sellar los contratos:
  ```bash
  python scripts/gatekeeper/verify_contract_integrity.py --seal
  ```

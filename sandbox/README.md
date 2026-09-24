# sandbox/ - Entorno Contenedorizado de Ejecución Aislada

El sandbox garantiza la reproducibilidad determinista y protege la máquina anfitrión de efectos secundarios no controlados o ejecuciones inseguras.

## Uso Rápido:

1. **Construir y ejecutar la aduana en Docker**:
   ```bash
   cd sandbox
   docker compose up --build
   ```

2. **Personalizar el runtime**:
   Cuando definas tu tecnología en `STACK.md`, actualiza la imagen base en `sandbox/Dockerfile` (por ejemplo a `node:20-alpine`, `golang:1.22`, `python:3.12-slim` o `rust:1.77-slim`).

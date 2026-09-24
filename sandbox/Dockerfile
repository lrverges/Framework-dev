# Dockerfile de Sandbox Aislado para Ejecución Determinista
# Permite correr pruebas y compilaciones sin contaminar el host del desarrollador.

FROM debian:bookworm-slim

# Metadatos
LABEL maintainer="DevOps & Software Architect"
LABEL description="Sandbox aislado para Starter Kit Anti-Vibecoding"

# Instalar utilidades esenciales
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    ca-certificates \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Configurar directorio de trabajo
WORKDIR /workspace

# Usuario no root para seguridad
RUN useradd -m -u 1000 sandboxuser && chown -R sandboxuser:sandboxuser /workspace
USER sandboxuser

CMD ["python3", "scripts/gatekeeper/gatekeeper.py"]

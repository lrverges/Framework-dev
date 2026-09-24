---
name: official-doc-verifier
description: Protocolo anti-alucinación de APIs. Verifica sintaxis, compatibilidad de versiones y firmas de métodos contra la documentación oficial antes de escribir código.
---

# Official Doc Verifier (Skill Anti-Alucinación)

Esta habilidad se activa SIEMPRE que un agente se disponga a utilizar una biblioteca de terceros, framework, módulo estándar con cambios recientes o CLI externa.

## Principio Fundamental
> **"Nunca asumas una API que no hayas consultado en su documentación oficial."**
> Los modelos de lenguaje tienden a inventar métodos convenientes (`client.send_magic()`, flags obsoletos o parámetros deprecados). Esta skill elimina esa fuente de errores.

---

## Cuándo Activar Esta Skill
- Antes de importar un paquete externo en `src/` o `tests/`.
- Al utilizar métodos de configuración, decoradores o argumentos con nombres dudosos.
- Cuando una prueba arroja `AttributeError`, `TypeError`, `ImportError` o `NoSuchMethodError`.

---

## Procedimiento de Verificación

1. **Identificar Paquete y Versión**:
   - Consultar el gestor de paquetes definido en [STACK.md](file:///c:/Finance/STACK.md) (ej. `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`).
   - Identificar la versión exacta instalada o requerida.

2. **Búsqueda en Fuentes Oficiales**:
   - Usar herramientas de búsqueda web (`search_web`) o lectura de URL (`read_url_content`) apuntando a:
     - Documentación oficial del proyecto (ej. `docs.python.org`, `readthedocs.io`, repositorios GitHub oficiales).
     - Notas de lanzamiento (Changelog / Release Notes) de la versión específica para confirmar métodos deprecados o renombrados.

3. **Verificación de la Firma**:
   - Validar nombre exacto de la función/clase.
   - Validar parámetros obligatorios vs opcionales.
   - Validar tipo de retorno y excepciones que arroja.

4. **Validación de Ejemplo Mínimo**:
   - Asegurarse de que el snippet propuesto replica exactamente el patrón recomendado por los mantenedores de la biblioteca.

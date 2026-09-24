# Estándares Base de Ingeniería (LIDR-Academy & Superpowers)

Este documento establece los estándares de ingeniería no negociables para todos los contribuyentes (desarrolladores humanos, agentes de IA y subagentes) en este repositorio.

---

## 1. Política de Lenguaje y Comunicación
- **Español como Lenguaje del Proyecto**: Todos los comentarios en línea, docstrings, descripciones de pull requests y logs de error DEBEN escribirse en español.
- **Términos Técnicos en Inglés**: Los nombres de variables, clases, funciones (code identifiers) y términos de dominio reconocidos internacionalmente (ej. linter, type checker, coverage) deben mantenerse en inglés en todo el código base.
- Los mensajes de los commits de Git siguen el formato de Conventional Commits (con los tipos en inglés), pero las descripciones deben estar en español.

---

## 2. Estándares de Commits de Git (Conventional Commits)
Todos los commits deben adherirse estrictamente a la especificación [Conventional Commits 1.0.0](https://www.conventionalcommits.org/):

```text
<type>(<optional scope>): <description>

[optional body]

[optional footer(s)]
```

### Tipos Permitidos (Types):
- `feat`: Una nueva característica para el usuario o consumidor.
- `fix`: Una corrección de bug para el usuario o sistema.
- `test`: Añadir tests faltantes o corregir existentes (Solo para Test Engineer / Fase RED).
- `refactor`: Un cambio en el código que no corrige un bug ni añade una característica.
- `docs`: Cambios exclusivos de documentación.
- `style`: Cambios que no afectan el significado del código (formato, espacios, etc.).
- `chore`: Tareas de mantenimiento, actualización de dependencias, herramientas o configuración de build.
- `perf`: Un cambio en el código que mejora el rendimiento (performance).

---

## 3. Umbrales de Cobertura de Pruebas (Test Coverage)
- **Cobertura Estricta Obligatoria**: Se requiere un mínimo de **85%** de coverage general en toda la lógica de negocio (`src/`). Los proyectos que aspiren a una certificación empresarial de alta criticidad deben alcanzar un **90%+**. Este umbral es configurable vía `MIN_COVERAGE` en `check_coverage.py`.
- **Cumplimiento Determinista**: El pipeline de aduana (`scripts/verify.sh` / `scripts/verify.ps1` o `gatekeeper.py`) aborta automáticamente y rechaza cualquier pull request o merge si el coverage total de líneas cae por debajo del umbral.
- **Cobertura de Ramas (Branch Coverage)**: Las decisiones de negocio críticas (ramas condicionales complejas) deben tener explícitamente test coverage para casos extremos.

---

## 4. Análisis Estático y Verificación de Tipos (Type Checking)
- **Cero Linter Warnings**: Tolerancia cero para errores o warnings del linter. El formato y estilo del código debe cumplir al 100% con el linter configurado.
- **Strict Static Typing**: El type checker estático del proyecto (ej. `mypy --strict`, TypeScript `strict: true`, etc.) debe ejecutarse sin errores. El uso de `any` o firmas sin tipar está prohibido a menos que esté justificado por una excepción arquitectónica explícita.
- **Código Muerto (Dead Code) y Código Zombi**: No se permiten bloques de código comentados, imports sin uso o variables huérfanas.

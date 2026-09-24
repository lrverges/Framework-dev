# SOP-04: Security & Quality Auditor (Auditor de Seguridad y Rendimiento)

## Objetivo
Realizar una revisión estática y dinámica profunda del código implementado en `src/`, evaluando vulnerabilidades de seguridad (OWASP), fugas de memoria o recursos, cuellos de botella de rendimiento y sincronización exacta entre código, contratos y especificaciones.

## Límites y Prohibiciones Estrictas:
- ❌ **PROHIBIDO** aprobar código con vulnerabilidades conocidas, secretos en texto plano, falta de sanitización o memory leaks.
- ❌ **PROHIBIDO** ignorar discrepancias entre la documentación en `.specs/approved/` y el comportamiento en `src/`.

## Procedimiento Paso a Paso:
1. **Activar Skill `deep-code-auditor`**:
   - Ejecutar la auditoría estática exhaustiva sobre los archivos de `src/`.
2. **Revisión de Seguridad (OWASP Top 10)**:
   - Inyección (SQL, Command, etc.).
   - Validación y sanitización estricta de inputs.
   - Manejo seguro de errores (sin filtrar stacktraces internos o información sensible).
3. **Revisión de Recursos y Rendimiento**:
   - Cierre adecuado de conexiones a bases de datos, descriptores de archivo y sockets.
   - Complejidad algorítmica y estructuras de datos adecuadas.
4. **Sincronización Documental**:
   - Verificar que todos los RF de `.specs/approved/SPEC-XXX.md` estén cubiertos y marcados adecuadamente.
   - Asegurar que los comentarios de código o docstrings no desincronicen de los contratos.
5. **Veredicto**:
   - Emitir informe de auditoría. Si hay hallazgos críticos, devolver al `Implementation Coder`. Si está limpio, transferir al `Gatekeeper`.

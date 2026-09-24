---
name: deep-code-auditor
description: Auditoría profunda de código para seguridad (OWASP), detección de fugas de recursos, optimización de rendimiento y sincronización documental con especificaciones y contratos.
---

# Deep Code Auditor (Skill de Auditoría Exhaustiva)

Esta habilidad dota al agente auditor de una lista de verificación sistemática para auditar código fuente y pruebas antes de cualquier integración.

---

## Dimensiones de Auditoría

### 1. Seguridad (Vulnerabilidades OWASP)
- **Inyección**: Asegurar que consultas a base de datos usen parámetros tipados/preparados y que comandos de shell no concatenen strings no confiables.
- **Manejo de Secretos**: Ninguna credencial, token API o clave privada en código plano. Uso estricto de variables de entorno seguras.
- **Validación de Límites y Tipos**: Todos los inputs externos deben validarse contra el esquema en `contracts/`.
- **Exposición de Información Sensible**: Los mensajes de error públicos no deben volcar stacktraces ni detalles internos de infraestructura.

### 2. Rendimiento y Gestión de Recursos
- **Fugas de Recursos (Resource Leaks)**: Uso de context managers (`with` en Python, `using` en C#, `try-with-resources` o `defer` en Go) para cerrar conexiones, archivos y sockets.
- **Complejidad Algorítmica**: Detección de bucles anidados innecesarios ($O(n^2)$ o superior) en colecciones potencialmente grandes.
- **Concurrencia**: Detección de condiciones de carrera, bloqueos mutuos (deadlocks) o variables compartidas sin sincronización adecuada.

### 3. Sincronización Documental y Trazabilidad
- **Verificación contra `.specs/`**: Comprobar que cada funcionalidad implementada cuenta con su especificación y cumple los criterios de aceptación Given-When-Then.
- **Verificación contra `contracts/`**: Comprobar que los nombres de campos, tipos de datos y códigos de estado HTTP coinciden exactamente con los contratos formales.
- **Documentación de Código**: Docstrings y comentarios precisos, actualizados y sin comentarios obsoletos o código comentado ("zombie code").

---

## Formato del Reporte de Auditoría

```markdown
### Reporte de Auditoría Profunda
- **Componente Auditado**: `src/...`
- **Estado General**: APROBADO / OBSERVACIONES / RECHAZADO

#### 1. Hallazgos de Seguridad
- [SEVERIDAD: ALTA/MEDIA/BAJA] Descripción y mitigación sugerida.

#### 2. Hallazgos de Rendimiento y Recursos
- [SEVERIDAD: ALTA/MEDIA/BAJA] Descripción y mitigación sugerida.

#### 3. Trazabilidad con Especificaciones y Contratos
- [OK / DISCREPANCIA] Detalle de cobertura de especificaciones.
```

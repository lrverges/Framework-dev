---
name: systematic-debugging
description: Protocolo de depuración científica de 4 pasos (Superpowers). Erradica el 'shotgun debugging' mediante formulación de hipótesis, reproducción determinista en test, diagnóstico por trazas y corrección quirúrgica.
---

# Skill: Systematic Debugging (Superpowers Protocol)

Esta habilidad establece el procedimiento científico obligatorio para resolver fallos de pruebas, regresiones y defectos en tiempo de ejecución.

## 🛑 Regla Estricta Anti-Vibecoding
> **Queda terminantemente prohibido el "Shotgun Debugging"** (modificar código al azar, insertar `try/catch` vacíos, relajar aserciones de tests o alterar dependencias por intuición con la esperanza de que el error desaparezca).

---

## Protocolo Obligatorio de 4 Pasos

```text
+----------------+      +-------------------+      +----------------+      +-----------------------+
|  1. Hipótesis  | ---> | 2. Reproducción   | ---> | 3. Diagnóstico | ---> | 4. Corrección         |
|  (Causa raíz)  |      |    (Test RED)     |      |    (Trazas)    |      |    (Quirúrgica en src)|
+----------------+      +-------------------+      +----------------+      +-----------------------+
```

### Paso 1: Hipótesis Explícita
- Antes de modificar cualquier archivo, el agente debe formular por escrito:
  - ¿Qué comportamiento inesperado está ocurriendo?
  - ¿Cuál es la causa raíz teórica más probable?
  - ¿Qué supuesto del código resultó falso?

### Paso 2: Reproducción Determinista (Fase Red)
- Escribir un test unitario o de integración mínimo que reproduzca el bug de forma fiable e inequívoca.
- Ejecutar el test y comprobar que **FALLA** exactamente con el error reportado.
- *Nota*: Si el test pasa o arroja un error no relacionado, la hipótesis es errónea o incompleta; debe revisarse el Paso 1.

### Paso 3: Diagnóstico Basado en Evidencia
- Usar registros estructurados (logs), trazas de depuración o inspección del estado en tiempo de ejecución para confirmar que la causa raíz coincide con la hipótesis.
- Prohibido suponer: la evidencia debe ser empírica y comprobable.

### Paso 4: Corrección Quirúrgica (Fase Green)
- Aplicar el cambio mínimo necesario **únicamente en `src/`**.
- Ejecutar el test de reproducción y la suite completa:
  - El test reproductor debe pasar a verde.
  - Ninguna prueba existente debe romperse (cero regresiones).
- **Prohibición**: Queda prohibido modificar las aserciones del test reproductor para forzar el aprobado.

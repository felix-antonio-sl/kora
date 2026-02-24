---
_manifest:
  urn: "urn:kora:agent-bootstrap:korax-cm-close:1.0.0"
  type: "lazy_load_endofunctor"
---

## Purpose

Ritual de cierre vespertino (PCA Módulo 3: "Noche — 2min de Cierre"). Cierra el día, vacía micro-capturas y ejecuta micro-check de Waiting (INV-12).

## Input/Output

- **Input:** day_state: {bloques_ejecutados, capturas_pendientes, waiting_items}
- **Output:** close: CloseResult {capturas_nuevas, waiting_alertas, triaje_recordado}

## Procedure

1. Preguntar: "¿Algo que capturar antes de cerrar?"
2. Si no hubo triaje hoy → recordar suavemente (vinculado a triaje vespertino, que el operador inicia manualmente con `/triaje`).
3. **Micro-check Waiting (INV-12):** ¿Algo en WAITING.md >3 días? → Alertar con lista.
4. Recordar vaciar micro-capturas del día al buffer.
5. Confirmar cierre.

**Duración:** 2 minutos máximo.

## Signature Output

```
🌙 Cierre del día.
{⚠️ Sin triaje hoy — ¿hacemos uno rápido? | ✓ Triaje hecho}
{⚠️ Waiting >3d: {lista} | ✓ Waiting OK}
¿Algo que capturar antes de cerrar?
```

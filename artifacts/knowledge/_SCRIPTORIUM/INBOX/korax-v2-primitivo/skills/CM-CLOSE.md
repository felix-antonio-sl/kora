---
_manifest:
  urn: urn:korvo:skill:korax-close:2.0.0
  type: lazy_load_endofunctor
---

## Proposito
Ritual de cierre vespertino (PCA Módulo 3: "Noche — 2min de Cierre"). Cierra el día, vacía micro-capturas, ejecuta micro-check de Waiting (INV-12) y ofrece espacio para reflexión.

## Input/Output
- **Input:** day_state: {bloques_ejecutados, capturas_pendientes, waiting_items}
- **Output:** close: CloseResult {capturas_nuevas, waiting_alertas, triaje_recordado, reflexion}

## Procedimiento
1. Preguntar: "¿Algo que capturar antes de cerrar?"
2. Si no hubo triaje hoy → recordar suavemente (vinculado a triaje vespertino, que el operador inicia manualmente con `/triaje`).
3. **Micro-check Waiting (INV-12):** ¿Algo en WAITING.md >3 días? → Alertar con lista.
4. Recordar vaciar micro-capturas del día al buffer.
5. **Reflexión breve (opcional):** "¿Cómo fue el día?" Si el operador quiere hablar → escuchar en registro relacional (no operacional). Si no → cerrar sin insistir.
6. Confirmar cierre.

**Duración:** 2-5 minutos (2 base + reflexión opcional).

## Signature Output
```
🌙 Cierre del día.
{⚠️ Sin triaje hoy — ¿hacemos uno rápido? | ✓ Triaje hecho}
{⚠️ Waiting >3d: {lista} | ✓ Waiting OK}
¿Algo que capturar antes de cerrar?
```

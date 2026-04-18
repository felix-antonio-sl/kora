---
_manifest:
  urn: urn:dev:skill:context-hygiene:1.1.2
  type: lazy_load_endofunctor
---

## Proposito

Auditar y mantener higiene de contexto. Detectar bloat, herramientas innecesarias, degradacion de sesion.

## Input/Output

- **Input:** Estado de sesion actual (tokens usados, herramientas cargadas, turnos transcurridos)
- **Output:** Recomendaciones: { compact_needed, tools_to_remove, session_reset_recommended, cleanup_actions }

## Procedimiento

1. Tokens usados > 70% de ventana? -> recomendar compaction o session reset.
2. Herramientas cargadas que no se han usado en >5 turnos? -> recomendar remocion.
3. MCPs activos? -> recomendar eliminacion (anti-patron por costo constante de contexto).
4. CLAUDE.md del repo target necesita actualizacion con learnings de la sesion? -> recomendar despacho de worker para update.

## Signature Output

```
## Hygiene Report
- Context usage: [N]% of window
- Unused tools: [list]
- MCPs active: [list — recommend removal]
- Session health: [healthy|degraded|critical]
- Action: [compact|reset|continue]
```

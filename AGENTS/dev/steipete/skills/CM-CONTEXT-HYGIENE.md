---
_manifest:
  urn: urn:dev:skill:context-hygiene:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Auditar y mantener higiene de contexto. Detectar bloat, herramientas innecesarias, degradación de sesión.

## Input/Output

- **Input:** Estado de sesión actual (tokens usados, herramientas cargadas, turnos transcurridos)
- **Output:** Recomendaciones: { compact_needed, tools_to_remove, session_reset_recommended, cleanup_actions }

## Procedimiento

1. Tokens usados > 70% de ventana? → recomendar compaction o session reset.
2. Herramientas cargadas que no se han usado en >5 turnos? → recomendar remoción.
3. MCPs activos? → recomendar eliminación (anti-patrón).
4. CLAUDE.md del repo target actualizado con learnings de la sesión? → recomendar update.
5. Steinberger: "MCPs are constant context cost and garbage."

## Signature Output

```
## Hygiene Report
- Context usage: [N]% of window
- Unused tools: [list]
- MCPs active: [list — recommend removal]
- Session health: [healthy|degraded|critical]
- Action: [compact|reset|continue]
```

---
_manifest:
  urn: "urn:ops:skill:deployer-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar contexto multi-turno de la sesion de deploy. Mantener estado acumulado (clasificaciones, estrategias, deploys, verificaciones) y generar resumen de sesion en nodo terminal.

## I/O

- **Input:** session_history: {turns: Turn[], current_state: FSM_State, deploys: DeployResult[], rollbacks: RollbackResult[]}
- **Output:** session_summary: {deploys_executed: number, strategies_used: StrategyCount, rollbacks_triggered: number, final_metrics: MetricsSnapshot, timeline: TimelineEntry[]}

## Procedimiento

1. **Agregar deploys ejecutados**:
   - Contar deploys exitosos vs fallidos
   - Agrupar por estrategia: fast-track, canary, manual
   - Listar versiones deployadas

2. **Agregar rollbacks**:
   - Contar rollbacks triggered
   - Para cada rollback: causa, version revertida, tiempo normalizacion
   - Tasa rollback: rollbacks / deploys

3. **Compilar timeline**:
   - Secuencia cronologica de acciones: clasificacion → estrategia → deploy → verificacion → (expansion|rollback)
   - Timestamps por cada accion
   - Duracion total de sesion

4. **Metricas finales**:
   - Estado actual de cada environment
   - Feature flags activos
   - Metricas actuales vs baseline original

5. **Detectar patrones**:
   - IF rollback rate > 30% → recomendar revision pipeline
   - IF mismo servicio falla multiples veces → recomendar investigacion
   - IF canary expansion exitosa → confirmar estabilidad

## Signature Output

```yaml
session_summary:
  deploys_executed: 3
  deploys_successful: 2
  deploys_failed: 1
  strategies_used:
    fast-track: 1
    canary: 1
    manual: 1
  rollbacks_triggered: 1
  rollback_rate: "33%"
  timeline:
    - timestamp: "2026-02-24T10:00:00Z"
      action: "CLASSIFY"
      detail: "PR #142 → lectura"
    - timestamp: "2026-02-24T10:01:00Z"
      action: "DEPLOY"
      detail: "fast-track v2.4.0 → success"
    - timestamp: "2026-02-24T10:15:00Z"
      action: "CLASSIFY"
      detail: "PR #143 → escritura"
    - timestamp: "2026-02-24T10:16:00Z"
      action: "DEPLOY"
      detail: "canary 5% v2.4.1"
    - timestamp: "2026-02-24T10:31:00Z"
      action: "ROLLBACK"
      detail: "v2.4.1 → v2.4.0, latency degraded"
  active_flags: ["ff-142-config"]
  final_state: "stable"
  recommendation: "Investigate PR #143 DB connection pooling before retry"
```

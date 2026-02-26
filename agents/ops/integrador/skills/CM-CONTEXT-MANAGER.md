---
_manifest:
  urn: "urn:ops:skill:integrador-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar contexto multi-turno de la sesion de integracion. Mantener estado acumulado (PRs analizados, conflictos resueltos, estado cola, backpressure) y generar resumen de sesion en nodo terminal.

## I/O

- **Input:** session_history: {turns: Turn[], current_state: FSM_State, merges: MergeResult[], conflicts: ConflictResult[], queue_state: QueueState}
- **Output:** session_summary: {prs_integrated: number, conflicts_resolved: {trivial: number, substantive_escalated: number}, coherence_checks: number, queue_final: QueueState, throughput: number, backpressure_events: number, timeline: TimelineEntry[]}

## Procedimiento

1. **Agregar merges ejecutados**:
   - Contar PRs mergeados exitosamente
   - Listar PRs rechazados con razon
   - Tasa de merge: merges exitosos / PRs analizados

2. **Agregar conflictos**:
   - Contar conflictos triviales resueltos autonomamente
   - Contar conflictos substantivos escalados a Operador
   - Para cada conflicto: tipo, PRs involucrados, resolucion/escalacion
   - Tasa resolucion autonoma: triviales / total conflictos

3. **Agregar verificaciones coherencia**:
   - Contar verificaciones cross-PR ejecutadas
   - Listar zonas verificadas
   - Contradicciones detectadas y estado (resueltas, pendientes, escaladas)

4. **Compilar estado cola**:
   - Queue depth final
   - Throughput promedio durante sesion (PRs/hora)
   - Eventos de backpressure: activaciones/desactivaciones
   - Tiempo promedio en cola

5. **Compilar timeline**:
   - Secuencia cronologica: analisis → merge → conflicto → resolucion → coherencia
   - Timestamps por accion
   - Duracion total de sesion

6. **Detectar patrones**:
   - IF conflictos substantivos > 30% del total → recomendar revision arquitectonica
   - IF misma zona genera conflictos repetidos → recomendar refactoring de zona
   - IF backpressure activado > 50% del tiempo → recomendar escalar capacidad merge

## Signature Output

```yaml
session_summary:
  prs_integrated: 12
  prs_rejected: 2
  merge_rate: "86%"
  conflicts_resolved:
    trivial: 8
    substantive_escalated: 3
    auto_resolution_rate: "73%"
  coherence_checks: 4
  zones_checked: ["src/services/orders/", "src/api/v2/", "src/models/"]
  queue_final:
    depth: 5
    throughput_per_hour: 8.5
  backpressure_events: 2
  timeline:
    - timestamp: "2026-02-24T10:00:00Z"
      action: "MERGE"
      detail: "PR #201 → coherent, merged"
    - timestamp: "2026-02-24T10:05:00Z"
      action: "CONFLICT"
      detail: "PR #205 vs #206 → trivial (imports), auto-resolved"
    - timestamp: "2026-02-24T10:12:00Z"
      action: "COHERENCE"
      detail: "PRs #208, #209, #210 → contradictory (cache implementations)"
    - timestamp: "2026-02-24T10:13:00Z"
      action: "ESCALATION"
      detail: "Conflicto cache #208/#209 → escalado a Operador"
    - timestamp: "2026-02-24T10:30:00Z"
      action: "BACKPRESSURE"
      detail: "Queue depth 18 > threshold 15 → backpressure ON"
  recommendation: "Zona src/services/orders/ genera 60% de conflictos. Considerar refactoring para reducir acoplamiento."
```

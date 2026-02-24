---
_manifest:
  urn: "urn:ops:skill:integrador-merge-queue-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar la merge queue: priorizar PRs por valor de negocio, aplicar backpressure cuando la cola se satura, reportar metricas de throughput y profundidad de cola.

## Input/Output

- **Input:** action: enqueue|dequeue|prioritize|status|backpressure_check, queue_state: {prs: PRQueueEntry[], threshold: number}, pr?: PRInfo
- **Output:** queue_update: {depth: number, throughput_per_hour: number, avg_wait_min: number, backpressure: {active: boolean, reason?: string}, ordered_prs: PRQueueEntry[], action_taken: string}

## Procedimiento

1. **Enqueue**:
   - Recibir PR con metadata: story asociada, prioridad de negocio, riesgo, zona target
   - Asignar posicion en cola segun prioridad de negocio de historia asociada
   - IF cola > threshold → activar backpressure antes de encolar

2. **Dequeue**:
   - Extraer PR de mayor prioridad que este listo para merge (CI verde, evals passed, coherencia verificada)
   - IF PR de alta prioridad bloqueado por conflicto → procesar siguiente
   - Registrar tiempo en cola para metricas

3. **Prioritize**:
   - Re-evaluar orden de cola cuando: nueva historia de alta prioridad llega, conflicto resuelto desbloquea PR, backpressure cambia de estado
   - Criterios prioridad: valor negocio historia > antigueidad en cola > riesgo (bajo primero)

4. **Status**:
   - Reportar: depth actual, throughput (PRs mergeados/hora), tiempo promedio en cola
   - Listar PRs en cola con posicion, prioridad, estado (ready|blocked|in_review)
   - Histograma de tiempos de espera

5. **Backpressure check**:
   - IF queue_depth > threshold → backpressure ON
   - IF queue_depth < threshold * 0.7 → backpressure OFF (histeresis para evitar flapping)
   - IF backpressure ON → notificar orquestador: reducir tasa generacion PRs
   - IF backpressure OFF → notificar orquestador: tasa normal

## Signature Output

```yaml
queue_update:
  depth: 18
  throughput_per_hour: 8.5
  avg_wait_min: 12.3
  backpressure:
    active: true
    reason: "queue_depth (18) > threshold (15)"
    notification_sent: true
  ordered_prs:
    - pr: "#201"
      priority: 1
      story: "US-42 (P0)"
      status: "ready"
      wait_min: 3
    - pr: "#205"
      priority: 2
      story: "US-45 (P1)"
      status: "ready"
      wait_min: 8
    - pr: "#208"
      priority: 3
      story: "US-47 (P1)"
      status: "blocked_conflict"
      wait_min: 15
  action_taken: "BACKPRESSURE_ACTIVATED"
```

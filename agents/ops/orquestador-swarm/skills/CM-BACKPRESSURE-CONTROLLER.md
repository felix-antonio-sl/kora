---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-backpressure-controller:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Controlar la presion del pipeline cuando la cola de verificacion se satura. Reducir tasa de generacion de PRs del enjambre. Redirigir agentes a tareas productivas no-PR. Priorizar por valor de negocio. Monitorear drenaje hasta restaurar tasa normal.

## Input/Output

- **Input:** queue_status: {depth: number, threshold: number, drain_rate: number, pr_generation_rate: number, business_priorities: PriorityMap}
- **Output:** backpressure_action: {activated: boolean, pr_rate_reduction: float, agent_redirections: AgentRedirection[], priority_reorder: PriorityReorder[], estimated_drain_time_min: number, status: monitoring|active|draining|resolved}

## Procedimiento

1. **Evaluar estado de cola**:
   - IF depth > threshold → activar backpressure
   - IF depth > threshold * 2 → backpressure critica, reduccion agresiva
   - IF depth <= threshold → desactivar backpressure, restaurar tasa normal

2. **Reducir tasa generacion PRs**:
   - Backpressure normal: reducir tasa al 50% (factor 0.5)
   - Backpressure critica: reducir tasa al 20% (factor 0.2)
   - Comunicar a agentes generadores: pausar creacion PRs nuevos

3. **Redirigir agentes a tareas no-PR**:
   - Analisis arquitectonico y deuda tecnica
   - Refactoring de contexto (ARCHITECTURE.md, CONSTRAINTS.md)
   - Planificacion de proximas historias
   - Documentacion y actualizacion de KBs
   - Revision de calidad de evals existentes

4. **Priorizar cola por valor de negocio**:
   - Historias alta prioridad (PO-defined) → primero en cola
   - Hotfixes → prioridad maxima independiente de backpressure
   - Lectura (config/docs) → pueden esperar
   - Merge queues inteligentes: PRs NO compiten igualmente por CI time

5. **Monitorear drenaje**:
   - Calcular drain_rate actual
   - Estimar tiempo hasta cola bajo umbral
   - IF drain_rate insuficiente → incrementar reduccion
   - IF cola drenada → desactivar backpressure, notificar enjambre

## Signature Output

```yaml
backpressure_action:
  activated: true
  status: "active"
  queue_depth: 47
  threshold: 20
  pr_rate_reduction: 0.5
  agent_redirections:
    - agent: "fxsl/coder-1"
      from: "pr_generation"
      to: "architecture_analysis"
    - agent: "fxsl/coder-2"
      from: "pr_generation"
      to: "tech_debt_review"
  priority_reorder:
    - pr: "#248"
      priority: 1
      reason: "hotfix produccion"
    - pr: "#245"
      priority: 2
      reason: "historia alta prioridad PO"
  estimated_drain_time_min: 35
```

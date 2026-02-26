---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-golden-path-router:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Construir y ejecutar el plan de golden path correspondiente al evento clasificado. Despachar agentes especializados para cada paso del camino. Monitorear progreso y detectar desviaciones.

## I/O

- **Input:** classification: {event_type, risk, golden_path, priority, affected_systems}, agents_available: AgentRegistry
- **Output:** execution_plan: {path: string, steps: Step[], agents_dispatched: AgentDispatch[], status: in_progress|completed|failed|hold, deviations: Deviation[]}

## Procedimiento

1. **Seleccionar golden path** segun clasificacion:

   **Historia estandar** (lectura/escritura):
   1. ops/integrador → verificar coherencia semantica, merge check
   2. ops/tester → lint + types + tests unitarios
   3. ops/tester → eval regresion (modelo diferente al autor)
   4. ops/integrador → merge
   5. ops/deployer → deploy canary 5%
   6. ops/observer → monitoreo 15min
   7. ops/deployer → expand (25%→50%→100%)

   **Historia destructiva**:
   1. ops/integrador → verificar coherencia semantica
   2. ops/tester → lint + types + tests unitarios
   3. ops/tester → eval regresion
   4. ops/security → eval seguridad (modelo diferente)
   5. HOLD → esperar aprobacion Operador
   6. ops/deployer → deploy canary agresivo (monitoreo extendido)
   7. ops/observer → monitoreo extendido 30min

   **Infraestructura**:
   1. Registrar intent del Operador
   2. Agente infra → generar IaC (Terraform/Pulumi/docker-compose)
   3. Agente infra → ejecutar plan
   4. HOLD → Operador revisa diff
   5. Agente infra → apply
   6. ops/observer → verificar estado post-apply
   7. ops/observer → drift monitor continuo

   **Hotfix**:
   1. ops/observer → diagnosticar bug (correlacion con deploys recientes)
   2. fxsl/coder → generar fix + test
   3. ops/tester → eval express (subset critico)
   4. ops/deployer → deploy directo con rollback automatico
   5. ops/observer → verificacion post-deploy inmediata

2. **Despachar agentes** para cada paso secuencialmente. Esperar resultado de cada paso antes de avanzar.

3. **Monitorear progreso**: IF paso falla → evaluar si circuit breaker o retry. IF HOLD → notificar Operador y esperar aprobacion.

4. **Detectar desviaciones**: IF agente reporta anomalia → registrar desviacion. IF desviacion critica → pausar golden path y alertar Operador.

## Signature Output

```yaml
execution_plan:
  path: "estandar"
  steps:
    - step: 1
      agent: "ops/integrador"
      action: "merge_check"
      status: "completed"
    - step: 2
      agent: "ops/tester"
      action: "lint_types_tests"
      status: "completed"
    - step: 3
      agent: "ops/tester"
      action: "eval_regresion"
      status: "in_progress"
  agents_dispatched:
    - agent: "ops/integrador"
      task: "merge_check"
      dispatched_at: "2026-02-24T10:00:00Z"
    - agent: "ops/tester"
      task: "eval_regresion"
      dispatched_at: "2026-02-24T10:02:00Z"
  status: "in_progress"
  deviations: []
```

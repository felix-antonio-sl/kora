---
_manifest:
  urn: "urn:ops:agent-bootstrap:orquestador-swarm-tools:1.0.0"
  type: "bootstrap_tools"
---

## event_classify

- **Firma:** event: {type: commit|pr|alert|config_change|sentinel_proposal|eval_result|heartbeat, payload: EventPayload} → classification: {event_type: string, risk: lectura|escritura|destructiva, golden_path: estandar|destructiva|infraestructura|hotfix, priority: number}
- **Cuando usar:** S-EVENTO. Clasificar evento entrante para determinar tipo, riesgo y golden path correspondiente.
- **Cuando NO usar:** Evento ya clasificado en turno actual.
- **Notas:** Heuristicas: config/docs→lectura, new features→escritura, schema migration/auth→destructiva. Alertas produccion→hotfix. Cambios IaC→infraestructura.

## golden_path_execute

- **Firma:** classification: {event_type, risk, golden_path}, agents_available: AgentRegistry → execution_plan: {path: string, steps: Step[], agents_dispatched: AgentDispatch[], estimated_time: string}
- **Cuando usar:** S-GOLDEN-PATH. Construir y ejecutar plan de golden path basado en clasificacion del evento.
- **Cuando NO usar:** Sin clasificacion previa. Sin agentes disponibles.
- **Notas:** Cuatro golden paths: estandar (PR→merge→canary→expand), destructiva (PR→eval seguridad→HOLD→canary agresivo), infraestructura (Intent→IaC→plan→apply→verify), hotfix (Bug→fix→eval express→deploy directo).

## backpressure_control

- **Firma:** queue_status: {depth: number, threshold: number, drain_rate: number} → backpressure_action: {activated: boolean, pr_rate_reduction: number, agent_redirection: AgentTask[], estimated_drain_time: string}
- **Cuando usar:** S-BACKPRESSURE. Cuando profundidad de cola excede umbral o para monitorear estado de backpressure.
- **Cuando NO usar:** Cola bajo umbral y backpressure no activa.
- **Notas:** Activacion automatica. Agentes redirigidos a tareas no-PR: analisis, refactoring contexto, planificacion. Priorizacion por valor de negocio.

## circuit_breaker_manage

- **Firma:** system_metrics: {deploy_failures: number, pipeline_saturation: number, infra_drift: boolean, observer_heartbeat: boolean} → circuit_status: {breakers_open: CircuitBreaker[], containment_actions: Action[], operator_alert: AlertPayload}
- **Cuando usar:** S-CIRCUITO. Detectar modos de fallo y activar circuit breakers. Tambien en monitoreo periodico.
- **Cuando NO usar:** Sistema estable sin indicadores de fallo.
- **Notas:** Cuatro modos de fallo: cascada deploys (§10.1), saturacion pipeline (§10.2), drift infra (§10.3), fallo observer (§10.4). Contencion automatica; recuperacion requiere Operador.

## system_status

- **Firma:** void → system_state: {events_queued: number, golden_paths_active: GoldenPathStatus[], agents_executing: AgentStatus[], backpressure_level: number, circuit_breakers: CircuitBreakerStatus[], heartbeats: HeartbeatLog[]}
- **Cuando usar:** S-ESTADO. Generar reporte completo del estado del sistema.
- **Cuando NO usar:** No aplica; siempre disponible.
- **Notas:** Tabla resumen con todos los flujos activos, agentes despachados, niveles de backpressure y estado de circuit breakers.

## agent_dispatch

- **Firma:** task: {type: string, golden_path_step: string, payload: any} → dispatch_result: {agent: string, status: dispatched|queued|rejected, reason?: string}
- **Cuando usar:** S-GOLDEN-PATH. Despachar agente especializado para un paso del golden path.
- **Cuando NO usar:** Ejecutar directamente tareas que corresponden a agentes especializados.
- **Notas:** Agentes disponibles: ops/deployer, ops/tester, ops/observer, ops/integrador, ops/security. El orquestador despacha, nunca ejecuta directamente.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Xanpan metodologia, DoD, pipeline, historias | urn:fxsl:kb:xanpan-agents-metodologia |
| Swarm ops, sistema nervioso, golden paths, circuit breakers | urn:fxsl:kb:swarm-ops-metodologia |
| Agent spec, workspace, FSM, coalgebra | urn:kora:kb:agent-spec-md |
| Stack LLM, arquitectura, modelos | urn:fxsl:kb:stack-llm-arquitectura |

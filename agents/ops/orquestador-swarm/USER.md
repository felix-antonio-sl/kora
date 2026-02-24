---
_manifest:
  urn: "urn:ops:agent-bootstrap:orquestador-swarm-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

Operadores y Tech Leads que gobiernan el enjambre de agentes. Contexto: equipos que usan Xanpan::Agents con Swarm::Ops, donde los agentes son ejecutores primarios y el humano declara intenciones y constraints.

## Rutinas

Sesion de orquestacion: recibir eventos → clasificar → rutear por golden path → monitorear ejecucion → reportar estado. Supervision continua de backpressure y circuit breakers. Intervencion humana solo en cambios destructivos, desviaciones de golden paths y circuit breakers no resolubles automaticamente.

## Preferencias de Output

- Formato: Markdown con tablas de estado y metricas de flujo
- Tablas: eventos en cola, golden paths activos, agentes despachados, niveles backpressure, circuit breakers
- Status codes: IDLE, ROUTING, BACKPRESSURE, CIRCUIT_OPEN, DISPATCHING, HOLD
- Idioma: es-CL

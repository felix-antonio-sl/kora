---
_manifest:
  urn: "urn:ops:agent-bootstrap:integrador-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

Tech Leads, Senior Engineers, Operadores que gestionan integracion de codigo en equipos con enjambre de agentes. Contexto: equipos que usan Xanpan con multiples agentes generando PRs en rafagas (10-30 PRs/hora).

## Rutinas

Sesion de integracion: recibir PRs → verificar coherencia semantica → clasificar conflictos → resolver triviales / escalar substantivos → gestionar cola → reportar. Iterativa multi-turno con monitoreo de merge queue y backpressure.

## Preferencias de Output

- Formato: Markdown con diagnosticos y status
- Tablas: comparacion de conflictos, estado cola, throughput
- Code blocks: diffs conflictuantes, resoluciones aplicadas
- Metricas: queue depth, throughput PRs/hora, conflictos triviales/substantivos, tasa resolucion
- Idioma: es-CL

---
_manifest:
  urn: urn:kora:skill:taskmaster-status-reporter:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-STATUS-REPORTER

## Proposito
Resume estado de backlog y ejecucion por columnas.

## Input/Output
- **Input:** scope
- **Output:** status_report

## Procedimiento
1. Recibir y estructurar el input relevante.
2. Aplicar la transformacion cognitiva segun el dominio.
3. Entregar un output claro y reutilizable por la FSM.

## Signature Output
Resultado estructurado consistente con el dominio del skill.

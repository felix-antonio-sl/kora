---
_manifest:
  urn: urn:kora:skill:taskmaster-issue-builder:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-ISSUE-BUILDER

## Proposito
Construye un issue accionable con descripcion, alcance y criterios de aceptacion.

## Input/Output
- **Input:** solicitud_usuario
- **Output:** issue_template

## Procedimiento
1. Recibir y estructurar el input relevante.
2. Aplicar la transformacion cognitiva segun el dominio.
3. Entregar un output claro y reutilizable por la FSM.

## Signature Output
Resultado estructurado consistente con el dominio del skill.

---
_manifest:
  urn: urn:kora:skill:taskmaster-request-classifier:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-REQUEST-CLASSIFIER

## Proposito
Clasifica la intencion del usuario dentro del dominio de gestion de tareas.

## Input/Output
- **Input:** mensaje_usuario
- **Output:** intent_classification

## Procedimiento
1. Recibir y estructurar el input relevante.
2. Aplicar la transformacion cognitiva segun el dominio.
3. Entregar un output claro y reutilizable por la FSM.

## Signature Output
Resultado estructurado consistente con el dominio del skill.

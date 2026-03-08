---
_manifest:
  urn: urn:kora:skill:taskmaster-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Mantiene coherencia de la conversacion y detecta cambios de hilo.

## Input/Output
- **Input:** estado_actual, mensaje_usuario
- **Output:** context_shift, siguiente_estado

## Procedimiento
1. Recibir y estructurar el input relevante.
2. Aplicar la transformacion cognitiva segun el dominio.
3. Entregar un output claro y reutilizable por la FSM.

## Signature Output
Resultado estructurado consistente con el dominio del skill.

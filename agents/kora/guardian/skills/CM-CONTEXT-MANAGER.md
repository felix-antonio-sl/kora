---
_manifest:
  urn: "urn:kora:skill:guardian-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito

Gestionar el contexto multi-turno de la sesion guardian: detectar cambios de tema, preservar el hilo de gobernanza, y reorientar al estado FSM correcto cuando hay deriva.

## Procedimiento

1. Al inicio de cada turno, comparar tema del mensaje actual vs estado FSM activo (EVALUATOR | DEFENDER | AUDITOR | DIAGNOSTICIAN | IMPROVER | EDUCATOR | REPRESENTATIVE)
2. Detectar senales de cambio: nueva entidad mencionada, verbo de accion diferente, dominio distinto al estado actual
3. Si continuidad: mantener estado FSM, preservar contexto acumulado (principios discutidos, veredictos emitidos, nivel usuario)
4. Si cambio de tema claro: marcar CONTEXT_SHIFT → redirigir a S-DISPATCHER con resumen del cambio detectado
5. Si cambio parcial (mismo dominio, sub-tema nuevo): ajustar profundidad sin cambiar estado
6. Preservar registro de: nivel usuario establecido, componentes KORA ya discutidos, veredictos previos emitidos

## Output

Continuidad o CONTEXT_SHIFT con descripcion del cambio. Estado FSM recomendado si hay cambio. Contexto acumulado preservado para el siguiente estado.

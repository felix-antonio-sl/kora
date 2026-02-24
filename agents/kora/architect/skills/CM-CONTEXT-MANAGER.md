---
_manifest:
  urn: "urn:kora:skill:architect-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito

Gestionar el contexto multi-turno de la sesion arquitecto: detectar cambios de tarea, preservar artefactos en construccion, y reorientar al estado FSM correcto ante deriva.

## Procedimiento

1. Al inicio de cada turno, comparar objetivo del mensaje actual vs estado FSM activo (TRANSFORMER | AGENT-BUILDER | KB-MANAGER | VALIDATOR | EDUCATOR | CONSULTANT)
2. Detectar senales de cambio: nuevo tipo de artefacto mencionado, cambio de verbo (construir vs transformar vs validar), dominio fuera de KORA
3. Si continuidad: mantener estado FSM, preservar artefactos en construccion (agente parcial, KB en progreso, doc en transformacion)
4. Si cambio claro: marcar CONTEXT_SHIFT → redirigir a S-DISPATCHER con resumen del artefacto en progreso
5. Si fuera de scope KORA/YAML/agentes: aplicar rejection_response sin cambiar estado
6. Preservar registro de: nivel usuario, artefactos completados en sesion, fases ejecutadas del proceso activo

## Output

Continuidad o CONTEXT_SHIFT con descripcion del cambio detectado. Artefacto en progreso preservado y resumido para el nuevo estado.

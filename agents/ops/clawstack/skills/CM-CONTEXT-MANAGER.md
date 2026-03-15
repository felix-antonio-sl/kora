---
_manifest:
  urn: urn:ops:skill:clawstack-context-manager:1.0.0
  type: lazy_load_endofunctor
---

# CM-CONTEXT-MANAGER

## Proposito
Detecta cambios de contexto durante la conversacion multi-turno, preservando estado del stack entre turnos.

## Input/Output
- **Input:** mensaje_actual: string, estado_fsm: string, foco_previo: string | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
1. Comparar tema del mensaje actual con el foco previo y estado FSM activo.
2. Clasificar:
   - **continuar**: mismo stack, mismo tema, profundizar o ajustar.
   - **nuevo**: cambia de capa, scope o capacidad operacional.
   - **atras**: quiere regresar a estado anterior o rehacer paso.
   - **terminar**: indica cierre de sesion operacional.
   - **fuera**: tema no relacionado con operaciones de stack OpenClaw/Unix/Docker.
3. Preservar estado entre turnos:
   - plataforma_host (OS, version kernel)
   - version_openclaw
   - canales_activos y su estado
   - modelo_principal configurado
   - issues_abiertos de la sesion
   - historial_acciones aplicadas
4. Si shift=fuera -> activar SCOPE_COMPLIANCE en co-induccion.
5. Si shift=nuevo -> evaluar si requiere S-DISPATCHER.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| shift | enum | continuar, nuevo, atras, terminar, fuera |
| detalle | string | Explicacion del cambio detectado |
| estado_preservado | StackState | Estado del stack entre turnos |

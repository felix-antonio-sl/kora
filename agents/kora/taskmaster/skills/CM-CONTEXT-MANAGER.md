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
- **Input:** foco_actual: string | null, mensaje_usuario: string
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Recibir y estructurar el foco actual y el mensaje del usuario.
2. Clasificar si el mensaje continua el hilo actual, abre uno nuevo, retoma uno previo o cierra la tarea.
3. Preservar solo el contexto semantico necesario para continuar o reiniciar el trabajo.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| clasificacion | enum(CONTINUA\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| requiere_revision_de_foco | bool | True si el foco actual debe reinterpretarse |
| foco_recomendado | string \| null | Referencia semantica al foco resultante |

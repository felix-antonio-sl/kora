---
_manifest:
  urn: urn:dev:skill:reviewer-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona contexto multi-turno del reviewer: detecta cambios de tarea, preserva continuidad semantica del review y señala chequeos pendientes.

## Input/Output
- **Input:** foco_actual: string | null, mensaje_usuario: string
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Comparar tema del mensaje actual vs foco de review activo.
2. Determinar si el mensaje continua el mismo PR, abre un review nuevo, retoma uno previo o cierra la tarea.
3. Señalar si conviene revalidar diversidad de provider antes de continuar el review.
4. Clasificar: CONTINUA(mismo PR), NUEVO(PR diferente), ATRAS(retoma review anterior), TERMINAR(fin), FUERA(fuera de scope).
5. Si CONTINUA: preservar hallazgos y evidencia acumulada.
6. Si NUEVO: marcar que el foco actual requiere reinterpretacion.
7. Si ATRAS: restaurar referencia semantica al review previo.
8. Si TERMINAR: marcar cierre solicitado.
9. Si FUERA: aplicar rejection.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| clasificacion | enum(CONTINUA\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| pr_activo | bool | True si el foco actual corresponde al mismo PR o review |
| requiere_revision_de_foco | bool | True si el review debe reinterpretarse desde cero |
| revisar_diversidad | bool | True si conviene revalidar diversidad antes de continuar |
| alerta | string \| null | Observacion relevante para el review activo |

---
_manifest:
  urn: urn:dev:skill:planner-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del planner: detecta cambios de tarea, detecta mezcla de sombreros PO/Operador, mantiene coherencia entre turnos.

## Input/Output
- **Input:** foco_actual: string | null, mensaje_usuario: string
- **Output:** ContextDecision (ver Signature Output)

## Procedimiento
1. Comparar tema del mensaje actual vs foco de trabajo activo.
2. Detectar sombrero: PO(definiendo valor, priorizando, aceptando) vs Operador(configurando, optimizando, infraestructura).
3. Si detecta mezcla de sombreros: alertar. "Estas mezclando sombreros. Cuando llevas el sombrero PO, prioriza por valor de negocio sin dejarte seducir por la elegancia tecnica."
4. Clasificar: CONTINUA(mismo tema), NUEVO(tema diferente), ATRAS(retoma anterior), TERMINAR(fin), FUERA(fuera de scope).
5. Si CONTINUA: preservar el foco actual.
6. Si NUEVO: marcar que el foco actual requiere reinterpretacion.
7. Si ATRAS: restaurar referencia semantica anterior.
8. Si TERMINAR: marcar cierre solicitado.
9. Si FUERA: aplicar regla de rejection.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| clasificacion | enum(CONTINUA\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| sombrero_detectado | enum(PO\|Operador\|Mixto) | Sombrero dominante detectado |
| requiere_revision_de_foco | bool | True si el foco actual debe reinterpretarse |
| alerta_sombrero | string \| null | Advertencia semantica si hay mezcla de sombreros |

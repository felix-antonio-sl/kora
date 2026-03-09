---
_manifest:
  urn: urn:kora:skill:curator-context-manager:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del agente: detecta cambios de tema, retornos semanticos, finalizaciones y solicitudes fuera de scope.

## Input/Output
- **Input:** mensaje_actual: string (mensaje del usuario), foco_actual: string | null, contexto_sesion: SessionContext | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
1. COMPARAR tema del mensaje actual vs foco de trabajo activo:
   - ¿El tema es coherente con la tarea actual?
   - ¿El usuario esta pidiendo algo nuevo?
   - ¿El usuario quiere volver a una fase anterior?
   - ¿El usuario quiere terminar?
   - ¿El tema esta fuera del scope de curator?
2. CLASIFICAR cambio:
   - CONTINUAR: tema coherente con el foco actual.
   - NUEVO: tema requiere revisar el foco de trabajo.
   - ATRAS: usuario quiere retomar una referencia semantica previa.
   - TERMINAR: usuario indica fin.
   - FUERA: tema fuera scope.
3. PRESERVAR contexto relevante:
   - Si el cambio mantiene el mismo trabajo, conservar artefacto, plan y observaciones.
   - Si el cambio es radical, limpiar el foco acumulado y devolver solo una señal de reinicio semantico.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| accion | enum(CONTINUAR\|NUEVO\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| requiere_revision_de_foco | bool | True si el trabajo actual debe ser reinterpretado |
| fase_sugerida | string \| null | Etiqueta semantica de la fase previa si el usuario quiere retomar |
| contexto_preservar | object \| null | Datos a mantener al transicionar |

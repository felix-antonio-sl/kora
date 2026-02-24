---
_manifest:
  urn: "urn:fxsl:skill:refactorer-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del refactorer: detecta cambios de tarea, mantiene estado de refactoring entre turnos, gestiona zona de trabajo activa.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. Verificar contexto de refactoring activo:
   - Zona en analisis? Refactorings en progreso? Metricas baseline registradas?
   - Context files cargados? CONVENTIONS.md vigente?
3. Clasificar: CONTINUA(misma zona/tarea), NUEVO(zona diferente), ATRAS(retoma zona previa), TERMINAR(fin), FUERA(fuera de scope).
4. IF CONTINUA → mantener estado, continuar con siguiente oportunidad priorizada.
5. IF NUEVO → verificar si la zona actual tiene refactorings en progreso. Si hay refactorings incompletos, alertar: "Zona [X] tiene refactorings en progreso. Completar o pausar antes de cambiar."
6. IF ATRAS → restaurar estado de la zona previa si contexto disponible.
7. IF TERMINAR → transicionar a S-END con resumen de metricas.
8. IF FUERA → aplicar regla de rejection.
9. Gestionar regla 70/30: verificar que el contexto cargado es >=70% relevante a la zona de refactoring actual.

## Output
Clasificacion: {tipo, zona_activa?, refactorings_en_progreso?, metricas_baseline?, context_files_cargados[], alerta?}.

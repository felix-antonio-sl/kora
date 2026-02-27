---
_manifest:
  urn: "urn:dev:skill:coder-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del coder: detecta cambios de tarea, mantiene estado de implementacion entre turnos, gestiona context files cargados.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. Verificar contexto de implementacion activo:
   - Historia en progreso? Plan aprobado? Tarea actual?
   - Context files cargados? CONVENTIONS.md vigente?
3. Clasificar: CONTINUA(mismo historia/tarea), NUEVO(historia diferente), ATRAS(retoma tarea previa), TERMINAR(fin), FUERA(fuera de scope).
4. IF CONTINUA → mantener estado, continuar con siguiente tarea del plan.
5. IF NUEVO → verificar si la historia actual esta completa. Si no, alertar: "Historia [X] en progreso. Completar o pausar antes de iniciar otra."
6. IF ATRAS → restaurar estado de la tarea previa si contexto disponible.
7. IF TERMINAR → transicionar a S-END con resumen.
8. IF FUERA → aplicar regla de rejection.
9. Gestionar regla 70/30: verificar que el contexto cargado es >=70% relevante a la tarea actual.

## Output
Clasificacion: {tipo, historia_activa?, tarea_actual?, context_files_cargados[], alerta?}.

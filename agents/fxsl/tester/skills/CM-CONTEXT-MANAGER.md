---
_manifest:
  urn: "urn:fxsl:skill:tester-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona el contexto multi-turno del tester: detecta cambios de tarea, mantiene estado de verificacion entre turnos, gestiona historias y ACs en scope.

## Procedimiento
1. Comparar tema del mensaje actual vs estado FSM activo.
2. Verificar contexto de verificacion activo:
   - Historia en scope? ACs parseados? Tests generados?
   - Suite ejecutada? Reporte de cobertura vigente?
3. Clasificar: CONTINUA(misma historia/suite), NUEVO(historia diferente), ATRAS(retoma verificacion previa), TERMINAR(fin), FUERA(fuera de scope).
4. IF CONTINUA → mantener estado, continuar con siguiente paso del flujo (generar → ejecutar → reportar).
5. IF NUEVO → verificar si la verificacion actual esta completa. Si no, alertar: "Verificacion de [historia X] en progreso. Completar o pausar antes de iniciar otra."
6. IF ATRAS → restaurar estado de la verificacion previa si contexto disponible.
7. IF TERMINAR → transicionar a S-END con resumen.
8. IF FUERA → aplicar regla de rejection.

## Output
Clasificacion: {tipo, historia_activa?, acs_en_scope?, tests_generados?, suite_ejecutada?, alerta?}.

---
_manifest:
  urn: "urn:kora:skill:transformer-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito

Gestionar el contexto multi-turno de sesiones de transformacion y auditoria: preservar documentos en proceso, detectar cambios de tarea, y mantener coherencia de metricas entre turnos.

## Procedimiento

1. Al inicio de cada turno, comparar tema del mensaje actual vs estado FSM activo (ANALYZER | TELEGRAFIZER | VALIDATOR | AUDITOR | COMPARATOR | CONSULTANT)
2. Detectar senales de cambio: nuevo documento proporcionado, cambio de tipo de tarea (transformar → auditar), solicitud de retroceder una fase
3. Si continuidad: mantener estado activo, preservar documento en proceso y metricas calculadas (FS, CR parcial)
4. Si nueva tarea (documento diferente): confirmar si abandona transformacion en curso o abre nueva sesion paralela
5. Si fuera de scope (construir agentes, gestionar hub): aplicar rejection_response sin cambiar estado activo
6. Preservar registro de: documentos transformados en sesion, metricas FS/CR por documento, fase actual de cada transformacion

## Output

Continuidad en estado activo o CONTEXT_SHIFT con descripcion. Documento en progreso y metricas acumuladas preservados para el siguiente turno.

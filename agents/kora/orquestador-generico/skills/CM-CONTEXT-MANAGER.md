---
_manifest:
  urn: "urn:kora:skill:orquestador-generico-context-manager:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito

Gestionar el contexto compartido de una sesion de orquestacion multi-agente: preservar configuracion activa, detectar cambios de objetivo, y mantener coherencia entre turnos.

## Procedimiento

1. Al inicio de cada turno, comparar objetivo del mensaje actual vs orquestacion configurada (participantes, protocolo, roles asignados)
2. Detectar senales de cambio: nuevo objetivo mencionado, participantes diferentes solicitados, cambio de dominio de la tarea
3. Si continuidad: mantener configuracion de orquestacion activa, preservar contexto compartido entre participantes (resultados parciales, acuerdos previos)
4. Si cambio de objetivo: marcar CONTEXT_SHIFT → redirigir a S-DISPATCHER con resumen de orquestacion en progreso
5. Si cambio parcial (refinamiento del mismo objetivo): actualizar configuracion sin reiniciar orquestacion
6. Preservar registro de: participantes activos, protocolo en ejecucion, resultados recopilados hasta el momento

## Output

Continuidad o CONTEXT_SHIFT con descripcion del cambio. Configuracion de orquestacion activa preservada para el siguiente turno.

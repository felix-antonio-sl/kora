---
_manifest:
  urn: "urn:ops:skill:observer-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar el contexto de sesion de observacion. Mantener estado de anomalias activas, correlaciones en curso y diagnosticos pendientes. Detectar cambios de contexto y transiciones implicitas.

## I/O

- **Input:** session_state: {active_anomalies, pending_correlations, pending_diagnoses, heartbeat_status, last_health_check}, new_message: string
- **Output:** context_update: {context_shift: bool, recommended_state: FSM_STATE, active_context: SessionContext, stale_data: [{item, age, recommendation: REFRESH|DISCARD}]}

## Procedimiento

1. **Evaluar frescura de datos:**
   - Health check > 5 min: marcar como stale, recomendar REFRESH
   - Anomalia detectada > 30 min sin correlacion: recomendar retomar correlacion
   - Correlacion > 15 min sin diagnostico: recomendar retomar diagnostico
   - Heartbeat > intervalo configurado: alerta inmediata

2. **Detectar cambio de contexto:**
   - Operador pregunta por servicio diferente al contexto activo → CONTEXT_SHIFT
   - Operador cambia de anomalia a monitoreo general → CONTEXT_SHIFT
   - Operador pide terminar investigacion activa → cerrar contexto, volver a S-DISPATCHER

3. **Mantener contexto acumulativo:**
   - Anomalias activas: lista con severidad y timestamp
   - Correlaciones en curso: hipotesis con confianza
   - Diagnosticos pendientes: acciones propuestas sin respuesta del Operador
   - Historial de alertas enviadas en sesion

4. **Verificar continuidad de heartbeat:**
   - Si heartbeat no emitido en intervalo → forzar emision
   - Si heartbeat falla → alerta maxima prioridad

## Signature Output

```yaml
context_update:
  context_shift: false
  recommended_state: "S-CORRELACION"
  active_context:
    active_anomalies: 2
    pending_correlations: 1
    pending_diagnoses: 0
    heartbeat_status: ACTIVE
    last_health_check: "2026-02-24T14:30:00Z (5 min ago)"
  stale_data:
    - item: "health_check"
      age: "5 min"
      recommendation: REFRESH
```

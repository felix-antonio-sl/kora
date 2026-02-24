---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-cm-alert-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar el ciclo de vida de alertas. Mantener alertas clasicas como backstop independiente. Generar alertas inteligentes desde deteccion de anomalias. Rutear al Operador via canal configurado con reglas de escalacion.

## Input/Output

- **Input:** alert_trigger: {source: CLASSIC|INTELLIGENT, severity, anomaly?: AnomalyEvent, diagnosis?: DiagnosisReport}, config: alert_channels (de config.json)
- **Output:** alert_result: {alert_id, sent: bool, channels_used: string[], escalation_scheduled: bool, summary: string}

## Procedimiento

1. **Clasificar fuente de alerta:**
   - CLASSIC: alerta de Prometheus/Grafana. Backstop. Siempre activa independientemente del observer.
   - INTELLIGENT: alerta generada por CM-ANOMALY-DETECTOR o CM-DIAGNOSIS-PROPOSER. Con contexto enriquecido.

2. **Seleccionar canal segun severidad (config.json):**
   - LOW: log interno. No notificar a menos que el Operador lo pida.
   - MEDIUM: canal default (telegram).
   - HIGH: canal default + escalation (telegram + slack).
   - CRITICAL: todos los canales (telegram + slack + email).

3. **Componer mensaje de alerta:**
   - Titulo: severidad + metrica afectada
   - Cuerpo: valor actual vs baseline, timestamp, tendencia
   - Contexto (si INTELLIGENT): correlacion, confianza, hipotesis principal
   - Accion recomendada (si aplica)

4. **Invocar alert_send** con mensaje y canal(es).

5. **Programar escalacion si no hay respuesta:**
   - MEDIUM: escalar a HIGH si sin respuesta en 30 min
   - HIGH: escalar a CRITICAL si sin respuesta en 15 min
   - CRITICAL: re-enviar cada 5 min hasta respuesta

6. **Verificar backstop:**
   - Confirmar que alertas clasicas Prometheus siguen activas.
   - Si backstop caido → alerta CRITICAL inmediata: "Backstop de alertas clasicas no responde."

## Signature Output

```yaml
alert_result:
  alert_id: "ALT-2026-0224-001"
  severity: HIGH
  sent: true
  channels_used: ["telegram", "slack"]
  escalation_scheduled: true
  escalation_timeout: "15 min"
  summary: "Alerta HIGH enviada: spike latencia p95 890ms. Correlacion con deploy v2.4.1 (82%). Recomendacion: ROLLBACK."
```

---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-tools:1.0.0"
  type: "bootstrap_tools"
---

## health_check

- **Firma:** service_filter: string? → health_report: {services: [{name, uptime, latency_p95, error_rate_5xx, cpu, memory, status: HEALTHY|DEGRADED|CRITICAL}]}
- **Cuando usar:** S-MONITOR. Recopilar metricas clave de salud del sistema.
- **Cuando NO usar:** Datos ya recopilados en turno actual.
- **Notas:** Fuente: Prometheus/Grafana. Incluye metricas LLM (costes, tokens) si disponibles.

## anomaly_detect

- **Firma:** metrics: MetricSeries, window: duration → anomalies: [{metric, baseline, current, deviation_sigma, severity: LOW|MEDIUM|HIGH|CRITICAL, timestamp}]
- **Cuando usar:** S-ANOMALIA. Analizar series temporales para detectar desviaciones estadisticas.
- **Cuando NO usar:** Sin metricas base recopiladas previamente.
- **Notas:** Umbrales configurables. Desviacion > 2σ = anomalia. > 3σ = severa.

## deploy_timeline

- **Firma:** window: duration → deploys: [{version, timestamp, author, changes_summary, status: SUCCESS|FAILED|ROLLED_BACK}]
- **Cuando usar:** S-CORRELACION. Obtener timeline de deploys recientes para cruzar con anomalias.
- **Cuando NO usar:** Timeline ya obtenida en turno actual.
- **Notas:** Ventana default: 24h. Incluye cambios de config y actualizaciones de modelo.

## correlate

- **Firma:** anomaly: AnomalyEvent, events: Event[] → correlations: [{event, temporal_proximity, confidence_pct, hypothesis}]
- **Cuando usar:** S-CORRELACION. Cruzar anomalia con eventos para calcular confianza de correlacion.
- **Cuando NO usar:** Sin anomalia detectada o sin eventos disponibles.
- **Notas:** Confianza basada en proximidad temporal, tipo de cambio y zona afectada. Jamas 100%.

## diagnosis_propose

- **Firma:** anomaly: AnomalyEvent, correlations: Correlation[] → diagnosis: {hypotheses: [{rank, description, confidence_pct, recommended_action: ROLLBACK|INVESTIGATE|WAIT|ESCALATE}]}
- **Cuando usar:** S-DIAGNOSTICO. Proponer hipotesis y acciones basadas en anomalia + correlaciones.
- **Cuando NO usar:** Sin correlacion previa.
- **Notas:** Top-3 hipotesis. Accion siempre como propuesta, Operador aprueba.

## alert_send

- **Firma:** alert: {severity, title, body, recommended_action}, channel: string → delivery_status: {sent: bool, channel, timestamp}
- **Cuando usar:** S-ALERTA. Enviar alerta al Operador via canal configurado.
- **Cuando NO usar:** Severidad LOW sin solicitud explicita del Operador.
- **Notas:** Canales configurados en config.json. Escalacion automatica si no hay respuesta.

## heartbeat

- **Firma:** → heartbeat_status: {alive: bool, timestamp, checks_since_last: int, uptime_observer: duration}
- **Cuando usar:** Periodicamente. Emitir heartbeat para verificar que el observer esta operativo.
- **Cuando NO usar:** Nunca omitir. El heartbeat es obligatorio.
- **Notas:** Intervalo configurado en config.json. Si heartbeat perdido → alerta automatica al Operador.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Consultas de conocimiento. Clasificar tema → resolver URN.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Observabilidad, metricas, alertas, monitoring | urn:fxsl:kb:swarm-ops-metodologia |
| Observer, etapas implementacion, heartbeat | urn:fxsl:kb:chapter0-operador-solitario |
| Stack, Prometheus, Grafana, Langfuse, OpenTelemetry | urn:fxsl:kb:stack-llm-arquitectura |
| Agent spec, principios, estados, transiciones | urn:kora:kb:agent-spec-md |

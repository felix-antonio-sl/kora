---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-cm-anomaly-detector:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar series temporales de metricas para detectar anomalias estadisticas. Clasificar severidad y generar reporte de anomalias detectadas.

## Input/Output

- **Input:** metrics: MetricSeries (via anomaly_detect tool), window: duration (default 1h), baseline_window: duration (default 24h)
- **Output:** anomaly_report: {anomalies_found: int, anomalies: [{metric, type, baseline, current, deviation_sigma, severity, timestamp, trend}], overall_severity: LOW|MEDIUM|HIGH|CRITICAL}

## Procedimiento

1. **Invocar anomaly_detect** con ventana temporal configurada.

2. **Analizar desviaciones por tipo de anomalia:**
   - **Spike latencia:** p95 actual vs baseline 24h. > 2σ = anomalia, > 3σ = severa
   - **Incremento error rate:** 5xx rate actual vs baseline. Cualquier incremento > 5x baseline es anomalia
   - **Explosion costes LLM:** Coste/hora actual vs promedio 7d. > 2x = anomalia, > 5x = severa
   - **Patrones trafico inusuales:** Requests/s vs patron horario historico. Desviacion > 3σ
   - **Consumo recursos:** CPU/memoria con tendencia ascendente sostenida > 30 min

3. **Clasificar severidad global:**
   - LOW: desviaciones < 2σ o metricas no criticas afectadas
   - MEDIUM: desviaciones 2-3σ en metricas relevantes
   - HIGH: desviaciones > 3σ o multiples metricas afectadas simultaneamente
   - CRITICAL: servicio no responde, perdida datos posible, o cascada de anomalias

4. **Detectar tendencia:**
   - SPIKE: aumento subito (< 5 min)
   - RAMP: incremento gradual sostenido (> 15 min)
   - OSCILLATION: fluctuacion atipica

5. **Si severidad >= HIGH:** recomendar transicion automatica a S-CORRELACION.

## Signature Output

```yaml
anomaly_report:
  anomalies_found: 2
  anomalies:
    - metric: "latency_p95"
      type: SPIKE
      baseline: "120ms (avg 24h)"
      current: "890ms"
      deviation_sigma: 4.2
      severity: HIGH
      timestamp: "2026-02-24T14:32:00Z"
      trend: SPIKE
    - metric: "error_rate_5xx"
      type: RAMP
      baseline: "0.02%"
      current: "1.8%"
      deviation_sigma: 3.1
      severity: HIGH
      timestamp: "2026-02-24T14:33:00Z"
      trend: RAMP
  overall_severity: HIGH
  recommendation: "Transicion a S-CORRELACION. Multiples metricas afectadas simultaneamente."
```

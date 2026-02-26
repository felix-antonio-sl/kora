---
_manifest:
  urn: "urn:ops:skill:observer-correlation-engine:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Cruzar anomalias detectadas con eventos recientes del sistema (deploys, cambios config, actualizaciones modelo, cambios trafico) para calcular confianza de correlacion.

## I/O

- **Input:** anomaly: AnomalyEvent (output de CM-ANOMALY-DETECTOR), events: Event[] (via deploy_timeline + correlate tools)
- **Output:** correlation_report: {anomaly_summary, events_analyzed: int, correlations: [{event, temporal_proximity, causal_plausibility, confidence_pct, hypothesis}], top_correlation: Correlation, recommendation: string}

## Procedimiento

1. **Invocar deploy_timeline** para obtener eventos de las ultimas 24h: deploys, cambios config, actualizaciones modelo, cambios trafico.

2. **Calcular proximidad temporal:**
   - Ventana critica: evento ocurrio 0-15 min antes de anomalia → proximidad ALTA
   - Ventana relevante: 15-60 min antes → proximidad MEDIA
   - Ventana lejana: 1-24h antes → proximidad BAJA

3. **Evaluar plausibilidad causal:**
   - Deploy con cambios en componente afectado → plausibilidad ALTA
   - Cambio config en servicio correlacionado → plausibilidad ALTA
   - Actualizacion modelo LLM + anomalia en latencia/costes → plausibilidad ALTA
   - Cambio trafico externo + anomalia en carga → plausibilidad MEDIA
   - Evento en componente no relacionado → plausibilidad BAJA

4. **Invocar correlate** para calcular confianza combinada:
   - Confianza = f(proximidad_temporal, plausibilidad_causal, numero_metricas_afectadas)
   - Formula orientativa: base 40% (temporal) + 30% (plausibilidad) + 30% (amplitud)
   - Techo: 95%. Jamas 100%. La certeza no existe en correlacion.

5. **Ordenar correlaciones** por confianza descendente. Seleccionar top correlation.

6. **Generar recomendacion:**
   - Confianza >= 70%: "Correlacion fuerte. Recomendar transicion a diagnostico."
   - Confianza 40-70%: "Correlacion posible. Investigar mas datos."
   - Confianza < 40%: "Correlacion debil. Monitorear y esperar mas evidencia."

## Signature Output

```yaml
correlation_report:
  anomaly_summary: "Spike latencia p95 (120ms→890ms) + error rate (0.02%→1.8%)"
  events_analyzed: 5
  correlations:
    - event: "Deploy v2.4.1 (migracion modelo LLM)"
      temporal_proximity: "4 min antes de anomalia"
      causal_plausibility: ALTA
      confidence_pct: 82
      hypothesis: "Nuevo modelo LLM con latencia de inferencia superior"
    - event: "Cambio config rate-limiter"
      temporal_proximity: "2h antes de anomalia"
      causal_plausibility: BAJA
      confidence_pct: 15
      hypothesis: "Improbable. Cambio menor en componente no relacionado"
  top_correlation:
    event: "Deploy v2.4.1"
    confidence_pct: 82
  recommendation: "Correlacion fuerte (82%). Transicion a diagnostico recomendada."
```

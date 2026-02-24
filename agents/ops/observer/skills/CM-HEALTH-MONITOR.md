---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-cm-health-monitor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Recopilar y sintetizar metricas clave del sistema de produccion. Generar tabla de estado de salud con clasificacion global.

## Input/Output

- **Input:** service_filter: string? (opcional, filtrar por servicio), metrics_source: health_check tool output
- **Output:** health_report: {timestamp, global_status: HEALTHY|DEGRADED|CRITICAL, services: [{name, metrics, status}], llm_metrics: {cost_24h, tokens_24h, consumption_rate}, summary: string}

## Procedimiento

1. **Invocar health_check** con filtro de servicio si aplica.

2. **Recopilar metricas clave por servicio:**
   - Uptime (% ultimas 24h)
   - Latencia p95 (ms)
   - Error rate 5xx (%)
   - CPU (%)
   - Memoria (%)

3. **Recopilar metricas LLM (si disponibles):**
   - Coste acumulado 24h (USD)
   - Tokens consumidos 24h
   - Tasa de consumo tokens/hora
   - Coste proyectado mensual

4. **Clasificar cada servicio:**
   - HEALTHY: todas las metricas dentro de umbrales normales
   - DEGRADED: al menos una metrica fuera de umbral pero servicio operativo
   - CRITICAL: servicio no responde o multiples metricas fuera de umbral

5. **Calcular estado global:**
   - HEALTHY: todos los servicios HEALTHY
   - DEGRADED: al menos un servicio DEGRADED, ninguno CRITICAL
   - CRITICAL: al menos un servicio CRITICAL

6. **Generar resumen textual** calibrado al estado (calmo si HEALTHY, factual si DEGRADED, urgente si CRITICAL).

## Signature Output

```markdown
## Estado de Salud — 2026-02-24 14:30 UTC

| Servicio | Uptime | Latencia p95 | Error 5xx | CPU | Memoria | Estado |
|----------|--------|-------------|-----------|-----|---------|--------|
| api-gateway | 99.99% | 45ms | 0.01% | 32% | 48% | HEALTHY |
| llm-proxy | 99.95% | 230ms | 0.03% | 55% | 61% | HEALTHY |
| postgres | 99.99% | 8ms | 0.00% | 22% | 71% | HEALTHY |

### Metricas LLM
- Coste 24h: $12.40 | Tokens 24h: 1.2M | Tasa: 50K tok/h
- Proyeccion mensual: $372

**Estado global: HEALTHY**
Sin anomalias en las ultimas 6h.
```

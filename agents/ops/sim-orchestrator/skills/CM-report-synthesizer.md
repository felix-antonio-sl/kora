---
_manifest:
  urn: "urn:kora:agent-bootstrap:sim-orchestrator-cm-report-synthesizer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Purpose

Sintetizar resultados de evaluacion en un reporte estructurado con metricas, disclaimer SIMULATED y recomendaciones.

## Input/Output

- **Input:** evaluations: list, evidences: list, target_agent: {name, spec}
- **Output:** report: {summary, metrics, details, recommendations, disclaimer}

## Procedure

1. Agregar todas las evaluations recibidas del TESTER
2. Calcular metricas: total tests, pass count, fail count, pass rate
3. Priorizar hallazgos por impacto (CRITICAL > HIGH > MEDIUM > LOW)
4. Generar disclaimer: "TODA EVIDENCIA EN ESTE REPORTE ES SIMULATED"
5. Compilar sugerencias especificas por cada fallo
6. Estructurar reporte final con secciones

## Signature Output

```markdown
## Reporte Testing Simulado — [Agent Name]

> DISCLAIMER: Toda evidencia es SIMULATED. No sustituye testing real.

### Metricas
- Tests: N | Pass: M (X%) | Fail: K (Y%)

### Hallazgos
[Por prioridad: CRITICAL → LOW]

### Recomendaciones
[Acciones especificas]

### Proximos Pasos
- Testing real en entorno
```

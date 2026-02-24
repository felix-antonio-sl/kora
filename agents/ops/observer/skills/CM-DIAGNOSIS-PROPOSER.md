---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-cm-diagnosis-proposer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Basado en anomalia detectada y correlaciones calculadas, proponer top-3 hipotesis de diagnostico con confianza y recomendar accion concreta para cada una.

## Input/Output

- **Input:** anomaly: AnomalyEvent, correlations: CorrelationReport (output de CM-CORRELATION-ENGINE)
- **Output:** diagnosis: {hypotheses: [{rank, description, confidence_pct, evidence, recommended_action: ROLLBACK|INVESTIGATE|WAIT|ESCALATE, action_detail}], auto_rollback_eligible: bool, summary: string}

## Procedimiento

1. **Invocar diagnosis_propose** con anomalia y correlaciones.

2. **Generar hipotesis ordenadas por confianza:**
   - Hipotesis 1: basada en top correlation. Desarrollar mecanismo causal plausible.
   - Hipotesis 2: causa alternativa compatible con los datos. Considerar factores no correlacionados.
   - Hipotesis 3: causa de fondo (degradacion gradual, deuda tecnica, crecimiento organico). Siempre incluir una hipotesis no ligada a eventos recientes.

3. **Asignar accion recomendada por hipotesis:**
   - ROLLBACK: si el deploy correlacionado es la causa mas probable y el rollback es seguro
   - INVESTIGATE: si la confianza es insuficiente para rollback o el impacto del rollback es alto
   - WAIT: si la anomalia es leve y puede resolverse sola (spike transitorio, autoscaling)
   - ESCALATE: si el impacto es critico y requiere intervencion humana experta

4. **Evaluar elegibilidad auto-rollback:**
   - Condiciones TODAS requeridas:
     - Severidad anomalia: CRITICAL
     - Confianza correlacion con deploy: >= 85%
     - Deploy reciente (< 30 min)
     - Rollback no destructivo (no hay migracion de datos irreversible)
   - Si todas se cumplen: auto_rollback_eligible = true
   - Aun asi: el Operador DEBE aprobar. Proponer, no ejecutar.

5. **Generar resumen ejecutivo** con accion prioritaria.

## Signature Output

```yaml
diagnosis:
  hypotheses:
    - rank: 1
      description: "Migracion a modelo LLM v2 causa latencia superior"
      confidence_pct: 78
      evidence: "Deploy v2.4.1 (4 min antes), cambio de modelo, latencia LLM +600ms"
      recommended_action: ROLLBACK
      action_detail: "Rollback a v2.4.0. Restaura modelo anterior. Riesgo bajo."
    - rank: 2
      description: "Congestion red interna por pico trafico concurrente"
      confidence_pct: 12
      evidence: "Requests/s +40% en ventana de anomalia"
      recommended_action: INVESTIGATE
      action_detail: "Verificar logs de red y balanceador. Autoscaling puede resolver."
    - rank: 3
      description: "Degradacion gradual de pool conexiones PostgreSQL"
      confidence_pct: 8
      evidence: "Conexiones activas trending up ultimas 72h"
      recommended_action: WAIT
      action_detail: "Monitorear 30 min. Si persiste, investigar pool config."
  auto_rollback_eligible: false
  summary: "Hipotesis principal: migracion modelo LLM (78%). Recomendacion: ROLLBACK a v2.4.0. Aprobar?"
```

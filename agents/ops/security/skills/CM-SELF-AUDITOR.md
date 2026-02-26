---
_manifest:
  urn: "urn:ops:skill:security-self-auditor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar los 4 controles quis custodiet ipsos custodes sobre el propio agente de seguridad. Quien vigila al vigilante? Este CM verifica la integridad, rendimiento y diversidad del agente de seguridad. Detecta degradacion propia y genera flag para auditoria humana externa.

## I/O

- **Input:** own_config: AgentConfig, swarm_config: SwarmConfig, audit_logs: {period: DateRange, decisions: Decision[], findings_confirmed: number, findings_rejected: number}
- **Output:** meta_eval: {controls: ControlResult[], overall_status: OPERATIONAL|DEGRADED|COMPROMISED, flag_human_audit: boolean, next_audit_date: ISO8601}

## Procedimiento

1. **Control 1 — Diversidad de Modelo/Provider**:
   - Leer own_config.model y own_config.provider
   - Leer swarm_config.model y swarm_config.provider
   - IF mismo modelo → FAIL: "Mismo modelo que enjambre"
   - IF mismo provider → FAIL: "Mismo provider que enjambre"
   - IF mismo modelo OR mismo provider → overall_status = COMPROMISED, flag_human_audit = true
   - Pass: modelo Y provider diferentes

2. **Control 2 — Revision Logs Aprobacion/Rechazo**:
   - Calcular rejection_rate = decisions.rejected / decisions.total
   - Calcular approval_rate = decisions.approved / decisions.total
   - IF rejection_rate > 0.40 → WARNING: "Posible exceso de false positives (>40% rejection)"
   - IF approval_rate > 0.95 → WARNING: "Posible degradacion detectora (>95% approval)"
   - IF rejection_rate > 0.60 → FAIL: "Blocking excesivo, probable mal calibracion"
   - IF approval_rate > 0.99 → FAIL: "Approval rate anomalo, posible compromiso"
   - Buscar patrones: misma persona/PR bloqueada repetidamente, cambio brusco en tasas

3. **Control 3 — Tasas False Positive/Negative**:
   - false_positive_rate = findings_rejected / total_findings (hallazgos reportados que fueron revertidos/descartados)
   - false_negative_rate = incidents_missed / total_incidents (incidentes que pasaron sin deteccion)
   - IF false_positive_rate > 0.20 → WARNING: "Tasa false positive >20%, recalibrar"
   - IF false_negative_rate > 0.05 → FAIL: "Tasa false negative >5%, degradacion critica"
   - Tendencia: comparar contra periodos anteriores. IF empeorando → flag

4. **Control 4 — Flag Auditoria Humana Externa**:
   - IF cualquier control FAIL → flag_human_audit = true
   - IF 2+ controles WARNING → flag_human_audit = true
   - IF ultimo audit humano > 90 dias → flag_human_audit = true
   - Calcular next_audit_date: MIN(ultimo_audit + 30 dias, fecha de cualquier FAIL + 7 dias)

5. **Clasificar overall_status**:
   - OPERATIONAL: todos los controles PASS, warnings <= 1
   - DEGRADED: 1+ FAIL en controles 2-4, o 2+ WARNING
   - COMPROMISED: FAIL en control 1 (diversidad), o false_negative_rate > 0.10

## Signature Output

```yaml
meta_eval:
  controls:
    - id: "diversity_check"
      status: "PASS"
      detail: "own=claude-opus-4-6/anthropic, swarm=gpt-4o/openai — diferentes"
    - id: "log_review"
      status: "PASS"
      detail: "rejection_rate=17.7% (8/45), dentro de rango normal"
    - id: "false_rates"
      status: "WARNING"
      detail: "false_positive_rate=12.5% (1/8), tendencia estable. false_negative_rate=0%"
    - id: "human_audit"
      status: "PASS"
      detail: "Ultimo audit humano: 2026-02-01, dentro de ventana 30 dias"
  overall_status: "OPERATIONAL"
  flag_human_audit: false
  next_audit_date: "2026-03-01"
  recommendations:
    - "Revisar hallazgo revertido PR #76 para recalibrar heuristica auth detection"
```

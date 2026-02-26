---
_manifest:
  urn: "urn:ops:skill:security-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar contexto multi-turno de la sesion de seguridad. Mantener estado acumulado (hallazgos por PR, vetos emitidos, amenazas runtime, CVEs evaluados, tests adversariales) y generar resumen de sesion en nodo terminal.

## I/O

- **Input:** session_history: {turns: Turn[], current_state: FSM_State, prs_analyzed: PRAnalysis[], runtime_assessments: RuntimeAssessment[], dependency_audits: DependencyAudit[], adversarial_reports: AdversarialReport[], meta_evals: MetaEval[]}
- **Output:** session_summary: {prs_analyzed: number, findings_total: number, findings_by_severity: SeverityCount, vetos_emitted: number, threats_detected: number, cves_evaluated: number, adversarial_tests: number, meta_eval_status: string, timeline: TimelineEntry[]}

## Procedimiento

1. **Agregar analisis PR**:
   - Contar PRs analizados
   - Agrupar hallazgos por severidad: critical, high, medium, low
   - Contar vetos emitidos
   - Listar PRs bloqueados con razon

2. **Agregar monitoreo runtime**:
   - Contar assessments realizados
   - Clasificaciones: INFO, SUSPICIOUS, THREAT, ACTIVE_ATTACK
   - Intentos injection agent-to-agent detectados
   - Acciones recomendadas pendientes

3. **Agregar auditoria dependencias**:
   - Total CVEs encontrados vs CVEs expuestos
   - Mitigaciones propuestas por prioridad
   - Dependencias pendientes de upgrade

4. **Agregar testing adversarial**:
   - Tests ejecutados, pass rate
   - Vulnerabilidades por categoria y severidad
   - Regresiones detectadas

5. **Agregar meta-evaluacion**:
   - Estado de los 4 controles quis custodiet
   - Flag auditoria humana si aplica
   - Proxima fecha auditoria

6. **Compilar timeline**:
   - Secuencia cronologica de acciones
   - Timestamps por accion
   - Duracion total sesion

7. **Detectar patrones sesion**:
   - IF veto rate > 50% → recomendar revision de standards del equipo
   - IF mismo tipo hallazgo en multiples PRs → recomendar training o tooling
   - IF CVEs expuestos no mitigados → recomendar sprint de seguridad

## Signature Output

```yaml
session_summary:
  prs_analyzed: 3
  findings_total: 5
  findings_by_severity:
    critical: 2
    high: 1
    medium: 2
    low: 0
  vetos_emitted: 1
  threats_detected: 0
  cves_evaluated: 12
  cves_exposed: 2
  adversarial_tests: 0
  meta_eval_status: "OPERATIONAL"
  timeline:
    - timestamp: "2026-02-24T14:00:00Z"
      action: "ANALISIS_PR"
      detail: "PR #87 → 2 findings (1 critical, 1 medium) → VETO"
    - timestamp: "2026-02-24T14:15:00Z"
      action: "ANALISIS_PR"
      detail: "PR #92 → LIMPIO"
    - timestamp: "2026-02-24T14:30:00Z"
      action: "DEPENDENCIAS"
      detail: "12 CVEs evaluados, 2 expuestos (1 critical, 1 high)"
    - timestamp: "2026-02-24T14:45:00Z"
      action: "ANALISIS_PR"
      detail: "PR #95 → 2 findings (1 high, 1 medium)"
  blocked_prs:
    - pr: "#87"
      reason: "Endpoint sin auth expone PII a internet"
  pending_mitigations:
    - "requests upgrade >=2.31.0 (CRITICAL)"
    - "pyyaml upgrade >=6.0.1 (MEDIUM)"
  recommendation: "Patron: 2/3 PRs con hallazgos auth. Recomendar training equipo en secure endpoint design."
```

---
_manifest:
  urn: "urn:ops:agent-bootstrap:verificador-tools:1.0.0"
  type: "bootstrap_tools"
---

## ci_execute

- **Firma:** changeset: {files: string[], pr_metadata: PRInfo} → ci_result: {status: pass|fail, lint: LintResult, types: TypeCheckResult, tests: TestResult, duration_ms: number}
- **Cuando usar:** S-CAPA-CI. Ejecutar lint + type check + tests unitarios sobre un changeset.
- **Cuando NO usar:** CI ya ejecutado en turno actual. Fuera del contexto de verificacion.
- **Notas:** Resultado binario. Si cualquier componente (lint, types, tests) falla, el resultado global es fail. Reportar detalle del componente fallido.

## regression_run

- **Firma:** changeset: Changeset, dataset: {golden?: GoldenDataset, regression: RegressionDataset} → regression_result: {status: pass|degraded, outputs_compared: number, degradations: Degradation[], delta: DeltaReport}
- **Cuando usar:** S-CAPA-REGRESION. Ejecutar dataset de regresion y comparar outputs vs expected.
- **Cuando NO usar:** Sin changeset clasificado. CI no ejecutado previamente.
- **Notas:** Si golden dataset disponible, usar como anchor. Reportar delta con evidencia. Si no hay dataset, emitir WARN y pass condicional (no silenciar la ausencia).

## diversity_check

- **Firma:** coder_info: {provider: string, model: string}, reviewer_info: {provider: string, model: string}, changeset: Changeset → diversity_result: {status: pass|fail, same_provider: boolean, cross_eval: EvalResult, coder_provider: string, reviewer_provider: string}
- **Cuando usar:** S-CAPA-DIVERSIDAD. Verificar que reviewer usa provider diferente al coder y ejecutar cross-eval.
- **Cuando NO usar:** Sin informacion de providers. Sin changeset.
- **Notas:** Verificacion de provider es prerequisito. IF mismo provider → fail inmediato SIN ejecutar cross-eval. La diversidad se verifica, no se asume.

## security_scan

- **Firma:** changeset: Changeset, architecture_context?: ArchitectureDoc → security_result: {status: pass|fail, static_analysis: SASTResult, dynamic_analysis: DASTResult, privilege_check: PrivilegeResult, findings: SecurityFinding[], prioritized_by_impact: boolean}
- **Cuando usar:** S-CAPA-SEGURIDAD. Ejecutar analisis estatico + dinamico + check de privilegios.
- **Cuando NO usar:** Para cambios tipo lectura (no requieren capa 4). Sin changeset.
- **Notas:** Analisis contextual con ARCHITECTURE.md si disponible. Priorizar hallazgos por impacto real, no por volumen. Hallazgos criticos → fail. Hallazgos medium/low → pass con warnings.

## human_gate

- **Firma:** verification_summary: {layers_executed: LayerResult[], change_type: destructiva, recommendation: string, evidence: Evidence[]} → gate_result: {status: approved|rejected|timeout, operator_comment?: string, timestamp: ISO8601}
- **Cuando usar:** S-CAPA-HUMANA. Solo para cambios destructivos. Presentar resumen y esperar aprobacion.
- **Cuando NO usar:** Para cambios lectura o escritura. Sin capas previas ejecutadas.
- **Notas:** HOLD hasta que el Operador apruebe o rechace. Timeout configurable. NUNCA aprobar automaticamente. Presentar resumen completo de todas las capas + recomendacion basada en evidencia.

## verification_report

- **Firma:** session: {change_type: string, layers_required: number[], layers_results: LayerResult[], verdict: APROBADO|RECHAZADO} → report: {summary: string, layers_table: LayerTable, verdict: string, evidence: Evidence[], recommendation: string}
- **Cuando usar:** S-END. Generar reporte final de verificacion con evidencia por capa.
- **Cuando NO usar:** Sin capas ejecutadas.
- **Notas:** Reporte incluye tabla de capas con estado, detalle y evidencia. Verdict claro. Si rechazado, indicar capa fallida y accion requerida.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Xanpan metodologia, verificacion, 5 capas | urn:fxsl:kb:xanpan-agents-metodologia |
| Swarm ops, verificacion multi-capa, CI verde insuficiente | urn:fxsl:kb:swarm-ops-metodologia |
| Agent spec, workspace, FSM | urn:kora:kb:agent-spec-md |

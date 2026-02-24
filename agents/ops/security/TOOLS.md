---
_manifest:
  urn: "urn:ops:agent-bootstrap:security-tools:1.0.0"
  type: "bootstrap_tools"
---

## pr_security_analyze

- **Firma:** pr: {diff: string, architecture: ArchDoc, metadata: PRInfo} → analysis: {findings: Finding[], attack_surfaces: string[], veto: boolean, summary: string}
- **Cuando usar:** S-ANALISIS-PR. Analizar seguridad de un PR con contexto arquitectonico.
- **Cuando NO usar:** Sin ARCHITECTURE.md disponible. Sin diff. Analisis ya completado en turno actual.
- **Notas:** Requiere ARCHITECTURE.md como contexto obligatorio. Clasifica superficie de ataque: auth, data, external_interfaces, crypto, llm_prompt. Cada finding: severity, evidence(file:line), attack_vector, real_impact, suggested_fix.

## runtime_monitor

- **Firma:** baseline: BehaviorBaseline, current: BehaviorSnapshot → assessment: {classification: INFO|SUSPICIOUS|THREAT|ACTIVE_ATTACK, anomalies: Anomaly[], patterns: Pattern[]}
- **Cuando usar:** S-RUNTIME. Monitorear patrones de comportamiento en produccion contra baseline.
- **Cuando NO usar:** Sin baseline establecido. Para WAF rules estaticas (no es WAF).
- **Notas:** Detecta patrones anomalos: acceso fuera horario, volumenes atipicos, payloads con encoding anomalo, intentos escalacion, prompt injection agent-to-agent. Entiende que es "normal" para la app.

## cve_check

- **Firma:** dependencies: {name: string, version: string}[] → cves: {dependency: string, cve_id: string, severity: string, description: string, affected_versions: string}[]
- **Cuando usar:** S-DEPENDENCIAS. Consultar base CVE para dependencias del proyecto.
- **Cuando NO usar:** Dependencias ya consultadas en turno actual.
- **Notas:** Retorna CVEs raw. Requiere exposure_evaluate para determinar si la vulnerabilidad esta realmente expuesta.

## exposure_evaluate

- **Firma:** cve: CVEInfo, codebase: {usage_locations: FileLocation[], input_sources: InputSource[]} → exposure: {exposed: boolean, reason: string, priority: critical|high|medium|low, mitigation: string}
- **Cuando usar:** S-DEPENDENCIAS, despues de cve_check. Evaluar si un CVE tiene exposicion real en el codebase.
- **Cuando NO usar:** Sin resultado cve_check previo. Para CVEs sin uso de la funcion vulnerable.
- **Notas:** CVE + funcion vulnerable expuesta a input externo = EXPOSED. CVE + funcion vulnerable solo en path interno con input controlado = NOT EXPOSED. Diferencia entre "tiene CVE" y "el CVE nos afecta".

## adversarial_test

- **Firma:** target: {agent_id: string, endpoint: string, test_category: string} → result: {vector: string, outcome: pass|fail, severity: string, reproducibility: string, evidence: string}
- **Cuando usar:** S-ADVERSARIAL. Ejecutar test adversarial contra un agente o endpoint del enjambre.
- **Cuando NO usar:** Fuera de ventana de testing (mensual o recalibracion). Sin aprobacion para testing destructivo.
- **Notas:** Categorias: prompt_injection (direct, indirect, agent-to-agent), validation_bypass (schema, auth, input), privilege_escalation (horizontal, vertical), owasp_llm_top10.

## self_audit

- **Firma:** audit_period: {start: ISO8601, end: ISO8601}, logs: AuditLog[] → meta_eval: {diversity_check: boolean, rejection_rate: float, false_positive_rate: float, false_negative_rate: float, degraded: boolean, recommendations: string[]}
- **Cuando usar:** S-META-EVAL. Ejecutar los 4 controles quis custodiet sobre el propio agente.
- **Cuando NO usar:** Periodo de auditoria menor a 7 dias (datos insuficientes).
- **Notas:** 4 controles: (1) modelo diferente al enjambre, (2) revision logs aprobacion/rechazo, (3) tasas false positive/negative, (4) flag si degradado para auditoria humana externa.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Xanpan metodologia, agentes, swarm | urn:fxsl:kb:xanpan-agents-metodologia |
| Swarm ops, seguridad, enjambre | urn:fxsl:kb:swarm-ops-metodologia |
| Agent spec, workspace, FSM | urn:kora:kb:agent-spec-md |
| Stack LLM, arquitectura, providers | urn:fxsl:kb:stack-llm-arquitectura |

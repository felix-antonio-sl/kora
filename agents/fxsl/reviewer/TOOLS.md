---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:reviewer-tools:1.0.0"
  type: "bootstrap_tools"
---

## pr_read

- **Firma:** {pr_ref: string} → {titulo, descripcion, diff, archivos_modificados[], tests_agregados[], historia_asociada?}
- **Cuando usar:** S-REVIEW. Leer PR completo antes de revisar.
- **Cuando NO usar:** Si el PR ya fue leido en este turno.
- **Notas:** Leer SIEMPRE el diff completo, no solo el resumen.

## convention_check

- **Firma:** {diff: string, conventions: CONVENTIONS.md} → {hallazgos: [{severidad, archivo, linea, violacion, sugerencia}]}
- **Cuando usar:** S-REVIEW. Verificar conformidad con convenciones del proyecto.
- **Notas:** Verificar: naming, estructura de archivos, patrones de error handling, imports, exports.

## type_audit

- **Firma:** {diff: string} → {hallazgos: [{archivo, linea, tipo_problema, sugerencia}]}
- **Cuando usar:** S-REVIEW. Verificar type safety.
- **Notas:** Buscar: `any`, `unknown` sin refinamiento, `as` casts innecesarios, Zod/Pydantic ausente en boundaries, tipos implícitos en funciones publicas.

## test_coverage_audit

- **Firma:** {diff: string, criterios_aceptacion: string[]} → {acs_cubiertos: [{ac, test_asociado, cubierto: bool}], funciones_sin_test: string[]}
- **Cuando usar:** S-REVIEW. Verificar que tests cubren ACs y funciones nuevas.
- **Notas:** Cada AC DEBE tener al menos un test. Cada funcion publica nueva DEBE tener test unitario.

## security_scan

- **Firma:** {diff: string, architecture: ARCHITECTURE.md?} → {hallazgos: [{severidad, categoria_owasp, archivo, linea, descripcion, sugerencia}]}
- **Cuando usar:** S-SEGURIDAD. Analisis de seguridad contextual.
- **Notas:** Verificar: input validation, SQL injection, XSS, secrets hardcoded, privilege escalation, data exposure, prompt injection (si toca LLM). Analizar en contexto de ARCHITECTURE.md.

## eval_runner

- **Firma:** {tipo: regresion|alucinacion|coste, dataset?: string} → {resultado: PASS|FAIL, detalles: string[]}
- **Cuando usar:** S-EVAL. Ejecutar evals automatizados contra dataset.
- **Cuando NO usar:** Si no hay dataset de regresion disponible (reportar como NO_DATASET).
- **Notas:** Eval de regresion: ejecutar dataset de input→output esperado. Eval de alucinacion: verificar que outputs no contienen informacion fabricada. Eval de coste: tokens en rango esperado.

## verdict_issue

- **Firma:** {hallazgos_review[], hallazgos_seguridad[], resultados_eval[]} → {veredicto: APPROVE|REQUEST_CHANGES|REJECT, justificacion, hallazgos_consolidados[]}
- **Cuando usar:** S-VEREDICTO. Sintetizar y emitir veredicto final.
- **Notas:** APPROVE: 0 criticos, 0 mayores. REQUEST_CHANGES: >0 mayores, 0 criticos. REJECT: >0 criticos o violacion de principio fundamental.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Consultar corpus para decisiones de review.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| DoD, evals, diversidad modelos, calidad, code review, TDD | urn:fxsl:kb:xanpan-agents-metodologia |
| Stack, tipos, validacion, seguridad OWASP, aislamiento | urn:fxsl:kb:stack-llm-arquitectura |
| CI/CD, 5 capas verificacion, agente-security | urn:fxsl:kb:swarm-ops-metodologia |
| Context engineering, regla 70/30 | urn:fxsl:kb:chapter0-operador-solitario |

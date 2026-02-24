---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:sentinel-tools:1.0.0"
  type: "bootstrap_tools"
---

## context_diff

- **Firma:** {context_file: string, codebase_path: string} → {drift_detected: bool, diffs: [{seccion, estado_declarado, estado_real, diff_propuesto}]}
- **Cuando usar:** S-CONTEXT-HYGIENE. Comparar context file contra realidad del codebase.
- **Cuando NO usar:** Si el context file ya fue auditado en este Pulso.
- **Notas:** Auditar: CONVENTIONS.md (naming, patrones, estructura), ARCHITECTURE.md (componentes, flujos, dependencias), SCHEMA.md (tablas, relaciones, tipos).

## swarm_metrics

- **Firma:** {periodo: string} → {metricas: {ta_por_agente: {}, cycle_time_por_zona: {}, cph_promedio: float, fallback_rate: float, rechazos_patron: string[]}}
- **Cuando usar:** S-SWARM-AUDIT. Recopilar metricas agregadas del enjambre.
- **Cuando NO usar:** Si no hay datos de ejecucion del enjambre disponibles.
- **Notas:** Metricas de Xanpan::Agents §14.1: 5 dimensiones (coste, calidad, velocidad, modelo, enjambre).

## eval_coverage

- **Firma:** () → {evals_existentes: [{tipo, cobertura, ultima_ejecucion}], gaps: [{area, tipo_eval_faltante, riesgo}], golden_dataset_status: {size, freshness}}
- **Cuando usar:** S-EVAL-AUDIT. Revisar corpus de evals y detectar gaps.
- **Notas:** Verificar que cada incidente previo (bug, rechazo, vulnerabilidad) tiene eval de regresion.

## purple_card_create

- **Firma:** {tipo: ajuste_prompt|nuevo_eval|reconfig_topologia|context_update|model_change, descripcion: string, justificacion: string, datos_soporte: {}, impacto: alto|medio|bajo, riesgo: alto|medio|bajo} → {tarjeta: PurpleCard}
- **Cuando usar:** S-PURPLE-CARD. Generar propuesta de mejora formal.
- **Notas:** SIEMPRE marcar como "requiere aprobacion humana". NUNCA auto-ejecutar. Justificacion DEBE incluir datos.

## self_eval_run

- **Firma:** {tarjetas_aplicadas: PurpleCard[], metricas_antes: {}, metricas_despues: {}} → {tasa_mejora: float, tarjetas_efectivas: [], tarjetas_sin_efecto: [], tarjetas_contraproducentes: []}
- **Cuando usar:** S-SELF-EVAL. Evaluar retroactivamente las propuestas del sentinel.
- **Notas:** Tasa <50% = alertar Operador. El sentinel no se auto-protege: si no sirve, lo dice.

## adversarial_test

- **Firma:** {test_suite: string} → {resultado: PASS|FAIL, categorias_falladas: string[]}
- **Cuando usar:** S-SELF-EVAL. Someterse a pruebas adversariales periodicas.
- **Notas:** Tests: prompt injection, bypass de validacion, falsa urgencia, manipulacion de metricas. Mensual o ante recalibracion.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Consultar corpus para decisiones de auditoria.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Sentinel, enjambre auto-evolutivo, tarjetas purpura, quis custodiet, evals, DoD, metricas | urn:fxsl:kb:xanpan-agents-metodologia |
| Context engineering, regla 70/30, artefactos, economia contexto | urn:fxsl:kb:stack-llm-arquitectura |
| Observabilidad, agente-observer, circuit breakers, modos de fallo | urn:fxsl:kb:swarm-ops-metodologia |
| Operador solitario, fases, dual-hat, context engineering progresivo | urn:fxsl:kb:chapter0-operador-solitario |

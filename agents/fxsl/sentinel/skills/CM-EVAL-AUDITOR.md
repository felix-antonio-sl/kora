---
_manifest:
  urn: "urn:fxsl:skill:sentinel-eval-auditor:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-EVAL-AUDITOR

## Proposito
Audita el corpus de evals del enjambre: cobertura, freshness, gaps, golden dataset. Propone nuevos evals.

## Procedimiento
1. Inventariar evals existentes por tipo:
   - Regresion: ¿dataset curado? ¿cuantos casos? ¿ultima ejecucion?
   - Alucinacion: ¿golden dataset humano-curado? ¿tamano? ¿freshness?
   - Tool-calling: ¿cobertura de herramientas? ¿accuracy medida?
   - Seguridad: ¿OWASP Top 10 cubierto? ¿prompt injection inter-agente? ¿escalada privilegios?
   - Coste: ¿budget enforcement activo? ¿alertas configuradas?
   - Adversarial: ¿existe suite? ¿frecuencia de ejecucion?
2. Detectar gaps de cobertura:
   - Areas del codebase sin eval de regresion.
   - Features nuevas sin eval de alucinacion.
   - Interfaces LLM sin eval de prompt injection.
   - Incidentes previos (bugs, rechazos, vulnerabilidades) sin eval de regresion correspondiente.
3. Evaluar golden dataset:
   - ¿Tamano suficiente? (minimo 20-50 casos por agente, Xanpan §9.2).
   - ¿Respuestas escritas por humanos? (no generadas por agentes — ancla contra drift).
   - ¿Freshness? (actualizado en ultimo Ciclo).
4. Detectar evals obsoletos: evals que ya no aplican por cambio de stack o feature eliminada.
5. Proponer nuevos evals como tarjetas purpura con prioridad.

## Output
Reporte: {evals_existentes: [{tipo, cobertura, freshness}], gaps: [{area, eval_faltante, prioridad}], golden_dataset: {size, humano_curado, freshness}, evals_obsoletos[], propuestas_nuevos_evals[]}.

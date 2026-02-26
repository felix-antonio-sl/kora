---
_manifest:
  urn: "urn:fxsl:skill:reviewer-eval-executor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-EVAL-EXECUTOR

## Proposito
Ejecuta evals automatizados aplicables al PR. Capa 2-4 de las 5 capas de verificacion (Swarm::Ops §4.4).

## Procedimiento
1. Determinar evals aplicables segun tipo de cambio:
   - Todo PR: eval de regresion (si existe dataset).
   - PR que toca logica LLM/agentes: eval de alucinacion + eval de tool-calling.
   - PR que cambia modelo o config de agente: eval de coste.
   - PR que toca seguridad: eval de seguridad (cubierto por CM-SECURITY-REVIEWER).
2. Eval de regresion:
   - Ejecutar dataset de input→output esperado.
   - Verificar que outputs no degradan vs baseline.
   - Resultado: PASS(sin regresion) | FAIL(regresion detectada) | NO_DATASET(sin dataset disponible).
3. Eval de alucinacion:
   - Verificar que outputs del agente no contienen informacion fabricada.
   - Comparar contra golden dataset (humano-curado) si disponible.
   - Resultado: PASS | FAIL | NO_GOLDEN_DATASET.
4. Eval de coste:
   - Estimar tokens consumidos por la nueva logica.
   - Comparar contra presupuesto del Ciclo.
   - Resultado: PASS(dentro de presupuesto) | WARNING(>80% presupuesto) | FAIL(excede presupuesto).
5. Consolidar resultados de todos los evals ejecutados.

## Output
Resultados: [{tipo_eval, resultado: PASS|FAIL|WARNING|NO_DATASET, detalles}]. Resumen: X evals ejecutados, Y pasaron, Z fallaron.

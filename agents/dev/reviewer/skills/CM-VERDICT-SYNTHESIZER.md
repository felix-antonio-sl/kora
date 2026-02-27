---
_manifest:
  urn: "urn:dev:skill:reviewer-verdict-synthesizer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-VERDICT-SYNTHESIZER

## Proposito
Consolida hallazgos de todas las fases de review y emite veredicto final justificado.

## Procedimiento
1. Recopilar hallazgos de:
   - CM-CODE-REVIEWER: calidad, convenciones, tipos, tests.
   - CM-SECURITY-REVIEWER: seguridad, superficie de ataque.
   - CM-EVAL-EXECUTOR: regresion, alucinacion, coste.
2. Consolidar por severidad:
   - Contar CRITICOS, MAYORES, MENORES, NOTAS.
   - Listar evals PASS, FAIL, WARNING.
3. Aplicar reglas de veredicto:
   - **APPROVE:** 0 CRITICOS, 0 MAYORES, 0 evals FAIL. Puede tener MENORES y NOTAS.
   - **REQUEST_CHANGES:** 0 CRITICOS, >0 MAYORES o evals WARNING. Corregible sin rediseno.
   - **REJECT:** >0 CRITICOS, o eval FAIL critico, o violacion de principio fundamental (ej: zero tests, `any` masivo, secret hardcoded).
4. Generar reporte final:
   - Resumen ejecutivo (1-2 lineas): "PR de [tipo] para [historia]. Veredicto: [X]."
   - Tabla de hallazgos ordenada por severidad.
   - Resultados de evals.
   - Veredicto con justificacion.
   - Si REQUEST_CHANGES o REJECT: lista concreta de acciones para el coder.
5. Si APPROVE: reconocer brevemente el buen trabajo. No ser efusivo.

## Output
Reporte: {resumen, hallazgos_tabla[], evals_resultados[], veredicto, justificacion, acciones_requeridas[]?}.

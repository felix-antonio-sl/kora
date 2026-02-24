---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:tester-tools:1.0.0"
  type: "bootstrap_tools"
---

## ac_parse

- **Firma:** {historia_id: string} → {criterios_aceptacion: [{id, dado, cuando, entonces}], historia_resumen: string}
- **Cuando usar:** S-ACCEPTANCE. Extraer y estructurar los ACs de una historia antes de generar tests.
- **Cuando NO usar:** Si los ACs ya fueron parseados en este turno.
- **Notas:** Si la historia no tiene ACs, RECHAZAR y derivar a fxsl/planner. Cada AC DEBE tener condicion (dado), accion (cuando) y resultado esperado (entonces).

## acceptance_test_generate

- **Firma:** {criterios_aceptacion: AC[], framework: vitest|pytest} → {tests: [{ac_id, test_code, formato: DADO_CUANDO_ENTONCES}]}
- **Cuando usar:** S-ACCEPTANCE. Generar tests ejecutables desde ACs parseados.
- **Cuando NO usar:** Si no se han parseado ACs primero (requiere ac_parse previo).
- **Notas:** Un test minimo por AC. Formato DADO/CUANDO/ENTONCES obligatorio. Tests independientes entre si. Deterministas.

## integration_test_generate

- **Firma:** {componentes: string[], boundaries: [{from, to, protocolo}]} → {tests: [{boundary, test_code, tipo: api|db|service}]}
- **Cuando usar:** S-INTEGRATION. Generar tests de integracion para boundaries entre componentes.
- **Cuando NO usar:** Si no se han identificado boundaries. Si el test es de logica interna (→test unitario, responsabilidad del coder).
- **Notas:** Cubrir: happy path, error path, edge cases por boundary. Tipos: endpoint API (HTTP), query DB (SQL), servicio externo (mock/stub).

## test_run

- **Firma:** {suite: acceptance|integration|unit|all, filter?: string} → {resultados: [{test_name, status: pass|fail, tiempo_ms, error?: string, stack_trace?: string}], resumen: {total, passed, failed, tiempo_total_ms}}
- **Cuando usar:** S-EXECUTE. Ejecutar suite de tests.
- **Cuando NO usar:** Si no hay tests generados o existentes para ejecutar.
- **Notas:** Ejecutar en entorno sandboxed. Reportar cada test individualmente. Stack trace completo en fallos. Agrupar por tipo.

## coverage_report

- **Firma:** {historia?: string, componente?: string} → {cobertura_por_ac: [{ac_id, tests_count, status}], cobertura_por_componente: [{componente, tests_count, tipos}], cobertura_por_tipo: {unit, acceptance, integration}, gaps: [{tipo, descripcion}]}
- **Cuando usar:** S-COVERAGE. Generar reporte de cobertura.
- **Cuando NO usar:** Si no se ha ejecutado la suite primero (requiere resultados de test_run).
- **Notas:** Gaps criticos: ACs sin test, componentes sin test de integracion, boundaries descubiertos. Presentar como tabla.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Consultar corpus xanpan para decisiones de testing y metodologia.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| TDD, evals, DoD, code review, testing standards, quality, aceptacion | urn:fxsl:kb:xanpan-agents-metodologia |
| Stack, TypeScript, Next.js, FastAPI, PostgreSQL, vitest, pytest, frameworks | urn:fxsl:kb:stack-llm-arquitectura |
| CI/CD, pipeline, test execution, environments, aislamiento | urn:fxsl:kb:swarm-ops-metodologia |
| Fases, context engineering minimo, perfil de proyecto | urn:fxsl:kb:chapter0-operador-solitario |

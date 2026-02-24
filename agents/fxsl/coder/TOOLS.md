---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:coder-tools:1.0.0"
  type: "bootstrap_tools"
---

## story_consume

- **Firma:** {historia_id: string} → {who_what_why, criterios_aceptacion[], valor, complejidad, riesgo, dependencias[]}
- **Cuando usar:** S-PLANIFICAR. Leer y entender la historia antes de planificar implementacion.
- **Cuando NO usar:** Si la historia ya fue consumida en este turno.
- **Notas:** Si faltan elementos, RECHAZAR y derivar a fxsl/planner.

## implementation_plan

- **Firma:** {historia: story, context_files: string[]} → {tareas: [{orden, descripcion, archivos_afectados[], tipo: type|test|code|refactor}], estimacion_complejidad}
- **Cuando usar:** S-PLANIFICAR. Generar plan de implementacion descompuesto en tareas.
- **Cuando NO usar:** Si el plan ya fue generado y aprobado.
- **Notas:** DEBE consumir CONVENTIONS.md y SCHEMA.md como contexto minimo. El plan DEBE presentarse al Operador antes de ejecutar.

## type_define

- **Firma:** {contrato: string} → {tipos: TypeDefinition[]}
- **Cuando usar:** S-IMPLEMENTAR, primera tarea de cada bloque. Definir tipos/interfaces antes de implementar.
- **Cuando NO usar:** Si los tipos ya existen y son correctos para la tarea.
- **Notas:** TypeScript: interfaces + Zod schemas. Python: Pydantic models. NUNCA `any`.

## test_write

- **Firma:** {tipo: unit|integration|acceptance, descripcion: string, criterio_aceptacion?: string} → {test_code: string, framework: vitest|pytest}
- **Cuando usar:** S-IMPLEMENTAR, ANTES de escribir codigo de produccion. S-DEPURAR, para reproducir bug.
- **Cuando NO usar:** Nunca omitir. TDD es obligatorio.
- **Notas:** Tests de aceptacion derivados de ACs de la historia. Tests unitarios por funcion/componente. Framework: vitest (TypeScript), pytest (Python).

## code_generate

- **Firma:** {tarea: string, tipos: TypeDefinition[], tests: TestCode[]} → {codigo: string, archivos: [{path, content}]}
- **Cuando usar:** S-IMPLEMENTAR, DESPUES de definir tipos y escribir tests.
- **Cuando NO usar:** Antes de tener tests escritos (viola TDD).
- **Notas:** DEBE respetar CONVENTIONS.md. DEBE hacer pasar los tests existentes. Codigo minimo necesario.

## lint_typecheck

- **Firma:** {archivos: string[]} → {lint_ok: bool, type_ok: bool, errores: string[]}
- **Cuando usar:** S-INTEGRAR, antes de generar PR.
- **Implementacion:** `tsc --noEmit` + ESLint (TypeScript), `ruff` + `mypy` (Python).
- **Notas:** Si falla, corregir antes de generar PR. Zero warnings en PR.

## pr_generate

- **Firma:** {historia: story, archivos_modificados: string[], tests_agregados: string[]} → {pr: {titulo, descripcion, archivos, checklist}}
- **Cuando usar:** S-INTEGRAR, despues de lint+types verdes.
- **Cuando NO usar:** Si lint o types fallan.
- **Notas:** Formato: What (que cambia), Why (historia asociada), How (approach), Tests (que se agrego). Titulo < 70 chars.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Consultar corpus xanpan para decisiones tecnicas.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Stack, TypeScript, Next.js, FastAPI, PostgreSQL, Drizzle, Zod, Pydantic, Docker | urn:fxsl:kb:stack-llm-arquitectura |
| TDD, evals, DoD, code review, coding standards, quality | urn:fxsl:kb:xanpan-agents-metodologia |
| CI/CD, pipeline, deploy, feature flags, aislamiento | urn:fxsl:kb:swarm-ops-metodologia |
| Fases, context engineering minimo, perfil de proyecto | urn:fxsl:kb:chapter0-operador-solitario |

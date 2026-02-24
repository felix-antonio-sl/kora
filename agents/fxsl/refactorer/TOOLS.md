---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:refactorer-tools:1.0.0"
  type: "bootstrap_tools"
---

## complexity_analyze

- **Firma:** {zona: string, archivos?: string[]} → {funciones: [{nombre, archivo, complejidad_ciclomatica, lineas, parametros}], promedio, max, distribucion}
- **Cuando usar:** S-ANALIZAR. Calcular complejidad ciclomatica por funcion/metodo en una zona del codebase.
- **Cuando NO usar:** Para medir cobertura de tests (eso es del tester). Para evaluar calidad de PR (eso es del reviewer).
- **Notas:** Umbral de alerta: complejidad >10 por funcion. Resultado ordenado por complejidad descendente.

## duplication_detect

- **Firma:** {zona: string, min_lines?: number} → {bloques_duplicados: [{fragmento, archivos: [{path, linea_inicio}], lineas}], porcentaje_duplicacion, total_lineas_duplicadas}
- **Cuando usar:** S-ANALIZAR. Detectar bloques de codigo duplicado (default >=5 lineas identicas o casi identicas).
- **Cuando NO usar:** Para detectar copy-paste entre proyectos diferentes.
- **Notas:** Detecta duplicacion exacta y near-duplicates (>80% similitud). Agrupa clones por cluster.

## refactor_apply

- **Firma:** {tipo: refactoring_type, target: string, parametros: object} → {archivos_modificados: [{path, diff}], tests_status: pass|fail, metricas: {antes, despues}}
- **Cuando usar:** S-REFACTORIZAR. Aplicar un refactoring atomico con verificacion de tests.
- **Cuando NO usar:** Para implementar features nuevas (→fxsl/coder). Para cambios que alteran comportamiento observable.
- **Notas:** Tipos soportados: extract_function, rename, simplify_conditional, remove_duplication, extract_component, improve_types, inline_temp, replace_magic_number, decompose_conditional, consolidate_duplicate_conditional. SIEMPRE verificar tests antes y despues.

## dependency_audit

- **Firma:** {manifest: string} → {outdated: [{nombre, version_actual, version_latest, tipo_update: major|minor|patch, breaking_changes?: string[]}], deprecated: [{nombre, razon, alternativa}], vulnerabilities: [{nombre, severidad, cve}]}
- **Cuando usar:** S-MODERNIZAR. Auditar dependencias del proyecto contra versiones actuales y vulnerabilidades conocidas.
- **Cuando NO usar:** Para evaluar dependencias de un proyecto ajeno.
- **Notas:** Lee package.json (Node), requirements.txt/pyproject.toml (Python). Clasifica riesgo de update.

## debt_catalog

- **Firma:** {zona: string, items: debt_item[]} → {catalogo: [{id, descripcion, severidad, esfuerzo, tipo, archivo, metricas}], tendencia: {resueltos_cycle, pendientes, delta}}
- **Cuando usar:** S-DEUDA. Catalogar y rastrear items de deuda tecnica. Generar reporte de tendencia para Retrospectiva Analitica.
- **Cuando NO usar:** Para planificar historias de negocio (→fxsl/planner).
- **Notas:** Severidad: CRITICA|ALTA|MEDIA|BAJA. Esfuerzo: XS|S|M|L|XL. Tipo: complejidad|duplicacion|naming|dependencias|patrones|tipos.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Consultar corpus xanpan para decisiones de refactoring y mejora continua.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Stack, TypeScript, Next.js, FastAPI, PostgreSQL, Drizzle, Zod, Pydantic, Docker | urn:fxsl:kb:stack-llm-arquitectura |
| TDD, evals, DoD, code review, coding standards, quality, refactoring | urn:fxsl:kb:xanpan-agents-metodologia |
| CI/CD, pipeline, deploy, feature flags, aislamiento | urn:fxsl:kb:swarm-ops-metodologia |
| Fases, context engineering minimo, perfil de proyecto | urn:fxsl:kb:chapter0-operador-solitario |

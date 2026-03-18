---
_manifest:
  urn: "urn:dev:agent-bootstrap:steipete-tools:1.0.0"
  type: "bootstrap_tools"
---

## dispatch_worker

- **Firma:** `package: WorkPackage -> WorkerHandle`
- **Parámetros:** `package` contiene: archivos target, intención en lenguaje natural, blast radius estimado, close-the-loop criteria, CLI preferido (claude-code/codex/gemini-cli/opencode), modelo específico
- **Cuando usar:** En S-DISPATCH, cuando un paquete de trabajo está listo para ejecución
- **Cuando NO usar:** Sin blast radius evaluado (INV-02). Para preguntas o consultas.
- **Descripción funcional:** Envía paquete a obrero de código via exec. El obrero recibe la intención, lee el codebase, ejecuta el ciclo (types → tests → code → lint → commit), y reporta resultado.
- **Notas:** En transmutación OpenClaw, mapea a `exec: claude -p "..."`, `exec: codex --task "..."`, `exec: gemini -p "..."`, o `exec: opencode -p "..."` según CLI seleccionado

## monitor_workers

- **Firma:** `filter?: WorkerFilter -> WorkerStatus[]`
- **Parámetros:** `filter` opcional: por worker_id, estado (running/completed/failed), tiempo
- **Cuando usar:** En S-MONITOR para verificar progreso. En S-DISPATCHER si Felix pregunta status.
- **Cuando NO usar:** Antes de despachar (no hay workers)
- **Descripción funcional:** Retorna estado de obreros activos: running, completed, failed, tiempo transcurrido, último output
- **Notas:** Polling pattern. No bloquea.

## cancel_worker

- **Firma:** `worker_id: string -> CancelResult`
- **Parámetros:** `worker_id` del obrero a cancelar
- **Cuando usar:** Obrero stuck en loop, produciendo garbage, o superando tiempo razonable
- **Cuando NO usar:** Cuando obrero está haciendo progreso visible. Paciencia.
- **Descripción funcional:** Envía señal de cancelación al obrero. Cambios parciales del obrero quedan en el filesystem.
- **Notas:** Steinberger: "Don't fear stopping models mid-way — file changes are atomic and they're good at picking up where they stopped"

## search_kb

- **Firma:** `query: string -> KBEntry[]`
- **Parámetros:** `query` con topic o concepto de metodología
- **Cuando usar:** En S-CONSULT para responder preguntas metodológicas. En S-ASSESS/S-PLAN para consultar heurísticas.
- **Cuando NO usar:** Para detalles de implementación (eso es trabajo del obrero)
- **Descripción funcional:** Busca en KB agentic-engineering-praxis y recursos relacionados
- **Notas:** Complementa razonamiento; no reemplaza output final

## read_codebase

- **Firma:** `paths: string[] -> FileContent[]`
- **Parámetros:** `paths` con rutas de archivos a leer del repo target
- **Cuando usar:** En S-ASSESS para evaluar blast radius. En S-VERIFY para revisar arquitectura.
- **Cuando NO usar:** Para escribir código (obreros hacen eso). Para leer todo el repo (ser selectivo).
- **Descripción funcional:** Lee archivos específicos del repositorio target para contexto
- **Notas:** Selectividad es clave — context hygiene. Leer solo lo necesario para la decisión.

## review_diff

- **Firma:** `worker_id: string -> DiffContent`
- **Parámetros:** `worker_id` del obrero cuyo diff se quiere revisar
- **Cuando usar:** En S-VERIFY para validar coherencia arquitectónica del output del obrero
- **Cuando NO usar:** Para review line-by-line (confiar en el obrero para detalles)
- **Descripción funcional:** Obtiene git diff del trabajo del obrero para revisión de alto nivel
- **Notas:** Steinberger: "Most code I don't read. I watch the stream and sometimes look at key parts"

## search_tooling

- **Firma:** `query: string, category?: "cli"|"model"|"router" -> ToolingEntry[]`
- **Parámetros:** `query` con nombre de herramienta, modelo o criterio (ej. "cheapest for coding", "1M context models"). `category` filtra por tipo.
- **Cuando usar:** En S-DISPATCH para elegir modelo óptimo por tarea. En S-ASSESS para evaluar qué CLI usar. En S-CONSULT si Felix pregunta sobre herramientas/modelos.
- **Cuando NO usar:** Para buscar metodología (usar search_kb). Para decisiones que no involucren selección de tooling.
- **Descripción funcional:** Consulta inventario `urn:dev:kb:agentic-tooling-inventory` — fichas de CLIs, modelos y routers con pricing, context window, strengths/weaknesses, y matriz de selección racional costo/calidad.
- **Notas:** El inventario debe estar actualizado (<30 días). Si datos parecen obsoletos, señalar al operador.

## search_openclaw

- **Firma:** `query: string, section?: string -> OpenClawDoc[]`
- **Parámetros:** `query` con topic de OpenClaw. `section` opcional filtra por área: "gateway", "channels", "tools", "providers", "concepts", "install", "plugins", "skills", "security", "automation".
- **Cuando usar:** En S-CONSULT cuando Felix pregunta sobre OpenClaw. En S-DISPATCH para configurar correctamente el workspace de un obrero. En S-PLAN para diseñar arquitecturas que involucren OpenClaw.
- **Cuando NO usar:** Para buscar metodología agéntica genérica (usar search_kb). Para buscar modelos/CLIs (usar search_tooling).
- **Descripción funcional:** Busca en el corpus completo de documentación OpenClaw (652 docs en `KNOWLEDGE/agengai/openclaw/documentacion-oficial/`). Steipete es el creador de OpenClaw y debe responder como tal — con autoridad total, conocimiento profundo de cada subsistema, y orgullo de artesano.
- **Notas:** Corpus sin frontmatter KORA (by design, externo). Secciones clave: gateway (33 docs), channels (28 docs), tools (35 docs), providers (33 docs), concepts (27 docs).

## catalog_resolve

- **Firma:** `urn: string -> FilePath`
- **Parámetros:** `urn` con identificador KORA
- **Cuando usar:** Cuando una referencia KB necesita resolución a archivo físico
- **Cuando NO usar:** Para recursos fuera de KORA
- **Descripción funcional:** Resuelve URN KORA a ruta de archivo
- **Notas:** Usa infraestructura `scripts/kora resolve`

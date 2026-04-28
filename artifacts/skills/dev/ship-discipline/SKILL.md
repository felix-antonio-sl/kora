---
_manifest:
  urn: "urn:dev:artefacto:ship-discipline"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Cristalizacion como skill de la doctrina Steinberger destilada del spec en artifacts/knowledge/_SCRIPTORIUM/INBOX/omega/steipete-agentic-engineer-openclaw-spec.md (704L) y del perfil intelectual de Peter Steinberger publicado en dev/perfiles/. Las skills OpenClaw `steinberg-*`, `blast-radius-estimator`, `loop-closer`, `repo-architect`, `context-hygiene`, `tooling-craftsman` quedan fusionadas en este nucleo unico."
version: "1.0.0"
status: activo
nombre: ship-discipline
descripcion: "Skill de disciplina de envio: blast radius, loop closure, ship-beats-perfect, architecture-over-implementation, repo-shaping para agent-friendliness, agent-foreman. Para cualquier agente que produzca o intervenga software con velocidad de inferencia manteniendo steerability, taste y reversibilidad."
tags: [ship, blast-radius, loop-closure, agentic-engineering, repo-shaping, steinberger, just-talk-to-it, taste]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2, 1, 3, 2, 1]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex, gemini, mastra, openclaw]
    nivel_prescripcion: alto
    conocimiento_permitido:
      - "urn:dev:kb:peter-steinberger-ingeniero-agentico-prodigio"
    componible_con:
      - "urn:kora:artefacto:mente-omega"
      - "urn:kora:artefacto:cat-thinking"
      - "urn:kora:artefacto:artifact-curator"
      - "urn:kora:artefacto:kora-skills"
      - "urn:kora:artefacto:kora-agents"
artefacto:
  perfil:
    dominio:
      - estimacion-de-blast-radius
      - cierre-de-loop
      - shaping-de-repos-para-agentes
      - architecture-over-implementation
      - context-hygiene
      - tooling-craftsmanship
      - agent-foreman
    disparadores:
      - "el agente debe modificar codigo y se necesita decidir topologia y nivel de cuidado"
      - "una tarea cambia archivos y debe cerrar el loop antes de declararse hecha"
      - "se va a estructurar un repositorio para que sea agent-friendly"
      - "hay que distinguir lo que delegar a agentes y lo irreducible humano (taste, arquitectura, schema, deps)"
      - "se va a producir CLI, MCP o tooling reusable y sube el rigor"
      - "el contexto del modelo se esta ensuciando y hay que podar"
    salidas:
      - "estimacion de blast radius con topologia recomendada"
      - "loop cerrado: build + test + lint + integracion + commit atomico"
      - "repo agent-friendly conforme al checklist"
      - "decision delegacion humano/agente declarada"
      - "context hygiene aplicada"
  plan:
    estado_inicial: triaje
    estado_terminal: cierre
    estados:
      - triaje
      - estimar-blast-radius
      - decidir-topologia
      - ejecutar-o-delegar
      - cerrar-loop
      - cierre
  interfaz:
    herramientas: [Read, Write, Edit, Glob, Grep, Bash]
    permisos: "Lectura/escritura sobre el repositorio target; ejecucion de build, test, lint, git via Bash."
    protocolos:
      entrada: "intent del operador sobre cambio de codigo + contexto del repo"
      salida: "blast radius estimado + topologia + cambio aplicado + loop cerrado + commit"
  invariantes:
    reglas_duras:
      - "Estimar blast radius ANTES de ejecutar: cuantos archivos toca, cuanto cuesta revertir, puedo cerrar el loop solo, el contexto ayuda o ensucia."
      - "Loop closure: nada esta hecho hasta que compila + tests pasan + se integra + commit atomico. Sin excepciones."
      - "Ship beats perfect: software util hoy > plan ideal hipotetico. La perfeccion ceremonial es enemiga del envio."
      - "Architecture over implementation: invertir tiempo del humano en dependencias, schema, boundaries; delegar implementacion."
      - "Less is more: cada capa, wrapper, MCP permanente, subagente debe justificar existencia. Cortar lo ceremonial."
      - "Just talk to it: prompts cortos, directos, en lenguaje natural. Sin teatro verbal."
      - "Context cost: todo lo que entra al contexto compite por atencion. Poda, resume, simplifica."
      - "Lo irreducible humano no se delega: taste, product judgement, architecture, dependency choice, schema evolution, software feel, frontera entre suficiente y mal hecho."
      - "Cuando subes a CLI/MCP/tooling reusable, sube tambien el rigor: defaults, versionado, errores recuperables, logging, help, tests, release."
      - "La skill NO escribe codigo de dominio: aporta disciplina y arquitectura de la actividad. El conocimiento del campo lo aporta el agente o el humano."
---

# ship-discipline

## Proposito

Skill de **disciplina de envio agentic-engineering**. Da al agente
invocador la capacidad de mover ideas a software con velocidad de
inferencia preservando **steerability**, **loop closure**, **blast
radius** controlado, **taste** y **reversibilidad**.

Doctrina destilada de Peter Steinberger: ingeniero de producto
aumentado por enjambres de agentes — no programador que usa IA. El
software se descubre construyendolo en vivo, con agentes como mano de
obra cognitiva y el humano como sistema de direccion, gusto y
correccion.

## Cuando Usar

- el agente va a modificar codigo y se necesita decidir topologia
  (secuencial cuidadoso, paralelo moderado, maximo paralelismo).
- una tarea cambia archivos y antes de declararla hecha debe cerrar el
  loop (build + test + lint + integracion + commit).
- se va a estructurar un repositorio para que sea agent-friendly o se
  detecta que un repo existente penaliza a los agentes.
- hay que distinguir lo que delegar a agentes vs lo irreducible humano.
- se va a producir CLI, MCP o tooling reusable: sube el rigor.
- el contexto del modelo se esta ensuciando y hay que podar.

## Cuando NO Usar

- razonamiento estructural-discursivo abstracto → usar
  `urn:kora:artefacto:mente-omega`.
- enmarque categorial puro → usar `urn:kora:artefacto:cat-thinking`.
- ciclo de vida de artefactos KORA → usar
  `urn:kora:artefacto:artifact-curator` y sus hermanas.
- diseno de celulas humano-agente organizacionales → usar
  `urn:fxsl:artefacto:cell-design`.

## Workflow

### `triaje`

Tres preguntas guia:

1. **Hay codigo a producir/modificar?** Si no, declinar la skill.
2. **Cuanto sabe el operador del cambio?** (idea borrosa vs requerimiento concreto vs spec completa)
3. **Que tipo de cambio es?** (feature, refactor, fix, cleanup, tooling reusable)

### `estimar-blast-radius`

Antes de ejecutar cualquier cambio no trivial:

1. Identificar archivos directos e indirectos tocados.
2. Clasificar:

| Nivel | Criterio | Ruta |
|---|---|---|
| **Bajo** | 1-3 archivos, reversible, sin deps cruzadas | Ejecutar directo |
| **Medio** | 4-10 archivos, reversible, algunas deps | Tests + commit atomico |
| **Alto** | 10+ archivos, potencialmente irreversible, multiples deps | Plan antes de ejecutar + validacion humana |

3. Documentar la estimacion en una linea antes de actuar.

**Defaults**:
- Ante duda, estimar hacia arriba.
- Schema, dependencias, boundaries → siempre alto.
- Estilo, formatting, docs → siempre bajo.

Detalle en `referencias/blast-radius-checklist.md`.

### `decidir-topologia`

| Tipo de trabajo | Topologia |
|---|---|
| Feature principal con riesgo medio | 1-2 acciones secuenciales |
| Cleanup, tests, UI, satelite | Paralelo moderado |
| Refactor pesado o cambios con alto conflicto | Secuencial cuidadoso |
| Multiples features independientes | Maximo paralelismo |

### `ejecutar-o-delegar`

**Lo irreducible humano** (no delegar a agentes ejecutores):

- system design, distributed systems, dependencias, boundaries
- DB schema, server/client split
- UX feel, naming, seleccion de plataforma
- product judgement, taste, frontera "suficiente vs mal hecho"

**Lo delegable** (a agentes ejecutores via exec/codigo):

- escribir, transformar, mover, refactorizar
- generar, probar, repetir hasta verde
- shaping mecanico de codigo

Detalle en `referencias/separacion-estratos.md`.

### `cerrar-loop`

Una tarea **NO** esta lista hasta que:

1. **Build** — compila/transpila. Si falla, corregir antes de seguir.
2. **Test** — tests relevantes pasan. Si no hay y el cambio es no
   trivial, escribirlos.
3. **Lint** — corregir warnings criticos.
4. **Integracion** — sin romper imports, tipos, deps existentes.
5. **Feel** — la solucion se siente correcta al usarla.
6. **Commit atomico** — un cambio = un commit, mensaje descriptivo.

Detalle en `referencias/loop-closure-checklist.md`.

### `cierre`

Reportar:

- blast radius estimado y topologia elegida,
- cambio aplicado con paths,
- loop cerrado (build/test/lint/integracion verde),
- commit hash o referencia,
- siguiente paso si la tarea es multi-incremento.

## Reglas Duras

1. **Blast radius antes de exec**.
2. **Loop closure obligatorio**: build + test + lint + integracion +
   commit atomico.
3. **Ship beats perfect**: util hoy > ideal hipotetico.
4. **Architecture over implementation**: humano en deps/schema/boundaries.
5. **Less is more**: cada capa justifica existencia.
6. **Just talk to it**: prompts cortos, lenguaje natural.
7. **Context cost**: poda lo que no aporta.
8. **Lo irreducible humano no se delega**.
9. **Sube rigor cuando produces tooling reusable** (CLI, MCP, lib).
10. **No invadir dominio**: la skill da disciplina, no semantica del campo.

## Anti-patrones

| Anti-patron | Falla | Correccion |
|---|---|---|
| Prompt charade | Sustituye claridad por teatro | Just talk to it; prompt corto |
| MCP para todo | Costo permanente de contexto | CLI cuando alcanza |
| Worktree mania | Carga cognitiva innecesaria | Trabajar en main si cabe |
| Subagent soup | Empaqueta complejidad manejable | Una sesion |
| Background-first | Pierde steerability | Foreground por defecto |
| Spec completa antes de tocar sistema | No calza con descubrimiento iterativo | Prototipar temprano |
| Leer todo el codigo generado | Desperdicia atencion senior | Mirar puntos de leverage |
| Loop abierto | Tarea declarada hecha sin build/test | Cerrar siempre |

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:mente-omega` | la decision de arquitectura requiere razonamiento estructural-discursivo previo |
| `urn:kora:artefacto:cat-thinking` | la composicion del repo o la integracion entre subsistemas tensiona y se necesita lectura categorial |
| `urn:kora:artefacto:artifact-curator` | el cambio toca artefactos KORA y debe pasar por su ciclo de vida |
| `urn:kora:artefacto:kora-skills` / `kora-agents` | se va a producir un nuevo agente o skill KORA |

## Recursos

### Referencias

- `referencias/blast-radius-checklist.md` — checklist de estimacion +
  defaults + criterios.
- `referencias/loop-closure-checklist.md` — pasos del loop, gotchas y
  reglas.
- `referencias/repo-shaping-checklist.md` — checklist agent-friendly:
  estructura, naming, docs, CLI, ejemplos.
- `referencias/separacion-estratos.md` — humano-vs-agente: que delegar
  y que no, con criterios.

## Salida Esperada

- diagnostico de tarea + tipo de cambio,
- blast radius estimado con topologia,
- decision de delegacion humano/agente declarada,
- cambio aplicado,
- loop cerrado con evidencia (build verde, tests verdes, commit),
- siguiente paso operativo.

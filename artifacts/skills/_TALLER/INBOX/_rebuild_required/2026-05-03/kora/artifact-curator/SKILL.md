---
_manifest:
  urn: "urn:kora:artefacto:artifact-curator"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Cristalizacion como skill del agente curator legacy (retirado el 2026-04-28; URN absorbido). Destila el metodo de ciclo de vida de artefactos KORA bajo el dominio de habilidad de autoria-spec v1.2 y el proceso de agent-skill-construction-spec v1.0. Las dimensiones Mu=2 y Phi=2 del agente legacy quedan en el invocador; la skill aporta la tecnica."
version: "1.0.0"
status: retirado
nombre: Artifact Curator
descripcion: "Conduce el ciclo de vida de cualquier artefacto KORA productivo (knowledge, spec, agente, skill): clasifica intent, korafica, cristaliza, audita, repara, mejora o deprecara preservando fidelidad, SSOT y trazabilidad URN, delegando en las skills hermanas cuando corresponde."
tags: [curator, ciclo-de-vida, koraficacion, cristalizacion, auditoria, reparacion, artefactos]
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
    rebuild:
      required: true
      current_is_source: false
      directive: "urn:kora:kb:meta-kora-rebuild-directive"
    conocimiento_permitido:
      - "urn:kora:kb:gobernanza"
      - "urn:kora:kb:harness-spec"
      - "urn:kora:kb:autoria-spec"
      - "urn:kora:kb:agent-skill-construction-spec"
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
      - "urn:kora:kb:qa-spec"
      - "urn:kora:kb:risk-register-spec"
      - "urn:kora:kb:transmutation-spec"
    componible_con:
      - "urn:kora:artefacto:cat-thinking"
      - "urn:kora:artefacto:curation-conductor"
      - "urn:kora:artefacto:kora-skills"
      - "urn:kora:artefacto:kora-agents"
artefacto:
  perfil:
    dominio:
      - ciclo-de-vida-artefactos
      - koraficacion
      - cristalizacion
      - auditoria
      - reparacion
      - diseno-pre-transmutacion
    disparadores:
      - "el operador pide curar, koraficar, cristalizar, auditar, reparar, mejorar o deprecar un artefacto KORA"
      - "una fuente humana o decision implicita debe convertirse a artefacto KORA conforme a md-spec o autoria-spec"
      - "un artefacto productivo (knowledge, spec, skill, agente) requiere conformidad re-verificada o reparacion minima"
      - "se va a construir una skill o agente nuevo y el flujo necesita gate de autoria-spec + agent-skill-construction-spec"
    salidas:
      - "diagnostico de intent y ruta elegida"
      - "artefacto KORA productivo conforme a la spec gobernante"
      - "reporte de auditoria con severidades y metricas FS/CR cuando aplica"
      - "outcome operativo explicito: ready, needs_repair, processing, rerouted, blocked"
  plan:
    estado_inicial: triaje
    estado_terminal: emitir-outcome
    estados:
      - triaje
      - enmarcar
      - delegar-o-conducir
      - producir
      - auditar
      - emitir-outcome
  interfaz:
    herramientas: [Read, Write, Edit, Glob, Grep, Bash]
    permisos: "Lectura y escritura sobre staging (artifacts/{knowledge,agents,skills}/_*) y ejecucion controlada de toolchain KORA (kora index, check, validate, kb-graph, transmute --dry-run)."
    protocolos:
      entrada: "intent + artefacto target o fuente raw + tipo declarado o derivable + modo (libre o guiado)"
      salida: "ruta elegida, artefacto resultante o handoff a skill hermana, reporte de auditoria, outcome operativo"
  invariantes:
    reglas_duras:
      - "Fidelidad radical: no perder hechos, condiciones, fechas ni cifras de la fuente; declarar perdida cuando ocurra (md-spec §5.5, agent-skill-construction-spec §2.2 ley 4)."
      - "SSOT: un hecho existe en exactamente un lugar del corpus; no duplicar entre artefactos sin relacion explicita."
      - "Trazabilidad URN: toda referencia se declara como URN resoluble, no como path duro (knowledge-spec §4.1, agent-skill-construction-spec §3.4)."
      - "Precedencia: gobernanza > harness > autoria/md/knowledge > runtime > extensiones; si un documento tensiona con la CLI o las specs vigentes, manda la spec."
      - "Nunca publicar directo a productivo: el target inmediato es REVIEW (knowledge-spec §6, autoria-spec §5)."
      - "Jamas eludir la skill hermana especializada: si la ruta es atomic -> atomize; si es KB normal descriptivo -> knowledge-curator; si es flujo end-to-end de knowledge -> curation-conductor."
      - "Construccion de agentes y skills nuevos pasa por agent-skill-construction-spec: requerimientos -> blueprint con vector PMI x LFS -> IR canonico (AGENT.md o SKILL.md), antes de cualquier transmutacion."
      - "Auditoria fallida nunca cierra como ready: el outcome es needs_repair, processing o blocked."
      - "No invade dominio del operador: la skill aporta metodo y diagnostico estructural; la decision editorial final queda en el agente invocador o el humano."
---

# Artifact Curator

## Proposito

Skill de **ciclo de vida de artefactos KORA productivos**. Da al agente
invocador la capacidad de mover un artefacto cualquiera (knowledge, spec,
skill, agente) por las fases de koraficacion, cristalizacion, diseno,
auditoria, reparacion, mejora y deprecacion, sin perder fidelidad, SSOT ni
trazabilidad URN.

No es una skill ejecutora unica: es una skill **conductora generica** que
clasifica el intent, elige ruta, delega en la skill hermana especializada
cuando corresponde, y solo conduce directamente las ramas que ninguna
hermana cubre (cristalizacion de specs, diseno y auditoria de artefactos
agenticos).

Anclaje normativo:

- `urn:kora:kb:gobernanza` — precedencia, regimenes URN, lifecycle.
- `urn:kora:kb:harness-spec` — ontologia PMI x LFS y leyes inter-eje.
- `urn:kora:kb:autoria-spec` — shape unificado de artefactos agenticos.
- `urn:kora:kb:agent-skill-construction-spec` — proceso pre-transmutacion.
- `urn:kora:kb:md-spec` — formato base y perfil prescriptivo de specs.
- `urn:kora:kb:knowledge-spec` — pipeline de knowledge y morfismos.

## Cuando Usar

- el operador pide curar un artefacto KORA y la ruta no esta claramente
  contenida en una skill hermana (atomize, knowledge-curator,
  curation-conductor).
- hay una fuente humana o un conjunto de decisiones implicitas que debe
  convertirse en artefacto KORA productivo (knowledge descriptivo, spec
  prescriptivo, skill o agente conforme a autoria-spec).
- un artefacto productivo necesita auditoria de conformidad,
  reparacion minima, mejora controlada o deprecacion.
- se va a disenar una skill o agente nuevo y se quiere que el flujo
  pase explicitamente por el gate de autoria-spec +
  agent-skill-construction-spec antes de transmutar a runtime.

## Cuando NO Usar

- pipeline knowledge end-to-end ya definido por el operador → usar
  `urn:kora:artefacto:curation-conductor` directamente.
- ruta KB normal descriptiva en `_SCRIPTORIUM/REVIEW` → usar la skill en
  staging `artifacts/skills/_TALLER/INBOX/knowledge-curator/SKILL.md`.
- familia documental `atomic` → usar la skill en staging
  `artifacts/skills/_TALLER/INBOX/atomize/SKILL.md`
  (productor en revalidacion, knowledge-spec §12).
- enmarque categorial profundo previo al diseno → usar
  `urn:kora:artefacto:cat-thinking` y volver con la lectura.
- transmutacion a runtime concreto → la skill prepara el IR; la
  proyeccion la hace `python3 toolchain/kora transmute`.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud combinando el dispatch que aporte la skill en staging
`artifacts/skills/_TALLER/INBOX/intent-classifier/SKILL.md` (cuando este
disponible en el agente invocador) con la tabla local de
`referencias/dispatcher-table.md`.
Producir tres campos minimos:

1. **intent** — uno de: `koraficar`, `cristalizar`, `disenar`, `auditar`,
   `reparar`, `editar`, `mejorar`, `deprecar`, `ambiguo`.
2. **tipo de artefacto** — uno de: `knowledge-descriptivo`,
   `knowledge-atomic`, `spec`, `skill`, `subagente`,
   `agente-propiamente-tal`, `agente-plataforma`, `desconocido`.
3. **modo** — `libre` (ejecutar directo) o `guiado` (consolidar
   checkpoints via la skill en staging
   `artifacts/skills/_TALLER/INBOX/lifecycle-orchestrator/SKILL.md`).

Salida: si el intent o el tipo no se pueden determinar con confianza
suficiente, emitir `outcome: blocked` con clarificacion solicitada y
detener el workflow.

### `enmarcar`

Si el caso involucra arquitectura, composicion no trivial,
delegacion, materia ambiental, dominio nuevo o riesgo no obvio,
ejecutar lectura categorial minima conforme a
`agent-skill-construction-spec §2.3` invocando
`urn:kora:artefacto:cat-thinking`. La salida fija el vector PMI x LFS
candidato y elige la lectura categorial mas debil suficiente.

Para artefactos agenticos nuevos, derivar tambien:

- `atlas.forma_material` desde el dominio de proyeccion (`autoria-spec §5`).
- `atlas.arnes_categorico` desde el vector y la tabla de `harness-spec §5.1`.
- `extensions.kora.conocimiento_permitido` como URNs resolubles
  (`agent-skill-construction-spec §3.4`).

### `delegar-o-conducir`

Decidir, segun la combinacion `(intent, tipo)`, si la ruta corresponde
a una skill hermana o a esta skill:

| Tipo \ Intent | knowledge-descriptivo | knowledge-atomic | spec | skill / agente |
| --- | --- | --- | --- | --- |
| `koraficar` | delegar `knowledge-curator` | delegar `atomize` | conducir aqui (cristalizar) | conducir aqui (disenar) |
| `cristalizar` | conducir aqui | no aplica | conducir aqui | conducir aqui |
| `disenar` | conducir aqui | no aplica | conducir aqui | conducir aqui |
| `auditar` | conducir aqui | conducir aqui (sobre output de atomize) | conducir aqui | conducir aqui |
| `reparar` | delegar `knowledge-curator` o conducir aqui | conducir aqui | conducir aqui | conducir aqui |
| `editar` | conducir aqui | conducir aqui | conducir aqui | conducir aqui |
| `mejorar` | conducir aqui | conducir aqui | conducir aqui | conducir aqui |
| `deprecar` | conducir aqui | conducir aqui | conducir aqui | conducir aqui |

Para flujos knowledge end-to-end con clasificacion de familia abierta,
delegar al `urn:kora:artefacto:curation-conductor`. La delegacion es
una salida valida de la skill: emitir handoff explicito con contrato de
ruta y outcome `rerouted`.

### `producir`

Aplicar el funtor correspondiente al `(intent, tipo)`:

- `koraficar` (descriptivo no-knowledge, ej. nota tecnica de
  workspace agentico): aplicar `md-spec §6` para la transformacion
  `DocHumano → KORA/MD`. Mantener `FS=100%`, apuntar a `CR>1.5`,
  emitir en `_SCRIPTORIUM/REVIEW/` (knowledge) o staging local del
  artefacto consumidor.
- `cristalizar` (spec, perfil prescriptivo): aplicar `md-spec §5.6.2`
  (RFC 2119, `Traces to:` o `Rationale:`, patron
  regla+ejemplo+traza, invariantes prescriptivos). Salida bajo
  `serialization/`, `governance/`, `ontology/` o `runtime/` segun
  competencia, con familia `spec`.
- `disenar` (skill o agente): aplicar `agent-skill-construction-spec`
  fases A→H. Producir el `SKILL.md` o `AGENT.md` en
  `artifacts/skills/_TALLER/REVIEW/{nombre}/` o
  `artifacts/agents/_FRAGUA/REVIEW/{ns}/{nombre}/` con vector,
  forma material, FSM si aplica, conocimiento por URN y reglas
  duras suficientes.
- `editar` / `reparar` / `mejorar`: aplicar fix minimo sin alterar
  identidad URN ni invariantes; preservar trazabilidad. Repair
  conserva URN, familia y forma material salvo cambio explicito de
  diseno.
- `deprecar`: cambiar `status` segun `gobernanza §5` (artefacto
  conceptual: `borrador → publicado → deprecado`; agentico:
  `borrador → activo → deprecado → retirado`). Si emerge un
  reemplazo, apuntar `supersedes` desde el reemplazo. No reactivar
  artefactos retirados.

### `auditar`

Correr conformidad antes de cualquier `ready`. Checks minimos por
familia:

| Familia | Checks aplicables |
| --- | --- |
| knowledge / nota / guide | `md-spec §3.1` envelope, `§5` gramatica, `§5.5` fidelidad, `knowledge-spec §4` relations validas |
| spec | `md-spec §5.6.2` perfil prescriptivo: RFC 2119, `Traces to:` o `Rationale:`, regla+ejemplo+traza, consistencia interna, auto-suficiencia, no-circularidad, enforcement declarado |
| atomic | `md-spec §5.6.1` enum cerrado de tipos, ID `Pxxx` unico, fuentes resolubles, `## Indice de fuentes`, FS=100% sobre cifras y particion semantica |
| skill / subagente / agente / agente-plataforma | `autoria-spec §3-§7` envelope + shape condicional por forma material, `§13` fidelidad-agentskills cuando habilidad, `§5` dominio de proyeccion, `harness-spec §4.1` leyes inter-eje, `§9` checks ontologicos |

Toda construccion agentica nueva ademas pasa el gate del
`agent-skill-construction-spec §5.2` (tabla de checks
`construction-*`).

Para todo cierre, ejecutar:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

Cuando se toco knowledge o relaciones:

```bash
python3 toolchain/kora kb-graph --json --orphans
```

Si la auditoria falla, regresar a `producir` con el hallazgo
delimitado, o emitir `needs_repair` cuando el operador esta en el
loop.

### `emitir-outcome`

Una sola linea de outcome operativo, enum cerrado:

| Outcome | Significado |
| --- | --- |
| `ready` | artefacto valida y se puede promover o transmutar |
| `needs_repair` | artefacto en REVIEW con hallazgos no bloqueantes |
| `processing` | trabajo en curso multi-turno |
| `rerouted` | ruta delegada a skill hermana o pipeline distinto |
| `blocked` | falta input o decision editorial del operador |
| `deprecated` | artefacto deprecado o supersedido emitido |

Adjuntar siempre:

- URN target (resoluble),
- path de la fuente primaria producida o auditada,
- siguiente paso operativo (promote, transmute, repair, esperar
  decision).

## Reglas Duras

1. Fidelidad radical: no perder hechos, condiciones, fechas, cifras ni
   referencias. Cualquier perdida se declara como descarte justificado,
   riesgo o deuda residual.
2. SSOT: un hecho existe en exactamente un lugar; duplicacion solo
   con relacion explicita (`refines`, `cites`).
3. Trazabilidad URN: toda referencia entre artefactos KORA se expresa
   como URN resoluble, nunca como path duro.
4. Precedencia: si una guia, README o doc generado tensiona con la spec
   vigente o con la CLI actual, manda la spec.
5. REVIEW antes que productivo: el target inmediato es siempre staging
   (`_SCRIPTORIUM/REVIEW`, `_TALLER/REVIEW`, `_FRAGUA/REVIEW`).
6. No suplantar a la skill especializada: `atomize` para `atomic`,
   `knowledge-curator` para KB normal descriptivo,
   `curation-conductor` para flujos knowledge end-to-end.
7. Construccion agentica pasa siempre por `autoria-spec` +
   `agent-skill-construction-spec`. No saltar a runtime sin IR canonico
   valido.
8. Auditoria fallida nunca cierra `ready`. Outcomes validos en falla:
   `needs_repair`, `processing`, `blocked`.
9. Cat-thinking se invoca cuando hay riesgo de sobre-formalizacion o
   cuando la composicion es ambigua; usar la lectura categorial mas
   debil suficiente.
10. La skill no aporta semantica de dominio: aporta metodo. La decision
    editorial final queda en el agente invocador o el humano.

## Composicion con otras skills

| Composable con | Cuando |
| --- | --- |
| `intent-classifier` (staging: `artifacts/skills/_TALLER/INBOX/intent-classifier/SKILL.md`) | dispatch inicial cuando el agente invocador tiene taxonomia local de capacidades |
| `lifecycle-orchestrator` (staging: `artifacts/skills/_TALLER/INBOX/lifecycle-orchestrator/SKILL.md`) | modo guiado con checkpoints inter-fase visibles |
| `urn:kora:artefacto:cat-thinking` | enmarque categorial obligatorio para arquitectura, composicion o riesgo no obvio |
| `urn:kora:artefacto:curation-conductor` | flujo knowledge end-to-end con clasificacion abierta de familia |
| `knowledge-curator` (staging: `artifacts/skills/_TALLER/INBOX/knowledge-curator/SKILL.md`) | ruta descriptiva KB normal, draft → REVIEW |
| `atomize` (staging: `artifacts/skills/_TALLER/INBOX/atomize/SKILL.md`) | familia atomic; productor en revalidacion |

## Recursos

### Referencias

- `referencias/dispatcher-table.md` — tabla canonica de despacho
  `(intent, tipo) → ruta`, incluyendo cuando delegar y cuando conducir.
- `referencias/audit-checklist.md` — checks aplicables por familia
  documental y forma material; comandos de toolchain por escenario.

## Salida Esperada

- diagnostico de intent + tipo + modo,
- ruta elegida con razon (delegada a hermana o conducida aqui),
- artefacto resultante en staging conforme a la spec gobernante o
  handoff explicito,
- reporte de auditoria con severidades y, cuando aplica, metricas FS y
  CR,
- outcome operativo (`ready`, `needs_repair`, `processing`, `rerouted`,
  `blocked`, `deprecated`),
- siguiente paso operativo concreto.

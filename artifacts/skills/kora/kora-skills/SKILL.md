---
_manifest:
  urn: "urn:kora:artefacto:kora-skills"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Skill hermana de kora-agents para la rama de habilidad. Especializa el proceso de creacion, mantenimiento, mejora y evolucion de skills KORA bajo el dominio de habilidad de autoria-spec v1.2 y el proceso de agent-skill-construction-spec v1.0."
version: "1.0.0"
status: activo
nombre: kora-skills
descripcion: "Conduce la creacion, mantenimiento, mejora, evolucion y deprecacion de skills KORA (forma_material: habilidad) preservando vector ontologico, dominio de proyeccion, fidelidad agentskills y nivel de prescripcion antes de cualquier transmutacion runtime."
tags: [kora-skills, habilidad, diseno-de-skills, evolucion, autoria-spec, construction-spec, agentskills]
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
      - "urn:kora:kb:gobernanza"
      - "urn:kora:kb:harness-spec"
      - "urn:kora:kb:autoria-spec"
      - "urn:kora:kb:agent-skill-construction-spec"
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
      - "urn:kora:kb:qa-spec"
      - "urn:kora:kb:risk-register-spec"
      - "urn:kora:kb:runtime-spec-md"
      - "urn:kora:kb:transmutation-spec"
      - "urn:kora:kb:claude-code-runtime-extension"
      - "urn:kora:kb:codex-runtime-extension"
      - "urn:kora:kb:gemini-runtime-extension"
      - "urn:kora:kb:mastra-runtime-extension"
      - "urn:kora:kb:agentskills-runtime-extension"
    componible_con:
      - "urn:kora:artefacto:artifact-curator"
      - "urn:kora:artefacto:kora-agents"
      - "urn:kora:artefacto:cat-thinking"
artefacto:
  perfil:
    dominio:
      - diseno-de-skills
      - mantencion-de-skills
      - mejora-de-skills
      - evolucion-de-skills
      - deprecacion-de-skills
      - construccion-pre-transmutacion
    disparadores:
      - "el operador pide crear una skill nueva (forma_material: habilidad)"
      - "una skill productiva requiere mejora, refactor, ajuste de vector o expansion de capacidades portables"
      - "una skill debe evolucionar a subagente (promocion habilidad → subagente)"
      - "una skill debe auditarse contra autoria-spec, harness-spec, fidelidad agentskills.io y nivel de prescripcion"
      - "una skill debe deprecarse o retirarse y se requiere transicion limpia"
    salidas:
      - "SKILL.md conforme a autoria-spec v1.2 en _TALLER/REVIEW o productivo"
      - "blueprint con vector PMI x LFS, nivel_prescripcion, dominio de proyeccion habilidad e interfaz tipada"
      - "plan de evolucion con bumps semver y descartes justificados"
      - "reporte de auditoria con severidades por check de construccion, skill-structure y fidelidad-agentskills"
      - "outcome operativo: ready, needs_repair, processing, blocked, deprecated"
  plan:
    estado_inicial: triaje
    estado_terminal: emitir-outcome
    estados:
      - triaje
      - intake
      - enmarcar
      - disenar
      - materializar
      - auditar
      - emitir-outcome
  interfaz:
    herramientas: [Read, Write, Edit, Glob, Grep, Bash]
    permisos: "Lectura y escritura sobre artifacts/skills/_TALLER/{INBOX,REVIEW}/ y workspaces productivos artifacts/skills/{ns}/{name}/. Ejecucion controlada de toolchain KORA (kora index, check, validate, transmute --target agentskills --dry-run, kb-graph)."
    protocolos:
      entrada: "intent (disenar, mantener, mejorar, evolucionar, auditar, deprecar) + skill target o requerimientos + nivel_prescripcion declarado o derivable + modo (libre o guiado)"
      salida: "SKILL.md productivo o draft, reporte de auditoria, plan de evolucion cuando aplica, outcome operativo, siguiente paso para transmute o promote"
  invariantes:
    reglas_duras:
      - "Construir IR canonico primero: Req → Blueprint → IR (SKILL.md) antes de cualquier transmutacion (agent-skill-construction-spec §1, §2.2 ley 5)."
      - "El vector ontologico debe caer dentro del dominio de habilidad (Π∈{1,2}, Μ∈{0,1}, Ξ∈{1,2}, Λ=0, Φ=1) y respetar las leyes inter-eje (harness-spec §4.1, autoria-spec §5.1)."
      - "`nivel_prescripcion` (alto, medio, bajo) es obligatorio y se elige segun el grado de prescriptividad operacional de la skill."
      - "Body ≤ 500 lineas; detalle voluminoso pasa a `referencias/` (progressive disclosure)."
      - "Subdirs canonicos exclusivos: `scripts/`, `referencias/`, `recursos/`. Cualquier otro subdir es invalido en `status: activo`."
      - "Si hay subdirs, body debe declarar seccion `## Recursos`."
      - "Conocimiento gobernado se declara por URN resoluble en `extensions.kora.conocimiento_permitido`, no por path duro."
      - "La skill debe ser proyectable byte-identical a paquete agentskills.io conforme autoria-spec §5.5: `kora transmute --target agentskills --dry-run` no puede emitir perdida estructural."
      - "Promocion entre formas (habilidad → subagente) preserva URN, bumpea version major, expande shape y reorganiza topologia (autoria-spec §8). La democion esta prohibida."
      - "El target inmediato es REVIEW (artifacts/skills/_TALLER/REVIEW/{nombre}/), no productivo."
      - "Cualquier elemento de Req que no entre en IR queda como descarte justificado, riesgo o deuda residual; nunca silenciado."
      - "Auditoria fallida no cierra como ready: outcomes validos en falla son `needs_repair`, `processing` o `blocked`."
      - "La skill no aporta semantica de dominio: aporta metodo y diagnostico estructural; la decision editorial queda en el agente invocador o el humano."
---

# kora-skills

## Proposito

Skill de **construccion y evolucion de skills KORA**. Da al agente
invocador la capacidad de crear, mantener, mejorar, evolucionar, auditar
y deprecar artefactos agenticos productivos cuya forma material es
`habilidad`, conforme estricto a `autoria-spec v1.2` y
`agent-skill-construction-spec v1.0`, preservando ademas la fidelidad
de proyeccion al estandar externo agentskills.io.

Es la rama hermana de `urn:kora:artefacto:kora-agents`: ambas comparten
metodo (fases A→H del construction-spec) pero se diferencian en el
dominio de proyeccion, los checks aplicables y la topologia de
materializacion. Para `habilidad` esta skill conduce; para
`subagente`, `agente-propiamente-tal` o `agente-plataforma` la rama es
`kora-agents`.

Anclaje normativo:

- `urn:kora:kb:gobernanza` — precedencia, regimenes URN, lifecycle.
- `urn:kora:kb:harness-spec` — ontologia PMI x LFS, leyes inter-eje,
  matriz de realizabilidad.
- `urn:kora:kb:autoria-spec` — shape unificado, dominio de habilidad,
  proyeccion fiel a agentskills.io, validacion condicional.
- `urn:kora:kb:agent-skill-construction-spec` — fases A→H del metodo
  pre-transmutacion.
- `urn:kora:kb:md-spec` — formato base KORA/MD.
- `urn:kora:kb:knowledge-spec` — URNs de conocimiento permitido.
- `urn:kora:kb:qa-spec`, `urn:kora:kb:risk-register-spec` — quality
  attributes y riesgo cuando aplica.
- `urn:kora:kb:transmutation-spec`, `urn:kora:kb:runtime-spec-md` y
  runtime-extensions — leyes de proyeccion runtime.
- `urn:kora:kb:agentskills-runtime-extension` — encaje canonico hacia
  agentskills.io (proyeccion fiel byte-identical).

## Cuando Usar

- diseno de una skill nueva (`forma_material: habilidad`) desde
  requerimientos.
- mantencion: refactor del workflow, ajuste de vector ontologico,
  expansion de `conocimiento_permitido`, normalizacion de invariantes.
- mejora: comprimir grasa del body para entrar en ≤500 lineas, alinear
  con bump de spec gobernante, ajustar `nivel_prescripcion`,
  reorganizar `referencias/` o `recursos/`.
- evolucion: promocion `habilidad → subagente` conforme a
  `autoria-spec §8.1` (handoff a `kora-agents`).
- auditoria contra `autoria-spec`, `harness-spec`, `skill-structure` y
  `fidelidad-agentskills`.
- deprecacion o retiro de una skill con transicion limpia y, cuando
  aplica, emision de un reemplazo con `supersedes`.

## Cuando NO Usar

- creacion o evolucion de agentes (`subagente`,
  `agente-propiamente-tal`, `agente-plataforma`) → usar
  `urn:kora:artefacto:kora-agents`.
- ciclo de vida de artefactos de conocimiento (`note`, `guide`,
  `atomic`, `spec`) → usar `urn:kora:artefacto:artifact-curator` o sus
  hermanas (`knowledge-curator`, `atomize`, `curation-conductor`).
- transmutacion concreta a runtime → la skill prepara y verifica el IR;
  la proyeccion la hace `python3 toolchain/kora transmute`.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud combinando, cuando esta disponible, la salida de la
skill en staging `artifacts/skills/_TALLER/INBOX/intent-classifier/SKILL.md`
con la tabla local de `referencias/dispatcher-table.md`. Producir tres campos:

1. **intent** — uno de: `disenar`, `mantener`, `mejorar`,
   `evolucionar`, `auditar`, `deprecar`, `ambiguo`.
2. **forma material target** — `habilidad`. Si el operador pide
   `subagente`, `agente-propiamente-tal` o `agente-plataforma`,
   devolver handoff a `kora-agents` con outcome `rerouted`.
3. **modo** — `libre` (ejecutar directo) o `guiado` (consolidar
   checkpoints via la skill en staging
   `artifacts/skills/_TALLER/INBOX/lifecycle-orchestrator/SKILL.md`).

Si la combinacion es ambigua, emitir `outcome: blocked` con
clarificacion solicitada y detener el workflow.

### `intake`

Capturar requerimientos conforme a `agent-skill-construction-spec §3.1`:

| Campo | Pregunta | Salida en IR |
| --- | --- | --- |
| identidad | que rol cumple y para quien | `perfil.dominio`, `descripcion`, `tags` |
| objetivo | que resultado observable entrega | `perfil.salidas`, `plan.estado_terminal` |
| nivel_prescripcion | que tan prescriptiva es la skill | `extensions.kora.nivel_prescripcion` (alto, medio, bajo) |
| conocimiento | que URNs puede consultar | `conocimiento_permitido` |
| interaccion | que entradas, herramientas, permisos | `interfaz` |
| portabilidad | que runtimes la van a invocar | `entornos_objetivo` |
| riesgo | que puede salir mal y como se mitiga | `invariantes`, `qa_budget`, `risk_register` |

Campos no aplicables se omiten o declaran vacios; **nunca** placeholder
decorativo.

### `enmarcar`

Aplicar lectura categorial minima conforme a
`agent-skill-construction-spec §2.3` invocando
`urn:kora:artefacto:cat-thinking` cuando el caso involucra composicion,
delegacion implicita, riesgo no obvio o ambiguedad estructural.

Derivar el vector PMI x LFS dentro del dominio de habilidad
(`autoria-spec §5.1`):

| Eje | Rango habilidad | Lectura |
| --- | --- | --- |
| Π | {1, 2} | plan ejecutable, sin recursion (Π=3 prohibido) |
| Μ | {0, 1} | sin memoria persistente; scratchpad efimero permitido |
| Ξ | {1, 2} | invocacion atomica o lente bidireccional |
| Λ | 0 | individual |
| Φ | 1 | instrumental — supertool |
| Σ | [v1..v5] | compromisos eticos enriched |

Verificar las 5 leyes inter-eje (`harness-spec §4.1`) antes de fijar el
vector. Si el dominio de habilidad no alcanza, considerar promocion a
subagente (handoff a `kora-agents`).

### `disenar`

Producir el blueprint conforme a `agent-skill-construction-spec §3.3-3.7`:

1. **Atlas**: `forma_material: habilidad`. Derivar
   `arnes_categorico` (autoria-spec §4.2): tipicamente `utilidad`,
   `disciplina` o `delegado` cuando se invoca por otro artefacto.
   `metafora_relacional`: tipicamente `supertool`.

2. **Nivel de prescripcion**: obligatorio (autoria-spec §3.2):

   | Nivel | Cuando usar |
   | --- | --- |
   | `alto` | la skill prescribe metodo riguroso (ej. atomize, knowledge-curator) |
   | `medio` | la skill organiza metodo pero acepta variacion del invocador |
   | `bajo` | la skill ofrece capacidad portable opcional |

3. **Contrato de conocimiento**: `conocimiento_permitido` con URNs
   resolubles, no paths duros (`agent-skill-construction-spec §3.4`).

4. **Workflow**: cuando hay ramificacion real, modelar el plan como
   FSM (estados, terminales, transiciones); cuando es lineal,
   describirlo como secuencia. `verificacion_coalgebraica: true` solo
   si realmente se requiere termination check.

5. **Interfaz**: declarar herramientas, permisos, entradas y salidas.
   Las herramientas tipicas para skills: `[Read, Grep, Glob]` para
   skills introspectivas; `[Read, Write, Edit, Glob, Grep, Bash]` para
   skills productoras. Declarar `api_observable` cuando la skill se
   compone con otras (`autoria-spec §3.5.1`).

6. **Invariantes**: reglas duras suficientes; `compromisos_eticos`
   opcionales en habilidad (no obligatorios). `qa_budget` y
   `risk_register` cuando el riesgo no es trivial.

### `materializar`

Escribir el archivo fuente conforme a `autoria-spec §5.1`:

```
artifacts/skills/{nombre}/                 # top-level sin namespace
  SKILL.md                                  # obligatorio
  scripts/                                  # opcional, automatizacion determinista
  referencias/                              # opcional, documentacion lazy-load
  recursos/                                 # opcional, plantillas de salida
```

O con namespace:

```
artifacts/skills/{namespace}/{nombre}/
  SKILL.md
  scripts/
  referencias/
  recursos/
```

Reglas:

- Body ≤ 500 lineas (progressive disclosure).
- Si hay subdirs, body debe tener seccion `## Recursos` declarando
  cada subdir.
- Subdirs canonicos exclusivos: `scripts/`, `referencias/`,
  `recursos/`. Cualquier otro subdir es invalido en `status: activo`.

Ubicacion canonica para skills nuevas:
`artifacts/skills/_TALLER/REVIEW/{nombre}/`. Promocion a productivo
via gate strict y procedimiento revisado.

### `auditar`

Aplicar checks especificos de habilidad (`autoria-spec §6, §14` +
`agent-skill-construction-spec §5.2`):

| Check | Aplicabilidad |
| --- | --- |
| `envelope-valido`, `manifest-type-artefacto`, `vector-ontologico-presente` | universal |
| `vector-rango-valido`, `leyes-inter-eje` | universal |
| `forma-material-declarada` | universal |
| `dominio-forma-material` | dominio Π∈{1,2}, Μ∈{0,1}, Ξ∈{1,2}, Λ=0, Φ=1 |
| `arnes-compatible-con-forma` | (utilidad, disciplina, delegado) |
| `shape-condicional` | universal |
| `topologia-valida` | `artifacts/skills/{nombre}` o `{ns}/{nombre}` |
| `progressive-disclosure` | body ≤ 500 lineas |
| `recursos-documentados` | si hay subdirs, body declara `## Recursos` |
| `skill-structure` | subdirs canonicos exclusivos |
| `fidelidad-agentskills` | `kora transmute --target agentskills --dry-run` byte-identical |
| `entornos-objetivo-soportan` | cada runtime acepta `(arnes, habilidad)` |
| `referencias-resolubles` | URNs en `componible_con`, `conocimiento_permitido` resuelven |
| `construction-source-primary`, `construction-vector-fit`, `construction-knowledge-explicit`, `construction-fsm-valid`, `construction-interface-typed`, `construction-risk-declared`, `construction-runtime-separation`, `construction-categorical-minimality`, `construction-authoring-shape` | construccion nueva |

Comandos:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 toolchain/kora transmute --target agentskills --agent kora/{nombre} --dry-run
python3 toolchain/kora kb-graph --json --orphans
```

Si `fidelidad-agentskills` falla, regresar a `disenar` o
`materializar` con el hallazgo acotado: la skill no cumple el contrato
de interop con el estandar externo. Para checks de construccion,
regresar a la fase correspondiente.

### `emitir-outcome`

Outcome operativo, enum cerrado:

| Outcome | Significado |
| --- | --- |
| `ready` | skill cumple gates; se puede promover o transmutar |
| `needs_repair` | skill en REVIEW con hallazgos no bloqueantes |
| `processing` | trabajo en curso multi-turno |
| `rerouted` | ruta delegada (forma material no es habilidad → kora-agents; familia knowledge → artifact-curator) |
| `blocked` | falta requerimiento o decision editorial del operador |
| `deprecated` | skill deprecada o supersedida emitida |

Adjuntar siempre:

- URN target,
- path de la fuente primaria producida o auditada,
- siguiente paso operativo (promote, transmute, repair, esperar
  decision).

## Reglas Duras

1. IR primero: `Req → Blueprint → IR (SKILL.md)` antes de cualquier
   transmutacion. La construccion no salta a runtime.
2. Vector dentro del dominio de habilidad y respetando leyes inter-eje;
   si el dominio no alcanza, considerar promocion a subagente.
3. `nivel_prescripcion` obligatorio (alto, medio, bajo); no se puede
   omitir.
4. Body ≤ 500 lineas; comprimir grasa o mover detalle a `referencias/`.
5. Subdirs canonicos exclusivos: `scripts/`, `referencias/`,
   `recursos/`. Cualquier otro subdir es invalido en `status: activo`.
6. Si hay subdirs, body declara `## Recursos` con cada subdir.
7. Conocimiento por URN resoluble, jamas por path duro.
8. Fidelidad agentskills: la skill se transmuta byte-identical a
   paquete agentskills.io sin perdida estructural; si falla, es bug.
9. Promocion `habilidad → subagente` preserva URN, bumpea major y
   reorganiza topologia (handoff a `kora-agents` para conducir la
   rama agente). Democion prohibida.
10. REVIEW antes que productivo.
11. Cualquier elemento de Req que no entre en IR queda como descarte
    justificado, riesgo o deuda residual.
12. Auditoria fallida nunca cierra `ready`. Outcomes validos en falla:
    `needs_repair`, `processing`, `blocked`.

## Composicion con otras skills

| Composable con | Cuando |
| --- | --- |
| `urn:kora:artefacto:artifact-curator` | el operador entra por el ciclo de vida general; kora-skills recibe handoff cuando la forma material es habilidad |
| `urn:kora:artefacto:kora-agents` | rama hermana para `subagente`, `agente-propiamente-tal`, `agente-plataforma`; recibe handoff en evolucion `habilidad → subagente` |
| `intent-classifier` (staging: `artifacts/skills/_TALLER/INBOX/intent-classifier/SKILL.md`) | dispatch inicial cuando el agente invocador tiene taxonomia local de capacidades |
| `lifecycle-orchestrator` (staging: `artifacts/skills/_TALLER/INBOX/lifecycle-orchestrator/SKILL.md`) | modo guiado con checkpoints inter-fase visibles |
| `urn:kora:artefacto:cat-thinking` | enmarque categorial cuando hay composicion implicita o ambiguedad estructural |

## Recursos

### Referencias

- `referencias/dispatcher-table.md` — tabla canonica de despacho
  `(intent × situacion) → ruta`, incluyendo cuando delegar a hermanas
  y cuando conducir.
- `referencias/blueprint-checklist.md` — checks de construccion por
  fase A→H aplicados a habilidad; tabla rapida de dominios y leyes
  inter-eje; matriz de fidelidad agentskills.

## Salida Esperada

- diagnostico de intent + nivel_prescripcion + modo,
- blueprint con vector PMI x LFS, atlas, workflow y contrato de
  conocimiento,
- SKILL.md productivo o draft en staging,
- reporte de auditoria con severidades y comandos toolchain ejecutados,
- outcome operativo (`ready`, `needs_repair`, `processing`, `rerouted`,
  `blocked`, `deprecated`),
- siguiente paso operativo concreto.

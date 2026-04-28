---
_manifest:
  urn: "urn:kora:artefacto:kora-agents"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Cristalizacion como skill del agente forgemaster legacy v2.0.0. Especializa el proceso de creacion, mantenimiento, mejora y evolucion de agentes KORA (subagente, agente-propiamente-tal, agente-plataforma) bajo el dominio de habilidad de autoria-spec v1.2 y el proceso de agent-skill-construction-spec v1.0. La memoria persistente y el acoplamiento colaborativo del agente legacy quedan en el invocador; la skill aporta el metodo."
version: "1.0.0"
status: activo
nombre: kora-agents
descripcion: "Conduce la creacion, mantenimiento, mejora, evolucion y deprecacion de agentes KORA (forma_material: subagente, agente-propiamente-tal, agente-plataforma) preservando vector ontologico, dominio de proyeccion, FSM coalgebraica y compromisos eticos antes de cualquier transmutacion runtime."
tags: [forgemaster, agentes, diseno-agentico, coalgebra, evolucion, autoria-spec, construction-spec]
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
      - "urn:kora:kb:multiagente-spec"
      - "urn:kora:kb:runtime-spec-md"
      - "urn:kora:kb:transmutation-spec"
      - "urn:kora:kb:claude-code-runtime-extension"
      - "urn:kora:kb:codex-runtime-extension"
      - "urn:kora:kb:gemini-runtime-extension"
      - "urn:kora:kb:mastra-runtime-extension"
      - "urn:agengai:kb:openclaw-runtime-extension"
    componible_con:
      - "urn:kora:artefacto:artifact-curator"
      - "urn:kora:artefacto:kora-skills"
      - "urn:kora:artefacto:cat-thinking"
      - "urn:kora:artefacto:intent-classifier"
      - "urn:kora:artefacto:lifecycle-orchestrator"
artefacto:
  perfil:
    dominio:
      - diseno-de-agentes
      - mantencion-de-agentes
      - mejora-de-agentes
      - evolucion-de-agentes
      - deprecacion-de-agentes
      - construccion-pre-transmutacion
    disparadores:
      - "el operador pide crear un agente nuevo (subagente, agente-propiamente-tal o agente-plataforma)"
      - "un agente productivo requiere mejora, refactor de FSM, ajuste de vector o expansion de capacidades"
      - "un agente debe evolucionar entre formas materiales (promocion habilidad → subagente → agente-propiamente-tal → agente-plataforma)"
      - "un agente debe auditarse contra autoria-spec, harness-spec o la matriz de realizabilidad runtime"
      - "un agente debe deprecarse o retirarse y se requiere transicion limpia"
    salidas:
      - "AGENT.md conforme a autoria-spec v1.2 en _FRAGUA/REVIEW o productivo"
      - "blueprint con vector PMI x LFS, atlas, FSM coalgebraica e interfaz tipada"
      - "plan de evolucion con bumps semver y descartes justificados"
      - "reporte de auditoria con severidades por check de construccion"
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
    permisos: "Lectura y escritura sobre artifacts/agents/_FRAGUA/{INBOX,REVIEW}/ y workspaces productivos artifacts/agents/{ns}/{name}/. Ejecucion controlada de toolchain KORA (kora index, check, validate, kb-graph, transmute --dry-run, roundtrip-check)."
    protocolos:
      entrada: "intent (disenar, mantener, mejorar, evolucionar, auditar, deprecar) + workspace target o requerimientos + tipo de forma material declarado o derivable + modo (libre o guiado)"
      salida: "AGENT.md productivo o draft, reporte de auditoria, plan de evolucion cuando aplica, outcome operativo, siguiente paso para transmute o promote"
  invariantes:
    reglas_duras:
      - "Construir IR canonico primero: Req → Blueprint → IR (AGENT.md) antes de cualquier transmutacion (agent-skill-construction-spec §1, §2.2 ley 5)."
      - "El vector ontologico debe caer dentro del dominio de proyeccion de la forma material declarada (autoria-spec §5.2-5.4) y respetar las leyes inter-eje (harness-spec §4.1)."
      - "Toda promocion entre formas materiales preserva el URN, bumpea version major, expande el shape y reorganiza la topologia (autoria-spec §8). La democion esta prohibida."
      - "Conocimiento gobernado se declara por URN resoluble en `extensions.kora.conocimiento_permitido`, no por path duro (agent-skill-construction-spec §3.4)."
      - "Cuando `extensions.kora.verificacion_coalgebraica: true`, declarar `artefacto.plan.fsm` valido (estados, terminales, transiciones, sub-coalgebra de safety cerrada) conforme a autoria-spec §3.5."
      - "Compromisos eticos obligatorios en agente-propiamente-tal y agente-plataforma (autoria-spec §6); risk_register declarado cuando el riesgo no es trivial (agent-skill-construction-spec §3.7)."
      - "Agente-plataforma exige un runtime que soporte Mu=3 (hoy solo openclaw); declararlo en `entornos_objetivo` y `extensions.{plataforma}` (autoria-spec §5.4, openclaw-runtime-extension)."
      - "El target inmediato es REVIEW (artifacts/agents/_FRAGUA/REVIEW/{ns}/{nombre}/), no productivo."
      - "Cualquier elemento de Req que no entre en IR queda como descarte justificado, riesgo o deuda residual; nunca silenciado (agent-skill-construction-spec §2.2 ley 4)."
      - "Auditoria fallida no cierra como ready: outcomes validos en falla son `needs_repair`, `processing` o `blocked`."
      - "La skill no aporta semantica de dominio: aporta metodo y diagnostico estructural; la decision editorial queda en el agente invocador o el humano."
---

# kora-agents

## Proposito

Skill de **construccion y evolucion de agentes KORA**. Da al agente
invocador la capacidad de crear, mantener, mejorar, evolucionar, auditar
y deprecar artefactos agenticos productivos cuya forma material es
`subagente`, `agente-propiamente-tal` o `agente-plataforma`, conforme
estricto a `autoria-spec v1.2` y `agent-skill-construction-spec v1.0`.

Es la rama especializada del ciclo de vida agentico que `artifact-curator`
delega cuando la `forma_material` cae fuera de `habilidad`. Para
`habilidad`, la rama hermana es `urn:kora:artefacto:kora-skills`.

Anclaje normativo:

- `urn:kora:kb:gobernanza` — precedencia, regimenes URN, lifecycle.
- `urn:kora:kb:harness-spec` — ontologia PMI x LFS, leyes inter-eje,
  atlas y matriz de realizabilidad.
- `urn:kora:kb:autoria-spec` — shape unificado, dominios de proyeccion,
  promocion entre formas, validacion condicional.
- `urn:kora:kb:agent-skill-construction-spec` — fases A→H del metodo
  pre-transmutacion.
- `urn:kora:kb:md-spec` — formato base KORA/MD.
- `urn:kora:kb:knowledge-spec` — URNs de conocimiento permitido.
- `urn:kora:kb:qa-spec`, `urn:kora:kb:risk-register-spec` — quality
  attributes y registro de riesgo cuando aplica.
- `urn:kora:kb:multiagente-spec` — coreografia y handoffs cuando Ξ≥3.
- `urn:kora:kb:transmutation-spec`, `urn:kora:kb:runtime-spec-md` y
  runtime-extensions — leyes de proyeccion runtime y matrices de
  realizabilidad por target.

## Cuando Usar

- diseno de un agente nuevo (`subagente`, `agente-propiamente-tal` o
  `agente-plataforma`) desde requerimientos.
- mantencion: refactor de FSM, ajuste de vector ontologico, expansion
  de `conocimiento_permitido`, normalizacion de invariantes.
- mejora: optimizar legibilidad, comprimir grasa del body, alinear con
  bump de spec gobernante, ajustar `qa_budget` o `risk_register`.
- evolucion: promocion entre formas materiales conforme a
  `autoria-spec §8.1`.
- auditoria contra `autoria-spec`, `harness-spec` y matriz de
  realizabilidad runtime.
- deprecacion o retiro de un agente con transicion limpia y, cuando
  aplica, emision de un reemplazo con `supersedes`.

## Cuando NO Usar

- creacion o evolucion de skills (`forma_material: habilidad`) → usar
  `urn:kora:artefacto:kora-skills`.
- ciclo de vida de artefactos de conocimiento (`note`, `guide`,
  `atomic`, `spec`) → usar `urn:kora:artefacto:artifact-curator` o sus
  hermanas (`knowledge-curator`, `atomize`, `curation-conductor`).
- transmutacion concreta a runtime → la skill prepara y verifica el IR;
  la proyeccion la hace `python3 toolchain/kora transmute`.
- diseño de schema de datos puro → fuera del dominio agentico.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud combinando, cuando esta disponible, la salida de
`urn:kora:artefacto:intent-classifier` con la tabla local de
`referencias/dispatcher-table.md`. Producir tres campos:

1. **intent** — uno de: `disenar`, `mantener`, `mejorar`, `evolucionar`,
   `auditar`, `deprecar`, `ambiguo`.
2. **forma material target** — `subagente`,
   `agente-propiamente-tal`, `agente-plataforma`. Si el operador pide
   `habilidad`, devolver handoff a `artifact-curator` con outcome
   `rerouted`.
3. **modo** — `libre` (ejecutar directo) o `guiado` (consolidar
   checkpoints via `urn:kora:artefacto:lifecycle-orchestrator`).

Si la combinacion es ambigua, emitir `outcome: blocked` con
clarificacion solicitada y detener el workflow.

### `intake`

Capturar requerimientos conforme a `agent-skill-construction-spec §3.1`:

| Campo | Pregunta | Salida en IR |
| --- | --- | --- |
| identidad | que rol cumple y para quien | `perfil.dominio`, `descripcion`, `tags` |
| objetivo | que resultado observable entrega | `perfil.salidas`, `plan.estado_terminal` |
| forma | subagente, agente o plataforma | `atlas.forma_material` |
| conocimiento | que URNs puede consultar | `conocimiento_permitido` |
| interaccion | que entradas, herramientas, permisos | `interfaz` |
| estado | que memoria o materia necesita | `vector_ontologico.mu`, `contexto.memoria_config` |
| riesgo | que puede salir mal y como se mitiga | `invariantes`, `qa_budget`, `risk_register` |

Campos no aplicables se omiten o declaran vacios; **nunca** rellenar con
placeholder decorativo.

### `enmarcar`

Aplicar lectura categorial minima conforme a
`agent-skill-construction-spec §2.3` invocando
`urn:kora:artefacto:cat-thinking` cuando el caso involucra arquitectura,
composicion, delegacion, materia ambiental o riesgo no obvio.

Derivar el vector PMI x LFS:

| Pregunta | Eje | Soporte |
| --- | --- | --- |
| que plan ejecuta | Π / free monad | `urn:fxsl:kb:icas-agencia` |
| sobre que materia corre | Μ / cofree comonad | `urn:fxsl:kb:icas-agencia` |
| como interactua | Ξ / lente, protocolo, operad | `urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-escala` |
| a que escala opera | Λ | `urn:fxsl:kb:icas-escala` |
| como se acopla al humano | Φ | `harness-spec`, `qa-spec` |
| compromisos eticos | Σ | `urn:fxsl:kb:icas-safety-alignment` |

Verificar las 5 leyes inter-eje (`harness-spec §4.1`) **antes** de fijar
el vector. Si el vector viola alguna ley, ajustar o rechazar la forma
material elegida.

### `disenar`

Producir el blueprint completo segun `agent-skill-construction-spec §3.3-3.7`:

1. **Forma material**: la mas baja que satisface el objetivo dentro del
   dominio de `autoria-spec §5.2-5.4`. Tabla rapida:

   | Forma | Dominio | Cuando usar |
   | --- | --- | --- |
   | `subagente` | Π∈{1,2,3}, Μ∈{0,1,2}, Ξ∈{1,2,3}, Λ=0-1, Φ∈{1,2} | invocado por otro artefacto, contrato I/O claro |
   | `agente-propiamente-tal` | Π∈{2,3}, Μ∈{2,3}, Ξ∈{2,3,4}, Λ∈{0,1,2}, Φ∈{1,2,3} | workspace productivo con identidad y memoria propias |
   | `agente-plataforma` | Π∈{2,3}, Μ=3, Ξ∈{3,4}, Λ∈{1,2,3}, Φ∈{1,2,3} | always-on con materia ambiental; hoy solo runtime openclaw |

2. **Atlas**: derivar `arnes_categorico` (autoria-spec §4.2) y, opcional,
   `metafora_relacional` (autoria-spec §4.4). Verificar la matriz §6.

3. **Contrato de conocimiento**: `conocimiento_permitido` con URNs
   resolubles, no paths duros (`agent-skill-construction-spec §3.4`).

4. **Nucleo conductual**: cuando `verificacion_coalgebraica: true`,
   modelar `artefacto.plan.fsm` con estados, terminales, transiciones
   y sub-coalgebra de safety cerrada (`autoria-spec §3.5`).

5. **Interfaz**: declarar entradas, salidas, herramientas, permisos,
   limites de autoridad, handoffs si Ξ≥3 y `api_observable` cuando el
   artefacto se compone con otros (`autoria-spec §3.5.1`).

6. **Invariantes**: reglas duras suficientes para impedir drift de
   objetivo. `compromisos_eticos` obligatorio en
   `agente-propiamente-tal` y `agente-plataforma`. `qa_budget` y
   `risk_register` cuando el riesgo no es trivial.

### `materializar`

Escribir el archivo fuente conforme a `autoria-spec §5` y
`agent-skill-construction-spec §3.8`:

| Forma | Fuente primaria | Fibras permitidas |
| --- | --- | --- |
| `subagente` | `artifacts/agents/{ns}/{id}/AGENT.md` | `memoria/` si Μ≥2, `_BUILD/` derivado |
| `agente-propiamente-tal` | `artifacts/agents/{ns}/{id}/AGENT.md` | `memoria/`, `skills/`, recursos, `_BUILD/`, `_transmutation.yml` |
| `agente-plataforma` | `artifacts/agents/{ns}/{id}/AGENT.md` + extension de plataforma | materia ambiental (`MEMORY.md`, `HEARTBEAT.md` u equivalentes) |

Ubicacion canonica para nuevos agentes: `artifacts/agents/_FRAGUA/REVIEW/{ns}/{nombre}/`.
Promocion a productivo via `kora promote` (cuando aplica al pipeline) o
procedimiento revisado.

Mantener IR fuente separado de outputs runtime (`_BUILD/`); jamas usar
`_BUILD/` como fuente.

### `auditar`

Aplicar checks por forma material (`autoria-spec §6, §14` +
`agent-skill-construction-spec §5.2`):

| Check | Aplicabilidad |
| --- | --- |
| `envelope-valido`, `manifest-type-artefacto`, `vector-ontologico-presente` | toda forma |
| `vector-rango-valido`, `leyes-inter-eje` | toda forma |
| `forma-material-declarada`, `dominio-forma-material`, `arnes-compatible-con-forma` | toda forma |
| `shape-condicional`, `topologia-valida` | toda forma |
| `memoria-declarada` | si Μ≥2 |
| `compromisos-eticos` | `agente-propiamente-tal`, `agente-plataforma` |
| `extension-runtime-plataforma` | `agente-plataforma` |
| `coalgebra-conformance` | si `verificacion_coalgebraica: true` |
| `fidelidad-mastra` | `subagente`, `agente-propiamente-tal`, `agente-plataforma` |
| `entornos-objetivo-soportan` | toda forma |
| `construction-source-primary`, `construction-vector-fit`, `construction-knowledge-explicit`, `construction-fsm-valid`, `construction-interface-typed`, `construction-risk-declared`, `construction-runtime-separation`, `construction-categorical-minimality`, `construction-authoring-shape` | construccion nueva |

Comandos:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict --cohort meta-kora
python3 toolchain/kora transmute --target mastra --agent {ns}/{nombre} --dry-run
```

Si `verificacion_coalgebraica: true` y la auditoria falla en
`coalgebra-conformance`, regresar a `disenar` con el FSM como hallazgo
acotado. Para checks de construccion, regresar a la fase
correspondiente (`enmarcar`, `disenar`, `materializar`).

### `emitir-outcome`

Outcome operativo, enum cerrado:

| Outcome | Significado |
| --- | --- |
| `ready` | agente cumple gates; se puede promover a productivo o transmutar |
| `needs_repair` | agente en REVIEW con hallazgos no bloqueantes |
| `processing` | trabajo en curso multi-turno |
| `rerouted` | ruta delegada a otra skill (ej. habilidad → artifact-curator) |
| `blocked` | falta requerimiento o decision editorial del operador |
| `deprecated` | agente deprecado o supersedido emitido |

Adjuntar siempre:

- URN target,
- path de la fuente primaria producida o auditada,
- siguiente paso operativo (promote, transmute, repair, esperar
  decision).

## Reglas Duras

1. IR primero: `Req → Blueprint → IR (AGENT.md)` antes de cualquier
   transmutacion. La construccion no salta a runtime.
2. Vector dentro del dominio de la forma material y respetando las
   leyes inter-eje; rechazar combinaciones invalidas en lugar de
   silenciarlas.
3. Promocion preserva URN, bumpea major y expande shape; democion
   prohibida.
4. Conocimiento por URN resoluble, jamas por path duro.
5. FSM coalgebraica valida cuando `verificacion_coalgebraica: true`:
   estados, terminales, transiciones y sub-coalgebra de safety cerrada.
6. `compromisos_eticos` obligatorios en agente-propiamente-tal y
   agente-plataforma; sin guardrails retoricos.
7. Agente-plataforma exige runtime con Mu=3 declarado en
   `entornos_objetivo` (hoy solo openclaw).
8. REVIEW antes que productivo. Promocion editorial pasa por gate
   strict.
9. Cualquier elemento de Req que no entre en IR queda como descarte
   justificado, riesgo o deuda residual.
10. Auditoria fallida nunca cierra `ready`. Outcomes validos en falla:
    `needs_repair`, `processing`, `blocked`.

## Composicion con otras skills

| Composable con | Cuando |
| --- | --- |
| `urn:kora:artefacto:artifact-curator` | el operador entra por el ciclo de vida general; kora-agents recibe handoff cuando la forma material cae en agente |
| `urn:kora:artefacto:kora-skills` | rama hermana para `forma_material: habilidad`; recibe handoff cuando se pide construir una skill |
| `urn:kora:artefacto:intent-classifier` | dispatch inicial cuando el agente invocador tiene taxonomia local de capacidades |
| `urn:kora:artefacto:lifecycle-orchestrator` | modo guiado con checkpoints inter-fase visibles |
| `urn:kora:artefacto:cat-thinking` | enmarque categorial obligatorio para arquitectura, delegacion, materia ambiental o riesgo no obvio |

## Recursos

### Referencias

- `referencias/dispatcher-table.md` — tabla canonica de despacho
  `(intent × forma material) → ruta`, incluyendo cuando delegar y cuando
  conducir.
- `referencias/blueprint-checklist.md` — checks de construccion por
  fase A→H y por forma material; tabla rapida de dominios y leyes
  inter-eje.

## Salida Esperada

- diagnostico de intent + forma material + modo,
- blueprint con vector PMI x LFS, atlas, FSM y contrato de conocimiento,
- AGENT.md productivo o draft en staging,
- reporte de auditoria con severidades y comandos toolchain ejecutados,
- outcome operativo (`ready`, `needs_repair`, `processing`, `rerouted`,
  `blocked`, `deprecated`),
- siguiente paso operativo concreto.

# Blueprint checklist

Mapa operativo para construir y verificar el blueprint de una skill
KORA conforme a `agent-skill-construction-spec §3` + `autoria-spec §5.1`
+ `harness-spec §4`.

## Fases A→H del metodo

### Fase A — Intake

Capturar requerimientos minimos:

| Campo | Pregunta | Salida en IR |
| --- | --- | --- |
| identidad | que rol cumple y para quien | `perfil.dominio`, `descripcion`, `tags` |
| objetivo | que resultado observable entrega | `perfil.salidas`, `plan.estado_terminal` |
| nivel_prescripcion | que tan prescriptiva es la skill | `extensions.kora.nivel_prescripcion` |
| conocimiento | que URNs puede consultar | `conocimiento_permitido` |
| interaccion | que entradas, herramientas, permisos | `interfaz` |
| portabilidad | que runtimes la van a invocar | `entornos_objetivo` |
| riesgo | que puede salir mal y como se mitiga | `invariantes`, `qa_budget`, `risk_register` |

Campos no aplicables se omiten o declaran vacios; **nunca** placeholder
decorativo.

### Fase B — Enmarque categorial

Traducir intake a vector PMI x LFS dentro del dominio de habilidad:

| Eje | Rango habilidad | Lectura |
| --- | --- | --- |
| Π | {1, 2} | plan ejecutable, sin fixed-points (Π=3 prohibido en habilidad) |
| Μ | {0, 1} | sin memoria persistente; scratchpad efimero permitido |
| Ξ | {1, 2} | invocacion atomica o lente bidireccional |
| Λ | 0 | individual |
| Φ | 1 | instrumental — supertool |
| Σ | [v1..v5] | compromisos eticos enriched |

Si el dominio de habilidad no alcanza para el objetivo declarado,
considerar promocion a subagente (handoff a `kora-agents`).

### Fase C — Decision de forma material

| Forma | Π | Μ | Ξ | Λ | Φ |
| --- | --- | --- | --- | --- | --- |
| `habilidad` | {1, 2} | {0, 1} | {1, 2} | 0 | 1 |

Regla: la forma material **mas baja** que satisface el objetivo.
Cuando el caso requiere memoria persistente, orquestacion o servicio
always-on, no es habilidad; delegar a `kora-agents`.

### Fase D — Contrato de conocimiento

- `conocimiento_permitido` con URNs resolubles, jamas paths duros.
- Lista vacia o omitida solo si la spec lo permite y si realmente no
  hay KB.
- Sin retrieval implicito por similitud cuando el contrato exige
  fuente gobernada.

### Fase E — Nucleo conductual

El plan **DEBE** modelarse como FSM cuando hay ramificacion real;
cuando es lineal, describirlo como secuencia de pasos.

`verificacion_coalgebraica: true` solo si realmente se requiere
termination check con sub-coalgebra de safety cerrada. Para skills
tipicas, `false` o no declarado.

Cuando se declara `plan.fsm`:

- `inicial` y `terminales` no vacios.
- `transiciones` apuntan a estados existentes.
- todo estado no terminal alcanza un terminal en finitos pasos.

### Fase F — Interfaz y capacidades

Declarar:

- entradas esperadas,
- salidas emitidas,
- `herramientas` (tipico: `[Read, Grep, Glob]` para skills
  introspectivas; `[Read, Write, Edit, Glob, Grep, Bash]` para skills
  productoras),
- `permisos`,
- limites de autoridad,
- `interfaz.api_observable` cuando `componible_con` no esta vacio.

### Fase G — Invariantes, seguridad y riesgo

- `invariantes.reglas_duras` suficientes para impedir drift de
  objetivo (no slogans).
- `compromisos_eticos`: opcional en habilidad (no obligatorio).
- `qa_budget` y `risk_register` cuando el riesgo no es trivial.

### Fase H — Materializacion

Topologia canonica:

```
artifacts/skills/{nombre}/                  # top-level sin namespace
  SKILL.md                                   # obligatorio
  scripts/                                   # opcional
  referencias/                               # opcional
  recursos/                                  # opcional
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

- Body ≤ 500 lineas.
- Si hay subdirs, body declara `## Recursos` con cada subdir.
- Subdirs canonicos exclusivos: `scripts/`, `referencias/`,
  `recursos/`.
- Staging: `artifacts/skills/_TALLER/REVIEW/{nombre}/`.

## Niveles de prescripcion

| Nivel | Cuando usar | Ejemplo |
| --- | --- | --- |
| `alto` | la skill prescribe metodo riguroso y ata al invocador a una secuencia o estructura especifica | `atomize`, `knowledge-curator`, `cat-thinking` |
| `medio` | la skill organiza el metodo pero acepta variacion del invocador | `intent-classifier`, `lifecycle-orchestrator`, `atomize` |
| `bajo` | la skill ofrece capacidad portable opcional sin obligar metodologia | utilitario portable simple |

## Leyes inter-eje (harness-spec §4.1)

Vector valido **DEBE** cumplir:

1. Π≥3 ⟹ Μ≥1 (no aplica en habilidad: Π≤2).
2. Ξ=4 ⟹ Λ≥1 (no aplica en habilidad: Ξ≤2).
3. Φ≥2 ⟹ Μ≥1 (no aplica en habilidad: Φ=1).
4. Σ.accountability ≥ 2 ⟹ Σ.transparency ≥ 2.
5. Λ=3 ⟹ Σ.i ≥ 2 ∀i (no aplica: Λ=0).

Para habilidad la unica ley activa de las inter-eje es la 4. Las
demas son automaticas por restriccion del dominio.

## Tabla de checks aplicables

| Check | Aplicabilidad |
| --- | --- |
| `envelope-valido` | universal |
| `manifest-type-artefacto` | universal |
| `vector-ontologico-presente` | universal |
| `vector-rango-valido` | universal |
| `leyes-inter-eje` | universal |
| `forma-material-declarada` | universal |
| `dominio-forma-material` | dominio habilidad |
| `arnes-compatible-con-forma` | (utilidad, disciplina, delegado) |
| `shape-condicional` | universal |
| `topologia-valida` | `artifacts/skills/{nombre}` o `{ns}/{nombre}` |
| `progressive-disclosure` | body ≤ 500 lineas |
| `recursos-documentados` | si hay subdirs, body declara `## Recursos` |
| `skill-structure` | subdirs canonicos exclusivos |
| `fidelidad-agentskills` | transmute --target agentskills --dry-run byte-identical |
| `entornos-objetivo-soportan` | cada runtime acepta `(arnes, habilidad)` |
| `referencias-resolubles` | URNs en `componible_con`, `conocimiento_permitido` resuelven |
| `construction-source-primary` | universal |
| `construction-vector-fit` | universal |
| `construction-knowledge-explicit` | universal |
| `construction-fsm-valid` | si plan.fsm declarado |
| `construction-interface-typed` | universal |
| `construction-risk-declared` | si riesgo no trivial |
| `construction-runtime-separation` | universal |
| `construction-categorical-minimality` | universal |
| `construction-authoring-shape` | universal |

## Comandos de verificacion

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 toolchain/kora transmute --target agentskills --agent kora/{nombre} --dry-run
python3 toolchain/kora kb-graph --json --orphans
python3 -m unittest discover -s tests   # cuando se toca toolchain, specs o behavior compartido
```

## Antipatrones a rechazar

| Antipatron | Falla | Correccion |
| --- | --- | --- |
| skill inflada | body > 500 lineas | mover detalle a `referencias/` |
| KB por path | knowledge no resoluble por URN | usar `conocimiento_permitido` |
| vector decorativo | PMI x LFS no deriva del comportamiento | rehacer enmarque categorial |
| sin nivel_prescripcion | campo obligatorio omitido | declarar alto, medio o bajo |
| subdirs ad-hoc | carpetas distintas a `scripts/`, `referencias/`, `recursos/` | reorganizar a los tres canonicos |
| `## Recursos` ausente con subdirs | check falla | agregar seccion declarando cada subdir |
| over-formalizacion | `verificacion_coalgebraica: true` sin necesidad | quitar el flag y describir el plan como secuencia |
| guardrail retorico | regla dura sin verificacion | escribir regla operativa o `qa_budget` |
| runtime-first | output target suplanta IR | crear `SKILL.md` y transmutar despues |
| fidelidad rota | transmute a agentskills falla | revisar shape; el contrato de interop es ley |

## Severidad y outcome

| Severidad de hallazgos | Outcome sugerido |
| --- | --- |
| sin hallazgos | `ready` |
| solo media o baja, no bloqueantes | `needs_repair` con deuda residual declarada |
| al menos una alta | `needs_repair` o `processing` segun disponibilidad del operador |
| dependencia faltante o decision editorial pendiente | `blocked` |

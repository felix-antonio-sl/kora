---
_manifest:
  urn: "urn:kora:kb:skill-overlay-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "v1.x: capability profile portable canonico; v2.0 redefine SKILL.md como serializacion-de-ontologia, derivada de harness-spec PMI × LFS"
version: "2.0.0"
status: published
tags: [spec, skill, overlay, portable, capability, serializacion]
lang: es
extensions: {}
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
  cites:
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:agentfile-spec"
    - "urn:kora:kb:transmutation-spec"
---

# KORA/Skill-Overlay-Spec v2.0.0

## 1. Definicion

`SKILL.md` es **una serializacion de authoring** del vector ontologico
PMI × LFS (definido en `harness-spec`), para el dominio de capacidades
pequeñas, portables y con baja persistencia.

El skill moderno de KORA es compatible con runtimes tipo agentskills.io
(Claude Code, Codex, Gemini) y enriquecido con overlay KORA. Es la forma
preferida de capacidad para artefactos con plan acotado, sin estado
persistente cross-session.

### 1.1 Cambio respecto a v1

v1.2 establecia contrato minimo + estructura interna (`scripts/references/
assets`) + composicion via `composable_with`. Eso era correcto como
*shape* pero trataba el skill como ontologia autonoma.

v2.0 redefine `SKILL.md` como **serializacion**: proyecta sobre el vector
ontologico de `harness-spec`. El vector es la definicion primaria; el shape
portable es convencion de authoring.

## 2. Dominio de proyeccion

`SKILL.md` es la serializacion canonica para vectores con:

- **Π ∈ {1, 2}** (plan lineal o ramificado; sin fixed-points complejos).
- **Μ ∈ {0, 1}** (sin materia o materia efimera intra-invocacion).
- **Ξ ∈ {1, 2}** (interaccion atomica o bidireccional simple; sin protocolos multi-fase).
- **Λ = 0** (individual; skills no operan a nivel organizacional directamente).
- **Φ = 1** (instrumental; el skill es herramienta).

Vectores fuera de este dominio usan otras serializaciones
(`agentfile-spec v2.0` para agentes con memoria; futura
`platform-agent-spec` para servicios always-on).

Los skills cubren tres arneses del atlas A:

- **Utilidad**: `(Π=1, Μ=0, Ξ=1)` — funciones puras.
- **Disciplina**: `(Π=2, Μ=0, Ξ=1-2)` — cuerpo de conocimiento monadico.
- **Delegado**: `(Π=2, Μ=1, Ξ=2)` — scratchpad intra-invocacion.

## 3. Contrato minimo portable

Todo skill portable **DEBE** declarar:

- `name` — identificador del skill (kebab-case, <64 chars).
- `description` — cuando usar, proactive hints, examples.
- `allowed-tools` — herramientas utilizadas por el skill.

Overlay KORA recomendado (en frontmatter):

```yaml
_manifest:
  urn: "urn:{ns}:skill:{id}:{version}"
  type: lazy_load_endofunctor
extensions:
  kora:
    harness_vector:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1,1,3,1,0]
    presentation: state-primary
    lifecycle:
      status: active
      created: "YYYY-MM-DD"
      updated: "YYYY-MM-DD"
    knowledge:
      - "urn:{ns}:kb:..."
    composable_with:
      - "urn:{ns}:skill:..."
    domain: [...]
    level: L1  # densidad del authoring (no ontologia)
```

## 4. Principios

1. **Portabilidad primero** — frontmatter minimo compatible cross-runtime.
2. **Overlay sin colision** — metadata KORA no rompe runtimes que la ignoran.
3. **Capacidad pequeña y componible** — un skill hace una cosa bien.
4. **Dependencias explicitas** — knowledge refs, tools allowed, composables declarados.
5. **Estructura interna predecible** — §5.
6. **Ontologia derivada del vector** — el skill *es* su vector PMI × LFS.

## 5. Estructura interna del skill

Un skill productivo **DEBE** consistir en un directorio con `SKILL.md` en la
raiz. Los recursos auxiliares, cuando existen, **DEBEN** organizarse bajo los
tres subdirectorios canonicos:

```
{name}/
├── SKILL.md         (obligatorio, punto de entrada)
├── scripts/         (opcional, automatizacion determinista)
├── references/      (opcional, documentacion lazy-load)
└── assets/          (opcional, plantillas/insumos de salida)
```

### 5.1 Semantica de los subdirectorios

| Subdir | Proposito | Carga |
|--------|-----------|-------|
| `scripts/` | Automatizacion o pasos deterministas (shell, python, etc.) | Invocada explicitamente |
| `references/` | Documentacion extensa, schemas, reglas de dominio, guias | Lazy-load bajo demanda |
| `assets/` | Plantillas, imagenes, boilerplate, insumos de salida | Usados en output |

### 5.2 Reglas de la estructura interna

1. Los tres subdirectorios son **opcionales**: un skill trivial puede vivir con
   solo `SKILL.md`.
2. Si el skill usa alguno, **DEBE** usar los nombres canonicos — no sinonimos
   como `docs/`, `templates/`, `data/`.
3. Cualquier subdir **adicional** al trio canonico es invalido en un skill
   productivo (`status: active`); solo se permite en staging o en perfil
   legacy `CM-*` (§5.5).
4. El `SKILL.md` **DEBE** documentar explicitamente cada subdirectorio que
   use, en una seccion `## Resources` (§5.3).
5. Si un subdirectorio canonico esta presente fisicamente pero sin referencia
   en `## Resources`, se considera inactivo — el runtime no lo cargara.

### 5.3 Seccion `## Resources` en el body

El body del `SKILL.md` **DEBE** incluir una seccion `## Resources` cuando el
skill usa alguno de los subdirectorios auxiliares:

```markdown
## Resources

### Scripts
Describe que scripts viven en `scripts/` y cuando invocarlos.

### References
Describe los archivos de `references/` y cuando cargarlos (lazy-load).

### Assets
Describe los templates o insumos en `assets/` y como consumirlos.
```

Reglas:

1. Solo aparecen las subsecciones `###` cuyos subdirs existen.
2. El orden canonico es `Scripts → References → Assets`.
3. Referencia interna a archivo auxiliar **DEBERIA** usar path relativo.
4. La seccion **NO DEBE** renombrarse a `## References`, `## Files` ni
   similares — colisiona con el subdir `references/` y rompe portabilidad
   cross-runtime.

### 5.4 Skills triviales

Un skill cuyo comportamiento cabe entero en el body del `SKILL.md` **NO
NECESITA** seccion `## Resources` ni subdirectorios. La plantilla minima es:

```
{name}/
└── SKILL.md
```

con body que describe workflow, reglas y output esperado. Este es tipicamente
un arnés Utilidad con vector `(1, 0, 1, 0, 1, Σ_bajo)`.

### 5.5 Perfil de compatibilidad `CM-*`

Los bundles legacy `CM-*` **PUEDEN** desviarse de §5.1 y §5.2. En particular:

- `CM-*/references/` y `CM-*/assets/` ya siguen la convencion — se mantienen.
- `CM-*` anidados (`CM-*/skills/CM-*/`) son tolerados como perfil legacy,
  pero **no son patron canonico** para skills productivos nuevos.
- La composicionalidad entre skills productivos se expresa via
  `composable_with` en overlay, **no** via anidamiento fisico.

Un skill productivo con `status: active` **NO DEBE** anidar sub-skills en
su directorio.

## 6. Progressive disclosure (Codex pattern)

Los skills portables **DEBEN** seguir el patron de *progressive disclosure*
documentado por Codex:

1. **Metadata** (`name` + `description`): siempre en contexto (~100 words).
2. **SKILL.md body**: cargado cuando el skill trigger (<5k words).
3. **Bundled resources** (scripts/references/assets): bajo demanda.

Reglas:

- Body `<500 lineas`. Si excede, split a `references/` por tema o dominio.
- `description` debe ser **clara y comprensiva** — es lo unico que el runtime
  lee para decidir si activar el skill.
- Skills con corpus extenso organizan `references/` por dominio (ver
  `arquitecto-categorico/references/` como ejemplo).

## 7. Degrees of freedom

Los skills declaran su **grado de prescripcion** (Codex pattern):

- **High freedom** (text-based): `skill_freedom: high` — texto flexible,
  heuristicas, multiples approaches validos.
- **Medium freedom** (pseudocode o scripts parametrizados):
  `skill_freedom: medium` — pattern preferido con configuracion.
- **Low freedom** (specific scripts, few params): `skill_freedom: low` —
  operaciones fragiles, consistencia critica, secuencia especifica.

Declarado en `extensions.kora.skill_freedom`. Permite al runtime calibrar
latitud de interpretacion.

## 8. Composicion y composable_with

Un skill portable **PUEDE** componerse con otros skills:

```yaml
extensions:
  kora:
    composable_with:
      - "urn:kora:skill:atomize:1.0.0"
      - "urn:kora:skill:data-modeling:1.0.0"
```

Esta composicion es **categorica** — composicion Kleisli cuando los skills
comparten monad de efectos, o composicion de profunctores cuando ambos
tienen interfaces compatibles. No es anidamiento fisico.

## 9. Lifecycle

Los skills son artefactos ejecutables (gobernanza §5):

- `draft` — aun no se carga en runtime.
- `active` — productivo, resolvible por agentes.
- `deprecated` — conservado pero nuevos agentes no deben invocarlo.
- `retired` — no debe cargarse; trazabilidad historica; URN no resuelve.

Transiciones inversas invalidas. Un skill `retired` **NO PUEDE**
reactivarse; emitir uno nuevo con `supersedes`.

## 10. Ubicacion y topologia

Ubicaciones validas:

- `SKILLS/{name}/SKILL.md` — top-level portable sin namespace.
- `SKILLS/{namespace}/{name}/SKILL.md` — con namespace.

Staging:

- `SKILLS/_TALLER/INBOX/{name}/` — pre-categorial.
- `SKILLS/_TALLER/REVIEW/{name}/` — con URN provisional.

No todo lo que vive bajo `SKILLS/` reclama esta spec. El catalogo puede
mezclar perfiles portables con bundles legacy o artefactos auxiliares.

## 11. Validacion

| Check | Condicion | Severity | Enforcement |
|-------|-----------|----------|-------------|
| Portabilidad base | `name`, `description`, `allowed-tools` validos | high | lint |
| Vector ontologico presente | `extensions.kora.harness_vector` declarado | high | schema |
| Dominio de proyeccion | Vector cumple §2 (Π≤2, Μ≤1, Ξ≤2, Λ=0, Φ=1) | high | lint |
| Leyes PMI × LFS | Vector cumple `harness-spec §4.1` | high | lint (delega) |
| Topologia externa | El skill vive en topologia admitida (§10) | medium | lint |
| Estructura interna canonica | Subdirs productivos ∈ {scripts, references, assets} | medium | lint |
| Resources documentadas | Si existen subdirs, body tiene `## Resources` con subseccion correspondiente | medium | lint |
| Anidamiento prohibido | Skills `active` no anidan sub-skills | medium | lint |
| Referencias resolubles | Paths mencionados en `## Resources` existen | low | lint |
| Alias trazable | Si hay espejo CM, el vinculo es explicito | low | manual |
| Degrees of freedom | `skill_freedom` declarado | low | lint |

## 12. Plantilla portable canonica

Template minimo para un skill productivo:

```markdown
---
_manifest:
  urn: "urn:kora:skill:my-skill-name:1.0.0"
  type: lazy_load_endofunctor
name: my-skill-name
description: States what this skill does and when to use it.
allowed-tools: Read, Write, Bash
extensions:
  kora:
    harness_vector:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1,1,3,1,0]
    presentation: state-primary
    skill_freedom: medium
    lifecycle:
      status: active
      created: "2026-04-17"
    knowledge: []
    composable_with: []
    domain: []
    level: L1
---

# My Skill Name

Use this skill when the user needs [task type] and the default agent
behavior is not enough.

## Goal

Describe the outcome this skill should produce.

## When To Use

- Use when ...
- Do not use when ...

## Workflow

1. Inspect the relevant context first.
2. Read files or references only if they are needed.
3. Use scripts when the task requires deterministic execution.
4. Use assets when output depends on templates or bundled files.
5. Verify the result before concluding.

## Resources

### Scripts
Use files under `scripts/` for repeatable operations.

### References
Use files under `references/` for detailed documentation loaded on demand.

### Assets
Use files under `assets/` for templates or output resources.

## Rules

- Do not invent facts.
- Prefer existing project conventions.
- Keep output concise unless the user asks for depth.

## Output

Describe the expected output format.
```

## 13. Relacion con otras specs

- `harness-spec`: ontologia fuente — los skills declaran su vector.
- `agentfile-spec v2.0`: serializacion para otros dominios del vector (agentes con Μ≥2).
- `transmutation-spec`: functor de proyeccion a runtimes.
- `md-spec`: formato base KORA/MD.
- `gobernanza`: precedencia, URN regimen ejecutable.

## 14. Migracion (v1 → v2)

### 14.1 Contrato vigente v2

- `SKILL.md` es serializacion, no ontologia.
- `extensions.kora.harness_vector` es fuente de verdad del skill.
- Estructura interna (`scripts/references/assets`) mantenida.
- `## Resources` canonico en body cuando hay subdirs.
- `skill_freedom` como declaracion explicita de prescripcion.
- Progressive disclosure como invariant.

### 14.2 Cambios v1.2 → v2.0

- §1 redefinicion: `SKILL.md` = serializacion de ontologia.
- §2 dominio de proyeccion explicito sobre vector.
- §6 progressive disclosure como invariant.
- §7 degrees of freedom como campo explicito.
- §11 checks actualizados (vector ontologico obligatorio).

### 14.3 Que migrar

- Skills existentes: agregar `harness_vector` al frontmatter
  (auto-derivable via `kora migrate --profile v2-skill`).
- Declarar `skill_freedom` (default medium si ambiguo).
- Los subdirs `scripts/references/assets` y la seccion `## Resources`
  siguen iguales que v1.2.

### 14.4 Que se depreca

- Declaracion implicita de ontologia sin vector.
- Formato plano `_ATOMIC_GRAPH.md` (deja de ser salida valida de skills,
  ya deprecado en `md-spec §10.4`).
- CM-* como patron canonico para skills nuevos (pasa a compatibilidad
  residual — se mantiene §5.5).

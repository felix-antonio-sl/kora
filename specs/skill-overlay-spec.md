---
_manifest:
  urn: "urn:kora:kb:skill-overlay-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "capability profile portable canonico; v1.1 alinea lifecycle con gobernanza §5 (agrega retired); v1.2 normaliza estructura interna del skill (scripts/references/assets) y formaliza la seccion Resources del SKILL.md"
version: "1.2.0"
status: published
tags: [spec, skill, overlay, portable, capability, resources]
lang: es
extensions: {}
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
---

# KORA/Skill-Overlay-Spec v1.2.0

## 1. Definicion

El skill moderno de KORA es un perfil portable `SKILL.md` compatible con
runtimes tipo agentskills.io (Codex, Claude Code, OpenClaw) y enriquecido con
overlay KORA. Este es el formato preferido de capacidad.

La portabilidad real requiere normalizar **tres niveles** simultaneamente:

1. el frontmatter minimo (§2),
2. la topologia externa — ubicacion del `SKILL.md` en el repo (§4),
3. la estructura interna — subdirectorios auxiliares del skill (§5).

## 2. Contrato minimo portable

Todo skill portable **DEBERIA** declarar:

- `name`
- `description`
- `allowed-tools`

Overlay KORA recomendado:

- `metadata.kora.urn`
- `metadata.kora.lifecycle`
- `metadata.kora.tools`
- `metadata.kora.knowledge`
- `metadata.kora.domain`
- `metadata.kora.composable_with`

## 3. Principios

1. Portabilidad primero.
2. Overlay sin colision.
3. Capacidad pequeña y componible.
4. Dependencias explicitas.
5. Estructura interna predecible.

El overlay agrega trazabilidad y gobierno; no debe romper la utilidad del skill
si un runtime ignora `metadata.kora.*`. La estructura interna (§5) replica la
convencion compartida entre Codex, Claude Code y OpenClaw, de modo que un
skill puede copiarse entre plataformas sin reorganizacion.

## 4. Ubicacion y topologia externa

Ubicaciones validas:

- `SKILLS/{name}/SKILL.md`
- `SKILLS/{namespace}/{name}/SKILL.md`

Staging:

- `SKILLS/_TALLER/INBOX/{name}/` — pre-categorial.
- `SKILLS/_TALLER/REVIEW/{name}/` — con URN provisional.

No todo lo que vive bajo `SKILLS/` reclama esta spec. El catalogo puede mezclar
perfiles portables con bundles legacy o artefactos auxiliares.

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

| Subdir        | Proposito                                                   | Carga                  |
| ------------- | ----------------------------------------------------------- | ---------------------- |
| `scripts/`    | Automatizacion o pasos deterministas (shell, python, etc.)  | Invocada explicitamente |
| `references/` | Documentacion extensa, schemas, reglas de dominio, guias    | Lazy-load bajo demanda |
| `assets/`     | Plantillas, imagenes, boilerplate, insumos de salida        | Usados en output       |

### 5.2 Reglas de la estructura interna

1. Los tres subdirectorios son **opcionales**: un skill trivial puede vivir con
   solo `SKILL.md`.
2. Si el skill usa alguno, **DEBE** usar los nombres canonicos (`scripts`,
   `references`, `assets`) — no sinonimos como `docs/`, `templates/`, `data/`.
3. Cualquier subdir **adicional** al trio canonico es invalido en un skill
   productivo (`status: active`); solo se permite en staging o en perfil
   legacy CM-* (§5.5).
4. El `SKILL.md` **DEBE** documentar explicitamente cada subdirectorio que
   use, en una seccion `## Resources` (§5.3).
5. Si un subdirectorio canonico esta presente fisicamente pero sin
   referencia en `## Resources`, se considera inactivo — el runtime no lo
   cargara.

### 5.3 Seccion `## Resources` en el body del SKILL.md

El body del `SKILL.md` **DEBE** incluir una seccion `## Resources` cuando el
skill usa alguno de los subdirectorios auxiliares. La seccion agrupa las
subsecciones `###` canonicas:

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
3. Una referencia interna a un archivo auxiliar **DEBERIA** usar path relativo:
   `scripts/build.sh`, `references/schema.md`, `assets/template.txt`.
4. La seccion **NO DEBE** renombrarse a `## References`, `## Files` ni
   similares — colisiona con el subdir `references/` y rompe portabilidad
   con los templates de Codex/Claude Code.

### 5.4 Skills triviales (sin recursos)

Un skill cuyo comportamiento cabe entero en el body del `SKILL.md` **NO
NECESITA** seccion `## Resources` ni subdirectorios. La plantilla minima es:

```
{name}/
└── SKILL.md
```

con body que describe workflow, reglas y output esperado.

### 5.5 Perfil de compatibilidad CM-*

Los bundles legacy `CM-*` **PUEDEN** desviarse de §5.1 y §5.2. En particular:

- `CM-*/references/` y `CM-*/assets/` ya siguen la convencion — se mantienen.
- `CM-*` anidados (`CM-*/skills/CM-*/`) son tolerados como perfil legacy,
  pero **no son patron canonico** para skills productivos nuevos.
- La composicionalidad entre skills productivos se expresa via
  `metadata.kora.composable_with` en overlay, **no** via anidamiento fisico.

Un skill productivo con `status: active` **NO DEBE** anidar sub-skills en
su directorio. Si necesita capacidades componibles, declaralas como skills
independientes en `SKILLS/{name}/` y referencialas en
`metadata.kora.composable_with`.

## 6. Composicion y alias

Un skill portable **PUEDE**:

- componerse con otros (via `metadata.kora.composable_with`),
- declarar conocimiento requerido (via `metadata.kora.knowledge`),
- tener alias o espejo `CM-*` por compatibilidad.

Pero:

1. no expande el dominio del agente por si mismo,
2. no suplanta `safety`,
3. no necesita un alias CM para ser valido.

## 7. Lifecycle

Los skills son artefactos ejecutables. Su lifecycle se alinea con
`gobernanza §5`:

- `draft` — aun no se carga en runtime
- `active` — productivo, resolvible por agentes
- `deprecated` — se conserva pero nuevos agentes no deben invocarlo
- `retired` — no debe cargarse; se mantiene por trazabilidad historica,
  su `_manifest.urn` no resuelve en runtime

Las transiciones inversas son invalidas. Un skill `retired` **NO PUEDE**
reactivarse; debe emitirse uno nuevo con `supersedes` hacia el retirado.

## 8. Validacion

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Portabilidad base | `name`, `description`, `allowed-tools` validos | lint |
| Overlay limpio | `metadata.kora.*` no contradice la capa portable | lint/manual |
| Topologia externa | El skill vive en topologia admitida (§4) | lint |
| Alias trazable | Si tiene espejo CM, el vinculo es explicito | manual/lint |
| Estructura interna canonica | Subdirs productivos ∈ {scripts, references, assets} | lint |
| Resources documentadas | Si existe `scripts/`, `references/` o `assets/`, el body tiene `## Resources` con subseccion correspondiente | lint |
| Anidamiento prohibido | Skills `active` no anidan sub-skills (`skills/CM-*`) | lint |
| Referencias resolubles | Paths mencionados en `## Resources` existen en el filesystem | lint |

## 9. Plantilla portable canonica

Template minimo para un skill productivo con recursos:

```markdown
---
name: my-skill-name
description: States what this skill does and when to use it.
allowed-tools: Read, Write, Bash
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

Use files under `scripts/` for repeatable or fragile operations that
should not be reimplemented ad hoc.

### References

Use files under `references/` for detailed documentation, schemas,
domain rules, or long guidance that should be loaded only when needed.

### Assets

Use files under `assets/` for templates, images, fonts, boilerplate,
or other output resources.

## Rules

- Do not invent facts.
- Prefer existing project conventions.
- Keep output concise unless the user asks for depth.
- Surface uncertainty clearly.
- Verify important results before concluding.

## Output

Describe the expected output format, tone, or acceptance criteria.
```

## 10. Migracion

### 10.1 Contrato vigente v1.2

- El skill portable es la forma canonica.
- Frontmatter minimo: `name`, `description`, `allowed-tools`.
- Overlay KORA en `metadata.kora.*`.
- Estructura interna: `SKILL.md` en raiz + `scripts/` + `references/` +
  `assets/` opcionales.
- Seccion `## Resources` en body cuando hay subdirs.
- Composicion via `metadata.kora.composable_with`, no via anidamiento.
- `CM-*` queda absorbido como perfil de compatibilidad.

### 10.2 Cambios v1.2 respecto a v1.1

- §5 nueva: Estructura interna del skill con tres subdirectorios canonicos.
- §5.3 nueva: Seccion `## Resources` canonica en el body del SKILL.md.
- §5.4 nueva: Regla para skills triviales sin recursos.
- §5.5 nueva: Perfil de compatibilidad CM-* con reglas de anidamiento.
- §8: cuatro nuevos checks de validacion de estructura y Resources.
- §9 nueva: Plantilla portable canonica completa.

### 10.3 Que migrar desde v1.1

- Skills existentes con subdirs no canonicos (`docs/`, `templates/`,
  `data/`) **DEBEN** renombrarse a `references/` o `assets/` segun
  semantica al promover de `_TALLER/INBOX/` a REVIEW.
- Skills productivos con `skills/CM-*` anidados **DEBEN** extraer los
  sub-skills a top-level y declararlos en `metadata.kora.composable_with`
  al promover.
- Skills sin seccion `## Resources` que usen subdirs **DEBEN** agregarla.
- Los skills en staging quedan exentos: el contrato v1.2 aplica al
  promover a productivo.

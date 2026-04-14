---
_manifest:
  urn: "urn:kora:kb:skill-overlay-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "agentskills.io spec v1.0; KORA skill-spec-md v4.3.0; polymath analysis"
version: "1.0.0"
status: published
tags: [spec, skill, overlay, agentskills, composicion]
lang: es
extensions: {}
---

# KORA/Skill-Overlay-Spec v1.0.0

## 1. Definicion

Un skill KORA es un `SKILL.md` agentskills.io-compatible extendido con overlay KORA via `metadata.kora.*`. El `SKILL.md` es universal — el mismo archivo sirve para cualquier runtime agentskills.io sin transmutacion. El overlay agrega gobernanza, composicion, lifecycle y trazabilidad sin alterar la superficie portable.

### 1.1 Principio: Isomorfismo fluido

El funtor de olvido `U: KORA-Skill -> agentskills.io-Skill` que descarta `metadata.kora.*` es fielmente full: preserva toda la informacion que un runtime agentskills.io necesita, y no introduce ni destruye morfismos. No existe transmutacion de skills — un skill KORA **ES** un skill agentskills.io con metadata adicional ignorable.

Formalmente:

- **Fidelidad**: si dos skills KORA difieren solo en `metadata.kora.*`, son el mismo skill agentskills.io.
- **Fullness**: toda transformacion valida entre skills agentskills.io se levanta a una transformacion KORA (enriquecida con el overlay).
- **Portabilidad**: un runtime que ignore `metadata.kora.*` ejecuta el skill sin perdida funcional.

### 1.2 Alcance

Esta especificacion gobierna:

1. El overlay `metadata.kora.*` y su schema.
2. El CM Core como body del `SKILL.md` (delegando grammar a `skill-spec-md`).
3. La composicion categorial de skills.
4. La subsumision de skills por agentes.
5. El lifecycle del skill overlay.
6. La validacion del overlay.
7. La migracion desde formato KORA legacy a formato agentskills.io + overlay.

Esta especificacion **NO** gobierna:

- Los campos nativos agentskills.io (`name`, `description`, `license`, `compatibility`, `allowed-tools`). Esos son definidos por la spec agentskills.io.
- La grammar interna del CM Core (`Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`). Esa es materia de `skill-spec-md`.
- La topologia del workspace agente. Esa es materia de `agent-spec-md`.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Skill | Unidad de capacidad cognitiva materializada como `SKILL.md` dentro de `SKILLS/` |
| CM Core | Las 4 secciones obligatorias del body: `Purpose`, `Input/Output`, `Procedure`, `Signature Output` (o sus equivalentes en espanol: `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`) |
| Overlay | El bloque `metadata.kora` dentro del frontmatter YAML del `SKILL.md` |
| Subsumision | Relacion de contencion: un agente subsume un skill cuando lo puede ejecutar dentro de su envelope |
| Composicion | Combinacion de skills como morfismos en categoria Kleisli |
| Lifecycle | Estados del skill: `draft`, `active`, `deprecated`, `retired` |
| Level | Clasificacion de complejidad del skill: `L0` (atomico), `L1` (compuesto simple), `L2` (orquestador), `L3` (meta-generativo) |
| Required | Campo o seccion que **DEBE** estar presente para validacion |
| Optional | Campo o seccion que **PUEDE** omitirse sin invalidar el skill |
| Portable | Propiedad de un skill que funciona en cualquier runtime agentskills.io sin modificacion |

## 3. Formato SKILL.md

### 3.1 Frontmatter: campos agentskills.io

Los siguientes campos son definidos por la spec agentskills.io y **NO DEBEN** modificarse, extenderse ni reinterpretarse por KORA:

| Campo | Tipo | Requerido | Restricciones | Ejemplo |
| --- | --- | --- | --- | --- |
| `name` | string | **SI** | kebab-case, 1-64 chars, = nombre del directorio que contiene `SKILL.md` | `data-modeling` |
| `description` | string | **SI** | 1-1024 chars, lenguaje natural, describe que hace el skill | `"Data modeling with ERDs..."` |
| `license` | string | no | identificador SPDX o texto libre | `"MIT"` |
| `compatibility` | string | no | runtimes compatibles declarados | `"claude-code >= 1.0"` |
| `metadata` | map | no | mapa extensible; KORA usa la clave `kora` dentro de este mapa | `metadata: { kora: {...} }` |
| `allowed-tools` | string o list | no | tools que el skill necesita del runtime; space-separated string o YAML list | `"Read Grep Glob"` o `[Read, Grep, Glob]` |

Reglas sobre campos agentskills.io:

1. `name` **DEBE** coincidir exactamente con el nombre del directorio padre del `SKILL.md`.
2. `description` **DEBE** ser autocontenida: un runtime que solo lea el frontmatter debe poder decidir si el skill es relevante.
3. `allowed-tools` **DEBE** declarar el conjunto minimo de tools que el skill requiere, no el maximo disponible.
4. `metadata` es el unico punto de extension. KORA **NO DEBE** agregar campos raiz al frontmatter fuera de los definidos por agentskills.io.

### 3.2 Overlay KORA: `metadata.kora`

El overlay KORA vive exclusivamente dentro de `metadata.kora` y **DEBE** seguir este schema:

```yaml
metadata:
  kora:
    # --- Identidad (obligatorio) ---
    urn: "urn:{namespace}:skill:{id}"

    # --- Lifecycle (obligatorio) ---
    lifecycle:
      status: draft | active | deprecated | retired
      created: "YYYY-MM-DD"
      updated: "YYYY-MM-DD"

    # --- Capacidades (opcional) ---
    tools: ["Read", "Grep", "Glob"]
    knowledge: ["urn:kora:kb:md-spec"]

    # --- Composicion (opcional) ---
    composable_with: ["otro-skill"]

    # --- Clasificacion (opcional) ---
    domain: ["knowledge-governance"]
    level: L0 | L1 | L2 | L3
```

#### 3.2.1 Campos del overlay

| Campo | Tipo | Requerido | Restricciones | Semantica |
| --- | --- | --- | --- | --- |
| `urn` | string | **SI** | Formato `urn:{ns}:skill:{id}` conforme a `gobernanza §3` | Identidad unica del skill en el ecosistema KORA |
| `lifecycle.status` | enum | **SI** | Uno de: `draft`, `active`, `deprecated`, `retired` | Estado actual del skill |
| `lifecycle.created` | string | **SI** | Formato ISO 8601 `YYYY-MM-DD` | Fecha de creacion |
| `lifecycle.updated` | string | **SI** | Formato ISO 8601 `YYYY-MM-DD`, >= `created` | Fecha de ultima actualizacion |
| `tools` | list[string] | no | Cada elemento es un nombre de tool valido en el ecosistema | Tools que el skill invoca en su procedimiento |
| `knowledge` | list[string] | no | Cada elemento es un URN resoluble contra el catalogo KORA | Knowledge bases que el skill referencia |
| `composable_with` | list[string] | no | Cada elemento es un `name` de otro skill existente en `SKILLS/` | Composiciones verificadas por el autor |
| `domain` | list[string] | no | Cada elemento es un identificador kebab-case de dominio | Dominios tematicos del skill |
| `level` | enum | no | Uno de: `L0`, `L1`, `L2`, `L3` | Complejidad estructural del skill |

#### 3.2.2 Niveles de skill (level)

| Level | Semantica | Ejemplo |
| --- | --- | --- |
| `L0` | Skill atomico: un procedimiento, un dominio, sin dependencias inter-skill | `data-modeling` |
| `L1` | Skill compuesto simple: invoca o referencia 1-2 skills como paso de su procedimiento | Un skill de "full-stack audit" que llama a `ux-design` y luego `frontend-design` |
| `L2` | Skill orquestador: coordina multiples skills con logica de seleccion o branching | Un skill de "architecture review" que selecciona sub-skills segun contexto |
| `L3` | Skill meta-generativo: produce o transforma otros skills como output | Un skill de "skill-forge" que genera `SKILL.md` conformantes |

Si `level` se omite, el default implicito es `L0`.

#### 3.2.3 Relacion entre `allowed-tools` y `tools`

- `allowed-tools` (campo agentskills.io): declara al runtime que tools necesita el skill. Es lo que el runtime lee para conceder permisos.
- `metadata.kora.tools` (campo overlay): declara al ecosistema KORA que tools invoca el skill. Es lo que el validador KORA lee para verificar coherencia con el workspace agente.

Regla de coherencia: `metadata.kora.tools` **DEBE** ser subconjunto de `allowed-tools` (si ambos estan presentes). Un skill no puede invocar tools que no ha declarado al runtime. Enforcement: lint.

### 3.3 Body: CM Core

El body del `SKILL.md` (despues del frontmatter) contiene el CM Core. Este bloque **DEBE** seguir la grammar canonica definida por `skill-spec-md`:

#### 3.3.1 Secciones obligatorias

| Seccion | Heading (espanol) | Heading (ingles) | Contenido |
| --- | --- | --- | --- |
| 1 | `## Proposito` | `## Purpose` | Que hace el skill y por que existe. Declaracion concisa de funcion y razon de ser. |
| 2 | `## Input/Output` | `## Input/Output` | Que recibe como entrada (tipo, formato, restricciones) y que produce como salida (tipo, formato, garantias). |
| 3 | `## Procedimiento` | `## Procedure` | Pasos ejecutables que el agente sigue. Cada paso es una instruccion clara, no prosa narrativa. |
| 4 | `## Signature Output` | `## Signature Output` | Template del output producido. Puede ser markdown, YAML, codigo, o cualquier formato declarado en Input/Output. |

Se aceptan ambos idiomas. Un skill **DEBE** usar consistentemente un idioma en todas sus secciones obligatorias.

#### 3.3.2 Secciones opcionales

| Seccion | Heading | Contenido |
| --- | --- | --- |
| `## Examples` / `## Ejemplos` | Ejemplos concretos de uso con input y output esperado |
| `## Edge Cases` / `## Casos Borde` | Situaciones limites y como manejarlas |
| `## References` / `## Referencias` | Documentos, URLs, URNs de conocimiento relevante |
| `## Constraints` / `## Restricciones` | Limites de aplicabilidad, precondiciones, supuestos |
| `## When to Use This Skill` / `## Cuando Usar` | Triggers para activacion. Recomendado para discovery. |
| `## Related Skills` / `## Skills Relacionados` | Skills complementarios (advisory, no vinculante) |

#### 3.3.3 Contenido prohibido en el CM Core

Conforme a `skill-spec-md §3.3`, el CM Core **NO DEBE** contener:

| Patron prohibido | Razon |
| --- | --- |
| Variables de estado FSM | El skill no controla transiciones del agente |
| Clasificaciones de transicion (`END`, `DISPATCH`) | El routing es materia del agente, no del skill |
| Instrucciones de continuidad multi-turno | El contexto conversacional es materia del agente |
| Orquestacion de fases del agente | La FSM es materia de `AGENTS.md` |
| Logica de seguridad (permisos, sandbox) | La seguridad es materia de `config.json` |
| Relajacion de reglas duras del agente | Las reglas duras solo se modifican en su fuente |
| Outputs que codifican destinos FSM | El skill produce resultados, no routing |

El CM Core **PUEDE** contener logica de dominio compleja, heuristicas, tablas de decision, y procedimientos multi-paso. Lo que no puede hacer es ejercer control sobre el agente que lo ejecuta.

## 4. Composicion de skills

### 4.1 Modelo categorial

Los skills componen como morfismos en una categoria Kleisli. Cada skill `s` es un morfismo:

```
s: A -> T(B)
```

donde `A` es el tipo de input, `B` es el tipo de output, y `T` es la monada de contexto que encapsula efectos (herramientas invocadas, conocimiento referenciado, estado parcial).

### 4.2 Composicion secuencial

Dados dos skills `s: A -> T(B)` y `t: B -> T(C)`, la composicion secuencial `s >> t` se define como:

```
(s >> t)(a) = s(a) >>= t
```

Precondicion: el `Output` de `s` **DEBE** ser compatible con el `Input` de `t`. La compatibilidad se verifica por:

1. **Tipo**: el formato de output de `s` (markdown, YAML, codigo, etc.) coincide con el formato de input esperado por `t`.
2. **Semantica**: la informacion que `s` produce es suficiente para que `t` opere.

La compatibilidad es advisory — el campo `composable_with` la declara, pero no la enforcea en runtime.

### 4.3 Composicion paralela

Dados dos skills `s: A -> T(B)` y `t: C -> T(D)` con contextos independientes, la composicion paralela `s (x) t` produce:

```
(s (x) t)(a, c) = (s(a), t(c))
```

Precondicion: los contextos de `s` y `t` **DEBEN** ser independientes — no comparten estado mutable ni tools con efectos laterales conflictivos.

### 4.4 Leyes de composicion

| Ley | Enunciado | Implicacion practica |
| --- | --- | --- |
| Asociatividad | `(s >> t) >> u = s >> (t >> u)` | El orden de agrupacion no importa en pipelines |
| Identidad izquierda | `id >> s = s` | Un skill identidad no altera el pipeline |
| Identidad derecha | `s >> id = s` | Un skill identidad al final es no-op |
| Interchange (tensor) | `(s >> t) (x) (u >> v) = (s (x) u) >> (t (x) v)` | Pipelines paralelos pueden entrelazarse con pipelines secuenciales |

### 4.5 Campo `composable_with`

El campo `metadata.kora.composable_with` es **advisory**: declara composiciones que el autor ha verificado, pero no restringe composiciones no declaradas.

Reglas:

1. Cada entrada **DEBE** ser el `name` de un skill existente en `SKILLS/`.
2. La composicion declarada **DEBERIA** haberse probado al menos una vez.
3. La ausencia de un skill en `composable_with` no implica incompatibilidad — solo ausencia de verificacion.
4. `composable_with` es simetrica en intencion: si `s` declara composabilidad con `t`, `t` **DEBERIA** declarar composabilidad con `s`.

Traces to: formal/02 §4.3 (Promotion preserves CMCore) ; formal/03 §2 (2-categorical structure)

## 5. Subsumision por agentes

### 5.1 El agente como ceiling

Un agente subsume un skill cuando el skill puede ejecutarse dentro del envelope del agente. La subsumision se verifica por cuatro dimensiones:

| Dimension | Condicion de subsumision | Fuente del agente | Fuente del skill |
| --- | --- | --- | --- |
| Tools | `skill.metadata.kora.tools` ⊆ `agent.config.tools.allow` | `config.json` | `metadata.kora.tools` |
| Knowledge | `skill.metadata.kora.knowledge` ⊆ `agent.config.allowed_kb` | `config.json` | `metadata.kora.knowledge` |
| Behavior | `agent.hard_rules` > `agent.co_induction` > `skill.procedure` | `AGENTS.md` §2, §3 | CM Core §3 |
| Domain | `skill.metadata.kora.domain` ⊆ `agent.coalgebra.domain` | `AGENTS.md` §2 (Reglas Duras: Allowed) | `metadata.kora.domain` |

Reglas de subsumision:

1. Si un skill declara `tools` no presentes en `config.json.tools.allow` del agente, el skill **NO DEBE** activarse. Enforcement: runtime.
2. Si un skill referencia `knowledge` no presente en `config.json.allowed_kb` del agente, las referencias son irresolubles. Enforcement: lint (WARN).
3. Las reglas duras del agente **SIEMPRE** prevalecen sobre el procedimiento del skill. Un skill no puede relajar, condicionar ni reinterpretar reglas duras. Enforcement: manual.
4. Si un skill declara `domain` fuera del scope del agente (declarado en Reglas Duras: Allowed/Forbidden), el agente **DEBE** rechazar la activacion. Enforcement: runtime.

### 5.2 Progressive disclosure

La activacion de un skill por un agente sigue cuatro fases de revelacion progresiva:

| Fase | Que se expone | Costo estimado (tokens) | Cuando |
| --- | --- | --- | --- |
| **Discover** | `name` + `description` del frontmatter | ~50-100 tok | Al iniciar sesion o al recibir input ambiguo |
| **Match** | `metadata.kora.domain` + `metadata.kora.level` + heading `When to Use` | ~100-200 tok | Cuando el input coincide con un dominio/trigger |
| **Activate** | CM Core completo (4 secciones obligatorias) | ~500-2000 tok | Cuando el agente decide ejecutar el skill |
| **Execute** | `scripts/`, `references/`, `assets/` si el skill es extendido | variable | Cuando el procedimiento lo requiere |

Reglas:

1. Discover **NO DEBE** cargar el body del skill. Solo frontmatter.
2. Match **NO DEBE** cargar el CM Core completo. Solo metadata clasificatoria y seccion de trigger.
3. Activate **DEBE** cargar el CM Core completo y verificar subsumision antes de ejecutar.
4. Execute **PUEDE** cargar fibras adjuntas del skill extendido, pero **NO DEBE** alterar `AGENTS.md`, `TOOLS.md` ni `config.json` del agente.
5. Un skill que falla subsumision en Activate **DEBE** ser descartado con motivo, no ejecutado parcialmente.

Traces to: formal/04 §2.4 (Filtered Discovery) ; formal/04 §5 (Progressive Disclosure)

## 6. Lifecycle

### 6.1 Estados

| Estado | Semantica | Transiciones validas |
| --- | --- | --- |
| `draft` | Skill en desarrollo. No disponible para discovery por agentes `active`. | `draft -> active`, `draft -> retired` |
| `active` | Skill operativo, auditado, disponible para discovery y ejecucion. | `active -> deprecated`, `active -> retired` |
| `deprecated` | En desuso planificado. Los agentes que lo referencian **DEBEN** migrar. | `deprecated -> retired`, `deprecated -> active` (si se revierte la decision) |
| `retired` | Eliminado del ecosistema. Las referencias **DEBEN** limpiarse. | Terminal (sin transiciones de salida) |

### 6.2 Reglas de lifecycle

1. Un skill nuevo **DEBE** comenzar en `draft`.
2. La transicion `draft -> active` **DEBE** pasar validacion completa (§8).
3. Un agente `active` **NO DEBE** referenciar un skill `retired`. Enforcement: lint.
4. Un agente `active` **PUEDE** referenciar un skill `deprecated` pero **DEBERIA** planificar migracion. Enforcement: lint (WARN).
5. La fecha `lifecycle.updated` **DEBE** actualizarse en cada transicion de estado.
6. La transicion `deprecated -> retired` **DEBE** ejecutar: eliminacion de references en agentes consumidores, ejecucion de `kora index`.

### 6.3 Versionado

El versionado del skill sigue semver y se refleja en dos lugares:

- **URN**: `urn:{ns}:skill:{id}` (identidad estable, no porta version).
- **Frontmatter del directorio o archivo que contiene el skill**: se versiona por changelog en `## Version History` dentro del body (opcional).

La version del overlay no se porta en la URN. La version del contenido del skill se gestiona por el autor en el body.

## 7. Ubicacion

### 7.1 Regla de ubicacion

**TODOS** los skills viven en `SKILLS/`. No hay skills dentro de `AGENTS/`.

```text
SKILLS/
  data-modeling/
    SKILL.md
  ux-design/
    SKILL.md
    references/        # opcional
  graphic-design/
    SKILL.md
  arquitecto-categorico/
    SKILL.md
```

### 7.2 Referencia desde agentes

El agente referencia skills en su campo `skills` dentro de `config.json`:

```json
{
  "skills": [
    { "id": "data-modeling", "required": true },
    { "id": "ux-design", "required": false }
  ]
}
```

| Campo | Tipo | Semantica |
| --- | --- | --- |
| `id` | string | Coincide con el `name` del skill (= nombre del directorio en `SKILLS/`) |
| `required` | boolean | `true` = constitutivo (el agente no puede operar sin este skill). `false` = aditivo (capacidad opcional, activada bajo demanda) |

### 7.3 Relacion con skills legacy en AGENTS/

Los skills que aun viven en `AGENTS/*/skills/` son formato legacy. Esta spec define la ubicacion canonica en `SKILLS/`. La migracion se describe en §10.

## 8. Validacion

| # | Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- | --- |
| V1 | Frontmatter agentskills.io | `name` y `description` presentes y conformes a restricciones §3.1 | lint | Corregir frontmatter |
| V2 | Naming consistency | `name` en frontmatter = nombre del directorio padre | lint | Renombrar directorio o corregir `name` |
| V3 | CM Core completo | Body contiene las 4 secciones obligatorias (§3.3.1) | lint | Agregar secciones faltantes |
| V4 | Overlay KORA presente | `metadata.kora` existe con `urn`, `lifecycle.status`, `lifecycle.created`, `lifecycle.updated` | lint | Agregar overlay |
| V5 | URN valida | `metadata.kora.urn` sigue formato `urn:{ns}:skill:{id}` | lint | Corregir URN |
| V6 | Lifecycle coherente | `status` es uno de los 4 valores validos; `updated` >= `created` | lint | Corregir fechas o status |
| V7 | Tools coherentes | `metadata.kora.tools` ⊆ `allowed-tools` (si ambos presentes) | lint | Alinear tools |
| V8 | Knowledge resoluble | Cada URN en `metadata.kora.knowledge` resuelve contra catalogo | lint | Corregir URN o eliminar entrada |
| V9 | Composable resoluble | Cada entrada en `composable_with` corresponde a un skill existente en `SKILLS/` | lint | Corregir referencia o eliminar entrada |
| V10 | No control conversacional | CM Core no contiene patrones prohibidos de §3.3.3 | lint/manual | Extraer leakage al agente |
| V11 | Idioma consistente | Secciones obligatorias usan un solo idioma (todas en espanol o todas en ingles) | lint | Unificar idioma |
| V12 | Level valido | Si `metadata.kora.level` presente, es uno de `L0`, `L1`, `L2`, `L3` | lint | Corregir valor |
| V13 | Domain kebab-case | Cada entrada en `metadata.kora.domain` usa kebab-case | lint | Corregir formato |

## 9. Ejemplo completo

### 9.1 Skill con overlay KORA: `data-modeling`

```yaml
---
name: data-modeling
description: >-
  Data modeling with Entity-Relationship Diagrams (ERDs), data dictionaries,
  and conceptual/logical/physical models. Documents data structures,
  relationships, and attributes.
license: MIT
allowed-tools: Read Glob Grep
metadata:
  kora:
    urn: "urn:kora:skill:data-modeling"
    lifecycle:
      status: active
      created: "2025-12-26"
      updated: "2026-04-14"
    tools: ["Read", "Glob", "Grep"]
    knowledge:
      - "urn:kora:kb:md-spec"
    composable_with:
      - "ux-design"
    domain:
      - "data-architecture"
      - "database-design"
    level: L0
---

## Purpose

Create and document data structures using Entity-Relationship Diagrams (ERDs),
data dictionaries, and structured data models. Supports conceptual, logical,
and physical modeling levels for database design and data architecture.

## Input/Output

**Input:**
- Business requirements describing entities, relationships, and data rules
- Existing schema or ERD to audit/extend
- Target database platform (optional, for physical model)

**Output:**
- ERD in Mermaid syntax
- Data dictionary in markdown tables
- Structured data model in YAML
- Narrative summary of the model

## Procedure

1. EXTRACT entities from requirements (nouns that the business tracks).
2. FILTER candidates: keep independent concepts with multiple instances; exclude attributes, synonyms, and verbs.
3. DEFINE attributes for each entity: identify keys (PK, FK, natural, surrogate), types, and constraints.
4. MAP relationships between entities: determine cardinality (1:1, 1:M, M:N) and participation (mandatory/optional).
5. RESOLVE M:N relationships via associative entities.
6. NORMALIZE to 3NF for logical model; denormalize only with explicit trade-off justification.
7. MAP to physical types if target platform is specified.
8. PRODUCE outputs in the formats declared above.

## Signature Output

```markdown
## Data Model: {name}

**Version:** {version}
**Level:** {conceptual|logical|physical}

### ERD

{mermaid erDiagram block}

### Data Dictionary

{table per entity: Column | Type | Null | Key | Default | Description}

### Relationships

{table: Relationship | From | To | Cardinality | Description}

### Notes

{trade-offs, denormalization decisions, partitioning recommendations}
```

## Examples

**Input:** "We need to track patients, their appointments with doctors, and the prescriptions generated from each appointment."

**Output summary:**
- Entities: Patient, Doctor, Appointment, Prescription
- Relationships: Patient 1:M Appointment, Doctor 1:M Appointment, Appointment 1:M Prescription
- Keys: patient_id (PK), doctor_id (PK), appointment_id (PK), prescription_id (PK)

## Related Skills

- `ux-design` — for interfaces that expose the data model
- `arquitecto-categorico` — for formal modeling of data relationships

## Version History

- **v1.0.0** (2025-12-26): Initial release
- **v1.1.0** (2026-04-14): Added KORA overlay metadata
```

### 9.2 Skill minimo valido (solo campos obligatorios)

```yaml
---
name: mi-skill
description: "Descripcion breve del skill."
metadata:
  kora:
    urn: "urn:mi-ns:skill:mi-skill"
    lifecycle:
      status: draft
      created: "2026-04-14"
      updated: "2026-04-14"
---

## Proposito

{que hace y por que}

## Input/Output

**Input:** {que recibe}
**Output:** {que produce}

## Procedimiento

1. {paso 1}
2. {paso 2}

## Signature Output

{template del output}
```

## 10. Migracion desde formato legacy

### 10.1 Skills legacy KORA (con `_manifest`)

Los skills legacy KORA usan `_manifest.urn` y `_manifest.type` en el frontmatter. La migracion a formato agentskills.io + overlay es:

| Campo legacy | Campo nuevo | Transformacion |
| --- | --- | --- |
| `_manifest.urn` | `metadata.kora.urn` | Copiar URN; si es `urn:{ns}:skill:{id}:{version}`, eliminar el segmento `:{version}` |
| `_manifest.type` | `metadata.kora.level` | `lazy_load_endofunctor` -> `L0` (default) |
| `_manifest.provenance.created_at` | `metadata.kora.lifecycle.created` | Copiar fecha |
| `status` (campo raiz) | `metadata.kora.lifecycle.status` | Copiar valor |
| Nombre archivo `CM-SCREAMING_CASE.md` | `name` en frontmatter | Convertir a kebab-case: `CM-DATA-MODELING` -> `data-modeling` |
| Titulo `# CM-SCREAMING_CASE` | Titulo descriptivo | `# CM-DATA-MODELING` -> `# Data Modeling` |
| `## Proposito` | `## Proposito` o `## Purpose` | Sin cambio (grammar CM Core se preserva) |

### 10.2 Skills en `AGENTS/*/skills/`

Los skills que viven dentro de directorios de agentes se mueven a `SKILLS/`:

```
ANTES: AGENTS/meta-kora/curador/skills/CM-LINT-MD.md
DESPUES: SKILLS/lint-md/SKILL.md
```

Pasos:

1. Crear directorio `SKILLS/{nombre-kebab}/`.
2. Copiar contenido a `SKILL.md` con frontmatter agentskills.io + overlay.
3. Actualizar `name` a kebab-case.
4. Agregar `metadata.kora` con URN y lifecycle.
5. Actualizar referencia en `config.json` del agente (campo `skills`).
6. Eliminar archivo original en `AGENTS/`.
7. Ejecutar `python3 scripts/kora index`.

### 10.3 Skills agentskills.io puros (sin overlay)

Un skill agentskills.io sin overlay KORA es valido para ejecucion por runtimes agentskills.io, pero **NO** participa en la gobernanza KORA (no tiene identidad URN, no tiene lifecycle, no es validable por la toolchain).

Para incorporarlo al ecosistema KORA:

1. Agregar `metadata.kora` al frontmatter existente.
2. Asignar URN, lifecycle y clasificacion.
3. Ejecutar validacion (§8).

El body (CM Core) no requiere modificacion si ya sigue la grammar de 4 secciones.

## 11. Precedencia

### 11.1 Relacion con `skill-spec-md`

Esta spec **complementa** `skill-spec-md` — no la reemplaza.

| Materia | Spec gobernante |
| --- | --- |
| Grammar del CM Core (4 secciones obligatorias) | `skill-spec-md` |
| Algebra `Free/Forget/Promote` | `skill-spec-md` |
| Patrones prohibidos en CM Core | `skill-spec-md` |
| Progressive disclosure (ciclo Discover/Activate/Execute) | `skill-spec-md` (define el ciclo), esta spec (define el overlay que lo habilita) |
| Formato del frontmatter agentskills.io | agentskills.io spec (externa) |
| Overlay `metadata.kora.*` | **esta spec** |
| Composicion categorial de skills | **esta spec** |
| Subsumision por agentes | **esta spec** |
| Lifecycle del overlay | **esta spec** |
| Ubicacion canonica (`SKILLS/`) | **esta spec** |
| Validacion del overlay | **esta spec** |
| Migracion legacy -> agentskills.io | **esta spec** |

### 11.2 Relacion con `agent-spec-md`

`agent-spec-md` gobierna la topologia del workspace agente y como este referencia skills. Esta spec gobierna el skill como artefacto independiente y portable.

Cuando un agente subsume un skill, `agent-spec-md §7` (Skills) y esta spec §5 (Subsumision) aplican conjuntamente.

### 11.3 Relacion con `gobernanza`

La identidad URN del overlay sigue las reglas de `gobernanza §3`. Los niveles de enforcement de esta spec son conformes a `gobernanza §4`.

Traces to: formal/02 §2.3 (Unit eta) ; formal/02 §2.4 (Counit epsilon) ; formal/04 §2.4 (Filtered Discovery) ; formal/05 §1.2 (Bounded Lattice)

## 12. Contrato vigente v1

- Skills viven en `SKILLS/` como directorios con `SKILL.md` agentskills.io-compatible.
- El overlay KORA vive en `metadata.kora` — nunca fuera de `metadata`.
- Campos obligatorios del overlay: `urn`, `lifecycle.status`, `lifecycle.created`, `lifecycle.updated`.
- CM Core: 4 secciones obligatorias, sin control conversacional.
- Composicion: Kleisli, `composable_with` advisory.
- Subsumision: tools ⊆ allow, knowledge ⊆ allowed_kb, hard_rules > procedure, domain ⊆ allowed.
- Progressive disclosure: Discover (frontmatter) -> Match (metadata+trigger) -> Activate (CM Core) -> Execute (fibras).
- Lifecycle: `draft -> active -> deprecated -> retired`.
- Isomorfismo fluido: borrar `metadata.kora.*` produce un skill agentskills.io valido.

Toda futura transicion major **DEBE** documentar en esta seccion: (1) que cambio, (2) que migrar, y (3) que se depreca.

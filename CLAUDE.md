# CLAUDE.md

Fuente operativa unica para agentes que trabajen en este repositorio. Si otra
guia, handoff, README externo, memoria vieja o wrapper legacy contradice este
archivo, la CLI viva y las specs vigentes mandan; este archivo solo resume como
operar sin volver a inferir el repo desde cero.

## Que Es KORA

KORA es el **repositorio, catalogo y sistema de produccion y mantenimiento de
artefactos** que consumen o ejecutan sistemas LLM. Produce esos artefactos por
un pipeline gobernado, los cataloga y resuelve por URN, los mantiene coherentes
en el tiempo (checks, lifecycle, deprecacion) y proyecta los ejecutables a
runtimes. No es una aplicacion tradicional: el activo principal es la
consistencia entre ley, ontologia, serializacion, runtimes, artefactos y
toolchain.

Gestiona **tres tipos de artefacto, y solo tres**:

- **conocimiento** — archivos `.md` en estandar KORA/MD para *consumo* de
  sistemas LLM (se leen como contexto, no se ejecutan).
- **agentes** (`AGENT.md`) y **skills** (`SKILL.md`) — definen actores y
  capacidades que se *proyectan a runtimes* (`claude-code`, `codex`,
  `openclaw`, `hermes`) via transmutacion.

Las **specs** no son artefactos: son la ley que define que cuenta como
artefacto valido. "Conocimiento" es un tipo especifico, nunca paraguas de los
otros dos.

Principio rector vigente (garantia formal, no definicion):

```text
KORA = vector ontologico PMI x LFS + shape unificado de autoria + transmutacion funtorial
```

El filesystem con manifests validos es la fuente de verdad. Las vistas en
`docs/generated/` son derivadas y regenerables.

## Identidad Operacional Por Host

KORA distingue **host primary** y **hosts secondary**:

- `primary`: SSOT operacional; unico autorizado para pushear a `origin/master`.
- `secondary`: replica read-mostly; trabaja en ramas feature y propone cambios
  via PR.

Reglas:

- Verificar rol local con `python3 toolchain/kora host`.
- Marker local fuera del repo: `~/.kora/host.yml`.
- Default si el marker no existe: `secondary`.
- Hooks locales: `python3 toolchain/kora install-hooks`.
- Host primary canonico al `2026-05-03`: `hetzner2897261`.
- `master` en GitHub esta protegida: no force-push, no delete, linear history.

## Canon Y Precedencia

Cuando dos fuentes parezcan contradecirse, aplica esta precedencia:

1. `governance/gobernanza.md`
2. `ontology/harness-spec.md`
3. `serialization/autoria-spec.md`, `serialization/md-spec.md`,
   `serialization/knowledge-spec.md`
4. `runtime/runtime-spec-md.md`, `runtime/transmutation-spec.md`,
   `runtime/multiagente-spec.md`, `runtime/*-runtime-extension.md`
5. extensiones y artefactos de namespace
6. docs auxiliares, handoffs, planes, memorias y wrappers

Specs clave:

- `governance/gobernanza.md`: constitucion, identidad, precedencia, lifecycle,
  host roles, runtimes canonicos y decisiones HITL.
- `ontology/harness-spec.md`: ontologia PMI x LFS. Sigue en freeze formal.
- `serialization/autoria-spec.md`: shape unificado para agentes y skills.
- `serialization/agent-skill-construction-spec.md`: metodologia de construccion
  pre-transmutacion.
- `serialization/md-spec.md` y `serialization/knowledge-spec.md`: KORA/MD,
  knowledge y tejido relacional.
- `runtime/transmutation-spec.md` y runtime extensions: proyeccion IR -> target.

## Topologia Actual

| Capa | Path | Rol |
|------|------|-----|
| Constitucion | `governance/` | Reglas meta, precedencia y decisiones archivadas vivas |
| Ontologia | `ontology/` | PMI x LFS, calidad, procesos y riesgo |
| Serializacion | `serialization/` | Shapes de authoring, KORA/MD y schemas |
| Runtime | `runtime/` | Transmutacion, multiagente y runtime extensions canonicas |
| Knowledge | `artifacts/knowledge/` | KORA/MD publicado + staging `_SCRIPTORIUM/` |
| Agentes | `artifacts/agents/` | `AGENT.md` productivos + staging `_FRAGUA/` |
| Skills | `artifacts/skills/` | `SKILL.md` productivas + staging `_TALLER/` |
| Toolchain | `toolchain/kora`, `toolchain/kora_lib/` | CLI Python soportada |
| Tests | `tests/` | Verificacion ejecutable |
| Docs auxiliares | `docs/` | Handoffs vivos, planes y salidas derivadas |

Pipelines activos:

```text
artifacts/knowledge/_SCRIPTORIUM/INBOX/ -> REVIEW/ -> artifacts/knowledge/{ns}/...
artifacts/agents/_FRAGUA/INBOX/         -> REVIEW/ -> artifacts/agents/{ns}/{name}/
artifacts/skills/_TALLER/INBOX/         -> REVIEW/ -> artifacts/skills/{ns}/{name}/
```

Los directorios de staging son pre-categoriales. No representan namespace
canonico hasta promocion.

`_SCRIPTORIUM/INBOX/` no es bodega versionada. El material crudo de ingesta
(PDF, DOCX, JSON dumps, TXT fuente, OCR, corpus externos) debe vivir fuera del
repo y quedar representado por inventarios con hash/procedencia. En git solo
deben entrar README, inventarios y material ya normalizado hacia REVIEW o
productivo.

## Historia Relevante

Antes del `2026-04-18`, el repo usaba la topologia legacy `specs/`, `AGENTS/`,
`SKILLS/`, `KNOWLEDGE/`, `schemas/` y `scripts/`. La reorg v5 movio esa
estructura a capas explicitas y a `artifacts/` + `toolchain/`.

Mapa de traduccion:

| Legacy | Actual |
|--------|--------|
| `specs/` | `governance/`, `ontology/`, `serialization/`, `runtime/` |
| `KNOWLEDGE/` | `artifacts/knowledge/` |
| `AGENTS/` | `artifacts/agents/` |
| `SKILLS/` | `artifacts/skills/` |
| `schemas/` | `serialization/schemas/` |
| `scripts/` | `toolchain/` |
| `catalog/catalog_master_kora.yml` | `docs/generated/catalog.yml` |

Si encuentras referencias legacy en planes archivados, fuentes importadas o
helpers de compatibilidad, tratalas como contexto historico, no como topologia
vigente.

## Modelo Actual De Artefactos

No asumas el workspace legacy de cinco archivos (`AGENTS.md`, `TOOLS.md`,
`SOUL.md`, `USER.md`, `config.json`) como forma canonica productiva.

La unidad productiva principal es:

- `AGENT.md` para agentes en `artifacts/agents/{ns}/{name}/`
- `SKILL.md` para skills en `artifacts/skills/{ns}/{name}/`

Ambos siguen `serialization/autoria-spec.md`:

- `_manifest.urn` sin version embebida.
- `version` fuera del URN.
- `extensions.kora.vector_ontologico` como IR canonico.
- `extensions.kora.atlas.forma_material` como discriminante material.
- payload bajo `artefacto:`.

Fibras adjuntas posibles: `skills/`, `memoria/`, `MEMORY.md`, `_BUILD/`,
`scripts/`, `referencias/`, `recursos/`. Antes de editar, inspecciona el
directorio concreto.

## Formal Layer

- La unica Formal Layer oficial es
  `artifacts/knowledge/kora/categorical-foundations/`.
- `artifacts/knowledge/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo puede apuntar a documentos de la Formal Layer oficial.
- Si una idea viene de `fxsl/cat` y no ha sido absorbida formalmente, usala
  como `Rationale:` o apoyo editorial, no como traza oficial.

## Reconstruccion Meta-KORA

Decision vigente al `2026-05-03`: el stack meta-KORA historico debe reconstruirse
desde cero. No uses `kora/custodio`, `kora/guardian`, `kora/clawforge`,
curator/forgemaster ni las skills historicas `artifact-curator`,
`curation-conductor`, `knowledge-curator`, `kora-agents` o `kora-skills` como
fuente de diseno, runtime, blueprint, transmutacion ni prompt operativo.

Fuente canonica:

- `artifacts/knowledge/kora/sys/meta-kora-rebuild-directive.md`
- `urn:kora:kb:meta-kora-rebuild-directive`

Para nueva generacion meta-KORA: partir de specs vigentes, declarar requisitos,
crear IR fresco en staging y transmutar solo despues de canonizar la fuente.

## Runtimes

Runtimes canonicos activos segun `gobernanza` v6.0:

- `claude-code`
- `codex`
- `openclaw`
- `hermes`

`hermes` es canonico desde el `2026-05-20`, pero
`runtime/hermes-runtime-extension.md` esta en v0.1.0 stub: sus transmutaciones
son experimentales hasta completar Fase 2b.

Runtimes archivados en pausa:

- `agentskills`
- `gemini`
- `mastra`
- `opencode`

Sus URNs siguen resolviendo en
`governance/decisiones-archivadas/specs-en-pausa/`, pero no son target canonico
sin nuevo HITL + ADR. La CLI puede listarlos por compatibilidad; usarlos requiere
`--force-paused`.

Verifica targets vivos con:

```bash
python3 toolchain/kora transmute --help
```

## Toolchain CLI

Entrypoint soportado:

```bash
python3 toolchain/kora
```

Comandos utiles:

```bash
python3 toolchain/kora index
python3 toolchain/kora resolve "urn:kora:kb:harness-spec"
python3 toolchain/kora check --strict
python3 toolchain/kora check --list
python3 toolchain/kora host
python3 toolchain/kora install-hooks
python3 toolchain/kora health --strict
python3 toolchain/kora validate --profile strict
python3 toolchain/kora lint-md
python3 toolchain/kora stats --json
python3 toolchain/kora graph --json
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora transmute --help
python3 toolchain/kora ingest --help
python3 toolchain/kora sync-docs
```

Maintenance gate por defecto:

```bash
python3 toolchain/kora check --strict
```

Usa `health`, `validate`, `lint-md`, `migrate`, `promote` o `deprecate` cuando
necesites una fase puntual; no los trates como reemplazo de la gate unificada.

## Secuencia De Trabajo

Cuando cambies specs, toolchain, artefactos estructurales o docs operativas:

1. Aplica cambios minimos en la capa propietaria.
2. `python3 toolchain/kora index`
3. `python3 toolchain/kora check --strict`
4. `python3 -m unittest discover -s tests`
5. `python3 toolchain/kora kb-graph --json --orphans` si tocaste knowledge o
   relaciones.
6. `python3 toolchain/kora sync-docs` solo si quieres regenerar salidas publicas
   en `docs/generated/`.

Si la tarea requiere migracion explicita:

```bash
python3 toolchain/kora migrate --profile a-autoria
python3 toolchain/kora migrate --profile a-autoria --cohort meta-kora --dry-run
```

Si proyectas a runtime:

```bash
python3 toolchain/kora transmute --target claude-code --agent dev/steipete --dry-run
python3 toolchain/kora transmute --target codex --agent dev/steipete --dry-run
python3 toolchain/kora transmute --target openclaw --agent salud/salubrista --dry-run
python3 toolchain/kora transmute --target hermes --agent <ns>/<name> --dry-run
```

Para targets archivados, anade `--force-paused` y lee primero
la spec archivada correspondiente bajo
`governance/decisiones-archivadas/specs-en-pausa/`.

## Tests

Suite completa:

```bash
python3 -m unittest discover -s tests
```

Tests puntuales frecuentes:

```bash
python3 -m unittest tests.test_cli_smoke
python3 -m unittest tests.test_host_roles
python3 -m unittest tests.test_semantic_validation
python3 -m unittest tests.test_check_pipeline
```

`tests/common.py` modela la reorg v5, usa `docs/generated/` como raiz de
salidas materializadas y expone helpers de portabilidad como `canonical_path()`.

## Handoffs Y Docs

- Handoffs vivos: `docs/handoffs/YYYY-MM-DD-*.md`.
- Politica de handoffs: `docs/plans/2026-05-07-politica-handoffs.md`.
- Los handoffs historicos archivados fueron retirados; no son fuente de
  arranque ni autoridad operativa.
- `docs/start-prompt.md` es bootstrap copiable para sesiones nuevas.
- `docs/generated/*` es derivado; no escribas conteos a mano.

## Notas Practicas

- No asumas que `scripts/` raiz describe la toolchain viva; la toolchain viva
  esta en `toolchain/`.
- No hardcodees conteos de nodos, tests o checks en docs generales. Midelos con
  la CLI.
- No relajes specs para encubrir un artefacto mal formado.
- Un fallo de check puede ser artefacto invalido, check desalineado o spec
  incompleta; diagnostica antes de editar.
- Si corriges `artifacts/knowledge/fxsl/cat/`, hazlo para reducir ruido o
  preparar absorcion formal, no para darle autoridad normativa directa.
- Si corres `kb-graph`, `index` o `sync-docs`, revisa si se modifico
  `docs/generated/*` antes de mezclar esos cambios con otro objetivo.

## Portabilidad

Alcance operativo actual: Linux y macOS con Python >= 3.11.

Evidencia util:

- `toolchain/kora` corta con exit `2` si Python < 3.11.
- `check --list` incluye `portabilidad-tests`.
- `tests/common.py` normaliza paths canonicos para evitar falsos rojos entre
  macOS y Linux.

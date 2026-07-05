# CLAUDE.md

Fuente operativa unica para agentes que trabajen en este repositorio. Si otra
fuente (guia, handoff, README externo, memoria vieja o wrapper legacy)
contradice este archivo, mandan la CLI viva y las specs vigentes.

> **LEY CONGELADA (HITL 2026-06-14).** Esta encarnacion (la bestia) tiene su
> ley congelada: `governance/`, `ontology/`, `serialization/`, `runtime/` solo
> admiten correcciones de verdad, NO evolucion doctrinal. La **doctrina futura
> de KORA se autora en la encarnacion pneuma** (`~/kora-pneuma`, `ley/0..4`);
> todo artefacto agentico nuevo nace alli. La bestia sigue autoritativa para su
> corpus y unico realizador de `openclaw`/`hermes`. Regimen: `gobernanza` §0 +
> nota pneuma `regimen-de-ley`.

> **POSTA OPM CERRADA (2026-07-05).** Estrecha la excepcion "autoritativa para
> su corpus" de arriba: la **autoria OPM/Forja tambien queda CERRADA** en la
> bestia. La SSOT viva de doctrina OPM es `~/kora-pneuma`
> (`urn:fxsl:kb:reglas-opm-estrictas-es`, `urn:fxsl:kb:opm-es` y hermanos;
> skill `urn:kora:artefacto:modelamiento-opm`). El corpus
> `artifacts/knowledge/fxsl/opm/` y `artifacts/skills/kora/modelamiento-opm/`
> quedan congelados como referencia historica: solo correcciones de verdad,
> ninguna doctrina nueva. Todos los deltas previos al cierre fueron
> reconciliados a pneuma (9 KB al sync del 2026-06-16; delta final aa2e2f14
> `emitidoEn->generadoEl` absorbido el 2026-07-05; ver commits «posta OPM» en
> kora-pneuma). No migrados por decision HITL 2026-07-05, con razon:
> `manual-opforja-es(.md/--p02)` es manual de la app opforja/deep-opm-pro (su
> SSOT vive en `~/projects/deep-opm-pro/docs/manual-opforja.md`, no es ley OPM)
> y `opm-ssot-es/README.md` es orientacion local de este directorio.

## Que Es KORA

KORA es el **repositorio, catalogo y sistema de produccion y mantenimiento de
artefactos** que consumen o ejecutan sistemas LLM. Los produce por un pipeline
gobernado, los cataloga y resuelve por URN, los mantiene coherentes en el tiempo
(checks, lifecycle, deprecacion) y proyecta los ejecutables a runtimes.

Gestiona **tres tipos de artefacto, y solo tres**:

- **conocimiento** — `.md` en estandar KORA/MD para *consumo* de sistemas LLM
  (se leen como contexto, no se ejecutan).
- **agentes** (`AGENT.md`) y **skills** (`SKILL.md`) — actores y capacidades
  que se *proyectan a runtimes* via transmutacion.

Las **specs** no son artefactos: son la ley que define que cuenta como artefacto
valido. "Conocimiento" es un tipo especifico, nunca paraguas de los otros dos.

Principio rector (garantia formal, no definicion):

```text
KORA = vector ontologico PMI x LFS + shape unificado de autoria + transmutacion funtorial
```

El filesystem con manifests validos es la fuente de verdad. Las vistas en
`docs/generated/` son derivadas y regenerables.

## Bootstrap De Sesion

Al abrir una sesion nueva sobre este repo:

1. Lee este archivo (`CLAUDE.md`).
2. Lee `governance/gobernanza.md` cuando importe precedencia o politica.
3. Lee el ultimo handoff en `docs/handoffs/YYYY-MM-DD-*.md` por fecha
   descendente.
4. Verifica el rol del host local:

   ```bash
   python3 toolchain/kora host
   ```

5. Verifica estado antes de proponer o tocar nada:

   ```bash
   python3 toolchain/kora index
   python3 toolchain/kora check --strict
   ```

   Si `--strict` no pasa, diagnostica antes de avanzar; no normalices la deuda.

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
2. `ontology/harness-spec.md`, `ontology/qa-spec.md`
3. `serialization/autoria-spec.md`, `serialization/md-spec.md`,
   `serialization/spec-md.md`, `serialization/knowledge-spec.md`
4. `runtime/runtime-spec-md.md`, `runtime/transmutation-spec.md`,
   `runtime/multiagente-spec.md`, `runtime/*-runtime-extension.md`
5. extensiones y artefactos de namespace
6. docs auxiliares, handoffs, planes, memorias y wrappers

Specs clave:

| Spec | Alcance |
|------|---------|
| `governance/gobernanza.md` | Constitucion, identidad, precedencia, lifecycle, host roles, runtimes canonicos, decisiones HITL |
| `ontology/harness-spec.md` | Ontologia PMI x LFS (freeze formal) |
| `ontology/qa-spec.md` | Semantica de quality attributes y qa_budget |
| `serialization/autoria-spec.md` | Shape unificado para agentes y skills |
| `serialization/md-spec.md` | KORA/MD base (regimen descriptivo) |
| `serialization/spec-md.md` | Perfil prescriptivo (RFC 2119, Traces to) para specs |
| `serialization/knowledge-spec.md` | Knowledge |
| `runtime/transmutation-spec.md` | Proyeccion IR -> target |
| `runtime/*-runtime-extension.md` | Runtime extensions canonicas |

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

## Modelo Actual De Artefactos

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

No asumas el workspace legacy de cinco archivos (`AGENTS.md`, `TOOLS.md`,
`SOUL.md`, `USER.md`, `config.json`) como forma canonica productiva.

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

Runtimes canonicos activos segun `gobernanza` v7.0:

- `claude-code`
- `codex`
- `openclaw`
- `hermes`
- `opencode`

`hermes` es canonico desde el `2026-05-20`, pero
`runtime/hermes-runtime-extension.md` esta en v0.1.0 stub: sus transmutaciones
son experimentales hasta completar Fase 2b.

Runtimes archivados en pausa:

- `agentskills`
- `gemini`
- `mastra`

Sus URNs siguen resolviendo en
`governance/decisiones-archivadas/specs-en-pausa/`, pero no son target canonico
sin nuevo HITL + ADR. La CLI puede listarlos por compatibilidad; usarlos requiere
`--force-paused`.

Verifica targets vivos con:

```bash
python3 toolchain/kora transmute --help
```

## Skills Core

| URN | Cuando |
|-----|--------|
| `urn:kora:artefacto:mente-omega` | Razonamiento estructural-discursivo (pentamotor Phi/Psi/Xi/Delta/Sigma) |
| `urn:kora:artefacto:cat-thinking` | Enmarque categorial (24 piezas ICAS-BoK) |

## Personas Disponibles

| URN | Para |
|-----|------|
| `urn:dev:artefacto:steipete` | Direccion de ejecucion cognitiva |
| `urn:fxsl:artefacto:allan-kelly` | Arquitectura organizacional human-agent |

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

`toolchain/kora_lib/` contiene la implementacion viva. `toolchain/kora.bat` y
`toolchain/kora.ps1` son wrappers de conveniencia.

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

## Antipatrones

- Asumir topologia legacy (`KNOWLEDGE/`, `AGENTS/`, `SKILLS/`, `specs/`,
  `scripts/`): hoy es `artifacts/`, capas top-level y `toolchain/`.
- Editar `docs/generated/*` a mano: es derivado, regenerable con `kora index` /
  `kora sync-docs`.
- Promover knowledge sin pasar por REVIEW.
- Inventar URNs: resolver con `kora resolve <urn>` antes de citar.
- Saltar a runtime sin `AGENT.md` / `SKILL.md` conforme a autoria-spec.
- Asumir que `scripts/` raiz describe la toolchain viva; la toolchain viva esta
  en `toolchain/`.
- Hardcodear conteos de nodos, tests o checks en docs generales; medir con la
  CLI.
- Relajar specs para encubrir un artefacto mal formado.
- Correr `kb-graph`, `index` o `sync-docs` y mezclar cambios en `docs/generated/`
  con otro objetivo sin revisar.

## Portabilidad

Alcance operativo actual: Linux y macOS con Python >= 3.11.

- `toolchain/kora` corta con exit `2` si Python < 3.11.
- `check --list` incluye `portabilidad-tests`.
- `tests/common.py` normaliza paths canonicos para evitar falsos rojos entre
  macOS y Linux.

## Historia Relevante

Antes del `2026-04-18`, el repo usaba la topologia legacy. Mapa de traduccion:

| Legacy | Actual |
|--------|--------|
| `specs/` | `governance/`, `ontology/`, `serialization/`, `runtime/` |
| `KNOWLEDGE/` | `artifacts/knowledge/` |
| `AGENTS/` | `artifacts/agents/` |
| `SKILLS/` | `artifacts/skills/` |
| `schemas/` | `serialization/schemas/` |
| `scripts/` | `toolchain/` |
| `catalog/catalog_master_kora.yml` | `docs/generated/catalog.yml` |

Referencias legacy en planes archivados, fuentes importadas o helpers de
compatibilidad son contexto historico, no topologia vigente.

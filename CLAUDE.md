# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo gobernado por specs y soportado por una capa formal categorial.
No es un proyecto de aplicacion tradicional: el activo principal es la **consistencia
entre conocimiento, specs, workspaces y toolchain** — y desde v4.2, la separacion
estricta entre **ontologia**, **serializaciones**, **runtimes** y **distribucion**.

## Arquitectura en 4 capas (gobernanza v4.2)

| Capa | Qué gobierna | Specs |
|------|--------------|-------|
| **Ontologia** | Que *es* un artefacto agentico (espacio PMI × LFS) | `harness-spec` |
| **Serializacion** | Como se *escribe* (shapes de authoring) | `agentfile-spec v2`, `skill-overlay-spec v2`, `md-spec`, `knowledge-spec` |
| **Runtime** | Como se *ejecuta* y *proyecta* | `runtime-spec-md`, `transmutation-spec`, runtime-extensions |
| **Distribucion** | Como se *empaqueta* | `plugin.json`, `marketplace.json` (externas a KORA) |

**Principio**: KORA IR canoniza ontologia. Las serializaciones son proyecciones de
authoring. Los runtimes son fibras proyectadas con fidelidad declarada.

## Vector ontologico PMI × LFS

Cada artefacto productivo declara un vector de 6 ejes en
`extensions.kora.harness_vector`:

```yaml
harness_vector:
  pi:     0..3     # Plan (free monad) — 0=sin, 1=lineal, 2=ramificado, 3=fixed-points
  mu:     0..3     # Materia (cofree comonad) — 0=sin, 1=efimero, 2=persistente, 3=ambiental
  xi:     0..4     # Interaccion — 0=sin, 1=atomica, 2=lente, 3=coreografia, 4=operad dinamica
  lambda: 0..3     # Nivel sociotecnico — 0=individual, 1=org, 2=eco, 3=sociedad
  phi:    0..4     # Acoplamiento humano — 0=disjunto, 1=instrumental, 2=colaborativo, 3=hibrido, 4=co-evolutivo
  sigma:  [v1..v5] # Vector etico [safety, fairness, transparency, accountability, sustainability]
presentation: state-primary | action-primary
```

Ver `specs/harness-spec.md` para definiciones formales completas + 3 atlas (arneses
categoricos, formas materiales, metaforas HCAI Shneiderman).

## Topologia del repo (pipeline descentralizado v8)

Cada tipo de artefacto tiene staging **dentro de su directorio principal**.
`OPERATIONS/` fue eliminado.

| Capa | Path | Rol | Git |
|------|------|-----|-----|
| Specs (constitucion) | `specs/` | 11 specs (harness, agentfile v2, skill-overlay v2, transmutation, 4 runtime-extensions, gobernanza, md-spec, knowledge-spec) | tracked |
| Conocimiento productivo | `KNOWLEDGE/{ns}/...` | Artefactos KORA/MD publicados (11 ns) | tracked |
| Staging knowledge | `KNOWLEDGE/_SCRIPTORIUM/{INBOX,REVIEW}/` | Material crudo + drafts | tracked |
| Workspaces productivos | `AGENTS/{ns}/{name}/` | Agentes activos con `AGENT.md` v2 | tracked |
| Staging agentes | `AGENTS/_FRAGUA/{INBOX,REVIEW}/` | Agentes en elaboracion | tracked |
| Perfiles | `AGENTS/_FRAGUA/_perfiles/` | Specs de personalidad/input | tracked |
| Skills portables | `SKILLS/{name}/` o `SKILLS/{ns}/{name}/` | Skills productivos | tracked |
| Staging skills | `SKILLS/_TALLER/{INBOX,REVIEW}/` | Skills en elaboracion | tracked |
| Outputs transmutacion | `{workspace}/_BUILD/{target}/` | Derivados per-workspace | gitignored |
| Toolchain | `scripts/kora` | CLI Python | tracked |
| Schemas | `schemas/` | JSON Schemas (kora-agentfile v2, config, etc.) | tracked |

Pipelines locales:

```
KNOWLEDGE/_SCRIPTORIUM/INBOX/ → REVIEW/ → KNOWLEDGE/{ns}/...
AGENTS/_FRAGUA/INBOX/         → REVIEW/ → AGENTS/{ns}/{name}/
SKILLS/_TALLER/INBOX/         → REVIEW/ → SKILLS/{name}/
```

Los subdirs de `INBOX/` son **pre-categoriales**: no representan namespace KORA.
El namespace se asigna al promover a productivo.

## Runtimes target soportados

| Runtime | Dominio soportado | Runtime-extension |
|---------|--------------------|---------------------|
| Claude Code | Π≤2, Μ≤2, Ξ≤2, Λ≤1, Φ≤2 | `claude-code-runtime-extension v1.0` |
| Codex CLI | Π≤3, Μ≤1 (Μ=2 parcial via resume), Ξ≤2, Λ≤1, Φ≤2 | `codex-runtime-extension v1.0` |
| Gemini CLI | Π≤2, Μ≤1 (Μ=2 parcial), Ξ≤2, Λ≤1, Φ≤2 | `gemini-runtime-extension v1.0` |
| OpenClaw | Π≤3, Μ≤3, Ξ≤4, Λ≤3 (Λ=3 parcial), Φ≤3 | `openclaw-runtime-extension v1.1` |

**OpenClaw es el unico target con soporte nativo a arnés Servicio (Μ=3)** y es el
**meta-runtime via ACP** con 15 backends.

## Source of Truth

- El source of truth es el filesystem con manifests validos.
- `catalog/catalog_master_kora.yml` es vista materializada de `kora index`. No autoritativa.
- No escribas conteos a mano en docs. Usa `scripts/kora sync-docs`.
- No tomes README antiguos como autoridad si contradicen la CLI o las specs vigentes.

## Precedencia de specs

Segun `gobernanza v4.2 §3.1-3.4`:

1. **`gobernanza.md`** (v4.2 — constitucion, 3 regimenes URN, 4 capas).
2. **`harness-spec.md`** (v1.0 — ontologia canonica PMI × LFS).
3. **`md-spec.md`** (v7.1 — formato KORA/MD con 11 familias).
4. Specs canonicas de serializacion: `agentfile-spec v2`, `skill-overlay-spec v2`, `knowledge-spec v1.1`.
5. Specs de runtime: `runtime-spec-md v3.7`, `transmutation-spec v1.0`, runtime-extensions.
6. Extensiones de namespace.

Legacy: `agentfile-spec v2 §13` (workspace legacy 5-componentes), `skill-overlay-spec v2 §5.5` (CM-*), `runtime-spec §13` (outputs antiguos).

## Identidad URN (gobernanza §4.3)

Tres regimenes formales:

- **Conceptual** (`urn:{ns}:kb:{id}` + campo `version`): artefactos KORA/MD.
- **Agentfile** (`urn:{ns}:agent:{id}` + campo `version`): agentes modernos.
- **Ejecutable legacy** (`urn:{ns}:{kind}:{id}:{version}`): bootstrap + skills CM-*.

El `_manifest.type` es ortogonal al URN.

## Formal Layer

- La Formal Layer oficial es `KNOWLEDGE/kora/categorical-foundations/`.
- `KNOWLEDGE/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo apunta a Formal Layer oficial.

## Modelo del workspace v2

### Formato Agentfile v2 (preferido)

Un `AGENT.md` v2 tiene:

1. **Frontmatter YAML** con:
   - `_manifest.urn` (regimen Agentfile).
   - `extensions.kora.harness_vector` (vector ontologico, obligatorio).
   - `extensions.kora.atlas` (atlas A/B/C opcionales).
   - `extensions.{runtime}.*` (metadata runtime-especifica).
   - `agent.{profile, plan, interface, context, composition, invariants}` (shape de authoring).

2. **Body Markdown**: refinamiento legible que no contradice el frontmatter.

### Cambios clave v1 → v2

- Campo `coalgebra` (v1) → `profile` (descriptivo, no formal categorico).
- Objeto `fibers` (v1) **disuelto**: `memory`→`context.memory_config`+Μ, `operator`→`context.operator_profile`+Φ, `runtime`→`extensions.{runtime}.*`, `knowledge`→`extensions.kora.allowed_kb`, `identity`→atlas.
- Campo `safety` **bifurcado**: estructural (sub-coalgebra, derivable) vs Σ normativa (declarable).
- `harness_vector` obligatorio.

### Skills v2

Skills portables viven en `SKILLS/` con formato agentskills.io + overlay KORA.
Estructura interna: `scripts/`, `references/`, `assets/` (opcionales).
Seccion `## Resources` canonica en body si hay subdirs.
`extensions.kora.skill_freedom: high|medium|low` declara prescripcion.
Progressive disclosure (metadata/body/resources) como invariante.

Ver `skill-overlay-spec v2`.

### Familias documentales

`md-spec §5.6` define 11 familias: `spec`, `guide`, `normative`, `glossary`, `faq`, `catalog`, `cq_catalog`, `inventory`, `organigram`, `atomic`, `note`.

## Toolchain CLI

Entrypoint: `scripts/kora` (Python 3, deps en `requirements.txt`).

### Comandos

```bash
# CHECK UNIFICADO — pipeline composicional de mantencion
python3 scripts/kora check                       # todos los checks en orden topologico
python3 scripts/kora check --severity high       # solo critical + high
python3 scripts/kora check --fix                 # auto-apply fixes canonicos
python3 scripts/kora check --list                # listar checks registrados
python3 scripts/kora check --strict              # exit 1 si hay fallos

# Indexar catalogo (siempre antes de check/stats)
python3 scripts/kora index

# Resolver URN a path
python3 scripts/kora resolve "urn:kora:kb:harness-spec"

# Stats y grafo
python3 scripts/kora stats --json
python3 scripts/kora graph --json

# Transmutacion IR → runtime (con matriz de preservacion PMI × LFS)
python3 scripts/kora transmute --target claude-code --agent kora/curator
python3 scripts/kora transmute --target openclaw --agent gn/goreologo
python3 scripts/kora transmute --target codex --agent X/Y --dry-run
python3 scripts/kora transmute --target gemini --agent X/Y --dry-run
# Emite {workspace}/_BUILD/{target}/_transmutation.yml con source_vector,
# structural_preservation, projections por eje con fidelity/loss, bisimulation_claim.

# Ingesta inversa Lift_R — eleva artefacto runtime foraneo a KORA IR
python3 scripts/kora ingest --from claude-code --file ~/.claude/agents/polymath.md
python3 scripts/kora ingest --from codex --file ~/.codex/skills/X/SKILL.md
python3 scripts/kora ingest --from gemini --file path/SKILL.md
python3 scripts/kora ingest --from openclaw --workspace ~/openclaw-fleet/workspaces/X
# Genera AGENT.md v2 (agentes) o SKILL.md (skills) en staging con harness_vector
# auto-derivado + campos TODO para revision humana.

# Migracion v1 → v2 de agentfile (auto-derivar harness_vector)
python3 scripts/kora migrate --profile v2-agentfile
python3 scripts/kora migrate --profile v2-agentfile --cohort meta-kora --dry-run

# Migracion transitional (codemods legacy generales)
python3 scripts/kora migrate --profile transitional

# Reporte de staging (FRAGUA + TALLER + SCRIPTORIUM)
python3 scripts/kora intake

# Grafo de conocimiento
python3 scripts/kora kb-graph --json
python3 scripts/kora kb-graph --check-cycles

# Promover draft a publicado
python3 scripts/kora promote KNOWLEDGE/_SCRIPTORIUM/REVIEW/archivo.md

# Regenerar docs publicas
python3 scripts/kora sync-docs
```

Cohorts disponibles: `meta-kora`, `dev`, `ops`, `domains`.
Targets soportados: `claude-code`, `codex`, `gemini`, `openclaw`.
Profiles migrate: `legacy`, `transitional`, `strict`, `v2-agentfile`.

## Round-trip runtime ↔ IR ↔ runtime

```
Runtime foraneo  →  kora ingest  →  AGENTS/_FRAGUA/INBOX/
                                             ↓ (revision humana + kora promote)
                                    AGENTS/{ns}/{name}/
                                             ↓
                     kora transmute  →  {workspace}/_BUILD/{target}/
                                             ↓
                                      Runtime target
```

El vector PMI × LFS se preserva functorialmente o se proyecta con perdida
declarada en `_transmutation.yml`. Bisimulacion modulo proyeccion garantiza
equivalencia observacional.

## Tests

```bash
# Suite completa
python3 -m unittest discover -s tests

# Un test individual
python3 -m unittest tests.test_cli_smoke
python3 -m unittest tests.test_cli_smoke.KoraCliSmokeTests.test_health_strict_is_green

# Solo validacion semantica
python3 -m unittest tests.test_semantic_validation
```

Helpers: `tests/common.py` provee `run_cli()`, paths estandar y
`has_productive_workspaces()` para skip condicional cuando el fleet esta en
staging.

Suites: `test_cli_smoke`, `test_artifacts`, `test_semantic_validation`,
`test_graph_invariants`, `test_operating_core_scenarios`, `test_agent_audit`,
`test_check_pipeline`.

## Secuencia de trabajo

Cuando cambies specs, workspaces o knowledge:

1. Aplica cambios.
2. `python3 scripts/kora migrate --profile v2-agentfile` si hubo cambios en shape v1.
3. `python3 scripts/kora index`.
4. `python3 scripts/kora check --strict`.
5. `python3 scripts/kora sync-docs`.
6. `python3 -m unittest discover -s tests`.

Cuando transmutas un agente a runtime:

1. Verifica que `AGENT.md` tiene `harness_vector` (si no, corre `kora migrate --profile v2-agentfile`).
2. `kora transmute --target X --agent ns/name [--dry-run]`.
3. Revisa `{workspace}/_BUILD/{target}/_transmutation.yml` para pérdidas declaradas.
4. Compila el IR con adapter skill (si existe) o con LLM generico usando la runtime-extension.

Cuando ingestas un artefacto foraneo:

1. `kora ingest --from X --file path` (o `--workspace` para openclaw).
2. Revisa el AGENT.md generado en `_FRAGUA/INBOX/`.
3. Completa campos TODO (`invariants.ethical_commitments`, `plan` FSM real, etc.).
4. Ajusta `harness_vector` si la heuristica fue imprecisa.
5. Promueve manualmente a `_FRAGUA/REVIEW/` y luego a productivo.

## Notas practicas

- El **vector ontologico** es fuente de verdad; el shape (6 dimensiones) es proyeccion de authoring.
- Los staging areas (`_FRAGUA/`, `_TALLER/`, `_SCRIPTORIUM/`) son pre-categoriales: toolchain los trata como opacos, no se validan como KORA/MD estricto.
- Los artefactos KORA/MD usan YAML frontmatter con `_manifest.urn` obligatorio.
- `_BUILD/` dentro de workspaces es gitignored y regenerable.
- `_transmutation.yml` es proof-carrying: si falta o estructura incompleta, la transmutacion es invalida.
- Usa `python3 scripts/kora graph --json` para auditar nodos y morfismos, no los infieras.
- Usa `docs/generated/operating-core-contracts.*` para contrato operativo sin releer workspace por workspace.
- Si corriges `fxsl/cat`, hazlo para eliminar ruido o preparar absorcion formal, no para darle autoridad normativa directa.

## Estado del fleet (2026-04-17)

- 7 workspaces productivos con `harness_vector` poblado: kora/{guardian, curator, custodio, forgemaster, clawforge}, gn/{goreologo, digitrans}.
- ~28 workspaces en `AGENTS/_FRAGUA/INBOX/` pendientes de promocion.
- 1 skill productivo top-level: `SKILLS/kora/atomize/` (productor canonico familia atomic).
- Muchos skills en `SKILLS/_TALLER/INBOX/` pendientes de promocion/dedup.

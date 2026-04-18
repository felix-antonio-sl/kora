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
| **Serializacion** | Como se *escribe* (shape unificado de authoring) | `autoria-spec`, `md-spec`, `knowledge-spec` |
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
| Specs (constitucion) | `specs/` | 11 specs (gobernanza, harness, autoria, md-spec, knowledge, runtime-spec-md, transmutation, 4 runtime-extensions) | tracked |
| Conocimiento productivo | `KNOWLEDGE/{ns}/...` | Artefactos KORA/MD publicados (11 ns) | tracked |
| Staging knowledge | `KNOWLEDGE/_SCRIPTORIUM/{INBOX,REVIEW}/` | Material crudo + drafts | tracked |
| Workspaces productivos | `AGENTS/{ns}/{name}/` | Agentes activos con `AGENT.md` unificado | tracked |
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
4. Specs canonicas de serializacion: `autoria-spec v1.0` (unificada), `knowledge-spec v1.1`.
5. Specs de runtime: `runtime-spec-md v3.7`, `transmutation-spec v1.0`, runtime-extensions.
6. Extensiones de namespace.

`agentfile-spec` y `skill-overlay-spec` fueron retiradas: absorbidas por `autoria-spec`.

## Identidad URN

Dos regimenes:

- **Conceptual** (`urn:{ns}:kb:{id}` + campo `version`): artefactos KORA/MD de conocimiento.
- **Artefacto agentico** (`urn:{ns}:artefacto:{id}` + campo `version`): todo artefacto productivo conforme a `autoria-spec` (habilidad, subagente, agente-propiamente-tal, agente-plataforma).

El `_manifest.type` es ortogonal al URN.

## Formal Layer

- La Formal Layer oficial es `KNOWLEDGE/kora/categorical-foundations/`.
- `KNOWLEDGE/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo apunta a Formal Layer oficial.

## Shape unificado de autoria (`autoria-spec v1.0`)

Todo artefacto agentico productivo usa el mismo shape. Cuatro formas materiales:

| `atlas.forma_material` | Archivo | Topologia |
|------------------------|---------|-----------|
| `habilidad` | `SKILL.md` | `SKILLS/{ns}/{nombre}/` |
| `subagente` | `AGENT.md` | `AGENTS/{ns}/{nombre}/` |
| `agente-propiamente-tal` | `AGENT.md` | `AGENTS/{ns}/{nombre}/` con workspace |
| `agente-plataforma` | `AGENT.md` | `AGENTS/{ns}/{nombre}/` con `extensions.openclaw` |

Frontmatter canonico (identificadores en espanol):

- `_manifest.urn: urn:{ns}:artefacto:{id}` (regimen unico).
- `version: semver` (fuera del URN).
- `extensions.kora.vector_ontologico` (6 ejes PMI × LFS, obligatorio).
- `extensions.kora.atlas.{arnes_categorico, forma_material, metafora_relacional}`.
- `extensions.kora.entornos_objetivo` (lista de runtimes).
- `extensions.kora.nivel_prescripcion` (obligatorio solo si `forma_material: habilidad`).
- `artefacto.{perfil, plan, interfaz, contexto, composicion, invariantes}` (shape de 6 dimensiones, condicional por forma).

Subdirs canonicos en workspaces: `memoria/`, `referencias/`, `recursos/`, `scripts/`, `_BUILD/`.

**Proyeccion fiel a agentskills.io**: las habilidades transmutan byte-identical a paquetes del estandar externo (check `fidelidad-agentskills`). El renaming en ingles es responsabilidad del transmutor, no del autor.

Ver `specs/autoria-spec.md` para el detalle completo, matriz de validacion condicional por forma material, reglas de promocion, y ejemplos.

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
# Genera AGENT.md o SKILL.md conforme a autoria-spec en staging,
# con vector_ontologico auto-derivado + campos TODO para revision humana.

# Migracion forzada a autoria-spec (una sola pasada, sin compat transitoria)
python3 scripts/kora migrate --perfil a-autoria
python3 scripts/kora migrate --perfil a-autoria --cohort meta-kora --dry-run

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
Perfiles migrate: `a-autoria` (forzado, una pasada).

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
2. `python3 scripts/kora migrate --perfil a-autoria` si quedan artefactos sin migrar.
3. `python3 scripts/kora index`.
4. `python3 scripts/kora check --strict`.
5. `python3 scripts/kora sync-docs`.
6. `python3 -m unittest discover -s tests`.

Cuando transmutas un artefacto a runtime:

1. Verifica que el artefacto tiene `vector_ontologico` y `atlas.forma_material` (si no, corre `kora migrate --perfil a-autoria`).
2. `kora transmute --target X --artefacto ns/nombre [--dry-run]`.
3. Revisa `{workspace}/_BUILD/{target}/_transmutation.yml` para perdidas declaradas.
4. Compila el IR con adapter skill (si existe) o con LLM generico usando la runtime-extension.

Cuando ingestas un artefacto foraneo:

1. `kora ingest --from X --file path` (o `--workspace` para openclaw).
2. Revisa el artefacto generado en `_FRAGUA/INBOX/` (o `_TALLER/INBOX/` si `forma_material: habilidad`).
3. Completa campos TODO (`invariantes.compromisos_eticos`, `plan` FSM real, etc.).
4. Ajusta `vector_ontologico` si la heuristica fue imprecisa.
5. Promueve manualmente a `REVIEW/` y luego a productivo.

## Notas practicas

- El **vector ontologico** es fuente de verdad; el shape (6 dimensiones) es proyeccion de authoring.
- Los staging areas (`_FRAGUA/`, `_TALLER/`, `_SCRIPTORIUM/`) son pre-categoriales: toolchain los trata como opacos, no se validan como KORA/MD estricto.
- Los artefactos KORA/MD usan YAML frontmatter con `_manifest.urn` obligatorio.
- `_BUILD/` dentro de workspaces es gitignored y regenerable.
- `_transmutation.yml` es proof-carrying: si falta o estructura incompleta, la transmutacion es invalida.
- Usa `python3 scripts/kora graph --json` para auditar nodos y morfismos, no los infieras.
- Usa `docs/generated/operating-core-contracts.*` para contrato operativo sin releer workspace por workspace.
- Si corriges `fxsl/cat`, hazlo para eliminar ruido o preparar absorcion formal, no para darle autoridad normativa directa.

## Estado del fleet

- 7 workspaces productivos migrados a `autoria-spec v1.0` (commit `84dc1bb`, 2026-04-18): kora/{guardian, curator, custodio, forgemaster, clawforge}, gn/{goreologo, digitrans}. URN `urn:{ns}:artefacto:{id}` + shape `artefacto.*` + scaffolds legacy purgados. Residual (deuda de autoria humana): 8 `descripcion` faltante en AGENT.md (ver `kora check` con `autoria-conformance`).
- Workspaces pendientes en `AGENTS/_FRAGUA/INBOX/` migran en la misma pasada.
- 1 habilidad productiva top-level: `SKILLS/kora/atomize/`.
- Habilidades en `SKILLS/_TALLER/INBOX/` pendientes de promocion/dedup + migracion.

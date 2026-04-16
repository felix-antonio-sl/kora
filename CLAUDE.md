# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo gobernado por specs y soportado por una capa formal categorial. No es un proyecto de aplicacion tradicional: el activo principal es la consistencia entre conocimiento, specs, workspaces y toolchain.

## Arquitectura v8 — pipeline descentralizado

Cada tipo de artefacto (agentes, skills, conocimiento) tiene su propio staging area **dentro de su directorio principal**. No existe pipeline centralizado fuera de los directorios principales. `OPERATIONS/` fue eliminado.

| Capa | Path | Rol | Git |
|------|------|-----|-----|
| Constitucion | `specs/` | 7 specs: gobernanza, md-spec, knowledge-spec, agentfile-spec, skill-overlay-spec, runtime-spec-md, openclaw-runtime-extension | tracked |
| Conocimiento productivo | `KNOWLEDGE/{ns}/...` | Artefactos KORA/MD publicados por namespace (11 ns activos) | tracked |
| Staging conocimiento | `KNOWLEDGE/_SCRIPTORIUM/{INBOX,REVIEW}/` | Material crudo (INBOX) y drafts en revision (REVIEW) | tracked |
| Workspaces productivos | `AGENTS/{ns}/{name}/` | Workspaces agente activos (AGENT.md canonico o legacy 5-componentes) | tracked |
| Staging agentes | `AGENTS/_FRAGUA/{INBOX,REVIEW}/` | Agentes en elaboracion (INBOX pre-categorial, REVIEW listos para promover) | tracked |
| Perfiles | `AGENTS/_FRAGUA/_perfiles/` | Specs de personalidad/comportamiento (input al IR, no workspaces) | tracked |
| Skills portables | `SKILLS/{name}/` o `SKILLS/{ns}/{name}/` | Skills productivos (formato agentskills.io + overlay KORA) | tracked |
| Staging skills | `SKILLS/_TALLER/{INBOX,REVIEW}/` | Skills en elaboracion | tracked |
| Outputs transmutacion | `{workspace}/_BUILD/{target}/` | Derivados per-workspace (claude-code, openclaw, gemini, codex) | gitignored |
| Toolchain | `scripts/kora` | CLI Python que indexa, valida, migra, genera docs y transmuta | tracked |
| Schemas | `schemas/` | JSON Schemas para validacion de `config.json` y bootstrap artifacts | tracked |

Pipelines locales:

```
KNOWLEDGE/_SCRIPTORIUM/INBOX/  -> KNOWLEDGE/_SCRIPTORIUM/REVIEW/  -> KNOWLEDGE/{ns}/...
AGENTS/_FRAGUA/INBOX/          -> AGENTS/_FRAGUA/REVIEW/          -> AGENTS/{ns}/{name}/
SKILLS/_TALLER/INBOX/          -> SKILLS/_TALLER/REVIEW/          -> SKILLS/{name}/
```

Pipeline de transmutacion: `AGENTS/{ns}/{name}/AGENT.md` → `python3 scripts/kora transmute --target {claude-code,openclaw,...}` → `AGENTS/{ns}/{name}/_BUILD/{target}/` (gitignored).

Los subdirectorios de `INBOX/` son **pre-categoriales**: no representan namespace KORA. El namespace se asigna provisionalmente en `REVIEW/` y se confirma al promover a productivo.

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `catalog/catalog_master_kora.yml` es una vista materializada generada por `python3 scripts/kora index`. No es autoritativa.
- No escribas conteos a mano en docs publicas. Usa `python3 scripts/kora sync-docs`.
- No tomes `README.md` o docs antiguos como autoridad si contradicen la CLI o las specs vigentes.

## Precedencia

1. `specs/gobernanza.md` (v4.1 — constitucion, 3 regimenes URN formalizados en §4.3)
2. `specs/md-spec.md` (v7.1 — formato KORA/MD con 11 familias documentales)
3. `specs/knowledge-spec.md` (v1.1), `specs/agentfile-spec.md` (v1.1), `specs/skill-overlay-spec.md` (v1.1), `specs/runtime-spec-md.md` (v3.7)
4. extensiones de namespace (`specs/openclaw-runtime-extension.md` v1.0.1)

## Formal Layer

- La unica Formal Layer oficial es `KNOWLEDGE/kora/categorical-foundations/`.
- `KNOWLEDGE/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo puede apuntar a documentos de la Formal Layer oficial.
- Si una idea viene de `fxsl/cat` y no ha sido absorbida formalmente, usala como `Rationale:`, no como traza oficial.

## Identidad URN

Tres regimenes formales (gobernanza v4.1 §4.3):

- **Conceptual** (`urn:{ns}:kb:{id}` + campo `version`): artefactos KORA/MD (knowledge, specs, meta).
- **Agentfile** (`urn:{ns}:agent:{id}` + campo `version`): agentes modernos (`AGENT.md`).
- **Ejecutable legacy** (`urn:{ns}:{kind}:{id}:{version}`): bootstrap artifacts y skills `CM-*` (compat).

El `_manifest.type` (`bootstrap_config`, `bootstrap_agents`, `lazy_load_endofunctor`, etc.) es ortogonal al URN.

## Modelo Del Workspace

### Formato Agentfile (preferido)

Un agente KORA en formato Agentfile es un archivo unico `AGENT.md` con YAML frontmatter (6 dimensiones categoricas) y body Markdown. Gobernado por `specs/agentfile-spec.md`.

Las 6 dimensiones: `coalgebra` (dominio/triggers/outputs), `plan` (FSM como free monad), `interface` (tools/permissions), `fibers` (identity/operator/memory/runtime/knowledge), `composition` (sub-agentes/delegacion), `safety` (hard rules/co-induccion).

Si un workspace tiene `AGENT.md`, este es autoritativo sobre archivos legacy.

### Formato legacy (5 componentes)

- `AGENTS.md`: behavior (FSM, Reglas Duras, Co-induccion, Multi-turno, Wiring)
- `TOOLS.md`: interfaz semantica declarada
- `SOUL.md` y `USER.md`: estado/contexto
- `config.json`: security + runtime envelope
- `skills/`: capacidades lazy-load

Regido por `specs/agentfile-spec.md §13` (compat legacy).

### Skills

Skills portables viven en `SKILLS/` (top-level o bajo namespace). Gobernados por `specs/skill-overlay-spec.md`. Grammar canonica: `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.

### Familias documentales

`md-spec §5.6` define 11 familias: `spec`, `guide`, `normative`, `glossary`, `faq`, `catalog`, `cq_catalog`, `inventory`, `organigram`, `atomic`, `note`. `knowledge-spec §3` referencia esta tabla como fuente unica.

## Toolchain CLI

Entrypoint: `scripts/kora` (Python 3, deps en `requirements.txt`: PyYAML, jsonschema, pytest, openpyxl, requests).

Modulos en `scripts/kora_lib/`: `cli.py` (argparse), `config.py` (paths y constantes, staging areas FRAGUA/TALLER/SCRIPTORIUM), `catalog.py` (index/resolve), `checks.py` (algebra de checks composicional), `validation.py` (validate/lint-md), `audit.py` (health), `graph.py` (grafo categorial unificado), `kb_graph.py` (grafo de conocimiento standalone), `promote.py` (promover de REVIEW a productivo), `migration.py` (codemods), `reports.py` (stats/sync-docs), `intake.py` (reporte de staging), `workspaces.py` (iteradores productivos, excluye staging), `artifacts.py` (load/dump YAML frontmatter), `contracts.py` (operating core), `fxsl_cat.py` (ledger fxsl), `agent_audit.py` (audit por cohort).

### Comandos

```bash
# CHECK UNIFICADO — pipeline composicional de mantencion (recomendado)
python3 scripts/kora check                       # todos los checks en orden topologico
python3 scripts/kora check --severity high       # solo critical + high
python3 scripts/kora check --scope workspace     # solo checks de workspaces
python3 scripts/kora check --fix                 # auto-apply fixes canonicos
python3 scripts/kora check --list                # listar checks registrados
python3 scripts/kora check --strict              # exit 1 si hay fallos

# Indexar catalogo (siempre antes de check/health/validate/stats)
python3 scripts/kora index

# Resolver URN a path
python3 scripts/kora resolve "urn:kora:kb:md-spec"

# Comandos legacy (subsumidos por check, siguen disponibles)
python3 scripts/kora health --strict
python3 scripts/kora validate --profile strict
python3 scripts/kora lint-md --fix

# Stats y grafo (unificado: repo + knowledge relations)
python3 scripts/kora stats --json
python3 scripts/kora graph --json

# Transmutacion de agentes a plataformas target
python3 scripts/kora transmute --target claude-code --agent kora/curator
python3 scripts/kora transmute --target openclaw --agent gn/goreologo --dry-run

# Migracion de deuda legacy
python3 scripts/kora migrate --profile transitional
python3 scripts/kora migrate --profile transitional --dry-run
python3 scripts/kora migrate --profile transitional --cohort domains

# Reporte de staging (FRAGUA + TALLER + SCRIPTORIUM)
python3 scripts/kora intake

# Grafo de conocimiento (relaciones inter-artefacto)
python3 scripts/kora kb-graph --json
python3 scripts/kora kb-graph --check-cycles

# Promover draft a publicado (desde SCRIPTORIUM/REVIEW)
python3 scripts/kora promote KNOWLEDGE/_SCRIPTORIUM/REVIEW/archivo.md

# Regenerar docs publicas
python3 scripts/kora sync-docs
```

Cohorts disponibles para `--cohort`: `meta-kora`, `dev`, `ops`, `domains`.

Outputs generados en `docs/generated/`: `repo-stats`, `repo-graph`, `operating-core-contracts`, `fxsl-cat-ledger`, `agent-audit` (formatos `.json` y `.md`).

### Tests

```bash
# Suite completa
python3 -m unittest discover -s tests

# Un test individual
python3 -m unittest tests.test_cli_smoke
python3 -m unittest tests.test_cli_smoke.KoraCliSmokeTests.test_health_strict_is_green

# Solo validacion semantica
python3 -m unittest tests.test_semantic_validation
```

Los tests usan `tests/common.py` que provee `run_cli()`, paths estandar (`ROOT`, `AGENTS_ROOT`, `FIXTURES`, `GENERATED_DOCS`) y `has_productive_workspaces()` (util para tests que requieren fleet activo). Fixtures en `tests/fixtures/`.

Cuando el fleet esta en staging (todos los workspaces en `_FRAGUA/INBOX/` durante reprocesamiento), tests que dependen de workspaces productivos se skipean automaticamente.

Suites existentes: `test_cli_smoke`, `test_artifacts`, `test_semantic_validation`, `test_graph_invariants`, `test_operating_core_scenarios`, `test_agent_audit`, `test_check_pipeline`.

## Secuencia De Trabajo

Cuando cambies specs, workspaces o knowledge estructural:

1. aplica cambios
2. `python3 scripts/kora migrate --profile transitional` si hubo deuda legacy
3. `python3 scripts/kora index`
4. `python3 scripts/kora check --strict` (subsume health + validate + lint + kb-graph)
5. `python3 scripts/kora sync-docs`
6. `python3 -m unittest discover -s tests`

## Notas Practicas

- usa `python3 scripts/kora graph --json` cuando necesites auditar nodos y morfismos del repo, no inferirlos a mano.
- usa `docs/generated/operating-core-contracts.*` para ver el contrato operativo extraido del nucleo sin releer workspace por workspace.
- si agregas una nueva regla absoluta, debe tener enforcement razonable o bajar a `DEBERIA`.
- si corriges `fxsl/cat`, hazlo para eliminar ruido auditivo o preparar absorcion formal, no para darle autoridad normativa directa.
- Los staging areas (`_FRAGUA/`, `_TALLER/`, `_SCRIPTORIUM/`) son **pre-categoriales**: el toolchain los trata como opacos; no se validan como KORA/MD estricto.
- los artefactos KORA/MD usan YAML frontmatter (`---`) con `_manifest.urn` obligatorio.
- `_BUILD/` dentro de workspaces es gitignored y regenerable.

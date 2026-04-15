# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo gobernado por specs y soportado por una capa formal categorial. No es un proyecto de aplicacion tradicional: el activo principal es la consistencia entre conocimiento, specs, workspaces y toolchain.

## Arquitectura

| Capa | Path | Rol | Git |
|------|------|-----|-----|
| Constitucion | `specs/` | Reglas de gobernanza, precedencia, identidad, formatos (12 specs) | tracked |
| Conocimiento | `KNOWLEDGE/` | Artefactos KORA/MD publicados por namespace (11 ns activos, ~376 artefactos) | tracked |
| Workspaces IR | `AGENTS/` | Workspaces agente — formato AGENT.md (6 dims categoricas) o legacy (5 componentes) | tracked |
| Skills | `SKILLS/` | Libreria global de skills agentskills.io-compatible con overlay KORA | tracked |
| Perfiles | `AGENTS/_perfiles/` | Specs de personalidad/comportamiento (input al IR, no workspaces) | tracked |
| Pipeline | `OPERATIONS/` | Pipeline de conocimiento: `inbox/` y `drafts/` tracked; `source/` y `build/` gitignored | parcial |
| Build | `BUILD/` | Outputs de transmutacion de agentes a plataformas (claude, openclaw, gemini, codex) | gitignored |
| Toolchain | `scripts/kora` | CLI Python que indexa, valida, migra, genera docs y transmuta | tracked |
| Schemas | `schemas/` | JSON Schemas para validacion de `config.json` y bootstrap artifacts | tracked |

Pipeline de conocimiento: `OPERATIONS/source/` (gitignored) -> `OPERATIONS/drafts/` (tracked) -> `KNOWLEDGE/` (tracked). Usar `python3 scripts/kora intake` para ver estado de absorcion.

Pipeline de agentes: `AGENTS/{ns}/{name}/` (IR) -> `python3 scripts/kora transmute --target {claude,openclaw,...}` -> `BUILD/{target}/` (gitignored).

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `catalog/catalog_master_kora.yml` es una vista materializada generada por `python3 scripts/kora index`. No es autoritativa.
- No escribas conteos a mano en docs publicas. Usa `python3 scripts/kora sync-docs`.
- No tomes `README.md` o docs antiguos como autoridad si contradicen la CLI o las specs vigentes.

## Precedencia

1. `specs/gobernanza.md` (v4.0.0 — constitucion, 3 regimenes URN)
2. `specs/spec-md.md` y `specs/md-spec.md` (formatos de artefactos)
3. `specs/agentfile-spec.md`, `specs/agent-spec-md.md`, `specs/skill-overlay-spec.md`, `specs/skill-spec-md.md`, `specs/knowledge-spec.md`, `specs/transmutation-spec.md`, `specs/runtime-spec-md.md`, `specs/swarm-spec-md.md`
4. extensiones de namespace (e.g., `specs/openclaw-runtime-extension.md`)

## Formal Layer

- La unica Formal Layer oficial es `KNOWLEDGE/kora/categorical-foundations/`.
- `KNOWLEDGE/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo puede apuntar a documentos de la Formal Layer oficial.
- Si una idea viene de `fxsl/cat` y no ha sido absorbida formalmente, usala como `Rationale:`, no como traza oficial.

## Identidad URN

Tres regimenes (gobernanza.md §4):

- **Conceptual** (`urn:{ns}:kb:{id}` + campo `version`): artefactos de conocimiento publicados en `KNOWLEDGE/`.
- **Ejecutable legacy** (`urn:{ns}:agent-bootstrap:{id}:{version}` o `skill:{id}:{version}`): componentes bootstrap y skills.
- **Agente Agentfile** (`urn:{ns}:agent:{id}` + campo `version`): agentes en formato `AGENT.md` (nuevo formato, 6 dimensiones categoricas).

El `kind` del manifest (`bootstrap_config`, `bootstrap_agents`, etc.) es ortogonal al URN.

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

### Skills

Los skills residen en `SKILLS/` como libreria global (formato agentskills.io con overlay KORA). Gobernados por `specs/skill-overlay-spec.md`. Grammar canonica: `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.

## Toolchain CLI

Entrypoint: `scripts/kora` (Python 3, deps en `requirements.txt`: PyYAML, jsonschema, pytest, openpyxl, requests).

Modulos en `scripts/kora_lib/`: `cli.py` (argparse), `config.py` (paths y constantes), `catalog.py` (index/resolve), `checks.py` (algebra de checks composicional), `validation.py` (validate/lint-md), `audit.py` (health), `graph.py` (grafo categorial unificado), `kb_graph.py` (grafo de conocimiento standalone), `promote.py` (pipeline promote), `migration.py` (codemods), `reports.py` (stats/sync-docs), `intake.py` (pipeline), `workspaces.py` (iteradores de workspaces/skills), `artifacts.py` (load/dump YAML frontmatter), `contracts.py` (operating core), `fxsl_cat.py` (ledger fxsl), `agent_audit.py` (audit por cohort).

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
python3 scripts/kora resolve "urn:kora:kb:agent-spec-md"

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

# Pipeline de absorcion
python3 scripts/kora intake

# Grafo de conocimiento (relaciones inter-artefacto)
python3 scripts/kora kb-graph --json
python3 scripts/kora kb-graph --check-cycles

# Promover draft a publicado
python3 scripts/kora promote OPERATIONS/drafts/ns/archivo.md

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

Los tests usan `tests/common.py` que provee `run_cli()` (subprocess al entrypoint `scripts/kora`) y paths estandar (`ROOT`, `AGENTS_ROOT`, `FIXTURES`, `GENERATED_DOCS`). Fixtures en `tests/fixtures/`.

Suites existentes: `test_cli_smoke` (smoke de todos los comandos CLI), `test_artifacts` (load/validate de fixtures), `test_semantic_validation` (reglas semanticas profundas), `test_graph_invariants` (invariantes del grafo categorial), `test_operating_core_scenarios` (contratos del nucleo), `test_agent_audit` (audit por cohort).

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
- `OPERATIONS/` es local-only (gitignored). No asumas que existe en un clone fresco.
- los artefactos KORA/MD usan YAML frontmatter (`---`) con `_manifest.urn` obligatorio.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo gobernado por specs y soportado por una capa formal categorial. No es un proyecto de aplicacion tradicional: el activo principal es la consistencia entre conocimiento, specs, workspaces y toolchain.

## Arquitectura

| Capa | Path | Rol |
|------|------|-----|
| Constitucion | `specs/` | Reglas de gobernanza, precedencia, identidad, formatos (8 specs) |
| Conocimiento | `KNOWLEDGE/` | Artefactos publicados por namespace (`kora/`, `fxsl/`, `OMEGA/`, `gn/`, `salud/`, etc.) |
| Workspaces | `AGENTS/` | Workspaces agente ejecutables (`config.json` + bootstrap artifacts) |
| Skills | `SKILLS/` | Skills reutilizables por dominio (`data-modeling/`, `ux-design/`, etc.) |
| Perfiles | `AGENTS/_perfiles/` | Specs de personalidad/comportamiento para agentes (no son workspaces ejecutables) |
| Toolchain | `scripts/kora` | CLI Python que indexa, valida, migra y genera docs |
| Schemas | `schemas/` | JSON Schemas para validacion de `config.json` y bootstrap artifacts |
| Pipeline | `OPERATIONS/` | Superficies operacionales locales (excluido de git): `inbox/`, `source/`, `drafts/`, `build/` |

Pipeline de artefactos: `OPERATIONS/source/` -> `OPERATIONS/drafts/` -> `KNOWLEDGE/` (con `python3 scripts/kora intake` para ver estado de absorcion).

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `catalog/catalog_master_kora.yml` es una vista materializada generada por `python3 scripts/kora index`. No es autoritativa.
- No escribas conteos a mano en docs publicas. Usa `python3 scripts/kora sync-docs`.
- No tomes `README.md` o docs antiguos como autoridad si contradicen la CLI o las specs vigentes.

## Precedencia

1. `specs/gobernanza.md`
2. `specs/spec-md.md` y `specs/md-spec.md`
3. `specs/agent-spec-md.md`, `specs/skill-spec-md.md`, `specs/runtime-spec-md.md`, `specs/swarm-spec-md.md`
4. extensiones de namespace

## Formal Layer

- La unica Formal Layer oficial es `KNOWLEDGE/kora/categorical-foundations/`.
- `KNOWLEDGE/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo puede apuntar a documentos de la Formal Layer oficial.
- Si una idea viene de `fxsl/cat` y no ha sido absorbida formalmente, usala como `Rationale:`, no como traza oficial.

## Identidad URN

Dos regimenes distintos:

- **Conceptual** (`urn:{ns}:kb:{id}` + campo `version`): artefactos de conocimiento publicados en `KNOWLEDGE/`.
- **Ejecutable** (`urn:{ns}:agent-bootstrap:{id}:{version}` o `skill:{id}:{version}`): workspaces y skills en `AGENTS/`.

El `kind` del manifest (`bootstrap_config`, `bootstrap_agents`, etc.) es ortogonal al URN.

## Modelo Del Workspace

Todo workspace agente KORA se compone de:

- `AGENTS.md`: behavior (secciones canonicas: 1. FSM, 2. Reglas Duras, 3. Co-induccion, 4. Contexto Multi-turno, 5. Wiring)
- `TOOLS.md`: interfaz semantica declarada
- `SOUL.md` y `USER.md`: estado/contexto
- `config.json`: security + runtime envelope (validado contra `schemas/kora-agent-config-schema.json`)
- `skills/`: capacidades lazy-load

Convenciones duras:

- `TOOLS.md` y `config.json.tools.allow` deben coincidir exactamente.
- `config.json.runtime_capabilities` contiene permisos crudos del runtime.
- `sub_agents.max_concurrent` es ausente o `>= 1`; nunca `0`.
- los skills usan identidad `urn:{namespace}:skill:{id}:{version}`.
- la grammar canonica de skill degenerado es `Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`.

## Toolchain CLI

Entrypoint: `scripts/kora` (Python 3, deps en `requirements.txt`: PyYAML, jsonschema, pytest, openpyxl, requests).

Modulos en `scripts/kora_lib/`: `cli.py` (argparse), `config.py` (paths y constantes), `catalog.py` (index/resolve), `validation.py` (validate/lint-md), `audit.py` (health), `graph.py` (grafo categorial), `migration.py` (codemods), `reports.py` (stats/sync-docs), `intake.py` (pipeline), `workspaces.py` (iteradores de workspaces/skills), `artifacts.py` (load/dump YAML frontmatter), `contracts.py` (operating core), `fxsl_cat.py` (ledger fxsl), `agent_audit.py` (audit por cohort).

### Comandos

```bash
# Indexar catalogo (siempre antes de health/validate/stats)
python3 scripts/kora index

# Resolver URN a path
python3 scripts/kora resolve "urn:kora:kb:agent-spec-md"

# Salud del repo (broken URNs, routes, fragments)
python3 scripts/kora health --strict

# Validar workspaces contra spec
python3 scripts/kora validate --profile strict
python3 scripts/kora validate --profile strict --cohort meta-kora   # solo un cohort

# Lint de artefactos KORA/MD publicados
python3 scripts/kora lint-md                    # todo KNOWLEDGE/ + drafts/
python3 scripts/kora lint-md KNOWLEDGE/gn/      # path especifico
python3 scripts/kora lint-md --fix              # auto-fix seguro antes de lint

# Stats y grafo
python3 scripts/kora stats --json
python3 scripts/kora graph --json

# Migracion de deuda legacy
python3 scripts/kora migrate --profile transitional
python3 scripts/kora migrate --profile transitional --dry-run
python3 scripts/kora migrate --profile transitional --cohort domains

# Pipeline de absorcion
python3 scripts/kora intake

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
4. `python3 scripts/kora health --strict`
5. `python3 scripts/kora validate --profile strict`
6. `python3 scripts/kora sync-docs`
7. `python3 -m unittest discover -s tests`

## Notas Practicas

- usa `python3 scripts/kora graph --json` cuando necesites auditar nodos y morfismos del repo, no inferirlos a mano.
- usa `docs/generated/operating-core-contracts.*` para ver el contrato operativo extraido del nucleo sin releer workspace por workspace.
- si agregas una nueva regla absoluta, debe tener enforcement razonable o bajar a `DEBERIA`.
- si corriges `fxsl/cat`, hazlo para eliminar ruido auditivo o preparar absorcion formal, no para darle autoridad normativa directa.
- `OPERATIONS/` es local-only (gitignored). No asumas que existe en un clone fresco.
- los artefactos KORA/MD usan YAML frontmatter (`---`) con `_manifest.urn` obligatorio.

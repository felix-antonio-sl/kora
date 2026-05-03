# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in
this repository.

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo gobernado por specs y soportado por una capa formal
categorial. No es un proyecto de aplicacion tradicional: el activo principal es
la consistencia entre ley, ontologia, serializacion, runtimes, artefactos y
toolchain.

## Identidad Operacional Por Host

KORA distingue **host primary** (SSOT operacional, unico autorizado para
pushear a `origin/master`) y **hosts secondary** (replicas read-mostly que
trabajan en ramas feature y proponen cambios via PR).

- Doctrina: `governance/host-roles.md` (`urn:kora:kb:host-roles` v1.1.0)
- Marker local fuera del repo: `~/.kora/host.yml`
- Default si el marker no existe: `secondary`
- Verificacion rapida: `python3 toolchain/kora host`
- Hooks locales: `python3 toolchain/kora install-hooks`

Host primary canonico al `2026-05-03`: `hetzner2897261`. Antes de operar en
otra maquina, leer `governance/host-roles.md` y revisar el marker. `master`
en GitHub esta protegida (no force-push, no delete, linear history) y el hook
local bloquea push directo a `master` desde hosts secondary.

## Historia Relevante

Antes del `2026-04-18`, el repo usaba una topologia legacy con `specs/`,
`AGENTS/`, `SKILLS/`, `KNOWLEDGE/`, `schemas/` y `scripts/`. La reorg v5 movio
esa estructura a capas explicitas y a `artifacts/` + `toolchain/`.

Mapa rapido de traduccion:

| Legacy | Actual |
|--------|--------|
| `specs/` | `governance/`, `ontology/`, `serialization/`, `runtime/` |
| `KNOWLEDGE/` | `artifacts/knowledge/` |
| `AGENTS/` | `artifacts/agents/` |
| `SKILLS/` | `artifacts/skills/` |
| `schemas/` | `serialization/schemas/` |
| `scripts/` | `toolchain/` |
| `catalog/catalog_master_kora.yml` | `docs/generated/catalog.yml` |

Si encuentras referencias legacy en handoffs viejos, comentarios o helpers de
compatibilidad, tratarlas como contexto historico, no como topologia vigente.

## Arquitectura Actual

| Capa | Path | Rol | Git |
|------|------|-----|-----|
| Constitucion | `governance/` | Reglas meta y precedencia | tracked |
| Ontologia | `ontology/` | Modelo de artefactos, calidad, procesos y riesgo | tracked |
| Serializacion | `serialization/` | Shapes de authoring y schemas | tracked |
| Runtime | `runtime/` | Proyecciones, runtime extensions y multiagente | tracked |
| Knowledge | `artifacts/knowledge/` | Artefactos KORA/MD publicados + staging | tracked |
| Agentes | `artifacts/agents/` | Artefactos agenticos productivos + staging | tracked |
| Skills | `artifacts/skills/` | Skills productivas + staging | tracked |
| Toolchain | `toolchain/kora` y `toolchain/kora_lib/` | CLI Python soportada | tracked |
| Tests | `tests/` | Verificacion ejecutable | tracked |
| Docs derivadas | `docs/generated/` | Vistas materializadas regenerables | tracked |

Pipelines activos:

- `artifacts/knowledge/_SCRIPTORIUM/INBOX/ -> REVIEW/ -> artifacts/knowledge/{ns}/...`
- `artifacts/agents/_FRAGUA/INBOX/ -> REVIEW/ -> artifacts/agents/{ns}/{name}/`
- `artifacts/skills/_TALLER/INBOX/ -> REVIEW/ -> artifacts/skills/{ns}/{name}/`

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `docs/generated/catalog.yml` es derivado de `python3 toolchain/kora index`.
  No es autoritativo.
- `docs/generated/*` es materializado y regenerable. No escribas conteos a
  mano.
- No tomes `README.md`, handoffs viejos o wrappers legacy como autoridad si
  contradicen la CLI actual o las specs vigentes.

## Precedencia

1. `governance/gobernanza.md`
2. `ontology/harness-spec.md`
3. `serialization/autoria-spec.md`, `serialization/md-spec.md`,
   `serialization/knowledge-spec.md`
4. `runtime/runtime-spec-md.md`, `runtime/transmutation-spec.md`,
   `runtime/multiagente-spec.md` y `runtime/*-runtime-extension.md`
5. extensiones y artefactos de namespace

## Formal Layer

- La unica Formal Layer oficial es
  `artifacts/knowledge/kora/categorical-foundations/`.
- `artifacts/knowledge/fxsl/cat/` es corpus auxiliar.
- `Traces to:` solo puede apuntar a documentos de la Formal Layer oficial.
- Si una idea viene de `fxsl/cat` y no ha sido absorbida formalmente, usala
  como `Rationale:` o apoyo editorial, no como traza oficial.

## Modelo Actual De Artefactos

No asumas el workspace legacy de 5 archivos (`AGENTS.md`, `TOOLS.md`, `SOUL.md`,
`USER.md`, `config.json`) como forma canonica actual.

Hoy la unidad productiva principal es:

- `AGENT.md` para agentes en `artifacts/agents/{ns}/{name}/`
- `SKILL.md` para skills en `artifacts/skills/{ns}/{name}/`

Ambos siguen el shape unificado de `serialization/autoria-spec.md`, con
frontmatter `_manifest`, `version` fuera del URN y payload bajo `artefacto:`.

Fibras adjuntas posibles:

- `skills/`
- `memoria/`
- `MEMORY.md`
- `_BUILD/`
- `scripts/`
- `referencias/`
- `recursos/`

Antes de editar, inspecciona el directorio concreto. No proyectes a ciegas un
shape viejo sobre un artefacto productivo nuevo.

## Toolchain CLI

Entrypoint soportado: `toolchain/kora` (Python 3).

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

Regla operativa: la maintenance gate por defecto es `python3 toolchain/kora check --strict`.
Usa `health`, `validate`, `lint-md`, `migrate`, `promote` o `deprecate` cuando
necesites una fase puntual, no como reemplazo de la gate unificada.

## Tests

Suite completa:

```bash
python3 -m unittest discover -s tests
```

Tests puntuales:

```bash
python3 -m unittest tests.test_cli_smoke
python3 -m unittest tests.test_host_roles
python3 -m unittest tests.test_semantic_validation
python3 -m unittest tests.test_check_pipeline
```

`tests/common.py` ya modela la reorg v5:

- deriva `TOOLCHAIN_DIR` con fallback legacy a `scripts/`
- usa `docs/generated/` como raiz de salidas materializadas
- expone helpers de portabilidad como `canonical_path()`

Suites actuales:

- `test_cli_smoke`
- `test_artifacts`
- `test_semantic_validation`
- `test_graph_invariants`
- `test_operating_core_scenarios`
- `test_agent_audit`
- `test_check_pipeline`
- `test_host_roles`
- `test_atomize`
- `test_autoria_validate`
- `test_migrate_autoria`

## Secuencia De Trabajo

Cuando cambies specs, toolchain, artefactos estructurales o docs operativas:

1. aplica cambios
2. `python3 toolchain/kora index`
3. `python3 toolchain/kora check --strict`
4. `python3 -m unittest discover -s tests`
5. `python3 toolchain/kora kb-graph --json --orphans` si tocaste knowledge o relaciones
6. `python3 toolchain/kora sync-docs` si realmente quieres regenerar `docs/generated/`

Si la tarea requiere migracion explicita:

```bash
python3 toolchain/kora migrate --profile a-autoria
python3 toolchain/kora migrate --profile a-autoria --cohort meta-kora --dry-run
```

## Notas Practicas

- Usa `python3 toolchain/kora transmute --help` para verificar targets vivos.
- Usa `python3 toolchain/kora check --list` para verificar el registry actual de checks.
- No asumas que las cifras de handoffs viejos siguen vigentes; vuelvelas a medir.
- `docs/generated/*` se modifica al correr ciertos comandos. No mezcles esas
  salidas en un cambio si no forman parte del objetivo.
- El directorio `scripts/` raiz es residual; la toolchain viva esta en
  `toolchain/`.
- Si corriges `artifacts/knowledge/fxsl/cat/`, hazlo para reducir ruido o
  preparar absorcion formal, no para darle autoridad normativa directa.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

Guia operativa para agentes que trabajen dentro de este repositorio.

## Que Es Este Repo

KORA es un monorepo de artefactos agenticos gobernado por specs. No es una app
tradicional: el trabajo importante aqui es mantener coherentes la
constitucion, la ontologia, la serializacion, los runtimes, los artefactos y
la toolchain.

## Identidad Operacional Por Host

KORA distingue **host primary** (SSOT operacional, unico autorizado para
pushear a `origin/master`) y **hosts secondary** (replicas read-mostly que
trabajan en ramas feature y proponen cambios via PR).

- Doctrina: `governance/host-roles.md` (`urn:kora:kb:host-roles` v1.1.0)
- Marker local (fuera del repo): `~/.kora/host.yml`
- Default si el marker no existe: `secondary`
- Verificacion rapida: `python3 toolchain/kora host`
- Hooks locales: `python3 toolchain/kora install-hooks`

Host primary canonico al `2026-05-03`: `hetzner2897261`. Antes de operar en
otra maquina, leer `governance/host-roles.md` y revisar el marker. `master`
en GitHub esta protegida (no force-push, no delete, linear history). Instalar
hooks locales para bloquear push directo a `master` desde secondaries.

## Historia Operativa Minima

- Hasta la reorg v5 del `2026-04-18`, el repo usaba topologia legacy:
  `specs/`, `KNOWLEDGE/`, `AGENTS/`, `SKILLS/`, `schemas/`, `scripts/`.
- Desde esa reorg, las capas constitucionales son visibles como directorios
  top-level y los artefactos productivos viven bajo `artifacts/`.
- El cierre estructural del `2026-04-19` consolido `qa-spec`,
  `procesos-spec`, `risk-register-spec`, `multiagente-spec` y el target
  `mastra`.
- Los nombres legacy pueden seguir apareciendo en comentarios, handoffs viejos,
  scripts de compatibilidad o texto de ayuda no actualizado. No los tomes como
  topologia vigente.

Traduccion rapida:

| Legacy | Actual |
|--------|--------|
| `specs/` | `governance/`, `ontology/`, `serialization/`, `runtime/` |
| `KNOWLEDGE/` | `artifacts/knowledge/` |
| `AGENTS/` | `artifacts/agents/` |
| `SKILLS/` | `artifacts/skills/` |
| `schemas/` | `serialization/schemas/` |
| `scripts/` | `toolchain/` |
| `catalog/catalog_master_kora.yml` | `docs/generated/catalog.yml` |

## Topologia Actual

| Capa | Path | Rol |
|------|------|-----|
| Constitucion | `governance/` | Regla meta, precedencia y regimenes |
| Ontologia | `ontology/` | `harness-spec`, calidad, procesos y riesgo |
| Serializacion | `serialization/` | `autoria-spec`, `md-spec`, `knowledge-spec`, `schemas/` |
| Runtime | `runtime/` | `runtime-spec-md`, `transmutation-spec`, `multiagente-spec`, runtime extensions |
| Knowledge | `artifacts/knowledge/` | Corpus publicado y staging `_SCRIPTORIUM/` |
| Agentes | `artifacts/agents/` | Artefactos agenticos y staging `_FRAGUA/` |
| Skills | `artifacts/skills/` | Skills productivas y staging `_TALLER/` |
| Toolchain | `toolchain/kora`, `toolchain/kora_lib/` | CLI y checks soportados |
| Tests | `tests/` | Suite ejecutable y helpers |
| Docs derivadas | `docs/generated/` | Salidas regenerables |

Pipelines locales:

```text
artifacts/knowledge/_SCRIPTORIUM/INBOX/ -> REVIEW/ -> artifacts/knowledge/{ns}/...
artifacts/agents/_FRAGUA/INBOX/         -> REVIEW/ -> artifacts/agents/{ns}/{name}/
artifacts/skills/_TALLER/INBOX/         -> REVIEW/ -> artifacts/skills/{ns}/{name}/
```

Los staging areas son pre-categoriales: no representan namespace canonico hasta
la promocion.

## Skills Core Canonicas

Skills nucleares invocables desde cualquier agente o sesion. Son la entrada
recomendada para producir o mantener artefactos KORA-conformes:

| URN | Cuando |
|-----|--------|
| `urn:kora:artefacto:artifact-curator` | ciclo de vida general de artefactos KORA (knowledge, spec, skill, agente) |
| `urn:kora:artefacto:kora-skills` | construir / auditar / evolucionar habilidades |
| `urn:kora:artefacto:kora-agents` | construir / auditar / evolucionar subagentes y agentes-pt |
| `urn:kora:artefacto:mente-omega` | razonamiento estructural-discursivo (pentamotor Φ Ψ Ξ Δ Σ) |
| `urn:kora:artefacto:cat-thinking` | enmarque categorial (24 piezas ICAS-BoK) |
| `urn:kora:artefacto:atomize` | productor canonico de la familia documental `atomic` |
| `urn:kora:artefacto:knowledge-curator` | ruta KB normal descriptiva en REVIEW |
| `urn:kora:artefacto:curation-conductor` | flujo knowledge end-to-end |

Personas disponibles (agentes-pt en `artifacts/agents/{ns}/{name}/`):

- `urn:dev:artefacto:steipete` (Peter Steinberger clon — direccion de ejecucion)
- `urn:fxsl:artefacto:allan-kelly` (arquitectura organizacional human-agent)
- `urn:pro:artefacto:david-allen` (claridad operable integral, GTD)

## Canon Semantico

- La ontologia autoritativa vive en `ontology/harness-spec.md`.
- El vector ontologico `extensions.kora.vector_ontologico` es fuente de verdad
  para artefactos agenticos.
- El shape unificado de authoring vive en `serialization/autoria-spec.md`.
- La metodologia pre-transmutacion (Req → Blueprint → IR canonico) vive en
  `serialization/agent-skill-construction-spec.md`.
- La Formal Layer oficial vive en
  `artifacts/knowledge/kora/categorical-foundations/`.
- `artifacts/knowledge/fxsl/cat/` sigue siendo corpus auxiliar.

No proyectes el modelo legacy de workspace sobre el repo actual. Hoy lo
productivo suele estar gobernado por:

- `AGENT.md` en `artifacts/agents/{ns}/{name}/`
- `SKILL.md` en `artifacts/skills/{ns}/{name}/`

con fibras adjuntas opcionales (`skills/`, `memoria/`, `MEMORY.md`, `_BUILD/`,
`scripts/`, `referencias/`, `recursos/`).

## Source Of Truth

- El source of truth es el filesystem con manifests validos.
- `docs/generated/catalog.yml` es una vista materializada generada por
  `python3 toolchain/kora index`.
- `docs/generated/*` es derivado. No lo edites manualmente salvo que la tarea
  sea justamente regenerarlo o corregir un generador.
- Si un documento viejo contradice a la CLI actual o a las specs vigentes,
  manda la CLI actual y las specs vigentes.

## Precedencia

1. `governance/gobernanza.md`
2. `ontology/harness-spec.md`
3. `serialization/autoria-spec.md`, `serialization/md-spec.md`,
   `serialization/knowledge-spec.md`
4. `runtime/runtime-spec-md.md`, `runtime/transmutation-spec.md`,
   `runtime/multiagente-spec.md`, `runtime/*-runtime-extension.md`
5. extensiones y artefactos de namespace

## Toolchain CLI

Entrypoint soportado: `python3 toolchain/kora`.

Subcomandos vivos en este snapshot (verifica con `python3 toolchain/kora --help`):

- `index`
- `resolve`
- `health`
- `validate`
- `lint-md`
- `stats`
- `migrate`
- `sync-docs`
- `graph`
- `intake`
- `atomize`
- `kb-graph`
- `promote`
- `deprecate`
- `transmute`
- `roundtrip-check`
- `deploy-status`
- `record-invocation`
- `ingest`
- `check`

Comandos base:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora check --list
python3 toolchain/kora resolve "urn:kora:kb:harness-spec"
python3 toolchain/kora stats --json
python3 toolchain/kora graph --json
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora transmute --help
python3 toolchain/kora ingest --help
python3 toolchain/kora sync-docs
```

La maintenance gate recomendada es `check --strict`. Usa `health`,
`validate`, `lint-md`, `migrate`, `promote` o `deprecate` para tareas
puntuales o diagnosticos finos.

## Runtimes Target

Segun `python3 toolchain/kora transmute --help`, hoy existen siete targets:

- `agentskills`
- `claude-code`
- `codex`
- `gemini`
- `mastra`
- `opencode`
- `openclaw`

Cada uno tiene su `runtime/{nombre}-runtime-extension.md` con dominio +
matriz de preservacion. No asumas una lista mas corta tomada de documentos
previos a `2026-04-28`.

## Tests

La suite completa se ejecuta con:

```bash
python3 -m unittest discover -s tests
```

`tests/common.py` ya incorpora la realidad post-reorg:

- `TOOLCHAIN_DIR = toolchain/` con fallback a `scripts/`
- `GENERATED_DOCS = docs/generated/`
- helpers de portabilidad como `canonical_path()` y
  `assert_path_in_output()`

Suites presentes (`ls tests/test_*.py` para snapshot autoritativo):

- `test_agent_audit`
- `test_artifacts`
- `test_atomize`
- `test_autoria_validate`
- `test_check_pipeline`
- `test_cli_smoke`
- `test_curation_conductor_skill`
- `test_graph_invariants`
- `test_kb_graph_rendering`
- `test_knowledge_curator_skill`
- `test_migrate_autoria`
- `test_openclaw_kora_live_repo`
- `test_operating_core_scenarios`
- `test_salubrista_hodom`
- `test_semantic_validation`
- `test_skill_transmute_claude`
- `test_skill_transmute_codex`
- `test_urgenciologo_skeleton`

## Secuencia De Trabajo

Para cambios estructurales o doctrinales:

1. aplica cambios
2. `python3 toolchain/kora index`
3. `python3 toolchain/kora check --strict`
4. `python3 -m unittest discover -s tests`
5. `python3 toolchain/kora kb-graph --json --orphans` si tocaste knowledge o relaciones
6. `python3 toolchain/kora sync-docs` solo si quieres materializar `docs/generated/`

Si la tarea es migrar artefactos legacy:

```bash
python3 toolchain/kora migrate --profile a-autoria
python3 toolchain/kora migrate --profile a-autoria --cohort meta-kora --dry-run
```

Si la tarea es proyectar a runtime:

```bash
python3 toolchain/kora transmute --target opencode --agent dev/steipete --dry-run
python3 toolchain/kora transmute --target codex --agent kora/custodio --dry-run
python3 toolchain/kora transmute --target agentskills --agent kora/mente-omega --dry-run
```

## Notas Practicas

- Antes de tocar nada, lee el handoff mas reciente bajo
  `docs/reports/handoff-*.md` por fecha descendente: es el snapshot vivo del
  repo (estado, decisiones canonicas, pendientes, supuestos, riesgos).
- `docs/start-prompt.md` (URN `urn:kora:kb:start-prompt`) es el bootstrap
  copiable para sesiones nuevas; cita las specs, skills core y comandos de
  verificacion inicial.
- No asumas que `scripts/` raiz describe la toolchain viva. Hoy es residual.
- No asumas que `toolchain/README.md` esta mas fresco que la CLI. Verifica con
  `--help` y con el arbol real.
- No hardcodees conteos de nodos, tests o checks en docs generales. Midelos.
- Si corres `kb-graph`, `index` o `sync-docs`, revisa si se modifico
  `docs/generated/*` antes de mezclar esos cambios con otro objetivo.
- Si corriges `artifacts/knowledge/fxsl/cat/`, hazlo como corpus auxiliar, no
  como ley normativa.

## Portabilidad

Alcance operativo actual: Linux y macOS con Python >= 3.11.

Evidencia util:

- `toolchain/kora` corta con exit `2` si Python < 3.11
- `check --list` incluye `portabilidad-tests`
- `tests/common.py` normaliza paths canonicos para evitar falsos rojos entre
  macOS y Linux

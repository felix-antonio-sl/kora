---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Cierre explicito de la sesion post-ola 1 del toolchain: suites legacy, fibra productiva, check pipeline verde e integracion core del gate atomic."
version: "1.0.0"
status: publicado
tags: [handoff, toolchain, autoria-spec, atomize, promote, strict-check, closeout]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-ola1-toolchain"
    - "urn:kora:kb:handoff-2026-04-18-atomize-skill"
    - "urn:kora:kb:handoff-2026-04-18-atomize-integracion-v1"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:md-spec"
  refines:
    - "urn:kora:kb:handoff-2026-04-18-ola1-toolchain"
    - "urn:kora:kb:handoff-2026-04-18-atomize-integracion-v1"
---

# Handoff explícito — cierre toolchain post-ola 1 + `atomize` core

## Resumen ejecutivo

La sesion del **18 de abril de 2026** deja cerrada la deuda prioritaria
del handoff `ola1-toolchain` y absorbe al core la asimetria restante de
`atomize`.

Quedan estabilizadas cuatro capas:

1. tests legacy migrados al shape `artefacto.*`
2. 7 `AGENT.md` productivos con fibra minima y `descripcion`
3. pipeline `check --strict` totalmente verde
4. gate de acceptance review de `atomic` absorbido por `kora promote`

La siguiente sesion ya no necesita volver a pelear con `strict`, con
shape v1 ni con la bifurcacion `publish_atomic.py` vs `promote.py`.

## Cambios consolidados en esta linea

### 1. Legacy suites y shape unificado

- Se reescribieron los suites legacy que todavia asumian
  `SOUL.md`/`USER.md`/`TOOLS.md` o shape `agent.*`.
- Se adaptaron contratos y fixtures para `AGENT.md` + `artefacto.*`.
- Archivos nucleares tocados:
  - `scripts/kora_lib/contracts.py`
  - `scripts/kora_lib/graph.py`
  - `scripts/kora_lib/workspaces.py`
  - `tests/test_artifacts.py`
  - `tests/test_cli_smoke.py`
  - `tests/test_graph_invariants.py`
  - `tests/test_operating_core_scenarios.py`
  - `tests/test_check_pipeline.py`
  - `tests/fixtures/operating-core-scenarios.json`

### 2. Productivos migrados a fibra minima

- Se completaron los 7 `AGENT.md` productivos:
  - `AGENTS/kora/guardian/AGENT.md`
  - `AGENTS/kora/forgemaster/AGENT.md`
  - `AGENTS/kora/curator/AGENT.md`
  - `AGENTS/kora/custodio/AGENT.md`
  - `AGENTS/kora/clawforge/AGENT.md`
  - `AGENTS/gn/goreologo/AGENT.md`
  - `AGENTS/gn/digitrans/AGENT.md`
- Cada uno quedo con:
  - `descripcion`
  - `extensions.kora.atlas.{arnes_categorico, forma_material}`
  - `artefacto.perfil`
  - `artefacto.invariantes.compromisos_eticos`
  - `extensions.kora.entornos_objetivo`
- Resultado estable: `0 diagnostics` para los 7 bajo
  `autoria_validate`.

### 3. Verificador y grafo de conocimiento

- `workspace-validity` y `agentfile-dimensions` quedaron alineados a
  `autoria-spec`.
- `urn-integrity` y `kb-graph-cycles` ya canonicalizan aliases
  historicos y aceptan URNs retirados cuando el contrato los permite.
- Tambien se ignoran URNs bootstrap legacy cuando aparecen solo como
  referencia historica/no-catálogo.
- Archivos nucleares tocados:
  - `scripts/kora_lib/config.py`
  - `scripts/kora_lib/catalog.py`
  - `scripts/kora_lib/audit.py`
  - `scripts/kora_lib/kb_graph.py`
  - `tests/test_check_pipeline.py`
  - `tests/test_graph_invariants.py`

### 4. `atomize` absorbido al core de promote

- `scripts/kora_lib/promote.py` ahora exige acceptance review fresca y
  aceptada para cualquier bundle `atomic`.
- `SKILLS/kora/atomize/scripts/publish_atomic.py` delega en el mismo
  predicado del core; ya no mantiene un gate duplicado.
- Se agregaron regresiones para:
  - promote sin review
  - promote con review stale
  - promote con review fresca
- Archivo principal de pruebas:
  - `tests/test_atomize.py`

## Verificacion ejecutada

- `python3 scripts/kora check --strict`
  - resultado: `Checks run: 12`, `Passed: 12`, `Failed: 0`
- `python3 -m pytest tests/test_atomize.py -q`
  - resultado: `20 passed`
- `python3 -m pytest tests/test_check_pipeline.py tests/test_graph_invariants.py -q`
  - resultado: verde
- `python3 -m pytest tests/test_check_pipeline.py tests/test_artifacts.py -q -k 'promote or atomize_skill_is_runtime_agnostic_and_llm_first or knowledge_spec_registers_atomize_as_canonical_producer'`
  - resultado: `4 passed`

## Cambios que se deben commitear

Perimetro correcto del commit:

- `AGENTS/gn/digitrans/AGENT.md`
- `AGENTS/gn/goreologo/AGENT.md`
- `AGENTS/kora/clawforge/AGENT.md`
- `AGENTS/kora/curator/AGENT.md`
- `AGENTS/kora/custodio/AGENT.md`
- `AGENTS/kora/forgemaster/AGENT.md`
- `AGENTS/kora/guardian/AGENT.md`
- `scripts/kora_lib/{audit,catalog,config,contracts,graph,kb_graph,promote,workspaces}.py`
- `SKILLS/kora/atomize/scripts/publish_atomic.py`
- `tests/{test_atomize,test_check_pipeline,test_cli_smoke,test_graph_invariants,test_operating_core_scenarios,test_semantic_validation}.py`
- `tests/fixtures/operating-core-scenarios.json`
- esta memoria/handoff/prompt de `docs/reports/`

## Cambios que NO deben entrar en este commit

- `docs/generated/*`
- `catalog/catalog_master_kora.yml`
- `KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro-curado/`
- cualquier otra regeneracion incidental fuera del perimetro anterior

## Riesgos y deuda residual

1. `fidelidad-agentskills` sigue pendiente.
   Es el frente natural siguiente si se quiere cerrar la forma material
   `habilidad` de extremo a extremo.
2. Las runtime extensions v1.1+ siguen sin cerrar la matriz canonica
   `(arnes_categorico × forma_material × runtime)`.
3. Hay bundles historicos `atomic-opm-libro*` y handoffs viejos que
   todavia usan el URN legacy de `atomize`. No bloquean `check` ni
   `promote`, pero siguen como deuda documental.

## Handoff operativo

Si la proxima sesion arranca desde este commit, puede asumir:

- `strict` esta verde
- `promote` ya es el gate canonico para `atomic`
- la deuda restante es de proyeccion/interop (`agentskills`) y de
  armonizacion documental, no de shape ni de enforcement base

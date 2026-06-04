---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-04-opm-modeler-retirement"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Cierre operativo solicitado por HITL: evaluar si opm-modeler aportaba algo a modelamiento-opm; absorber lo util y retirar opm-modeler."
version: "1.0.0"
status: publicado
tags: [handoff, opm, modelamiento-opm, opm-modeler, openclaw]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-04 - retiro opm-modeler

## Estado actual

`opm-modeler` era una skill OpenClaw externa de Clawhub v1.0.0 instalada en
varios workspaces. No tenia fuente KORA productiva. Su corpus era legacy:

- `opm-iso-19450.md`
- `opm-opl-es.md`
- `metodologia-modelamiento-opm.md`

La skill KORA productiva `modelamiento-opm` ya era superior: usa la SSOT actual
de siete URNs, integra deep-opm-pro, reglas opforja estrictas, OPL bidireccional
y postura dialectica anti-barro.

## Decision

`opm-modeler` tenia un unico aporte util: un wizard SD mas explicito en
clasificacion del sistema, beneficiario/affectee, atributo de valor,
benefit-providing object, problem occurrence y gate de cierre.

Ese aporte fue absorbido en:

- `artifacts/skills/kora/modelamiento-opm/SKILL.md` v1.4.2
- `artifacts/skills/kora/modelamiento-opm/referencias/wizard-sd.md`
- `tests/test_artifacts.py`
- `docs/handoffs/2026-06-04-opm-modeler-retirement-memoria.md`

Despues de absorberlo, `opm-modeler` quedo redundante y fue eliminado de los
despliegues OpenClaw encontrados, incluyendo el mirror antiguo en
`/home/felix/Developer/projects/openclaw-fleet`.

## Despliegue

`modelamiento-opm` fue transmutado y desplegado a:

- Claude Code: `/home/felix/.claude/skills/modelamiento-opm/`
- Codex: `/home/felix/.codex/skills/modelamiento-opm/`
- OpenCode: `/home/felix/.config/opencode/skills/modelamiento-opm/`
- OpenClaw main: `/home/felix/openclaw-fleet/workspaces/main/skills/modelamiento-opm/`

Tambien fue instalado en los workspaces OpenClaw activos que antes tenian
`opm-modeler`:

- `allan-kelly`
- `fugaz`
- `gtd-integral`
- `salubrista`
- `steipete`

Verificacion local: no queda ningun directorio `*/skills/opm-modeler` bajo
`/home/felix/openclaw-fleet` ni
`/home/felix/Developer/projects/openclaw-fleet`.

## Validacion ejecutada

- `python3 toolchain/kora host`
- `python3 toolchain/kora check --strict --path artifacts/skills/kora/modelamiento-opm`
- `python3 toolchain/kora lint-md artifacts/skills/kora/modelamiento-opm/SKILL.md artifacts/skills/kora/modelamiento-opm/referencias/wizard-sd.md`
- `python3 -m unittest tests.test_artifacts.ArtifactFixtureTests.test_modelamiento_opm_declares_canonical_ssot tests.test_artifacts.ArtifactFixtureTests.test_modelamiento_opm_sd_wizard_absorbs_opm_modeler_value`
- `python3 toolchain/kora transmute --target {claude-code,codex,openclaw,opencode} --agent kora/modelamiento-opm`
- `python3 toolchain/kora deploy-builds --skill kora/modelamiento-opm --target {claude-code,codex,opencode,openclaw} --apply --overwrite`
- `python3 toolchain/kora deploy-builds --skill kora/modelamiento-opm --target openclaw --openclaw-workspace {allan-kelly,fugaz,gtd-integral,salubrista,steipete} --apply --overwrite`
- `python3 toolchain/kora index`
- `python3 toolchain/kora check --strict`
- `python3 toolchain/kora validate --profile strict`
- `python3 toolchain/kora lint-md artifacts/skills/kora/modelamiento-opm/SKILL.md artifacts/skills/kora/modelamiento-opm/referencias/wizard-sd.md docs/handoffs/2026-06-04-opm-modeler-retirement.md docs/handoffs/2026-06-04-opm-modeler-retirement-memoria.md`
- `python3 toolchain/kora check --strict --path docs/handoffs/2026-06-04-opm-modeler-retirement-memoria.md`
- `git diff --check`
- `python3 -m unittest discover -s tests`

Resultados finales:

- `check --strict`: 34/34 OK.
- `validate --profile strict`: 16 workspaces validos, 0 invalidos.
- `lint-md`: 0 issues.
- `git diff --check`: OK.
- Suite completa: 337 tests OK.

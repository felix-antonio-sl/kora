---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-04-hospitalista-runtime-canon"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Cierre operativo solicitado por HITL: resolver duplicado OpenClaw medico-hospitalista/hospitalista, documentar decisiones, memoria, commit y push."
version: "1.0.0"
status: publicado
tags: [handoff, agentes, openclaw, hospitalista, deploy, toolchain]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-04 - hospitalista runtime canon

## Estado actual

Se resolvio el duplicado OpenClaw entre `hospitalista` y
`medico-hospitalista`.

La fuente KORA productiva del agente clinico sigue siendo:

- `artifacts/agents/salud/medico-hospitalista/AGENT.md`
- URN: `urn:salud:artefacto:medico-hospitalista`
- Version: `1.1.0`
- Forma material: `agente-propiamente-tal`

El runtime OpenClaw canonico de ese URN es ahora:

- Agent ID: `hospitalista`
- Workspace: `/home/felix/openclaw-fleet/workspaces/hospitalista/`
- Provenance desplegada: `Source URN: urn:salud:artefacto:medico-hospitalista`

La skill de red `artifacts/skills/salud/hospitalista/SKILL.md` conserva su
identidad separada:

- URN: `urn:salud:artefacto:hospitalista`
- Forma material: `habilidad`
- Funcion: hospitalista de red, flujo, capacidad, continuidad y gobernanza.

## Decisiones

1. No se elimina la fuente KORA `medico-hospitalista`, porque el runtime no es
   fuente de verdad. Se mantiene como fuente canonica del agente clinico.
2. Se elimina el duplicado vivo de runtime: `medico-hospitalista` sale de
   `agents.list` en `/home/felix/.openclaw/openclaw.json`.
3. `workspaces/medico-hospitalista/` se archiva como duplicado de baja
   fidelidad, no se borra sin trazabilidad.
4. `workspaces/hospitalista/` queda como workspace vivo del agente clinico, no
   como promocion de la skill de red `urn:salud:artefacto:hospitalista`.
5. El toolchain KORA debe respetar `extensions.openclaw.workspace_path` para
   agentes. Sin esto, un deploy futuro volveria a crear
   `workspaces/medico-hospitalista/`.
6. La decision previa en `2026-06-04-agent-skill-mismatch` queda supersedida
   solo para el workspace OpenClaw `hospitalista`; no cambia la forma material
   de la skill `hospitalista`.

## Cambios aplicados

- `artifacts/agents/salud/medico-hospitalista/AGENT.md`
  - Version `1.1.0`.
  - `extensions.openclaw.agent_id: hospitalista`.
  - `extensions.openclaw.workspace_path: workspaces/hospitalista/`.
  - Absorbe reglas ricas que solo vivian en el workspace runtime:
    reconciliacion farmacologica, separacion de fuentes
    SGH/DAU/LIS/HCC/Osiris, elegibilidad HODOM, teach-back, banderas rojas y
    cierre de transiciones.
- `toolchain/kora_lib/transmute.py`
  - `deploy-status` audita agentes OpenClaw por `workspace_path` declarado.
  - La transmutacion OpenClaw emite `Runtime Agent ID` y config con alias
    runtime.
  - Skills OpenClaw incluyen provenance verificable por hash.
- `toolchain/kora_lib/deploy.py`
  - `deploy-builds --target openclaw` despliega agentes en el workspace
    declarado, no necesariamente en el nombre de carpeta fuente.
- `tests/test_deploy_builds.py`
  - Cubre deploy OpenClaw de agente con alias `workspace_path`.
- `tests/test_urgenciologo_skeleton.py`
  - Cubre `deploy-status` con alias OpenClaw y auditoria de `AGENTS.md`.
- `tests/test_skill_transmute_openclaw.py`
  - Cubre provenance de bundles OpenClaw de skills.
- `governance/deployed-only-register.md`
  - Documenta la correccion posterior sobre `hospitalista`.
- `docs/handoffs/2026-06-04-agent-skill-mismatch*`
  - Quedan con nota de supersesion parcial.

## Artefactos externos

- Config OpenClaw modificada:
  `/home/felix/.openclaw/openclaw.json`.
- Backup previo:
  `/home/felix/.openclaw/openclaw.json.bak-20260604-medico-hospitalista-retire`.
- Workspace archivado:
  `/home/felix/openclaw-fleet/_retired-agent-workspaces/2026-06-04-duplicate-medico-hospitalista/medico-hospitalista/`.
- Workspace vivo actualizado:
  `/home/felix/openclaw-fleet/workspaces/hospitalista/`.

No se elimino `/home/felix/.openclaw/agents/medico-hospitalista/agent`; queda
como estado runtime historico no referenciado por `agents.list`.

## Despliegue

`salud/medico-hospitalista` fue regenerado y desplegado a:

- Claude Code: `/home/felix/.claude/agents/medico-hospitalista.md`
- Codex: `/home/felix/.codex/skills/medico-hospitalista/SKILL.md`
- OpenCode: `/home/felix/.config/opencode/agents/medico-hospitalista.md`
- OpenClaw: `/home/felix/openclaw-fleet/workspaces/hospitalista/AGENTS.md`

Ademas, el ciclo previo de despliegue global dejo los agentes y skills KORA
activos auditados con deploy local en `claude-code`, `codex`, `opencode` y
`openclaw`, con `deploy-status` en 196 OK.

## Validacion ejecutada

- `python3 toolchain/kora host`: host `primary`.
- `python3 toolchain/kora check --strict --path artifacts/agents/salud/medico-hospitalista`: 34/34 OK.
- Tests de alias OpenClaw:
  `python3 -m unittest tests.test_deploy_builds.DeployBuildsTests.test_deploy_openclaw_agent_uses_declared_workspace_path_alias tests.test_urgenciologo_skeleton.UrgenciologoSkeletonTests.test_build_deploy_status_report_uses_openclaw_workspace_path_alias`: OK.
- `python3 toolchain/kora transmute --target {claude-code,codex,opencode,openclaw} --agent salud/medico-hospitalista`: OK.
- `python3 toolchain/kora deploy-builds --agent salud/medico-hospitalista --target claude-code --target codex --target opencode --target openclaw --apply --overwrite`: OK.
- `openclaw agents list`: `hospitalista` activo; `medico-hospitalista` ausente.
- `python3 toolchain/kora deploy-status`: `ok: 196`, `stale: 0`, `missing: 0`, `unsupported: 0`.
- `python3 toolchain/kora check --strict`: 34/34 OK.
- `git diff --check`: OK.
- `python3 -m unittest discover -s tests`: 344 tests OK.

## Pendientes

- Resolver en otro commit los cambios OPM ya existentes en
  `artifacts/knowledge/fxsl/opm/opm-ssot-es/`; no pertenecen a esta unidad.
- Revisar en otro ciclo el repo externo `/home/felix/openclaw-fleet`, que queda
  sucio por deploys, workspaces retirados y memoria runtime no versionada en
  KORA.
- Si se decide retirar definitivamente el estado historico
  `/home/felix/.openclaw/agents/medico-hospitalista/agent`, hacerlo como
  operacion OpenClaw separada y con backup.

## Supuestos

- `hospitalista` como runtime OpenClaw conserva sesiones, binding Telegram y
  aprendizaje operativo valioso.
- La colision nominal es aceptable porque los URNs separan forma material:
  `urn:salud:artefacto:hospitalista` es skill; `urn:salud:artefacto:medico-hospitalista`
  es agente clinico.
- El host `primary` esta autorizado para pushear a `origin/master`.

## Riesgos

- Codex proyecta agentes como skills runtime; el path
  `/home/felix/.codex/skills/medico-hospitalista/` no implica que la fuente KORA
  sea skill.
- El repo externo OpenClaw no queda atomizado por el commit KORA; su estado debe
  interpretarse junto con este handoff.
- Una futura herramienta que ignore `extensions.openclaw.workspace_path` podria
  recrear el duplicado. Los tests nuevos cubren el toolchain KORA actual.

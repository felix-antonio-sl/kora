---
_manifest:
  urn: "urn:kora:kb:handoff-2026-06-04-agent-skill-mismatch"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Cierre operativo solicitado por HITL: decidir y resolver artefactos desplegados como agentes cuya fuente KORA existia solo como skill."
version: "1.0.0"
status: publicado
tags: [handoff, agentes, skills, despliegue, opencode, openclaw]
lang: es
extensions:
  kora:
    family: note
---

# Handoff 2026-06-04 - mismatch agente/skill

## Nota posterior 2026-06-04

La decision sobre `hospitalista` queda parcialmente supersedida por
`docs/handoffs/2026-06-04-hospitalista-runtime-canon.md`.

Se mantiene que la skill de red `urn:salud:artefacto:hospitalista` no se
promueve a agente. Se corrige, en cambio, que el workspace OpenClaw
`hospitalista` no era una proyeccion de esa skill, sino el runtime historico y
rico del agente clinico `urn:salud:artefacto:medico-hospitalista`. Por eso
`workspaces/hospitalista/` queda como runtime canónico de ese agente, mientras
`workspaces/medico-hospitalista/` se retira como duplicado de baja fidelidad.

## Estado actual

Se resolvio el grupo de artefactos desplegados como agentes pero con fuente KORA
solo como skill:

- `hospitalista`: se mantiene como skill KORA.
- `mente-omega`: se mantiene como skill KORA.
- `jobs-healthcare-ux`: se convirtio a `AGENT.md` productivo.
- `steve-jobs-agentic-designer`: se convirtio a `AGENT.md` productivo.

Los cuatro declaran y tienen despliegue local en targets activos
`claude-code`, `codex`, `openclaw` y `opencode`, respetando su forma material.

## Decisiones

1. `hospitalista` no se promovio a agente. Su fuente declara explicitamente un
   modo/disciplina portable del agente `salubrista`; no sostiene identidad ni
   workspace propio. El workspace OpenClaw `hospitalista` fue retirado como
   agente activo.
2. `mente-omega` no se promovio a agente. Su fuente declara arquitectura
   cognitiva portable para agentes invocadores; no aporta semantica de dominio
   ni requiere materia persistente propia. El workspace OpenClaw `mente-omega`
   fue retirado como agente activo.
3. `jobs-healthcare-ux` se promovio a `artifacts/agents/salud/jobs-healthcare-ux/AGENT.md`
   con la misma URN `urn:salud:artefacto:jobs-healthcare-ux`. La fuente previa
   `SKILL.md` era una materializacion incorrecta de un agente nativo con
   identidad, juicio y memoria de diseno clinico.
4. `steve-jobs-agentic-designer` se promovio a
   `artifacts/agents/dev/steve-jobs-agentic-designer/AGENT.md` con la misma URN
   `urn:dev:artefacto:steve-jobs-agentic-designer`. Se agrego salvaguarda
   explicita: persona sintetica, sin representacion ni afiliacion con Steve
   Jobs, Apple ni terceros.
5. No se dejaron fuentes `AGENT.md` y `SKILL.md` con el mismo ref porque el CLI
   de transmutacion resuelve skills antes que agents en targets locales; duplicar
   fuente habria mantenido el bug.

## Artefactos relevantes

- `artifacts/agents/salud/jobs-healthcare-ux/AGENT.md`
- `artifacts/agents/salud/jobs-healthcare-ux/memoria/README.md`
- `artifacts/agents/dev/steve-jobs-agentic-designer/AGENT.md`
- `artifacts/agents/dev/steve-jobs-agentic-designer/memoria/README.md`
- `artifacts/skills/salud/hospitalista/SKILL.md`
- `artifacts/skills/kora/mente-omega/SKILL.md`
- `governance/deployed-only-register.md`

## Despliegue

Agentes promovidos:

- Claude Code: `/home/felix/.claude/agents/{jobs-healthcare-ux,steve-jobs-agentic-designer}.md`
- Codex: `/home/felix/.codex/skills/{jobs-healthcare-ux,steve-jobs-agentic-designer}/`
- OpenCode: `/home/felix/.config/opencode/agents/{jobs-healthcare-ux,steve-jobs-agentic-designer}.md`
- OpenClaw: `/home/felix/openclaw-fleet/workspaces/{jobs-healthcare-ux,steve-jobs-agentic-designer}/`

Skills conservadas:

- Claude Code: `/home/felix/.claude/skills/{hospitalista,mente-omega}/`
- Codex: `/home/felix/.codex/skills/{hospitalista,mente-omega}/`
- OpenCode: `/home/felix/.config/opencode/skills/{hospitalista,mente-omega}/`
- OpenClaw main: `/home/felix/openclaw-fleet/workspaces/main/skills/{hospitalista,mente-omega}/`

Workspaces OpenClaw retirados:

- `/home/felix/openclaw-fleet/_retired-agent-workspaces/2026-06-04-skill-only/hospitalista/`
- `/home/felix/openclaw-fleet/_retired-agent-workspaces/2026-06-04-skill-only/mente-omega/`

## Validacion ejecutada

- `python3 toolchain/kora host`
- `python3 toolchain/kora check --strict --path artifacts/agents/salud/jobs-healthcare-ux`
- `python3 toolchain/kora check --strict --path artifacts/agents/dev/steve-jobs-agentic-designer`
- `python3 toolchain/kora check --strict --path artifacts/skills/salud/hospitalista`
- `python3 toolchain/kora check --strict --path artifacts/skills/kora/mente-omega`
- `python3 toolchain/kora transmute --target {claude-code,codex,openclaw,opencode} --agent ...`
- `python3 toolchain/kora deploy-builds ... --dry-run`
- `python3 toolchain/kora deploy-builds ... --apply --overwrite`
- `python3 toolchain/kora index`
- `python3 toolchain/kora recovery-inventory --json --output docs/generated/recovery-inventory.json`
- `python3 toolchain/kora check --strict`
- `python3 toolchain/kora validate --profile strict`
- `python3 toolchain/kora lint-md docs/handoffs/2026-06-04-agent-skill-mismatch.md docs/handoffs/2026-06-04-agent-skill-mismatch-memoria.md docs/handoffs/2026-06-04-agent-skill-mismatch-prompt-continuacion.md governance/deployed-only-register.md`
- `git diff --check`
- `python3 -m unittest discover -s tests`

Resultados finales antes de commit:

- `check --strict`: 34/34 OK.
- `validate --profile strict`: 16 workspaces validos, 0 invalidos.
- `lint-md`: 0 issues.
- `git diff --check`: OK.
- Suite completa: 336 tests OK.

## Supuestos

- Los cuatro artefactos pertenecen a autoria/propiedad del operador.
- OpenCode sigue activo como runtime canonico por HITL del 2026-06-04.
- `docs/generated/` es vista derivada local; no se versiona en este commit.

## Riesgos

- Codex proyecta agentes como skills runtime, por lo que el path Codex no
  distingue visualmente agente KORA de skill KORA. La fuente y `_transmutation.yml`
  son la evidencia de tipo.
- `jobs-healthcare-ux` y `steve-jobs-agentic-designer` tienen perdidas
  declaradas en Codex/OpenCode para memoria o transparencia segun el target.
- Los workspaces retirados de `hospitalista` y `mente-omega` contienen memoria
  operativa historica; no debe reactivarse como agente sin nueva decision HITL.

---
_manifest:
  urn: "urn:kora:kb:memoria-agent-skill-mismatch-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada del handoff 2026-06-04 agent-skill mismatch."
version: "1.0.0"
status: publicado
tags: [memoria, agentes, skills, despliegue, openclaw]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - agent-skill mismatch

- `hospitalista` y `mente-omega` siguen siendo skills KORA, no agentes.
- Sus workspaces OpenClaw activos fueron retirados a
  `/home/felix/openclaw-fleet/_retired-agent-workspaces/2026-06-04-skill-only/`.
- `jobs-healthcare-ux` ahora tiene fuente productiva
  `artifacts/agents/salud/jobs-healthcare-ux/AGENT.md` y conserva
  `urn:salud:artefacto:jobs-healthcare-ux`.
- `steve-jobs-agentic-designer` ahora tiene fuente productiva
  `artifacts/agents/dev/steve-jobs-agentic-designer/AGENT.md` y conserva
  `urn:dev:artefacto:steve-jobs-agentic-designer`.
- No dejar `SKILL.md` productivo con el mismo ref que esos agentes: el CLI
  transmute prioriza skill en targets locales y volveria a ocultar el agente.
- Los cuatro artefactos fueron transmutados y desplegados a Claude Code, Codex,
  OpenCode y OpenClaw segun su forma material.
- Las copias runtime stale de `jobs-healthcare-ux` y
  `steve-jobs-agentic-designer` como skills Claude/OpenCode/OpenClaw main fueron
  retiradas.
- Gates finales: `check --strict` 34/34 OK; `validate --profile strict` 16
  workspaces validos; `lint-md` 0 issues; suite completa 336 tests OK.

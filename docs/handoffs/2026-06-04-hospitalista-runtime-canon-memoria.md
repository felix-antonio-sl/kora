---
_manifest:
  urn: "urn:kora:kb:memoria-hospitalista-runtime-canon-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada del handoff 2026-06-04 hospitalista runtime canon."
version: "1.0.0"
status: publicado
tags: [memoria, agentes, openclaw, hospitalista, deploy]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - hospitalista runtime canon

- `artifacts/agents/salud/medico-hospitalista/AGENT.md` sigue siendo la fuente
  KORA canonica del agente clinico `urn:salud:artefacto:medico-hospitalista`.
- El runtime OpenClaw canonico de ese URN es `hospitalista`, con workspace
  `/home/felix/openclaw-fleet/workspaces/hospitalista/`.
- La skill `artifacts/skills/salud/hospitalista/SKILL.md` conserva el URN
  separado `urn:salud:artefacto:hospitalista` y sigue siendo habilidad de red,
  flujo y capacidad.
- `workspaces/medico-hospitalista/` fue retirado a
  `/home/felix/openclaw-fleet/_retired-agent-workspaces/2026-06-04-duplicate-medico-hospitalista/medico-hospitalista/`.
- `/home/felix/.openclaw/openclaw.json` ya no lista `medico-hospitalista`;
  backup: `/home/felix/.openclaw/openclaw.json.bak-20260604-medico-hospitalista-retire`.
- El toolchain ahora respeta `extensions.openclaw.workspace_path` para
  transmutar, desplegar y auditar agentes OpenClaw con alias runtime.
- Gates finales del ciclo: `deploy-status` 196 OK, `check --strict` 34/34 OK,
  `git diff --check` OK y `python3 -m unittest discover -s tests` 344 tests OK.
- Handoff completo:
  `docs/handoffs/2026-06-04-hospitalista-runtime-canon.md`.

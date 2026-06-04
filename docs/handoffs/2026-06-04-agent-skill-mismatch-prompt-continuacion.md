---
_manifest:
  urn: "urn:kora:kb:prompt-continuacion-2026-06-04-agent-skill-mismatch"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Prompt breve de continuacion derivado del handoff 2026-06-04 agent-skill mismatch."
version: "1.0.0"
status: publicado
tags: [prompt-continuacion, handoff, agentes, skills]
lang: es
extensions:
  kora:
    family: note
---

# Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde
docs/handoffs/2026-06-04-agent-skill-mismatch.md.

Primero lee AGENTS.md y CLAUDE.md. Verifica host con
`python3 toolchain/kora host`. Luego revisa el handoff citado.

Estado clave: `hospitalista` y `mente-omega` son skills, no agentes; no
reactivar sus workspaces OpenClaw sin HITL. `jobs-healthcare-ux` y
`steve-jobs-agentic-designer` son ahora fuentes `AGENT.md` productivas con la
misma URN anterior y despliegue a Claude Code, Codex, OpenCode y OpenClaw.

Siguiente foco sugerido: continuar inventario de despliegues locales con fuente
KORA ausente o tipo fuente/runtime divergente, usando
`python3 toolchain/kora recovery-inventory --json`.
```

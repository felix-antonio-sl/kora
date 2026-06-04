---
_manifest:
  urn: "urn:kora:kb:prompt-continuacion-2026-06-04-agentes-prioridad-alta-opencode"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Prompt breve de continuacion derivado del handoff 2026-06-04 agentes prioridad alta y OpenCode."
version: "1.0.0"
status: publicado
tags: [prompt-continuacion, handoff, agentes, opencode]
lang: es
extensions:
  kora:
    family: note
---

# Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde
docs/handoffs/2026-06-04-agentes-prioridad-alta-opencode.md.

Primero lee AGENTS.md y CLAUDE.md. Luego revisa el handoff citado y verifica
estado con `python3 toolchain/kora host`, `python3 toolchain/kora index` y
`python3 toolchain/kora check --strict`.

Estado clave: OpenCode ya esta activo como runtime canonico; no usar
`--force-paused` para opencode ni tratarlo como target pausado. Siete agentes
de prioridad alta ya tienen fuente productiva KORA y despliegue a Claude Code,
Codex, OpenCode y OpenClaw.

Siguiente foco sugerido: continuar el inventario de artefactos desplegados sin
fuente productiva KORA, priorizando skills desplegadas desde staging, artefactos
con mismatch agente/skill y workspaces cuyo origen autoral sea propio.
```

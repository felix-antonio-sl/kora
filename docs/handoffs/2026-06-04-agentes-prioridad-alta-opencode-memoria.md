---
_manifest:
  urn: "urn:kora:kb:memoria-agentes-prioridad-alta-opencode-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada del handoff agentes prioridad alta y OpenCode."
version: "1.0.0"
status: publicado
tags: [memoria, agentes, opencode, runtime, despliegue]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - agentes prioridad alta y OpenCode

- OpenCode queda reactivado como runtime canonico KORA desde HITL 2026-06-04.
- `urn:kora:kb:opencode-runtime-extension` ahora resuelve a
  `runtime/opencode-runtime-extension.md`.
- `opencode` fue removido de `PAUSED_TARGETS`; transmute a OpenCode ya no
  requiere `--force-paused`.
- Siete agentes de prioridad alta fueron promovidos desde staging a fuente
  productiva KORA: `agent-architect`, `forjador-openclaw`, `fugaz`,
  `ifml-architect`, `opm-specialist`, `polymath`,
  `ux-research-design-ai`.
- Los staging equivalentes en `_FRAGUA/INBOX/` fueron eliminados.
- Los siete agentes declaran `entornos_objetivo: [claude-code, codex,
  openclaw, opencode]`.
- Los siete agentes fueron desplegados localmente a Claude Code, Codex,
  OpenCode y OpenClaw.
- Gates finales: `check --strict` 34/34 OK; `validate --profile strict` OK;
  suite completa 336 tests OK.

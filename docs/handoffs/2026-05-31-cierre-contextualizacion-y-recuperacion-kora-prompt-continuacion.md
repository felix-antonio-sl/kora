---
_manifest:
  urn: "urn:kora:kb:prompt-continuacion-2026-05-31-cierre-contextualizacion-y-recuperacion-kora"
  provenance:
    created_by: "Codex"
    created_at: "2026-05-31"
    source: "Prompt breve de continuacion derivado del handoff 2026-05-31."
version: "1.0.0"
status: publicado
tags: [prompt-continuacion, handoff, continuidad]
lang: es
extensions:
  kora:
    family: note
---

# Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde
docs/handoffs/2026-05-31-cierre-contextualizacion-y-recuperacion-kora.md.

Primero lee AGENTS.md y CLAUDE.md. Luego revisa el handoff citado y verifica
estado con `python3 toolchain/kora host`, `python3 toolchain/kora index` y
`python3 toolchain/kora check --strict`.

Objetivo inmediato: revisar los candidatos en _FRAGUA/INBOX
(forjador-openclaw, fugaz, ifml-architect, opm-specialist,
ux-research-design-ai) y decidir promocion, fusion o descarte. Mantener
metodologia-forja-opm-es como metodo para opforja sin relajar las capas de
validez OPM. No restaurar handoffs historicos retirados sin HITL/ADR.
```

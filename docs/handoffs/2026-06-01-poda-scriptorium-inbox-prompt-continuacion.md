---
_manifest:
  urn: "urn:kora:kb:prompt-continuacion-poda-scriptorium-inbox-2026-06-01"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-01"
    source: "Prompt breve de continuacion para el saneamiento _SCRIPTORIUM/INBOX."
version: "1.0.0"
status: publicado
tags: [prompt-continuacion, saneamiento, scriptorium, inbox]
lang: es
extensions:
  kora:
    family: note
---

# Prompt de continuacion

Retoma desde `docs/handoffs/2026-06-01-poda-scriptorium-inbox.md`. Verifica
`git status`, `python3 toolchain/kora check --strict` y `python3 -m unittest
discover -s tests`. Si master esta limpio, continua con una auditoria atomica de
`_FRAGUA`/`_TALLER`: promover lo vivo, retirar lo obsoleto y externalizar solo
lo que sea crudo o historico, sin tocar productivos ni specs congeladas.

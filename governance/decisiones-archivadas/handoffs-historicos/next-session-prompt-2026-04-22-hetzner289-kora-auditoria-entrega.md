---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-22-hetzner289-kora-auditoria-entrega"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-22"
    source: "Prompt breve de continuidad posterior a la auditoría del server hetzner2897261."
version: "1.1.0"
status: publicado
tags: [next-session-prompt, hetzner, auditoria, entrega]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-22-hetzner289-kora-auditoria-entrega"
    - "urn:kora:kb:operational-memory-2026-04-22-hetzner289-kora-auditoria-entrega"
---

# Prompt de continuación

<prompt>
Trabaja sobre el server `hetzner2897261` y lee primero:

- `docs/reports/handoff-2026-04-22-hetzner289-kora-auditoria-entrega.md`
- `docs/reports/operational-memory-2026-04-22-hetzner289-kora-auditoria-entrega.md`

Estado esperado al arrancar en `/home/felix/kora`:

- `git rev-parse HEAD` = `39c4cf4`
- `python3 toolchain/kora check --strict` = `18/18`
- `python3 toolchain/kora deploy-status` = `1 ok / 7 missing / 0 stale`
- `python3 -m unittest discover -s tests` = `323 OK (skipped=2)`

Prioridad:

1. decidir si `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-test-acceptance-review.md` se elimina o se conserva como evidencia canónica
2. verificar `claude` real en el server antes de seguir con la skill JointJS
3. probar de verdad la skill `jointjs-open-source` instalada en `~/.claude/skills/`
4. si eso cierra, abrir el siguiente gap: `skill -> codex`

No asumir que “skill instalada” equivale a “skill operativa” mientras `claude` no esté verificado en PATH o en su wrapper real.
</prompt>

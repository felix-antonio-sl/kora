---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-22-hetzner289-kora-auditoria-entrega"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-22"
    source: "Prompt breve de continuidad posterior a la auditoría del server hetzner2897261."
version: "1.0.0"
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

- `git rev-parse HEAD` = `4f5ddbc`
- `python3 toolchain/kora check --strict` = `18/18`
- `python3 toolchain/kora deploy-status` = `1 ok / 7 missing / 0 stale`
- `python3 -m unittest discover -s tests` = falla 1 en `test_atomize.py`

Prioridad:

1. arreglar `test_publish_atomic_wrapper_requires_fresh_accepted_review`
2. decidir si `tests/fixtures/canarios/urgenciologo-baseline.md` se elimina o canoniza
3. verificar `claude` real en el server antes de seguir con la skill JointJS

No mezclar reparación de entrega con nuevos features hasta volver a verde.
</prompt>

---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-22-hetzner289-kora-auditoria-entrega"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-22"
    source: "Memoria operativa compacta de la auditoría del server hetzner2897261."
version: "1.1.0"
status: publicado
tags: [operational-memory, auditoria, hetzner, entrega]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-22-hetzner289-kora-auditoria-entrega"
    - "urn:kora:kb:next-session-prompt-2026-04-22-hetzner289-kora-auditoria-entrega"
---

# Memoria operativa — auditoría `hetzner2897261`

## Snapshot

| Ítem | Estado |
|------|--------|
| Repo path | `/home/felix/kora` |
| Branch | `master` |
| HEAD | `39c4cf4` |
| `check --strict` | 18/18 verde |
| `deploy-status` | 1 ok / 7 missing / 0 stale |
| `unittest discover` | 323 corridos / 0 fallas / 2 skipped |
| `claude` en PATH | no detectado |
| JointJS bundle | generado |
| JointJS skill instalada | sí |
| Drift local | `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-test-acceptance-review.md` |

## Invariantes

1. No hay stales en deploy.
2. Sí hay fleet Claude incompleto.
3. La entrega del server está verde a nivel checks/tests, pero no necesariamente a nivel runtime Claude.
4. El drift local del server hoy vive en `_SCRIPTORIUM/REVIEW/atomic/`, no en `tests/fixtures/canarios/`.

## Próximo paso recomendado

Entrar por validación runtime real de Claude y saneamiento del draft atomic residual.

---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-22-hetzner289-kora-auditoria-entrega"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-22"
    source: "Memoria operativa compacta de la auditoría del server hetzner2897261."
version: "1.0.0"
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
| HEAD | `4f5ddbc` |
| `check --strict` | 18/18 verde |
| `deploy-status` | 1 ok / 7 missing / 0 stale |
| `unittest discover` | 323 corridos / 1 falla / 2 skipped |
| `claude` en PATH | no detectado |
| JointJS bundle | generado |
| JointJS skill instalada | sí |
| Drift local | `tests/fixtures/canarios/urgenciologo-baseline.md` |

## Invariantes

1. No hay stales en deploy.
2. Sí hay fleet Claude incompleto.
3. La entrega del server no es “verde total” hasta reparar `test_atomize.py`.
4. La línea JointJS no debe tocarse antes de cerrar la falla de atomize si el objetivo es sanear entrega.

## Próximo paso recomendado

Entrar directo por el test roto de `atomize`.

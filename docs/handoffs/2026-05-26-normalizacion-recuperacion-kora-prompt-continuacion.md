---
_manifest:
  urn: "urn:kora:kb:prompt-continuacion-2026-05-26-normalizacion-recuperacion-kora"
  provenance:
    created_by: "Codex"
    created_at: "2026-05-26"
    source: "Prompt breve de continuacion solicitado en el cierre del pase de normalizacion/recuperacion KORA."
version: "1.0.0"
status: publicado
tags: [prompt-continuacion, handoff, recuperacion, normalizacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-05-26-normalizacion-recuperacion-kora"
---

# Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el handoff:
docs/handoffs/2026-05-26-normalizacion-recuperacion-kora.md

Objetivo inmediato: revisar staging recuperado y decidir promocion, fusion o
descarte de `jobs-web-ux`, `database-designer`, `agent-architect` y `polymath`.
Usa `docs/plans/2026-05-26-normalizacion-recuperacion-kora.md` como ledger.

Restricciones: no ingerir OpenClaw MEMORY.md crudo, no promover runtime output
sin fuente revisada, no incluir secretos/PII. Verifica con
`python3 toolchain/kora recovery-inventory --json`,
`python3 toolchain/kora check --strict` y tests acotados antes de promover.
```

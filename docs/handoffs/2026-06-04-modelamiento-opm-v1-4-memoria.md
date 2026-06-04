---
_manifest:
  urn: "urn:kora:kb:memoria-modelamiento-opm-v1-4-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada del cierre modelamiento-opm v1.4.1."
version: "1.0.0"
status: publicado
tags: [memoria, modelamiento-opm, opforja, opl-es, deploy]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - modelamiento-opm v1.4.1

- `modelamiento-opm` queda en v1.4.1.
- La skill incorpora `reglas-opm-estrictas-es` y `spec-forja-opl-es`.
- AP-01 a AP-30 no se tratan todos como bloqueo: aplicar la politica exacta de
  `reglas-opm-estrictas-es` §11.
- El vocabulario OPL se toma de `spec-forja-opl-es` §1.1 completo; no usar
  conteos manuales incompletos.
- Entradas OPL GAP-* son canon textual con deuda de implementacion; no prometer
  roundtrip operacional/importable hasta cerrar §20.
- `opencode` sigue pausado en gobernanza. Para esta ronda fue desplegado con
  `--force-paused` por pedido HITL, sin agregarlo a `entornos_objetivo`.
- Runtime deploy aplicado a Claude Code, Codex, OpenCode y OpenClaw para
  `modelamiento-opm`.

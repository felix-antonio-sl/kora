---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-18-toolchain-wave1-closeout"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Memoria operativa compacta para reanudar el cierre post-ola 1 del toolchain y la integracion core de atomize."
version: "1.0.0"
status: publicado
tags: [memory, toolchain, autoria-spec, atomize, promote, closeout]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-ola1-toolchain"
    - "urn:kora:kb:handoff-2026-04-18-atomize-skill"
    - "urn:kora:kb:handoff-2026-04-18-atomize-integracion-v1"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:md-spec"
---

# Memoria operativa — cierre post-ola 1 + `atomize`

## Estado estable

- Los 7 `AGENT.md` productivos quedaron en shape `autoria-spec v1.0` con
  `descripcion`, fibra minima explicita y `0 diagnostics` bajo
  `autoria_validate`.
- Los suites legacy que bloqueaban `kora check --strict` fueron
  reescritos al shape `artefacto.*`.
- `workspace-validity`, `agentfile-dimensions`, `urn-integrity` y
  `kb-graph-cycles` ya operan sobre la ontologia unificada; los aliases
  historicos y URNs retirados no se cuentan como rotos cuando su estado
  es resoluble por contrato.
- `python3 scripts/kora check --strict` termino en verde el
  **18 de abril de 2026**: `Checks run: 12`, `Passed: 12`, `Failed: 0`.

## Estado estable de `atomize`

- `atomize` ya esta integrado al core del repo como productor canonico de
  la familia `atomic`.
- `scripts/kora_lib/promote.py` exige acceptance review fresca y aceptada
  para bundles `atomic`.
- `SKILLS/kora/atomize/scripts/publish_atomic.py` ya no mantiene logica
  divergente: delega al mismo predicado del core.
- La linea quedo cubierta por regresiones para:
  - promote `atomic` sin review
  - promote `atomic` con review stale
  - promote `atomic` con review fresca

## Deuda real remanente

1. `fidelidad-agentskills` sigue pendiente.
   `autoria-spec §5.5` ya define la proyeccion; falta cerrar el check y
   el `transmute --target agentskills` byte-identical.
2. Las runtime extensions v1.1+ siguen pendientes.
   Falta cerrar la matriz canonica
   `(arnes_categorico × forma_material × runtime)`.
3. Hay artefactos historicos en `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/`
   y handoffs viejos que aun mencionan el URN legacy
   `urn:kora:skill:atomize:1.0.0`; no bloquean el toolchain ni el
   promote, pero siguen como deuda documental/baseline.

## Higiene del worktree

- Esta sesion **no** debe mezclar `docs/generated/*`,
  `catalog/catalog_master_kora.yml` ni `KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro-curado/`
  salvo que la proxima sesion quiera hacer una pasada de sincronizacion
  documental.
- El cierre de esta sesion debe commitear solo codigo/tests/docs de la
  linea toolchain + `atomize`, no material incidental regenerado.

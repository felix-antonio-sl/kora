---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-18-atomize-delivery-closeout"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Memoria operativa compacta posterior al cierre funcional de atomize en el nuevo KORA."
version: "1.0.0"
status: publicado
tags: [memory, atomize, atomic, autoria-spec, promote, closeout]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-atomize-integracion-v1"
    - "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
    - "urn:kora:kb:operational-memory-2026-04-18-toolchain-wave1-closeout"
---

# Memoria operativa — cierre de entrega `atomize`

## Estado estable

- `atomize` ya esta entregado como productor canonico de la familia
  `atomic` dentro del nuevo KORA.
- `SKILLS/kora/atomize/SKILL.md` conforma `autoria-spec v1.0` con URN
  `urn:kora:artefacto:atomize`.
- `scripts/kora_lib/promote.py` ya es el gate canonico de publicacion
  para bundles `atomic`; exige acceptance review fresca y aceptada.
- `SKILLS/kora/atomize/scripts/publish_atomic.py` ya no mantiene logica
  divergente; valida y delega al mismo predicado del core.

## Verificacion vigente

- `python3 -m unittest tests.test_atomize tests.test_check_pipeline`
  termino en verde el **18 de abril de 2026**: `Ran 41 tests`, `OK`.
- `python3 scripts/kora check --path SKILLS/kora/atomize`
  termino en verde el **18 de abril de 2026**: `Checks run: 12`,
  `Passed: 12`, `Failed: 0`.

## Que NO volver a debatir

- No reabrir la deuda "subir el acceptance gate al core": ya esta cerrada.
- No tratar `publish_atomic.py` como fuente de verdad separada del core.
- No tratar el glosario ingles (`references`, `assets`, `Resources`) como
  shape de autoria valido para skills nuevas.

## Deuda real fuera de la entrega de `atomize`

1. `fidelidad-agentskills` sigue pendiente como deuda de interop para
   `forma_material: habilidad`.
2. Las runtime extensions v1.1+ siguen pendientes para cerrar la matriz
   `(arnes_categorico × forma_material × runtime)`.
3. Los bundles historicos `atomic-opm-libro*` y handoffs viejos todavia
   arrastran URN legacy de `atomize`; es deuda documental, no bloqueo
   funcional.
4. `atomic-opm-libro-rebuilt-*` sigue siendo baseline util pero con
   acceptance review en `reject` por `editorial_quality`.

## Higiene del worktree

- No mezclar en esta linea `docs/generated/*`,
  `catalog/catalog_master_kora.yml` ni
  `KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro-curado/` salvo que una sesion
  futura haga sincronizacion documental explicita.

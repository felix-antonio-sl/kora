---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-atomize-delivery-closeout"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Handoff explicito posterior al cierre funcional de atomize como productor canonico atomic en el nuevo KORA."
version: "1.0.0"
status: publicado
tags: [handoff, atomize, atomic, autoria-spec, promote, closeout]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-atomize-skill"
    - "urn:kora:kb:handoff-2026-04-18-atomize-integracion-v1"
    - "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
    - "urn:kora:kb:operational-memory-2026-04-18-atomize-delivery-closeout"
  refines:
    - "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
---

# Handoff explícito — entrega completa de `atomize`

## Resumen ejecutivo

La linea `atomize` queda cerrada como entrega funcional dentro del nuevo
KORA.

Lo que al inicio eran dos deudas separadas:

1. migrar la skill al shape `autoria-spec v1.0`
2. subir el acceptance gate de `atomic` al core

ya esta resuelto y verificado.

En el estado actual:

- `atomize` es el productor canonico de `atomic`
- el core y el wrapper comparten el mismo rigor de publicacion
- la deuda restante ya no es de shape ni de enforcement base

## Estado consolidado

### 1. Skill integrada al nuevo KORA

- `SKILLS/kora/atomize/SKILL.md` ya usa URN
  `urn:kora:artefacto:atomize`.
- El skill conforma `autoria-spec v1.0` y usa el glosario canonico en
  espanol.
- `ATOMIC_PRODUCER_URN` ya esta alineado en emision y validacion.

### 2. Gate de publicacion unificado

- `scripts/kora_lib/promote.py` valida acceptance review para bundles
  `atomic`.
- El gate cubre al menos:
  - review ausente
  - review stale
  - review aceptada y fresca
- `publish_atomic.py` ya no introduce una segunda politica de publicacion.

### 3. Verificacion vigente

- `python3 -m unittest tests.test_atomize tests.test_check_pipeline`
  verde.
- `python3 scripts/kora check --path SKILLS/kora/atomize`
  verde.

## Alcance del cierre

Este cierre afirma solo lo siguiente:

- `atomize` ya esta entregado al nuevo KORA
- la publicacion de `atomic` ya tiene enforcement canonico en el core
- el estado es apto para continuar con la siguiente deuda del toolchain

Este cierre NO afirma lo siguiente:

- que `atomic-opm-libro-rebuilt-*` este listo para publicar
- que `fidelidad-agentskills` este cerrada
- que la matriz completa de runtime extensions este terminada

## Deuda residual real

1. Interop `agentskills` para `forma_material: habilidad`.
2. Runtime extensions v1.1+ y su matriz canonica.
3. Armonizacion documental de bundles/handoffs historicos que todavia
   mencionan el URN legacy de `atomize`.
4. Decision editorial sobre si `atomic-opm-libro-rebuilt-*` se deja como
   baseline rechazado o se sigue curando.

## Instruccion operativa para la siguiente sesion

La siguiente sesion no debe volver a invertir tiempo en revisar si
`atomize` "ya esta o no esta" integrado.

Debe partir desde estas invariantes:

- `atomize` ya esta cerrado como linea funcional
- la deuda siguiente es de interop/proyeccion, no de capacidad base
- el commit de esta sesion debe ser solo documental

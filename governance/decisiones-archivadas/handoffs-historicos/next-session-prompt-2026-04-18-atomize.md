---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-18-atomize"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Prompt operativo para retomar la linea atomize/atomic en la sesion siguiente."
version: "1.0.0"
status: publicado
tags: [prompt, next-session, atomize, atomic, acceptance-review]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-atomize-skill"
---

# Prompt próxima sesión — `atomize`

```text
Retoma la línea `atomize` en /home/felix/kora desde el estado consolidado en `docs/reports/handoff-2026-04-18-atomize-skill.md`.

Objetivo principal:
- subir el acceptance gate de `atomic` al core del repo para que `scripts/kora promote` y el wrapper `SKILLS/kora/atomize/scripts/publish_atomic.py` tengan el mismo rigor.

Contexto que debes asumir como vigente:
- `atomize` es el productor canónico único de la familia `atomic`
- la skill ya tiene quality review, fidelity packet y acceptance review persistente
- `prepare_atomic_fidelity_review.py` prepara evidencia; no juzga semántica por sí mismo
- `atomic-opm-libro-rebuilt-*` existe como baseline útil, pero su review actual está en `reject`

Primero:
1. inspecciona `scripts/kora_lib/promote.py`, `SKILLS/kora/atomize/scripts/publish_atomic.py`, `tests/test_atomize.py` y `docs/reports/handoff-2026-04-18-atomize-skill.md`
2. diseña la subida del gate al core sin romper la promoción normal de familias no-atomic
3. agrega tests de regresión para:
   - promote de `atomic` sin acceptance review
   - promote de `atomic` con review stale
   - promote de `atomic` con review aceptada y fresca
4. solo después evalúa si conviene seguir limpiando `atomic-opm-libro-rebuilt-*` o dejarlo como baseline rechazado

Mantén el commit acotado a esa línea. No arrastres cambios no relacionados del worktree.
```

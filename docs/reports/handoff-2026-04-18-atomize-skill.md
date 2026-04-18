---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-atomize-skill"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Cierre operativo de la linea atomize/atomic: skill canonica, gates de calidad y bundles de referencia para handoff de sesion."
version: "1.0.0"
status: publicado
tags: [handoff, atomize, atomic, md-spec, knowledge-spec, skill, acceptance-review, tension]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:skill:atomize:1.0.0"
---

# Handoff sesión 2026-04-18 — `atomize` como skill canónica de `atomic`

## Resumen ejecutivo

La línea `atomize` quedó consolidada como productor canónico de la familia `atomic`, en forma de skill runtime-agnostic para Claude Code y Codex. El estado actual ya no depende de un scaffold determinista mínimo: hay recuperación de estructura para `.txt`/OCR, deduplicación multi-source, emisión de `tension` para conflictos obvios entre fuentes, review editorial, packet de fidelidad semántica y acceptance review persistente antes de publicar vía wrapper.

El cierre de sesión deja además una memoria operativa explícita, un bundle de referencia real (`opm-libro-rebuilt`) y un bundle malo conservado como contraejemplo. La deuda principal ya no es de capacidad base, sino de rigor uniforme: el acceptance gate fuerte vive en el skill wrapper, no todavía en `scripts/kora promote`.

## Estado consolidado

### 1. Productor canónico

- `SKILLS/kora/atomize/SKILL.md` declara a `atomize` como la única vía soportada para emitir artefactos `atomic`.
- `scripts/kora_lib/atomize.py` es la superficie CLI canónica del productor.
- La segmentación usa `~15.000` caracteres como referencia blanda y `200` proposiciones como máximo duro.

### 2. Calidad y fidelidad

- `review_atomic_quality.py` detecta contaminación editorial, microsegmentos y anclajes sospechosos.
- `prepare_atomic_fidelity_review.py` prepara evidencia y prioriza muestras de riesgo, especialmente `tension`, negaciones/excepciones y multi-source.
- `review_atomic_acceptance.py` persiste el veredicto (`accept|reject`), `publish_ready`, `bundle_stats` y los resultados de los gates.
- `review_atomic_fidelity.py` queda solo como alias de compatibilidad; el nombre canónico es `prepare_atomic_fidelity_review.py`.

### 3. Publicación

- `SKILLS/kora/atomize/scripts/publish_atomic.py` exige una acceptance review aceptada y fresca antes de correr `kora promote`.
- `scripts/kora_lib/promote.py` todavía no replica este gate fuerte a nivel core. Esa es la principal asimetría pendiente.

### 4. Casos de referencia

- Golden cases documentados:
  - `opm-libro` para libro `.txt` largo
  - OCR/procedimiento sucio
  - dedup multiarchivo
  - `tension` multiarchivo por número, negación y excepción
- Fixtures de test creados en `tests/fixtures/atomize/`.

## Artefactos operativos dejados versionados

- Skill y referencias:
  - `SKILLS/kora/atomize/SKILL.md`
  - `SKILLS/kora/atomize/references/*`
  - `SKILLS/kora/atomize/scripts/*`
- Core y validación:
  - `scripts/kora_lib/atomize.py`
  - `scripts/kora_lib/validation.py`
  - `scripts/kora_lib/promote.py`
- Cobertura:
  - `tests/test_atomize.py`
  - `tests/test_artifacts.py`
  - `tests/fixtures/atomize/*`
- Bundles de referencia:
  - `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-*`
  - `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-*`
  - `KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-review.md`

## Validación ejecutada

- `python3 -m pytest tests/test_atomize.py tests/test_artifacts.py -q -k 'test_atomize or atomize_skill_is_runtime_agnostic_and_llm_first'`
  - resultado: `18 passed`
- `python3 SKILLS/kora/atomize/scripts/review_atomic_acceptance.py KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-opm-libro-rebuilt-index.md --decision reject --summary 'Control de cierre previo al handoff; bundle util como referencia pero aun con residuos editoriales.'`
  - resultado: review persistente escrita
  - estado: `publish_ready: no`

No se corrió el suite completo del repo en este cierre.

## Riesgos y deuda real

### Alta prioridad

1. Subir el acceptance gate al core del repo.
   Hoy `publish_atomic.py` bloquea bien, pero `scripts/kora promote` sigue siendo más laxo. Mientras exista esa diferencia, hay dos niveles de rigor.

2. Mejorar conflictos semánticos no obvios.
   `tension` ya cubre diferencias numéricas, negaciones y excepciones explícitas. Los conflictos más sutiles siguen dependiendo de la revisión del agente.

3. Decidir si `atomic-opm-libro-rebuilt-*` se deja solo como baseline de referencia o se sigue curando hasta volverlo publicable.
   El acceptance review actual lo deja explícitamente rechazado por residuos editoriales.

### Media prioridad

4. Añadir uno o dos casos reales más, no solo fixtures sintéticos.
   Especialmente un corpus multiarchivo productivo con dedup/tension real.

5. Endurecer la plantilla de veredicto semántico.
   Hoy ya hay packet y acceptance review; todavía puede obligarse mejor el juicio explícito por muestra crítica.

## Handoff explícito

### Lo que puede asumirse al retomar

- `atomize` ya está alineado mecánicamente con `md-spec` para `atomic`.
- El skill ya guía mucho mejor la atomización que al inicio, sobre todo en `.txt`/OCR.
- Hay una base de tests y golden cases suficiente para seguir endureciendo sin empezar de cero.

### Lo que NO debe asumirse

- No asumir que `lint OK` equivale a fidelidad suficiente.
- No asumir que `scripts/kora promote` ya impone el mismo gate que `publish_atomic.py`.
- No asumir que `atomic-opm-libro-rebuilt` está listo para publicar; el review vigente lo rechaza.

## Prompt de continuación

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

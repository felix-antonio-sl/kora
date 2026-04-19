---
_manifest:
  urn: "urn:kora:kb:catalogo-patrones-skills"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-19"
    source: "Cierre H17: destila patrones de skills desde la skill productiva atomize y el staging activo en _TALLER/INBOX y _FRAGUA/INBOX."
version: "1.0.0"
status: publicado
tags: [skills, patterns, catalog, staging, kora]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:runtime-spec-md"
---

# Catalogo de patrones de skills en KORA

## 1. Base empirica

Este catalogo no se deriva solo de skills productivas. Usa dos fuentes:

- skill productiva: `artifacts/skills/kora/atomize/SKILL.md`
- staging activo relevante:
  - `artifacts/skills/_TALLER/INBOX/{arquitecto-categorico,data-modeling,graphic-design,transmute-claude-code,transmute-openclaw,ux-design,atomize}/`
  - skills embebidas en agentes de `artifacts/agents/_FRAGUA/INBOX/`

La decision es explicita: para H17, staging cuenta como corpus activo porque
la muestra productiva todavia es demasiado pequena para inducir patrones sin
sobreajuste.

## 2. Patrones canonicos

### P1. Skill-productor

La skill no solo asesora: produce un artefacto con workflow gobernado y
scripts auxiliares verificables.

Evidencia:

- `atomize` productiva
- `transmute-claude-code`
- `transmute-openclaw`

Shape:

- `SKILL.md` como interfaz humana
- `scripts/` como ejecucion mecanica
- `referencias/` como contrato epistemico

### P2. Skill de traduccion estructural

La skill toma un corpus o IR y lo proyecta a otra forma manteniendo
invariantes declarados.

Evidencia:

- `atomize`
- `data-modeling`
- `arquitecto-categorico`
- `transmute-*`

Operacion dominante:

- traducir sin colapsar estructura relevante

### P3. Skill guiada por corpus

La autoridad vive en `referencias/`, no en prosa libre del prompt.

Evidencia:

- `atomize`
- `arquitecto-categorico`
- `ux-design`

Regla:

- la skill debe poder explicar desde que corpus decide y que parte del corpus
  gobierna cada salida

### P4. Skill con productor y gate

La skill valida que su output no solo exista, sino que cumpla gates
semanticos, de calidad o aceptacion.

Evidencia:

- `atomize` (quality, fidelity, acceptance)
- skills embebidas en `kora/clawforge`

### P5. Skill de progressive disclosure

La interfaz principal se mantiene compacta y delega profundidad a recursos o
scripts concretos, en lugar de inflar `SKILL.md`.

Evidencia:

- `atomize`
- staging de `arquitecto-categorico`
- staging de `data-modeling`

## 3. Anti-patrones

- skill monolitica sin `referencias/` ni `scripts/`
- skill que mezcla guidance y plumbing operativo en la misma superficie
- skill que afirma autoridad pero no declara corpus
- skill que promete outputs mecanicos sin gate de validacion
- skill embebida que no deja claro si es reusable o local al agente

## 4. Decision operativa

Mientras el fleet productivo de skills siga pequeno, este catalogo funciona
como referencia de curaduria para promociones desde `_TALLER` y `_FRAGUA`.

Cuando existan al menos tres skills productivas heterogeneas, KORA DEBERIA
revisar este catalogo y separar:

- patrones confirmados por productivo
- patrones provisionales inferidos desde staging

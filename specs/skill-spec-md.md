---
_manifest:
  urn: "urn:kora:kb:skill-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 02, KORA/Agent-Spec v8.0.0"
version: "3.0.0"
status: published
tags: [spec, skill, cm, lazy-load, grammar]
lang: es
---

# KORA/Skill-Spec v3.0.0

## 1. Definicion

Un Skill es una capacidad ejecutable lazy-load. Puede existir como:

1. Skill degenerado: archivo `CM-*.md`
2. Skill extendido: directorio con `SKILL.md`

Ambas formas comparten la misma identidad: `urn:{namespace}:skill:{id}:{version}`.

## 2. Skill degenerado

Reglas:

1. Vive dentro de `skills/`.
2. Usa frontmatter con `_manifest.type = lazy_load_endofunctor`.
3. Usa identidad `skill`, nunca `agent-bootstrap`.
4. Debe tener exactamente estas secciones canónicas:
   - `## Proposito`
   - `## Input/Output`
   - `## Procedimiento`
   - `## Signature Output`

## 3. Skill extendido

Topologia:

```text
{skill}/
  SKILL.md
  scripts/
  references/
  assets/
```

`SKILL.md` preserva el mismo CM Core que el skill degenerado y agrega metadata o capacidades auxiliares.

## 4. Relacion entre ambas formas

- Wrap: CM -> Skill extendido
- Extract: Skill extendido -> CM Core

El extracto de un Skill extendido **DEBE** seguir siendo un Skill degenerado válido.

Traces to: formal/02 §2.3 (eta-like preservation)

## 5. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Identidad skill | Todo skill usa URN `skill` | lint | Migrar URN |
| Grammar canonica | Existen las 4 secciones exactas | lint | Normalizar headings |
| Lazy load | El skill no vive inline en bootstrap | lint | Extraer a `skills/` |
| Extract preserva core | Un skill extendido conserva CM Core valido | manual | Reescribir `SKILL.md` |

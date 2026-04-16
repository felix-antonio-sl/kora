---
_manifest:
  urn: urn:dev:skill:prompt-craft:1.1.0
  type: lazy_load_endofunctor
---

## Proposito

Escribir prompts efectivos para obreros de codigo. Minimos, con intencion, no sintaxis.

## Input/Output

- **Input:** WorkPackage + modelo target + contexto del repo
- **Output:** Prompt optimizado para el obrero

## Procedimiento

1. Empezar con intencion en 1-2 oraciones: que debe lograr el obrero.
2. Incluir archivos target especificos.
3. Referir a CONVENTIONS.md / SCHEMA.md del repo si existen.
4. Especificar close-the-loop criteria: "compile, lint, test before committing".
5. Si es cambio visual: incluir screenshot o referencia visual.
6. NO incluir: sintaxis exacta, implementacion paso-a-paso, motivacion excesiva.
7. Trigger words para tareas complejas: "take your time", "comprehensive", "read all related code", "create hypothesis".

## Signature Output

```
## Prompt para [modelo]
[Prompt de 1-5 lineas con intencion clara]
```

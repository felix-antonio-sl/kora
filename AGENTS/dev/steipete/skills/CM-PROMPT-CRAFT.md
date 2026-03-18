---
_manifest:
  urn: urn:dev:skill:prompt-craft:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Escribir prompts efectivos para obreros de código. Mínimos, con intención, no sintaxis.

## Input/Output

- **Input:** WorkPackage + modelo target + contexto del repo
- **Output:** Prompt optimizado para el obrero

## Procedimiento

1. Empezar con intención en 1-2 oraciones: qué debe lograr el obrero.
2. Incluir archivos target específicos.
3. Referir a CONVENTIONS.md / SCHEMA.md del repo si existen.
4. Especificar close-the-loop criteria: "compile, lint, test before committing".
5. Si es cambio visual: incluir screenshot o referencia visual.
6. NO incluir: sintaxis exacta, implementación paso-a-paso, motivación excesiva.
7. Steinberger: "Often it's just 1-2 sentences + an image."
8. Trigger words para tareas complejas: "take your time", "comprehensive", "read all related code", "create hypothesis".

## Signature Output

```
## Prompt para [modelo]
[Prompt de 1-5 líneas con intención clara]
```

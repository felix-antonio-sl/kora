---
_manifest:
  urn: "urn:korvo:skill:korax-problem-solver:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Resolución estructurada de problemas complejos. Combina problem framing, root cause analysis y generación de soluciones para ayudar al operador a abordar retos que no se resuelven con una simple captura al GTD.

## I/O

- **Input:** problem_description: string, context: {domain, prior_attempts, resources}
- **Output:** solution_plan: {problem_statement, root_causes[], options[], recommendation, action_plan}

## Procedimiento

1. **Problem Framing** — definir el problema con 5 preguntas:
   - ¿Cuál es el problema específico?
   - ¿Qué impacto tiene en tu vida/trabajo?
   - ¿Qué ya intentaste?
   - ¿Qué recursos tienes?
   - ¿Cómo se vería el éxito?

2. **Root Cause Analysis** — separar síntomas de causas:
   - Identificar patrones recurrentes
   - Buscar la causa detrás de la causa
   - Producir 2-3 causas raíz principales

3. **Solution Generation** — mínimo 3 opciones viables:
   - Evaluar pros/cons de cada una
   - Considerar esfuerzo vs impacto
   - Incorporar experiencias pasadas del operador si relevantes
   - web_search si necesita información factual

4. **Recommendation** — recomendar con fundamento:
   - Opción recomendada con razón
   - Plan de acción con pasos concretos
   - Métricas de éxito
   - Timeline estimado

### Puente con GTD

Si la solución produce acciones concretas y el operador quiere capturarlas:
- Preguntar: "¿capturo estas acciones?" (INV-16).
- Si sí → capturar cada acción como /inbox → sistema GTD se encarga.

## Signature Output

```
🔍 Problema
{Definición clara}

Causas Raíz
1. {causa 1}
2. {causa 2}

Opciones
| Opción | Pros | Contras | Esfuerzo |
|--------|------|---------|----------|
| A | ... | ... | ... |
| B | ... | ... | ... |
| C | ... | ... | ... |

Recomendación
{Opción + razón + plan de acción}
```

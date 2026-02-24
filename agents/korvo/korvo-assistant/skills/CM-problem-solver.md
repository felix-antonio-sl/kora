---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korvo-assistant-cm-problem-solver:1.0.0"
  type: "lazy_load_endofunctor"
---

## Purpose

Motor de resolucion de problemas que combina problem framing, root cause analysis y generacion de soluciones para ayudar a Felix a abordar retos complejos de forma estructurada.

## Input/Output

- **Input:** problem_description: string, context: {domain, prior_attempts, resources}
- **Output:** solution_plan: {problem_statement, root_causes, options, recommendation, action_plan}

## Procedure

1. **Problem Framing** — Definir problema claramente:
   - Cual es el problema especifico?
   - Que impacto tiene?
   - Que ya intentaste?
   - Que recursos tienes?
   - Cual seria el exito?

2. **Root Cause Analysis** — Identificar causas raiz:
   - Separar sintomas de causas
   - Buscar patrones recurrentes
   - Identificar 2-3 causas principales

3. **Solution Generation** — Generar opciones:
   - Minimo 3 opciones viables
   - Evaluar pros/cons de cada una
   - Considerar esfuerzo vs impacto
   - Incorporar experiencias pasadas relevantes

4. **Recommendation** — Recomendar con fundamento:
   - Opcion recomendada con razon
   - Plan de accion con pasos concretos
   - Metricas de exito
   - Timeline estimado

## Signature Output

```markdown
### Problema
[Definicion clara]

### Causas Raiz
1. [causa 1]
2. [causa 2]

### Opciones
| Opcion | Pros | Cons | Esfuerzo |
|--------|------|------|----------|
| A | ... | ... | ... |

### Recomendacion
[Opcion + razon + plan]
```

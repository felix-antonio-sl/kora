---
_manifest:
  urn: urn:dev:skill:tooling-advisor:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Asesorar sobre seleccion de herramientas, modelos y CLIs para tareas de desarrollo, consultando el inventario de tooling.

## Input/Output

- **Input:** Pregunta sobre herramientas, modelos, routers, o criterio de seleccion (costo, calidad, context window)
- **Output:** Recomendacion fundamentada con referencia al inventario de tooling

## Procedimiento

1. Consultar inventario via search_tooling con query y categoria apropiada (cli, model, router).
2. Evaluar opciones contra criterios de la tarea: costo, calidad, context window, strengths/weaknesses.
3. Si search_tooling no retorna resultado claro, usar defaults de model_routing como fallback.
4. Formular recomendacion con justificacion concreta.
5. Si datos parecen obsoletos (>30 dias), senalar al operador.

## Signature Output

```
## Tooling Recommendation
- Tarea: [descripcion]
- Recomendacion: [modelo/CLI]
- Razon: [justificacion]
- Alternativa: [si aplica]
- Referencia: [ficha de inventario consultada]
```

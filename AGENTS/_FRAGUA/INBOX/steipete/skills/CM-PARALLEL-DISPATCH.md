---
_manifest:
  urn: urn:dev:skill:parallel-dispatch:1.2.0
  type: lazy_load_endofunctor
---

## Proposito

Definir estrategia de despacho: cuantos obreros, que modelo para cada uno, en que orden, con que prompts.

## Input/Output

- **Input:** Lista de WorkPackages + contexto de modelos disponibles
- **Output:** Plan de despacho: { workers: [{ package_id, model, worktree, prompt_draft }], orden_de_grupos }

## Procedimiento

1. Consultar `search_tooling` con la naturaleza de cada paquete para obtener modelo optimo costo/calidad.
2. Si search_tooling no retorna resultado claro, usar defaults de model routing como fallback.
3. Seleccionar CLI sin preferencia de vendor: Claude Code, Codex CLI, Gemini CLI y OpenCode son igualmente validos. La seleccion depende del modelo optimo para la tarea.
4. Asignar worktree si hay multiples obreros en paralelo (evitar conflictos en working directory).
5. Para cada paquete, registrar en el plan: modelo, CLI, worktree y referencia al paquete.
6. Organizar workers en grupos por dependencia: paquetes independientes en el mismo grupo, paquetes dependientes en grupos secuenciales.
7. Si costos son una preocupacion, preferir modelo budget que cumpla calidad minima para la tarea.

## Signature Output

```
## Dispatch Plan
| Worker | Paquete | Modelo | Worktree | Grupo |
|--------|---------|--------|----------|-------|
| W1     | #1      | codex  | wt-1     | A     |
| W2     | #2      | claude | wt-2     | A     |
| W3     | #3      | codex  | main     | B     |
```

---
_manifest:
  urn: urn:dev:skill:parallel-dispatch:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Definir estrategia de despacho: cuántos obreros, qué modelo para cada uno, en qué orden, con qué prompts.

## Input/Output

- **Input:** Lista de WorkPackages + contexto de modelos disponibles
- **Output:** Plan de despacho: { workers: [{ package_id, model, worktree, prompt_draft }], orden_de_grupos }

## Procedimiento

1. Consultar `search_tooling` con la naturaleza de cada paquete para obtener modelo óptimo costo/calidad.
2. Aplicar configuración operativa por defecto:
   - Implementación nueva → Claude Code + Opus 4.6 (1M context, máxima calidad)
   - Refactoring/cleanup → Claude Code + Opus 4.6 (reestructuración profunda)
   - Review → Codex CLI + GPT-5.4 (diversidad de blind spots vs implementador)
   - Bug fix simple → Claude Code + Sonnet 4.6 o Gemini CLI + Flash (según costo)
   - Bulk/repetitivo → OpenCode + DeepSeek V3.2 o Gemini CLI free tier
3. Seleccionar CLI sin preferencia de vendor: Claude Code, Codex CLI, Gemini CLI y OpenCode son igualmente válidos. La selección depende del modelo óptimo para la tarea.
4. Asignar worktree si hay múltiples obreros en paralelo (evitar conflictos en working directory).
5. Invocar CM-PROMPT-CRAFT para cada paquete.
6. Despachar grupo A en paralelo → esperar → despachar grupo B → etc.
7. Si costos son una preocupación, preferir modelo budget que cumpla calidad mínima para la tarea.

## Signature Output

```
## Dispatch Plan
| Worker | Paquete | Modelo | Worktree | Grupo |
|--------|---------|--------|----------|-------|
| W1     | #1      | codex  | wt-1     | A     |
| W2     | #2      | claude | wt-2     | A     |
| W3     | #3      | codex  | main     | B     |
```

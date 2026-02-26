---
_manifest:
  urn: "urn:gn:skill:arquitecto-automatizacion-organizacional-llm-engineering:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Aplicar mejores practicas de ingenieria de LLMs al disenar e implementar agentes y flujos con modelos de lenguaje.

## I/O

- **Input:** Diseno de agente o flujo que involucra LLM
- **Output:** Implementacion con mejores practicas aplicadas (prompt, contexto, errores, costos, observabilidad)

## Procedimiento

1. Prompt Design:
   - System prompt claro con rol, contexto, restricciones
   - Few-shot examples para tareas complejas
   - Output format explicito (JSON, markdown)
   - Instrucciones especificas > vagas

2. Context Management:
   - Mantener contexto relevante, descartar ruido
   - Chunking apropiado para documentos largos
   - Metadata para filtrado y relevancia
   - Limites de tokens conscientes

3. Error Handling:
   - Validar outputs del LLM
   - Retry con backoff exponencial
   - Fallbacks para casos de falla
   - Logging de inputs/outputs

4. Cost Optimization:
   - Modelo apropiado para la tarea (no siempre el mas grande)
   - Caching de respuestas repetibles
   - Batch processing cuando posible
   - Monitoreo de costos por flujo

5. Observability:
   - Traces de cada llamada
   - Metricas de latencia y tokens
   - Logs estructurados
   - Evaluacion de calidad

## Signature Output

System prompt disenado + Tool definitions + Error handling strategy + Cost estimate + Observability plan.

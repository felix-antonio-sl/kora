---
_manifest:
  urn: "urn:gn:agent-bootstrap:arquitecto-automatizacion-organizacional-cm-automation-patterns:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Seleccionar y aplicar patrones de automatizacion e integracion apropiados para cada oportunidad identificada.

## Input/Output

- **Input:** Oportunidad de automatizacion con clasificacion y contexto
- **Output:** Patron seleccionado con componentes, integraciones y arquitectura propuesta

## Procedimiento

1. Evaluar patron de automatizacion apropiado:
   - Workflow Orchestration: secuencia pasos automatizados. Trigger -> Steps -> Output. Para procesos con pasos definidos y predecibles.
   - Agent with Tools: LLM que decide que herramientas usar. System prompt + Tools + Memory. Para tareas que requieren razonamiento y multiples acciones.
   - RAG Retrieval: recuperacion informacion para contexto. Vector store + Retriever + LLM. Para preguntas sobre documentos o knowledge bases.
   - Human-in-the-Loop: puntos decision humana en flujo automatizado. Automation + Approval step + Notification. Para decisiones alto impacto o casos edge.
   - Event-Driven: reaccion a eventos del sistema. Event source + Handler + Actions. Para integraciones en tiempo real.

2. Evaluar patron de integracion:
   - API Integration: llamadas HTTP. Considerar auth, rate limits, retry, error handling.
   - Webhook Trigger: eventos externos inician flujos. Considerar validacion, idempotencia, seguridad.
   - Database Sync: sincronizacion datos entre sistemas. Considerar conflictos, consistencia, latencia.
   - File Processing: procesar documentos. Considerar formatos, tamano, parsing.

3. Disenar arquitectura: componentes + interfaces + flujo de datos

## Signature Output

Patron seleccionado + Componentes (tabla) + Diagrama arquitectura + Integraciones requeridas + Consideraciones (errores, edge cases, costos).

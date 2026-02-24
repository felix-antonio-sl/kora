---
_manifest:
  urn: "urn:gn:agent-bootstrap:dgi-virtual-cm-dmaic-evaluator:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Evaluar en que fase DMAIC (Define-Measure-Analyze-Improve-Control) esta un proyecto de mejora de procesos y guiar hacia la siguiente fase.

## Input/Output

- **Input:** Descripcion del proyecto de mejora, estado actual, entregables existentes
- **Output:** Fase DMAIC actual, entregables pendientes, preguntas diagnosticas, recomendacion de avance

## Procedimiento

1. Evaluar fase DEFINE:
   - Entregables esperados: Charter, Alcance, Stakeholders, Caso negocio
   - Preguntas: Esta definido el problema? Hay objetivos SMART?
   - Si incompleto: guiar a completar Define

2. Evaluar fase MEASURE:
   - Entregables esperados: Linea base, VSM AS-IS, Datos recopilados
   - Preguntas: Hay metricas actuales? Se valido el sistema de medicion?
   - Si incompleto: guiar a completar Measure

3. Evaluar fase ANALYZE:
   - Entregables esperados: Causa raiz, 5 Porques, Pareto
   - Preguntas: Se identificaron las causas? Hay priorizacion por impacto?
   - Si incompleto: guiar a completar Analyze

4. Evaluar fase IMPROVE:
   - Entregables esperados: Diseno TO-BE, Prototipo, Piloto
   - Preguntas: Hay solucion disenada? Se piloteo?
   - Si incompleto: guiar a completar Improve

5. Evaluar fase CONTROL:
   - Entregables esperados: Controles, Estandares, Alertas
   - Preguntas: Hay controles en lugar? Esta documentado?
   - Si incompleto: guiar a completar Control

6. Determinar fase actual y proponer proximos pasos

## Signature Output

Fase DMAIC actual + Entregables existentes vs pendientes (tabla) + Preguntas diagnosticas + Recomendacion proxima fase con entregables esperados.

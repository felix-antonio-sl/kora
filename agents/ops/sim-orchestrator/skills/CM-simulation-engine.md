---
_manifest:
  urn: "urn:kora:agent-bootstrap:sim-orchestrator-cm-simulation-engine:1.0.0"
  type: "lazy_load_endofunctor"
---

## Purpose

Motor de simulacion que asume la identidad del agente TARGET para generar respuestas basadas en su spec. Ejecuta el ciclo completo de cambio de identidad, procesamiento y restauracion.

## Input/Output

- **Input:** test_case: {id, type, prompt}, target_agent: {name, spec, states}
- **Output:** simulated_response: {test_id, response, evidence_type: SIMULATED}

## Procedure

1. Obtener test actual del test_suite
2. CAMBIAR IDENTIDAD → TARGET: adoptar role, objective, states del spec cargado
3. Procesar prompt segun spec del TARGET:
   - Identificar estado FSM correspondiente
   - Ejecutar process del estado
   - Evaluar transitions
   - Generar respuesta como lo haria el TARGET
4. RESTAURAR IDENTIDAD → SIM-ORCHESTRATOR
5. Marcar respuesta como evidence_type: SIMULATED
6. Retornar evidencia con metadata

## Signature Output

```yaml
evidence:
  test_id: "T-001"
  test_type: "STATE_COVERAGE"
  prompt: "[input del test]"
  simulated_response: "[respuesta generada como TARGET]"
  evidence_type: SIMULATED
  target_state: "S-XXX"
```

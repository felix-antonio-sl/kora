---
name: eval-architecture
description: Design evaluation architectures for agentic systems. Use when the user needs to establish how agent outputs are validated, who evaluates, what data is used, and how evaluation independence is maintained. Covers eval debt diagnosis and remediation.
---

# Eval Architecture

Disenar arquitecturas de evaluacion para sistemas agenticos.

## Cuando activar

- El usuario quiere disenar como se evaluan outputs de agentes.
- Hay sospechas de eval debt (tests pasan pero regresiones reales aparecen).
- Necesita separar autor de evaluador.
- Quiere establecer datasets, policies o pipelines de evaluacion.

## Procedimiento

1. **Auditar estado actual.** Que se evalua hoy? Quien evalua? Con que datos?
2. **Identificar eval debt.** Donde la validacion es fragil, incompleta o dependiente del autor?
3. **Disenar independencia.** Separar autor, evaluador y dataset. Minimo: evaluador != autor.
4. **Definir niveles de eval.**
   - L1: Sintactico (compila, formatos correctos, constraints satisfechas).
   - L2: Semantico (el output responde a la intencion).
   - L3: De riesgo (el output no introduce dano, regresion o vulnerabilidad).
   - L4: De valor (el beneficiario confirma que el resultado es util).
5. **Disenar datasets.** Casos positivos, negativos, edge cases, datos de produccion anonimizados.
6. **Establecer cadencia.** Que evals corren en cada commit, cuales semanalmente, cuales trimestralmente.
7. **Disenar alertas.** Que dispara intervencion humana.
8. **Documentar.** Producir artefacto de arquitectura de eval.

## Formato de salida

```
## Eval Architecture: {scope}
- Estado actual: {resumen de evaluacion existente}
- Eval debt identificada: {lista}
- Independencia: {quien evalua vs quien produce}
- Niveles activos:
  - L1 (sintactico): {que, como, frecuencia}
  - L2 (semantico): {que, como, frecuencia}
  - L3 (riesgo): {que, como, frecuencia}
  - L4 (valor): {que, como, frecuencia}
- Datasets: {descripcion y ubicacion}
- Alertas: {condiciones de escalamiento}
- Cadencia de meta-eval: {cada cuanto se evalua la evaluacion misma}
```

## Gotchas

- El verde del pipeline no basta. Se necesita validacion semantica y de riesgo.
- Si el mismo agente que genera evalua su propio output, no hay eval real.
- Eval debt es invisible hasta que explota en produccion.
- Demasiados evals irrelevantes son eval theatre, no eval architecture.

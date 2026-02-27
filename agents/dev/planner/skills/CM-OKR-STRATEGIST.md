---
_manifest:
  urn: "urn:dev:skill:planner-okr-strategist:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-OKR-STRATEGIST

## Proposito
Estructura OKRs para un Ciclo (4-6 semanas): Objetivos cualitativos + Key Results analogos. Deriva epicas necesarias. Estima presupuesto de tokens.

## Procedimiento
1. Elicitar contexto de negocio: que problema se resuelve, para quien, que metricas importan, que se aprendio del Ciclo anterior.
2. Proponer 1-3 Objetivos cualitativos alineados con el Higher Purpose (Kelly).
3. Para cada Objetivo, derivar 2-4 Key Results:
   - DEBEN ser analogos (gradiente medible): "Reducir X de A a B" no "Implementar X".
   - DEBEN ser medibles con datos disponibles.
   - DEBERIAN tener baseline y target explicitos.
4. Reservar BAU como Objetivo 0 (20-30% presupuesto tokens).
5. Estimar presupuesto de tokens por partida: 60-70% historias, 20-25% BAU, 10-15% calibracion.
6. Derivar epicas necesarias para lograr cada KR.
7. Presentar OKRs en tabla para aprobacion del PO.

## Output
Tabla OKRs: {objetivo, key_results: [{kr, baseline, target}], epicas_derivadas[], presupuesto_tokens}. Listo para aprobacion.

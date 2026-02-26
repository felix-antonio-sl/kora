---
_manifest:
  urn: "urn:fxsl:skill:analyst-retro-reporter:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-RETRO-REPORTER

## Proposito
Genera el reporte de Retrospectiva Analitica para fin de Ciclo: datos consolidados para que PO y Operador tomen decisiones informadas.

## Input/Output
- **Input:** Metricas del Ciclo (via CM-METRICS-COLLECTOR), OKRs del Ciclo con progreso, patrones de rechazo observados, gaps de evals detectados, tarjetas purpura del sentinel (si disponibles).
- **Output:** Reporte estructurado con 4 secciones: progreso OKRs, analisis de costes, patrones de calidad, propuestas de ajuste.

## Procedimiento
1. Seccion PROGRESO OKRs:
   - Tabla por Objetivo: {objetivo, kr, baseline, target, actual, %_completado}.
   - Destacar KRs con progreso <30% o >90%.
   - Sin juicios de valor: reportar numeros, el PO interpreta.
2. Seccion ANALISIS DE COSTES:
   - Presupuesto total asignado vs consumido.
   - Desglose por partida: historias (development), BAU (mantenimiento), calibracion (evals y ajustes).
   - CpH del Ciclo vs CpH planificado (si existia estimacion).
   - Costo por zona del codebase (si datos disponibles).
3. Seccion PATRONES DE CALIDAD:
   - TA del Ciclo.
   - Tipos de rechazo: clasificar por categoria (bug, alucinacion, scope creep, format).
   - Frecuencia de rechazo por agente (si datos disponibles).
   - Gaps de evals: areas sin cobertura de testing detectadas.
4. Seccion PROPUESTAS DE AJUSTE:
   - Basadas exclusivamente en datos de las 3 secciones anteriores.
   - Formato: {observacion, dato_soporte, ajuste_posible}.
   - Tipos: cambio_modelo, ajuste_context_engineering, nuevo_eval, reconfig_topologia.
   - Estas son OBSERVACIONES para consideracion del PO/Operador, NO prescripciones.
5. Anexar tarjetas purpura del sentinel si disponibles (referencia, no duplicar contenido).
6. Validar: 4 secciones presentes, toda metrica con fuente.

## Signature Output
Reporte Markdown con 4 secciones H3: ### Progreso OKRs, ### Analisis de Costes, ### Patrones de Calidad, ### Propuestas de Ajuste. Tablas en cada seccion. Fuentes citadas.

---
_manifest:
  urn: urn:pro:skill:salubrista-quality-auditor:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-QUALITY-AUDITOR

## Proposito
Conducir auditorías en salud y ciclos de mejora continua. Trasciende lo punitivo: cultura de aprendizaje y seguridad. Evalúa concordancia entre práctica clínica/operativa y estándares. Produce hallazgos clasificados y plan de mejora basado en evidencia. Alineado con Plan de Acción Mundial para la Seguridad del Paciente 2021-2030.

## Input/Output
- **Input:** alcance: string (qué se audita: proceso, unidad, servicio, programa), datos: object (registros, trazabilidad disponible, guías de referencia)
- **Output:** AuditReport { alcance, criterios_evaluacion, hallazgos[], plan_mejora[], kpis_seguimiento[], trazabilidad_normativa }

## Procedimiento
1. DEFINIR ALCANCE: ¿qué proceso/servicio/programa se audita? ¿Qué GPC o estándar de referencia aplica? ¿Auditoría concurrente o retrospectiva?
2. CONSULTAR kb_route → `urn:pro:kb:gestion-redes-general` (Cap 4: Calidad y seguridad del paciente) + sección específica del dominio auditado.
3. DEFINIR CRITERIOS DE EVALUACIÓN:
   - Fuente: GPC vigente / NT MINSAL / estándar acreditación / guía internacional (IHI, NICE, Joint Commission, AHRQ)
   - Estructura (Donabedian): estructura → proceso → resultado
   - 6 aims IOM: safe, effective, patient-centered, timely, efficient, equitable — identificar cuáles aplican
4. RECOLECTAR EVIDENCIA: analizar trazabilidad disponible (registros, HCE, RIPS, estadísticas operacionales, CMBD). Identificar fuentes de dato para cada criterio.
5. IDENTIFICAR HALLAZGOS: comparar práctica vs. criterio. Para cada desviación:
   - Clasificar severidad: **Crítico** (riesgo vida/daño permanente/evento centinela) | **Moderado** (impacto seguridad/calidad, requiere corrección) | **Leve** (desviación menor, mejora recomendada)
   - Evaluar impacto en seguridad del paciente
   - Si evento centinela: activar RCA (Root Cause Analysis) — diagrama de causas, factores contribuyentes
6. PDSA como ciclo operativo:
   - Plan: acciones correctivas propuestas, responsable, cronograma
   - Do: descripción de implementación
   - Study: indicadores para medir impacto del cambio
   - Act: cómo se institucionaliza la mejora
7. PLAN DE MEJORA: por cada hallazgo Crítico o Moderado → acción correctiva + responsable + plazo + indicador de impacto + método de seguimiento.
8. KPIs DE SEGUIMIENTO: formato estándar (Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad).
9. TRAZABILIDAD NORMATIVA: citar norma/guía para cada criterio evaluado.

## Signature Output
| Campo | Tipo | Descripción |
|-------|------|-------------|
| alcance | string | Proceso/servicio/programa auditado |
| tipo_auditoria | string | Concurrente / Retrospectiva |
| criterios_evaluacion | string[] | GPC/estándares de referencia usados |
| hallazgos | Hallazgo[] | {descripcion, severidad, impacto, RCA si centinela} |
| plan_mejora | AccionMejora[] | {accion, responsable, plazo, indicador_impacto} |
| kpis_seguimiento | KPISpec[] | Indicadores para monitorear mejora |
| trazabilidad_normativa | string[] | Norma/guía por criterio |
| resumen_ejecutivo | string | 3-5 líneas: hallazgos principales + recomendación prioritaria |

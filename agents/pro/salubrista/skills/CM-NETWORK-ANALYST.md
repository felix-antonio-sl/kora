---
_manifest:
  urn: urn:pro:skill:salubrista-network-analyst:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-NETWORK-ANALYST

## Proposito
Analizar problemas de gestión de redes asistenciales (FIRS Dim III): diseño, operación y mejora de sistemas de salud. Aplica frameworks de finalidad (VBHC, Quadruple Aim), operación (HRO, quality, EBMgt) e instrumentación (BSC, SWOT). Systems thinking como gramática integradora. Base: corpus gestión-redes (36 capítulos + 11 anexos).

## Input/Output
- **Input:** problema: string, contexto: object (tipo de unidad, nivel de red, datos disponibles, normativa local si aplica)
- **Output:** NetworkAnalysis { subcapa: string, marcos_aplicados: string[], análisis: string, recomendaciones: string[], kpis_propuestos: KPISpec[], trazabilidad: string[], riesgos: string[] }

## Procedimiento
1. CONSULTAR kb_route → corpus gestión-redes (sección más relevante al problema: general, unidades, urgencias, salud-mental o herramientas). Verificar corpus antes de usar web o modelo.
2. POSICIONAR en Dim III. Identificar nivel: macro (red/sistema) / meso (establecimiento) / micro (unidad/servicio).
3. IDENTIFICAR SUBCAPA:
   - **Finalidad**: ¿el problema es de dirección estratégica? → VBHC / Quadruple Aim
   - **Operación**: ¿el problema es de cómo funciona el sistema? → HRO / Quality & Patient Safety / EBMgt
   - **Instrumentación**: ¿el problema es de medición? → BSC / SWOT (subordinados a marcos de operación)
   - WARNING: herramientas (BSC, SWOT) ≠ marcos (HRO, VBHC). No confundir.
4. APLICAR SYSTEMS THINKING: mapear interdependencias y bucles de retroalimentación. Identificar efectos no intencionales de posibles intervenciones. ¿El sistema es complejo-adaptativo? ¿Hay resistencia al cambio?
5. SI PROBLEMA DE FINALIDAD (VBHC / Quadruple Aim):
   - VBHC: Valor = outcomes relevantes paciente / costo total ciclo atención. Identificar segmento demográfico, diseñar trayectoria integrada multidisciplinaria, conectar clínica + procesos + costos.
   - Quadruple Aim: mapear los 4 vectores (experiencia paciente, salud poblacional, costo per cápita, bienestar equipo). ¿Cuál está comprometido?
6. SI PROBLEMA DE OPERACIÓN:
   - HRO: aplicar 5 principios mindful organizing (preocupación por fracaso, reticencia a simplificar, sensibilidad a operaciones, resiliencia, deferencia a experticia). ¿Near-misses estudiados? ¿Deferencia a primera línea en crisis?
   - Quality & Patient Safety: 6 aims IOM (safe, effective, patient-centered, timely, efficient, equitable). ¿Cuál/cuáles comprometidos? → indicadores específicos
   - EBMgt 6A: Ask (pregunta gerencial) → Acquire (evidencia interna + externa) → Appraise (calidad evidencia) → Aggregate (triangular) → Apply (implementar) → Assess (medir impacto). Rechazar decisiones basadas en anécdota o moda.
7. SI PROBLEMA DE INSTRUMENTACIÓN:
   - BSC 4 perspectivas: paciente, financiera, procesos internos, crecimiento/aprendizaje → mapear KPIs
   - SWOT: lectura situacional. Declarar su limitación: no modela causalidad, no prioriza dinámica temporal. Subordinar a systems thinking.
8. PROPONER RECOMENDACIONES: con evidencia (OPS/OMS/IHI/NICE/AHRQ + normativa local si disponible). Si web_search requerido para evidencia actualizada → ejecutar y citar.
9. PROPONER KPIs donde aplique: formato estándar (Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad).
10. IDENTIFICAR RIESGOS: por cada recomendación, ¿riesgo de consecuencia no intencional (systems thinking)? → declarar mitigación.

## Signature Output
| Campo | Tipo | Descripción |
|-------|------|-------------|
| nivel_red | string | macro / meso / micro |
| subcapa | string | finalidad / operación / instrumentación |
| marcos_aplicados | string[] | VBHC, Quadruple Aim, HRO, EBMgt, BSC, SWOT, etc. |
| análisis | string | Diagnóstico sistémico del problema |
| recomendaciones | string[] | Recomendaciones con evidencia y fuente |
| kpis_propuestos | KPISpec[] | KPIs con fórmula, meta, benchmark, fuente, periodicidad |
| trazabilidad | string[] | Normativa / guías citadas |
| riesgos | string[] | Riesgo → mitigación (systems thinking) |

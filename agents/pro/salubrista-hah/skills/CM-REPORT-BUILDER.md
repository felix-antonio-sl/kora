---
_manifest:
  urn: "urn:pro:skill:salubrista-hah-report-builder:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-REPORT-BUILDER

## Propósito
Construir informes estructurados que integran análisis FIRS, recomendaciones con evidencia, KPIs (BSC 4 perspectivas cuando aplique) y trazabilidad normativa. Output final orientado a decisión de gestión, clínica o de política sanitaria.

## I/O

- **Input:** contenido_analisis: object (output de CMs previos en sesión), tipo_informe: string, audiencia: string
- **Output:** Report { encabezado, resumen_ejecutivo, posicion_firs, analisis, recomendaciones[], kpis[], trazabilidad_normativa[], disclaimer }

## Procedimiento

1. RECIBIR contenido acumulado de sesión (outputs de CM-FIRS-REASONER, CM-NETWORK-ANALYST, CM-QUALITY-AUDITOR o CM-EPI-VIGILANCE).
2. IDENTIFICAR TIPO DE INFORME:
   - Clínico-epidemiológico (problema individual o poblacional)
   - Gestión de red (análisis sistémico, rediseño, mejora)
   - Auditoría / calidad / seguridad paciente
   - Vigilancia / alertas sanitarias
   - Estratégico (decisión de política sanitaria)
3. IDENTIFICAR AUDIENCIA: alta dirección / equipos clínicos / organismos reguladores / organismos internacionales → calibrar tecnicidad y registro.
4. ESTRUCTURAR INFORME:
   - **Encabezado**: Título, fecha, dimensión(es) FIRS trabajadas, nivel de análisis, autor/agente
   - **Resumen ejecutivo**: 3-5 líneas — problema, hallazgo principal, recomendación prioritaria
   - **Posición FIRS**: declarar dimensión(es) y ejes transversales aplicados
   - **Análisis**: síntesis del razonamiento (Dim I/II/III según corresponda). Incluir incertidumbre residual si existe.
   - **Tensiones navegadas**: si el análisis involucra tensiones estructurales FIRS → explicitar cómo se navegaron
   - **Recomendaciones**: con prioridad (Alta/Media/Baja), responsable sugerido, fuente de evidencia, plazo orientativo
   - **KPIs propuestos** (si aplica): tabla estándar (Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad)
   - **BSC si gestión**: 4 perspectivas (paciente, financiera, procesos internos, crecimiento/aprendizaje) → KPIs por perspectiva
   - **Trazabilidad normativa**: OPS/OMS + guías internacionales + normativa local si provista por usuario
   - **Disclaimer**: "Informe de apoyo analítico. Decisiones clínicas y de gestión requieren validación profesional in situ y adherencia al marco normativo local vigente."
5. VERIFICAR COHERENCIA: ¿recomendaciones son consistentes con el nivel de análisis declarado? ¿No hay cruce de nivel sin mediación? ¿Herramientas correctamente identificadas (≠ marcos)?
6. SI WEB_SEARCH requerido para evidencia faltante → ejecutar, integrar, citar.

## Signature Output

| Campo | Tipo | Descripción |
|-------|------|-------------|
| tipo_informe | string | Clínico-epi / Gestión / Auditoría / Vigilancia / Estratégico |
| audiencia | string | Dirección / Clínicos / Reguladores / Internacional |
| resumen_ejecutivo | string | 3-5 líneas: problema + hallazgo + recomendación prioritaria |
| posicion_firs | string | Dimensiones y ejes aplicados |
| analisis | string | Razonamiento completo con incertidumbre declarada |
| tensiones_navegadas | string[] | Tensiones FIRS relevantes + cómo se navegaron |
| recomendaciones | Recomendacion[] | {texto, prioridad, responsable, evidencia, plazo} |
| kpis | KPISpec[] | Tabla KPI estándar |
| bsc | BSCSpec? | Solo si gestión: KPIs por perspectiva BSC |
| trazabilidad_normativa | string[] | OPS/OMS + guías + normativa local |
| disclaimer | string | Fijo: apoyo analítico, validación profesional requerida |

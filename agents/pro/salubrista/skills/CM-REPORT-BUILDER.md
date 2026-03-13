---
_manifest:
  urn: urn:pro:skill:salubrista-report-builder:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-REPORT-BUILDER

## Proposito
Construir informes estructurados para apoyar al medico salubrista humano en decisiones epidemiologicas, organizacionales y de implementacion. Integra analisis, diseno, opciones, riesgos, KPIs, supuestos y trazabilidad en un formato util para conducir sistemas sanitarios complejos.

## Input/Output
- **Input:** contenido_analisis: object, tipo_informe: string, audiencia: string
- **Output:** Report { encabezado, resumen_ejecutivo, escala, analisis, opciones: string[], implementacion: string[], kpis: string[], riesgos: string[], trazabilidad: string[], disclaimer }

## Procedimiento
1. RECIBIR el contenido acumulado de sesion desde analisis epidemiologico, sistemico, diseno, implementacion, evaluacion o vigilancia.
2. IDENTIFICAR tipo de informe:
   - diagnostico situacional
   - escenario de decision
   - propuesta de rediseño
   - plan de implementacion
   - evaluacion de desempeno
   - vigilancia / alerta sanitaria
3. IDENTIFICAR audiencia: medico salubrista, direccion de red, direccion de establecimiento, equipo tecnico, regulador u otra autoridad.
4. ESTRUCTURAR informe:
   - problema y escala
   - hallazgos epidemiologicos o sistemicos
   - opciones o alternativas
   - riesgos, supuestos y dependencias
   - consideraciones de implementacion
   - KPIs y criterio de seguimiento
   - trazabilidad de evidencia y normativa
   - disclaimer de rol de copiloto
5. VERIFICAR coherencia:
   - la escala esta clara
   - las recomendaciones no saltan de analisis a ejecucion sin puente
   - la decision final queda en la conduccion humana
6. SI `web_search` fue necesario para evidencia faltante o vigencia normativa -> integrar y citar.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_informe | string | Tipo de producto generado |
| audiencia | string | Destinatario principal |
| resumen_ejecutivo | string | Sintesis para decision |
| escala | string | Escala del problema |
| analisis | string | Analisis principal |
| opciones | string[] | Opciones o cursos de accion |
| implementacion | string[] | Implicancias operativas o siguientes pasos |
| kpis | string[] | Indicadores de seguimiento |
| riesgos | string[] | Riesgos, tradeoffs y dependencias |
| trazabilidad | string[] | Evidencia y normativa citada |
| disclaimer | string | Apoyo tecnico; la conduccion y decision final permanecen en la persona responsable |

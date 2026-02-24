---
_manifest:
  urn: "urn:fxsl:skill:analyst-metrics-collector:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-METRICS-COLLECTOR

## Proposito
Recopila datos crudos de ejecucion del enjambre y calcula las metricas fundamentales del Ciclo.

## Input/Output
- **Input:** Datos del Ciclo: historias completadas (Done), historias rechazadas (Rejected), tokens consumidos por historia, modelo utilizado por historia, fechas de transicion (backlog→done), presupuesto asignado.
- **Output:** Metricas calculadas: CpH, TA, Cycle Time promedio, presupuesto consumido %, desglose por historia.

## Procedimiento
1. Inventariar historias del Ciclo: Done y Rejected, con metadata (tokens, modelo, fechas).
2. Calcular CpH (Cost per History):
   - Formula: tokens_totales_consumidos / count(historias_Done).
   - Unidad: tokens/historia.
   - Fuente: logs de ejecucion del enjambre.
3. Calcular TA (Tasa de Aceptacion):
   - Formula: count(historias_aceptadas_primer_intento) / count(historias_totales) × 100.
   - Unidad: porcentaje.
   - "Primer intento" = aprobada por reviewer sin rework.
4. Calcular Cycle Time promedio:
   - Formula: promedio(fecha_Done - fecha_entrada_backlog) por historia.
   - Unidad: dias.
   - Incluir distribucion: min, max, p50, p90.
5. Calcular presupuesto consumido:
   - Formula: tokens_totales_consumidos / presupuesto_asignado_tokens × 100.
   - Desglosar por partida: historias, BAU, calibracion.
6. Generar tabla de metricas por historia: {historia, tokens, modelo, cycle_time, aceptada, fuente}.
7. Validar: toda metrica tiene fuente y fecha. Si falta dato, reportar "dato no disponible" en celda correspondiente.

## Signature Output
Tabla resumen: {metrica, valor, unidad, fuente, fecha}. Tabla detalle: {historia, tokens, modelo, cycle_time_dias, aceptada_primer_intento, fuente}.

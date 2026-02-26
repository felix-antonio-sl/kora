---
_manifest:
  urn: "urn:fxsl:skill:analyst-backlog-health-checker:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-BACKLOG-HEALTH-CHECKER

## Proposito
Evalua la salud del flujo de backlog: detecta estancamiento, cuellos de botella, violaciones de WIP y desbalances en el ritmo de nutricion.

## Input/Output
- **Input:** Historias pendientes con estado y fechas, throughput actual (historias/dia), WIP limits por zona, historias entrando al backlog por periodo.
- **Output:** Diagnostico de salud del backlog con anomalias detectadas, causas probables y tabla de salud.

## Procedimiento
1. Detectar historias stale:
   - Stale = historia sin cambio de estado por >N dias (default: 5 dias, configurable via config.json).
   - Listar: {historia, estado_actual, dias_sin_movimiento, zona}.
   - Si count(stale) > 20% del backlog: alertar.
2. Detectar cuellos de botella:
   - Agrupar historias por estado (backlog, in_progress, review, done).
   - Bottleneck = estado con acumulacion desproporcionada (>40% de historias activas).
   - Reportar: {estado, count, % del total}.
3. Verificar WIP limits:
   - Para cada zona del codebase: comparar historias in_progress vs WIP limit.
   - Violacion = actual > limit.
   - Reportar: {zona, actual, limit, violacion: bool}.
4. Calcular profundidad de cola (queue depth):
   - Formula: historias_pendientes / throughput_diario.
   - Unidad: dias de trabajo acumulado.
   - Si queue_depth > 2× Ciclo promedio: alertar "backlog sobrecargado".
5. Calcular ratio de nutricion:
   - Formula: historias_entrando_por_periodo / historias_saliendo_por_periodo.
   - Si ratio > 1.5: backlog creciendo mas rapido de lo que se consume. Alertar.
   - Si ratio < 0.5: backlog se agota. Alertar al planner.
6. Diagnosticar causa probable de anomalias detectadas:
   - Stale + bottleneck en review → "reviewer es cuello de botella".
   - WIP violation + stale → "zona sobrecargada con trabajo estancado".
   - Queue depth alto + ratio >1.5 → "ingreso supera capacidad de procesamiento".
7. Presentar tabla de salud consolidada.

## Signature Output
Tabla salud: {indicador, valor, umbral, estado: sano|alerta|critico}. Lista de anomalias: {anomalia, causa_probable, recomendacion}. Metricas de flujo: queue_depth, nutrition_ratio, stale_count, wip_violations_count.

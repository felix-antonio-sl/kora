---
_manifest:
  urn: "urn:dev:agent-bootstrap:analyst-tools:1.0.0"
  type: "bootstrap_tools"
---

## metrics_collect

- **Firma:** {ciclo: int, historias_done: story[], historias_rejected: story[], tokens_consumidos: int, presupuesto_asignado: int} → {cph: float, ta: float, cycle_time_avg: float, presupuesto_consumido_pct: float, metricas_por_historia: [{historia, tokens, modelo, cycle_time, aceptada: bool}]}
- **Cuando usar:** S-METRICAS. Recopilar y calcular metricas crudas de un Ciclo.
- **Cuando NO usar:** Si no hay datos de ciclo disponibles. No fabricar datos.
- **Notas:** CpH = tokens_totales / historias_done. TA = historias_aceptadas_primer_intento / historias_totales × 100. Cycle Time = promedio(fecha_done - fecha_backlog). Toda metrica con fuente.

## dashboard_generate

- **Firma:** {metricas_actuales: metrics, metricas_anteriores: metrics?} → {tablero: [{dimension, metrica, actual, anterior, delta, tendencia}]}
- **Cuando usar:** S-DASHBOARD. Generar Tablero Neural de 5 dimensiones.
- **Cuando NO usar:** Si no hay metricas recopiladas. Recopilar primero via metrics_collect.
- **Notas:** 5 dimensiones obligatorias: coste, calidad, velocidad, modelo, enjambre. Delta = actual - anterior. Tendencia = direccion (↑↓→). Si no hay datos anteriores, columna anterior = "N/A".

## retro_report

- **Firma:** {ciclo: int, metricas: metrics, okrs: [{objetivo, krs: [{kr, baseline, target, actual}]}], patrones_rechazo: string[], gaps_evals: string[]} → {reporte: {progreso_okrs, analisis_costes, patrones_calidad, propuestas_ajuste}}
- **Cuando usar:** S-REPORTE. Generar Retrospectiva Analitica de fin de Ciclo.
- **Cuando NO usar:** Si el Ciclo no ha terminado. Metricas parciales no son retrospectiva.
- **Notas:** Propuestas de ajuste son observaciones basadas en datos, no prescripciones. El PO y Operador deciden.

## trend_analyze

- **Firma:** {metricas_por_ciclo: [{ciclo, cph, ta, cycle_time, presupuesto_consumido}]} → {tendencias: [{metrica, serie_temporal, delta_acumulado, punto_inflexion?, compatible_exponencial: bool}]}
- **Cuando usar:** S-TENDENCIA. Analizar tendencias inter-Ciclo (requiere minimo 2 Ciclos).
- **Cuando NO usar:** Si solo hay datos de 1 Ciclo. Reportar "insuficientes datos para tendencia".
- **Notas:** Comparar contra hipotesis exponencial de Chapter 0 §2.3. Inflexion = punto donde la derivada cambia de signo. No extrapolar mas alla de los datos.

## backlog_health

- **Firma:** {historias_pendientes: story[], throughput: float, wip_limits: {zona: int}} → {salud: {stale_stories: story[], bottlenecks: [{estado, count}], wip_violations: [{zona, actual, limit}], queue_depth: float, nutrition_ratio: float}}
- **Cuando usar:** S-BACKLOG-HEALTH. Evaluar salud del flujo de backlog.
- **Cuando NO usar:** Si no hay backlog activo.
- **Notas:** Stale = >5 dias sin movimiento (configurable). Queue depth = historias_pendientes / throughput_diario. Nutrition ratio = historias_entrando / historias_saliendo por periodo.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema → resolver URN → consultar KB del corpus xanpan.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Metricas, tablero, economia tokens, evals, roles, enjambre, metodologia | urn:fxsl:kb:xanpan-agents-metodologia |
| Stack, arquitectura, model router, context engineering, CI/CD | urn:fxsl:kb:stack-llm-arquitectura |
| Operaciones, pipeline, deploy, observabilidad, seguridad | urn:fxsl:kb:swarm-ops-metodologia |
| Bootstrap, operador solitario, fases, dual-hat, curva exponencial | urn:fxsl:kb:chapter0-operador-solitario |

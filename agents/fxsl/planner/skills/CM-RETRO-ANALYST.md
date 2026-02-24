---
_manifest:
  urn: "urn:fxsl:skill:planner-retro-analyst:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-RETRO-ANALYST

## Proposito
Genera reporte para la Retrospectiva Analitica al final de un Ciclo. Metricas puras, sin emocion.

## Procedimiento
1. Recopilar datos del Ciclo:
   - Historias completadas (Done) y rechazadas (Rejected).
   - Tokens consumidos por historia (CpH).
   - Tasa de aceptacion al primer intento (TA).
   - Cycle Time promedio (backlog→done).
   - Presupuesto de tokens: asignado vs consumido.
   - Progreso de KRs: baseline → actual → target.
2. Calcular metricas agregadas:
   - CpH promedio y tendencia vs Ciclo anterior.
   - TA global y por tipo de historia.
   - Cycle Time promedio y distribucion.
   - % presupuesto consumido por partida (historias/BAU/calibracion).
3. Analizar patrones:
   - Patrones de rechazo: que tipos de historias se rechazan mas? Por que?
   - Alucinaciones recurrentes: hubo evals que detectaron patrones repetidos?
   - Gaps en evals: hubo fallos no detectados por evals existentes?
4. Proponer ajustes para proximo Ciclo:
   - Cambios de modelo?
   - Ajustes a context engineering?
   - Nuevos evals necesarios?
   - Reconfiguracion de topologia del enjambre?
5. Revisar tarjetas purpura pendientes del Sentinel (si aplica).
6. Presentar reporte consolidado con tablas y recomendaciones.

## Output
Reporte Retrospectiva: {metricas_ciclo, progreso_okrs, patrones_observados, ajustes_propuestos, tarjetas_purpura_pendientes}.

---
_manifest:
  urn: "urn:fxsl:skill:analyst-dashboard-generator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-DASHBOARD-GENERATOR

## Proposito
Genera el Tablero Neural: vista consolidada del enjambre en 5 dimensiones con comparativa temporal.

## Input/Output
- **Input:** Metricas del Ciclo actual (via CM-METRICS-COLLECTOR), metricas del Ciclo anterior (si disponibles), datos de distribucion de modelos y carga de agentes.
- **Output:** Tablero de 5 dimensiones con columnas: dimension, metrica, actual, anterior, delta, tendencia.

## Procedimiento
1. Dimension COSTE:
   - CpH (tokens/historia): actual vs anterior.
   - Presupuesto consumido (%): actual vs planificado.
   - Coste por zona del codebase (si datos disponibles).
2. Dimension CALIDAD:
   - TA (%): tasa de aceptacion primer intento.
   - Tasa de rechazo (%): inversa de TA.
   - Patrones de alucinacion: frecuencia detectada por evals (si datos disponibles).
3. Dimension VELOCIDAD:
   - Cycle Time promedio (dias).
   - Throughput (historias completadas / dias del Ciclo).
   - Distribucion: p50, p90 de Cycle Time.
4. Dimension MODELO:
   - Distribucion por tier: % historias en T1, T2, T3, T4.
   - Fallbacks de modelo: count y frecuencia.
   - Coste por tier: CpH segmentado.
5. Dimension ENJAMBRE:
   - Carga por agente: historias procesadas por cada agente.
   - Utilizacion: % de capacidad usada (estimada).
   - Cuellos de botella: agente con mayor cola o mayor cycle time.
6. Para cada metrica: calcular delta = actual - anterior. Asignar tendencia: ↑ (creciente), ↓ (decreciente), → (estable, delta <5%).
7. Si no hay datos del Ciclo anterior: columna anterior = "N/A", delta = "—", tendencia = "primer Ciclo".
8. Validar: 5 dimensiones presentes, toda celda con dato o "sin datos".

## Signature Output
Tabla: {dimension, metrica, actual, anterior, delta, tendencia}. Una fila por metrica, agrupadas por dimension. Minimo 2 metricas por dimension.

---
_manifest:
  urn: "urn:fxsl:skill:analyst-trend-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-TREND-ANALYZER

## Proposito
Analiza tendencias de metricas entre Ciclos. Detecta direccion, puntos de inflexion y compatibilidad con la hipotesis de curva exponencial.

## Input/Output
- **Input:** Metricas por Ciclo: [{ciclo, cph, ta, cycle_time, presupuesto_consumido, throughput}]. Minimo 2 Ciclos.
- **Output:** Tendencias por metrica con serie temporal, delta acumulado, inflexiones detectadas, compatibilidad exponencial.

## Procedimiento
1. Verificar datos suficientes: minimo 2 Ciclos. Si <2, emitir "insuficientes datos para analisis de tendencia".
2. Para cada metrica clave (CpH, TA, Cycle Time, throughput):
   a. Construir serie temporal: tabla {ciclo, valor, delta_vs_anterior, delta_%}.
   b. Calcular delta acumulado desde C1.
   c. Determinar direccion: creciente, decreciente, estable (delta <5%), volatil (cambios de signo).
3. Detectar puntos de inflexion:
   - Inflexion = Ciclo donde la derivada (delta) cambia de signo.
   - Reportar: {metrica, ciclo_inflexion, valor_antes, valor_despues, interpretacion}.
4. Evaluar hipotesis exponencial (Chapter 0 §2.3):
   - Para CpH: se espera decrecimiento exponencial (eficiencia aprendida por el enjambre).
   - Para TA: se espera crecimiento asintótico (calidad converge).
   - Para throughput: se espera crecimiento (aceleracion).
   - Compatibilidad: la serie real se ajusta razonablemente a la curva teorica? Reportar: compatible|parcialmente_compatible|no_compatible.
5. Generar preguntas abiertas para el PO/Operador basadas en anomalias:
   - Si CpH crece: "CpH aumento en C_N. Historias mas complejas? Cambio de modelo? Rework excesivo?"
   - Si TA cae: "TA disminuyo. Evals insuficientes? Cambio de scope? Context drift?"
6. No extrapolar mas alla de los datos. Las tendencias describen el pasado, no predicen el futuro.

## Signature Output
Tabla por metrica: {ciclo, valor, delta, delta_%}. Resumen: {metrica, tendencia, delta_acumulado, inflexiones, compatible_exponencial}. Preguntas abiertas si hay anomalias.

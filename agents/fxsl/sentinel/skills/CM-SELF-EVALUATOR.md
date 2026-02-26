---
_manifest:
  urn: "urn:fxsl:skill:sentinel-self-evaluator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-SELF-EVALUATOR

## Proposito
El sentinel se evalua a si mismo. Verifica que sus propuestas mejoran realmente el enjambre. Si no, lo reporta.

## Procedimiento
1. Recopilar tarjetas purpura aplicadas en el Ciclo anterior.
2. Para cada tarjeta aplicada:
   - Registrar metricas ANTES de aplicar (baseline).
   - Registrar metricas DESPUES de aplicar (actual).
   - Clasificar resultado: MEJORO(metrica objetivo subio), SIN_EFECTO(sin cambio significativo), EMPEORO(metrica degrado).
3. Calcular tasa de mejora efectiva: tarjetas que MEJORARON / total aplicadas.
4. Evaluacion:
   - Tasa >= 70%: SANO. Las propuestas del sentinel son efectivas.
   - Tasa 50-69%: WARNING. Propuestas parcialmente efectivas. Revisar criterios.
   - Tasa < 50%: CRITICO. "Mis propuestas no estan mejorando el enjambre. Recalibrar."
5. Analizar tarjetas contraproducentes: por que empeoraron? Extraer leccion.
6. Si hay suite de pruebas adversariales disponible:
   - Ejecutar: prompt injection, falsa urgencia, manipulacion de metricas, bypass de validacion.
   - Reportar categorias falladas.
7. Presentar reporte de auto-evaluacion al Operador con total transparencia.
8. Si CRITICO: proponer recalibracion del sentinel como tarjeta purpura meta (que el Operador decida).

## Output
Auto-eval: {tarjetas_evaluadas: int, tasa_mejora: float, tarjetas_efectivas[], tarjetas_sin_efecto[], tarjetas_contraproducentes[], adversarial_result?: PASS|FAIL, veredicto: SANO|WARNING|CRITICO, propuesta_recalibracion?}.

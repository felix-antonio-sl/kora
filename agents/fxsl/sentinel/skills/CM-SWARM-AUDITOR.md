---
_manifest:
  urn: "urn:fxsl:skill:sentinel-swarm-auditor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-SWARM-AUDITOR

## Proposito
Analiza rendimiento del enjambre usando metricas agregadas. Detecta anomalias. Diagnostica causas probables.

## Procedimiento
1. Recopilar metricas del periodo (Pulso o Ciclo):
   - **Coste:** CpH promedio, coste total, % presupuesto consumido.
   - **Calidad:** TA por agente, tasa de alucinacion, patrones de rechazo.
   - **Velocidad:** Cycle Time promedio, historias Done/Pulso, throughput.
   - **Modelo:** Tasa de exito por modelo, latencia, frecuencia de fallback.
   - **Enjambre:** WIP por zona, profundidad de cola, tarjetas purpura pendientes.
2. Comparar con periodo anterior: calcular delta por metrica.
3. Detectar anomalias (umbrales configurables):
   - TA de agente < 70%: WARNING.
   - Cycle Time subio >30%: WARNING.
   - CpH subio >50% sin cambio de complejidad: WARNING.
   - Fallback rate >20%: WARNING (provider inestable).
   - TA global < 60%: CRITICO.
4. Para cada anomalia, diagnosticar causa probable:
   - ¿Cambio de modelo reciente?
   - ¿Context files modificados?
   - ¿Tipo de historias cambio (mas complejas)?
   - ¿Zona del codebase nueva sin context engineering?
5. Proponer ajustes como tarjetas purpura.
6. Si no hay anomalias: reportar "enjambre sano" con metricas clave.

## Output
Reporte: {periodo, metricas_resumen, anomalias: [{metrica, valor, umbral, diagnostico, propuesta}], veredicto: SANO|WARNING|CRITICO}.

---
_manifest:
  urn: "urn:dev:skill:sentinel-purple-card-generator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-PURPLE-CARD-GENERATOR

## Proposito
Formula propuestas de mejora como tarjetas purpura formales. Mecanismo central de auto-evolucion gobernada del enjambre.

## Procedimiento
1. Recibir diagnostico de CM-CONTEXT-AUDITOR, CM-SWARM-AUDITOR o CM-EVAL-AUDITOR.
2. Clasificar tipo de tarjeta:
   - **ajuste_prompt:** Optimizar system prompt de un agente. Causa: patrones de rechazo recurrentes.
   - **nuevo_eval:** Agregar eval faltante. Causa: gap de cobertura o incidente sin regresion.
   - **reconfig_topologia:** Cambiar tier de modelo, agregar/quitar agente, reasignar zona. Causa: anomalia de rendimiento persistente.
   - **context_update:** Actualizar context file. Causa: drift detectado.
   - **model_change:** Cambiar modelo base de un agente. Causa: degradacion de calidad o coste.
3. Para cada tarjeta, completar formato estandar:
   - **Tipo:** (enum arriba).
   - **Descripcion:** Que se propone cambiar, en 1-3 lineas.
   - **Justificacion:** Datos que soportan la propuesta (metricas, tendencias, incidentes).
   - **Impacto esperado:** Que mejora se espera y como se medira.
   - **Riesgo:** Que podria salir mal si se aplica.
   - **Agentes afectados:** Cuales agentes tocaria el cambio.
4. Marcar SIEMPRE: "Requiere aprobacion del Operador."
5. Limitar a 5 tarjetas por Pulso. Priorizar por impacto/riesgo.
6. Presentar al Operador.

## Output
Tarjetas purpura: [{tipo, descripcion, justificacion, impacto, riesgo, agentes_afectados, estado: "pendiente_aprobacion"}].

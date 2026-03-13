---
_manifest:
  urn: urn:pro:skill:salubrista-implementation-planner:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-IMPLEMENTATION-PLANNER

## Proposito
Traducir analisis, disenos o mejoras en planes de implementacion operables. Aborda factibilidad, fases, pilotaje, escalamiento, gestion del cambio, monitoreo y ajuste adaptativo para que una propuesta sanitaria pueda pasar a ejecucion real.

## Input/Output
- **Input:** propuesta: string, contexto: object
- **Output:** ImplementationPlan { objetivo_operativo, supuestos: string[], fases: string[], responsables: string[], riesgos: string[], indicadores: string[], decision_logica: string }

## Procedimiento
1. KB_FIRST: resolver `kb_route` hacia gestion-redes general o herramientas segun la propuesta y recuperar el contenido pertinente con `knowledge_retrieval`.
2. DEFINIR el objetivo operativo y el resultado esperado.
3. EVALUAR factibilidad:
   - capacidad instalada
   - dependencias criticas
   - restricciones institucionales
   - madurez del equipo
   - ventana temporal
4. IDENTIFICAR actores y responsables:
   - sponsor
   - responsables operativos
   - equipos afectados
   - nodos de coordinacion
5. ESTRUCTURAR fases:
   - preparacion
   - piloto o prueba controlada
   - escalamiento progresivo
   - estabilizacion
6. GESTION DEL CAMBIO:
   - comunicacion
   - entrenamiento
   - soporte en terreno
   - feedback y ajuste
7. IDENTIFICAR riesgos y mitigaciones:
   - resistencia organizacional
   - brechas de datos
   - limitaciones de capacidad
   - desalineacion entre niveles del sistema
8. PROPONER monitoreo:
   - indicadores de proceso, resultado y seguridad
   - hitos de revision
   - gatillos de correccion o rollback
9. OUTPUT: objetivo operativo, supuestos, fases, responsables, riesgos, indicadores y logica de decision de implementacion.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| objetivo_operativo | string | Resultado operativo buscado |
| supuestos | string[] | Condiciones necesarias para implementar |
| fases | string[] | Secuencia de implementacion |
| responsables | string[] | Roles o actores responsables |
| riesgos | string[] | Riesgos principales y mitigaciones |
| indicadores | string[] | KPIs o hitos de seguimiento |
| decision_logica | string | Criterio de pilotaje, escalamiento o ajuste |

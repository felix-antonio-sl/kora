---
_manifest:
  urn: "urn:fxsl:skill:ingeniero-sistemas-composicional-evolution-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar y gestionar evolucion del sistema. Clasificar cambios y evaluar impacto en breakdown structures y requisitos.

## Input/Output

- **Input:** Solicitud de cambio o evolucion desde S-EVOLUTION
- **Output:** Clasificacion del cambio, analisis de impacto, estrategia de evolucion

## Procedimiento

1. Clasificar TIPO: cambio planificado (proyecto) vs adaptativo (workaround)?
2. Evaluar IMPACTO: que elementos FBS/PBS/LBS afecta?
3. Analizar PROPAGACION: que otros elementos se ven afectados por dependencia?
4. Proponer ESTRATEGIA: delta incremental o rediseno?
5. Mapear a fase WSLC:
   - Operacion/Mantenimiento: adaptaciones menores
   - Iniciacion: nuevo proyecto de cambio
   - Desarrollo: crear/adquirir recursos
   - Implementacion: transicion al nuevo estado

## Signature Output

```
## Analisis de Evolucion
- **Tipo**: [planificado|adaptativo]
- **Impacto**: [elementos afectados]
- **Propagacion**: [dependencias impactadas]
- **Estrategia**: [delta|rediseno]
- **Fase WSLC**: [fase recomendada]
```

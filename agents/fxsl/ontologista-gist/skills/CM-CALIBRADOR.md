---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-calibrador:1.0.0"
  type: "lazy_load_endofunctor"
---
## Proposito

Calibrar y estructurar el output ontologico final para entrega: chunks 3-5, progresion familiar→nuevo, capas sintesis→desarrollo→detalle tecnico, con anclas Gist explicitas.

## I/O

- **Input:** Modelo ontologico en bruto o borrador de respuesta desde S-PRODUCCION
- **Output:** Respuesta ontologica calibrada en capas (sintesis→desarrollo→detalle), chunks <=5, anclas Gist visibles

## Procedimiento
1. Chunks: dividir el output en bloques tematicos de maximo 5 elementos cada uno. Nunca presentar listas planas de mas de 5 items sin agrupar.
2. Progresion: ordenar el contenido de familiar a nuevo, de concreto a abstracto. Comenzar con el patron Gist mas conocido y avanzar hacia extensiones o casos especiales.
3. Capas de entrega:
   - Capa 1 (sintesis): concepto central y patron Gist aplicado en 2-3 lineas.
   - Capa 2 (desarrollo): clases, propiedades, justificacion de decisiones, trade-offs.
   - Capa 3 (detalle tecnico): fragmento Turtle o diagrama si el usuario lo requiere.
4. Anclas Gist: en cada claim ontologico, citar la clase o propiedad Gist especifica que lo fundamenta (p.ej. gist:TemporalRelation, gist:isCategorizedBy).
5. Verificar checklist pre-output del agente antes de entregar: FOCUS, GIST_CONFORMANCE, NAMESPACE_HYGIENE, PATTERN_SELECTION, COMPLEXITY, CALIBRATION, TRADE_OFFS.

## Signature Output

Respuesta ontologica calibrada: estructura en capas (sintesis → desarrollo → detalle), chunks <= 5, anclas Gist visibles, trade-offs explicitos. Lista de decisiones ontologicas clave al final si el trabajo fue extenso.

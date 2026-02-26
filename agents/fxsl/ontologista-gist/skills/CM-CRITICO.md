---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-critico:1.0.0"
  type: "lazy_load_endofunctor"
---
## Proposito

Evaluar criticamente un modelo ontologico en 4 dimensiones: cobertura del dominio, costo de implementacion, modos de fallo y conformidad con principios Gist.

## I/O

- **Input:** Modelo ontologico a evaluar desde S-OPERACION
- **Output:** Reporte critico con conformidad Gist, problemas identificados, sugerencias de mejora

## Procedimiento
1. Cobertura: verificar que el modelo cubre todos los casos de uso identificados. Detectar entidades o relaciones del dominio no representadas.
2. Costo: evaluar complejidad del modelo — numero de clases, propiedades, axiomas OWL. Identificar simplificaciones posibles sin perder expresividad.
3. Fallo: anticipar como fallaria el modelo: datos inconsistentes, instancias que no encajan, inferencias incorrectas, ambiguedades de clasificacion.
4. Principios Gist: verificar conformidad con:
   - Minimalismo: no crear clase si puede ser Category o propiedad.
   - Namespace hygiene: extensiones en namespace propio, nunca en gist:.
   - Patron apropiado: TemporalRelation para temporalidad, Magnitude para valores con UoM.
   - No anti-patrones: no namespace squatting, no subclases innecesarias.
5. Formular al menos 3 criticas concretas con sugerencia de mejora para cada una.

## Signature Output

Reporte critico: tabla Dimension/Problema-identificado/Sugerencia-mejora. Veredicto de conformidad Gist: [conforme / no conforme / parcial] con justificacion. Prioridad de correcciones.

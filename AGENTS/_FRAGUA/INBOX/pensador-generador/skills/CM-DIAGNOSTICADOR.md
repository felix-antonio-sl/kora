---
_manifest:
  urn: urn:fxsl:skill:pensador-generador-diagnosticador:2.0.0
  type: lazy_load_endofunctor
---

## Proposito
Clasificar el problema recibido en sus dimensiones de dificultad para determinar el tipo de trabajo analitico requerido antes de operar.

## Input/Output
- **Input:** Problema o solicitud del usuario (post-posicionamiento)
- **Output:** Diagnostico dimensional: dimension(es) dominante(s), justificacion breve, senal de informacion critica faltante si aplica

## Procedimiento
1. Evaluar el problema en 5 dimensiones:
   - INFORMACION: ¿faltan datos suficientes para avanzar con rigor?
   - ESTRUCTURA: ¿el problema esta mal comprendido o mal formulado por el usuario?
   - DEFINICION: ¿es ambiguo que constituye una solucion valida o exitosa?
   - RESTRICCIONES: ¿hay restricciones que se contradicen entre si?
   - RECURSOS: ¿hay limites de tiempo, espacio o formato que condicionan la respuesta?
2. Identificar dimension(es) dominante(s); puede haber mas de una activa simultaneamente
3. Si INFORMACION es dominante: marcar falta_informacion_critica = true en el output
4. Comunicar diagnostico al usuario cuando sea relevante para alinear expectativas sobre la respuesta

## Signature Output
Tabla: Dimension | Activa (si/no) | Observacion. Veredicto: falta_informacion_critica (true|false).

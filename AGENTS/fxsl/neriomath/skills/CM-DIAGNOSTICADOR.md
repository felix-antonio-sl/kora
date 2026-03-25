---
_manifest:
  urn: urn:fxsl:skill:neriomath-diagnosticador:1.2.0
  type: lazy_load_endofunctor
---

## Proposito
Clasificar el problema en sus dimensiones de dificultad, tipar restricciones y verificar si el problema planteado es el problema real.

## Input/Output
- **Input:** Problema o solicitud del usuario (post-posicionamiento), clase de activacion
- **Output:** Diagnostico dimensional, restricciones tipadas, senal de informacion critica faltante si aplica, limite_humano si aplica, reformulacion propuesta si aplica

## Procedimiento
1. Evaluar el problema en 5 dimensiones:
   - INFORMACION: faltan datos suficientes para avanzar con rigor?
   - ESTRUCTURA: el problema esta mal comprendido o mal formulado?
   - DEFINICION: es ambiguo que constituye una solucion valida?
   - RESTRICCIONES: hay restricciones que se contradicen entre si?
   - RECURSOS: hay limites de tiempo, espacio o formato que condicionan la respuesta?
2. Tipar restricciones presentes:
   - DURAS: no negociables (fisicas, legales, logicas)
   - BLANDAS: negociables con costo (presupuesto, tiempo, calidad)
   - SUPUESTAS: asumidas pero no declaradas (verificar con usuario)
   - Checklist minimo de restricciones reales: tiempo, recursos, capacidades, marco normativo, limites institucionales, disponibilidad de datos, viabilidad politica/social, tolerancia al riesgo
   - Anti-patrones: no tratar como dura una restriccion heredada o solo supuesta; no degradar restricciones no tecnicas a ruido contextual
3. Identificar dimension(es) dominante(s); puede haber mas de una activa
4. Si INFORMACION dominante: marcar falta_informacion_critica = true
5. Reformulacion: el problema como fue planteado ES el problema real? Si no, proponer reformulacion explicita reconociendo el cambio y su razon. Reformular recursivamente si la reformulacion revela otra capa.
6. Si el cuello de botella no es analitico sino de presencia humana, autoridad, confianza, cuidado o negociacion, marcar limite_humano = true y no sobreoptimizar.
7. Comunicar diagnostico al usuario cuando sea relevante para alinear expectativas
8. MULTIPLICAR: si el framework diagnostico (5 dimensiones, tipado restricciones, test de reformulacion) seria util para que el interlocutor diagnostique sus propios problemas, senalizar para transferencia en produccion.

## Signature Output
Tabla: Dimension | Activa (si/no) | Observacion. Restricciones tipadas: [tipo] descripcion. Veredicto: falta_informacion_critica (true|false), limite_humano (true|false). Reformulacion propuesta si aplica.

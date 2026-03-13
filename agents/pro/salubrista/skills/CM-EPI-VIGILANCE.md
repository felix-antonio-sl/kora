---
_manifest:
  urn: urn:pro:skill:salubrista-epi-vigilance:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-EPI-VIGILANCE

## Proposito
Conducir vigilancia epidemiologica activa para apoyar decisiones sanitarias oportunas: deteccion temprana de riesgos, evaluacion de brotes, aplicacion del RSI 2005, gestion de RAM y lectura de impacto operacional para el sistema de salud.

## Input/Output
- **Input:** señal: string, contexto: object
- **Output:** VigilanceReport { tipo_amenaza, evaluacion_riesgo, clasificacion_rsi, acciones_inmediatas: string[], notificacion_requerida: bool, implicancias_sistema: string[], analisis_epi_ampliado_requerido: bool }

## Procedimiento
1. KB_FIRST: resolver `kb_route` hacia el tema de vigilancia o razonamiento sanitario integrado y recuperar el contenido pertinente con `knowledge_retrieval` antes de complementar con web.
2. CARACTERIZAR la señal: cuando, donde, cuantos casos, poblacion afectada, severidad, velocidad de propagacion y capacidad de respuesta disponible.
3. CLASIFICAR el tipo de amenaza:
   - brote infeccioso o clúster inusual
   - amenaza quimica o radiologica
   - salud ocupacional
   - resistencia antimicrobiana
4. EVALUAR riesgo:
   - gravedad
   - probabilidad de propagacion
   - capacidad del sistema para contener o responder
5. CLASIFICAR segun RSI 2005:
   - IF evento inusual/grave con potencial internacional -> evaluar notificacion
   - IF aplica -> `notificacion_requerida = true`
6. DEFINIR acciones inmediatas:
   - contencion
   - investigacion de campo
   - proteccion de equipos
   - coordinacion interinstitucional
7. ESTIMAR implicancias para el sistema:
   - tension sobre capacidad
   - reordenamiento de flujos
   - refuerzo de vigilancia o laboratorio
   - necesidad de comunicacion de riesgo
8. SI el evento requiere lectura epidemiologica mas amplia -> `analisis_epi_ampliado_requerido = true`
9. SI `web_search` es necesario para situacion epidemiologica actual o normativa vigente -> ejecutar y citar.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_amenaza | string | Infecciosa / Quimica / Radiologica / RAM / Ocupacional |
| evaluacion_riesgo | string | Gravedad x propagacion x respuesta |
| clasificacion_rsi | string | Clasificacion operacional del evento |
| acciones_inmediatas | string[] | Acciones de contencion o respuesta |
| notificacion_requerida | bool | True si la situacion amerita notificacion |
| implicancias_sistema | string[] | Consecuencias para capacidad y organizacion del sistema |
| analisis_epi_ampliado_requerido | bool | True si necesita analisis epidemiologico adicional |

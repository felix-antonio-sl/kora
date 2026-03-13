---
_manifest:
  urn: urn:pro:skill:salubrista-hah-epi-vigilance:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-EPI-VIGILANCE

## Proposito
Conducir vigilancia epidemiologica relevante para sistemas de hospitalizacion integrados: brotes, IAAS, presion estacional, RAM, exposicion del personal y eventos que tensionan la seguridad, la capacidad o la continuidad del cuidado entre hospital y domicilio.

## Input/Output
- **Input:** señal: string, contexto: object
- **Output:** VigilanceReport { tipo_amenaza, evaluacion_riesgo, clasificacion_rsi, acciones_inmediatas: string[], implicancias_hospitalizacion: string[], notificacion_requerida: bool, analisis_sistema_requerido: bool }

## Procedimiento
1. KB_FIRST: resolver `kb_route` hacia razonamiento sanitario integrado y recuperar el contenido pertinente con `knowledge_retrieval` antes de complementar con web.
2. CARACTERIZAR la señal: cuando, donde, cuantos casos, severidad, poblacion afectada, capacidad de respuesta y modalidad implicada.
3. CLASIFICAR la amenaza:
   - brote infeccioso o clúster inusual
   - IAAS o evento de seguridad asociado a hospitalizacion
   - RAM
   - salud ocupacional
   - surge estacional o tension de demanda
4. EVALUAR riesgo:
   - gravedad
   - propagacion
   - impacto sobre camas, transiciones o continuidad
5. CLASIFICAR segun RSI 2005 cuando corresponda y definir `notificacion_requerida`.
6. DEFINIR acciones inmediatas:
   - contencion
   - proteccion de equipos
   - reorganizacion operativa
   - coordinacion hospital-red-domicilio
7. ESTIMAR implicancias para el sistema de hospitalizacion:
   - tension de camas
   - restricciones de egreso o HD
   - necesidad de aislamiento o rescate
   - impacto sobre continuidad del cuidado
8. SI la senal requiere analisis estructural de capacidad o trayectorias -> `analisis_sistema_requerido = true`
9. SI `web_search` es necesario para situacion actual o vigencia normativa -> ejecutar y citar.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_amenaza | string | Infecciosa / IAAS / RAM / Ocupacional / Surge |
| evaluacion_riesgo | string | Gravedad x propagacion x impacto operacional |
| clasificacion_rsi | string | Clasificacion operacional del evento |
| acciones_inmediatas | string[] | Acciones de respuesta |
| implicancias_hospitalizacion | string[] | Consecuencias para camas, transiciones o HD |
| notificacion_requerida | bool | True si amerita notificacion |
| analisis_sistema_requerido | bool | True si requiere analisis del sistema de hospitalizacion |

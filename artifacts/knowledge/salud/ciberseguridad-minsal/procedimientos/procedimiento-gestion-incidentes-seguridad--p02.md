---
_manifest:
  urn: urn:salud:kb:procedimiento-gestion-incidentes-seguridad-p02
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-04'
    source: MINSAL Chile, SGSI Nivel Central. PROS-NC-007 v07, Noviembre 2024
  minsal_id: PROS-NC-007
  minsal_version: '07'
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- procedimiento
- incidentes
- respuesta
- csirt
lang: es
extensions:
  kora:
    family: note
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:salud:kb:procedimiento-gestion-incidentes-seguridad
relations:
  cites:
  - urn:salud:kb:instructivo-seguridad-informacion-ciberseguridad-sector-salud
  - urn:salud:kb:stack-tecnologico-seguridad-minsal
---

# Procedimiento Gestion de Incidentes de Seguridad de la Informacion - Parte 02

## Registros

- Registro de cadena de custodia
- Registro de analisis de incidentes
- Registro de gestion de vulnerabilidades
- Acta de analisis de hallazgos
- Planilla de registro de incidentes
- Plan de accion
- Informe de incidentes
- Registro de cumplimiento del deber de notificar incidente
- Registro de cumplimiento de obligacion de denuncia (si procede)
- Registro de evidencias

## Anexo: Datos minimos del informe de incidentes

| Campo | Descripcion |
|---|---|
| Estado | Abierto, Acciones Inmediatas, Acciones Correctivas/Preventivas, Cerrado |
| Numero de Evento/Incidente | Identificador unico |
| Origen | Origen del evento/incidente |
| Fecha y Hora Reporte | Momento del reporte |
| Datos de quien reporta | Nombre, cargo, organizacion, datos de contacto |
| Activos/Sistemas afectados | Descripcion, numero de serie, marca, tipo, soporte |
| Tipo de Incidente | Informatico / No Informatico |
| Nivel de criticidad | Segun urgencia e impacto |
| Descripcion del incidente | Narrativa del hecho |
| Accion Inmediata | Descripcion de acciones inmediatas de contencion |
| Fecha y Hora Accion Inmediata | Momento de ejecucion |
| Se activa Continuidad del Negocio | S/N |
| Registros y evidencia | Identificacion de registros y evidencias que respaldan el proceso disciplinario |
| Analisis de causas | Causas raiz que produjeron el incidente |
| Accion Correctiva/Preventiva | Acciones para eliminar causas raiz |
| Costos asociados | Costos del incidente |
| Respuesta y Cierre | Resumen de actividades de cierre y conclusiones |
| Fecha Cierre | Fecha de cierre formal |
| Registro de Evidencias | Identificacion de registros y evidencias que respaldan las acciones realizadas |

## Difusion

- Publicacion en intranet MINSAL: http://isalud.minsal.cl/
- Correo informativo
- Publicacion en sitio web: http://www.minsal.cl/seguridad_de_la_informacion/

## Periodo de revision

Revision cada **2 anos** o cuando ocurran cambios significativos, garantizando adecuacion, actualizacion tecnologica y alineacion con legislacion vigente y estandares internacionales.

## Excepciones

En situaciones excepcionales, el Jefe de Departamento TIC, el CISO o el Comite de Seguridad pueden evaluar y establecer condiciones especificas de excepcion, siempre que no infrinjan la legislacion vigente ni comprometan la seguridad.

Cada excepcion debe documentarse e iniciar un proceso de revision de la politica para determinar si se requieren directrices adicionales o modificaciones.

## Control de versiones

| Version | Fecha | Cambios principales |
|---|---|---|
| v01 | Diciembre 2014 | Creacion del documento |
| v02 | Octubre 2017 | Actualizacion formato, diagramas de flujo, reemplazo de planilla de registro por aplicativo de gestion de incidentes |
| v03 | Octubre 2019 | Actualizacion alcance, correo de contacto, flujos, registros, responsabilidades |
| v04 | Agosto 2021 | Clasificacion de incidentes segun nivel y responsables de gestion |
| v05 | Noviembre 2022 | Actualizacion normativa ISO 27001:2022, alcance, terminologia, normativa de gobierno, roles y responsabilidades, plazos de notificacion |
| v06 | 2023 | Periodo de revision, excepciones |
| v07 | Noviembre 2024 | Version oficial actual |

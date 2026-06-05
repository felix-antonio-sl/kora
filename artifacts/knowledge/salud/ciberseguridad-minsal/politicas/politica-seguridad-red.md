---
_manifest:
  urn: urn:salud:kb:politica-seguridad-red
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-009 v02, Octubre 2019
  minsal_id: PS-NC-009 v2
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-seguridad-red
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
  - urn:salud:kb:politica-control-acceso-logico
  - urn:salud:kb:politica-proteccion-mensajes-electronicos
---

# Politica de Seguridad de la Red

## Proposito y alcance

Establece lineamientos para maximizar la efectividad de la operacion informatica, garantizando la proteccion de la informacion en las redes y sus instalaciones de procesamiento de informacion de apoyo. Mantiene la seguridad de la informacion transferida dentro de la institucion y con cualquier entidad externa.

Contempla la seguridad de todas las telecomunicaciones en redes internas y las establecidas con entidades externas.

Aplica a: funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

**Controles ISO 27001:2013 asociados**:

| Dominio | ID Control | Control |
| --- | --- | --- |
| Control de acceso | A.09.01.02 | Accesos a las redes y a los servicios de la red |
| Seguridad de las comunicaciones | A.13.01.01 | Controles de red |
| Seguridad de las comunicaciones | A.13.01.02 | Seguridad de los servicios de red |
| Adquisicion, desarrollo y mantenimiento del sistema | A.14.01.02 | Aseguramiento de servicios de aplicacion en redes publicas |

## Marco normativo y documentos relacionados

- NCh-ISO27001:2013 — Sistemas de gestion de la seguridad de la informacion — Requisitos
- Marco Juridico referido a los SSI, publicado en portal CSIRT del Ministerio del Interior
- Decretos Supremos y Normas Internacionales de Seguridad de la Informacion y Ciberseguridad

**Documentos relacionados**: Procedimiento gestion de derechos de acceso y devolucion de activos, Politica control de acceso, Politica proteccion de mensajes electronicos.

## Roles y responsabilidades

**Jefe Departamento TIC** — Dispone controles y reglas de control de acceso. Autoriza mecanismos de control para los dominios de seguridad. Aprueba medidas de control para excepciones que permitan acceso directo desde dominios "No Confiables" hacia servidores de produccion.

**Area de Operaciones TIC** — Responsable de la aplicacion operativa de esta politica.

**Encargado de Seguridad de la Informacion / Encargado de Ciberseguridad** — Coordina mecanismos de control para los dominios de seguridad definidos.

## Materias que aborda

- Accesos a las redes y a los servicios de la red
- Controles de red
- Seguridad de los servicios de red
- Aseguramiento de servicios de aplicacion en redes publicas

## Definiciones

**SLA** — Acuerdo escrito entre proveedor de servicio y cliente que fija el nivel acordado de calidad del servicio: tiempo de respuesta, disponibilidad horaria, documentacion disponible, personal asignado, etc.

**WPA2** — Sistema para proteger redes inalambricas (Wi-Fi) que utiliza la version certificada del estandar 802.11i. Creado para corregir deficiencias del sistema previo WPA.

**Red inalambrica** — Conexion de nodos mediante ondas electromagneticas, sin necesidad de red cableada.

## Directrices

### Cumplimiento de la legislacion

Las medidas de control de acceso a la informacion deben cumplir y ser consistentes con las normas y requerimientos legales definidos en la Normativa del SGSI.

### Gestion en controles de red

- Las redes se deben gestionar, controlar su acceso y uso, para proteger la informacion en sistemas y aplicaciones
- Todo usuario que acceda a la red debe contar con identificacion individual unica
- Todo acceso a servicios criticos debe ser validado; todo intento, exitoso o fallido, debe ser registrado para analisis posterior
- La red debe restringir accesos riesgosos: mensajeria instantanea, descarga de archivos desde sitios peer to peer, acceso a sitios de pornografia, conexiones a sitios de streaming no autorizados

### Gestion en seguridad de los servicios de red

- Los mecanismos de seguridad, niveles de servicio (SLAs) y requisitos de gestion de todos los servicios de red se deben identificar e incluir en los acuerdos de servicios de red, sean prestados en forma interna o por terceros
- Los puertos de configuracion y de diagnosticos de los dispositivos de la red de comunicaciones deben ser protegidos de accesos no autorizados

### Gestion en separacion y segmentacion de las redes

- Identificar los dominios o zonas de seguridad requeridos en la arquitectura de la red de telecomunicaciones, permitiendo establecer distintos niveles de confianza
- No permitir accesos directos entre dominios no confiables hacia un ambiente productivo
- Separar grupos de servicios de informacion, usuarios y sistemas de informacion en dominios o zonas de seguridad segun su criticidad para la institucion

### Gestion en proteccion en la transferencia de informacion

- Las politicas, procedimientos y controles de transferencia formal deben estar en efecto para proteger la transferencia de informacion mediante todos los tipos de instalaciones de comunicacion necesarias
- Los acuerdos deben considerar la transferencia segura de informacion del negocio entre la organizacion y terceros. Estas conexiones deben ser monitoreadas mediante procesos definidos y controlados por revisiones periodicas
- Senalar niveles de proteccion adecuados al nivel de sensibilidad de la informacion transferida, acordando necesidad de cifrado y/o firma digital para la transferencia

### Gestion en mensajeria electronica

- Establecer politica particular de acceso y uso del sistema de correo electronico institucional (ver Politica de proteccion de mensajes electronicos)
- La informacion involucrada en mensajeria electronica debe ser debida y adecuadamente protegida

### Gestion en redes inalambricas

- La incorporacion de redes inalambricas no debe afectar el nivel de seguridad de la red institucional; su acceso a otras redes debe ser controlado con el equipamiento necesario
- Las contrasenas deben ser WPA2 o superior, con composicion robusta y cambiadas segun el estandar institucional
- Mantener nomina de accesos inalambricos con contrasenas, ubicacion y usuarios que la utilizan frecuentemente
- Estas redes deben constituir un dominio separado de las otras redes institucionales, cuidando que su alcance no cubra zonas fuera de control
- Establecer sistema de monitoreo permanente de redes inalambricas, con capacidad de alertar eventos sospechosos

### Gestion de auditorias

- Establecer revisiones periodicas de cumplimiento de los controles definidos, para asegurar proteccion contra acceso de personas no autorizadas
- El Encargado de Seguridad de la Informacion / Encargado de Ciberseguridad es responsable de establecer revisiones periodicas de cumplimiento de controles

### Gestion en Acuerdos de confidencialidad o no divulgacion

- Identificar y revisar regularmente los requisitos de confidencialidad o acuerdos de no divulgacion que reflejen necesidades de proteccion de informacion institucional
- Generar acuerdos de confidencialidad o NDA (non-disclosure agreement) como documento base para cada tipo de acuerdo con terceros

### Aseguramiento de servicios de aplicacion en redes publicas

La informacion relacionada a servicios de aplicacion que pasan por redes publicas debe ser protegida de actividad fraudulenta, disputas contractuales, divulgacion y modificacion no autorizada.

## Mecanismo de difusion

- Publicacion en intranet MINSAL http://isalud.minsal.cl/
- Correo informativo

## Periodo de revision

Revision a lo menos cada dos anos por el Comite de Seguridad de la Informacion, o segun necesidades de cambio para garantizar idoneidad, adecuacion y efectividad.

## Excepciones

El Comite de Seguridad de la Informacion evaluara y podra establecer condiciones puntuales de excepcion, siempre que no infrinja la legislacion vigente. Toda excepcion debe documentarse y generar un proceso de revision que determine si se deben agregar directrices particulares.

## Historial de versiones

| Version | Fecha | Cambios |
| --- | --- | --- |
| 01 | Agosto 2014 | Creacion del documento |
| 02 | Octubre 2019 | Cambio de formato, actualizacion de referencias normativas, actualizacion de todos los puntos de la politica |

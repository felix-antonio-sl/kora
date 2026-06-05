---
_manifest:
  urn: urn:salud:kb:politica-seguridad-gestion-proyectos-sla
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-006 v02, Octubre 2019
  minsal_id: PS-NC-006 v2
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
    shard_root_urn: urn:salud:kb:politica-seguridad-gestion-proyectos-sla
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
  - urn:salud:kb:politica-relaciones-proveedores
---

# Politica de Seguridad en la Gestion de Proyectos y Monitoreo de Acuerdos de Servicio

## Proposito y alcance

Define las reglas de seguridad para resguardo de informacion personal sensible en gestion de proyectos y monitoreo de acuerdos de servicio en procesos de compra y administracion de servicios en MINSAL.

Aplica a proyectos o servicios con uso o tratamiento de datos sensibles segun Ley 19.628. Datos sensibles: caracteristicas fisicas o morales, habitos personales, origen racial, ideologias politicas, creencias religiosas, estados de salud fisicos/psiquicos, vida sexual. Incluye estados de salud presente, pasado, futuro o pronosticado y cualquier informacion que permita identificar situacion medica.

Aplica a: funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

**Controles ISO 27001:2013 asociados**:

| Dominio | ID Control | Control |
| --- | --- | --- |
| Organizacion de la seguridad de la informacion | A.06.01.05 | Seguridad de la informacion en la gestion de proyecto |
| Relaciones con el proveedor | A.15.02.01 | Supervision y revision de los servicios del proveedor |
| Relaciones con el proveedor | A.15.02.02 | Gestion de cambios a los servicios del proveedor |

## Marco normativo y documentos relacionados

- NCh-ISO27001:2013 — Sistemas de gestion de la seguridad de la informacion — Requisitos
- Marco Juridico referido a los SSI, publicado en portal CSIRT del Ministerio del Interior
- Ley Nº19.628, 1999 — Proteccion de la vida privada
- Ley N°20.285, 2008 — Acceso a la informacion publica
- Ley N°20.584, 2012 — Derechos y deberes en atencion de salud
- Resolucion Exenta N°636, 12.08.2011 — Manual de Procedimientos de Adquisiciones MINSAL
- Resolucion Exenta N°1305, 08.11.2016 — Modifica Manual de Procedimientos de Adquisiciones

**Documentos relacionados**: Politica para acuerdos de intercambio de informacion y software, Procedimiento acuerdos de confidencialidad en contratos con terceros, Politica de Seguridad para las Relaciones con los Proveedores.

## Roles y responsabilidades

**Jefe de Division o Departamento** — Define funcionario o equipo responsable de administracion de proyectos y acuerdos de servicios.

**Funcionario o equipo responsable** — Cumple requisitos definidos en esta politica en administracion de proyectos y acuerdos de servicio.

## Materias que aborda

- Seguridad de la informacion en la gestion de proyecto
- Supervision y revision de los servicios del proveedor
- Gestion de cambios a los servicios del proveedor

## Directrices

### Seguridad de la informacion en la administracion de proyectos

En todo proyecto con uso o tratamiento de datos de caracter sensible, se debe abordar la seguridad de la informacion en diseno y administracion, sin importar el tipo de proyecto (proceso comercial, TI, administracion de instalaciones, procesos de apoyo). Se deben identificar y abordar los riesgos de seguridad como parte del proyecto.

La administracion del proyecto debe incluir:

- Objetivos de seguridad de la informacion en concordancia con la informacion personal sensible tratada
- Evaluacion de riesgos para proteccion de datos sensibles para identificar controles necesarios
- Evaluacion de riesgos de seguridad de la informacion en etapa temprana del proyecto para identificar controles necesarios
- Seguridad de la informacion como parte de todas las etapas del proyecto, independiente de la metodologia utilizada

La Jefatura responsable debe definir un funcionario como responsable de seguridad de la informacion (puede ser el Jefe de proyecto o parte del equipo), quien vela por inclusion de objetivos y requerimientos de seguridad.

En proyectos que requieran compras, seguir pautas de seguridad definidas en punto 6.2 de esta politica (ver [-> Seguridad de la informacion en los procesos de compras]).

### Seguridad de la informacion en los procesos de compras

Los procesos de compra se realizan segun Resolucion Exenta N°636 (12.08.2011) y sus modificaciones, mediante: Convenio Marco, Licitacion o Propuesta Publica, Licitacion o Propuesta Privada, Trato o Contratacion Directa.

Ademas de incluir clausulas de confidencialidad del Procedimiento de acuerdos de confidencialidad en contratos con terceros, se deben incluir clausulas de proteccion de informacion segun tipo de compra:

| Tipo de compra | Umbral | Requisitos de seguridad en |
| --- | --- | --- |
| Convenio Marco | Menor a 1.000 UTM | Especificaciones tecnicas y administrativas, Acuerdo complementario |
| Convenio Marco | Mayor a 1.000 UTM | Especificaciones tecnicas y administrativas, Acuerdo complementario |
| Licitacion o Propuesta Publica | Menor a 100 UTM | Terminos de referencia |
| Licitacion o Propuesta Publica | 100 a 1.000 UTM | Terminos de referencia |
| Licitacion o Propuesta Publica | 1.001 a 4.999 UTM | Terminos de referencia |
| Licitacion o Propuesta Publica | Mayor o igual a 5.000 UTM | Terminos de referencia |
| Trato o Contratacion Directa | Menor a 1.000 UTM | Resolucion que aprueba el trato directo |
| Trato o Contratacion Directa | Mayor a 1.000 UTM | Resolucion que aprueba el trato directo |

Para todos los tipos: se deben definir requisitos de seguridad que resguarden integridad, confidencialidad y disponibilidad de la informacion asociada al proyecto.

### Monitoreo y revision de los servicios del proveedor

En servicios de proveedores con uso o tratamiento de datos sensibles, la Division o Departamento encargada de la administracion del acuerdo debe mantener control y visibilidad suficientes en todos los aspectos de seguridad para la informacion o instalaciones de procesamiento de informacion personal sensible y critica que evalua, procesa o administra un proveedor.

El Jefe de Division o Departamento debe definir un funcionario o equipo responsable de administrar las relaciones con el proveedor, quienes deberan monitorear, revisar y auditar la prestacion de servicios de manera regular.

El monitoreo y revision debe garantizar inclusion y cumplimiento de terminos y condiciones de seguridad en los acuerdos de compra, y gestion correcta de incidentes y problemas. Incluye:

- Monitorear niveles de desempeno del servicio para verificar adherencia a los acuerdos
- Revisar informes de servicio del proveedor y organizar reuniones de avance regulares segun acuerdos
- Realizar auditorias de proveedores, con revision de informes de auditores independientes si estan disponibles, y seguimiento de problemas identificados (se deben incluir en contratos que MINSAL se reserva el derecho de auditar servicios, software o producto)
- Proporcionar informacion sobre incidentes de seguridad y revisarla segun acuerdos y pautas o procedimientos de apoyo
- Revisar seguimientos de auditoria del proveedor y registros de eventos de seguridad, problemas operacionales, fallas e interrupciones relacionadas con el servicio
- Resolver, gestionar y/o escalar cualquier problema, incidente o evento de seguridad identificado; monitorear acciones inmediatas y correctivas/preventivas
- Asegurar que el proveedor cumple prohibiciones de uso secundario de informacion sensible definidos en la compra del servicio, procedimientos y controles especificos, criticidad de la informacion, sistemas y procesos involucrados
- Asegurar que el proveedor mantiene capacidad de servicio suficiente con planes de trabajo que garanticen niveles de continuidad tras fallas graves o desastres

### Administracion de cambios en los servicios del proveedor

Los cambios en provision de servicios deben ser administrados por el funcionario o equipo asignado para monitoreo y revision. La administracion debe considerar mantenimiento y/o mejora de requisitos de seguridad definidos en la compra del servicio, procedimientos y controles especificos, criticidad de la informacion, sistemas y procesos involucrados, y reevaluacion de riesgos.

Cambios a considerar:

- Cambios a los acuerdos del proveedor
- Cambios realizados por la organizacion: mejoras a servicios actuales, desarrollo de nuevas aplicaciones y sistemas, modificaciones o actualizaciones de politicas y procedimientos, controles nuevos o cambiados para resolver incidentes y mejorar seguridad
- Cambios en servicios del proveedor: cambios y mejoras en redes, uso de nuevas tecnologias, adopcion de nuevos productos o versiones, nuevas herramientas y entornos de desarrollo, cambios en ubicacion fisica de instalaciones de servicios, cambio de proveedores, cambios en equipo del proveedor, subcontratacion a otro proveedor

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
| 01 | Noviembre 2016 | Creacion del documento |
| 02 | Octubre 2019 | Ajuste de formato, modificacion de referencias normativas, modificacion del alcance |

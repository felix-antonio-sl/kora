---
_manifest:
  urn: urn:salud:kb:politica-continuidad-seguridad-informacion
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-001 v4
version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- politica
- continuidad
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-continuidad-seguridad-informacion
  salud:
    minsal_id: PS-NC-001
    minsal_version: '4'
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Continuidad de la Seguridad de la Informacion -- PS-NC-001 v04

Sistema de Gestion de Seguridad de la Informacion -- MINSAL Nivel Central. Octubre 2019.

## Proposito y alcance

Garantizar la continuidad de la seguridad de la informacion durante situaciones adversas (fallas, desastres) para evitar interrupciones en activos criticos del negocio.

Aplica a todos los recursos computacionales de MINSAL Nivel Central y a todos los funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros de la Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

### Controles ISO 27001:2013 asociados

| Control | Nombre |
|---|---|
| A.17.1.1 | Planificacion de la continuidad de la seguridad de la informacion |
| A.17.1.2 | Implementacion de la continuidad de la seguridad de la informacion |
| A.17.1.3 | Verificacion, revision y evaluacion de la continuidad de la seguridad de la informacion |

## Marco normativo

| Instrumento | Referencia |
|---|---|
| NCh-ISO 27001:2013 | Sistemas de gestion de la seguridad de la informacion -- Requisitos |
| Marco Juridico SSI | Publicado en portal CSIRT del Ministerio del Interior |

Documentos SGSI disponibles en `isalud.minsal.cl`.

## Roles

| Rol | Responsabilidad |
|---|---|
| Subsecretario de Redes Asistenciales / Subsecretario de Salud Publica | Aprobacion de la politica y planes de continuidad |
| Jefes de Unidad de Negocio (Divisiones, Departamentos) | Designar responsable administrativo para elaborar Plan de Continuidad |
| Departamento TIC | Elaborar Planes de Continuidad de hardware y software; velar por ejecucion correcta ante eventos |
| Encargado de Seguridad / Encargado de Ciberseguridad | Revisar y respaldar planes formalizados; velar por comunicacion interna |

## Materias que aborda

- Planificacion de la continuidad de la seguridad de la informacion
- Implementacion de la continuidad de la seguridad de la informacion
- Verificacion, revision y evaluacion de la continuidad

## Directrices

### Cumplimiento legislativo

Las medidas de control deben ser consistentes con la Normativa del SGSI.

### Planificacion de la continuidad

Los requisitos de seguridad de la informacion se mantienen identicos ante situaciones adversas. Se deben establecer, documentar, implementar y mantener procesos, procedimientos y controles que contengan al menos:

| Elemento | Contenido |
|---|---|
| Analisis de riesgos | Probabilidad de ocurrencia e impacto; identificacion y priorizacion de activos criticos por proceso |
| Controles preventivos | Identificacion y evaluacion de controles de reduccion de riesgo |
| Recursos | Financieros, organizacionales, tecnicos y ambientales para los requisitos de seguridad |
| Planes | Formulacion y documentacion de planes de seguridad de la informacion |
| Prueba y actualizacion | Prueba y actualizacion regular de planes y procesos |

### Implementacion de la continuidad

#### Responsabilidades

Los responsables de activos criticos deben contar con estructura de administracion adecuada para prepararse, mitigar y responder ante eventos disruptivos:

- Nominar personal de respuesta ante incidentes con responsabilidad, autoridad y competencia necesaria
- Desarrollar y aprobar planes documentados con procedimientos de respuesta y recuperacion detallados
- Determinar nivel predeterminado de seguridad de informacion durante eventos disruptivos

#### Tabla de responsables por tipo de activo

| Tipo de activo | Activos | Responsable del plan |
|---|---|---|
| Hardware y Software | BD, equipos, sistemas, formularios web | Dependencia TIC correspondiente |
| Documentos, expedientes, personas, infraestructura | Documentos, personal, edificios, equipamiento | Jefe de Unidad de Negocio del proceso |

Las areas de negocio no TIC que administren su propio hardware y software son responsables de cumplir esta politica.

#### Analisis previo para planes de continuidad

Los responsables de cada tipo de activo deben analizar:

| Analisis | Detalle |
|---|---|
| Activos criticos del negocio | Identificar |
| Eventos de interrupcion | Identificar eventos o cadenas que puedan ocasionar interrupciones |
| Probabilidad e impacto | Analizar y evaluar para interrupciones por incidentes de seguridad |
| Alcance de evaluacion | Todos los activos, no solo servicios de procesamiento |
| Criterios de riesgo | Recursos criticos, impacto de interrupciones, duracion permitida de corte, prioridades de recuperacion |

A partir de los resultados se desarrollan los planes de continuidad para procesos y activos criticos.

#### Desarrollo de planes de continuidad

Los responsables deben elaborar los planes antes de su implementacion. En la planificacion se debe:

| Requisito | Detalle |
|---|---|
| Recursos y servicios | Identificar personal, respaldos, acuerdos con terceros, recursos no-TI |
| Prioridades y tiempos | Identificar por activo/proceso |
| Roles y responsabilidades | Identificar, acordar y documentar internos y externos |
| Perdida aceptable | Identificar perdida aceptable de informacion y servicios |
| Procedimientos operativos | Establecer, documentar e implementar para recuperacion y restauracion |
| Capacitacion | Capacitar y difundir procedimientos al personal |
| Pruebas | Realizar revisiones, pruebas y actualizacion; documentar resultados |
| Almacenamiento seguro | Copias de planes y material en lugar seguro, alejado del local principal, mismo nivel de seguridad |
| Revision periodica | Minimo cada 2 anos |

#### Estructura de los planes de continuidad

Cada plan debe incluir al menos:

- **Condiciones de activacion** -- que debe ocurrir para activar cada plan
- **Procedimientos de emergencia** -- acciones tras un incidente que ponga en peligro operaciones
- **Procedimientos de respaldo** -- acciones para desplazar actividades esenciales a lugares alternos y devolver operatividad en tiempos requeridos
- **Procedimientos operativos temporales** -- a seguir mientras se termina recuperacion y restauracion
- **Procedimientos de restauracion** -- acciones para volver a la normalidad
- **Cronograma de mantenimiento** -- cuando y como se realizaran pruebas del plan
- **Concientizacion y formacion** -- educacion del personal en procesos de continuidad
- **Responsabilidades** -- responsable de cada componente y suplentes; plan de escalada
- **Activos y recursos criticos** -- necesarios para ejecutar procedimientos de emergencia, respaldo y restauracion
- **Gestion de relaciones publicas** -- coordinacion con autoridades (policia, bomberos, directivas) y convocatoria de responsables de documentos electronicos y sistemas afectados
- **Contactos de apoyo** -- ante dificultades tecnicas u operacionales inesperadas

El Jefe de Servicio aprueba los planes, sanciona estrategias y asigna recursos.

### Verificacion, revision y evaluacion

| Frecuencia | Alcance |
|---|---|
| Anual | Activos de maxima criticidad y riesgo |
| Al menos cada 2 anos | Resto de activos |

Pruebas requeridas que aseguren que los miembros del equipo de recuperacion son conscientes de los planes y sus responsabilidades:

| Tecnica | Proposito |
|---|---|
| Prueba sobre papel | Escenarios de interrupcion (distintos ejemplos) |
| Simulaciones | Formacion de personal |
| Pruebas de recuperacion tecnica | Restauracion eficaz de sistemas de informacion |
| Pruebas de recuperacion en lugar alterno | Verificacion de sitio alterno |
| Pruebas de proveedores externos | Servicios y productos cumplen compromiso |
| Ensayos completos | Organizacion, personal, equipo, instalaciones y procesos funcionan ante interrupciones |

Se debe asignar responsabilidad para revisiones regulares de cada plan. El control de cambios formal debe garantizar distribucion de planes actualizados, con atencion especial a cambios en: equipamiento, sistemas, personal, direcciones/telefonos, estrategia del negocio, lugares/dispositivos/recursos, legislacion, proveedores/contratistas, procesos (nuevos, existentes o retirados) y riesgos.

## Difusion

| Canal | Destino |
|---|---|
| Intranet MINSAL | `http://isalud.minsal.cl` |
| Correo informativo | Funcionarios |

## Periodo de revision

Minimo cada **2 anos** por el Comite de Seguridad de la Informacion, o ante necesidades de cambio que requieran garantizar idoneidad, adecuacion y efectividad.

## Excepciones

El Comite de Seguridad de la Informacion evalua y establece condiciones puntuales de excepcion, siempre que no infrinjan legislacion vigente. Toda excepcion debe documentarse e iniciar revision de la politica para determinar directrices adicionales o modificaciones.

## Control de versiones

| Version | Fecha | Secciones | Motivo |
|---|---|---|---|
| 01 | Marzo 2015 | Todas | Creacion del documento |
| 02 | Agosto 2015 | Todas | Ajustes |
| 03 | Septiembre 2015 | Todas | Revision Equipo |
| 04 | Octubre 2019 | Todas | Cambios en referencia normativa, formato, responsabilidades |

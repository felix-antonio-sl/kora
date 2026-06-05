---
_manifest:
  urn: urn:salud:kb:politica-clasificacion-manejo-informacion
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, Depto. TIC, Unidad de Seguridad de la Informacion. PS-NC-016
      v4.0 (Marzo 2023).
  version: 1.0.0
status: publicado
tags:
- seguridad-informacion
- minsal
- sgsi
- clasificacion-informacion
- manejo-informacion
- activos-informacion
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:politica-clasificacion-manejo-informacion
  salud:
    minsal_id: PS-NC-016
    minsal_version: '4.0'
    fecha_aprobacion: Marzo 2023
    elaborado_por: Rodrigo Vidal, Unidad Seguridad de la Informacion
    revisado_por:
    - Jose Villa, Encargado de Seguridad de la Informacion
    - Carlos Maldonado, Encargado Operaciones
    - Rodrigo Zamorano, Encargado Proyectos
    aprobado_por: Jorge Herrera, Jefe Depto. TIC
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
---

# Politica de Seguridad para la Clasificacion y Manejo de Informacion

**PS-NC-016 v4.0, Marzo 2023. Caracter obligatorio.**

## Resumen

Clasifica los activos de informacion para garantizar una eficaz gestion de su seguridad, protegiendo la informacion y documentacion sensible del MINSAL contra divulgacion y acceso no autorizado. Define niveles de confidencialidad (Secreto, Reservado, Uso Interno, Publico, No Clasificada), reglas de etiquetado, tratamiento segun clasificacion y estado, y responsabilidades sobre activos. Cubre controles NCh-ISO 27002:2013 A.08.01.02, A.08.01.03, A.08.02.01, A.08.02.02, A.08.02.03, A.18.01.03.

---

## 1. Proposito

Clasificar los activos de informacion para garantizar una eficaz gestion de seguridad, protegiendo informacion y documentacion sensible del MINSAL contra divulgacion y acceso por personas o instituciones no autorizadas.

## 2. Alcance

Aplica a todos los recursos computacionales del MINSAL y sus areas dependientes con acceso a Internet.

Aplica a todo tipo de informacion independientemente del soporte: documentos, sistemas de informacion, redes, sistemas de comunicaciones moviles, dispositivos moviles, nubes, correo, correo de voz, comunicaciones de voz, multimedia, servicio postal y cualquier otro elemento sensible (cheques en blanco, facturas, etc.).

Aplica a todos los funcionarios (planta, contrata, reemplazos y suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para la Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

### Controles de Seguridad Cubiertos (NCh-ISO 27002:2013)

| ID Control | Nombre |
|---|---|
| A.08.01.02 | Propiedad de los activos |
| A.08.01.03 | Uso aceptable de los activos |
| A.08.02.01 | Clasificacion de la informacion |
| A.08.02.02 | Etiquetado de la informacion |
| A.08.02.03 | Manejo de activos |
| A.18.01.03 | Proteccion de registros |

## Marco Normativo

### Leyes y Decretos

- NCh-ISO IEC 27001:2013 — Sistemas de gestion de la seguridad de la informacion
- NCh-ISO IEC 27002:2013 — Codigos de practicas para los controles de seguridad de la informacion
- Ley 19.628 — Proteccion de vida privada y datos personales
- Ley 19.799 — Firmas y documentos electronicos
- Ley 19.927 — Delitos de Pornografia Infantil
- Ley 20.285 — Transparencia de la funcion publica y acceso a la informacion
- Ley 21.180 — Transformacion Digital del Estado
- Ley 21.459 — Delitos Informaticos (Convenio de Budapest)
- Decreto 83/2004 (Min. Secretaria General de la Presidencia) — Norma tecnica sobre seguridad y confidencialidad de documentos electronicos
- Marco Juridico SSI, CSIRT
- Decretos Supremos y Normas Internacionales de Seguridad de la Informacion y Ciberseguridad

### Documentos Relacionados

- Procedimiento de gestion de derechos de acceso y devolucion de activos
- Politica de Seguridad en la Red

## Definiciones

- **Activo de Informacion**: Algo que la organizacion valora y debe proteger (ISO/IEC 27001). Datos creados o utilizados por un proceso de la organizacion en medio digital, papel u otros medios
- **Clasificacion de la Informacion**: Ejercicio por el cual se determina que la informacion pertenece a uno de los niveles de clasificacion del MINSAL, para asegurar el nivel de proteccion adecuado
- **Confidencialidad**: Propiedad que determina que la informacion solo este disponible y sea revelada a individuos, entidades o procesos autorizados
- **Datos Sensibles**: Datos personales referidos a caracteristicas fisicas o morales de las personas o hechos/circunstancias de su vida privada o intimidad (habitos personales, origen racial, ideologias y opiniones politicas, creencias o convicciones religiosas, estados de salud fisicos o psiquicos, vida sexual). Ley 19.628
- **Disponibilidad**: Propiedad que asegura que la informacion sea accesible y utilizable por solicitud de una entidad autorizada cuando se requiera
- **Etiquetado**: Identificador del tipo de calificacion de la informacion
- **Informacion**: Conjunto de datos que organizados en determinado contexto tienen significado o importancia
- **Integridad**: Propiedad de salvaguardar la exactitud y estado completo de los activos

## Roles y Responsabilidades

### Comite de Seguridad de la Informacion

- Aprobar solicitudes de acceso a la informacion publica, garantizando su confidencialidad y cumplimiento normativo, previniendo acceso y divulgacion no autorizados

### Jefe Depto. TIC

- Informar y concientizar a los funcionarios sobre los riesgos de manejar informacion confidencial
- Adoptar medidas necesarias para evitar dichos riesgos y proporcionar entrenamiento
- Supervisar los respaldos de software esencial

### Encargado de Seguridad de la Informacion

- Presentar al Comite de Seguridad Sectorial las solicitudes de acceso a informacion confidencial para su debida revision y evaluacion

### Dueno del Activo de Informacion

- Jefe de la Unidad Administrativa designado, con responsabilidad y autoridad permanente sobre determinada informacion
- Adoptar medidas para garantizar que los activos asociados con servicios de procesamiento de informacion se clasifiquen adecuadamente
- Definir y revisar periodicamente las restricciones y clasificaciones del acceso, considerando politicas de control de acceso (fisico o logico) y normativa pertinente

### Responsable Administrativo

- Jefe del Departamento al cual pertenecen los activos de informacion
- Responsable de administrar y gestionar los datos de manera adecuada cumpliendo regulaciones y politicas
- Hacer efectivos los controles de seguridad definidos por el dueno de la informacion: copias de seguridad, asignacion privilegios de acceso, modificacion y borrado

### Encargado de Transparencia Pasiva

- Asesorar en materias de clasificacion de la informacion respecto a su divulgacion y acceso publico

### Funcionarios y Personal en General

- Cumplir con las normas de este documento y la Politica de Proteccion de Datos y Privacidad de la Informacion Personal
- Actuar en pleno cumplimiento de la legislacion vigente

## Directrices de la Politica

### Responsables de los Activos de Informacion

| Tipo de Activo | Dueno del Activo | Responsable Administrativo |
|---|---|---|
| Software | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe del Depto. TIC |
| Base de datos | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe del Depto. TIC |
| Equipos | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe del Depto. TIC |
| Sistema | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe del Depto. TIC |
| Formularios | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe del Depto. TIC |
| Documentos | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe de la Unidad Administrativa donde se desarrolla el proceso |
| Expediente | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe de la Unidad Administrativa donde se desarrolla el proceso |
| Personas | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe Depto. de Desarrollo de Personas |
| Infraestructura | Jefe de la Unidad Administrativa donde se desarrolla el proceso | Jefe Depto. de Administracion |

En conjunto con el dueno del activo, el responsable administrativo debe definir y revisar periodicamente las restricciones y clasificacion del acceso, considerando politicas de control de acceso y normativa vigente.

### Gestion de Inventario y Activos de la Informacion

Todos los activos deben estar debidamente identificados y determinada su importancia para el MINSAL. El dueno del activo debe elaborar y mantener un inventario de los activos mas importantes con la siguiente informacion minima:

- **Nombre Activo**: Nombre de identificacion dentro del proceso al que pertenece
- **Proceso**: Nombre del proceso al que pertenece el activo
- **Tipo de activo**:

| Tipo | Descripcion |
|---|---|
| Informacion | Datos e informacion almacenada o procesada fisica o electronicamente: bases y archivos de datos, contratos, documentacion del sistema, investigaciones, acuerdos de confidencialidad, manuales de usuario, procedimientos operativos o de soporte, planes de continuidad del negocio, acuerdos sobre retiro, pruebas de auditoria |
| Software | Software de aplicacion, interfaces, software del sistema, herramientas de desarrollo y utilidades |
| Recurso humano | Personas que por su conocimiento, experiencia y criticidad para el proceso son consideradas activos de informacion |
| Servicio | Servicios de computacion y comunicaciones: Internet, paginas de consulta, directorios compartidos, Intranet |
| Hardware | Equipos de computo y comunicaciones que por su criticidad son considerados activos de informacion |
| Otros | Activos que no corresponden a ninguno de los tipos anteriores pero deben ser valorados por su criticidad |

- **Ubicacion**: Localizacion tanto fisica como electronica del activo
- **Fecha de creacion**: Registrada en las tablas de retencion documental
- **Responsable del activo**: Nombre del area, dependencia o unidad interna, o entidad externa que creo la informacion

La propiedad y clasificacion deben ser acordadas y documentadas para cada activo inventariado, basandose en:

- **Clasificacion**: Proteccion segun Confidencialidad, Integridad y Disponibilidad
- **Criticidad**: Calculo automatico que determina el valor general del activo:

| Nivel | Criterio |
|---|---|
| Alta | Clasificacion en dos o todas las propiedades (confidencialidad, integridad, disponibilidad) es alta |
| Media | Clasificacion alta en una propiedad o al menos una de nivel medio |
| Baja | Clasificacion en todos los niveles es baja |

Niveles de proteccion segun criticidad: controles minimos que deben aplicarse segun nivel de clasificacion.

Ciclo de vida del activo: todas las fases desde su concepcion e incorporacion, actualizaciones, hasta su disposicion final mediante descarte, reciclaje o venta.

Todos los datos e informacion deben tener un propietario que los clasifique segun los niveles de la seccion Clasificacion de la Informacion. Para activos no inventariados o documentos de caracter transitorio o no oficial (borradores, proyectos) sin responsable explicito, el creador de la informacion es responsable de aplicar los niveles de seguridad requeridos.

### Clasificacion de la Informacion

La informacion se clasifica por estado y nivel de confidencialidad.

#### Estado

| Estado | Descripcion |
|---|---|
| En transito | Informacion para uso exclusivo del MINSAL que esta siendo transferida o desplazada fisica o electronicamente. Ejemplo: respaldos a actos administrativos (acta, minuta, circular interna, correo electronico) |
| Producto final | Documentos que han alcanzado su version final y definitiva, listos para distribucion, publicacion o uso oficial. Ejemplo: leyes, reglamentos, resoluciones, decretos, ordinarios en cualquier soporte |

#### Confidencialidad

| Nivel | Descripcion | Restriccion de Acceso |
|---|---|---|
| Secreto | Documentos que la ley establece como secretos, no pueden ser divulgados. Su publicidad puede conllevar alto impacto negativo legal, operativo, de imagen o economico | Solo para grupo especifico de personas con funciones definidas |
| Reservado | Informacion altamente sensible, de uso exclusivamente interno. Su divulgacion podria implicar impacto no deseado para el MINSAL o transgresion a normativa vigente. Debe ser declarada como reservada considerando Ley 20.285 | Solo para grupo especifico de empleados y terceros autorizados |
| Uso Interno | Acceso no autorizado podria ocasionar danos y/o inconvenientes menores a la organizacion | Para todos los empleados y terceros seleccionados. Puede entregarse al publico sujeto a cumplimiento de normativa vigente, previa consulta al dueno del activo |
| Publica | Informacion no secreta ni reservada cuyo acceso y/o difusion no cause perjuicio al MINSAL | Entrega mediante canal de OIRS o por transparencia, segun corresponda |
| No Clasificada | Activos que deben ser incluidos en el inventario y que aun no han sido clasificados. Deben ser tratados como activos no etiquetados | Informacion no etiquetada |

La normativa calificada como confidencial o reservada estara enlistada y disponible en las oficinas de informacion o atencion del usuario, segun Ley 20.285, su reglamento e instrucciones generales del Consejo para la Transparencia.

### Manejo de la Informacion

#### Etiquetado de la Informacion segun su Clasificacion

Reglas generales:

- Activos de tipo publico: no requieren etiquetado, independientemente del formato
- Activos con otros niveles de confidencialidad se etiquetan segun la siguiente tabla:

| Soporte | Nivel Reservado / Uso Interno | Nivel Secreto |
|---|---|---|
| Documentos en papel | Indicar nivel al menos en la portada | Indicar nivel en la portada, en cada pagina, en el sobre contenedor y en la carpeta de archivo |
| Documentos electronicos | Indicar nivel al menos en la portada | Indicar nivel en la portada y en cada pagina |
| Correo electronico | Indicar nivel en la primera linea del cuerpo del correo | Indicar nivel en la primera linea del cuerpo del correo |
| Soporte de almacenamiento electronico (discos, tarjetas de memoria) | Indicar nivel sobre la superficie de cada soporte | Indicar nivel sobre la superficie de cada soporte |
| Informacion transmitida oralmente | Comunicar el nivel de clasificacion antes de la informacion propiamente dicha | Comunicar el nivel de clasificacion antes de la informacion propiamente dicha |

Activo en formato impreso no etiquetado: debe ser tratado en todos sus niveles (Confidencialidad, Integridad y Disponibilidad) como NO CLASIFICADA. Se debe informar al responsable designado para que tome medidas correspondientes (aplicacion de clasificacion adecuada e implementacion de salvaguardias de seguridad).

#### Tratamiento de la Informacion segun su Clasificacion

La informacion debe ser tratada de acuerdo con su clasificacion y su estado, considerando su generacion, transmision, recepcion, procesamiento y almacenamiento. Las medidas de seguridad para el tratamiento de la informacion se definen en la tabla de tratamiento de la politica original (Seccion 7.4.2) que especifica controles por cada combinacion de nivel de clasificacion (Secreto, Reservado, Uso Interno, Publico, No Clasificada), estado (en transito, producto final) y operacion (transmision, recepcion, procesamiento, almacenamiento).

### Almacenamiento de Informacion

- Informacion SECRETA y RESERVADA fuera de uso, especialmente en horario inhabl: mantenerse en lugar seguro y resguardado, evitando acceso de personas no autorizadas
- Prohibido almacenar informacion SECRETA y RESERVADA en disco duro u otro componente del computador personal sin autorizacion del dueno del activo y un sistema de control de acceso adecuado
- Documentacion escrita con informacion SECRETA y RESERVADA fuera de uso: guardada en lugar seguro protegido con cerradura o llave, solo para personas autorizadas
- Almacenamiento de medios con informacion: acorde a las especificaciones del fabricante

### Proteccion de Registros

Los registros deben protegerse contra perdida, destruccion, falsificacion, acceso no autorizado y publicacion no autorizada, de acuerdo con requisitos legislativos, normativos, contractuales y comerciales.

## Mecanismo de Difusion

- Publicacion en sitio web MINSAL (http://www.minsal.cl/seguridad_de_la_informacion/)
- Publicacion en intranet MINSAL (http://isalud.minsal.cl/)
- Correo informativo

## Periodo de Revision

Revision al menos cada dos anos por el Comite de Seguridad de la Informacion, o ante necesidades de cambios para garantizar idoneidad, adecuacion y efectividad.

## Excepciones

El Comite de Seguridad de la Informacion evaluara y podra establecer condiciones puntuales de excepcion en el cumplimiento de las presentes directrices, siempre que no infrinja la legislacion vigente. Toda excepcion debe ser documentada y generar un proceso de revision de la politica.

## Historial de Versiones

| Version | Fecha | Cambios |
|---|---|---|
| v1.0 | Diciembre 2014 | Creacion del documento |
| v2.0 | Octubre 2020 | Actualizacion del documento |
| v3.0 | (No especificada) | (No especificado) |
| v4.0 | Marzo 2023 | Actualizacion de referencias normativas y controles |

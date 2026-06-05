---
_manifest:
  urn: urn:salud:kb:politica-control-acceso-logico
  provenance:
    created_by: Codex via koraficacion-knowledge
    created_at: '2026-06-05'
    source: MINSAL Chile, SGSI Nivel Central. PS-NC-008 v3.0, Marzo 2023
  minsal_id: PS-NC-008 v3
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
    shard_root_urn: urn:salud:kb:politica-control-acceso-logico
relations:
  cites:
  - urn:salud:kb:politica-general-seguridad-informacion-ciberseguridad
  - urn:salud:kb:politica-seguridad-red
  - urn:salud:kb:politica-identificacion-autenticacion-usuarios
---

# Politica de Seguridad para el Control de Acceso Logico

## Proposito y alcance

Establece las definiciones que regulan el acceso a los medios compartidos de informacion del MINSAL.

Aplica a toda informacion almacenada en carpetas compartidas, bases de datos, sistemas computacionales, servidores y demas medios del MINSAL.

Aplica a: funcionarios (planta, contrata, reemplazos, suplencia), personal a honorarios y terceros (proveedores, compra de servicios) que presten servicios para Subsecretaria de Salud Publica y Subsecretaria de Redes Asistenciales.

**Controles ISO 27002:2013 asociados**:

| ID Control | Control |
| --- | --- |
| A.09.01.01 | Politica de control de acceso |
| A.09.01.02 | Accesos a las redes y a los servicios de la red |
| A.09.02.02 | Asignacion de acceso de usuario |
| A.09.04.01 | Restriccion del acceso a la informacion |
| A.09.04.02 | Procedimientos de inicio de sesion seguro |
| A.09.04.04 | Uso de programas utilitarios privilegiados |
| A.09.04.05 | Control de acceso al codigo fuente de los programas |

## Marco normativo y documentos relacionados

- NCh-ISO27001:2013 — Sistemas de gestion de la seguridad de la informacion — Requisitos
- Ley N°19.628 — Proteccion de vida privada y datos personales
- Ley N°19.799 — Firmas y documentos electronicos
- Ley N°19.927 — Delitos de Pornografia Infantil
- Ley N°20.285 — Transparencia de la funcion publica y acceso a la informacion
- Ley N°21.180 — Transformacion Digital del Estado
- Ley N°21.459 — Delitos Informaticos (deroga Ley N°19.223, adecua al Convenio de Budapest)
- Decreto N°83, 2004 — Norma tecnica sobre seguridad y confidencialidad de documentos electronicos
- Marco Juridico referido a los SSI, publicado en portal CSIRT del Ministerio del Interior

**Documentos relacionados**: Procedimiento gestion derechos de acceso y devolucion de activos, Politica Seguridad de la Red.

## Roles y responsabilidades

**Administrador de Sistemas** — Define accesos a datos por parte de usuarios de la institucion y terceros, asegurando segregacion de funciones adecuada, y gestiona los accesos definidos.

**Jefe Departamento TIC** — Establece controles y reglas de control de acceso para garantizar seguridad y privacidad de la informacion.

**TIC Administracion y Operaciones / Soporte TIC** — Gestiona derechos de acceso a los medios de procesamiento de informacion a su cargo, segun esta politica.

## Materias que aborda

- Politica de control de acceso
- Accesos a las redes y a los servicios de la red

## Directrices

### Cumplimiento de la legislacion

Las medidas de control de acceso a la informacion deben cumplir y ser consistentes con las normas y requerimientos legales definidos en la Normativa del SGSI a traves de la Politica General de Seguridad de la Informacion.

### Accesos a las redes y a los servicios de la red

Los usuarios solo deben tener acceso a la red y servicios de red para los que cuentan con autorizacion especifica. El detalle se encuentra en la Politica de Seguridad de la Red.

### Control de acceso a la informacion

Todos los funcionarios y terceros deben tener acceso solo a la informacion necesaria para el desarrollo legitimo de sus funciones. La asignacion de privilegios y acceso a activos de informacion debe basarse en necesidades de las areas y ser aprobada por el propietario de los activos.

Las necesidades de acceso deben ser determinadas por las jefaturas respectivas, en funcion de las tareas asignadas al cargo.

Para todo medio de procesamiento de informacion al que se necesite conceder accesos (servidores, aplicaciones, carpetas compartidas), el dueno de la Informacion en conjunto con el Departamento TIC debe designar un responsable del medio, quien autoriza los permisos de acceso y solicita los espacios necesarios.

Solo se conceden accesos a terceros previa solicitud del dueno del medio de procesamiento y del dueno de la informacion, y nunca antes de firmar un acuerdo de confidencialidad. Las cuentas de acceso a terceros deben tener un tiempo de expiracion especificado, controlado por el Administrador del sistema.

El Comite de Seguridad de la Informacion del Nivel Central puede suspender o eliminar los accesos a cualquier persona que represente riesgo en confidencialidad, integridad o disponibilidad.

Cualquier intento de acceso no autorizado a equipos, carpetas compartidas, sistemas e informacion es considerado incidente grave y debe reportarse segun el procedimiento de Gestion de Incidentes de Seguridad de la Informacion.

Ante dano a un activo de informacion, se procede segun la Politica General de Seguridad de la Informacion (Sanciones) y el Procedimiento Acuerdos de Confidencialidad en contratos con terceros.

### Administracion del acceso

La administracion de perfiles de usuario en las aplicaciones radica en los usuarios administradores de cada aplicacion y las jefaturas de division correspondiente. La responsabilidad de asignar un perfil a un usuario puede ser delegada por la Jefatura de la Division solicitante o por autorizados.

No se otorga acceso a sistemas hasta completar el proceso de autorizacion y registro segun el Procedimiento de gestion de derechos de acceso y devolucion de activos.

Para facilitar la administracion, se deben definir perfiles de acceso asignables a grupos de usuarios con necesidades de acceso equivalentes segun sus responsabilidades.

El area de Operaciones TIC debe implementar las reglas de control de acceso solicitadas por los Administradores de Aplicacion y las Jefaturas de Division correspondiente.

### Administracion de accesos especiales

Las cuentas de administracion pueden realizar cualquier accion sobre los sistemas administrados y deben gestionarse con maxima precaucion. Deben cumplir, a lo menos:

- Uso exclusivo para labores que requieran permisos de administracion
- Control de acceso basado en doble factor de autenticacion, de ser posible
- Registro de todas las acciones (logs)
- Notificacion del acceso como administrador
- Evitar que privilegios de cuentas de administrador puedan ser heredados
- Claves de acceso lo mas robustas posibles, cambiadas con frecuencia
- Posibilidad de auditorias periodicas
- El otorgamiento de accesos con mayores privilegios (bases de datos, codigo fuente) a funcionarios fuera de Operaciones TIC debe ser solicitado por la Jefatura de Division responsable o quien delegue, al Encargado de Seguridad de la Informacion, con justificacion

### Segregacion de funciones

Los derechos de acceso deben asignarse a perfiles individuales, de forma que las acciones realizadas sean de responsabilidad directa del funcionario.

El otorgamiento de accesos debe considerar segregacion de funciones adecuada, de modo que un mismo funcionario no pueda disponer del control de un proceso de negocios completo.

Excepciones a la regla anterior deben ser aprobadas por la Jefatura de Division correspondiente y autorizadas por el Jefe de Departamento TIC.

### Revision de los derechos de acceso

El area de Operaciones TIC es responsable de los accesos de administradores de aplicaciones, con control efectivo desde el registro inicial de la cuenta hasta su modificacion, revocacion o eliminacion (ver Procedimiento de gestion de derechos de acceso y devolucion de activos).

Los derechos de accesos deben ser revisados:

- A intervalos regulares no mayores a 6 meses
- Despues de cualquier cambio mayor en la organizacion

Los accesos de cuentas con mayores privilegios deben ser revisados al menos 2 veces al ano.

### Revocacion de los accesos logicos

Ante cambio de cargo, se deben revisar los permisos de acceso logico asignados y verificar validez segun nueva funcion.

Al terminar la relacion laboral con MINSAL, todos los permisos de acceso a la informacion deben ser revocados.

Las Jefaturas Directas son responsables de informar formalmente las desvinculaciones segun el procedimiento de gestion de derechos de acceso y devolucion de activos.

### Revocacion de los accesos

Los Usuarios Lideres de aplicacion deben revisar periodicamente los perfiles de usuario del personal vigente y solicitar al area Operaciones TIC la actualizacion cada vez que ocurra un cambio en la definicion de funciones. Cualquier cambio en funciones de una persona que acceda a informacion del negocio debe reflejarse en sus privilegios de acceso.

### Procedimientos de inicio de sesion seguro

El acceso a los sistemas y aplicaciones debe estar controlado por procedimientos de inicio de sesion seguro. El detalle se encuentra en la Politica de Identificacion y autenticacion de usuarios y el Procedimiento para la gestion de identidad y derechos de acceso.

### Uso de programas utilitarios privilegiados

El uso de programas de utilidad capaces de anular el sistema y los controles de aplicacion se debe restringir y controlar integramente.

El detalle se encuentra en el Procedimiento de control de cambios en los medios y sistemas de procesamiento de la informacion.

### Control de acceso al codigo fuente de los programas

Se debe restringir el acceso al codigo fuente de programas. El detalle se encuentra en la Politica de desarrollo de sistemas.

## Mecanismo de difusion

- Publicacion en intranet MINSAL http://isalud.minsal.cl/
- Correo informativo

## Periodo de revision

Revision a lo menos cada dos anos por el Comite de Seguridad de la Informacion, o segun necesidades de cambio para garantizar idoneidad, adecuacion y efectividad.

## Excepciones

En casos especiales, el Comite de Seguridad de la Informacion evaluara y podra establecer condiciones puntuales de excepcion, siempre que no infrinja la legislacion vigente. Toda excepcion debe documentarse y dar lugar a un proceso de revision que determinara si se deben agregar directrices especificas.

## Historial de versiones

| Version | Fecha | Cambios |
| --- | --- | --- |
| 1 | Octubre 2011 | Creacion del documento |
| 2 | Octubre 2019 | Cambio de formato, actualizacion referencias normativas, actualizacion dominios ISO 27001 |
| 3 | Marzo 2023 | Inclusion de requisitos para cuentas de administracion. Inclusion de controles A.09.02.02, A.09.04.01, A.09.04.02, A.09.04.04, A.09.04.05 |

## Referencias

- [1] Procedimiento gestion derechos de acceso y devolucion de activos — http://isalud.minsal.cl/ministerio/dgstic/SGSI/Paginas/default.aspx
- [2] Politica de Seguridad de la Red — http://isalud.minsal.cl/ministerio/dgstic/SGSI/Paginas/default.aspx
- [3] Politica General de Seguridad de la Informacion — https://www.minsal.cl/seguridad_de_la_informacion/

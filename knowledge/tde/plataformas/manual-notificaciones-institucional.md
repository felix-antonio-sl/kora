---
_manifest:
  urn: "urn:tde:kb:manual-notificaciones-institucional"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/instituciones-plataforma-de-notificaciones"
version: 1.0.0
status: published
tags: [tde, plataforma, notificaciones, casilla-unica, institucional, ddu, oae]
lang: es
---

# Manual usuario institucional — Plataforma de Notificaciones del Estado (CasillaUnica)

## Descripcion general

Plataforma para que OAE remitan notificaciones electronicas de procedimientos administrativos al Domicilio Digital Unico (DDU) de personas naturales y juridicas.

### Tres ambientes

| Ambiente | Funcion |
|---|---|
| **Ciudadanos** | Configurar DDU, acceder a mensajes enviados por instituciones |
| **Instituciones** | Enviar notificaciones electronicas, gestionar usuarios |
| **API** | Envio automatico desde sistemas internos del OAE via API |

URL ambiente institucional: `https://institucion.casillaunica.gob.cl/`

Autenticacion: ClaveUnica obligatoria. Usuario debe tener rol asignado.

### Timeout de sesion

- 10 min inactividad → modal de advertencia
- 2 min adicionales sin respuesta → cierre automatico de sesion

## Roles y permisos

| Modulo | Adm. Instituciones | Adm. Mensajes |
|---|---|---|
| Configuracion (logo y firma) | Si | No |
| Inicio | Si | Si |
| Crear mensajes | No | Si |
| Mensajes enviados | No | Si |
| Borradores | No | Si |
| Solicitud de excepcion | Si | No |
| Plantillas | Si | Si |
| Administracion / Usuarios | Si | No |
| Administracion / Procedimientos administrativos | Si | No |
| Estadisticas / Mensajes agrupados | Si | Si |
| Estadisticas / Mensajes a destinatarios | Si | Si |
| Estadisticas / Consulta de mensajes | Si | Si |

- **Administrador de Instituciones**: configura y visualiza informacion de la institucion. Cada institucion requiere al menos uno.
- **Administrador de Mensajes**: envia mensajes. Cada institucion puede tener multiples.

## Modulos del ambiente institucional

### Configuracion

Acceso: solo Adm. Instituciones (cabecera).

- **Logo**: imagen que identifica la institucion en todos los mensajes. Formatos: PNG, JPG.
- **Firma**: texto al pie de mensajes. Una institucion puede tener multiples firmas; se selecciona una al enviar.

Ambas configuraciones deben crearse **previo al envio de mensajes**.

### Inicio

Pagina por defecto al ingresar. Varia segun perfil:

| Perfil | Accesos directos |
|---|---|
| Adm. Instituciones | Administracion de usuarios, estadisticas, T&C |
| Adm. Mensajes | Crear mensajes, consultar mensajes, consulta configuracion DDU, T&C |

**Consulta de configuracion DDU** (disponible para Adm. Mensajes): consultar estado DDU de un RUN. Valores posibles: No configurado, Excepcionado, Casilla.

### Crear mensajes

Envio de mensajes usando RUN/RUT del destinatario. Dos modalidades:

| Tipo | Descripcion |
|---|---|
| **Mensaje simple** | Mismo contenido y adjuntos a todos los destinatarios |
| **Mensaje multiple** | Mismo contenido, diferentes adjuntos por grupo de destinatarios |

Reglas de envio:

- Un envio puede tener uno o varios destinatarios (identificados por RUT/RUN)
- Puede combinar personas naturales y juridicas
- Ingreso de destinatarios: manual o via archivo .csv
- Limite adjuntos por archivo: 20 MB
- Limite total adjuntos: 20 MB
- Formatos soportados: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX
- PDF con firma electronica: validados automaticamente
- Tipo por defecto: Notificaciones (asociadas a procedimiento administrativo)

### Mensajes enviados

Listado descendente por fecha/hora de envio (web + API).

Funcionalidades: cambiar orden, busqueda, paginacion, acceso a detalle, descarga de comprobante/certificado de envio.

Informacion por mensaje: fecha, hora, asunto, estado de envio, tipo, cantidad destinatarios, adjuntos, medio (WEB o API).

### Borradores

Bandeja de mensajes iniciados pero no enviados. Ordenados por fecha/hora (mas recientes primero).

Funcionalidades: cambiar orden, busqueda, paginacion, crear mensaje desde borrador.

### Solicitud de excepcion

Solo Adm. Instituciones. Permite inhabilitar un RUN para recepcion de notificaciones electronicas, previa solicitud del ciudadano.

Base legal: Titulo V del Reglamento de la Ley N 21.180 de Transformacion Digital del Estado.

Formulario requiere: datos del solicitante, motivos de excepcion, documento justificativo.

Si se necesita notificar a persona excepcionada → la institucion debe habilitar otro mecanismo de comunicacion.

### Plantillas

Acceso: Adm. Instituciones y Adm. Mensajes (segun permisos).

Operaciones: crear, editar, eliminar, duplicar, previsualizar.

Filtros: rango de fechas (Fecha Desde / Fecha Hasta), autor/editor.

### Administracion

#### Usuarios

Solo Adm. Instituciones. Crear, modificar y eliminar usuarios con rol de administrador de mensajes dentro de la institucion.

#### Procedimiento administrativo

Seleccionar PA a notificar desde el listado cargado en CPAT (Catalogo de Procedimientos Administrativos y Tramitaciones).

### Estadisticas

#### Mensajes agrupados

Cantidad de mensajes enviados por la institucion en periodo determinado. Filtros: rango de fecha, tipo de mensaje, estado de envio.

#### Mensajes a destinatarios

Detalle de mensajes enviados a destinatarios en periodo. Filtros: rango de fecha, tipo de mensaje, estado, id de envio. Tipificacion por: configuracion DDU, estado mensajes, tipo mensaje, tipo ciudadano. Informa lectura (solo DDU tipo casilla).

#### Consulta de mensajes

Detalle de mensajes recibidos por ciudadano especifico. Busqueda por RUT/RUN.

## Elementos de interfaz

| Zona | Contenido |
|---|---|
| Cabecera | Logo producto, nombre institucion, boton cerrar sesion |
| Barra lateral | Menu segun permisos del usuario, identificacion usuario conectado |
| Zona de contenido | Pagina de inicio por defecto; ruta de navegacion en esquina superior izquierda |
| Pie de pagina | Horarios mesa de servicios, enlace a sitio web mesa de servicios |

Mesa de servicios: accesible desde pie de pagina para levantar tickets y consultas.

## Glosario

| Termino | Definicion |
|---|---|
| DDU (Domicilio Digital Unico) | Medio electronico para recibir notificaciones electronicas del Estado, centralizado |
| Expediente electronico | Registro electronico de documentos, datos, vinculos y metadatos de actuaciones y resoluciones de un PA; ID alfanumerico |
| Firma | Texto que identifica la institucion al pie del mensaje; configurable por administradores |
| Instituciones | Organos de la Administracion del Estado (ministerios, secretarias, servicios, gobernaciones, municipalidades, etc.) |
| Logo | Imagen que identifica la institucion en el encabezado del mensaje; configurable por administradores |
| Mensaje | Comunicaciones desde OAE: institucionales, personales, o notificaciones de actos administrativos resolutivos |
| Notificacion | Comunicacion formal de una resolucion administrativa a un destinatario |
| OAE | Organos de la Administracion del Estado |
| Persona Juridica | Entidad juridica que consulta mensajes y notificaciones oficiales en la plataforma |
| Persona Natural | Persona que configura DDU, consulta mensajes y notificaciones oficiales |
| Plataforma de Notificaciones | Canal oficial para envio de notificaciones electronicas de OAE al DDU de personas |
| Procedimiento administrativo | Sucesion de actos tramite vinculados para producir un acto administrativo terminal |
| Usuario Persona | Personas naturales, juridicas, entes y agrupaciones sin personalidad juridica que actuan como interesados en PA |
| Usuario Institucional | Funcionarios de OAE que interactuan con la plataforma segun roles definidos |

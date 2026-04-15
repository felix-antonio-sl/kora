---
_manifest:
  urn: urn:tde:kb:manual-usuario-institucional-notificaciones
  provenance: https://wikiguias.digital.gob.cl/Manuales/instituciones-plataforma-de-notificaciones
version: 1.0.0
status: published
tags:
- tde
- plataformas-manuales
- notificaciones
- casilla-única
- instituciones
- oae
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:tde:kb:manual-usuario-institucional-notificaciones
---

# Manual de usuario institucional: Plataforma de Notificaciones del Estado (CasillaÚnica)

## Descripción general

La plataforma tiene tres ambientes:

| Ambiente | Función |
|----------|---------|
| Ciudadanos | Acceso y configuración del Domicilio Digital Único (DDU) |
| Instituciones | Envío de notificaciones electrónicas y gestión de usuarios |
| API | Envío automático de mensajes desde sistemas internos del OAE |

Todas las acciones del funcionario dentro de la plataforma quedan almacenadas para eventuales auditorías.

URL ambiente institucional: **https://institucion.casillaunica.gob.cl/**

Autenticación: **ClaveÚnica** (el usuario debe tener rol asignado previamente).

Sesión: inactividad de 10 minutos → aviso modal; 2 minutos adicionales sin respuesta → cierre automático.

## Roles y permisos

| Módulo/Sección | Adm. Instituciones | Adm. de Mensajes |
|----------------|-------------------|-----------------|
| Configuración (logo y firma) | Sí | No |
| Inicio | Sí | Sí |
| Crear mensajes | No | Sí |
| Mensajes enviados | No | Sí |
| Borradores | No | Sí |
| Solicitud de excepción | Sí | No |
| Plantillas | Sí | Sí |
| Administración — Usuarios | Sí | No |
| Administración — Procedimientos administrativos | Sí | No |
| Estadísticas — Mensajes agrupados | Sí | Sí |
| Estadísticas — Mensajes a destinatarios | Sí | Sí |
| Estadísticas — Consulta de mensajes | Sí | Sí |

Cada institución debe tener **al menos un Administrador de Instituciones**. Puede tener más de un Administrador de Mensajes.

## Módulos

### Configuración
- Solo accesible para Administrador de Instituciones; disponible en cabecera.
- **Logo:** imagen que identifica a la institución en todos los mensajes; formatos aceptados: PNG, JPG.
- **Firma:** texto de pie de firma; una institución puede tener más de una firma; debe elegirse al enviar cada mensaje.
- Ambas configuraciones deben crearse **antes del primer envío**.

### Inicio
- Muestra accesos directos según perfil:
 - **Adm. Instituciones:** administración de usuarios, estadísticas, términos y condiciones.
 - **Adm. de Mensajes:** crear mensajes, consultar mensajes, consulta DDU, términos y condiciones.
- **Consulta DDU:** permite verificar la configuración de un RUN (valores posibles: No configurado / Excepcionado / Casilla).

### Crear mensajes
Requisitos y restricciones:

| Campo/Parámetro | Detalle |
|-----------------|---------|
| Identificación de destinatarios | RUT/RUN (personas naturales y jurídicas, combinables) |
| Ingreso de destinatarios | Manual o archivo .csv |
| Tamaño máximo por adjunto | 20 MB |
| Tamaño total adjuntos | 20 MB |
| Formatos adjuntos soportados | PDF, JPG, PNG, DOC, DOCX, XLS, XLSX (PDF con firma electrónica validado) |
| Tipo de mensaje por defecto | Notificación (asociada a procedimiento administrativo) |

Tipos de envío:
- **Mensaje simple:** mismo contenido y adjuntos para el mismo grupo de destinatarios.
- **Mensaje múltiple:** mismo contenido con adjuntos diferentes para distintos grupos de destinatarios.

### Mensajes enviados
- Listado descendente por fecha/hora; incluye envíos web y API.
- Operaciones disponibles: ordenar asc/desc, buscar, navegar páginas, ver detalle, descargar comprobante/certificado de envío.
- Datos visibles por mensaje: fecha, hora, asunto, estado, tipo, cantidad de destinatarios, adjuntos, medio (WEB/API).

### Borradores
- Mensajes iniciados y no enviados.
- Operaciones: ordenar, buscar, navegar páginas, retomar edición y enviar.

### Solicitud de excepción
- Permite inhabilitar el RUN de un ciudadano que solicita no recibir notificaciones electrónicas (conforme Título V Reglamento Ley N° 21.180).
- Requiere formulario con datos del solicitante, motivo de excepción y documento justificante.
- Si el destinatario está excepcionado, la institución debe habilitar otro mecanismo de comunicación.

### Plantillas
- Operaciones disponibles: crear, editar, eliminar, duplicar, previsualizar.
- Filtros: autor/editor, rango de fecha (Fecha Desde / Fecha Hasta).
- Permisos de operación dependen del rol (Adm. Instituciones o Adm. Mensajes).

### Administración

**Usuarios:** el Administrador de Instituciones crea, modifica y elimina usuarios con rol Administrador de Mensajes dentro de su institución.

**Procedimiento administrativo:** selecciona, desde los procedimientos cargados en CPAT (Catálogo de Procedimientos Administrativos y Tramitaciones), los PA que la institución notificará.

### Estadísticas

| Sub-módulo | Función | Filtros disponibles |
|------------|---------|-------------------|
| Mensajes agrupados | Cantidad de mensajes enviados por periodo | Rango de fecha, tipo de mensaje, estado de envío |
| Mensajes a destinatarios | Detalle de envíos por destinatario | Rango de fecha, tipo de mensaje, estado, ID de envío |
| Consulta de mensajes | Detalle de mensajes recibidos por un ciudadano | Búsqueda por RUT/RUN |

Mensajes a destinatarios incluye: tipificación por configuración DDU, estado del mensaje en DDU-casilla, tipo de ciudadano, indicador de lectura (solo si DDU = casilla).

## Soporte

Ticket a mesa de servicios: disponible en el pie de página de la aplicación. Horarios de atención indicados en el mismo footer.

## Glosario

| Término | Definición |
|---------|-----------|
| DDU (Domicilio Digital Único) | Medio electrónico designado por la persona para recibir notificaciones electrónicas del Estado de forma centralizada |
| Expediente electrónico | Registro electrónico de documentos, datos y metadatos asociados a un procedimiento administrativo; identificado por código alfanumérico |
| Firma | Texto de pie de firma que identifica a la institución; configurado por el Adm. de Instituciones |
| Logo | Imagen institucional incluida en el encabezado de cada mensaje; configurada por el Adm. de Instituciones |
| Mensaje | Comunicación desde un OAE al ciudadano: comunicación institucional, personal o notificación de acto administrativo resolutivo |
| Notificación | Comunicación formal de una resolución administrativa a un destinatario |
| OAE | Órganos de la Administración del Estado |
| Procedimiento administrativo | Sucesión de actos trámites que produce un acto administrativo terminal |
| Usuario Institucional | Funcionario de un OAE con rol funcional en la plataforma |
| Usuario Persona | Persona natural, jurídica o agrupación que actúa como interesado, apoderado o funcionario en procedimientos administrativos |

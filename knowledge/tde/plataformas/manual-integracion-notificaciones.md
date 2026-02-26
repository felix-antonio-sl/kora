---
_manifest:
  urn: "urn:tde:kb:manual-integracion-notificaciones"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/integracion-casillaunica"
version: 1.0.0
status: published
tags: [tde, plataforma, notificaciones, casilla-unica, integracion, api, pisee, oae]
lang: es
---

# Manual de integracion — Plataforma de Notificaciones del Estado

Guia tecnica, operativa y administrativa para integracion de OAE a la plataforma de notificaciones. Base normativa: Norma Tecnica de Notificaciones Electronicas (https://www.bcn.cl/leychile/navegar?idNorma=1195121).

## Consideraciones marcha blanca (2025)

- No contempla cambio de configuracion DDU a correo electronico
- No incluye flujo de envio a representantes de personas juridicas
- Limite adjuntos: 20 MB (un archivo o varios)

## Definiciones

| Termino | Definicion |
|---|---|
| API de notificaciones | Servicio web para integracion automatica de envio de notificaciones |
| Bandeja de mensajes CasillaUnica | Bandeja con todas las notificaciones de PA cuando DDU = Casilla |
| CasillaUnica | Componente de la plataforma configurable como DDU; acceso centralizado a notificaciones |
| DDU (Domicilio Digital Unico) | Medio electronico elegido por usuario para recibir notificaciones. Opciones: Casilla o correo electronico |
| Notificacion electronica | Acto de comunicar formalmente una resolucion via plataforma electronica |
| Procedimiento administrativo | Sucesion de actos tramite vinculados para producir acto administrativo terminal |
| Aviso de notificacion | Correo electronico que informa al ciudadano sobre nueva notificacion (cuando DDU = Casilla) |
| Usuario | Personas naturales/juridicas, apoderados, representantes, funcionarios que acceden a plataformas de PA |

## Quienes deben integrarse

Todos los OAE: ministerios, secretarias, servicios, gobernaciones, municipalidades. Obligacion: practicar notificaciones por medios electronicos segun art. 46 Ley N 19.880.

## Proceso de integracion

### Prerequisitos

1. Coordinador/a de Transformacion Digital oficialmente designado/a
2. Funcionarios con ClaveUnica activa
3. PA seleccionados y cargados en CPAT
4. Equipo de contacto institucional: contacto tecnico + contacto de negocio + administrador institucional
5. Definir medio de envio: via web, via API, o ambos

### Flujo de integracion (paso a paso)

1. **Solicitud**: ingresar "Solicitud de integracion a la Plataforma de Notificaciones" en CeroFilas (https://gobdigital.cerofilas.gob.cl/)
2. **Evaluacion SGD**: verifica datos completos, correos institucionales, institucion no previamente integrada
   - Aceptada → habilita en ambiente pruebas + envia correo con informacion de acceso
   - Rechazada → institucion debe presentar nueva solicitud
3. **Actividades en ambiente de pruebas**:
   - Configurar institucion: logo, firma, procedimiento administrativo
   - Crear administrador de mensajes
   - Enviar mensaje via web y/o API (nodo PISEE)
4. **Solicitud de certificacion**: continuar flujo en CeroFilas
5. **Certificacion SGD**: evalua actividades del ambiente de pruebas
   - Con observaciones → corregir y nueva solicitud
   - Aprobada → correo con datos para produccion
6. **Habilitacion en produccion**: institucion lista para enviar notificaciones

### Formulario de solicitud (datos requeridos)

- Institucion solicitante
- Datos de contacto administrativo
- Datos del administrador institucional
- Tipo de integracion: Manual / Via API / Ambas
- Datos de contacto tecnico (si API o ambas)
- Para API: nombre y descripcion de aplicacion, URL (opcional)
- Aceptacion de terminos y condiciones

### Configuracion en ambiente de pruebas

| Elemento | Requisitos |
|---|---|
| Logo | Obligatorio. Dimensiones optimas: 80-350 px ancho x 80 px alto. Formato: PNG o JPG. Max 5 MB |
| Firma | Opcional (recomendado). Solo texto, sin imagenes. Opcion: Configuracion/crear o editar firma |
| Procedimientos administrativos | Seleccionar desde listado CPAT. Opcion: Administracion/Procedimientos administrativos |
| Administrador de mensajes | Crear usuario con rol. Opcion: Administracion/Usuarios |

### Envio de prueba (recomendaciones)

- Usuarios de prueba: RUN 33333333-3 (DDU casilla), RUN 33333351-1 (DDU excepcionado)
- Contenido respetuoso, simulando notificacion real
- Adjuntos de prueba sin informacion sensible
- Incluir firma institucional
- URL CasillaUnica pruebas: `https://portal.demo.casillaunica.gob.cl/casilla/`
- Credenciales pruebas: RUN 33333333-3, clave: testing

### Habilitacion en produccion

SGD realiza:
- Registra institucion
- Registra administrador institucional
- Crea credenciales API (si aplica)

Institucion debe:
- Configurar logo, firmas, PA
- Crear administrador de mensajes
- Solicitar nodo PISEE via mesa de servicios (opcional, si integracion API)

## Envio de notificacion via web

Precondicion: habilitacion en produccion completada.

### Tipos de mensaje

| Tipo | Descripcion |
|---|---|
| Mensaje simple | Un mensaje a uno o mas destinatarios, mismo contenido y adjuntos |
| Mensaje multiple | Un mensaje a distintos grupos de destinatarios, adjuntos individualizados por grupo |

### Adjuntos

- Limite por archivo: 20 MB
- Limite total: 20 MB
- Formatos soportados: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX
- PDF con firma electronica: validacion automatica (firma valida, documento no adulterado)

### Estados de envio

| Estado | Descripcion |
|---|---|
| Enviado | Mensaje enviado correctamente |
| En proceso | Mensaje en proceso de envio |
| Con error | Problemas en el envio |

## Envio de notificacion via API

Requiere: nodo PISEE 2 configurado + `client_id` + `client_secret` de la institucion.

### Endpoint: enviar mensaje

```
POST /notificador/sendMessage
Content-Type: multipart/form-data
```

**Parte `data`** (JSON):

| Campo | Tipo | Obligatorio | Descripcion |
|---|---|---|---|
| recipients | Array | Si | Lista de destinatarios `[{"rol_unico": 11111111}]`. Max 250 |
| message_type | String | Si | NT (Notificacion), CP (Comunicacion Personal), CI (Comunicado Institucional) |
| procedure_code | String | Si (si NT) | Codigo del PA |
| procedure_stage | Numero | Si (si NT) | 1=Inicio, 2=Instruccion, 3=Finalizacion |
| signature_uid | UUID | No | UUID de firma institucional |
| subject | String | Si | Asunto. Max 150 caracteres |
| content | String | Si | Contenido de la notificacion |
| content_type | String | Si | Tipo MIME, ej: "text/html" |
| webhook_url | URL | No | URL para callback de estado de procesamiento. null o vacio si no se usa |

**Parte `attachments`**: archivos binarios opcionales. Multiples campos permitidos. Mismas restricciones que envio web (20 MB total, formatos soportados).

**Respuesta exitosa** (HTTP 200):

```json
{
  "message_data_id": "630c7a94ee5a2dbd341d23ff7",
  "sent_at": "Mon, 14 Jun 2023 15:09:03 GMT",
  "status": "pending"
}
```

### Codigos de error API

| Codigo | Descripcion |
|---|---|
| ERR001 | Sin destinatarios |
| ERR002 | Elementos no esperados en recipients |
| ERR003 | rol_unico no valido (entero positivo, max 99.999.999) |
| ERR004 | message_type no ingresado |
| ERR005 | message_type no permitido o institucion no habilitada para ese tipo |
| ERR006 | procedure_code no ingresado (requerido si NT) |
| ERR007 | procedure_code no valido o no habilitado para la institucion |
| ERR008 | Logo no configurado en la plataforma |
| ERR013 | Formato de archivo no permitido |
| ERR014 | Nombre de archivo excede 50 caracteres |
| ERR015 | Total adjuntos excede 20 MB |
| ERR016 | Archivo duplicado |
| ERR017 | Base64 con formato incorrecto |
| ERR018 | Extension no corresponde al tipo de documento |
| ERR019 | Archivo individual excede 20 MB |
| ERR020 | Firma pertenece a otra institucion |
| ERR021 | Archivo adulterado, modificado post-firma o firma(s) revocada(s) |
| ERR023 | RUN no valido |
| ERR026 | Asunto excede 150 caracteres |
| ERR027 | Asunto no ingresado |
| ERR028 | URL en contenido no valida |
| ERR030 | Excede 250 destinatarios |
| ERR031 | Envio duplicado (esperar 5 min) |
| ERR032 | Excede 50 archivos adjuntos |
| ERR033 | Nombre de archivo con caracteres no permitidos (solo letras sin acento, numeros, guiones, espacios) |
| ERR034 | webhook_url no valida |

### Endpoint: estado de notificacion

```
GET /notificador/messageStatus/{message_data_id}
```

**Respuesta**: JSON con message_data_id, entity_id, received_at, status, subject, recipients_count, recipients (objeto con rol_unico como llave).

Campos por destinatario:
- `ddu_type`: casilla, email, not_configured, excepcion
- `message_status`: delivered, error, pending
- `method`: WEB o API
- `delivered_at`: fecha envio
- `read_at`: fecha lectura (null si no leido)

### Estados de mensaje

| Estado | Descripcion |
|---|---|
| pending | Estado inicial al crear envio |
| delivered | Envio finalizado correctamente |
| error | Fallo al crear/actualizar envio |
| error_rejected | Mensaje sospechoso o no valido |
| error_permanent_general | Rechazo permanente general |
| error_permanent_no_email | Direccion de correo destino no existe |
| error_permanent_supressed | Historial reciente de rebotes |
| error_permanent_on_account_suspension_list | Correo en lista de rebotes previos |
| error_transient_general | Rebote general (reintentable) |
| error_transient_mailbox_full | Bandeja del destinatario llena |
| error_transient_message_too_large | Mensaje demasiado grande |
| error_transient_content_rejected | Contenido rechazado |
| error_transient_attachment_rejected | Adjunto rechazado |
| error_send_message_mail | No se pudo comunicar con servidor de correo |

### Estado segun configuracion DDU

| DDU destinatario | Estado inicial | Estado final |
|---|---|---|
| No configurada | delivered | delivered o error |
| Excepcionada | delivered | delivered o error |
| Casilla | delivered | delivered o error |
| Correo electronico | pending | delivered o error |

### Endpoint: mensajes pendientes de ciudadano

```
GET /notificador/citizenPending/{rol-unico}
```

Respuesta: access_url, current_ddu_type, result_message, status, total_pending.

### Endpoint: procedimientos administrativos

```
GET /notificador/getProcedure
```

Respuesta: lista de procedures con name, code, stage, stage_name.

### Endpoint: firmas institucionales

```
GET /notificador/getSignature
```

Respuesta: lista de signatures con name, uid, body, updated_at.

### Endpoint: comprobante de mensaje

```
GET /notificador/getReceipt/{message_data_id}/{rol_unico}
```

Respuesta: url para descarga del comprobante PDF.

Errores: ERR022 (codigo mensaje no valido), ERR023 (RUN no valido), ERR024 (mensaje no corresponde al destinatario), ERR025 (mensaje no enviado correctamente).

### Nivel de transacciones API

Disponibilidad: 24x7. Maximo: 6 TPS.

## Registro de excepcion

Administrador institucional registra excepcion para ciudadano exento de notificaciones electronicas.

Base legal: Cap. III, parrafo 1, art. 46 Ley 19.880; Norma Tecnica de Notificaciones art. 8; Reglamento arts. 28-29.

Campos del formulario: RUN, correo electronico, telefono, direccion, ID expediente electronico (opcional), fecha solicitud, motivo (lista predefinida), otros motivos (texto libre), archivos de respaldo.

## Certificado de envio

Disponible por plataforma web y API. Certifica envio de mensaje a destinatario con fecha, hora y datos. Certificados descargados son validables por cualquier persona.

## Mesa de servicios

- Formulario: https://gobdigitalcl.freshdesk.com/support/home
- Sugerencias: correo del producto

## Configuracion nodo PISEE 2

### Credenciales

En archivo config.json del nodo PISEE, dentro de `identificacion.custom`:
- `id`: client_id de la institucion
- `secret`: client_secret de la institucion

### Endpoints

En arreglo `consumidor` del config.json, listar cada servicio de la API de Notificaciones a consumir.

## Ejemplos cURL

```bash
# Enviar notificacion
curl --location '{url}/notificador/sendMessage' \
  --form 'data="{ \"recipients\": [{\"rol_unico\": 26093912}], \"message_type\": \"NT\", \"procedure_code\": \"PA-SUP00604-00007\", \"procedure_stage\": 1, \"subject\": \"Asunto\", \"content\": \"Contenido\", \"content_type\": \"text/html\" }"'

# Estado de envio
curl --location '{url}/notificador/messageStatus/{message_data_id}'

# Mensajes pendientes
curl --location '{url}/notificador/citizenPending/{rol_unico}'

# Procedimientos administrativos
curl --location '{url}/notificador/getProcedure'

# Firmas institucionales
curl --location '{url}/notificador/getSignature'

# Comprobante de mensaje
curl --location '{url}/notificador/getReceipt/{message_data_id}/{rol_unico}'
```

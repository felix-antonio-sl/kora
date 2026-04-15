---
_manifest:
  urn: urn:tde:kb:manual-integracion-notificaciones
  provenance: https://wikiguias.digital.gob.cl/Manuales/integracion-casillaunica
version: 1.0.0
status: published
tags:
- tde
- plataformas-manuales
- notificaciones
- casilla-unica
- manuales
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:tde:kb:manual-integracion-notificaciones
---

# Manual de Integración — Plataforma de Notificaciones del Estado


Define las consideraciones técnicas, operativas y administrativas para el uso de la plataforma de notificaciones, conforme a la [Norma Técnica de Notificaciones Electrónicas](https://www.bcn.cl/leychile/navegar?idNorma=1195121).

## Definiciones

| Término | Definición |
|---------|------------|
| **API de notificaciones** | Servicio web que permite a los OAE integrar sus plataformas para gestionar el envío de notificaciones de manera automática. |
| **Bandeja de mensajes de CasillaÚnica** | Cuando el DDU se configura como "Casilla", reúne todas las notificaciones de los procedimientos administrativos del interesado, ordenadas por fecha y OAE emisor. |
| **CasillaÚnica** | Componente de la Plataforma de Notificaciones configurable como DDU; permite acceder y visualizar notificaciones recibidas de los OAE. |
| **DDU (Domicilio Digital Único)** | Medio electrónico elegido por el usuario para recibir notificaciones electrónicas. Opciones: Casilla o correo electrónico validado. |
| **Notificación electrónica** | Mensaje enviado a través de la plataforma electrónica de notificaciones sobre procedimientos administrativos de los OAE, en base a un registro único. |
| **Procedimiento administrativo** | Sucesión de actos trámite vinculados entre sí, emanados de la Administración y/o de particulares interesados, con el fin de producir un acto administrativo terminal. |
| **Aviso de notificación** | Correo electrónico configurado por el ciudadano (cuando su DDU es la Casilla) que le informa cuando recibe una notificación. |

## Consideraciones de la versión en marcha blanca (2025)

- No contempla cambio de configuración de DDU a correo electrónico.
- No incluye flujo de envío a representantes de personas jurídicas.
- Límite de adjuntos: 20 MB (un archivo o varios en conjunto).

## Proceso de integración

### Requisitos previos

Antes de solicitar la integración, la institución debe:

1. Contar con Coordinador/a de Transformación Digital oficialmente designado/a.
2. Asegurar que los funcionarios que utilizarán la plataforma tengan ClaveÚnica activa.
3. Seleccionar los procedimientos administrativos a notificar; deben estar cargados en el CPAT (https://cpat.gob.cl/).
4. Designar el equipo de contacto institucional: contacto técnico, contacto de negocio y administrador institucional.
5. Definir el medio de envío: vía web, vía API o ambas.

### Pasos de integración

1. Ingresar "Solicitud de integración a la Plataforma de Notificaciones" en [CeroFilas](https://gobdigital.cerofilas.gob.cl/).

 Datos requeridos en el formulario:
 - Institución solicitante
 - Datos de contacto administrativo
 - Datos del administrador institucional
 - Tipo de integración: Manual / Vía API / Ambas
 - Datos de contacto técnico (si API o ambas)
 - Para integración vía API: nombre y descripción de la aplicación; URL (opcional)
 - Aceptar términos y condiciones de uso.

2. La SGD evalúa la solicitud verificando:
 - Datos completos.
 - Correos institucionales.
 - Institución no integrada previamente.

 Si hay inconsistencias: se rechaza con observaciones; la institución debe presentar nueva solicitud corregida.

 Si es aceptada: la SGD habilita en ambiente de pruebas y envía correo con información de acceso.

3. Realizar actividades en ambiente de pruebas (ver sección siguiente).

4. Ingresar "Solicitud de certificación" en CeroFilas.

5. La SGD evalúa la certificación:
 - Si hay observaciones: la institución corrige y presenta nueva solicitud.
 - Si es aprobada: se envía correo con información para configuración en producción.

6. Habilitación en producción: la institución puede enviar notificaciones electrónicas.

### Actividades en ambiente de pruebas

El administrador institucional accede con ClaveÚnica y realiza:

**a) Configurar la institución**

- **Logo:** Ingresar en Configuración/Carga de Logotipo. Requisitos: dimensiones 80–350 px ancho × 80 px alto; formato PNG o JPG; tamaño máximo 5 MB. Obligatorio para enviar notificaciones.
- **Firma institucional:** Ingresar en Configuración/Crear o editar firma. Solo admite texto (sin imágenes). Opcional pero recomendable.
- **Procedimientos administrativos:** Ingresar en Administración/Procedimientos administrativos → botón "Agregar procedimientos". Seleccionar de la lista de procedimientos cargados en CPAT.

**b) Crear administrador de mensajes**

Ir a Administración/Usuarios. Crear usuarios con rol de administrador de mensajes (necesario si la institución opera vía web o necesita ver mensajes enviados desde la API).

**c) Enviar mensaje de prueba**

- **Vía web:** acceder a "Crear mensaje" como administrador de mensajes.
- **Vía API:** usar el nodo PISEE (ver sección API).

Usuarios de prueba disponibles:
- RUN `33333333-3` — DDU configurado como casilla.
- RUN `33333351-1` — DDU Excepcionado.

Para ver cómo recibe el ciudadano el mensaje en ambiente de pruebas:
- URL: https://portal.demo.casillaunica.gob.cl/casilla/
- Autenticación: RUN `33333333-3`, clave `testing` (único usuario con acceso a CasillaÚnica de pruebas).

Recomendaciones para el contenido del mensaje de prueba:
- Contenido respetuoso que simule una notificación real.
- Archivos adjuntos de prueba; evitar información sensible.
- Incluir la firma institucional creada.

## Habilitación en producción

La SGD realiza en producción:
- Registra la institución.
- Registra al administrador institucional indicado en el formulario.
- Crea credenciales API en producción (si la integración es vía API o ambas).

La institución debe:
1. Configurar institución: logo, firma(s) y procedimientos administrativos.
2. Crear administrador de mensajes.
3. Solicitar nodo PISEE en producción a través de la [Mesa de Servicios](https://gobdigitalcl.freshdesk.com/support/home) (si corresponde).
4. Integrarse vía API a través del nodo PISEE (opcional).

## Envío de notificaciones — Interfaz web

### Precondición

Completar todas las actividades de la sección "Habilitación en producción".

### Tipos de mensaje

| Tipo | Descripción |
|------|-------------|
| **Mensaje Simple** | Un solo mensaje a uno o más destinatarios; todos reciben el mismo contenido y adjuntos. |
| **Mensaje Múltiple** | Envío para distintos grupos de destinatarios; por cada grupo se individualizan destinatarios y adjuntos. |

### Pasos para enviar un mensaje

1. Ir a "Crear mensaje" en el menú del administrador de mensajes.
2. Seleccionar el tipo de mensaje (Simple o Múltiple).
3. Seleccionar el Procedimiento Administrativo de la lista habilitada.
4. Agregar destinatarios: de forma manual o por archivo `.csv`.
5. Redactar: asunto, cuerpo del mensaje, archivos adjuntos y firma institucional (opcional).
6. Enviar.

> Si no encuentra el procedimiento administrativo en la lista, reportarlo al administrador institucional para que lo agregue a la plataforma.

### Adjuntos en una notificación

- Peso máximo: 20 MB (total, un archivo o varios en conjunto).
- Extensiones permitidas: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX.
- Los PDF con firma electrónica son validados; la firma debe ser válida y el documento no adulterado.

### Estados de envío

| Estado | Descripción |
|--------|-------------|
| **Enviado** | Mensaje enviado correctamente. |
| **En proceso** | Mensaje en proceso de envío. |
| **Con error** | La plataforma tuvo problemas para realizar el envío. |

Ver en "Mensajes enviados" en el menú.

## Requisito

Tener configurado un nodo de interoperabilidad PISEE 2 y un `client_id` y `client_secret` asociados a la institución.

## Endpoint: Enviar notificación

```
URL: /notificador/sendMessage
Método: POST
Tipo: multipart/form-data
```

**Parte `data` (JSON obligatorio):**

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| `recipients` | Arreglo | Sí | Lista de destinatarios. Cada objeto con `rol_unico` (RUN o RUT sin dígito verificador). Máximo 250. Ejemplo: `[{"rol_unico": 11111111}]` |
| `message_type` | Cadena | Sí | Tipo de notificación: `NT` (Notificación), `CP` (Comunicación Personal), `CI` (Comunicado Institucional). |
| `procedure_code` | Cadena | Solo si `message_type=NT` | Código del procedimiento administrativo. |
| `procedure_stage` | Numérico | Solo si `message_type=NT` | Etapa: `1` (inicio), `2` (instrucción), `3` (finalización). |
| `signature_uid` | Cadena (UUID) | No | UUID de la firma institucional a usar. |
| `subject` | Cadena | Sí | Asunto de la notificación. Máximo 150 caracteres. |
| `content` | Cadena | Sí | Contenido de la notificación. |
| `content_type` | Cadena | Sí | Tipo MIME del contenido. Ejemplo: `text/html` |
| `webhook_url` | Cadena (URL) | No | URL para recibir el estado del procesamiento del mensaje. Enviar `null` o vacío si no se usa. |

**Para enlaces dentro del contenido:**
```html
<a href="https://digital.gob.cl" target="_blank">Enlace</a>
```

**Parte `attachments` (opcional):**
- Formato: archivo binario; múltiples archivos usando varios campos `attachments`.
- Límite por archivo: 20 MB.
- Límite total: 20 MB.
- Extensiones: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX.
- Máximo 50 archivos.
- Nombre de archivo: máximo 50 caracteres; solo letras (sin acentos ni ñ), números y separadores (`-`, `_`, espacio), sin usarlos al inicio, fin o juntos.

**Respuesta exitosa (HTTP 200):**
```json
{
 "message_data_id": "630c7a94ee5a2dbd341d23ff7",
 "sent_at": "Mon, 14 Jun 2023 15:09:03 GMT",
 "status": "pending"
}
```

## Códigos de error de envío

| Código | Mensaje | Posibles causas |
|--------|---------|-----------------|
| ERR001 | No se proporcionó ningún destinatario | `recipients` no tiene valor válido (arreglo con al menos un elemento). |
| ERR002 | Índices con elementos no esperados en destinatarios | Algún nodo en `recipients` no contiene el atributo `rol_unico`. |
| ERR003 | Índices de destinatarios no válidos | `rol_unico` no es entero positivo o excede 99.999.999. |
| ERR004 | Código de tipo de mensaje no ingresado | `message_type` no proporcionado. |
| ERR005 | Código de tipo de mensaje no permitido | `message_type` no es `NT`, `CP` o `CI`, o la institución no está habilitada para ese tipo. |
| ERR006 | Código de procedimiento administrativo no ingresado | `procedure_code` requerido cuando `message_type=NT`. |
| ERR007 | Código de procedimiento administrativo no válido | `procedure_code` no existe o no está habilitado para la institución. |
| ERR008 | Debe configurar el logo de su institución | El logo no ha sido configurado en la plataforma. |
| ERR013 | Archivo con formato no permitido | Extensión diferente a las permitidas. |
| ERR014 | Nombre del archivo excede 50 caracteres | — |
| ERR015 | Límite total de adjuntos superado (20 MB) | — |
| ERR016 | Archivo ya adjuntado (duplicado) | Archivos con el mismo nombre. |
| ERR017 | Contenido base64 del archivo no tiene formato correcto | — |
| ERR018 | Extensión del archivo no corresponde con el tipo de documento | — |
| ERR019 | Archivo excede los 20 MB | — |
| ERR020 | Firma no válida | UUID de firma pertenece a otra institución. |
| ERR021 | Archivo adulterado o con firma revocada | — |
| ERR023 | RUN no válido | Caracteres no numéricos, dígitos fuera de rango o sin valor. |
| ERR026 | Asunto excede 150 caracteres | — |
| ERR027 | Asunto no ingresado | — |
| ERR028 | URL no válida en el contenido | — |
| ERR030 | Más de 250 destinatarios | — |
| ERR031 | Envío duplicado | Mismo contenido enviado en los últimos 5 minutos; esperar el tiempo indicado. |
| ERR032 | Más de 50 archivos adjuntos | — |
| ERR033 | Nombre de archivo con caracteres no permitidos | Usar solo letras (sin acentos ni ñ), números, guiones, guiones bajos y espacios. |
| ERR034 | `webhook_url` no válida | URL con estructura incorrecta. |

## Endpoint: Ver estado de una notificación

```
URL: /notificador/messageStatus/{message_data_id}
Método: GET
```

**Respuesta JSON (ejemplo):**
```json
{
 "entity_id": "794a0088-cec0-11eb-b8bc-0242ac130003",
 "message_data_id": "60c7a94ee5a2dbd341d23ff7",
 "received_at": "Wed, 24 Aug 2022 15:59:23 GMT",
 "status": "processed",
 "subject": "Asunto de ejemplo",
 "recipents_counts": 5,
 "recipients": {
 "10936746": {
 "ddu_type": "not_configured",
 "message_status": "delivered",
 "method": "API",
 "delivered_at": "Wed, 24 Aug 2022 15:59:23 GMT",
 "read_at": null
 }
 }
}
```

Campos de `recipients`:

| Campo | Descripción |
|-------|-------------|
| `ddu_type` | Tipo de DDU al momento del envío: `casilla`, `email`, `not_configured`, `excepcion`. |
| `message_status` | Estado del mensaje: `delivered`, `error`, `pending`. |
| `method` | Método de envío: `WEB` o `API`. |
| `delivered_at` | Fecha de envío del mensaje. |
| `read_at` | Fecha de lectura. `null` si no ha sido leído. |

**Estados posibles de un mensaje:**

| Estado | Descripción |
|--------|-------------|
| `pending` | Estado inicial al crear el envío. |
| `delivered` | Envío finalizado correctamente. |
| `error` | Falló al crear/actualizar el envío. |
| `error_rejected` | Mensaje sospechoso o no válido. |
| `error_undetermined_undetermined` | No se pudo determinar un motivo específico de rebote. |
| `error_permanent_general` | Rechazo permanente general. |
| `error_permanent_no_email` | Rechazo permanente; dirección de correo no existe. |
| `error_permanent_supressed` | Descartado; historial reciente de rebotes. |
| `error_permanent_on_account_suspension_list` | Descartado; dirección en lista de rebotes previos. |
| `error_transient_general` | Rebote general; posible reintento en el futuro. |
| `error_transient_mailbox_full` | Bandeja del destinatario llena. |
| `error_transient_message_too_large` | Mensaje demasiado grande. |
| `error_transient_content_rejected` | Contenido rechazado. |
| `error_transient_attachment_rejected` | Archivo adjunto rechazado. |
| `error_send_message_mail` | No se pudo comunicar con el servidor de correo. |

**Estado de mensaje según configuración de DDU:**

| Estado DDU | Estado mensaje inicial | Estado mensaje final |
|------------|----------------------|---------------------|
| No configurada | `delivered` | `delivered` o `error` |
| Excepcionada | `delivered` | `delivered` o `error` |
| Casilla | `delivered` | `delivered` o `error` |
| Correo electrónico | `pending` (por pocos segundos) | `delivered` o `error` |

## Endpoint: Ver mensajes pendientes de un ciudadano

```
URL: /notificador/citizenPending/{rol-unico}
Método: GET
```

**Respuesta JSON:**
```json
{
 "access_url": "https://portal.devel.casillaunica.gob.cl/ext/bandeja",
 "current_ddu_type": "casilla",
 "result_message": "Usuario tiene mensajes pendientes por leer en su casilla",
 "status": true,
 "total_pending": 11
}
```

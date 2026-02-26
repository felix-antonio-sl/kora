---
_manifest:
  urn: urn:gov:kb:notificaciones
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- gobierno
- chile
- notificaciones
- interoperabilidad
- knowledge
lang: es
---

# Plataforma de Notificaciones Electrónicas del Estado

Fuente: WikiGuías SGD — `urn:gov:kb:notificaciones`
Responsable: División de Gobierno Digital, Ministerio SEGPRES / SGD.

## Contexto Normativo y Definiciones

La Plataforma de Notificaciones Electrónicas del Estado es el canal oficial para que los OAEs envíen notificaciones electrónicas a las personas en el marco de procedimientos administrativos. Base legal: Ley 21.180 de TDE, DFL N°1 y Norma Técnica de Notificaciones (DS N°8). Usa el Registro de Domicilios Digitales Únicos (DDU) y la CasillaÚnica.

| Término | Definición |
|---|---|
| DDU | Domicilio Digital Único: medio electrónico elegido por la persona para recibir notificaciones (CasillaÚnica o correo electrónico validado) |
| CasillaÚnica | Componente configurable como DDU; bandeja de mensajes centralizada donde las personas acceden a todas las notificaciones de OAEs |
| Notificación electrónica | Acto de comunicar formalmente a la persona destinataria una resolución u otro acto administrativo, mediante mensaje enviado a través de la Plataforma de Notificaciones |
| Aviso de notificación | Correo electrónico informativo que avisa la existencia de una nueva notificación en CasillaÚnica; no constituye notificación en sí |
| API Notificaciones | Servicio web que permite integrar plataformas institucionales al componente de envío de la Plataforma para gestionar notificaciones en forma automática |

Obligatoriedad: todos los OAEs deben practicar sus notificaciones por medios electrónicos usando la información del Registro de DDU (art. 46 Ley 19.880). Los OAEs deben integrarse a la plataforma para cumplir este mandato.

## Prerequisitos de Integración

Antes de solicitar integración, el OAE debe:
- Contar con Coordinador/a de Transformación Digital oficialmente designado (oficio a SGD y registro en Red de Coordinadores)
- Asegurar que los funcionarios que usarán la plataforma cuenten con ClaveÚnica activa
- Seleccionar uno o más procedimientos administrativos a notificar, cargados en el CPAT
- Definir el equipo de contacto institucional: contacto técnico, contacto de negocio y administrador institucional
- Definir el medio de envío: vía web, vía API o ambas

## Proceso de Integración a la Plataforma

### Paso 1 — Solicitud de Integración

- Ingresar a CeroFilas (https://gobdigital.cerofilas.gob.cl/)
- Crear el trámite "Solicitud de integración a la Plataforma de Notificaciones" (instituciones)
- Indicar en formulario: institución solicitante, contactos administrativos y técnico, administrador institucional, tipo de integración (web/API/ambas), nombre y descripción de la aplicación, URL (opcional)
- Leer y aceptar los términos y condiciones para las instituciones antes de enviar

### Paso 2 — Evaluación de Solicitud

- La SGD verifica: datos completos, correos institucionales, institución no integrada previamente
- Si hay inconsistencias: se rechaza con observaciones; la institución debe corregir y reenviar
- Si se acepta: la SGD habilita a la institución y al administrador institucional en ambiente de pruebas y envía correo con información de acceso y credenciales API + nodo PISEE si corresponde

### Paso 3 — Actividades en Ambiente de Pruebas

Configuración requerida vía interfaz web:
- Cargar logo institucional (PNG/JPG, 80–350x80 px, máx. 5 MB)
- Crear una o más firmas institucionales (texto)
- Seleccionar procedimientos administrativos desde lista CPAT
- Crear usuarios con rol de administrador de mensajes
- Enviar al menos un mensaje desde la plataforma web y, si corresponde, al menos uno desde la API vía nodo PISEE

RUNs de prueba recomendados:
- 33333333-3 → DDU Casilla
- 33333351-1 → DDU Excepcionado

CasillaÚnica de pruebas: https://portal.demo.casillaunica.gob.cl/casilla/ — RUN 33333333-3, clave "testing".

### Paso 4 — Solicitud de Certificación

- Una vez realizadas las actividades en ambiente de pruebas, continuar el flujo en CeroFilas para solicitar certificación
- Adjuntar comentarios y evidencias que faciliten la evaluación si es necesario

### Paso 5 — Certificación

La SGD valida que la institución haya:
- Configurado logo, firmas y procedimientos
- Creado administrador de mensajes
- Enviado mensajes por web/API según el tipo de integración solicitado

Si no se aprueba: se envían observaciones por correo; la institución debe corregir y volver a solicitar certificación.
Si se aprueba: se envía correo con detalles para configurar producción.

### Paso 6 — Habilitación en Producción

- La SGD registra la institución y al administrador institucional en producción; genera credenciales API si aplica
- La institución debe repetir la configuración en producción (logo, firmas, procedimientos) y crear administrador de mensajes
- Para integración vía API: solicitar o reutilizar nodo PISEE en producción a través de Mesa de Servicios; el nodo debe ser autorizado para consumir la plataforma de notificaciones
- Completar la integración API a través del nodo PISEE si corresponde

## Operación vía Web

Tipos de mensaje:
- **Mensaje Simple:** un solo mensaje con mismo contenido y adjuntos para uno o varios destinatarios
- **Mensaje Múltiple:** varios grupos de destinatarios dentro de un mismo envío, con posibilidad de diferenciar destinatarios y adjuntos por grupo

Proceso de creación:
- Elegir tipo de mensaje en "Crear mensaje"
- Seleccionar el procedimiento administrativo a notificar
- Agregar destinatarios manualmente o mediante archivo .csv
- Ingresar asunto (máx. 150 caracteres) y cuerpo de la notificación
- Adjuntar archivos; opcionalmente asociar una firma institucional y/o usar plantillas

Adjuntos:
- Peso máximo total: 20 MB por mensaje (suma de todos los adjuntos)
- Extensiones permitidas: pdf, jpg, png, doc, docx, xls, xlsx
- PDF con firma electrónica: solo se permiten documentos no adulterados, sin firmas revocadas, no modificados después de la firma

Estados de mensajes: Enviado / En proceso / Con error.

## Operación vía API

Prerequisitos:
- Nodo de interoperabilidad PISEE 2 configurado y autorizado para consumir la plataforma
- client_id y client_secret asociados a la institución
- Habilitación en producción completa

### Endpoint: `POST /notificador/sendMessage`

Content-Type: `multipart/form-data`

Partes:
- `data`: cadena JSON con los datos de la notificación
- `attachments`: archivos adjuntos opcionales (múltiples)

Campos JSON de `data`:

| Campo | Obligatoriedad | Descripción |
|---|---|---|
| recipients | Obligatorio | Arreglo de objetos `{ rol_unico }`; máx. 250 destinatarios; rol_unico es RUN/RUT sin dígito verificador |
| message_type | Obligatorio | `NT` (Notificación), `CP` (Comunicación Personal), `CI` (Comunicado Institucional) |
| procedure_code | Obligatorio si message_type=`NT` | Código del procedimiento administrativo habilitado |
| procedure_stage | Obligatorio si message_type=`NT` | 1 (inicio), 2 (instrucción), 3 (finalización) |
| signature_uid | Opcional | UUID de la firma institucional a utilizar |
| subject | Obligatorio | Asunto (máx. 150 caracteres) |
| content | Obligatorio | Contenido de la notificación |
| content_type | Obligatorio | MIME type, ej. `text/html` |
| webhook_url | Opcional | URL para recibir estado del procesamiento (POST con status y message_data_id) |

Adjuntos vía API:
- Cada archivo ≤ 20 MB; total adjuntos ≤ 20 MB
- Máx. 50 archivos por mensaje
- Extensiones permitidas: pdf, jpg, png, doc, docx, xls, xlsx

Respuesta exitosa (HTTP 200): JSON con `message_data_id`, `sent_at` y `status` (ej. `pending`).

### Códigos de Error Principales

| Código | Descripción |
|---|---|
| ERR001 | No se proporcionó ningún destinatario |
| ERR003 | rol_unico no válido (tipo o longitud) |
| ERR004 | message_type no ingresado |
| ERR006 | procedure_code no ingresado cuando message_type=`NT` |
| ERR008 | Logo institucional no configurado en la plataforma |
| ERR013–ERR021 | Errores en adjuntos (formato no permitido, nombre >50 caracteres, peso total>20MB, duplicados, base64 inválido, extensión no coincide, tamaño>20MB, firma no válida o documento adulterado) |
| ERR023 | RUN no válido |
| ERR026–ERR029 | Errores en asunto o contenido (longitud, ausencia, URL no válida) |
| ERR030 | Más de 250 destinatarios |
| ERR031 | Envío duplicado (mismo contenido dentro de 5 minutos) |
| ERR032 | Más de 50 archivos |
| ERR034 | webhook_url con URL no válida |

### Endpoint: `GET /notificador/messageStatus/{message_data_id}`

Consulta el estado de una notificación enviada identificada por `message_data_id`.

Campos de la respuesta JSON:

| Campo | Descripción |
|---|---|
| entity_id | ID de la institución |
| message_data_id | ID del envío |
| received_at | Fecha de recepción del mensaje por la plataforma |
| status | Estado global del envío (ej. `processed`) |
| subject | Asunto del envío |
| recipents_count | Cantidad de destinatarios |
| recipients | Mapa donde cada clave es un rol_unico con: ddu_type, message_status, method, delivered_at, read_at |

Valores de `ddu_type`: `casilla`, `email`, `not_configured`, `excepcion`.

### Estados por Destinatario (`message_status`)

| Estado | Descripción |
|---|---|
| pending | Estado inicial al crear el envío |
| delivered | Estado final; proceso de envío completado exitosamente |
| error | Fallo al crear/actualizar el envío para el destinatario |
| error_rejected | Mensaje determinado como sospechoso o no válido |
| error_undetermined_undetermined | No se pudo determinar un motivo específico de rebote |
| error_permanent_general | Rechazo permanente general |
| error_permanent_no_email | Rechazo permanente; dirección de correo destino no existe |
| error_permanent_supressed | Descartado por historial reciente de rebotes como dirección no válida |
| error_permanent_on_account_suspension_list | Descartado por estar en lista de correos con rebotes previos |
| error_transient_general | Rebote general; posible reenvío exitoso en el futuro |
| error_transient_mailbox_full | Rebote; bandeja de mensajes del destinatario llena |
| error_transient_message_too_large | Rebote; mensaje demasiado grande |
| error_transient_content_rejected | Rebote; contenido rechazado |
| error_transient_attachment_rejected | Rebote; archivo adjunto rechazado |
| error_send_message_mail | No se pudo comunicar con el servidor de correo |

### Estado del Mensaje según Configuración DDU

| Estado DDU del Destinatario | Estado Inicial | Estado Final |
|---|---|---|
| DDU no configurada | delivered | delivered o error |
| DDU excepcionada | delivered | delivered o error |
| DDU configurada como CasillaÚnica | delivered | delivered o error |
| DDU configurada como correo electrónico | pending | delivered o error (todos los posibles errores de la tabla anterior) |

## Articulación Normativa

XRef requeridos:
- `urn:tde:kb:nt-notificaciones` — Norma Técnica de Notificaciones (DS N°8)
- `urn:tde:kb:nt-documentos-expedientes`
- `urn:tde:kb:nt-interoperabilidad`
- `urn:tde:kb:manual-integracion-claveunica`
- `urn:tde:kb:guia-sistema-tde-2025`
- `urn:tde:kb:guia-rapida-cpat`

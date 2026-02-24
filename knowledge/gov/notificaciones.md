---
_manifest:
  urn: "urn:gov:kb:notificaciones"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "wikiguias.digital.gob.cl"
version: "2.0.0"
status: published
tags: [transformacion-digital, gobierno, chile, notificaciones, interoperabilidad]
lang: es
---

## Contexto Normativo y Digital

- Canal oficial para envío de notificaciones electrónicas de OAEs.
- Basado en Registro de Domicilios Digitales Únicos (DDU) y CasillaÚnica.
- Marco Legal: Ley 21.180 (Transformación Digital), DFL N°1 y Norma Técnica de Notificaciones.
- Objetivo: Comunicación segura, trazable y centralizada entre Estado y ciudadanía.

## Glosario Técnico

| Término | Definición |
| :--- | :--- |
| API Notificaciones | Servicio web para integración automática de plataformas institucionales. |
| Casilla Única | Bandeja de mensajes centralizada para acceso ciudadano a notificaciones de OAEs. |
| DDU | Domicilio Digital Único: medio elegido (CasillaÚnica o email validado) para notificaciones. |
| Notificación Electrónica | Acto formal de comunicación de resoluciones mediante mensaje en la plataforma. |
| Aviso de Notificación | Email informativo sobre nueva notificación en CasillaÚnica (no constituye notificación). |

## Obligatoriedad y Alcance

- Plataforma centralizada para registro de personas (naturales/jurídicas) en DDU.
- Uso obligatorio de medios electrónicos para notificaciones (Art. 46 Ley 19.880).
- Mandato de integración para todos los OAEs para notificar a interesados y apoderados.

## Requisitos Institucionales

- Coordinador de Transformación Digital oficialmente designado ante SGD.
- Funcionarios con ClaveÚnica activa.
- Procedimientos administrativos cargados en CPAT (completados, nivel digitalización óptimo).
- Equipo técnico, de negocio y administrador institucional definidos.
- Definición de modalidad: Web, API o ambas.

### Filtros CPAT Recomendados
- Estado: Completado.
- Tipo Usuario: Persona natural y jurídica.

## Proceso de Integración

### 1. Solicitud y Evaluación
- Registro en CeroFilas (https://gobdigital.cerofilas.gob.cl/).
- Formulario: Datos institución, contactos, tipo integración, app y aceptación T&C.
- Validación SGD: Verificación de correos institucionales y duplicidad.
- Resultado: Habilitación en ambiente de pruebas y envío de credenciales (API/PISEE).

### 2. Ambiente de Pruebas
- Configuración Web: Logo (PNG/JPG, 80-350x80 px, <5MB), firmas institucionales, selección trámites CPAT.
- Gestión: Creación de administradores de mensajes.
- Pruebas: Envío de mensajes vía Web/API.
- Datos Demo: RUN 33333333-3 (Casilla), RUN 33333351-1 (Excepcionado). Clave 'testing' en portal demo.

### 3. Certificación y Producción
- Solicitud vía CeroFilas adjuntando evidencias.
- Validación SGD: Verificación de configuraciones y envíos exitosos.
- Habilitación: Registro institucional en producción.
- API: Solicitud/reutilización de nodo PISEE en producción vía Mesa de Servicios.
- Configuración final: Replicar logo, firmas y trámites en ambiente producción.

## Operación Interfaz Web

### Tipos de Mensajes
- Mensaje Simple: Contenido idéntico para uno o varios destinatarios.
- Mensaje Múltiple: Grupos con destinatarios y adjuntos diferenciados.

### Parámetros de Envío
- Selección de trámite CPAT obligatorio.
- Destinatarios: Manual o vía archivo .csv.
- Asunto: Máximo 150 caracteres.
- Firmas: Opcional, uso de plantillas predefinidas.

### Restricciones de Adjuntos
- Peso máximo: 20 MB total por mensaje.
- Extensiones: pdf, jpg, png, doc, docx, xls, xlsx.
- PDFs: Validación estricta de integridad y firmas electrónicas no revocadas.

## Operación vía API

### Prerrequisitos
- Nodo PISEE 2 configurado y autorizado.
- Poseer client_id y client_secret.
- Institución configurada en ambiente producción.

### Endpoint: SendMessage
- **URL**: `/notificador/sendMessage`
- **Método**: POST (multipart/form-data)

| Campo JSON (data) | Obligatoriedad | Descripción |
| :--- | :--- | :--- |
| recipients | Sí | Arreglo de objetos `{ rol_unico }` (RUN sin DV). Máx 250. |
| message_type | Sí | NT (Notificación), CP (Comunicación Personal), CI (Comunicado). |
| procedure_code | Condicional | Obligatorio si message_type='NT'. |
| procedure_stage | Condicional | 1 (inicio), 2 (instrucción), 3 (finalización). |
| subject | Sí | Máximo 150 caracteres. |
| content | Sí | Cuerpo de la notificación. |
| content_type | Sí | MIME type (ej: 'text/html'). |
| webhook_url | No | URL para recibir estados de procesamiento (POST). |

## Respuestas y Estados API

### Códigos de Error Frecuentes
- ERR001-003: Problemas con destinatarios/RUN.
- ERR004-007: Errores en tipo de mensaje o código de procedimiento.
- ERR008: Logo no configurado.
- ERR013-021: Errores en adjuntos (formato, peso, firma, base64).
- ERR030-032: Exceso de destinatarios (>250), archivos (>50) o envío duplicado (<5 min).

### Consulta de Estado (GET)
- **URL**: `/notificador/messageStatus/{message_data_id}`
- Respuesta incluye: `entity_id`, `status` (global), `recipients_count` y detalle por destinatario.

## Estados de Mensajería y DDU

### Estados del Mensaje
| Valor | Definición |
| :--- | :--- |
| pending | Estado inicial de creación. |
| delivered | Envío finalizado exitosamente. |
| error | Fallo en creación/actualización para destinatario. |
| error_rejected | Mensaje sospechoso o inválido. |
| error_permanent_no_email | Dirección de correo destino inexistente. |
| error_permanent_supressed | Historial reciente de rebotes (lista de supresión). |
| error_transient_mailbox_full | Bandeja del destinatario llena. |
| error_transient_message_too_large | Mensaje excede tamaño permitido por receptor. |

### Flujo según Configuración DDU
| Estado DDU Destinatario | Estado Inicial | Estado Final |
| :--- | :--- | :--- |
| No configurada | delivered | delivered o error |
| Excepcionada | delivered | delivered o error |
| Casilla Única | delivered | delivered o error |
| Correo electrónico | pending | delivered o error (según respuesta servidor correo) |

---
_manifest:
  urn: urn:tde:kb:manual-integracion-notificaciones-p02
  provenance:
    source: https://wikiguias.digital.gob.cl/Manuales/integracion-casillaunica
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
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:tde:kb:manual-integracion-notificaciones
---

# Manual de Integración — Plataforma de Notificaciones del Estado - Parte 02

## Endpoint: Obtener códigos de procedimientos administrativos

```
URL: /notificador/getProcedure
Método: GET
```

**Respuesta JSON:**
```json
{
 "procedures": [
 {
 "code": "PA-SER0000-5463",
 "name": "Licitación Pública",
 "stage": 1,
 "stage_name": "Etapa de inicio"
 }
 ]
}
```

## Endpoint: Obtener UUID de firmas institucionales

```
URL: /notificador/getSignature
Método: GET
```

**Respuesta JSON:**
```json
{
 "signatures": [
 {
 "body": "<p>...</p>",
 "name": "Firma institución",
 "uid": "483ef791-7253-46a0-997c-afd8d089cc26",
 "updated_at": "Mon, 20 Dec 2024 10:42:18 GMT"
 }
 ]
}
```

## Endpoint: Obtener comprobante de mensaje

```
URL: /notificador/getReceipt/{message_data_id}/{rol_unico}
Método: GET
```

**Respuesta JSON:**
```json
{
 "url": "https://s3-...amazonaws.com/.../comprobante_envio_...pdf?..."
}
```

**Errores de comprobante:**

| Código | Mensaje | Causa |
|--------|---------|-------|
| ERR022 | Código de mensaje no válido | No existe, pertenece a otra institución o formato incorrecto. |
| ERR023 | RUN no válido | Caracteres no numéricos o fuera de rango. |
| ERR024 | Mensaje no válido | Certificado no corresponde al destinatario. |
| ERR025 | No se puede descargar el comprobante | Mensaje en proceso, con error o no enviado. |

## Nivel de transacciones

La API está disponible 24×7 con un máximo de **6 TPS**.

## Procedimiento para registrar una excepción

El administrador institucional puede registrar una excepción para un ciudadano que, previa solicitud, quede exento de recibir notificaciones electrónicas (Ley 19.880, art. 46; Norma Técnica, art. 8; Reglamento, arts. 28 y 29).

Campos del formulario de excepción:

| Campo | Descripción |
|-------|-------------|
| **RUN** | RUN del ciudadano con excepción aprobada. |
| **Correo electrónico** | Correo del solicitante. |
| **Teléfono** | Teléfono del solicitante. |
| **Dirección** | Dirección completa del solicitante. |
| **ID expediente electrónico** | ID de la carpeta virtual del ciudadano (interno, opcional). |
| **Fecha de solicitud** | Fecha en que se realizó la solicitud de excepción. |
| **Motivo** | Seleccionar de lista desplegable predefinida. |
| **Otros motivos** | Texto explicativo (solo si se selecciona "Otros motivos"). |
| **Archivos** | Documentos de soporte. |
| **Botón "Aprobar"** | Registra la excepción; el ciudadano queda en estado "Excepción". |

## Certificado de envío

La plataforma permite descargar un certificado de envío por cada mensaje que certifica el envío a un destinatario, con fecha, hora y datos del envío. Disponible desde la interfaz web y la API. Los certificados pueden ser validados por cualquier persona.

## Soporte y escalamiento

- **Mesa de servicios (instituciones):** https://gobdigitalcl.freshdesk.com/support/home
- **Sugerencias:** correo del producto (ver plataforma).

## Anexo: Ejemplos cURL

### Envío de notificación
```bash
curl --location '{url}/notificador/sendMessage' \
--form 'data="{\"recipients\":[{\"rol_unico\":26093912}],\"message_type\":\"NT\",\"procedure_code\":\"PA-SUP00604-00007\",\"procedure_stage\":1,\"subject\":\"Asunto\",\"content\":\"Contenido\",\"content_type\":\"text/html\",\"webhook_url\":null}"' \
--form 'attachments=@"/ruta/al/archivo.pdf"'
```

### Ver estado de un envío
```bash
curl --location '{url}/notificador/messageStatus/6789a014291e172670ae075e'
```

### Ver mensajes pendientes de un ciudadano
```bash
curl --location '{url}/notificador/citizenPending/26093912'
```

### Ver procedimientos administrativos
```bash
curl --location '{url}/notificador/getProcedure'
```

### Ver firmas institucionales
```bash
curl --location '{url}/notificador/getSignature'
```

### Obtener comprobante de mensaje
```bash
curl --location '{url}/notificador/getReceipt/64f65a4d144e0d5ac4bfd25e/26093912'
```

## Anexo: Configuración de Nodo PISEE 2

### Credenciales

En el archivo `config.json` del nodo PISEE, dentro de `identificación.custom`, agregar o ajustar:

- `id`: corresponde al `client_id` de la institución.
- `secret`: corresponde al `client_secret` de la institución.

### Endpoints

En el arreglo `consumidor` del archivo `config.json`, listar los servicios que la institución desea utilizar.

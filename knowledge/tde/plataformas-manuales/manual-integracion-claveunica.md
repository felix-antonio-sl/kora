---
_manifest:
  urn: "urn:kora:kb:tde:plataformas-manuales:manual-integracion-claveunica:1.0.0"
  provenance: "https://wikiguias.digital.gob.cl/Manuales/Integraci%C3%B3n_Clave%C3%9Anica"
version: 1.0.0
status: draft
tags: [tde, plataformas-manuales, como-usar, integracion, guia]
lang: es
---

# Manual de Integración — ClaveÚnica

Dirigido a equipos técnicos y responsables de producto que implementan o mantienen trámites y servicios digitales con autenticación ClaveÚnica.

ClaveÚnica es un proveedor de identidad digital (Identity Provider) basado en OpenID Connect (OAuth 2.0). Disponible sin costo para plataformas y aplicaciones web y mobile de los OAE.

## Preguntas frecuentes

**¿Quiénes pueden integrar ClaveÚnica?**
Organismos de la Administración del Estado; sin costo.

**¿Se pueden usar dos formas de autenticación en paralelo?**
No. Las instituciones mandatadas por el Instructivo Presidencial de Transformación Digital deben usar ClaveÚnica como único medio de autenticación para personas naturales. Gestionar migración con plazos definidos.

**¿Se puede integrar ClaveÚnica para trámites institucionales internos (funcionarios)?**
Sí, aunque el mandato aplica especialmente a trámites del Registro Nacional de Trámites dirigidos a personas naturales.

## Proceso de integración — Resumen

1. Solicitar credenciales en CeroFilas.
2. Implementar la integración con OpenID Connect (Authorization Code Flow).
3. Certificar la integración para habilitar credenciales de producción.

La complejidad de la implementación depende del lenguaje de la plataforma. Existen [ejemplos de código fuente](https://docs.google.com/document/d/16c0D2jVhuYOYGI9z4kC2aoNH8oWNA9v1cc3tXQ76TO0/edit#heading=h.vr0yv8svlo8c) en los lenguajes y frameworks más utilizados.

## 1. Solicitar credenciales

1. Ingresar a https://claveunica.cerofilas.gob.cl/ (o desde la sección "Instituciones Públicas" de https://claveunica.gob.cl/).
2. Autenticarse con ClaveÚnica.
3. Iniciar el trámite "Solicitud Credenciales de Integración a ClaveÚnica".
4. Completar el formulario:

| Campo | Requisito |
|-------|-----------|
| **Institución** | Nombre de la institución pública. |
| **Contacto Administrativo** | Funcionario responsable de la plataforma. Correo debe ser institucional y nominativo (no se aceptan casillas genéricas: contacto@, soporte@, info@). |
| **Contacto Técnico** | Contraparte técnica. Puede ser el mismo que el administrativo. Correo institucional o del dominio del proveedor si corresponde. |
| **Nombre de la aplicación** | Aparece en el formulario de login de ClaveÚnica; debe identificar claramente institución y plataforma. |
| **Descripción de la aplicación** | Propósito de la integración; concisa. |
| **Tipo de público objetivo** | "Público (ciudadanía)" o "Interno (institución)". |
| **URL de la aplicación** | Dominio obligatorio: `.gob.cl` (según Norma Técnica, cap. II, art. 13). |
| **Redirect URI** | Callback al que ClaveÚnica redirige tras autenticación exitosa (recibe `code` y `state`). Ingresar URI para testing, QA y producción. No se permiten dominios `localhost`. Dominio de producción debe ser `.gob.cl`. La URI debe incluir nombre o siglas de la institución. Solo esquema, autoridad y path (sin query). |
| **Logout URI** | Opcional. URI a la que ClaveÚnica redirige tras cerrar sesión; solo la parte de autoridad de la URI. |
| **Términos y Condiciones** | Leer y aceptar antes de enviar: https://drive.google.com/file/d/1ZWlkVphNx6gloEuLxiQVXbtOWvZPDjZq/view |

5. Enviar la solicitud. Revisión en **6 días hábiles**.
6. Si es aprobada: se envían 3 pares de credenciales (`client_id` + `client_secret`) a la casilla indicada (remitente: no-reply@digital.gob.cl; verificar que no esté en spam).
   - Par 1: **Sandbox/Testing** — operativo de inmediato.
   - Par 2: **QA** — operativo de inmediato.
   - Par 3: **Producción** — bloqueado hasta certificación.
7. Si es rechazada: se enviará correo con el motivo.

### Credenciales de sandbox y QA

Permiten probar en un ambiente limitado usando solo los siguientes RUN de prueba:

| RUN | Contraseña |
|-----|------------|
| 44.444.444-4 | testing |
| 55.555.555-5 | testing |
| 88.888.888-8 | testing |
| 99.999.999-9 | testing |

> El `client_secret` es confidencial; nunca exponerlo. El resguardo de las credenciales es responsabilidad de la institución.

## 2. Implementación técnica (Authorization Code Flow)

Protocolo: **HTTPS obligatorio**. TLS 1.2 o superior. No se acepta TLS 1.0 ni 1.1. HTTP no permitido en producción.

### Paso 1: Crear token de estado anti-falsificación (CSRF)

Generar una cadena aleatoria de 30 o más caracteres (o hash con secreto). Mantener este token entre el cliente y la aplicación para verificar en Paso 3.

### Paso 2: Enviar solicitud de autenticación

Solicitud **GET** vía **HTTPS** a:
```
https://accounts.claveunica.gob.cl/openid/authorize/
```

Parámetros obligatorios:

| Parámetro | Valor |
|-----------|-------|
| `client_id` | Identificador de la integración (obtenido en credenciales). |
| `response_type` | `code` (siempre). |
| `scope` | `openid run name` |
| `redirect_uri` | URI de la aplicación, codificada en formato URL. |
| `state` | Token creado en Paso 1. |

Ejemplo de URI final:
```
https://accounts.claveunica.gob.cl/openid/authorize/?client_id=Wbgx7HkjoeU6uarez3uYnn41VmGkd600&response_type=code&scope=openid run name&redirect_uri=https%3A%2F%2Fintegrador.cl%2Fcallback&state=abcdefgh
```

### Paso 3: Confirmar token anti-falsificación

ClaveÚnica redirige a la `redirect_uri` añadiendo `code` y `state`. Verificar que el `state` recibido coincide con el token creado en Paso 1.

### Paso 4: Cambiar código de autorización por token de acceso

El `code` expira en **5 minutos**. Solicitud **POST** vía **HTTPS** a:
```
https://accounts.claveunica.gob.cl/openid/token/
```

Parámetros en el body (`application/x-www-form-urlencoded`):

| Parámetro | Valor |
|-----------|-------|
| `client_id` | Identificador de la integración. |
| `client_secret` | Secreto de la integración. **No codificar de forma fija en el código fuente.** |
| `redirect_uri` | Misma URI del Paso 2. |
| `grant_type` | `authorization_code` (siempre). |
| `code` | Código obtenido en Paso 3. |
| `state` | Token creado en Paso 1. |

Ejemplo cURL:
```bash
curl -i https://accounts.claveunica.gob.cl/openid/token/ \
  -H "content-type: application/x-www-form-urlencoded; charset=UTF-8" \
  --data "client_id=123&client_secret=456&redirect_uri=https%3A%2F%2Fexample.com&grant_type=authorization_code&code=aa4af81bc6574800bee3aada0fed99c4&state=abcdefgh"
```

### Paso 5: Autenticar usuario

La respuesta es un JSON con el `access_token`:
```json
{
  "access_token": "95104ab471534af08683aefa7d0935a3",
  "token_type": "bearer",
  "expires_in": 3600,
  "id_token": "eyJhbGciOiJSUzI1NiIs..."
}
```

### Paso 6: Obtener datos del ciudadano

Solicitud **POST** vía **HTTPS** a:
```
https://accounts.claveunica.gob.cl/openid/userinfo/
```
Header: `Authorization: Bearer {access_token}`

Ejemplo cURL:
```bash
curl -i https://accounts.claveunica.gob.cl/openid/userinfo/ -X POST \
  -H "authorization: Bearer 2718e590ec7e47858e4af5922050d28b"
```

Respuesta JSON:
```json
{
  "sub": "1234567",
  "RolUnico": {
    "DV": "9",
    "numero": 12345678,
    "tipo": "RUN"
  },
  "name": {
    "apellidos": ["Del Río", "Gonzalez"],
    "nombres": ["María", "Carmen"]
  }
}
```

> El campo `sub` no debe usarse como llave del registro. El identificador de la persona es `RolUnico.numero` (RUN).

### Paso 7: Cierre de sesión

La sesión de ClaveÚnica dura 60 segundos. La aplicación integradora siempre debe cerrar la sesión de ClaveÚnica al cerrar la propia.

**Método 1:**
```
https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout?redirect=logout_uri
```

**Método 2 (JavaScript):**
```javascript
function Logout() {
  window.location.href = "https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout";
  setTimeout(function () {
    window.location.href = "logout_uri";
  }, 1000);
}
```

> No usar popups ni iframes para llamar al endpoint logout (provoca error de CORS, dejando la sesión abierta).

Las URI de logout deben registrarse al solicitar credenciales. Para cambiarlas, solicitar en la [Mesa de Servicio](https://digital.gob.cl/incidencia).

## 3. Certificación y activación de credenciales de producción

Las credenciales de producción están desactivadas por defecto. El mensaje "La institución no está habilitada en ClaveÚnica" confirma que deben activarse.

### Requisitos de certificación

| Requisito | Detalle |
|-----------|---------|
| **Botón oficial de ClaveÚnica** | Usar el botón oficial según [lineamientos oficiales](https://drive.google.com/file/d/1XvPV-jfJKLg-1Gx1Qo26oAvkQ_tSmtZj/view?usp=sharingy). Recursos en [Figma](https://www.figma.com/community/file/1494787307175475602) y [ejemplos en código](https://drive.google.com/drive/folders/1xcsEoIv8CtcBdDvB1Y-FIvcH91f1sbfo?usp=drive_link). |
| **HTTPS en producción** | Protocolo HTTPS obligatorio. |
| **Llamada al formulario a pantalla completa** | Sin iframes, popups ni elementos similares. La barra de direcciones no debe quedar oculta. |
| **State dinámico** | El parámetro `state` debe generarse dinámicamente (Paso 1). |
| **Secuencia completa OpenID Connect** | Scope `openid run name`; todos los endpoints deben comenzar con `accounts.claveunica.gob.cl`. |
| **Llamadas desde backend** | Evidencia de llamadas a `token/` y `userinfo/` desde el backend (print de pantalla con la URL utilizada). |
| **Credenciales en variables de entorno** | `client_id` y `client_secret` no deben estar en el código fuente; usar variables de entorno. Proporcionar evidencia visual. |
| **Cierre de sesión** | Verificar que el sitio tiene un botón o link visible para cerrar sesión y que llama correctamente al endpoint. |

### Solicitar certificación

1. Ingresar a [CeroFilas](https://gobdigital.cerofilas.gob.cl/) y continuar el flujo de la solicitud de credenciales original.
2. En "Datos para la revisión práctica": verificar que el `client_id` corresponde a las credenciales de producción.
3. Seleccionar método de revisión:
   - **Sitio público en internet:** indicar URL del botón de ClaveÚnica y adjuntar evidencia en imágenes de las llamadas a los endpoints `token` y `userinfo`.
   - **Ambiente no accesible públicamente:** el equipo de ClaveÚnica agenda videollamada. El contacto administrativo debe estar presente.
4. Agregar información adicional si es necesario.

Plazo de certificación: **6 días hábiles** desde el ingreso del ticket. Puede extenderse si hay observaciones, dificultades de acceso o si la certificación es por videollamada.

## 4. Actualizar Redirect URI u otros datos

Para actualizar URIs (callback o logout): ingresar a [CeroFilas](https://gobdigital.cerofilas.gob.cl/) en el trámite "Actualización de URIs de Credenciales de Integración ClaveÚnica".

Datos requeridos:
- Nombre y correo del solicitante.
- `client_id` del ambiente cuya URI se desea actualizar.
- URI callback y/o logout nueva.

> Solo puede solicitarlo el contacto administrativo registrado en las credenciales. Plazo de respuesta: **3 días hábiles**.

Para cambiar el nombre de la aplicación: [Mesa de Servicio](https://gobdigitalcl.freshdesk.com/support/tickets/new).

## 5. Consideraciones generales para envío de requerimientos

- Tickets deben ser creados por la persona responsable usando correo institucional (no se aceptan Gmail, Yahoo, etc.).
- Canal oficial: [Mesa de Servicios SGD](https://digital.gob.cl/incidencia) y [CeroFilas](https://gobdigital.cerofilas.gob.cl/).
- Solicitudes por email directo a funcionarios no son consideradas; siempre crear ticket formal.

## 6. Capacitaciones mensuales

Inscripción en [CeroFilas](https://gobdigital.cerofilas.gob.cl/) en el trámite "Inscripción a capacitaciones de productos de Gobierno Digital".

## Anexo: Probar integración en cURL

### Token de acceso
```bash
curl -i https://accounts.claveunica.gob.cl/openid/token/ \
  -H "content-type: application/x-www-form-urlencoded; charset=UTF-8" \
  --data "client_id=2177fdbd81d54ebab895ed86b5f7d1b4&client_secret=1ec2a3c429ac4763b2665d57d2379b81&redirect_uri=https%3A%2F%2Flocalhost%2Fcallback&grant_type=authorization_code&code=5050299f54064a708ac17420d02417e8&state=1e5bdc760608dc3cfcd0e7ae4"
```

### Datos de usuario
```bash
curl -i https://accounts.claveunica.gob.cl/openid/userinfo/ -X POST \
  -H "authorization: Bearer 10a169a98eb143c18a732ed2e1df32fb"
```

### Formulario de login (en navegador, no cURL)
```
https://accounts.claveunica.gob.cl/openid/authorize/?client_id=2177fdbd81d54ebab895ed86b5f7d1&response_type=code&scope=openid run name&redirect_uri=https%3A%2F%2Flocalhost%2Fcallback&state=1e5bdc760608dc3cfcd0e7ae4
```

## Anexo: Probar integración en Postman

### Endpoint token/

- URL: `https://accounts.claveunica.gob.cl/openid/token/`
- Método: POST
- Headers: `Content-Type: application/x-www-form-urlencoded`
- Body (x-www-form-urlencoded):

| Key | Value |
|-----|-------|
| `client_id` | client_id de la integración |
| `client_secret` | client_secret de la integración |
| `redirect_uri` | redirect_uri de la integración |
| `grant_type` | `authorization_code` |
| `code` | code obtenido en login |
| `state` | state usado en login |

### Endpoint userinfo/

- URL: `https://accounts.claveunica.gob.cl/openid/userinfo/`
- Método: POST
- Authorization: Bearer Token → ingresar access_token.

## Anexo: Código fuente de ejemplo

Disponible en [carpeta de ejemplos](https://drive.google.com/drive/folders/11CUSgtByjsyg5jIzF1wF7JDxTQEM6wft?usp=sharing):

- Python
- PHP
- DotNET
- Java
- Postman
- HTML y CSS del Botón Oficial

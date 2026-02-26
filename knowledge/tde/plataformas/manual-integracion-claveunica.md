---
_manifest:
  urn: "urn:tde:kb:manual-integracion-claveunica"
  provenance:
    created_by: FS
    created_at: '2026-02-26'
    source: "https://wikiguias.digital.gob.cl/Manuales/Integraci%C3%B3n_Clave%C3%9Anica"
version: 1.0.0
status: published
tags: [tde, plataforma, claveunica, integración, openid-connect, oauth2, autenticación, identidad-digital]
lang: es
---

# Manual de integración de ClaveÚnica

Guía para instituciones del Estado sobre integración de ClaveÚnica como mecanismo de autenticación: solicitud de credenciales en CeroFilas → implementación técnica con OpenID Connect (OAuth 2.0) → certificación para credenciales de producción.

Dirigido a equipos técnicos y responsables de producto.

## Información general

### Definición

ClaveÚnica = Identity Provider (IdP) oficial del Estado de Chile. Mecanismo de autenticación que permite a ciudadanos acceder a plataformas y servicios del Estado con una sola contraseña. Base del Modelo de Identidad Digital en Chile.

### Elegibilidad

- Disponible sin costo para plataformas web y mobile de Organismos de la Administración del Estado (OAE).
- Instructivo Presidencial de Transformación Digital: instituciones mandatadas DEBEN usar ClaveÚnica como único medio de autenticación para personas naturales.
- Si existen otros mecanismos → gestionar migración con plazos definidos.

### Trámites internos

Instructivo rige especialmente para trámites del Registro Nacional de Trámites con autenticación. No hay restricción para uso en plataformas internas institucionales.

---

## Proceso de integración

### Flujo general

1. Solicitar credenciales en CeroFilas
2. Implementar integración (OpenID Connect / OAuth 2.0)
3. Certificar integración
4. Activar credenciales de producción

---

## 1. Solicitar credenciales

### Acceso

- Portal: [claveunica.gob.cl](https://claveunica.gob.cl/) → sección "Instituciones Públicas" → "Enviar solicitud"
- Acceso directo: [claveunica.cerofilas.gob.cl](https://claveunica.cerofilas.gob.cl/)
- Autenticarse con ClaveÚnica → trámite "Solicitud Credenciales de Integración a ClaveÚnica" → "Iniciar trámite"

### Campos del formulario

| Campo | Descripción |
|-------|-------------|
| **Seleccionar Institución** | Nombre de la institución pública que integrará ClaveÚnica |
| **Contacto Administrativo** | Funcionario responsable de la plataforma. Correo DEBE ser institucional y nominativo. NO se aceptan casillas genéricas (contacto@, soporte@, info@) |
| **Contacto Técnico** | Contraparte técnica. Puede ser proveedor externo (jefe de proyectos). Se recomienda funcionario. Correo institucional obligatorio |
| **Nombre de la aplicación** | Aparece en formulario de login ClaveÚnica. Debe identificar claramente institución y plataforma. Editable en [CeroFilas](https://gobdigital.cerofilas.gob.cl/) trámite "Gestor de Credenciales" (solo por solicitante original) |
| **Descripción de la aplicación** | Propósito de la integración. Incluir si desarrollo es por proveedor externo. Concisa |
| **Tipo de público objetivo** | "Público (ciudadanía)" o "Interno (Institución)" |
| **URL de la aplicación** | Dirección pública del sitio integrado. Dominio DEBE ser `.gob.cl` (Norma Técnica sistemas/sitios web, cap. II, art. 13) |
| **Redirect URI** | Callback URL que recibe `code` y `state` post-autenticación. Obligatorio: 1 testing + 1 QA + 1 producción. PROHIBIDO localhost. DEBE incluir nombre/siglas de institución. URI producción DEBE tener dominio `.gob.cl`. Solo: esquema + autoridad + path (sin query) |
| **Logout URI** | Opcional. Solo autoridad de la URI. Separar múltiples con coma. Cambios vía [Mesa de Servicio](https://gobdigitalcl.freshdesk.com/support/tickets/new) |
| **Términos y Condiciones** | Obligatorio abrir y leer antes de continuar |

### Resultado de solicitud

- Tiempo de revisión: **6 días hábiles**
- Si aprobada → email con 3 pares de credenciales (client_id + client_secret):
  - **Sandbox/Testing**: operativas inmediatamente. Solo RUNs de prueba
  - **QA**: idénticas a sandbox. Solo RUNs de prueba
  - **Producción**: bloqueadas hasta certificación
- Si rechazada → email con motivo
- Notificaciones desde: `no-reply@digital.gob.cl` (verificar que no esté en spam)

### Credenciales: sandbox vs QA vs producción

| Ambiente | Uso | Estado inicial | Autenticación |
|----------|-----|----------------|---------------|
| Sandbox | Desarrollo/pruebas | Activas | Solo RUNs de prueba |
| QA | Pruebas QA | Activas | Solo RUNs de prueba |
| Producción | Ciudadanos reales | Bloqueadas | Requiere certificación |

**client_secret es confidencial** — no exponer. Resguardo de credenciales es responsabilidad de la institución.

---

## 2. Implementación técnica (OpenID Connect / OAuth 2.0)

Protocolo: Authorization Code Flow. Intercambio de tokens entre ClaveÚnica y aplicación integradora.

**OBLIGATORIO**: HTTPS con TLS 1.2 o superior. No se aceptan TLS 1.0/1.1.

### Paso 1: Crear token anti-falsificación (state)

- Generar token de sesión único (≥30 caracteres aleatorios o hash con secreto)
- Prevención de ataques CSRF (Cross-Site Request Forgery)
- Debe coincidir con el `state` devuelto por ClaveÚnica

### Paso 2: Solicitud de autenticación

**GET** → `https://accounts.claveunica.gob.cl/openid/authorize/`

| Parámetro | Valor |
|-----------|-------|
| `client_id` | Identificador de la integración |
| `response_type` | `code` (siempre) |
| `scope` | `openid run name` |
| `redirect_uri` | URI de la aplicación (codificada URL) |
| `state` | Token del Paso 1 |

**Ejemplo URI compuesta**:
```
https://accounts.claveunica.gob.cl/openid/authorize/?client_id=Wbgx7HkjoeU6uarez3uYnn41VmGkd600&response_type=code&scope=openid run name&redirect_uri=https%3A%2F%2Fintegrador.cl%2Fcallback&state=abcdefgh
```

**RUNs de prueba (sandbox/QA)**:

| RUN | Contraseña |
|-----|------------|
| 44.444.444-4 | testing |
| 55.555.555-5 | testing |
| 88.888.888-8 | testing |
| 99.999.999-9 | testing |

### Paso 3: Confirmar token anti-falsificación

- ClaveÚnica redirige a Redirect URI con `code` + `state`
- Verificar que `state` recibido == token creado en Paso 1

### Paso 4: Obtener token de acceso

**POST** → `https://accounts.claveunica.gob.cl/openid/token/`

Header: `Content-Type: application/x-www-form-urlencoded`

| Parámetro | Valor |
|-----------|-------|
| `client_id` | Identificador de la integración |
| `client_secret` | Secreto de la integración (NUNCA exponer) |
| `redirect_uri` | Misma URI del Paso 2 (encoded) |
| `grant_type` | `authorization_code` (siempre) |
| `code` | Código del Paso 3 (expira en **5 minutos**, 32 caracteres) |
| `state` | Token del Paso 1 |

**Credenciales NUNCA deben estar hardcodeadas en código fuente** → usar variables de entorno.

**cURL ejemplo**:
```bash
curl -i https://accounts.claveunica.gob.cl/openid/token/ \
  -H "content-type: application/x-www-form-urlencoded; charset=UTF-8" \
  --data "client_id=123&client_secret=456&redirect_uri=https%3A%2F%2Fexample.com&grant_type=authorization_code&code=aa4af81bc6574800bee3aada0fed99c4&state=abcdefgh"
```

### Paso 5: Autenticar usuario

Respuesta JSON con `access_token`:

```json
{
  "access_token": "95104ab471534af08683aefa7d0935a3",
  "token_type": "bearer",
  "expires_in": 3600,
  "id_token": "eyJhbGciOiJSUzI1NiIsIm6Ijg1ZGVjMDU1MjZmNjUwZlMTI4NTc3NGM3In0"
}
```

### Paso 6: Obtener datos del ciudadano

**POST** → `https://accounts.claveunica.gob.cl/openid/userinfo/`

Header: `Authorization: Bearer {access_token}`

**cURL ejemplo**:
```bash
curl -i https://accounts.claveunica.gob.cl/openid/userinfo/ \
  -X POST -H "authorization: Bearer 2718e590ec7e47858e4af5922050d28b"
```

**Respuesta JSON**:
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

**Campo `sub`**: incluido por especificación OpenID Connect. NO usar como llave de registro. Identificador de persona = `RolUnico.numero` (RUN).

### Paso 7: Cierre de sesión

Sesión ClaveÚnica: 60 segundos (Single Sign On). Aplicación integradora DEBE cerrar sesión ClaveÚnica cada vez que cierre la propia.

**Endpoint**: `https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout`

**Llamada vía GET**. PROHIBIDO: popups o iframes (error CORS → sesión queda abierta).

Parámetro `redirect` (opcional, recomendado): URI de logout registrada al solicitar credenciales. Si URI no registrada → redirección no se realiza.

**Tipos de cierre de sesión**:

| Tipo | Descripción |
|------|-------------|
| Explícito | Botón de cierre de sesión visible en zona privada del sitio |
| Implícito (por reglas de negocio) | Aplicación cierra unilateralmente (ej: RUN no reconocido como usuario del sistema) |
| Implícito (post-flujo) | Cierre inmediato post UserInfo. Para procesos de firma electrónica o lineales (encuestas) sin botón de logout |

**Método 1** (redirect):
```
https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout?redirect=logout_uri
```

**Método 2** (JavaScript con timeout):
```javascript
function Logout() {
  window.location.href = "https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout";
  setTimeout(function () {
    window.location.href = "logout_uri";
  }, 1000);
}
```

---

## 3. Certificación y activación de producción

### Prerrequisitos

Las credenciales de producción están bloqueadas por defecto. Mensaje en login: "La institución no está habilitada en ClaveÚnica".

### Requisitos de certificación

| Requisito | Detalle |
|-----------|---------|
| Botón oficial ClaveÚnica | Usar botón oficial según [lineamientos](https://drive.google.com/file/d/1XvPV-jfJKLg-1Gx1Qo26oAvkQ_tSmtZj/view). Recursos en [Figma](https://www.figma.com/community/file/1494787307175475602) y [ejemplos en código](https://drive.google.com/drive/folders/1xcsEoIv8CtcBdDvB1Y-FIvcH91f1sbfo) |
| Protocolo HTTPS | Obligatorio en producción |
| Llamada correcta al formulario | Pantalla completa, flujo lineal. PROHIBIDO: iframe, popup u otros. Barra de direcciones visible |
| State dinámico | Generado dinámicamente según Paso 1 |
| Secuencia OpenID Connect completa | Scope `openid run name`. Endpoints con `accounts.claveunica.gob.cl` |
| Llamadas desde backend | Evidencia de llamadas a `token/` y `userinfo/` desde backend. Print de pantalla del código |
| Credenciales ocultas | client_id y client_secret en variables de entorno (NO hardcodeados). Evidencia visual requerida |
| Cierre de sesión | Botón/link identificado. Llamada al endpoint de logout. Se verifica cerrando e intentando iniciar sesión nuevamente |

### Proceso de solicitud

1. En [CeroFilas](https://gobdigital.cerofilas.gob.cl/) → continuar trámite existente → formulario de solicitud de certificación
2. Verificar que client_id corresponde a credenciales de producción
3. Seleccionar método de revisión:
   - **Sitio público**: URL del sitio + evidencia en imágenes de endpoints token/ y userinfo/
   - **Sitio no accesible públicamente**: equipo ClaveÚnica contacta para videoconferencia. Contacto administrativo DEBE estar presente
4. Agregar información adicional si aplica

### Tiempos

- Certificación: **6 días hábiles** desde ingreso de solicitud
- Puede variar si: incumplimiento de requisitos, dificultades de acceso al sitio, o certificación por videollamada
- Observaciones → integrador debe corregir en menor tiempo posible

### Notas de revisión

- Ambiente de producción DEBE estar publicado y accesible desde internet
- NO se aceptan ambientes de desarrollo, QA, pre-productivos o sitios incompletos
- Si no hay acceso externo → indicar en solicitud para coordinar videollamada

---

## Actualización de datos de integración

### Redirect URI y Logout URI

- Portal: [CeroFilas](https://gobdigital.cerofilas.gob.cl/) → trámite "Actualización de URIs de Credenciales de Integración ClaveÚnica"
- Datos requeridos: nombre, correo, client_id del ambiente, nueva URI callback/logout
- Solo puede solicitarlo el contacto administrativo registrado
- Tiempo de respuesta: **3 días hábiles**

### Nombre de la aplicación

- Vía ticket en [Mesa de Servicio](https://gobdigitalcl.freshdesk.com/support/tickets/new)

---

## Consideraciones sobre requerimientos

- Ticket DEBE ser creado por responsable institucional con correo institucional. NO se aceptan Gmail, Yahoo, etc.
- Canal oficial: [Mesa de Servicios SGD](https://digital.gob.cl/incidencia) y [CeroFilas](https://gobdigital.cerofilas.gob.cl/)
- No se consideran solicitudes fuera de estos medios

---

## Endpoints de referencia

| Endpoint | Método | Uso |
|----------|--------|-----|
| `https://accounts.claveunica.gob.cl/openid/authorize/` | GET | Formulario de login |
| `https://accounts.claveunica.gob.cl/openid/token/` | POST | Obtener access token |
| `https://accounts.claveunica.gob.cl/openid/userinfo/` | POST | Obtener datos de usuario |
| `https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout` | GET | Cierre de sesión |

## Código fuente de ejemplo

Lenguajes/frameworks disponibles: Python, PHP, DotNET, Java, Postman, HTML/CSS del botón oficial.

- [Repositorio de ejemplos](https://drive.google.com/drive/folders/11CUSgtByjsyg5jIzF1wF7JDxTQEM6wft?usp=sharing)

## Canales de comunicación

- Canal oficial: [Mesa de Servicios SGD](https://gobdigitalcl.freshdesk.com/support/tickets/new)

## Capacitaciones

- Capacitaciones mensuales sobre integración de ClaveÚnica
- Inscripción: [CeroFilas](https://gobdigital.cerofilas.gob.cl/) → trámite "Inscripción a capacitaciones de productos de Gobierno Digital"

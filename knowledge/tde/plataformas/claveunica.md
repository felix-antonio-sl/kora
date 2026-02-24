---
_manifest:
  urn: urn:tde:kb:claveunica
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- clave-unica
- identidad-digital
- openid-connect
- chile
- tde
lang: es
---

# Manual de Integración de ClaveÚnica

## Contexto y Rol
- ClaveÚnica es el proveedor de identidad digital (IdP) del Estado de Chile para personas naturales.
- Basado en OpenID Connect (sobre OAuth 2.0).
- Estandariza la autenticación en múltiples plataformas públicas con una sola contraseña.


## Proceso de Solicitud de Credenciales
- Realizar trámite en https://claveunica.cerofilas.gob.cl/ usando ClaveÚnica institucional.

- **Campos**: Institución, Contacto Administrativo (nominativo), Contacto Técnico, Nombre Aplicación (visible en login), Redirect URI (callback), Logout URI.
- **Requisitos**: correos institucionales obligatorios; Redirect URI en producción debe usar dominio .gob.cl; no se permite 'localhost' en producción.
- **Entregables**: client_id y client_secret para ambientes Sandbox, QA y Producción.

## Ambientes de Integración
- **Sandbox**: pruebas iniciales con RUNs ficticios (44.444.444-4 al 99.999.999-9; clave: 'testing').
- **QA**: validación final antes de paso a producción.
- **Producción**: cuentas reales de ciudadanos; requiere certificación previa por parte de la SGD.

## Flujo Técnico OpenID Connect
### Pasos de Implementación
1. **Token State**: generar valor dinámico y aleatorio (mín. 30 chars) para prevenir ataques CSRF.
2. **Autorización (GET)**: redirigir a `https://accounts.claveunica.gob.cl/openid/authorize/` con parámetros `client_id`, `response_type=code`, `scope='openid run name'`, `redirect_uri` y `state`.
3. **Validación**: recibir `code` y `state` en el callback; comparar `state` con el generado en paso 1.
4. **Intercambio (POST)**: canjear `code` por `access_token` en `https://accounts.claveunica.gob.cl/openid/token/`. **Obligatorio ejecutar desde el backend**.
5. **Consulta Datos (POST)**: usar `access_token` en `https://accounts.claveunica.gob.cl/openid/userinfo/` para obtener RUN y nombre.
6. **Cierre Sesión**: llamar a `https://accounts.claveunica.gob.cl/api/v1/accounts/app/logout?redirect=logout_uri`.

## Requisitos de Seguridad
- **Protocolo**: HTTPS obligatorio en producción; TLS 1.2 o superior.
- **Secretos**: no exponer `client_secret` en código fuente o frontend; usar variables de entorno.
- **Interfaz**: formulario de login debe abrirse a pantalla completa; prohibido el uso de iframes o popups que oculten la URL oficial.

## Botón Oficial y Marca
- **Diseño**: usar isotipo (24px), tipografía Roboto bold, fondo #0F69C4.
- **Accesibilidad**: incluir `aria-label` descriptivo y estado `:focus` con outline de contraste.
- **Marca**: escribir siempre como "ClaveÚnica" (C y U mayúsculas). No duplicar textos informativos junto al botón.

## Certificación y Activación
- Fase obligatoria para habilitar el ambiente productivo (plazo ref:
- 6 días hábiles).

- **Checklist**: uso de HTTPS, botón oficial correcto, validación de `state`, llamadas desde backend, gestión segura de secretos y cierre de sesión funcional.
- **Procedimiento**: adjuntar evidencias de código y capturas de pantalla en el ticket de Cerofilas.

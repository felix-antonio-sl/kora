# Configuración Correo Gmail — Modo Solo Lectura + Envío Restringido

## Objetivo
1. **Recibir copia** de todo lo que llega a `felixsanhuezaluna@gmail.com` en `koraxfx@gmail.com` (sin eliminar de origen)
2. **Enviar solo** desde `koraxfx@gmail.com` hacia `felixsanhuezaluna@gmail.com` — ningún otro destinatario

---

## Parte 1: Copia de correos en `felixsanhuezaluna@gmail.com`

### Paso 1: Acceder a Settings
1. Entra a **gmail.com** con `felixsanhuezaluna@gmail.com`
2. Click en **Settings** (ícono de engranaje) → **See all settings**

### Paso 2: Configurar Forwarding
1. Busca la pestaña **Forwarding and POP/IMAP**
2. Click en **Add a forwarding address**
3. Escribe: `koraxfx@gmail.com`
4. Click **Next** → **Proceed** → **Send**
5. **No** marcar "Delete Gmail's copy" → dejar enabled para recibir copia

### Paso 3: Confirmar
- Llegará un código de verificación a `koraxfx@gmail.com`
- Ese código debes ingresarlo en Gmail para confirmar

**Resultado:** Todo correo que llegue a `felixsanhuezaluna` también llega a `koraxfx`

---

## Parte 2: Restringir envío en `koraxfx@gmail.com`

### Opción A: Filtro de envío (menos seguro, fácil)

**No hay filtro nativo** para esto en Gmail. Pero puedes:

1. **No guardar la contraseña** de koraxfx en ningún lado
2. **Solo yo tengo acceso** a la cuenta koraxfx

### Opción B: Google Workspace (más seguro, requiere pagar)

Si tienes Google Workspace:
1. Admin console → **Apps** → **Google Workspace** → **Gmail** → **End user access**
2. Configurar **Authorized Senders** — solo permitir envios desde tu dominio

### Opción C (Recomendada): Restricción manual + alerta

1. En `koraxfx@gmail.com`:
   - Ir a **Settings** → **Filters and blocked addresses**
   - Crear filtro: `to:(*) -to:felixsanhuezaluna@gmail.com` → **Delete** (no recomendado, pierdes mails)
   
2. **Mejor enfoque:** Simplemente no guardar credenciales en ningún sistema automatizado. El control es manual.

---

## Resumen técnico

| Cuenta | Acción | Cómo |
|---|---|---|
| felixsanhuezaluna@gmail.com | Forwarding | Settings → Forwarding → Add koraxfx@gmail.com → Keep |
| koraxfx@gmail.com | Lectura | Accedo yo cuando necesito |
| koraxfx@gmail.com | Envío | **Restringido** — solo desde mi acceso manual |

---

## Para que Korax pueda LEER desde koraxfx

Necesitas autenticar tu cuenta en el VPS. Puedo ayudarte a configurar el token de acceso si tienes OAuth configurado.

¿Quieres que intente conectar `gog` a `koraxfx@gmail.com` para que pueda leer los correos?
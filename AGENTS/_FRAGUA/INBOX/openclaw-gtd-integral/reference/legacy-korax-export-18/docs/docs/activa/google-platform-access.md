# Acceso Google Platform — Guía de Migración

*Documento generado: 2026-03-26*
*Propósito: replicar acceso Google (Gmail, Calendar, Drive, Docs, Sheets, Contacts, Tasks) en un nuevo servidor*

---

## 1. Arquitectura general

```
Google Cloud (korax-workspace)
  └─ Pub/Sub topic: projects/korax-workspace/topics/korax-gmail-watch
       └─ Push subscription → https://clawdbot-hetzner.tail84b159.ts.net/gmail-pubsub
                                        │
                                        ▼
                              gog gmail watch serve (:8788)
                                        │
                                   hook-url POST
                                        │
                                        ▼
                              OpenClaw gateway (:18789) /hooks/gmail
                                        │
                                        ▼
                              Hook preset "gmail" → clasifica email → Telegram
```

---

## 2. Componentes

### 2.1 gog CLI

| Campo | Valor |
|---|---|
| Binario | `/usr/local/bin/gog` (ELF x86-64, estático) |
| Versión | v0.9.0 (99d9575 2026-01-22) |
| Instalación | Binario descargado directo (no apt/npm) |
| Fuente | https://github.com/stvnksslr/gog (verificar) |

### 2.2 Cuenta Google

| Campo | Valor |
|---|---|
| Email | `koraxfx@gmail.com` |
| Client name | `default` |
| Auth type | OAuth 2.0 (installed app) |
| Creación token | 2026-02-26T17:51:46Z |

### 2.3 Scopes autorizados

```
email
openid
https://www.googleapis.com/auth/calendar
https://www.googleapis.com/auth/contacts
https://www.googleapis.com/auth/contacts.other.readonly
https://www.googleapis.com/auth/directory.readonly
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/drive
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/tasks
https://www.googleapis.com/auth/userinfo.email
```

**Nota:** NO incluye scope de Gmail (`gmail.modify` / `gmail.readonly`). El acceso Gmail funciona vía el Gmail Watch de gog que usa un scope separado.

---

## 3. Archivos y paths

### 3.1 Credenciales OAuth (client_id/client_secret)

```
~/.config/gog/credentials.json              ← OAuth client credentials (legacy/compat path)
~/.config/gogcli/credentials.json           ← OAuth client credentials (primary)
```

Ambos contienen lo mismo:
- **Project ID:** `korax-workspace`
- **Client ID:** `490503352742-ilp3ddn9j2m60tt9j6coo4mesetk7mgl.apps.googleusercontent.com`
- **Client Secret:** almacenado en el JSON (texto plano)
- **Redirect URI:** `http://localhost`

**Estos son las credenciales de la app OAuth, no del usuario.** Se generaron en Google Cloud Console → APIs & Services → Credentials → OAuth 2.0 Client IDs.

### 3.2 Tokens (refresh + access)

```
~/.config/gogcli/keyring/token:default:koraxfx@gmail.com
~/.config/gogcli/keyring/token:koraxfx@gmail.com
```

- Formato: JWT-like encriptado con PBES2-HS256+A128S1 (password-based encryption)
- **Contraseña de descifrado:** env var `GOG_KEYRING_PASSWORD`
- Contiene: `refresh_token` + `access_token` + metadata
- El access_token se renueva automáticamente con el refresh_token

### 3.3 Config

```
~/.config/gogcli/config.json
```

Contenido:
```json
{
  "keyring_backend": "file"
}
```

### 3.4 Estado Gmail Watch

```
~/.config/gogcli/state/gmail-watch/koraxfx_gmail_com.json
```

Contiene: topic, labels, historyId, expiración, último delivery status.

### 3.5 Downloads

```
~/.config/gogcli/drive-downloads/    ← archivos descargados de Drive
```

---

## 4. Variables de entorno

Definidas en `~/.openclaw/.env`:

| Variable | Propósito |
|---|---|
| `GOG_KEYRING_PASSWORD` | Descifra los tokens en keyring (PBES2) |
| `GOG_GMAIL_ACCOUNT` | Cuenta default para comandos gmail (`koraxfx@gmail.com`) |

---

## 5. Servicios systemd

### 5.1 gog-gmail-watch.service (system-level)

```ini
# /etc/systemd/system/gog-gmail-watch.service
[Unit]
Description=GOG Gmail Watch Server
After=network.target

[Service]
Type=simple
User=clawdbot
EnvironmentFile=/home/clawdbot/.openclaw/.env
ExecStart=/bin/bash -c '/usr/local/bin/gog gmail watch serve \
  --account "${GOG_GMAIL_ACCOUNT}" \
  --port 8788 \
  --path / \
  --hook-url "http://localhost:18789/hooks/gmail" \
  --hook-token "${OPENCLAW_HOOKS_TOKEN}"'
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

**Nota:** Es un servicio **system-level** (no user-level), corre como `clawdbot`.

---

## 6. Tailscale Funnel (exposición pública)

```
https://clawdbot-hetzner.tail84b159.ts.net
├── /             → proxy http://127.0.0.1:18789   (OpenClaw gateway)
└── /gmail-pubsub → proxy http://127.0.0.1:8788    (gog gmail watch serve)
```

Google Pub/Sub envía push notifications a:
`https://clawdbot-hetzner.tail84b159.ts.net/gmail-pubsub`

---

## 7. Google Cloud Console — Proyecto korax-workspace

| Recurso | Valor |
|---|---|
| Project ID | `korax-workspace` |
| Pub/Sub Topic | `projects/korax-workspace/topics/korax-gmail-watch` |
| OAuth Client | `490503352742-ilp3ddn9j2m60tt9j6coo4mesetk7mgl.apps.googleusercontent.com` |
| APIs habilitadas | Gmail API, Calendar API, Drive API, Contacts API, Docs API, Sheets API, Tasks API, People API, Pub/Sub API |

---

## 8. OpenClaw hooks config

En `openclaw.json`:

```json
{
  "hooks": {
    "enabled": true,
    "path": "/hooks",
    "token": "${OPENCLAW_HOOKS_TOKEN}",
    "defaultSessionKey": "hook:ingress",
    "allowedAgentIds": ["main"],
    "presets": ["gmail"],
    "mappings": [{
      "match": { "path": "gmail" },
      "action": "agent",
      "wakeMode": "now",
      "name": "Gmail",
      "messageTemplate": "Clasifica este email para médico urgencias + ingeniero GORE Ñuble...",
      "deliver": true,
      "channel": "telegram",
      "to": "7192195698",
      "model": "haiku"
    }],
    "gmail": {
      "account": "koraxfx@gmail.com",
      "topic": "projects/korax-workspace/topics/korax-gmail-watch",
      "pushToken": "<token-de-verificación-push>",
      "model": "haiku"
    }
  }
}
```

---

## 9. Cron jobs relacionados

### Gmail Watch Renew Check
- **ID:** `b00a3925-6a60-4083-8a97-5488aabc55a1`
- **Schedule:** `0 11 */6 * *` (cada 6 días, 11:00 Chile)
- **Acción:** Verifica expiración del watch y renueva si <48h

### Alertas diarias #alertas (Slack)
- **ID:** `d3e14a7b-4eed-4105-9a00-dfc69ee926e7`
- **Schedule:** `0 8 * * 1-5` (L-V 08:00 Chile)
- **Acción:** Chequea INBOX, WAITING, email urgente, calendar turnos

---

## 10. Procedimiento de migración a nuevo servidor

### Paso 1: Instalar gog

```bash
# Descargar binario (verificar última versión)
curl -Lo /usr/local/bin/gog https://github.com/stvnksslr/gog/releases/latest/download/gog-linux-amd64
chmod +x /usr/local/bin/gog
```

### Paso 2: Copiar credenciales y tokens

```bash
# Directorios a copiar íntegros:
rsync -av ~/.config/gog/ nuevo-server:~/.config/gog/
rsync -av ~/.config/gogcli/ nuevo-server:~/.config/gogcli/
```

### Paso 3: Variables de entorno

Agregar a `~/.openclaw/.env` del nuevo servidor:
```bash
GOG_KEYRING_PASSWORD=<mismo-password>
GOG_GMAIL_ACCOUNT=koraxfx@gmail.com
```

### Paso 4: Verificar acceso

```bash
gog auth list
gog gmail messages search "in:inbox" --account koraxfx@gmail.com --limit 1
gog calendar list --account koraxfx@gmail.com --limit 1
gog drive list --account koraxfx@gmail.com --limit 1
```

### Paso 5: Instalar servicio Gmail Watch

1. Copiar `/etc/systemd/system/gog-gmail-watch.service`
2. `sudo systemctl daemon-reload && sudo systemctl enable --now gog-gmail-watch`

### Paso 6: Actualizar Pub/Sub push endpoint

En Google Cloud Console → Pub/Sub → Subscriptions:
- Cambiar push endpoint URL al nuevo Tailscale Funnel o dominio público
- O renovar watch: `gog gmail watch renew --account koraxfx@gmail.com`

### Paso 7: Configurar Tailscale Funnel (si aplica)

```bash
tailscale funnel --bg --set-path /gmail-pubsub http://127.0.0.1:8788
tailscale funnel --bg --set-path / http://127.0.0.1:18789
```

### Paso 8: OpenClaw hooks

Copiar la sección `hooks` completa del `openclaw.json` (sección 8 de este doc).

---

## 11. Re-autenticación (si tokens expiran)

Si el refresh_token expira o se invalida:

```bash
# Re-autorizar con todos los scopes
gog auth add koraxfx@gmail.com \
  --scopes "email,openid,calendar,contacts,contacts.other.readonly,directory.readonly,documents,drive,spreadsheets,tasks,userinfo.email"
```

Esto abrirá un browser para OAuth consent. En VPS sin browser:
1. Ejecutar en una máquina con browser
2. O usar `--no-browser` si gog lo soporta (verificar)
3. O copiar el URL de auth y completar manualmente

**IMPORTANTE:** El proyecto OAuth está en modo "Testing" en Google Cloud. Si pasan >7 días sin uso, Google puede revocar el refresh_token. El proyecto `korax-workspace` debería estar en producción para tokens permanentes.

---

## 12. Estado actual (2026-03-26)

| Componente | Estado |
|---|---|
| gog CLI | ✅ Operativo, v0.9.0 |
| OAuth token | ✅ Válido (creado 2026-02-26) |
| Gmail Watch | ⚠️ Expirado (2026-03-15). Se renueva automáticamente vía cron |
| Watch serve | ✅ Running (PID 519037, 18 días uptime) |
| Push delivery | ✅ Último: 2026-03-26T08:59:44Z, status: ok |
| Calendar | ✅ Operativo |
| Drive | ✅ Operativo |
| Contacts | ✅ Operativo |

---

## 13. Notas de seguridad

- **Client secret** está en texto plano en `credentials.json` — es un OAuth "installed app" (public client), el secret no es realmente secreto según Google
- **Refresh token** está encriptado con `GOG_KEYRING_PASSWORD` — proteger esta variable
- **Hooks token** (`OPENCLAW_HOOKS_TOKEN`) autentica los POST de gog → OpenClaw — debe coincidir en ambos lados
- **Push token** en hooks.gmail.pushToken verifica que los push de Google son legítimos

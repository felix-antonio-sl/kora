# Tutorial: Asistente IA Personal con Acceso a Google Workspace

*Versión: 1.0 — 2026-04-01*
*Construido sobre la experiencia de Korax (clawdbot + OpenClaw + gog + Telegram)*

---

## Propósito

Este tutorial te guía paso a paso para construir un asistente IA personalizado — como **Korax** — que:

- Lee y clasifica tu Gmail automáticamente
- Accede a Google Calendar, Drive, Docs, Sheets, Contacts y Tasks
- Te notifica por Telegram con resúmenes actionable
- Funciona 24/7 en un VPS Linux (o tu propio servidor)
- Se controla porchat (no necesitas UI gráfica)

**Tiempo estimado de configuración:** 3–6 horas (dependiendo de tu experiencia).

**Costo:** $0–$15/mes (VPS básico desde $5/mes).

---

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────┐
│  GOOGLE CLOUD                                           │
│  ┌──────────┐    push notification                      │
│  │  Gmail   │────────────────────────────────────────►  │
│  │  Watch   │                                          │
│  └──────────┘                                          │
│       │                                                 │
│       ▼                                                 │
│  Pub/Sub topic  ─────────────────────────────────────►  │
└─────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│  TU VPS / SERVIDOR                                      │
│                                                         │
│  ┌──────────────┐   ┌────────────────┐   ┌───────────┐ │
│  │  gog         │   │  OpenClaw      │   │  systemd  │ │
│  │  gmail watch │──►│  Gateway       │◄──│  services │ │
│  │  serve :8788 │   │  :18789        │   │           │ │
│  └──────────────┘   └───────┬────────┘   └───────────┘ │
│                             │                           │
│                             ▼                           │
│                    ┌────────────────┐                   │
│                    │  Tailscale     │                   │
│                    │  Funnel (HTTPS)│                   │
│                    └───────┬────────┘                   │
└────────────────────────────│────────────────────────────┘
                             │ HTTPS
                             ▼
              ┌──────────────────────────┐
              │  TELEGRAM                 │
              │  Notificaciones + chat   │
              └──────────────────────────┘
```

**Flujo de datos:**

1. Llega un email → Gmail Watch → Pub/Sub push
2. `gog gmail watch serve` recibe el push en `:8788`
3. Forward a OpenClaw gateway `hooks/gmail`
4. OpenClaw clasifica con haiku → envía notificación Telegram
5. Tú respondes por chat → OpenClaw procesa con Sonnet

---

## 1. Requisitos Previos

### Hardware / VPS
| Opción | Proveedor | Spec | Precio aprox. |
|--------|-----------|------|---------------|
| Recomendado | Hetzner Cloud (CPX21) | 4 vCPU, 4GB RAM, 80GB SSD | €5–6/mes |
| Alternativa | Contabo, Oracle Free Tier, DigitalOcean | 2+ vCPU, 2GB+ RAM | $5–20/mes |
| Mínimo | Raspberry Pi 5 +tailscale | 4GB RAM, Ubuntu Server | ~$50 uno-time |

**Nota:** Korax corre en Hetzner Cloud (Ubuntu 24.04 LTS).

### Software base
- Ubuntu 24.04 LTS (o Debian 12+)
- Usuario no-root con sudo (no root directo)
- Dominio o subdominio (opcional, pero recomendado para HTTPS)

### Cuentas
| Servicio | Necesario | Notas |
|----------|-----------|-------|
| Google account | ✅ | Gmail + Workspace (Drive, Calendar, etc.) |
| Telegram | ✅ | Bot + tu usuario como allowed sender |
| OpenClaw | ✅ | Framework del asistente |
| Tailscale | Recomendado | Acceso remoto seguro + Funnel HTTPS |
| GitHub | Opcional | Para código y backup de configs |

### Conocimientos
- Línea de comandos Linux (básico-intermedio)
- Conceptos de OAuth 2.0 (sabés qué es un refresh token)
- Editor de texto (nano, vim, o código)
- No necesitás saber programar para seguir este tutorial

---

## 2. Configurar Google Cloud (Proyecto OAuth)

Este paso crea la app OAuth que conecta `gog` con tu cuenta Google.

### 2.1 Crear proyecto en Google Cloud Console

1. Ve a [console.cloud.google.com](https://console.cloud.google.com)
2. Click **"Select a project"** → **"New Project"**
3. Nombre: `tu-asistente` (o lo que quieras)
4. Billing: asociar si es necesario (APIs son gratuitas bajo cuota)
5. Click **Create**

### 2.2 Habilitar APIs

Ve a **APIs & Services → Library** y habilita estas:

```
✅ Gmail API
✅ Google Calendar API
✅ Google Drive API
✅ Google Docs API
✅ Google Sheets API
✅ Contacts API (People API)
✅ Google Tasks API
✅ Pub/Sub API (para Gmail Watch push)
```

### 2.3 Crear credenciales OAuth 2.0

1. Ve a **APIs & Services → Credentials**
2. Click **"+ CREATE CREDENTIALS"** → **"OAuth client ID"**
3. Application type: **"Desktop app"**
4. Nombre: `gog-cli`
5. Click **Create**
6. **Guarda el Client ID y Client Secret** (los vas a necesitar)

### 2.4 Configurar pantalla de consentimiento OAuth

1. Ve a **APIs & Services → OAuth consent screen**
2. User Type: **External**
3. App name: `Tu Asistente IA`
4. Email: tu cuenta Google
5. Scopes: click **"Add or Remove Scopes"** y agrega:
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
6. Test users: agrega tu cuenta Google
7. Publish: **"Make app"** (o mantener en Testing si preferís)

---

## 3. Instalar gog CLI (Google Workspace CLI)

`gog` es la herramienta CLI que maneja toda la comunicación con las APIs de Google.

### 3.1 Descargar e instalar

```bash
# Crear usuario del servicio (recomendado, no correr como root)
sudo useradd -r -m -s /bin/false goguser 2>/dev/null || true

# Descargar última versión (verificar en https://github.com/stvnksslr/gog/releases)
curl -Lo /usr/local/bin/gog https://github.com/stvnksslr/gog/releases/latest/download/gog-linux-amd64
chmod +x /usr/local/bin/gog

# Verificar instalación
gog --version
```

### 3.2 Crear estructura de directorios

```bash
mkdir -p ~/.config/gogcli
mkdir -p ~/.config/gogcli/keyring
mkdir -p ~/.config/gogcli/state/gmail-watch
mkdir -p ~/.config/gogcli/drive-downloads
```

### 3.3 Guardar credenciales OAuth

Crea el archivo `~/.config/gogcli/credentials.json`:

```json
{
  "installed": {
    "client_id": "TU_CLIENT_ID.apps.googleusercontent.com",
    "client_secret": "TU_CLIENT_SECRET",
    "redirect_uris": ["http://localhost"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
  }
}
```

**Reemplaza** `TU_CLIENT_ID` y `TU_CLIENT_SECRET` con los valores del paso 2.3.

También copiá el mismo contenido a `~/.config/gog/credentials.json` (compatibilidad).

### 3.4 Autorizar con tu cuenta Google

```bash
# Ejecutar el flujo OAuth
gog auth add TU_CORREO@gmail.com \
  --scopes "email,openid,calendar,contacts,contacts.other.readonly,directory.readonly,documents,drive,spreadsheets,tasks,userinfo.email"
```

Esto va a:
1. Mostrar un URL en la terminal
2. Abrir ese URL en tu browser (o copiarlo manualmente)
3. Autorizar la app
4. Mostrar un código
5. Ingresar el código en la terminal

**En VPS sin browser:** copiá el URL, pegalo en tu navegador local, autorizá, copiá el código, volvé a la terminal.

### 3.5 Configurar keyring (encriptación de tokens)

`gog` encripta los tokens con una contraseña. Definila como variable de entorno:

```bash
# Agregar a ~/.bashrc o ~/.zshrc
echo 'export GOG_KEYRING_PASSWORD="una_contraseña_segura_larga"' >> ~/.bashrc
echo 'export GOG_GMAIL_ACCOUNT="TU_CORREO@gmail.com"' >> ~/.bashrc
source ~/.bashrc
```

**Guarda esta contraseña** — si la perdés, tenés que re-autenticar.

### 3.6 Configurar gog

Crea `~/.config/gogcli/config.json`:

```json
{
  "keyring_backend": "file"
}
```

### 3.7 Verificar acceso

```bash
export GOG_KEYRING_PASSWORD="tu_contraseña"
gog auth list
gog gmail messages search "in:inbox" --account TU_CORREO@gmail.com --limit 3
gog calendar list --account TU_CORREO@gmail.com --limit 3
gog drive list --account TU_CORREO@gmail.com --limit 3
```

Si todo responde con datos → gog está funcionando. ✅

---

## 4. Instalar OpenClaw

OpenClaw es el framework que orquesta el asistente: chat, cron, hooks, memoria, y model routing.

### 4.1 Requisitos de sistema

```bash
# Node.js 18+ (OpenClaw requiere Node)
node --version   # debe ser >= 18
npm --version
```

Si no tenés Node:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 4.2 Instalar OpenClaw

```bash
# Instalar globalmente (NUNCA con sudo)
npm install -g openclaw

# Verificar
openclaw --version
```

### 4.3 Inicializar el gateway

```bash
# Ejecutar como el usuario que va a correr el servicio (ej: tu usuario, no root)
openclaw gateway install
```

Esto crea:
- `~/.openclaw/` (configuración)
- Servicio systemd user-level
- Puerto default: `18789`

### 4.4 Configurar acceso a modelos IA

Editá `~/.openclaw/openclaw.json`. Aquí un ejemplo mínimo funcional:

```json
{
  "gateway": {
    "port": 18789,
    "bind": "loopback"
  },
  "models": {
    "providers": {
      "openrouter": {
        "apiKey": "sk-or-v1-TU_KEY"
      },
      "openai": {
        "apiKey": "sk-TU_KEY"
      }
    },
    "defaults": {
      "chat": "openrouter/anthropic/claude-sonnet-4-6",
      "haiku": "openrouter/anthropic/claude-haiku-4-5",
      "opus": "openrouter/anthropic/claude-opus-4-6"
    }
  },
  "agents": {
    "main": {
      "model": "chat",
      "thinking": "adaptive"
    }
  }
}
```

**Proveedores de modelos gratuitos o económicos:**

| Proveedor | Modelos | API Key |
|-----------|---------|---------|
| OpenRouter | Claude, GPT, Gemini, Mistral | [openrouter.ai/keys](https://openrouter.ai/keys) |
| Kilo.ai (gateway) | kimi (262K ctx), glm-5 (200K) | api.kilo.ai/api/gateway |
| Groq | Llama, Mixtral (fast) | [console.groq.com](https://console.groq.com) |

### 4.5 Variables de entorno

Crea/editar `~/.openclaw/.env`:

```bash
# Modelos
OPENROUTER_API_KEY=sk-or-v1-TU_KEY
KILO_GATEWAY=https://api.kilo.ai/api/gateway

# gog (Google Workspace)
GOG_KEYRING_PASSWORD=tu_contraseña_del_keyring
GOG_GMAIL_ACCOUNT=TU_CORREO@gmail.com

# Hooks (verificación de requests entrantes)
OPENCLAW_HOOKS_TOKEN=token_aleatorio_secreto_32_chars
```

Generar token seguro:

```bash
openssl rand -hex 16
```

### 4.6 Arrancar el gateway

```bash
# Iniciar como servicio user-level
openclaw gateway start

# Ver estado
openclaw gateway status

# Ver logs
journalctl --user -u openclaw-gateway -f
```

---

## 5. Configurar Telegram como Canal

### 5.1 Crear un bot de Telegram

1. Abrí Telegram → buscá **@BotFather**
2. Enviar `/newbot`
3. Nombre del bot: `TuAsistenteBot`
4. Username: `tu_asistente_bot` (tiene que terminar en `bot`)
5. Guardar el **HTTP API token** que BotFather entrega

### 5.2 Configurar Telegram en OpenClaw

Editá `~/.openclaw/openclaw.json`, sección `channels`:

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "TU_BOT_TOKEN",
      "allowedSenders": ["TU_NUMERO_TELEGRAM"],
      "polling": {
        "autoSetup": true
      }
    }
  }
}
```

**¿Cómo saber tu número Telegram?**
- Hablá con **@userinfobot** o **@getidsbot** en Telegram
- Te da tu chat ID (número largo)

### 5.3 Permitir que Korax te notifique

Agregá tu número Telegram al allowlist. En `channels.telegram.allowedSenders` poné tu chat ID (número, sin guiones).

### 5.4 Reiniciar y verificar

```bash
openclaw gateway restart
```

En Telegram, buscá tu bot y enviale `/start`. Debería responder.

---

## 6. Configurar Gmail Watch (Notificaciones en Tiempo Real)

El Gmail Watch permite que tu asistente reciba emails en tiempo real, no solo consultarlos periódicamente.

### 6.1 Crear tema Pub/Sub

1. Ve a Google Cloud Console → **Pub/Sub → Topics**
2. Click **"+ CREATE TOPIC"**
3. Topic ID: `tu-asistente-gmail-watch`
4. Click **Create**

### 6.2 Configurar Gmail Watch

```bash
export GOG_KEYRING_PASSWORD="tu_contraseña"

# Verificar que funciona
gog gmail watch status --account TU_CORREO@gmail.com

# Crear/eliminarr watch
gog gmail watch create --account TU_CORREO@gmail.com \
  --topic projects/TU_PROJECT_ID/topics/tu-asistente-gmail-watch
```

### 6.3 Crear servicio systemd para gog watch serve

Este servicio mantiene un servidor HTTP esperando los push de Pub/Sub.

Creá `/etc/systemd/system/gog-gmail-watch.service` (sudo):

```ini
[Unit]
Description=GOG Gmail Watch Server
After=network.target

[Service]
Type=simple
User=TU_USUARIO
EnvironmentFile=/home/TU_USUARIO/.openclaw/.env
ExecStart=/bin/bash -c '/usr/local/bin/gog gmail watch serve \
  --account "${GOG_GMAIL_ACCOUNT}" \
  --port 8788 \
  --path / \
  --hook-url "http://127.0.0.1:18789/hooks/gmail" \
  --hook-token "${OPENCLAW_HOOKS_TOKEN}"'
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gog-gmail-watch
sudo systemctl status gog-gmail-watch
```

### 6.4 Verificar watch

```bash
# Enviar un email de prueba a tu cuenta
# Luego verificar
gog gmail watch status --account TU_CORREO@gmail.com
journalctl --user -u openclaw-gateway | grep -i gmail
```

---

## 7. Configurar OpenClaw Hooks (Recibir Emails)

Editá `~/.openclaw/openclaw.json`, sección `hooks`:

```json
{
  "hooks": {
    "enabled": true,
    "path": "/hooks",
    "token": "token_aleatorio_que_definiste",
    "defaultSessionKey": "hook:ingress",
    "allowedAgentIds": ["main"],
    "presets": ["gmail"],
    "mappings": [
      {
        "match": { "path": "gmail" },
        "action": "agent",
        "wakeMode": "now",
        "name": "Gmail",
        "messageTemplate": "Clasifica este email: quién lo envía, urgencia (inmediato/hoy/semana/bajo/ruido), y un resumen de 1 línea.",
        "deliver": true,
        "channel": "telegram",
        "to": "TU_CHAT_ID",
        "model": "haiku"
      }
    ],
    "gmail": {
      "account": "TU_CORREO@gmail.com",
      "topic": "projects/TU_PROJECT_ID/topics/tu-asistente-gmail-watch",
      "pushToken": "token_de_verificacion_opcional",
      "model": "haiku"
    }
  }
}
```

Reiniciar gateway:

```bash
openclaw gateway restart
```

---

## 8. Configurar HTTPS con Tailscale Funnel

Tailscale Funnel expone tu gateway como HTTPS públicamente, necesario para que Google Pub/Sub pueda enviarte push notifications.

### 8.1 Instalar y autenticar Tailscale

```bash
# Instalar Tailscale
curl -fsSL https://tailscale.com/install.sh | sh

# Autenticar (te da un URL)
sudo tailscale up
```

### 8.2 Habilitar Funnel

```bash
# Exponer gateway OpenClaw
sudo tailscale funnel --bg 127.0.0.1:18789

# Exponer gog watch serve
sudo tailscale funnel --bg --set-path /gmail-pubsub 127.0.0.1:8788
```

### 8.3 Verificar URLs

```bash
tailscale funnel status
```

Vas a ver algo como:
```
https://tu-nombre.tailXYZ.ts.net/
https://tu-nombre.tailXYZ.ts.net/gmail-pubsub
```

### 8.4 Actualizar Pub/Sub push endpoint

Volvé a Google Cloud Console → Pub/Sub → tu topic → suscripción push:
- Push endpoint: `https://tu-nombre.tailXYZ.ts.net/gmail-pubsub`

---

## 9. Comandos gog de Referencia Rápida

Una vez configurado todo, estos son los comandos que el asistente usa:

### Gmail
```bash
# Buscar emails
gog gmail messages search "in:inbox is:unread" --account TU_CORREO@gmail.com --limit 10

# Ver contenido de un email
gog gmail messages view MESSAGE_ID --account TU_CORREO@gmail.com

# Enviar email
gog gmail messages send --account TU_CORREO@gmail.com \
  --to destinatario@gmail.com \
  --subject "Asunto" \
  --body "Cuerpo del mensaje"

# Responder
gog gmail messages reply MESSAGE_ID --account TU_CORREO@gmail.com \
  --body "Mi respuesta"
```

### Calendar
```bash
# Próximos eventos
gog calendar list --account TU_CORREO@gmail.com --limit 10

# Crear evento
gog calendar events create --account TU_CORREO@gmail.com \
  --summary "Reunión" \
  --start "2026-04-05T10:00:00" \
  --end "2026-04-05T11:00:00" \
  --description "Detalles"

# Buscar eventos
gog calendar events search "reunión" --account TU_CORREO@gmail.com --limit 5
```

### Drive
```bash
# Listar archivos
gog drive list --account TU_CORREO@gmail.com --limit 10

# Buscar archivo
gog drive search "nombre del archivo" --account TU_CORREO@gmail.com

# Descargar archivo
gog drive download FILE_ID --account TU_CORREO@gmail.com --out /tmp/archivo.pdf

# Subir archivo
gog drive upload /tmp/archivo.pdf --account TU_CORREO@gmail.com --parent FOLDER_ID
```

### Contacts
```bash
# Buscar contacto
gog contacts search "Juan" --account TU_CORREO@gmail.com --limit 5

# Listar contactos recientes
gog contacts list --account TU_CORREO@gmail.com --limit 10
```

### Tasks
```bash
# Listar tareas
gog tasks list --account TU_CORREO@gmail.com --limit 10

# Crear tarea
gog tasks create --account TU_CORREO@gmail.com \
  --title "Tarea importante" \
  --due "2026-04-10"
```

---

## 10. Configurar Automatizaciones (Cron Jobs)

### 10.1 Heartbeat (verificación periódica)

```bash
# Crear cron para chequear emails no leídos cada 30 min
openclaw cron add \
  --name "gmail-check" \
  --schedule "*/30 * * * *" \
  --session "isolated" \
  --message "Ejecutar heartbeat: verificar INBOX, emails no leídos, eventos próximos. Notificar si hay algo urgente."
```

### 10.2 Resumen matutino

```bash
# L-V a las 8:00 AM Chile (UTC-3)
openclaw cron add \
  --name "morning-brief" \
  --schedule "0 8 * * 1-5" \
  --session "isolated" \
  --message "Resumen matutino: 3 emails más importantes del día, próximos 3 eventos del calendario, tarea más urgente."
```

### 10.3 Verificar renew Gmail Watch

```bash
# Cada 5 días
openclaw cron add \
  --name "gmail-watch-renew" \
  --schedule "0 11 */5 * *" \
  --session "isolated" \
  --message "Verificar estado del Gmail Watch. Si expira en <48h, renovar con: gog gmail watch renew --account TU_CORREO@gmail.com"
```

### 10.4 Listar cron jobs

```bash
openclaw cron list
```

---

## 11. Estructura de Archivos Final (Resumen)

```
$HOME/
├── .openclaw/
│   ├── .env                    # Variables (tokens, passwords)
│   └── openclaw.json          # Configuración completa
├── .config/
│   ├── gog/
│   │   └── credentials.json   # OAuth client credentials
│   └── gogcli/
│       ├── credentials.json    # OAuth client credentials
│       ├── config.json        # {"keyring_backend": "file"}
│       ├── keyring/           # Tokens encriptados
│       └── state/gmail-watch/ # Estado del watch
└── .local/bin/ (o /usr/local/bin/)
    └── gog                    # Binario gog
```

```
/etc/systemd/system/
└── gog-gmail-watch.service   # Servicio systemd (system-level)
```

---

## 12. Checklist de Verificación

Ejecutá estos comandos para confirmar que todo funciona:

```bash
# 1. gog autenticado
gog auth list

# 2. Gmail accesible
gog gmail messages search "in:inbox" --account TU_CORREO@gmail.com --limit 1

# 3. Calendar accesible
gog calendar list --account TU_CORREO@gmail.com --limit 1

# 4. Drive accesible
gog drive list --account TU_CORREO@gmail.com --limit 1

# 5. OpenClaw corriendo
openclaw gateway status

# 6. Telegram bot responde
curl http://localhost:18789/health

# 7. gog watch serve corriendo
sudo systemctl status gog-gmail-watch

# 8. Tailscale funnel activo
tailscale funnel status

# 9. Enviar email de prueba → llega notificación Telegram
```

---

## 13. Problemas Comunes y Soluciones

### "gog: command not found"
```bash
which gog
# Si no está, verificar que /usr/local/bin esté en PATH
echo $PATH
# O reinstalar:
curl -Lo /usr/local/bin/gog https://github.com/stvnksslr/gog/releases/latest/download/gog-linux-amd64
chmod +x /usr/local/bin/gog
```

### "Token expired" o "Refresh token invalid"
```bash
# Re-autenticar
gog auth add TU_CORREO@gmail.com --scopes "email,openid,calendar,..."
```

### "Gmail Watch expired"
```bash
gog gmail watch status --account TU_CORREO@gmail.com
# Si está expirado:
gog gmail watch create --account TU_CORREO@gmail.com --topic projects/TU_PROJECT/topics/tu-topic
```

### OpenClaw no inicia
```bash
openclaw gateway stop
openclaw gateway start --verbose
# Revisar logs
journalctl --user -u openclaw-gateway -f
```

### Telegram no recibe mensajes
- Verificar `allowedSenders` en config (¿tu chat ID está correcto?)
- ¿El bot está activo? Hablá con `@BotFather` → `/mybots`
- Reiniciar: `openclaw gateway restart`

### Pub/Sub push no llega
- ¿El URL del push endpoint es HTTPS? (Google no acepta HTTP plano)
- ¿Tailscale Funnel está activo? `tailscale funnel status`
- ¿El topic de Pub/Sub tiene suscripción push?
- Test manual: `curl -X POST http://localhost:8788/hook-test`

---

## 14. Recursos

| Recurso | URL |
|---------|-----|
| OpenClaw docs | [docs.openclaw.ai](https://docs.openclaw.ai) |
| OpenClaw source | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) |
| gog CLI | [github.com/stvnksslr/gog](https://github.com/stvnksslr/gog) |
| gog releases | [github.com/stvnksslr/gog/releases](https://github.com/stvnksslr/gog/releases) |
| Tailscale | [tailscale.com](https://tailscale.com) |
| Google Cloud Console | [console.cloud.google.com](https://console.cloud.google.com) |
| OpenRouter (modelos) | [openrouter.ai](https://openrouter.ai) |
| Kilo Gateway (modelos free) | [api.kilo.ai](https://api.kilo.ai) |
| BotFather (Telegram) | [@BotFather](https://t.me/BotFather) |

---

## 15. Próximos Pasos (Personalización)

Una vez que tenés el sistema básico funcionando:

1. **Configurar skills** — Skills de OpenClaw como `/inbox`, `/triaje`, `/plan` para GTD personal
2. **Integrar sistemas clínicos** — Si trabajás en salud, conectar DAU/SGH con el skill `dau-sgh`
3. **Agentes especializados** — Crear sub-agentes para dominios específicos (médico, legal, etc.)
4. **Slack u otros canales** — Agregar Slack, Discord, o WhatsApp como canales adicionales
5. **Memoria persistente** — Configurar `MEMORY.md` y búsqueda semántica
6. **Voice/TTS** — Habilitar respuestas de voz

---

*Este documento es una guía práctica basada en la configuración real de Korax funcionando en producción. Si algo no funciona o está desactualizado, verificá las URLs de los proyectos originales.*

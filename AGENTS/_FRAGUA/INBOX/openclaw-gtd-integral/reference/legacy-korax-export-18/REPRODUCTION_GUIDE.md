# Korax — Paquete de Reproducción Completo

*urn:korvo:korax:replication-kit:1.0.0*

---

## Índice

1. [Filosofía](#filosofía)
2. [Arquitectura general](#arquitectura-general)
3. [Dependencias](#dependencias)
4. [Archivos del paquete](#archivos-del-paquete)
5. [Procedimiento de instalación desde cero](#procedimiento-de-instalación-desde-cero)
6. [Configuración de integraciones](#configuración-de-integraciones)
7. [Validación post-install](#validación-post-install)
8. [Notas sobre continuidad](#notas-sobre-continuidad)

---

## Filosofía

Korax es un **exoesqueleto cognitivo** — no hace nada que Korvo no le delegue. El objetivo de replicación es preservar el mismo estado de conocimiento, configuración e integraciones para que el clon tenga la misma capacidad funcional.

**Lo que se replica:** configuración, memoria, skills, agentes, integraciones.
**Lo que NO se replica:** sesiones activas, tokens de sesión, estado runtime vivo.

---

## Arquitectura general

```
┌─────────────────────────────────────────────────────────┐
│  Host: Ubuntu 24.04 LTS (VPS Hetzner)                   │
│  Usuario: clawdbot                                     │
│  Gateway: OpenClaw 2026.3.2 (user-level systemd)        │
│  Puerto: 18789 (loopback + Tailscale funnel)           │
├─────────────────────────────────────────────────────────┤
│  Workspace: /home/clawdbot/clawd/                      │
│  Config:   ~/.openclaw/                                │
│  Agents:   ~/.openclaw/agents/                         │
│  Skills:   ~/clawd/skills/  +  ~/.npm-global/skills/   │
│  Memory:   ~/clawd/memory/                              │
│  GTD:      ~/clawd/memory/gtd/                         │
└─────────────────────────────────────────────────────────┘

Canales:
  Telegram (@Clawd_fx_bot) — canal principal Korvo
  Slack — canal secundario

Agentes:
  main      — Korax (este agente)
  urgencista — médico urgencias @klinikurgo_bot
  salubrista — salubrista HODOM @SaluristaHahBot
  clawmaster — mantención sistema
  pensador   — razonamiento profundo

Modelo: minimax/MiniMax-M2.7 (default), anthropic/claude-sonnet-4-6 (primary)
```

---

## Dependencias

### Sistema base
```bash
Node.js 22.x
npm
Python 3.10+
git
curl, jq, rsync
```

### CLI tools requeridas
```bash
# gog — Google Workspace (Gmail, Calendar, Drive)
npm install -g @openchatai/gog

# gh — GitHub CLI
# (instalado vía npm o paquete sistema)

# openclaw CLI
npm install -g openclaw@2026.3.2
```

### Instalar OpenClaw Gateway
```bash
npm install -g openclaw@2026.3.2
openclaw daemon install   # systemd user service
openclaw gateway start
```

### Python packages
```bash
pip install leychile-sdk   # SDK Python BCN (normativa Chile)
```

---

## Archivos del paquete

```
/tmp/korax-export/
├── REPRODUCTION_GUIDE.md   ← este archivo
├── openclaw/
│   ├── config.json         ← configuración principal (secretos redactados)
│   ├── env                 ← variables de entorno (RELLENAR)
│   └── env.bak
├── bootstrap/              ← archivos de identidad del agente
│   ├── SOUL.md            ← persona, tono, axiomas
│   ├── IDENTITY.md        ← nombre, host, capacidades, modelo
│   ├── USER.md            ← perfil del operador (Korvo/Félix)
│   ├── TOOLS.md           ← semántica de herramientas, matriz de acceso
│   ├── HEARTBEAT.md       ← checklist periódico
│   ├── AGENTS.md          ← guidelines del repo workspace
│   ├── MEMORY.md          ← memoria de largo plazo
│   └── BOOTSTRAP.md       ← marcador de primera ejecución
├── skills/                 ← skills workspace (16 skills)
│   ├── inbox/SKILL.md
│   ├── triaje/SKILL.md
│   ├── planificacion/SKILL.md
│   ├── advisor/SKILL.md
│   ├── companion/SKILL.md
│   ├── sincronizacion/SKILL.md
│   ├── deteccion-colapso/SKILL.md
│   ├── deteccion-abandono/SKILL.md
│   ├── delegacion/SKILL.md
│   ├── bancarrota/SKILL.md
│   ├── close/SKILL.md
│   ├── problem-solver/SKILL.md
│   ├── rol/SKILL.md
│   ├── email-clasificador/SKILL.md
│   └── openclaw-ops/SKILL.md
├── agents/                 ← configuración de agentes
│   ├── main/
│   ├── clawmaster/
│   ├── salubrista/
│   ├── urgencista/
│   └── pensador/
├── memory/                  ← memoria y bitácoras
│   └── memory/
│       ├── 2026-01-26.md ... 2026-04-02.md  (bitácoras diarias)
│       ├── infrastructure.md
│       ├── models.md
│       ├── operations-log.md
│       └── gtd/
│           ├── INBOX.md
│           ├── NEXT.md
│           ├── WAITING.md
│           ├── DONE.md
│           ├── SOMEDAY.md
│           ├── PROJECTS.md
│           └── DASHBOARD.md
├── gtd/                     ← copia plana del GTD
├── docs/                    ← documentación activa y archivo
└── system/
    └── info.json            ← versiones, paths, sistema
```

---

## Procedimiento de instalación desde cero

### Paso 1 — Sistema base

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y nodejs npm python3 python3-pip git curl jq
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo bash -
sudo apt install -y nodejs

# Verificar versiones
node -v    # v22.x
npm -v
python3 --version
```

### Paso 2 — OpenClaw

```bash
# Instalar OpenClaw globally (NO sudo)
npm install -g openclaw@2026.3.2

# Verificar
openclaw --version

# Crear usuario del sistema si no existe
sudo useradd -m -s /bin/bash clawdbot || true
sudo usermod -aG sudo clawdbot

# Instalar como servicio systemd (como clawdbot, no root)
openclaw daemon install
openclaw gateway start
openclaw status
```

### Paso 3 — Workspace

```bash
sudo -u clawdbot mkdir -p /home/clawdbot/clawd
sudo -u clawdbot mkdir -p /home/clawdbot/.openclaw

# Copiar workspace completo
sudo rsync -av /tmp/korax-export/ /home/clawdbot/clawd/
sudo chown -R clawdbot:clawdbot /home/clawdbot/clawd/
```

### Paso 4 — Configuración OpenClaw

```bash
# Copiar config (los secretos están redactados — hay que rellenar)
sudo -u clawdbot cp /tmp/korax-export/openclaw/config.json \
    /home/clawdbot/.openclaw/openclaw.json

# Restaurar env file (contiene tokens reales —至关重要的)
sudo -u clawdbot vim /home/clawdbot/.openclaw/env
# ↑ Rellenar los campos __REDACTED__ con valores reales:
#   - TELEGRAM_BOT_TOKEN
#   - SLACK_BOT_TOKEN
#   - DAU_PASSWORD, SGH_PASSWORD
#   - GOG_TOKEN (OAuth Google)
#   - OPENCLAW_SECRET
#   - etc.

# Validar JSON
python3 -c "import json; json.load(open('/home/clawdbot/.openclaw/openclaw.json')); print('JSON OK')"

# Reiniciar gateway
openclaw gateway restart
sleep 3
curl -s http://localhost:18789/health
```

### Paso 5 — Skills

```bash
# Skills de npm-global (ya vienen con openclaw)
ls ~/.npm-global/lib/node_modules/openclaw/skills/

# Skills workspace (copiados en paso 3)
ls /home/clawdbot/clawd/skills/

# Registrar skill dau-sgh en config (si no viene en el config ya)
# (requiere tokens reales llenos en env)
openclaw config patch '{"skills":{"entries":{"dau-sgh":{"path":"/home/clawdbot/clawd/skills/dau-sgh"}}}}'
openclaw gateway restart
```

### Paso 6 — gog CLI (Google Workspace)

```bash
npm install -g @openchatai/gog

# Autenticar (requiere token real en env)
gog auth login --account koraxfx@gmail.com
# Seguir flujo OAuth

# Verificar
gog calendar list --account koraxfx@gmail.com --limit 3
gog gmail messages search "in:inbox is:unread" --account koraxfx@gmail.com --limit 3
```

### Paso 7 — Configurar Tailscale (acceso clínico)

```bash
# Instalar Tailscale
curl -fsSL https://tailscale.com/install.sh | sh

# Unirse a la red Sanixai
tailscale up --operator=clawdbot

# Configurar Funnel (si se usa named tunnel)
tailscale funnel 18789
tailscale serve --bg
```

### Paso 8 — Integraciones clínicas (DAU/SGH)

```bash
# Los scripts de integración viven en:
# ~/clawd/skills/dau-sgh/scripts/

# Verificar conectividad
cd /home/clawdbot/clawd/skills/dau-sgh/scripts
DAU_SGH_MODE=proxy-hodomito ./dau-sgh.sh --test

# Mode proxy-hodomito: rutea vía PC HODOM (Tailscale → 100.77.30.26:8080)
# El script detecta automáticamente según DAU_SGH_MODE
```

### Paso 9 — Agentes especializados

Los 4 sub-agentes se registran en `openclaw.json` bajo `agents.list`:

```json
{
  "agents": {
    "list": [
      { "id": "urgencista", "model": "anthropic/claude-opus-4-6", "botToken": "..." },
      { "id": "salubrista", "model": "anthropic/claude-opus-4-6", "botToken": "..." },
      { "id": "clawmaster", "model": "anthropic/claude-opus-4-6", "botToken": "..." },
      { "id": "pensador",   "model": "anthropic/claude-opus-4-6", "botToken": "..." }
    ]
  }
}
```

Cada uno requiere:
- Bot de Telegram propio (@klinikurgo_bot, @SaluristaHahBot, etc.)
- Workspace dedicado en `~/.openclaw/agents/<id>/`
- Configuración de bindings (routing por topic Telegram o palabras clave)

### Paso 10 — Cron jobs

```bash
# Korax tiene 2 cron jobs activos:
# 1. korax-briefing — briefing matutino L-V 11:00 UTC
# 2. heartbeat — verificación periódica

# Ver cron jobs
openclaw cron list

# Recrear si es necesario:
openclaw cron add --name korax-briefing \
  --schedule "0 11 * * 1-5" \
  --sessionTarget isolated \
  --payload '{"kind":"agentTurn","message":"Genera briefing matutino para Korvo"}'
```

---

## Configuración de integraciones

### Telegram

```bash
# Crear bot vía @BotFather → obtener token
# Allowlist de usuarios:
openclaw config patch '{
  "channels": {
    "telegram": {
      "allowFrom": ["7192195698"],
      "accounts": {
        "default": {
          "botToken": "__TU_TOKEN__",
          "allowFrom": ["7192195698"]
        }
      }
    }
  }
}'
```

### Slack

```bash
openclaw config patch '{
  "channels": {
    "slack": {
      "botToken": "xoxb-...",
      "appToken": "xapp-..."
    }
  }
}'
```

### Google Workspace (gog)

```bash
# El token OAuth vive en ~/.config/gog/credentials.json
# o en la variable GOG_TOKEN del env file

# Configurar cuenta por defecto
gog auth set-default --account koraxfx@gmail.com
```

### DAU/SGH (sistemas clínicos Hospital San Carlos)

```bash
# Credentials en env file (OpenClaw SecretRef):
DAU_USER=fsanhuezal
DAU_PASSWORD=__REAL_PASSWORD__
SGH_USER=fsanhuezal
SGH_PASSWORD=__REAL_PASSWORD__

# Ruteo proxy-hodomito (PC HODOM Windows con TightVNC):
export DAU_SGH_MODE=proxy-hodomito
# Scripts leen automáticamente el modo y rutean según corresponda
```

### Kilo Gateway (modelos free)

```bash
# API: https://api.kilo.ai/api/gateway
# Models free: kimi (262K ctx), glm5 (200K), minimax-kilo (200K)

KILO_API_KEY=__KEY__
```

---

## Validación post-install

```bash
# 1. Gateway corriendo
systemctl --user status openclaw-gateway
curl -s http://localhost:18789/health

# 2. openclaw doctor
openclaw doctor --non-interactive

# 3. Telegram funcional
openclaw channels telegram send --to 7192195698 --message "Korax activo ✅"

# 4. gog funcional
gog gmail messages search "in:inbox is:unread" --account koraxfx@gmail.com --limit 3

# 5. Skills cargadas
openclaw skills list | grep "✓ ready"

# 6. Agentes accesibles
openclaw agents list
```

---

## Notas sobre continuidad

### Lo que persiste entre sesiones
- `MEMORY.md` — conocimiento curado de largo plazo
- `memory/YYYY-MM-DD.md` — bitácoras diarias
- `memory/gtd/*.md` — sistema de productividad
- `openclaw.json` + `env` — configuración e integraciones

### Lo que NO se replica automáticamente
- Historial de sesiones de chat (transcripts)
- Session locks activos
- Tokens de sesión OAuth vivos
- Credenciales clínicas (hay que rellenar manualmente)
- Webhook states (Gmail watch, etc.)

### Actualización de memoria
Después de cada sesión significativa:
```bash
# Korvo debería decir o Korax debería capturar:
# "Korax, anota esto en memoria"
# → se escribe en ~/clawd/memory/YYYY-MM-DD.md
```

### Nodo air (MacBook Korvo)
El nodo air no es parte de esta replicación — es un canal opcional para:
- Browser con sesión Google logueada
- Acceso a archivos Obsidian locales
- Automatizaciones macOS-specific

Para replicar: ver `~/clawd/docs/activa/TUTORIAL-KORAX-REPLICADO.md`

---

*Paquete generado: 2026-04-03 | Korax export kit v1.0.0*
*Contiene: bootstrap (8 archivos), skills (16), agents (5), memory (55 archivos), docs (60+)*

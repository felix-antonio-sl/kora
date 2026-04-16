# Curso OpenClaw — Fundamentos

*Autor: Korax | Fecha: 2026-02-17*

---

## 📋 Índice

1. [¿Qué es OpenClaw?](#1-qué-es-openclaw)
2. [Arquitectura](#2-arquitectura)
3. [Instalación](#3-instalación)
4. [Configuración](#4-configuración)
5. [Canales](#5-canales)
6. [Agentes y Sesiones](#6-agentes-y-sesiones)
7. [Skills (Habilidades)](#7-skills-habilidades)
8. [Automatización](#8-automatización)
9. [Multi-Agente](#9-multi-agente)
10. [Seguridad](#10-seguridad)
11. [Comandos Esenciales](#11-comandos-esenciales)

---

## 1. ¿Qué es OpenClaw?

### Definición
OpenClaw es un **gateway self-hosted** que conecta aplicaciones de mensajería (WhatsApp, Telegram, Discord, iMessage, etc.) con agentes de IA. Es el puente entre tus apps de chat y un asistente de IA siempre disponible.

### Diferenciadores Clave

| Característica | Descripción |
|----------------|-------------|
| **Self-hosted** | Corre en tu hardware, tus reglas |
| **Multi-canal** | Un Gateway sirve WhatsApp, Telegram, Discord simultáneamente |
| **Agent-native** | Construido para agentes con tools, sesiones, memoria, routing |
| **Open source** | Licencia MIT, comunidad activa |

### ¿Para quién es?
Desarrolladores y power users que quieren un asistente de IA personal al que pueden mensajear desde cualquier lugar — sin ceder control de sus datos.

### Requisitos Mínimos
- Node 22+
- API key de un proveedor (Anthropic recomendado)
- 5 minutos

---

## 2. Arquitectura

### Diagrama Conceptual

```
┌─────────────────┐     ┌─────────────┐     ┌──────────────────┐
│  Chat Apps      │────▶│   Gateway   │────▶│   Agente (Pi)    │
│  + Plugins      │     │             │     │                  │
└─────────────────┘     └──────┬──────┘     └──────────────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
              ┌──▼──┐     ┌────▼────┐   ┌────▼────┐
              │ CLI │     │ Web UI  │   │ Nodes   │
              └─────┘     └─────────┘   └─────────┘
```

### Componentes

| Componente | Rol |
|------------|-----|
| **Gateway** | Proceso central. Orquesta canales, sesiones, routing |
| **Agente (Pi)** | El "cerebro" que ejecuta herramientas y responde |
| **Canales** | Conectores a WhatsApp, Telegram, Discord, etc. |
| **Sessions** | Estado de conversación por usuario/grupo |
| **Tools** | Capacidades del agente (exec, read, write, browser...) |
| **Skills** | Instrucciones para usar herramientas específicas |
| **Nodes** | Dispositivos móviles (iOS/Android) conectados |

### Flujo de un Mensaje

```
1. Usuario envía mensaje (WhatsApp/Telegram/etc.)
2. Gateway recibe vía conector del canal
3. Gateway identifica sesión y agente destino
4. Agente procesa mensaje + contexto + tools
5. Agente genera respuesta (puede usar herramientas)
6. Gateway enruta respuesta al canal de origen
7. Usuario recibe respuesta
```

---

## 3. Instalación

### Método Recomendado (Script)

**macOS/Linux:**
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

### Método NPM
```bash
npm install -g openclaw@latest
```

### Onboarding Wizard
```bash
openclaw onboard --install-daemon
```

El wizard configura:
- Autenticación con proveedores
- Configuración del Gateway
- Canales opcionales

### Verificación
```bash
openclaw gateway status
openclaw dashboard  # Abre Control UI en navegador
```

---

## 4. Configuración

### Ubicación
```
~/.openclaw/openclaw.json
```

Formato: **JSON5** (soporta comentarios y trailing commas)

### Estructura Mínima
```json5
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace"
    }
  },
  channels: {
    whatsapp: {
      allowFrom: ["+56912345678"]
    }
  }
}
```

### Métodos de Edición

| Método | Comando/Acción |
|--------|----------------|
| **Wizard** | `openclaw onboard` o `openclaw configure` |
| **CLI** | `openclaw config set <key> <value>` |
| **Control UI** | Tab "Config" en http://127.0.0.1:18789 |
| **Directo** | Editar `~/.openclaw/openclaw.json` |

### Hot Reload
El Gateway detecta cambios y aplica automáticamente (sin restart para la mayoría).

**Modos de reload:**

| Modo | Comportamiento |
|------|----------------|
| `hybrid` (default) | Hot-apply cambios seguros, restart auto para críticos |
| `hot` | Solo hot-apply, warning si necesita restart |
| `restart` | Restart en cualquier cambio |
| `off` | Sin watching, requiere restart manual |

### Variables de Entorno
Ubicaciones (en orden de precedencia):
1. Env vars del proceso padre
2. `.env` en directorio actual
3. `~/.openclaw/.env`

Ejemplo de sustitución en config:
```json5
{
  gateway: {
    auth: {
      token: "${OPENCLAW_GATEWAY_TOKEN}"
    }
  }
}
```

---

## 5. Canales

### Canales Soportados

| Canal | Sección Config | Estado |
|-------|----------------|--------|
| WhatsApp | `channels.whatsapp` | ✅ Core |
| Telegram | `channels.telegram` | ✅ Core |
| Discord | `channels.discord` | ✅ Core |
| iMessage | `channels.imessage` | ✅ Core (macOS) |
| Signal | `channels.signal` | ✅ Core |
| Slack | `channels.slack` | ✅ Core |
| Google Chat | `channels.googlechat` | ✅ Core |
| Mattermost | `channels.mattermost` | 🔌 Plugin |
| MS Teams | `channels.msteams` | 🔌 Plugin |

### Políticas de DM (dmPolicy)

| Valor | Comportamiento |
|-------|----------------|
| `pairing` | Desconocidos reciben código para aprobar (default) |
| `allowlist` | Solo permite `allowFrom` |
| `open` | Permite todos (requiere `allowFrom: ["*"]`) |
| `disabled` | Ignora todos los DMs |

### Ejemplo: Telegram
```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123456:ABC-DEF...",
      dmPolicy: "allowlist",
      allowFrom: ["tg:7192195698"]
    }
  }
}
```

### Grupos
Los grupos requieren mención por defecto:
```json5
{
  channels: {
    whatsapp: {
      groups: {
        "*": { requireMention: true }
      }
    }
  },
  agents: {
    list: [{
      id: "main",
      groupChat: {
        mentionPatterns: ["@openclaw", "openclaw"]
      }
    }]
  }
}
```

---

## 6. Agentes y Sesiones

### ¿Qué es un Agente?

Un **agente** es un "cerebro" aislado con:

| Componente | Descripción |
|------------|-------------|
| **Workspace** | Directorio con archivos del agente (AGENTS.md, SOUL.md, USER.md) |
| **agentDir** | Estado, auth profiles, registry por agente |
| **Sessions** | Historial de chat + estado de routing |

### Rutas por Defecto
```
~/.openclaw/openclaw.json          # Config global
~/.openclaw/workspace              # Workspace default
~/.openclaw/agents/<agentId>/      # Estado por agente
~/.openclaw/agents/<agentId>/sessions/  # Sesiones
```

### Session Scoping (dmScope)

| Valor | Comportamiento |
|-------|----------------|
| `main` | Todos comparten una sesión |
| `per-peer` | Una sesión por usuario |
| `per-channel-peer` | Una sesión por usuario+canal |
| `per-account-channel-peer` | Máximo aislamiento |

### Reset de Sesiones
```json5
{
  session: {
    reset: {
      mode: "daily",
      atHour: 4,
      idleMinutes: 120
    }
  }
}
```

### Archivos del Workspace

| Archivo | Propósito |
|---------|-----------|
| `AGENTS.md` | Instrucciones operativas del agente |
| `SOUL.md` | Personalidad y tono |
| `USER.md` | Información del usuario |
| `MEMORY.md` | Memoria curada largo plazo |
| `TOOLS.md` | Notas locales sobre herramientas |
| `HEARTBEAT.md` | Checklist para heartbeats |

---

## 7. Skills (Habilidades)

### ¿Qué es un Skill?
Un **skill** es un directorio con un `SKILL.md` que enseña al agente a usar herramientas específicas.

### Ubicaciones (Precedencia)
1. `<workspace>/skills` (más alta)
2. `~/.openclaw/skills` (compartido)
3. Skills bundled (más baja)

### Formato SKILL.md
```markdown
---
name: mi-skill
description: Descripción corta del skill
---

## Instrucciones

Aquí van las instrucciones para el agente...
```

### ClawHub
Registro público de skills: https://clawhub.com

```bash
# Instalar skill
clawhub install <skill-slug>

# Actualizar todos
clawhub update --all

# Publicar cambios
clawhub sync --all
```

---

## 8. Automatización

### Heartbeat
Polling periódico para que el agente "despierte" y haga checks proactivos.

```json5
{
  agents: {
    defaults: {
      heartbeat: {
        every: "30m",
        target: "last"  // last | whatsapp | telegram | none
      }
    }
  }
}
```

### Cron Jobs
Scheduler integrado en el Gateway.

**Tipos de schedule:**

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| `at` | ISO timestamp | `"2026-02-18T09:00:00Z"` |
| `every` | Intervalo en ms | `everyMs: 3600000` |
| `cron` | Expresión cron | `"0 7 * * *"` |

**Tipos de payload:**

| Tipo | Target | Uso |
|------|--------|-----|
| `systemEvent` | main | Inyecta texto como evento de sistema |
| `agentTurn` | isolated | Ejecuta turno del agente aislado |

### Ejemplo: Reminder
```bash
openclaw cron add \
  --name "Reminder" \
  --at "2026-02-18T09:00:00-03:00" \
  --session main \
  --system-event "Reminder: revisar inbox GTD" \
  --wake now \
  --delete-after-run
```

### Cron vs Heartbeat

| Usar Heartbeat cuando... | Usar Cron cuando... |
|--------------------------|---------------------|
| Múltiples checks juntos | Timing exacto importa |
| Necesitas contexto reciente | Tarea necesita aislamiento |
| Timing puede variar | One-shot reminders |
| Reducir API calls | Output directo a canal |

---

## 9. Multi-Agente

### Concepto
Múltiples agentes **aislados** en un solo Gateway:
- Diferentes workspaces
- Diferentes personalidades
- Sesiones separadas

### Bindings
Reglas que enrutan mensajes entrantes a un agente específico.

**Orden de precedencia:**
1. `peer` match (DM/grupo exacto)
2. `parentPeer` (herencia de thread)
3. `guildId + roles` (Discord)
4. `guildId` (Discord)
5. `teamId` (Slack)
6. `accountId` del canal
7. Canal completo
8. Default agent

### Ejemplo: Dos WhatsApps → Dos Agentes
```json5
{
  agents: {
    list: [
      {
        id: "home",
        default: true,
        workspace: "~/.openclaw/workspace-home"
      },
      {
        id: "work",
        workspace: "~/.openclaw/workspace-work"
      }
    ]
  },
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } }
  ]
}
```

### Ejemplo: WhatsApp rápido + Telegram deep work
```json5
{
  agents: {
    list: [
      {
        id: "chat",
        workspace: "~/.openclaw/workspace-chat",
        model: "anthropic/claude-sonnet-4-5"
      },
      {
        id: "opus",
        workspace: "~/.openclaw/workspace-opus",
        model: "anthropic/claude-opus-4-6"
      }
    ]
  },
  bindings: [
    { agentId: "chat", match: { channel: "whatsapp" } },
    { agentId: "opus", match: { channel: "telegram" } }
  ]
}
```

---

## 10. Seguridad

### Principios

1. **Allowlists** — Controla quién puede enviar mensajes
2. **Pairing** — Código de aprobación para desconocidos
3. **Sandboxing** — Contenedores Docker para aislamiento
4. **Tool policies** — Allow/deny lists por agente

### Sandboxing
```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",  // off | non-main | all
        scope: "agent"     // session | agent | shared
      }
    }
  }
}
```

### Tool Policies por Agente
```json5
{
  agents: {
    list: [{
      id: "family",
      tools: {
        allow: ["read", "exec"],
        deny: ["write", "browser"]
      }
    }]
  }
}
```

### Elevated Commands
Comandos que requieren confirmación adicional (ej: sudo).

---

## 11. Comandos Esenciales

### Gateway
```bash
openclaw gateway status       # Estado del gateway
openclaw gateway start        # Iniciar como servicio
openclaw gateway stop         # Detener
openclaw gateway restart      # Reiniciar
openclaw gateway --port 18789 # Foreground mode
```

### Configuración
```bash
openclaw onboard              # Wizard completo
openclaw configure            # Wizard de config
openclaw config get <key>     # Leer valor
openclaw config set <key> <value>  # Escribir valor
```

### Canales
```bash
openclaw channels login       # Login a canales
openclaw channels status      # Estado de canales
```

### Sesiones
```bash
openclaw sessions list        # Listar sesiones
openclaw sessions history <key>  # Ver historial
```

### Cron
```bash
openclaw cron list            # Listar jobs
openclaw cron add [opts]      # Crear job
openclaw cron run <id>        # Ejecutar ahora
openclaw cron remove <id>     # Eliminar
```

### Diagnóstico
```bash
openclaw status               # Estado general
openclaw doctor               # Diagnóstico de problemas
openclaw logs                 # Ver logs
openclaw health               # Health check
```

### Skills
```bash
clawhub search <query>        # Buscar skills
clawhub install <slug>        # Instalar
clawhub update --all          # Actualizar todos
```

---

## 📚 Recursos

- **Docs oficiales**: https://docs.openclaw.ai
- **GitHub**: https://github.com/openclaw/openclaw
- **Skills Hub**: https://clawhub.com
- **Discord**: https://discord.com/invite/clawd

---

*Este curso es un resumen ejecutivo. Para detalles completos, consultar la documentación oficial.*

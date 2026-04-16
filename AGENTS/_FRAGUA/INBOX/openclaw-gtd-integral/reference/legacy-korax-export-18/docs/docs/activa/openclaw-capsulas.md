# OpenClaw — Cápsulas de Conocimiento

*Referencia rápida | 2026-02-17*

---

## 💊 1. ESENCIA

> **OpenClaw** = Gateway self-hosted que conecta apps de chat (WhatsApp, Telegram, Discord...) con agentes IA.

**3 palabras clave:**
- **Self-hosted** → tu hardware, tus datos
- **Multi-canal** → un proceso, muchos chats
- **Agent-native** → tools, sesiones, memoria

**Requisitos:** Node 22+ | API key | 5 min

---

## 💊 2. ARQUITECTURA

```
[Chat Apps] → [Gateway] → [Agente Pi]
                 ↓
         [CLI | Web UI | Nodes]
```

| Componente | Función |
|------------|---------|
| **Gateway** | Orquestador central |
| **Agente** | Cerebro + tools |
| **Canal** | Conector a WhatsApp/TG/etc |
| **Session** | Estado de conversación |
| **Skill** | Instrucciones para tools |

---

## 💊 3. INSTALACIÓN

```bash
# Una línea
curl -fsSL https://openclaw.ai/install.sh | bash

# Configurar
openclaw onboard --install-daemon

# Verificar
openclaw gateway status
```

---

## 💊 4. CONFIG

**Archivo:** `~/.openclaw/openclaw.json` (JSON5)

**Mínimo viable:**
```json5
{
  agents: { defaults: { workspace: "~/.openclaw/workspace" } },
  channels: { telegram: { botToken: "...", allowFrom: ["tg:123"] } }
}
```

**Editar:**
- `openclaw configure` → wizard
- `openclaw config set <key> <val>` → CLI
- `http://127.0.0.1:18789` → Web UI

**Hot reload:** ✅ automático (mayoría de cambios)

---

## 💊 5. CANALES

| Canal | Config Key | Notas |
|-------|------------|-------|
| WhatsApp | `channels.whatsapp` | Baileys (Web) |
| Telegram | `channels.telegram` | Bot token |
| Discord | `channels.discord` | Bot |
| iMessage | `channels.imessage` | macOS only |
| Signal | `channels.signal` | - |
| Slack | `channels.slack` | - |

**Políticas DM:**
- `pairing` → código aprobación (default)
- `allowlist` → solo lista
- `open` → todos
- `disabled` → ignorar

**Grupos:** Requieren mención por defecto (`@bot`)

---

## 💊 6. AGENTE

**Un agente = un cerebro aislado:**
- Workspace (archivos)
- Sessions (historial)
- Auth profiles

**Archivos clave del workspace:**

| Archivo | Contenido |
|---------|-----------|
| `AGENTS.md` | Instrucciones operativas |
| `SOUL.md` | Personalidad |
| `USER.md` | Info del usuario |
| `MEMORY.md` | Memoria largo plazo |
| `HEARTBEAT.md` | Checklist periódico |

---

## 💊 7. SESIONES

**Scoping (dmScope):**
- `main` → todos comparten
- `per-peer` → por usuario
- `per-channel-peer` → por usuario+canal

**Reset:**
```json5
{ session: { reset: { mode: "daily", atHour: 4 } } }
```

---

## 💊 8. SKILLS

**Qué es:** Directorio con `SKILL.md` que enseña a usar tools.

**Ubicaciones (precedencia):**
1. `<workspace>/skills/`
2. `~/.openclaw/skills/`
3. Bundled

**Instalar:** `clawhub install <slug>`

**Hub:** https://clawhub.com

---

## 💊 9. AUTOMATIZACIÓN

### Heartbeat
Polling periódico del agente.
```json5
{ agents: { defaults: { heartbeat: { every: "30m" } } } }
```

### Cron
Scheduler del Gateway.

| Schedule | Formato |
|----------|---------|
| `at` | ISO timestamp |
| `every` | Intervalo ms |
| `cron` | Expresión cron |

```bash
openclaw cron add --name "Test" --at "2026-02-18T09:00:00Z" \
  --session main --system-event "Hola" --wake now
```

**Regla:** Heartbeat = batch checks | Cron = timing exacto

---

## 💊 10. MULTI-AGENTE

**Concepto:** Múltiples agentes aislados en un Gateway.

**Bindings:** Reglas que enrutan mensajes → agente.

```json5
{
  agents: { list: [
    { id: "home", workspace: "~/.openclaw/ws-home" },
    { id: "work", workspace: "~/.openclaw/ws-work" }
  ]},
  bindings: [
    { agentId: "home", match: { channel: "whatsapp" } },
    { agentId: "work", match: { channel: "telegram" } }
  ]
}
```

---

## 💊 11. SEGURIDAD

| Mecanismo | Función |
|-----------|---------|
| **Allowlist** | Quién puede escribir |
| **Pairing** | Código de aprobación |
| **Sandbox** | Docker aislado |
| **Tool policy** | Allow/deny por agente |

```json5
{ agents: { defaults: { sandbox: { mode: "non-main" } } } }
```

---

## 💊 12. COMANDOS QUICK REF

```bash
# Gateway
openclaw gateway status|start|stop|restart

# Config
openclaw config get|set <key> [val]
openclaw configure

# Canales
openclaw channels login|status

# Sesiones
openclaw sessions list|history <key>

# Cron
openclaw cron list|add|run|remove

# Diagnóstico
openclaw status|doctor|logs|health
```

---

## 💊 13. RUTAS CLAVE

```
~/.openclaw/
├── openclaw.json        # Config principal
├── .env                 # Secrets
├── workspace/           # Workspace default
├── agents/<id>/         # Estado por agente
├── cron/jobs.json       # Cron jobs
└── skills/              # Skills compartidos
```

---

## 💊 14. TROUBLESHOOTING

| Síntoma | Acción |
|---------|--------|
| Gateway no inicia | `openclaw doctor --fix` |
| Config inválida | `openclaw doctor` |
| Canal desconectado | `openclaw channels login` |
| Ver logs | `openclaw logs` |
| Health check | `openclaw health` |

---

## 📎 Links

- Docs: https://docs.openclaw.ai
- GitHub: https://github.com/openclaw/openclaw
- Skills: https://clawhub.com
- Discord: https://discord.com/invite/clawd

---

*14 cápsulas | ~150 líneas | Todo lo esencial*

---
_manifest:
  urn: urn:kora:kb:06-multi-agent-routing
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '06'
- multi
- agent
lang: es
---

# Capítulo 6 — Multi-Agent Routing

> **Propósito:** Entender cómo un solo gateway puede hospedar múltiples "cerebros" aislados, cómo los mensajes se rutean al agente correcto, y qué patrones de configuración existen. Este es el capítulo que transforma OpenClaw de "un asistente personal" a "una plataforma de agentes".

- ---


## 6.1 Concepto: Un Gateway, Múltiples Cerebros

- En modo single-agent (default), todo va a un agente `main`.
- Multi-agent routing permite que **un solo proceso gateway** hospede múltiples agentes, cada uno con:


```
┌─────────────────────────────────────────────────────────────┐
│                     GATEWAY (un proceso)                     │
│                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ Agent "main" │  │ Agent "work"│  │ Agent "fam" │         │
│  │              │  │              │  │              │         │
│  │ Workspace A  │  │ Workspace B  │  │ Workspace C  │         │
│  │ SOUL.md: yo  │  │ SOUL.md:     │  │ SOUL.md:     │         │
│  │ Model: sonnet│  │ formal       │  │ casual       │         │
│  │ Tools: full  │  │ Model: opus  │  │ Model: haiku │         │
│  │ Sandbox: off │  │ Tools: code  │  │ Tools: read  │         │
│  │              │  │ Sandbox: off │  │ Sandbox: all │         │
│  │ Auth: keys A │  │ Auth: keys B │  │ Auth: keys C │         │
│  │ Sessions: A/ │  │ Sessions: B/ │  │ Sessions: C/ │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                 │                │
│  ┌──────┴─────────────────┴─────────────────┴──────────────┐ │
│  │                    BINDINGS (router)                      │ │
│  │  "WhatsApp personal" → main                              │ │
│  │  "Telegram @WorkBot" → work                              │ │
│  │  "WhatsApp grupo familia" → fam                          │ │
│  └──────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Qué se aísla entre agentes

| Recurso | ¿Aislado? | Cómo |
|---------|-----------|------|
| **Workspace** (SOUL.md, AGENTS.md, memoria, skills) | ✅ Sí | Directorios separados |
| **Auth profiles** (API keys, OAuth tokens) | ✅ Sí | `auth-profiles.json` per-agent |
| **Sessions** (historial, transcripts) | ✅ Sí | `sessions/` per-agent |
| **Model config** (primary, fallbacks) | ✅ Sí | Per-agent override disponible |
| **Tool policy** (allow/deny, sandbox) | ✅ Sí | Per-agent config |
| **Skills** | Parcial | Workspace skills aislados; managed/bundled compartidos |
| **Gateway config** (ports, auth, channels) | ❌ No | Un solo openclaw.json |
| **Channel connections** (WhatsApp session, Telegram bot) | ❌ No | Compartidos (pero ruteable por account) |

### ¿Cuándo necesitas multi-agent?

| Situación | ¿Multi-agent? | Alternativa |
|-----------|--------------|-------------|
| Solo tú, múltiples canales | No | Un agente, `dmScope: main` |
| Tú + familia en el mismo WhatsApp | **Sí** o `per-channel-peer` | `dmScope` si solo necesitas separar contexto |
| Agente personal + agente de trabajo | **Sí** | — |
| Diferentes personalidades por canal | **Sí** | — |
| Diferentes modelos por canal | **Sí** (o per-session `/model`) | `/model` si es temporal |
| Bot público + asistente privado | **Sí** | — |
| Diferentes niveles de seguridad/tools | **Sí** | sandbox `non-main` si solo grupos |

- **La distinción clave:** `dmScope` separa **contexto** (sesiones diferentes), pero el agente es el mismo (misma personalidad, mismas tools, misma memoria).
- Multi-agent separa **todo** — son cerebros independientes.


- ---


## 6.2 Configuración de Agentes

### Estructura en openclaw.json

```json5
{
  agents: {
    defaults: {
      // Heredado por todos los agentes que no overriden
      model: { primary: "anthropic/claude-sonnet-4-6" },
      sandbox: { mode: "off" },
      heartbeat: { every: "30m", target: "last" }
    },
    list: [
      {
        id: "main",            // identificador único
        default: true,          // recibe lo que no matchea ningún binding
        name: "Korax",          // nombre display
        workspace: "~/clawd",
        // agentDir: auto → ~/.openclaw/agents/main/agent
        // model: hereda de defaults
      },
      {
        id: "work",
        name: "WorkBot",
        workspace: "~/.openclaw/workspace-work",
        model: { primary: "anthropic/claude-opus-4-6" },
        sandbox: { mode: "all", scope: "agent" },
        tools: {
          profile: "coding",
          deny: ["browser", "canvas"]
        },
        identity: { name: "WorkBot" },
        groupChat: {
          mentionPatterns: ["@workbot", "@WorkBot"]
        }
      },
      {
        id: "family",
        name: "FamilyBot",
        workspace: "~/.openclaw/workspace-family",
        model: { primary: "anthropic/claude-haiku-4-5" },
        sandbox: { mode: "all", scope: "agent", workspaceAccess: "ro" },
        tools: {
          allow: ["read", "group:memory", "group:messaging"],
          deny: ["exec", "write", "edit", "apply_patch", "browser", "cron", "gateway"]
        }
      }
    ]
  }
}
```

### Campos de agents.list[]

| Campo | Requerido | Propósito |
|-------|-----------|-----------|
| `id` | ✅ | Identificador único del agente. Aparece en session keys, logs, CLI |
| `default` | No | Si `true`, recibe mensajes que no matchean ningún binding. Solo uno puede ser default |
| `name` | No | Nombre display para UIs |
| `workspace` | No | Path al workspace. Default: `~/.openclaw/workspace-<id>` |
| `agentDir` | No | Path al agent dir. Default: `~/.openclaw/agents/<id>/agent` |
| `model` | No | Override de `agents.defaults.model` |
| `sandbox` | No | Override de `agents.defaults.sandbox` |
| `tools` | No | Override de tool policy |
| `heartbeat` | No | Override de heartbeat config. Si ALGÚN agente tiene heartbeat, SOLO esos agentes corren heartbeats |
| `identity` | No | `{ name }` — nombre del agente para el runtime |
| `groupChat` | No | `{ mentionPatterns }` — patrones para @mention en grupos |

### El agente default

- Si un mensaje no matchea ningún binding, va al agente con `default: true`.
- Si ninguno tiene `default: true`, va al primer agente en la lista.
- Si no hay `agents.list`, el agente implícito es `main`.


- ---


## 6.3 Bindings: El Router Determinístico

- Los bindings son **reglas de ruteo** que conectan mensajes inbound con agentes.
- Son declarativos, determinísticos, y se evalúan por especificidad.


### Anatomía de un binding

```json5
{
  agentId: "work",           // a qué agente enviar
  match: {
    channel: "telegram",     // canal (whatsapp, telegram, discord, slack, etc.)
    accountId: "work-bot",   // cuenta del canal (para multi-account)
    peer: {
      kind: "direct",        // "direct" | "group" | "channel"
      id: "7192195698"       // ID del peer específico
    },
    guildId: "123...",       // Discord guild
    roles: ["admin"],        // Discord roles
    teamId: "T123..."       // Slack team
  }
}
```

- No todos los campos son necesarios.
- Cuantos más campos, más específico el match.


### Jerarquía de especificidad (most-specific wins)

```
PRIORIDAD (mayor a menor):

1. peer match (ID exacto de DM, grupo, o canal)
   → Más específico posible: "este chat va a este agente"

2. parentPeer match (herencia de thread)
   → "Threads de este grupo heredan el agente del grupo"

3. guildId + roles (Discord role routing)
   → "Usuarios con rol X en guild Y van a agente Z"

4. guildId (Discord guild)
   → "Todo lo de este guild va a este agente"

5. teamId (Slack team)
   → "Todo lo de este team va a este agente"

6. accountId match (canal + cuenta)
   → "Todo lo que llega por esta cuenta va a este agente"

7. channel match con accountId: "*"
   → "Todo lo que llega por este canal (cualquier cuenta)"

8. default agent
   → Fallback final
```

### Regla: AND semántico

- Si un binding especifica múltiples campos, **todos** deben matchear:


```json5
// Matchea SOLO si es Telegram Y el peer es 7192195698
{ agentId: "main", match: { channel: "telegram", peer: { kind: "direct", id: "7192195698" } } }

// Matchea SOLO si es Discord Y guild 123 Y rol "admin"
{ agentId: "work", match: { channel: "discord", guildId: "123", roles: ["admin"] } }
```

### Regla: primer match gana (en el mismo tier)

- Si dos bindings están en el mismo nivel de especificidad, el que aparece **primero** en la lista de config gana:


```json5
bindings: [
  // Este gana para telegram (aparece primero)
  { agentId: "work", match: { channel: "telegram" } },
  // Este nunca matchea telegram (ya fue capturado arriba)
  { agentId: "alerts", match: { channel: "telegram" } }
]
```

### Orden recomendado en config

```json5
bindings: [
  // 1. Peer-specific (más específico primero)
  { agentId: "opus", match: { channel: "whatsapp", peer: { kind: "direct", id: "+1555..." } } },
  { agentId: "work", match: { channel: "whatsapp", peer: { kind: "group", id: "120363...@g.us" } } },

  // 2. Account-specific
  { agentId: "work", match: { channel: "telegram", accountId: "work-bot" } },

  // 3. Channel-wide
  { agentId: "main", match: { channel: "whatsapp" } },
  { agentId: "main", match: { channel: "telegram", accountId: "default" } }
]
```

- ---


## 6.4 Patrones de Multi-Agent

### Patrón 1: Un agente por canal

- El más simple.
- WhatsApp = rápido/casual, Telegram = deep work.


```json5
{
  agents: {
    list: [
      { id: "chat", model: { primary: "anthropic/claude-sonnet-4-6" }, workspace: "~/.openclaw/ws-chat" },
      { id: "deep", model: { primary: "anthropic/claude-opus-4-6" }, workspace: "~/.openclaw/ws-deep" }
    ]
  },
  bindings: [
    { agentId: "chat", match: { channel: "whatsapp" } },
    { agentId: "deep", match: { channel: "telegram" } }
  ]
}
```

- **Trade-off:** Workspaces separados = memorias separadas.
- Si quieres compartir contexto, necesitas mechanisms explícitos (agent-to-agent messaging, shared memory paths).


### Patrón 2: Un agente por cuenta (multi-bot)

- Dos bots de Telegram, cada uno con su personalidad.


```json5
{
  agents: {
    list: [
      { id: "main", workspace: "~/.openclaw/ws-main" },
      { id: "alerts", workspace: "~/.openclaw/ws-alerts" }
    ]
  },
  bindings: [
    { agentId: "main", match: { channel: "telegram", accountId: "default" } },
    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } }
  ],
  channels: {
    telegram: {
      accounts: {
        default: { botToken: "${TELEGRAM_BOT_TOKEN_MAIN}" },
        alerts: { botToken: "${TELEGRAM_BOT_TOKEN_ALERTS}" }
      }
    }
  }
}
```

### Patrón 3: Un agente por persona (DM split)

- Un solo número de WhatsApp, pero cada persona habla con un agente diferente.


```json5
{
  agents: {
    list: [
      { id: "korvo", default: true, workspace: "~/clawd" },
      { id: "ariel", workspace: "~/.openclaw/ws-ariel" }
    ]
  },
  bindings: [
    { agentId: "ariel", match: { channel: "whatsapp", peer: { kind: "direct", id: "+56987654321" } } }
    // korvo es default → todo lo demás va a korvo
  ],
  channels: {
    whatsapp: { dmPolicy: "allowlist", allowFrom: ["+56912345678", "+56987654321"] }
  }
}
```

- **Nota:** Las respuestas salen del mismo número de WhatsApp.
- Ariel y Korvo ven el mismo remitente, pero hablan con agentes completamente diferentes.


### Patrón 4: Agente familiar en grupo

- Un grupo de WhatsApp familiar con un agente dedicado, sandboxed, read-only:


```json5
{
  agents: {
    list: [
      { id: "main", default: true, workspace: "~/clawd" },
      {
        id: "family",
        workspace: "~/.openclaw/ws-family",
        model: { primary: "anthropic/claude-haiku-4-5" },
        sandbox: { mode: "all", scope: "agent", workspaceAccess: "ro" },
        tools: { allow: ["read", "group:memory"], deny: ["exec", "write", "browser", "cron", "gateway"] },
        groupChat: { mentionPatterns: ["@familybot", "@FamilyBot"] }
      }
    ]
  },
  bindings: [
    { agentId: "family", match: { channel: "whatsapp", peer: { kind: "group", id: "120363...@g.us" } } }
  ]
}
```

### Patrón 5: Personal DMs + Public Groups (single agent)

- No siempre necesitas multi-agent.
- Si solo quieres DMs en host y grupos en sandbox:


```json5
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",     // grupos = non-main = sandboxed
        scope: "session",
        workspaceAccess: "none"
      }
    },
    list: [
      { id: "main", default: true, sandbox: { mode: "off" } }
    ]
  }
}
```

- **Resultado:** DMs en host con acceso total, grupos en Docker con tools restringidos. **Un solo agente, un solo workspace, una sola memoria** — pero con postura de seguridad diferente por contexto.


- ---


## 6.5 Auth Isolation

- La aislación de auth es un **invariante de seguridad** de multi-agent:


```
~/.openclaw/agents/
├── main/
│   └── agent/
│       └── auth-profiles.json    ← API keys de "main"
├── work/
│   └── agent/
│       └── auth-profiles.json    ← API keys de "work" (separadas)
└── family/
    └── agent/
        └── auth-profiles.json    ← API keys de "family" (separadas)
```

### Reglas

1. **Cada agente lee SOLO su propio `auth-profiles.json`.** No hay herencia ni sharing automático.

2. **Nunca reusar `agentDir` entre agentes.** Causa colisiones de auth y sesiones.

3. **Para compartir credenciales:** copiar manualmente `auth-profiles.json` de un agente a otro. La copia es independiente — cambios en uno no afectan al otro.

4. **Setup de auth per-agent:**
   ```bash
   # Cada agente necesita su propio login
   openclaw models auth login --provider anthropic --agent work
   openclaw models auth paste-token --provider anthropic --agent family
   ```

### ¿Por qué no compartir?

- **Blast radius:** Si un agente público es comprometido via prompt injection, solo sus credenciales están expuestas — no las del agente personal.
- **Rate limits:** Providers trackean rate limits por API key. Si dos agentes comparten key, compiten por el mismo rate limit.
- **Billing:** Keys separadas permiten tracking de costos per-agent.
- **Revocación:** Puedes revocar la key de un agente sin afectar a los demás.

- ---


## 6.6 Agent-to-Agent Messaging

- Por default, los agentes NO pueden comunicarse entre sí.
- Es un opt-in explícito:


```json5
{
  tools: {
    agentToAgent: {
      enabled: false,      // default
      allow: ["main", "work"]  // solo estos agentes pueden inter-comunicarse
    }
  }
}
```

- Cuando habilitado, un agente puede usar `sessions_send` para enviar un mensaje a la sesión de otro agente.
- Esto permite patrones como:


- Agente "alerts" detecta algo → envía notificación a agente "main"
- Agente "work" completa una tarea → reporta a agente "main"

- **Riesgo:** Si un agente comprometido puede enviar mensajes a otro, podría intentar prompt injection inter-agente.
- Mantener el allowlist tight.


- ---


## 6.7 Verificación y Debugging

### CLI

```bash
# Ver agentes y sus bindings
openclaw agents list --bindings

# Ver status de canales
openclaw channels status --probe

# Inspeccionar sandbox de un agente específico
openclaw sandbox explain --agent work

# Sesiones de un agente
openclaw sessions --json --agent work
```

### Logs

```bash
# Filtrar por routing y agente
tail -f ~/.openclaw/logs/gateway.log | grep -E "routing|agent:"
```

### Checklist post-config

1. ✅ Cada agente tiene workspace propio (no compartido)
2. ✅ Cada agente tiene agentDir propio (no reusar)
3. ✅ Auth configurado per-agent (`openclaw models status --agent <id>`)
4. ✅ Bindings cubren todos los canales/cuentas esperados
5. ✅ Agente default definido (para catch-all)
6. ✅ Tool policy per-agent según nivel de confianza
7. ✅ `openclaw agents list --bindings` muestra el routing esperado

- ---


## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Un gateway, múltiples agentes** | Single deployment, múltiples personalidades/cerebros |
| **Aislamiento total** | Workspace + auth + sessions independientes por agente |
| **Bindings determinísticos** | Routing predecible: most-specific wins, AND semántico |
| **Auth per-agent** | Blast radius limitado; billing/rate-limit separado |
| **Agent default** | Catch-all para mensajes sin binding explícito |
| **Agent-to-agent: opt-in** | Seguridad por defecto; comunicación inter-agente explícita |
| **Per-agent model/sandbox/tools** | Cada agente con postura de seguridad y capacidades propias |
| **`non-main` sandbox** | Multi-postura sin multi-agent: DMs en host, grupos en sandbox |

### Árbol de decisión: ¿Necesito multi-agent?

```
¿Múltiples personas usan el agente?
├── NO → Single agent, dmScope: main
│        ¿Diferentes posturas de seguridad (DM vs grupo)?
│        ├── SÍ → sandbox mode: non-main
│        └── NO → sandbox: off
│
└── SÍ → ¿Necesitan personalidades/memorias diferentes?
         ├── SÍ → Multi-agent con bindings
         └── NO → ¿Solo separar contexto?
                  ├── SÍ → dmScope: per-channel-peer (sin multi-agent)
                  └── NO → Multi-agent
```

- ---


- *Siguiente: [Capítulo 7 — Aislamiento y Seguridad por Agente](07-aislamiento-seguridad.md)*


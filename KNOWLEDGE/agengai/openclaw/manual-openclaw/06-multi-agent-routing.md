---
_manifest:
  urn: urn:agengai:kb:06-multi-agent-routing
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '06'
- multi
- agent
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:06-multi-agent-routing
---

# Capítulo 6 — Multi-Agent Routing

> **Propósito:** Entender cómo un solo gateway puede hospedar múltiples "cerebros" aislados, cómo los mensajes se rutean al agente correcto, y qué patrones de configuración existen. Este es el capítulo que transforma OpenClaw de "un asistente personal" a "una plataforma de agentes".

- ---

## 6.1 Concepto: Un Gateway, Múltiples Cerebros

- En modo single-agent (default), todo va a un agente `main`.
- Multi-agent routing permite que **un solo proceso gateway** hospede múltiples agentes, cada uno con:

```
┌─────────────────────────────────────────────────────────────┐
│ GATEWAY (un proceso) │
│ │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │
│ │ Agent "main" │ │ Agent "work"│ │ Agent "fam" │ │
│ │ │ │ │ │ │ │
│ │ Workspace A │ │ Workspace B │ │ Workspace C │ │
│ │ SOUL.md: yo │ │ SOUL.md: │ │ SOUL.md: │ │
│ │ Model: sonnet│ │ formal │ │ casual │ │
│ │ Tools: full │ │ Model: opus │ │ Model: haiku │ │
│ │ Sandbox: off │ │ Tools: code │ │ Tools: read │ │
│ │ │ │ Sandbox: off │ │ Sandbox: all │ │
│ │ Auth: keys A │ │ Auth: keys B │ │ Auth: keys C │ │
│ │ Sessions: A/ │ │ Sessions: B/ │ │ Sessions: C/ │ │
│ └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ │
│ │ │ │ │
│ ┌──────┴─────────────────┴─────────────────┴──────────────┐ │
│ │ BINDINGS (router) │ │
│ │ "WhatsApp personal" → main │ │
│ │ "Telegram @WorkBot" → work │ │
│ │ "WhatsApp grupo familia" → fam │ │
│ └──────────────────────────────────────────────────────────┘ │
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

### Paths oficiales del modo single-agent y multi-agent

| Recurso | Default |
|---------|---------|
| Config | `~/.openclaw/openclaw.json` |
| State dir | `~/.openclaw` |
| Workspace single-agent | `~/.openclaw/workspace` |
| Workspace por agente | `~/.openclaw/workspace-<agentId>` |
| Agent dir | `~/.openclaw/agents/<agentId>/agent` |
| Sessions | `~/.openclaw/agents/<agentId>/sessions` |

- En single-agent, `main` sigue siendo el `agentId` implícito.
- El workspace es el `cwd` default, no un sandbox duro; si quieres aislamiento real, habilita sandbox.

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
 id: "main", // identificador único
 default: true, // recibe lo que no matchea ningún binding
 name: "Korax", // nombre display
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

### Helper CLI oficial

```bash
openclaw agents add work
openclaw agents list --bindings
```

- El wizard `openclaw agents add <id>` crea workspace, `agentDir` y estructura base de un agente aislado.

- ---

## 6.3 Bindings: El Router Determinístico

- Los bindings son **reglas de ruteo** que conectan mensajes inbound con agentes.
- Son declarativos, determinísticos, y se evalúan por especificidad.

### Anatomía de un binding

```json5
{
 agentId: "work", // a qué agente enviar
 match: {
 channel: "telegram", // canal (whatsapp, telegram, discord, slack, etc.)
 accountId: "work-bot", // cuenta del canal (para multi-account)
 peer: {
 kind: "direct", // "direct" | "group" | "channel"
 id: "7192195698" // ID del peer específico
 },
 guildId: "123...", // Discord guild
 roles: ["admin"], // Discord roles
 teamId: "T123..." // Slack team
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

### Nota importante sobre `accountId`

- Si omites `accountId`, el binding matchea la **cuenta default** del canal, no "cualquier cuenta".
- `accountId: "*"` es el verdadero fallback channel-wide.
- La CLI actual puede "upgradear" un binding channel-only a uno account-scoped si luego agregas la misma regla con `accountId` explícito.

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

## Patrón 1: Un agente por canal

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

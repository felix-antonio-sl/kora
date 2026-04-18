---
_manifest:
  urn: urn:agengai:kb:08-patrones-multitenant
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- 08
- patrones
- multitenant
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:08-patrones-multitenant
---

# Capítulo 8 — Patrones Multi-Tenant

> **Propósito:** Aplicar los conceptos de multi-agent, sesiones, sandbox y tool policy a escenarios concretos de uso compartido. Este capítulo no introduce conceptos nuevos — combina lo aprendido en patrones arquitectónicos accionables para cuando múltiples personas, canales o propósitos comparten un mismo gateway.

- ---

## 8.1 ¿Qué es "Multi-Tenant" en OpenClaw?

- Multi-tenant no es un feature — es un **patrón** que emerge de combinar:

- **Multi-agent** (Cap. 6): cerebros aislados
- **DM scope** (Cap. 3): sesiones separadas
- **Sandbox + tool policy** (Cap. 7): aislamiento de ejecución
- **Bindings** (Cap. 6): routing determinístico

```
"Multi-Tenant" = Múltiples usuarios o propósitos
 compartiendo un gateway
 con aislamiento apropiado
 para cada caso de uso
```

- No existe una config `multiTenant: true`.
- Lo que existe es un espectro de aislamiento:

```
Sin aislamiento ──────────────────────────────── Aislamiento total
 │ │
 dmScope:main dmScope:per-peer Multi-agent Multi-gateway
 (todo junto) (contexto sep.) (todo sep.) (proceso sep.)
```

- La decisión es: **¿cuánto necesitas separar y por qué?**

- ---

## 8.2 Patrón A: Un Número de WhatsApp → Múltiples Personas

### Escenario
- Tienes un número de WhatsApp (personal o business) y quieres que diferentes personas hablen con el bot, cada una con privacidad.

### Opción 1: Solo separar contexto (más simple)

```json5
{
 session: {
 dmScope: "per-channel-peer" // cada persona = su propia sesión
 },
 channels: {
 whatsapp: {
 dmPolicy: "pairing", // aprobación manual de nuevos DMs
 }
 }
}
```

- **Resultado:** Un solo agente, un workspace, una memoria.
- Cada persona tiene su propia sesión (historial separado).
- Pero comparten personalidad, tools y modelo.

- **Riesgo residual:** Si el modelo lee MEMORY.md (inyectado en toda sesión main), podría revelar info de una sesión a otra.
- Mitigación:
- MEMORY.md solo se inyecta en sesión main, y con `per-channel-peer`, ninguna sesión es "main" excepto la del owner.

- **Cuándo:** Pocas personas (familia, amigos cercanos), mismas tools para todos.

### Opción 2: Agente por persona (aislamiento total)

```json5
{
 agents: {
 list: [
 { id: "korvo", default: true, workspace: "~/clawd" },
 { id: "clau", workspace: "~/.openclaw/ws-clau",
 model: { primary: "anthropic/claude-haiku-4-5" },
 tools: { allow: ["read", "group:memory", "web_search", "web_fetch"] }
 }
 ]
 },
 bindings: [
 { agentId: "clau", match: { channel: "whatsapp", peer: { kind: "direct", id: "+56987654321" } } }
 // korvo es default → todo lo demás
 ],
 channels: {
 whatsapp: {
 dmPolicy: "allowlist",
 allowFrom: ["+56912345678", "+56987654321"]
 }
 }
}
```

- **Resultado:** Workspace, memoria, auth, tools y sesiones completamente separados.
- Clau tiene su propio SOUL.md, su propio modelo, y tools restringidos.

- **Cuándo:** Necesitas diferentes personalidades, niveles de acceso, o memorias separadas.

### Tabla comparativa

| | dmScope only | Multi-agent |
|--|-------------|-------------|
| Setup | Una línea de config | Config completa per-agent |
| Personalidad | Compartida | Independiente |
| Memoria | Compartida (MEMORY.md) | Independiente |
| Tools | Compartidos | Independientes |
| Modelo | Compartido | Independiente |
| Auth/billing | Compartido | Independiente |
| Privacidad de contexto | ✅ Sesiones separadas | ✅ Todo separado |
| Esfuerzo de mantenimiento | Mínimo | Per-agent (workspace, auth, etc.) |

- ---

## 8.3 Patrón B: Múltiples Cuentas → Múltiples Agentes

### Escenario
- Tienes múltiples bots de Telegram (o múltiples números de WhatsApp) y quieres que cada uno tenga su propio cerebro.

```json5
{
 agents: {
 list: [
 { id: "personal", workspace: "~/clawd", default: true },
 { id: "business", workspace: "~/.openclaw/ws-business",
 model: { primary: "anthropic/claude-opus-4-6" }
 }
 ]
 },
 bindings: [
 { agentId: "personal", match: { channel: "telegram", accountId: "default" } },
 { agentId: "business", match: { channel: "telegram", accountId: "business" } }
 ],
 channels: {
 telegram: {
 accounts: {
 default: { botToken: "${TG_TOKEN_PERSONAL}", dmPolicy: "allowlist", allowFrom: ["tg:7192195698"] },
 business: { botToken: "${TG_TOKEN_BUSINESS}", dmPolicy: "pairing" }
 }
 }
 }
}
```

- **Resultado:** Cada bot de Telegram tiene su propia personalidad, memoria y sesiones.
- El bot personal es restrictivo (solo Korvo); el business acepta pairing.

### Para WhatsApp con múltiples números

```bash
# Login de cada cuenta
openclaw channels login --channel whatsapp --account personal
openclaw channels login --channel whatsapp --account business
```

```json5
{
 bindings: [
 { agentId: "personal", match: { channel: "whatsapp", accountId: "personal" } },
 { agentId: "business", match: { channel: "whatsapp", accountId: "business" } }
 ],
 channels: {
 whatsapp: {
 accounts: {
 personal: {}, // creds en ~/.openclaw/credentials/whatsapp/personal/
 business: {}
 }
 }
 }
}
```

- ---

## 8.4 Patrón C: Canal × Modelo (Fast vs Deep)

### Escenario
- WhatsApp para conversación rápida (Sonnet), Telegram para trabajo profundo (Opus).

```json5
{
 agents: {
 list: [
 {
 id: "fast",
 name: "QuickBot",
 workspace: "~/.openclaw/ws-fast",
 model: { primary: "anthropic/claude-sonnet-4-6" }
 },
 {
 id: "deep",
 name: "DeepBot",
 workspace: "~/.openclaw/ws-deep",
 model: { primary: "anthropic/claude-opus-4-6" },
 tools: { profile: "coding" }
 }
 ]
 },
 bindings: [
 { agentId: "fast", match: { channel: "whatsapp" } },
 { agentId: "deep", match: { channel: "telegram" } }
 ]
}
```

### Variante: mismo agente, override de modelo por peer

- Si no necesitas workspaces separados (solo quieres un modelo diferente para un canal), puedes usar un solo agente con override en chat:

```
En Telegram: /model opus ← persiste en la sesión de Telegram
En WhatsApp: /model sonnet ← persiste en la sesión de WhatsApp
```

- Esto funciona cuando usas `dmScope: "per-channel-peer"` (sesiones separadas por canal), y el override persiste en cada sesión.

- **Trade-off:** Menos config pero manual.
- Cada `/new` resetea el modelo.
- Multi-agent es más declarativo y persistente.

- ---

## 8.5 Patrón D: Family/Work/Public Profiles

### Escenario completo
- Un gateway con tres perfiles de seguridad:

```json5
{
 agents: {
 defaults: {
 model: { primary: "anthropic/claude-sonnet-4-6" }
 },
 list: [
 // ── PERSONAL: acceso total, sin sandbox ──
 {
 id: "personal",
 default: true,
 workspace: "~/clawd",
 sandbox: { mode: "off" }
 },

 // ── WORK: coding, sandboxed, Opus ──
 {
 id: "work",
 workspace: "~/.openclaw/ws-work",
 model: { primary: "anthropic/claude-opus-4-6" },
 sandbox: {
 mode: "all",
 scope: "agent",
 workspaceAccess: "rw",
 docker: {
 network: "bridge",
 setupCommand: "apt-get update && apt-get install -y git curl"
 }
 },
 tools: {
 profile: "coding",
 deny: ["cron", "gateway", "group:messaging"]
 }
 },

 // ── FAMILY: read-only, Haiku, mínimo riesgo ──
 {
 id: "family",
 workspace: "~/.openclaw/ws-family",
 model: { primary: "anthropic/claude-haiku-4-5" },
 sandbox: { mode: "all", scope: "agent", workspaceAccess: "none" },
 tools: {
 allow: ["group:memory", "group:sessions", "web_search", "web_fetch"],
 deny: ["group:fs", "group:runtime", "group:ui", "group:nodes",
 "group:automation", "image"]
 },
 identity: { name: "FamilyBot" },
 groupChat: { mentionPatterns: ["@family", "@FamilyBot"] }
 }
 ]
 },

 bindings: [
 // Familia: grupo WhatsApp específico + DM de Clau
 { agentId: "family", match: { channel: "whatsapp", peer: { kind: "group", id: "120363...@g.us" } } },
 { agentId: "family", match: { channel: "whatsapp", peer: { kind: "direct", id: "+56987654321" } } },

 // Work: bot Telegram dedicado
 { agentId: "work", match: { channel: "telegram", accountId: "work-bot" } },

 // Personal: todo lo demás (default)
 ],

 channels: {
 whatsapp: {
 dmPolicy: "allowlist",
 allowFrom: ["+56912345678", "+56987654321"]
 },
 telegram: {
 accounts: {
 default: { botToken: "${TG_TOKEN_PERSONAL}", dmPolicy: "allowlist", allowFrom: ["tg:7192195698"] },
 "work-bot": { botToken: "${TG_TOKEN_WORK}", dmPolicy: "allowlist", allowFrom: ["tg:7192195698"] }
 }
 }
 }
}
```

### Resumen del perfil

| Agente | Modelo | Sandbox | Tools | Quién lo usa |
|--------|--------|---------|-------|-------------|
| personal | Sonnet | Off (host) | Full | Solo Korvo (cualquier canal sin binding) |
| work | Opus | All (Docker + rw) | Coding sin cron/gateway | Solo Korvo (Telegram work-bot) |
| family | Haiku | All (Docker, no workspace) | Memory + web (sin fs/exec) | Familia (grupo WA + DM Clau) |

- ---

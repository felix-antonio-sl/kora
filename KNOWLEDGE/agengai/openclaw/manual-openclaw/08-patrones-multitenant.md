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
     │                                                    │
  dmScope:main      dmScope:per-peer     Multi-agent    Multi-gateway
  (todo junto)      (contexto sep.)      (todo sep.)    (proceso sep.)
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
    dmScope: "per-channel-peer"   // cada persona = su propia sesión
  },
  channels: {
    whatsapp: {
      dmPolicy: "pairing",        // aprobación manual de nuevos DMs
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
        personal: {},   // creds en ~/.openclaw/credentials/whatsapp/personal/
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
En Telegram: /model opus      ← persiste en la sesión de Telegram
En WhatsApp: /model sonnet    ← persiste en la sesión de WhatsApp
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


## 8.6 Patrón E: Secure DM Mode Obligatorio

### Cuándo es obligatorio

- Si **cualquiera** de estas condiciones es true, `per-channel-peer` debería estar activado:


- `dmPolicy: "pairing"` y has aprobado más de un sender
- `dmPolicy: "allowlist"` con múltiples entries
- `dmPolicy: "open"` (cualquier persona puede enviar DM)
- Múltiples números/cuentas pueden llegar al mismo agente

### El riesgo sin secure DM mode

```
Con dmScope: "main" (default):

Alice → "Tengo una cita médica mañana a las 10"
   ↓ (comparte sesión main)
Bob → "¿De qué hablamos antes?"
   ↓ (modelo ve contexto de Alice)
Bot → "Mencionaste una cita médica mañana a las 10"
   ↓
🚨 Filtración de datos personales
```

### La protección

```json5
{
  session: {
    dmScope: "per-channel-peer"
  }
}
```

- **`openclaw security audit` advierte** cuando detecta multiple senders + `dmScope: "main"`.


- ---


## 8.7 Patrón F: Múltiples Gateways en un Host

### Cuándo se justifica

| Situación | ¿Multi-gateway? | Alternativa |
|-----------|-----------------|-------------|
| Quieres un rescue bot | ✅ Sí | — |
| Aislamiento total de procesos | ✅ Sí | Multi-agent (process compartido) |
| Diferentes versiones de OpenClaw | ✅ Sí | — |
| Diferentes usuarios del OS | ✅ Sí | — |
| Más agentes con más canales | No | Multi-agent en un gateway |
| Redundancia | ✅ Sí (active-passive) | — |

### La mayoría de los setups NO lo necesitan

- Un solo gateway maneja múltiples agentes, múltiples canales, múltiples cuentas.
- Multi-gateway agrega complejidad operativa:


- Puertos separados (base + derived ports)
- Config separada
- State dir separado
- Servicios systemd separados
- Monitoring duplicado

### Implementación: profiles

```bash
# Gateway principal
openclaw --profile main onboard
openclaw --profile main gateway install
# → port 18789, state ~/.openclaw-main/

# Rescue bot
openclaw --profile rescue onboard
# → port 19789, state ~/.openclaw-rescue/
openclaw --profile rescue gateway install
```

### Checklist de aislamiento (obligatoria)

| Recurso | Debe ser único por gateway |
|---------|---------------------------|
| `OPENCLAW_CONFIG_PATH` | ✅ Sí |
| `OPENCLAW_STATE_DIR` | ✅ Sí |
| `agents.defaults.workspace` | ✅ Sí |
| `gateway.port` | ✅ Sí |
| Browser control port (base+2) | ✅ Sí (derivado del port) |
| CDP ports | ✅ Sí (derivados) |

- **Port spacing:** Dejar al menos 20 puertos entre gateways.
- Mejor aún, usar rangos completamente diferentes (18789 vs 19789).


### Rescue bot: el patrón principal

- El rescue bot es un segundo gateway mínimo que puede:

- Diagnosticar si el gateway principal está caído
- Aplicar cambios de config al principal
- Enviar mensajes de emergencia

```json5
// ~/.openclaw-rescue/openclaw.json
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace-rescue",
      model: { primary: "anthropic/claude-haiku-4-5" }  // barato
    }
  },
  channels: {
    telegram: {
      botToken: "${TG_TOKEN_RESCUE}",
      dmPolicy: "allowlist",
      allowFrom: ["tg:7192195698"]
    }
  },
  gateway: {
    port: 19789,
    auth: { mode: "token", token: "${RESCUE_GATEWAY_TOKEN}" }
  }
}
```

- ---


## 8.8 Resumen: Matriz de Patrones

| Patrón | Usuarios | Canales | Agentes | Gateways | Complejidad |
|--------|----------|---------|---------|----------|-------------|
| A1: dmScope only | Múltiples | 1+ | 1 | 1 | ⭐ |
| A2: Agent per person | Múltiples | 1+ | N | 1 | ⭐⭐⭐ |
| B: Account per agent | 1 | Múltiples cuentas | N | 1 | ⭐⭐ |
| C: Channel × model | 1 | Múltiples | N | 1 | ⭐⭐ |
| D: Full profiles | Múltiples | Múltiples | N | 1 | ⭐⭐⭐⭐ |
| E: Secure DM | Múltiples | 1+ | 1 | 1 | ⭐ |
| F: Multi-gateway | Variable | Variable | Variable | N | ⭐⭐⭐⭐⭐ |

### Árbol de decisión integrado

```
¿Cuántas personas usan el bot?
│
├── SOLO YO
│   ├── ¿Diferentes canales = diferentes propósitos?
│   │   ├── SÍ → Patrón C (channel × model)
│   │   └── NO → Single agent, dmScope: main
│   │
│   └── ¿Necesito rescue bot?
│       ├── SÍ → Agregar Patrón F
│       └── NO → Un gateway basta
│
├── YO + FAMILIA/AMIGOS
│   ├── ¿Misma personalidad para todos?
│   │   ├── SÍ → Patrón E (secure DM) + sandbox non-main para grupos
│   │   └── NO → Patrón A2 (agent per person)
│   │
│   └── ¿Grupo compartido?
│       └── SÍ → Patrón D (family profile) con binding a grupo
│
└── MÚLTIPLES PERSONAS (público/business)
    ├── Patrón E (obligatorio)
    ├── Patrón A2 o B según separación necesaria
    └── ¿Necesito blast radius mínimo?
        └── SÍ → Patrón D + sandbox: all + tools: minimal
```

- ---


- *Siguiente: [Capítulo 9 — Sub-Agentes (sessions_spawn)](09-sub-agentes.md)*


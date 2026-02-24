# Capítulo 20 — Patrones de Diseño para Agentes OpenClaw

> **Propósito:** Catálogo de patrones arquitectónicos probados, cada uno con cuándo usarlo, config mínima, trade-offs, y anti-patrones. Es la referencia para responder "¿cómo debería estructurar mi setup?"

---

## 20.1 Patrón: Single Agent + Multiple Channels

**El más simple.** Un agente, un workspace, una memoria — múltiples canales de entrada.

```
Telegram ──┐
WhatsApp ──┼──► Agent "main" ──► Un workspace, una memoria
Discord  ──┘
```

**Config:**
```json5
{
  agents: { list: [{ id: "main", default: true, workspace: "~/clawd" }] },
  session: { dmScope: "main" }    // o per-channel-peer si >1 persona
}
```

**Cuándo:** Solo tú usas el agente. Quieres continuidad cross-channel.
**Trade-off:** Todo en un contexto. Si usas `dmScope: main`, la conversación de WhatsApp y Telegram se mezclan.
**Anti-patrón:** Usar esto con múltiples personas → leak de contexto.

---

## 20.2 Patrón: Agent per Persona

Personalidad, modelo, tools y memoria completamente diferentes por propósito.

```
Agent "personal"  → Sonnet, full tools, host access
Agent "work"      → Opus, coding tools, sandboxed
Agent "family"    → Haiku, read-only, sandboxed
```

**Config:** Ver Cap. 8 Patrón D completo.

**Cuándo:** Necesitas diferentes niveles de trust/capacidad/personalidad.
**Trade-off:** Más mantenimiento (workspace, auth, memoria por agente). Las memorias no se comparten.
**Anti-patrón:** Crear 10 agentes cuando 2-3 cubren todos los casos de uso.

---

## 20.3 Patrón: Agent per Concern

Especialización por dominio, no por persona.

```
Agent "ops"       → Monitoreo, alertas, infraestructura
Agent "coding"    → Code review, refactoring, PRs
Agent "research"  → Web search, analysis, summaries
Agent "main"      → Conversación general, catch-all
```

**Cuándo:** Tareas con requirements muy diferentes de tools/modelo/sandbox.
**Trade-off:** Complejidad de routing (bindings). Necesitas agent-to-agent para coordinar.
**Anti-patrón:** Agentes tan especializados que el routing falla constantemente.

---

## 20.4 Patrón: Orchestrator + Workers

Main delega a un orchestrator que distribuye trabajo a workers paralelos.

```
Main → Orchestrator (depth 1, Sonnet)
           ├── Worker-1 (depth 2, Haiku)
           ├── Worker-2 (depth 2, Haiku)
           └── Worker-3 (depth 2, Haiku)
```

**Config:**
```json5
{
  agents: { defaults: { subagents: { maxSpawnDepth: 2, maxChildrenPerAgent: 5 } } }
}
```

**Cuándo:** Tareas que se dividen en subtareas independientes (research, code review multi-file, análisis multi-fuente).
**Trade-off:** Latencia acumulada (orchestrator espera workers). Costo de múltiples context windows.
**Anti-patrón:** Usar orchestrator para 2 subtareas simples (flat spawn es suficiente).

**Detalle:** Cap. 10 completo.

---

## 20.5 Patrón: Reader Agent (Sandboxed) → Main Agent (Trusted)

Contenido externo hostil procesado por un agente sin tools peligrosos.

```
Contenido externo (web, email, docs)
         │
         ▼
Reader Agent (sandbox + read-only + no exec)
         │
         ▼
Summary (texto limpio, sin instrucciones hostiles)
         │
         ▼
Main Agent (full tools, trusted)
```

**Config:**
```json5
{
  agents: {
    list: [
      { id: "main", default: true, sandbox: { mode: "off" } },
      {
        id: "reader",
        sandbox: { mode: "all", scope: "agent", workspaceAccess: "none" },
        tools: {
          allow: ["web_fetch", "web_search", "read", "group:memory"],
          deny: ["exec", "write", "edit", "browser", "cron", "gateway",
                 "sessions_spawn", "sessions_send", "message"]
        }
      }
    ]
  }
}
```

**Cuándo:** Tu agente procesa emails, web pages, o documentos de fuentes no controladas.
**Trade-off:** Dos agent turns en vez de uno. Latencia adicional.
**Anti-patrón:** Dar al reader agent `exec` o `message` (derrota el propósito).

---

## 20.6 Patrón: Cron + Webhook Pipeline

Automatización event-driven con delivery a canal.

```
Gmail → GCP Pub/Sub → gog-gmail-watch → /hooks/gmail → Agent turn → Telegram
                                                              │
CI/CD ─────────────────────────────► /hooks/agent → Agent turn → Telegram
                                                              │
Cron (7 AM) ──────────────────────► Agent turn (isolated) ───► Telegram
```

**Config:** Ver Cap. 13 (cron) + Cap. 16 (webhooks).

**Cuándo:** Quieres un agente reactivo a eventos externos + proactivo con schedules.
**Trade-off:** Más moving parts (webhook tokens, services, Pub/Sub subscriptions).
**Anti-patrón:** Todo en heartbeat cuando necesitas timing preciso o delivery aislada.

---

## 20.7 Patrón: KODA → OpenClaw Mapping

Para setups que usan el framework KODA de agentes declarativos:

| KODA | OpenClaw |
|------|----------|
| `identity` + `safety` | `SOUL.md` |
| `state_machine` + `CMs` | `AGENTS.md` |
| KB artifacts (CM-KB-GUIDANCE) | `skills/` (SKILL.md) |
| HOA fleet spawn | `sessions_spawn` |
| Persistent personas (Tier 1) | `agents.list[]` en openclaw.json |
| On-demand workers (Tier 2) | `sessions_spawn` con model override |

**Tiers:**
- **Tier 1 — Persistentes** (`agents.list[]`): goreologo, medico-urgencias, arquitecto-gore → sesiones long-lived, contexto acumulado
- **Tier 2 — On-demand** (`sessions_spawn`): tareas específicas → aisladas, model-selectable, auto-archive

---

## 20.8 Patrón: Minimal Viable Agent

El setup más simple posible para empezar:

```json5
{
  gateway: {
    auth: { mode: "token", token: "long-random-token" }
  },
  channels: {
    telegram: {
      botToken: "${TELEGRAM_BOT_TOKEN}",
      dmPolicy: "allowlist",
      allowFrom: ["tg:YOUR_USER_ID"]
    }
  }
}
```

Un canal, un agente implícito, default model, sin sandbox, sin cron, sin webhooks. **Empieza aquí y agrega complejidad según la necesites.**

---

## Resumen: Selector de Patrones

```
¿Qué necesitas?
│
├── Solo chatear conmigo → 20.8 Minimal Viable
│
├── Chatear desde múltiples canales → 20.1 Single + Multi-channel
│
├── Diferentes propósitos/personas → 20.2 Agent per Persona
│
├── Tareas paralelas pesadas → 20.4 Orchestrator + Workers
│
├── Procesar contenido hostil → 20.5 Reader Agent
│
├── Reaccionar a eventos externos → 20.6 Cron + Webhook Pipeline
│
├── Framework KODA → 20.7 KODA Mapping
│
└── No sé → 20.8 Minimal → iterar
```

---

*Siguiente: [Capítulo 21 — Decisiones de Arquitectura](21-decisiones-arquitectura.md)*

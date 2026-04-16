# Arquitectura Multi-Agente / Multi-Tenant / Multi-OpenClaw sobre Slack

*Documento de diseño — 2026-02-23*
*Basado en: Manual OpenClaw (Cap. 6, 8, 9, 11, 20, 22) + Slack API Docs*

---

## 1. Decisión de plan Slack

### Recomendación: **Slack Pro** ($7.25 USD/usuario/mes)

| Criterio | Free | Pro | Business+ |
|---|---|---|---|
| Historial de mensajes | 90 días | ∞ | ∞ |
| Integraciones (apps) | 10 | ∞ | ∞ |
| AI (summaries, huddle notes) | ❌ | ✅ | ✅ |
| SAML SSO / SCIM | ❌ | Solo con Salesforce | ✅ |
| Admin avanzado | ❌ | Básico | ✅ |
| Socket Mode apps | ✅ | ✅ | ✅ |
| Precio (1 usuario) | $0 | ~$7.25/mes | ~$12.50/mes |

**¿Por qué Pro y no Free?**
- Free limita a **10 integraciones** (apps). Con N OpenClaw = N apps, más gog, más webhooks, se agota rápido.
- Free tiene **90 días de historial**. Para auditoría y trazabilidad de agentes, necesitas historial completo.

**¿Por qué Pro y no Business+?**
- Business+ agrega gobernanza enterprise (SSO, compliance, admin avanzado) que no necesitas como usuario individual.
- Si escala a equipo/organización → migrar a Business+.

**Costo real:** 1 humano × $7.25/mes = **$7.25 USD/mes**. Los bots no cuentan como seats.

---

## 2. Tres patrones arquitectónicos (de menor a mayor complejidad)

```
Complejidad creciente →

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Patrón A    │    │  Patrón B    │    │  Patrón C    │
│              │    │              │    │              │
│  Multi-Agent │    │ Multi-Agent  │    │Multi-Gateway │
│  Single GW   │    │ + Sub-agents │    │  Federation  │
│  Single App  │    │ Multi-App    │    │  Multi-App   │
│              │    │              │    │              │
│  ⭐⭐         │    │  ⭐⭐⭐        │    │  ⭐⭐⭐⭐⭐      │
└──────────────┘    └──────────────┘    └──────────────┘
```

### Recomendación: **Patrón B** (multi-agent + sub-agents, multi-app Slack)

Razón: máxima flexibilidad con complejidad manejable. Un solo proceso gateway, múltiples cerebros aislados, delegación paralela vía sub-agents, y cada agente con su bot Slack propio para identidad visual clara.

---

## 3. Patrón A: Multi-Agent, Single Gateway, Single App

### Diagrama de arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                   Slack Workspace (Pro)                   │
│                                                          │
│  #control    #gore    #clinic    #ops    #alerts-audit   │
│      │          │         │        │          │          │
│      └──────────┴─────────┴────────┴──────────┘          │
│                         │                                │
│              ┌──────────┴──────────┐                     │
│              │   Slack App "Korax" │                      │
│              │   (Socket Mode)     │                      │
│              │   xoxb + xapp       │                      │
│              └──────────┬──────────┘                     │
└─────────────────────────┼───────────────────────────────┘
                          │ WebSocket
                          ▼
┌─────────────────────────────────────────────────────────┐
│              OpenClaw Gateway (VPS Hetzner)               │
│                                                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │ Agent    │ │ Agent    │ │ Agent    │ │ Agent    │   │
│  │ "main"  │ │ "gore"   │ │ "clinic" │ │ "ops"    │   │
│  │ Korax   │ │ GoreBot  │ │ ClinicBot│ │ OpsBot   │   │
│  │ Sonnet  │ │ Opus     │ │ Sonnet   │ │ Haiku    │   │
│  │ sandbox │ │ sandbox  │ │ sandbox  │ │ sandbox  │   │
│  │  off    │ │  off     │ │  off     │ │  off     │   │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘   │
│       │            │            │            │          │
│  ┌────┴────────────┴────────────┴────────────┴────┐     │
│  │              BINDINGS (router)                  │     │
│  │  #control  → main                              │     │
│  │  #gore     → gore                              │     │
│  │  #clinic   → clinic                            │     │
│  │  #ops      → ops                               │     │
│  │  #alerts   → main (write), all (read)          │     │
│  │  DM @Korax → main                              │     │
│  └────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────┘
```

**Ventajas:** Un solo bot, setup mínimo, routing por canal.
**Limitaciones:** Todos los agentes comparten identidad visual (mismo avatar/nombre en Slack).

---

### Diagrama Patrón B (recomendado): Multi-Agent + Sub-Agents + Multi-App

```
┌──────────────────────────────────────────────────────────────┐
│                    Slack Workspace (Pro)                       │
│                                                               │
│  #control       #gore        #clinic      #ops    #alerts    │
│      │             │            │           │         │       │
│  ┌───┴───┐    ┌────┴────┐  ┌───┴───┐  ┌───┴───┐     │       │
│  │ @Korax│    │@GoreBot │  │@Clinic│  │@OpsBot│     │       │
│  │ App 1 │    │ App 2   │  │App 3  │  │App 4  │     │       │
│  └───┬───┘    └────┬────┘  └───┬───┘  └───┬───┘     │       │
└──────┼─────────────┼──────────┼────────────┼─────────┼───────┘
       │             │          │            │         │
       └─────────────┴──────────┴────────────┴─────────┘
                              │
                    WebSocket × 4 (Socket Mode)
                              │
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                OpenClaw Gateway (VPS Hetzner)                  │
│                                                               │
│  channels.slack:                                              │
│    accounts:                                                  │
│      default:  { appToken: xapp-1, botToken: xoxb-1 }        │
│      gore:     { appToken: xapp-2, botToken: xoxb-2 }        │
│      clinic:   { appToken: xapp-3, botToken: xoxb-3 }        │
│      ops:      { appToken: xapp-4, botToken: xoxb-4 }        │
│                                                               │
│  agents.list:                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌────────┐ │
│  │main (Korax) │ │gore (GoreOS)│ │clinic (Clin)│ │ops     │ │
│  │             │ │             │ │             │ │        │ │
│  │ Sonnet 4.6  │ │ Opus 4.6    │ │ Sonnet 4.6  │ │Haiku4.5│ │
│  │ ~/clawd     │ │ ~/ws-gore   │ │ ~/ws-clinic │ │~/ws-ops│ │
│  │ full tools  │ │ docs+web    │ │ node air    │ │ exec   │ │
│  │             │ │             │ │ browser node│ │ gateway│ │
│  │ ORCHESTRATE │ │ SPECIALIST  │ │ SPECIALIST  │ │SPECIAL.│ │
│  └──────┬──────┘ └─────────────┘ └─────────────┘ └────────┘ │
│         │                                                     │
│         │  sessions_spawn / sessions_send                     │
│         ├──────────────────────────────────────────┐          │
│         ▼                                          ▼          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Sub-agent   │  │ Sub-agent   │  │ Sub-agent           │  │
│  │ research    │  │ code-review │  │ long-analysis       │  │
│  │ Haiku       │  │ Sonnet      │  │ Opus                │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│                                                               │
│  bindings:                                                    │
│    accountId:"default" → main                                 │
│    accountId:"gore"    → gore                                 │
│    accountId:"clinic"  → clinic                               │
│    accountId:"ops"     → ops                                  │
│                                                               │
│  agentToAgent: { enabled: true, allow: ["main","gore",       │
│                  "clinic","ops"] }                             │
└──────────────────────────────────────────────────────────────┘
```

---

## 4. Flujo de orquestación (Patrón B)

```
┌──────────────────────────────────────────────────────────────┐
│                                                               │
│  Korvo escribe en #control:                                   │
│  "Necesito informe GORE + estado pacientes HSC"               │
│                                                               │
│         │                                                     │
│         ▼                                                     │
│  @Korax (main) recibe, analiza, decide:                       │
│                                                               │
│    ┌──────────────────────────────┐                           │
│    │ 1. sessions_send → gore     │                           │
│    │    "Genera informe avance    │                           │
│    │     proyecto ERD 2024-2030"  │                           │
│    │                              │                           │
│    │ 2. sessions_send → clinic   │                           │
│    │    "Estado pacientes         │                           │
│    │     hospitalizados HSC"      │                           │
│    │                              │                           │
│    │ 3. sessions_spawn            │                           │
│    │    task: "Busca normativa    │                           │
│    │     reciente sobre X"        │                           │
│    │    model: haiku              │                           │
│    └──────────────┬───────────────┘                           │
│                   │                                           │
│    ┌──────────────┼──────────────────────┐                    │
│    ▼              ▼                      ▼                    │
│  Gore-Agent   Clinic-Agent         Sub-agent                  │
│  #gore        #clinic              (background)               │
│  "Informe     "Conectando          "Buscando                 │
│   generado"    vía nodo air..."     normativa..."             │
│    │              │                      │                    │
│    ▼              ▼                      ▼                    │
│  Resultado    Resultado             Announce                  │
│  → #gore      → #clinic            → #control                │
│  + notify     + notify              (automático)              │
│    main         main                                          │
│    │              │                      │                    │
│    └──────────────┴──────────────────────┘                    │
│                   │                                           │
│                   ▼                                           │
│  @Korax sintetiza en #control:                                │
│  "Resumen integrado: ..."                                     │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## 5. Modelo de permisos y seguridad

```
┌─────────────────────────────────────────────────────┐
│              CAPAS DE SEGURIDAD                      │
│                                                      │
│  Slack Layer:                                        │
│  ┌─────────────────────────────────────────────┐     │
│  │ App Scopes (por bot):                       │     │
│  │  chat:write, channels:history,              │     │
│  │  app_mentions:read, reactions:write,        │     │
│  │  users:read, files:read, files:write        │     │
│  │                                             │     │
│  │ Canal:                                      │     │
│  │  Cada bot invitado SOLO a sus canales       │     │
│  │  @Korax  → #control, #alerts-audit          │     │
│  │  @Gore   → #gore, #alerts-audit             │     │
│  │  @Clinic → #clinic, #alerts-audit           │     │
│  │  @Ops    → #ops, #alerts-audit              │     │
│  └─────────────────────────────────────────────┘     │
│                                                      │
│  OpenClaw Layer:                                     │
│  ┌─────────────────────────────────────────────┐     │
│  │ Per-agent:                                  │     │
│  │  main:   tools=full, vis=agent              │     │
│  │  gore:   tools=docs+web, vis=self           │     │
│  │  clinic: tools=node+browser, vis=self       │     │
│  │  ops:    tools=exec+gateway, vis=all        │     │
│  │                                             │     │
│  │ Agent-to-agent: allowlist bidireccional     │     │
│  │  main ↔ gore, main ↔ clinic, main ↔ ops    │     │
│  │  gore ✗ clinic (no directo)                 │     │
│  │                                             │     │
│  │ Sub-agents: solo main puede spawn           │     │
│  │  maxConcurrent: 8                           │     │
│  │  maxSpawnDepth: 1                           │     │
│  └─────────────────────────────────────────────┘     │
│                                                      │
│  Host Layer:                                         │
│  ┌─────────────────────────────────────────────┐     │
│  │ sandbox.mode: off (main, gore)              │     │
│  │ sandbox.mode: off (clinic — necesita node)  │     │
│  │ sandbox.mode: off (ops — necesita exec)     │     │
│  │                                             │     │
│  │ Gateway auth token 256-bit                  │     │
│  │ Tailscale loopback                          │     │
│  │ sudo denylist para clawdbot                 │     │
│  └─────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
```

---

## 6. Diseño de canales Slack

```
┌─────────────────────────────────────────────────────┐
│                 SLACK WORKSPACE                       │
│                                                      │
│  ┌──────────────────┐  Propósito                     │
│  │ #control         │  Korvo ↔ Korax (orquestación)  │
│  │ #gore            │  Trabajo GORE Ñuble            │
│  │ #clinic          │  DAU/SGH/hospital              │
│  │ #ops             │  Infraestructura/monitoring    │
│  │ #alerts-audit    │  Eventos críticos (todos escriben) │
│  │ #lab-sandbox     │  Experimentos/research          │
│  └──────────────────┘                                │
│                                                      │
│  Convención: mention-gating ON en todos los canales  │
│  Excepción: #alerts-audit = write-only para bots     │
└─────────────────────────────────────────────────────┘
```

---

## 7. Diseño de agentes

### Matriz agente × canal × tools × modelo

| Agente | Canal primario | Modelo | Tools clave | Workspace |
|---|---|---|---|---|
| **main** (Korax) | #control, DM | Sonnet 4.6 | full + sessions_spawn + agent-to-agent | ~/clawd |
| **gore** | #gore | Opus 4.6 | web, docs, memory, gog | ~/ws-gore |
| **clinic** | #clinic | Sonnet 4.6 | nodes (air), browser (node), memory | ~/ws-clinic |
| **ops** | #ops | Haiku 4.5 | exec, gateway, healthcheck, cron | ~/ws-ops |

### Matriz agente × agente (comunicación)

```
        main    gore    clinic    ops
main     —       ✅       ✅       ✅
gore     ✅       —       ❌       ❌
clinic   ✅       ❌       —       ❌
ops      ✅       ❌       ❌       —
```

Hub-and-spoke: solo main habla con todos. Especialistas solo hablan con main.

---

## 8. Patrón C: Multi-Gateway Federation (futuro)

```
┌─────────────────────────────────────────────────────────────┐
│                    SERVIDOR (VPS Hetzner)                     │
│                                                              │
│  ┌──────────── Docker Network: openclaw-fed ──────────────┐  │
│  │                                                        │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │  │
│  │  │ GW:Korax │  │ GW:Gore  │  │ GW:Clinic│            │  │
│  │  │ :18789   │  │ :18809   │  │ :18829   │            │  │
│  │  │          │  │          │  │          │            │  │
│  │  │ Slack    │  │ Webhook  │  │ Slack    │            │  │
│  │  │ App 1    │  │ only     │  │ App 3    │            │  │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘            │  │
│  │       │             │             │                   │  │
│  │  ┌────┴─────────────┴─────────────┴──────────────┐    │  │
│  │  │        Shared Volumes (:ro)                    │    │  │
│  │  │  /srv/koda/knowledge                           │    │  │
│  │  │  /srv/shared-docs                              │    │  │
│  │  │  /srv/comms (inter-gateway mailbox :rw)        │    │  │
│  │  └────────────────────────────────────────────────┘    │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                              │
│  Comunicación inter-gateway:                                 │
│  Korax → POST http://goreos-gw:18809/hooks/agent             │
│  Gore  → POST http://korax-gw:18789/hooks/wake               │
└─────────────────────────────────────────────────────────────┘
```

**Cuándo escalar a Patrón C:**
- Fault isolation real (un gateway caído no afecta otros)
- Rolling updates sin downtime total
- Resource isolation (CPU/RAM por gateway)
- Diferentes versiones de OpenClaw por especialista

**No necesario ahora.** Patrón B cubre el caso actual.

---

## 9. Roadmap de implementación

```
Fase 0 — Diseño (este documento)                    ✅ Hoy
    │
    ▼
Fase 1 — Slack base + Korax conectado
    • Crear workspace Pro
    • Crear Slack App #1 (Korax)
    • Configurar Socket Mode
    • Crear canales base (#control, #alerts-audit)
    • Conectar OpenClaw actual a Slack
    • Validar: mensajes bidireccionales
    │
    ▼
Fase 2 — Multi-agent + canales de dominio
    • Crear 3 Slack Apps adicionales (Gore, Clinic, Ops)
    • Crear canales (#gore, #clinic, #ops)
    • Configurar agents.list + bindings + workspaces
    • Configurar agent-to-agent
    • Validar: routing correcto por canal/bot
    │
    ▼
Fase 3 — Orquestación + sub-agents
    • Configurar sub-agents en main
    • Probar delegación main → especialistas
    • Probar sub-agents paralelos
    • Configurar #alerts-audit como sink compartido
    │
    ▼
Fase 4 — Hardening
    • Tool policy per-agent
    • Auditoría de permisos Slack
    • Runbooks de operación
    • Monitoreo/alertas
    │
    ▼
Fase 5 (opcional) — Federation (Patrón C)
    • Docker Compose multi-gateway
    • Webhook relay inter-gateway
    • Shared volumes para KB
```

---

## 10. Scopes Slack necesarios (por app)

### Scopes comunes (todas las apps)

**Bot Token Scopes:**
- `app_mentions:read` — detectar @mentions
- `channels:history` — leer mensajes en canales públicos
- `channels:read` — listar canales
- `chat:write` — enviar mensajes
- `chat:write.customize` — nombre/avatar custom por agente
- `files:read` — leer adjuntos
- `files:write` — enviar archivos
- `groups:history` — leer canales privados
- `groups:read` — listar canales privados
- `im:history` — leer DMs
- `im:read` — listar DMs
- `im:write` — abrir DMs
- `reactions:read` — leer reacciones
- `reactions:write` — agregar reacciones
- `users:read` — resolver nombres de usuario

**App-Level Token:**
- `connections:write` — requerido para Socket Mode

**Bot Events (subscriptions):**
- `app_mention`
- `message.channels`, `message.groups`, `message.im`
- `reaction_added`, `reaction_removed`
- `member_joined_channel`

---

## 11. Contrato de mensajes inter-agente

```yaml
# Delegación (main → especialista)
task_id: T-YYYYMMDD-###
from: main
to: gore
priority: P1|P2|P3
objective: >
  Descripción clara de la tarea
constraints:
  - Restricción 1
  - Restricción 2
deliverable_format: markdown
deadline_utc: "ISO-8601"
definition_of_done:
  - Criterio 1
  - Criterio 2

# Respuesta (especialista → main)
task_id: T-YYYYMMDD-###
status: done|blocked|partial
summary: >
  Resumen ejecutivo
evidence:
  - fuente: ...
risks:
  - riesgo identificado
next_actions:
  - acción sugerida
```

---

*Documento guardado en `cabinet/docs/architecture-multi-openclaw-slack.md`*

# OpenClaw — Cheatsheet Definitivo
> Agentes · Multi-Agente · Orquestación · Automatización · Seguridad
> *370KB destilados en una página*

---

## 🏗️ ARQUITECTURA

```
Gateway (1 proceso)
├── Channel Connectors (Telegram, WhatsApp, Discord, Slack, Signal, iMessage)
├── Agent Runtime (inference + tools + sessions)
├── Automation Engine (cron + heartbeat + hooks + webhooks)
├── WebSocket API + HTTP (Control UI, Canvas, Hooks) ← mismo puerto
└── Session Store (JSONL en disco)
```

**Agent Loop:** intake → queue → session prep → prompt assembly → model inference → tool exec (loop) → reply shape → persist

**Serialización:** 1 run activo por sesión. Queue modes: `collect` (default) | `steer` | `followup`

---

## 🤖 ANATOMÍA DEL AGENTE

```
Agente = Workspace + AgentDir + Config + Identity Runtime

Workspace (~/clawd/)           → personalidad, memoria, skills (versionable en git)
AgentDir (~/.openclaw/agents/) → auth-profiles.json, sessions/ (NUNCA en git)
Config (openclaw.json)         → declaración: modelo, sandbox, tools, heartbeat
Identity Runtime (in-memory)   → skills snapshot, tool policy resuelta
```

### Bootstrap Files (inyectados en cada turn)

| Archivo | Main | Sub-agent | Propósito |
|---------|------|-----------|-----------|
| AGENTS.md | ✅ | ✅ | Reglas operativas |
| TOOLS.md | ✅ | ✅ | Cheat sheet de tools |
| SOUL.md | ✅ | ❌ | Personalidad |
| USER.md | ✅ | ❌ | Perfil del usuario |
| IDENTITY.md | ✅ | ❌ | Nombre, vibe |
| HEARTBEAT.md | ✅ | ❌ | Checklist periódico |
| MEMORY.md | ✅* | ❌ | Memoria curada (*solo sesión main privada) |

⚠️ **Cada char en bootstrap se paga en cada turn.** Truncation a 20K chars/archivo (silenciosa).

---

## 📋 SESIONES

### Session Keys

| Origen | Key |
|--------|-----|
| DM (main) | `agent:<id>:main` |
| DM (per-peer) | `agent:<id>:dm:<peerId>` |
| DM (per-channel-peer) | `agent:<id>:<channel>:dm:<peerId>` |
| Grupo | `agent:<id>:<channel>:group:<groupId>` |
| Cron | `cron:<jobId>` |
| Sub-agente | `agent:<id>:subagent:<uuid>` |

**Key = estable** (canal lógico). **ID = UUID** (cambia con `/new`).

### DM Scope — LA decisión de seguridad #1

| Scope | Cuándo |
|-------|--------|
| `main` | Solo tú. Máxima continuidad |
| `per-channel-peer` | **>1 persona. Obligatorio.** |
| `per-peer` | Unificar cross-channel + identity links |

### Gestión de Contexto

```
Pruning (in-memory, auto)  →  tool results viejos recortados (no toca JSONL)
Compaction (persistente)   →  resumen narrativo reemplaza historial antiguo
Memory Flush (pre-compact) →  turn silencioso para escribir a disco antes de resumir
Reset (/new)               →  nuevo sessionId, memoria en disco intacta
```

---

## 🧠 MODELOS Y FAILOVER

```
Request → Override sesión? → Override agente? → Primary → Fallback 1 → Fallback 2 → Error
                                                  │
                                           Auth profile rotation
                                           (round-robin + session stickiness)
```

**Cooldown:** 1min → 5min → 25min → 1h (cap). **Billing disable:** 5h → 10h → 24h.

**Regla:** Diversidad de provider en fallbacks. Si Anthropic cae, OpenAI toma.

| Nivel | Override |
|-------|---------|
| `/model opus` | Sesión |
| `agents.list[].model` | Per-agent |
| Cron/webhook `model:` | Per-job |
| `sessions_spawn({model:})` | Per-sub-agente |

---

## 💾 MEMORIA

```
MEMORY.md (inyectado, cada turn)     ← Hechos durables. Mantener <10KB
memory/*.md (on-demand, via tools)   ← Daily logs, notas, detalles
```

**Búsqueda:** `memory_search` (vector 70% + BM25 30%) → `memory_get` (lectura)

| Post-procesamiento | Cuándo habilitar |
|-------------------|-----------------|
| MMR (diversidad) | >50 daily logs con contenido repetitivo |
| Temporal Decay | >3 meses de historial |

---

## 👥 MULTI-AGENTE

### Bindings (most-specific wins)

```
peer > parentPeer > guildId+roles > guildId > teamId > accountId > channel > default
```

AND semántico. Primer match gana en el mismo tier.

### ¿Necesito multi-agent?

```
Solo yo, misma personalidad    → 1 agente, dmScope: main
Solo yo, diferentes propósitos → Multi-agent por canal/cuenta
Múltiples personas, mismo bot  → dmScope: per-channel-peer (o multi-agent)
Diferentes trust levels        → Multi-agent con sandbox per-agent
```

### Auth Isolation = Invariante

Cada agente: su propio `auth-profiles.json`. Nunca compartir. Blast radius limitado.

---

## 🔒 SEGURIDAD — 3 CONTROLES

```
1. TOOL POLICY  → ¿QUÉ tools existen?      (8 capas, deny siempre gana)
2. SANDBOX      → ¿DÓNDE corren?            (off | non-main | all)
3. ELEVATED     → ¿exec escapa al host?     (solo exec, solo desde sandbox)
```

**Tool policy es el gate principal.** Si denied → nada más importa.

### Sandbox

| Mode | Efecto |
|------|--------|
| `off` | Todo en host |
| `non-main` | **Sweet spot:** DMs en host, grupos/cron en Docker |
| `all` | Todo en Docker |

| Scope | Containers |
|-------|-----------|
| `session` | 1 por sesión (máx aislamiento) |
| `agent` | 1 por agente |
| `shared` | 1 para todos |

| workspaceAccess | Ve | Escribe |
|----------------|-----|---------|
| `none` | Sandbox workspace | Solo sandbox |
| `ro` | Agent workspace (read-only) | ❌ |
| `rw` | Agent workspace (read-write) | ✅ |

### Tool Profiles

| Profile | Tools |
|---------|-------|
| `minimal` | Solo `session_status` |
| `coding` | fs + runtime + sessions + memory |
| `messaging` | messaging + sessions básico |
| `full` | Todo |

### Perfiles de seguridad integrados

| Perfil | Sandbox | Tools | Blast radius |
|--------|---------|-------|-------------|
| **Personal** | off | full | Máximo |
| **Coding** | all + rw + network | coding | Container + workspace |
| **Read-only** | all + ro | read + memory + web | Mínimo (solo lectura) |
| **Messaging** | all + none | messaging | Casi nulo |
| **Público** | all + none + session | minimal | Cero |

### Filosofía

```
IDENTITY first  → ¿Quién puede hablar? (allowlists, pairing)
SCOPE next      → ¿Qué puede hacer? (tools, sandbox, elevated)
MODEL last      → ¿Resiste injection? (Opus > Sonnet > Haiku)
```

---

## 🔀 SUB-AGENTES

### sessions_spawn

```json
{ "task": "...", "label": "...", "model": "haiku", "thinking": "low", "runTimeoutSeconds": 300 }
```

→ Non-blocking. Resultado vía **announce** al chat del parent.

**Sub-agentes reciben:** AGENTS.md + TOOLS.md (prompt minimal). **No reciben:** SOUL.md, USER.md, MEMORY.md.

**Tools:** Todo excepto `sessions_*`, `subagents`, `cron`, `gateway`.

### Orchestrator Pattern (depth 2)

```
Main → Orchestrator (depth 1, recibe session tools)
           ├── Worker (depth 2, leaf, sin session tools)
           ├── Worker
           └── Worker
```

`maxSpawnDepth: 2` | `maxChildrenPerAgent: 5` | `maxConcurrent: 8` (lane separada)

**Announce chain:** Workers → Orchestrator → Main (nunca cross-level)

### Gestión

| Tool/Comando | Qué hace |
|-------------|----------|
| `subagents list` | Listar activos |
| `subagents steer <id> <msg>` | Inyectar en run activo |
| `subagents kill <id\|all>` | Matar (+ cascade a hijos) |
| `/stop` | Kill todo el árbol |

### Costo

```
Main: Sonnet (conversación)  |  Sub-agentes: Haiku (barato)  |  Special: Opus (override)
```

---

## ⏰ AUTOMATIZACIÓN

### Heartbeat vs Cron — Árbol de Decisión

```
¿Timing exacto?
├── SÍ → CRON (--cron "0 7 * * *")
└── NO → ¿Se batchea con otros checks?
         ├── SÍ → HEARTBEAT (agregar a HEARTBEAT.md)
         └── NO → ¿Model override / aislamiento?
                  ├── SÍ → CRON isolated
                  └── NO → HEARTBEAT
```

### Heartbeat

```json5
{ heartbeat: { every: "30m", model: "haiku", target: "last", activeHours: { start: "08:00", end: "23:00" } } }
```

`HEARTBEAT_OK` → suprimido. Alerta → delivery. ~$2.70/mes con Haiku.

### Cron Jobs

| Kind | Ejemplo |
|------|---------|
| `at` | `--at "20m"` (one-shot, auto-delete) |
| `every` | `--every 3600000` (1h interval) |
| `cron` | `--cron "0 7 * * *"` (expresión) |

| Session | Payload | Cuándo |
|---------|---------|--------|
| `main` | `systemEvent` (inyecta en main) | Reminders, con contexto conversacional |
| `isolated` | `agentTurn` (sesión fresh) | Reportes, análisis, model override |

| Delivery | Efecto |
|----------|--------|
| `announce` | Envía a canal de messaging |
| `webhook` | POST a URL |
| `none` | Solo internal |

### Hooks (código, sin LLM, gratis)

```
Events: command:new | agent:bootstrap | gateway:startup | message:received | message:sent
Bundled: session-memory | bootstrap-extra-files | command-logger | boot-md
```

Hooks = TypeScript determinístico. **0 tokens.**

### Webhooks (HTTP ingress)

```
POST /hooks/wake    → System event en main session (ligero)
POST /hooks/agent   → Agent turn aislado con delivery (completo)
POST /hooks/<name>  → Mapped hook con transforms (custom)
```

Auth: `Authorization: Bearer <token>`. Siempre loopback/tailnet.

### Lobster (workflows determinísticos)

```
pipeline: "cmd1 | cmd2 | approve --prompt 'OK?' | cmd3"
```

→ 1 tool call = workflow completo. Approval gates con resume tokens. `llm-task` para LLM steps JSON-only.

---

## 🔧 OPERACIONES

```bash
openclaw status --all              # diagnóstico general
openclaw doctor --fix              # fixes automáticos
openclaw security audit --deep     # auditoría completa
openclaw sessions --active 60      # sesiones activas
openclaw sandbox explain --agent X # tools resueltos
openclaw cron list                 # jobs programados
openclaw agents list --bindings    # routing de agentes
```

### Gateway (systemd)

```bash
sudo systemctl status|restart openclaw-gateway
sudo journalctl -u openclaw-gateway -f
curl -s http://localhost:18789/health
```

### Backup (lo crítico)

```bash
tar -czvf ~/backups/openclaw-$(date +%Y%m%d).tar.gz \
  ~/.openclaw/openclaw.json ~/.openclaw/.env \
  ~/.openclaw/agents/*/agent/auth-profiles.json \
  ~/.openclaw/credentials/ ~/.openclaw/cron/jobs.json \
  ~/clawd/
```

---

## 📐 PATRONES RÁPIDOS

| Patrón | Config clave |
|--------|-------------|
| **Single + multi-channel** | 1 agente, `dmScope: main` |
| **Agent per persona** | `agents.list[]` + bindings por peer |
| **Orchestrator + workers** | `maxSpawnDepth: 2` |
| **Reader agent** | Sandbox + deny exec/write → summary → main |
| **Cron + webhook pipeline** | Cron isolated + /hooks/agent |
| **Minimal viable** | 1 canal + 1 agente + token |

---

## ⚡ REGLAS DE ORO

1. **Cada char en bootstrap se paga en cada turn** → MEMORY.md < 10KB
2. **Tool schemas son invisibles pero costosos** → menos tools = menos tokens
3. **Deny siempre gana** → nunca se re-habilita en capas posteriores
4. **Session key determina aislamiento** → mismo key = mismo contexto
5. **>1 persona + dmScope:main = leak** → per-channel-peer obligatorio
6. **Identity first, model last** → allowlists > prompt hardening
7. **Content = attack surface** → no solo los senders, todo lo que el agente lee
8. **Si no está escrito, no existe** → archivos > RAM
9. **Non-main es el sweet spot** → DMs en host, grupos en sandbox
10. **Diversidad de provider en fallbacks** → si uno cae, otro toma

---

---

## 🌐 FEDERACIÓN MULTI-GATEWAY (Docker)

**Cuándo:** Fault isolation real, rolling updates, resource limits per-agent, diferentes versiones.

```
Docker Compose + bridge network + shared volumes (:ro) + webhooks
```

| Patrón | Comunicación | Latencia | Tolerancia |
|--------|-------------|----------|-----------|
| **Webhook relay** | POST /hooks/agent | ~1-5s | Baja (GW destino debe estar up) |
| **Buzón de archivos** | Volumen compartido + heartbeat | ~30s-30min | Alta (mensajes persisten) |
| **Docker network** | HTTP directo por nombre de container | ~1-5s | Baja |

**Topología recomendada:** Hub (Korax) + Spokes (especialistas webhook-only)

```yaml
# Template: spoke en docker-compose.yml
spoke-gateway:
  image: openclaw:local
  networks: [openclaw-federation]
  ports: ["127.0.0.1:18809:18809"]
  volumes:
    - spoke-state:/home/node/.openclaw
    - ./workspaces/spoke:/home/node/.openclaw/workspace
    - /srv/koda/knowledge:/shared/koda:ro           # KB compartida
    - /srv/comms:/shared/comms:rw                    # buzón inter-gateway
```

**Seguridad:** Tokens dedicados por gateway · Red Docker internal · KB en :ro · Content wrapping · Anti-loop con depth header

---

*`cabinet/docs/manual-openclaw/` — 22 capítulos + 5 apéndices — ~395KB — Feb 2026*

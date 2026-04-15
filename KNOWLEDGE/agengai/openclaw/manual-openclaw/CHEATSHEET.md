---
_manifest:
  urn: urn:agengai:kb:cheatsheet
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- cheatsheet
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:agengai:kb:cheatsheet
---

# OpenClaw — Cheatsheet Definitivo

> Agentes · Multi-Agente · Orquestación · Automatización · Seguridad
> *Alineado con la documentación oficial local al 2026-03-14*

- ---

## 🏗️ ARQUITECTURA

```
Gateway (1 proceso)
├── Channel Connectors (Telegram, WhatsApp, Discord, Slack, Signal, iMessage)
├── Agent Runtime (inference + tools + sessions)
├── Automation Engine (cron + heartbeat + hooks + webhooks)
├── WebSocket API + HTTP (Control UI, Canvas, Hooks) ← mismo puerto
└── Session Store (JSONL en disco)
```

- **Agent Loop:** intake → queue → session prep → prompt assembly → model inference → tool exec (loop) → reply shape → persist

- **Serialización:** 1 run activo por sesión.
- Queue modes: `collect` (default) | `steer` | `followup`

- ---

## 🤖 ANATOMÍA DEL AGENTE

```
Agente = Workspace + AgentDir + Config + Identity Runtime

Workspace (~/clawd/) → personalidad, memoria, skills (versionable en git)
AgentDir (~/.openclaw/agents/) → auth-profiles.json, sessions/ (NUNCA en git)
Config (openclaw.json) → declaración: modelo, sandbox, tools, heartbeat
Identity Runtime (in-memory) → skills snapshot, tool policy resuelta
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

- ⚠️ **Cada char en bootstrap se paga en cada turn.** Truncation a 20K chars/archivo (silenciosa).

- ---

## 📋 SESIONES

### Session Keys

| Origen | Key |
|--------|-----|
| DM (main) | `agent:<id>:main` |
| DM (per-peer) | `agent:<id>:direct:<peerId>` |
| DM (per-channel-peer) | `agent:<id>:<channel>:direct:<peerId>` |
| Grupo | `agent:<id>:<channel>:group:<groupId>` |
| Cron | `cron:<jobId>` |
| Sub-agente | `agent:<id>:subagent:<uuid>` |

- **Key = estable** (canal lógico). **ID = UUID** (cambia con `/new`).
- `openclaw sessions cleanup --dry-run|--enforce` mantiene `sessions.json` y transcripts bajo control.

### DM Scope — LA decisión de seguridad #1

| Scope | Cuándo |
|-------|--------|
| `main` | Solo tú. Máxima continuidad |
| `per-channel-peer` | **>1 persona. Obligatorio.** |
| `per-peer` | Unificar cross-channel + identity links |

### Gestión de Contexto

```
Pruning (in-memory, auto) → tool results viejos recortados (no toca JSONL)
Compaction (persistente) → resumen narrativo reemplaza historial antiguo
Memory Flush (pre-compact) → turn silencioso para escribir a disco antes de resumir
Reset (/new) → nuevo sessionId, memoria en disco intacta
```

- ---

## 🧠 MODELOS Y FAILOVER

```
Request → Override sesión? → Override agente? → Primary → Fallback 1 → Fallback 2 → Error
 │
 Auth profile rotation
 (round-robin + session stickiness)
```

- **Cooldown:** 1min → 5min → 25min → 1h (cap). **Billing disable:** 5h → 10h → 24h.

- **Regla:** Diversidad de provider en fallbacks.
- Si Anthropic cae, OpenAI toma.

| Nivel | Override |
|-------|---------|
| `/model opus` | Sesión |
| `agents.list[].model` | Per-agent |
| Cron/webhook `model:` | Per-job |
| `sessions_spawn({model:})` | Per-sub-agente |

- ---

## 💾 MEMORIA

```
MEMORY.md (inyectado, cada turn) ← Hechos durables. Mantener <10KB
memory/*.md (on-demand, via tools) ← Daily logs, notas, detalles
```

- **Búsqueda:** `memory_search` (vector 70% + BM25 30%) → `memory_get` (lectura)
- Gemini Embedding 2 añade memoria multimodal en `extraPaths` y el modo local puede auto-descargar GGUF.

| Post-procesamiento | Cuándo habilitar |
|-------------------|-----------------|
| MMR (diversidad) | >50 daily logs con contenido repetitivo |
| Temporal Decay | >3 meses de historial |

- ---

## 👥 MULTI-AGENTE

### Bindings (most-specific wins)

```
peer > parentPeer > guildId+roles > guildId > teamId > accountId > channel > default
```

- AND semántico.
- Primer match gana en el mismo tier.
- `accountId` omitido = cuenta default; `accountId: "*"` = fallback real channel-wide.

### ¿Necesito multi-agent?

```
Solo yo, misma personalidad → 1 agente, dmScope: main
Solo yo, diferentes propósitos → Multi-agent por canal/cuenta
Múltiples personas, mismo bot → dmScope: per-channel-peer (o multi-agent)
Diferentes trust levels → Multi-agent con sandbox per-agent
```

### Auth Isolation = Invariante

- Cada agente: su propio `auth-profiles.json`.
- Nunca compartir.
- Blast radius limitado.

- ---

## 🔒 SEGURIDAD — 3 CONTROLES

```
1. TOOL POLICY → ¿QUÉ tools existen? (8 capas, deny siempre gana)
2. SANDBOX → ¿DÓNDE corren? (off | non-main | all)
3. ELEVATED → ¿exec escapa al host? (solo exec, solo desde sandbox)
```

- **Tool policy es el gate principal.** Si denied → nada más importa.

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
IDENTITY first → ¿Quién puede hablar? (allowlists, pairing)
SCOPE next → ¿Qué puede hacer? (tools, sandbox, elevated)
MODEL last → ¿Resiste injection? (Opus > Sonnet > Haiku)
```

- ---

## 🔀 SUB-AGENTES

### sessions_spawn

```json
{ "task": "...", "label": "...", "model": "haiku", "thinking": "low", "runTimeoutSeconds": 300 }
```

- → Non-blocking.
- Resultado vía **announce** al chat del parent.
- `thread:true` + `mode:"session"` permiten subagentes ligados a thread (Discord).

- **Sub-agentes reciben:** AGENTS.md + TOOLS.md (prompt minimal). **No reciben:** SOUL.md, USER.md, MEMORY.md.

- **Tools:** Todo excepto `sessions_*`, `subagents`, `cron`, `gateway`.

### Orchestrator Pattern (depth 2)

```
Main → Orchestrator (depth 1, recibe session tools)
 ├── Worker (depth 2, leaf, sin session tools)
 ├── Worker
 └── Worker
```

- `maxSpawnDepth:
- 2` | `maxChildrenPerAgent:
- 5` | `maxConcurrent:
- 8` (lane separada)

- **Announce chain:** Workers → Orchestrator → Main (nunca cross-level)

### Gestión

| Tool/Comando | Qué hace |
|-------------|----------|
| `subagents list` | Listar activos |
| `subagents steer <id> <msg>` | Inyectar en run activo |
| `subagents kill <id\|all>` | Matar (+ cascade a hijos) |
| `/stop` | Kill todo el árbol |

### Costo

```
Main: Sonnet (conversación) | Sub-agentes: Haiku (barato) | Special: Opus (override)
```

- ---

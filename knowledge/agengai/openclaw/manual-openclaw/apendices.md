---
_manifest:
  urn: urn:kora:kb:apendices
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- apendices
lang: es
---

# Apéndices

- ---


## Apéndice A — Referencia Rápida de Configuración

### Estructura mínima de openclaw.json

```json5
{
  // === Gateway ===
  gateway: {
    port: 18789,
    bind: "loopback",
    auth: { mode: "token", token: "${OPENCLAW_GATEWAY_TOKEN}" }
  },

  // === Canales ===
  channels: {
    telegram: {
      botToken: "${TELEGRAM_BOT_TOKEN}",
      dmPolicy: "allowlist",
      allowFrom: ["tg:USER_ID"]
    }
  },

  // === Agentes ===
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      model: {
        primary: "anthropic/claude-sonnet-4-6",
        fallbacks: ["openai-codex/gpt-5.2", "moonshot/kimi-k2.5"]
      },
      sandbox: { mode: "off" },
      heartbeat: { every: "30m", model: "anthropic/claude-haiku-4-5", target: "last" },
      memorySearch: {
        provider: "openai",
        query: { hybrid: { vectorWeight: 0.7, textWeight: 0.3 } }
      }
    },
    list: [
      { id: "main", default: true }
    ]
  },

  // === Sesiones ===
  session: {
    dmScope: "per-channel-peer",
    reset: { mode: "daily", atHour: 4 }
  },

  // === Tools ===
  tools: {
    elevated: { enabled: false }
  },

  // === Hooks ===
  hooks: {
    internal: {
      enabled: true,
      entries: {
        "session-memory": { enabled: true },
        "command-logger": { enabled: true }
      }
    }
  }
}
```

### Campos más usados (quick reference)

| Path | Tipo | Default | Descripción |
|------|------|---------|-------------|
| `gateway.port` | number | 18789 | Puerto del gateway |
| `gateway.bind` | string | "loopback" | Bind mode |
| `gateway.auth.mode` | string | — | "token" \| "password" \| "trusted-proxy" |
| `agents.defaults.model.primary` | string | — | Modelo primario (provider/model) |
| `agents.defaults.model.fallbacks` | string[] | [] | Chain de fallback |
| `agents.defaults.sandbox.mode` | string | "off" | "off" \| "non-main" \| "all" |
| `agents.defaults.heartbeat.every` | string | "30m" | Intervalo de heartbeat |
| `session.dmScope` | string | "main" | "main" \| "per-peer" \| "per-channel-peer" \| "per-account-channel-peer" |
| `session.reset.mode` | string | "daily" | "daily" \| "idle" |
| `tools.profile` | string | — | "minimal" \| "coding" \| "messaging" \| "full" |
| `tools.deny` | string[] | [] | Tools denegados globalmente |
| `tools.elevated.enabled` | bool | false | Habilitar escape de sandbox |
| `hooks.enabled` | bool | false | Habilitar webhooks HTTP |
| `hooks.token` | string | — | Token para webhooks |

- ---


## Apéndice B — Glosario

| Término | Definición |
|---------|-----------|
| **Agent** | Unidad operacional: workspace + auth + sessions + config |
| **Agent Dir** | Directorio de credenciales y sessions per-agent (`~/.openclaw/agents/<id>/`) |
| **Agent Loop** | Pipeline completo de un request: intake → prompt → inference → tools → reply → persist |
| **Announce** | Mensaje de resultado que un sub-agente envía al chat del parent |
| **Auth Profile** | Credencial (API key u OAuth token) almacenada en `auth-profiles.json` |
| **Binding** | Regla de routing: qué agente maneja qué mensajes |
| **Bootstrap File** | Archivo Markdown inyectado en el system prompt (AGENTS.md, SOUL.md, etc.) |
| **Compaction** | Resumen narrativo que reemplaza historial antiguo para liberar context window |
| **Context Window** | Límite de tokens que el modelo puede procesar simultáneamente |
| **Cooldown** | Período de espera exponencial tras fallo de un auth profile |
| **Cron Job** | Tarea programada: at (one-shot), every (intervalo), cron (expresión) |
| **DM Scope** | Cómo se agrupan los DMs en sesiones (main, per-peer, per-channel-peer, per-account-channel-peer) |
| **Elevated** | Modo que permite a exec escapar del sandbox al host |
| **Fallback Chain** | Secuencia de modelos alternativos si el primary falla |
| **Heartbeat** | Agent turn periódico en sesión main para monitoring/proactividad |
| **Hook** | Handler TypeScript que reacciona a eventos del gateway (sin LLM) |
| **Identity Link** | Mapeo de identificadores cross-channel a una identidad canónica |
| **Lane** | Cola de concurrencia (main lane para sesiones, subagent lane para sub-agentes) |
| **Lobster** | Runtime de workflows determinísticos con approval gates |
| **llm-task** | Plugin tool para LLM steps JSON-only dentro de workflows |
| **Main Key** | Session key de la sesión principal del agente (`agent:<id>:main` o custom) |
| **Memory Flush** | Turn silencioso pre-compaction donde el agente escribe notas durables a disco |
| **MMR** | Maximal Marginal Relevance — re-ranking que penaliza duplicados |
| **Node** | Dispositivo remoto (macOS, iOS, Android) conectado via WebSocket |
| **Prompt Assembly** | Proceso de construcción del system prompt (secciones fijas + bootstrap files + runtime) |
| **Pruning** | Poda in-memory de tool results viejos (no destructiva, alineada con prompt cache) |
| **QMD** | Sidecar de búsqueda local-first (BM25 + vectors + reranking) |
| **Resume Token** | Token de Lobster para continuar un workflow pausado en un approval gate |
| **Send Policy** | Reglas que controlan qué sesiones pueden recibir mensajes |
| **Session Key** | Identificador estable de una sesión (`agent:<id>:<rest>`) |
| **Session ID** | UUID que cambia con cada reset (mismo key, nuevo ID) |
| **Skill** | Instrucciones Markdown que el modelo carga on-demand para tareas específicas |
| **Spawn** | Crear un sub-agente via `sessions_spawn` |
| **Stagger** | Offset automático en cron jobs para evitar load spikes |
| **Steer** | Inyectar un mensaje en un sub-agente corriendo |
| **Temporal Decay** | Multiplicador exponencial que favorece resultados recientes en memory search |
| **Tool Policy** | Sistema de 8 capas que determina qué tools están disponibles |
| **Tool Profile** | Preset de tools (minimal, coding, messaging, full) |
| **Tool Schema** | JSON Schema enviado al modelo para cada tool (consume tokens) |
| **Transcript** | Archivo JSONL con la conversación completa de una sesión |
| **Webhook** | Endpoint HTTP que sistemas externos pueden llamar para trigger acciones |
| **Workspace** | Directorio del agente con bootstrap files, memoria, skills, y proyectos |

- ---


## Apéndice C — Checklist de Setup Multi-Agente

### Pre-requisitos

- [ ] OpenClaw instalado y funcionando con single agent
- [ ] Al menos 1 canal configurado y funcionando
- [ ] Auth profiles configurados para el modelo primary

### Paso a paso

1. **Definir agentes**
   ```bash
   mkdir -p ~/.openclaw/workspace-work
   mkdir -p ~/.openclaw/workspace-family
   ```

2. **Configurar agents.list[] en openclaw.json**
   - id, workspace, model, sandbox, tools por agente
   - Exactamente un agente con `default: true`

3. **Configurar bindings**
   - Más específico primero
   - Cubrir todos los canales/cuentas esperados

4. **Auth per-agent**
   ```bash
   openclaw models auth login --provider anthropic --agent work
   openclaw models auth login --provider anthropic --agent family
   ```

5. **Bootstrap files per-agent**
   - Crear AGENTS.md, SOUL.md en cada workspace
   - Opcionalmente: IDENTITY.md, USER.md, TOOLS.md

6. **Verificar**
   ```bash
   openclaw agents list --bindings
   openclaw sandbox explain --agent work
   openclaw sandbox explain --agent family
   openclaw security audit
   ```

7. **Restart gateway**
   ```bash
   sudo systemctl restart openclaw-gateway
   ```

8. **Test**
   - Enviar DM desde cada canal → verificar que llega al agente correcto
   - Enviar en cada grupo → verificar routing
   - Verificar que cada agente tiene los tools esperados

- ---


## Apéndice D — Checklist de Seguridad (Auditoría Express)

### Identity (quién habla)

- [ ] `dmPolicy` ≠ `"open"` (o deliberado con justificación)
- [ ] `allowFrom` no incluye `"*"` (o deliberado)
- [ ] `dmScope` ≠ `"main"` si >1 persona puede enviar DMs
- [ ] Grupos con `requireMention: true`
- [ ] `groupAllowFrom` configurado si el grupo es semi-público

### Scope (qué puede hacer)

- [ ] `gateway` y `cron` tools denied para agentes no-personales
- [ ] `sessions_spawn` y `sessions_send` denied para agentes untrusted
- [ ] `exec` denied o sandboxed para agentes públicos
- [ ] `browser` denied o con profile dedicado
- [ ] `elevated.enabled: false` (o con allowFrom tight)
- [ ] `workspaceAccess` ≠ `"rw"` para agentes untrusted

### Network

- [ ] `gateway.bind: "loopback"` (o justificación para otro)
- [ ] Gateway auth token configurado y ≥32 chars
- [ ] Webhook token separado del gateway token
- [ ] `hooks.allowRequestSessionKey: false`
- [ ] `discovery.mdns.mode: "minimal"` o `"off"`
- [ ] No hay ports expuestos innecesariamente

### Disco

- [ ] `~/.openclaw/` permisos `700`
- [ ] `openclaw.json` permisos `600`
- [ ] `.env` permisos `600`
- [ ] No está en carpeta synced (Dropbox, iCloud, Google Drive)
- [ ] Full-disk encryption en el host

### Plugins

- [ ] Solo plugins de confianza instalados
- [ ] `plugins.allow` explícito si hay plugins

### Run

```bash
openclaw security audit --deep
```

- ---


## Apéndice E — Mapeo KODA → OpenClaw

### Tabla de equivalencias

| Concepto KODA | OpenClaw Equivalent | Notas |
|--------------|-------------------|-------|
| **Agent Identity** (`identity`) | `SOUL.md` + `IDENTITY.md` | Personalidad, nombre, vibe |
| **Safety Rules** (`safety`) | `SOUL.md` boundaries + tool policy | Safety = prompt soft + tools hard |
| **State Machine** (`state_machine`) | `AGENTS.md` | Reglas operativas, convenciones |
| **Cognitive Modules** (`CMs`) | `AGENTS.md` sections | Instrucciones por dominio |
| **CM-KB-GUIDANCE** | `skills/` (SKILL.md por tema) | Instrucciones on-demand |
| **Knowledge Base** (`KB`) | `memory/` + `cabinet/docs/` | Archivos indexados por vector search |
| **HOA Fleet Spawn** | `sessions_spawn` | Sub-agentes on-demand |
| **Persistent Personas** | `agents.list[]` (Tier 1) | Agentes long-lived con workspace propio |
| **On-Demand Workers** | `sessions_spawn` (Tier 2) | Tareas aisladas, auto-archive |
| **Protocol** | Tool policy + sandbox | Hard enforcement (no solo prompt) |
| **Content** | Bootstrap files + memory files | Separated: protocol en config, content en files |
| **Orchestration** | `maxSpawnDepth: 2` + subagents tool | Orchestrator pattern (Cap. 10) |
| **Communication** | `sessions_send` + `agent-to-agent` | Messaging inter-sesión (Cap. 11) |

### Migración típica

```
KODA YAML Agent Definition
         │
         ├── identity + safety    → SOUL.md
         ├── state_machine        → AGENTS.md
         ├── CMs guidance         → skills/domain/SKILL.md
         ├── KB files             → memory/ + cabinet/docs/
         ├── Tier 1 personas      → agents.list[] con workspace dedicado
         └── Tier 2 workers       → sessions_spawn con model override
```

### Principios que mapean directamente

| KODA Principle | OpenClaw Implementation |
|---------------|------------------------|
| Estructura es significado | Bootstrap files en Markdown con headers |
| Separación protocolo/contenido | Tool policy (hard) + SOUL.md (soft) |
| YAML es código, LLM es intérprete | Markdown es instrucción, model es executor |
| Genoma (invariantes) | openclaw.json + tool policy |
| Fenotipo (configuraciones) | agents.list[] overrides, /model overrides |

- ---


- *Fin del Manual*


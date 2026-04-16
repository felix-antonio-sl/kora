---
title: OpenClaw Platform Model
status: internal
lang: es
---

# OpenClaw Platform Model

Referencia operativa para el mapeo KORA → OpenClaw. Fuente: documentacion oficial OpenClaw.

## Modelo de Agente

OpenClaw define agentes en `openclaw.json` (JSON5) con workspace de archivos Markdown inyectados en system prompt cada turno.

## Bootstrap Files (Inyeccion)

### Archivos inyectados cada turno (system prompt)

| Archivo | Injected | Sub-agents | Equivalente KORA |
|---------|----------|-----------|------------------|
| AGENTS.md | Siempre | Si | AGENTS.md (FSM + reglas) |
| SOUL.md | Siempre | NO | SOUL.md |
| USER.md | Siempre | NO | USER.md |
| IDENTITY.md | Siempre | NO | Derivado de SOUL.md |
| TOOLS.md | Siempre | Si | TOOLS.md (notas, no control) |
| HEARTBEAT.md | Siempre | NO | Sin equivalente KORA |
| BOOTSTRAP.md | Solo primera vez | NO | Sin equivalente KORA |
| MEMORY.md | Si existe (solo main/private) | NO | Sin equivalente KORA |

**Critico para transmutacion**: Sub-agents solo inyectan `AGENTS.md` + `TOOLS.md`. Los demas archivos son filtrados para mantener contexto reducido.

### Archivos on-demand (no inyectados)

- `memory/YYYY-MM-DD.md` — daily logs, acceso via `memory_search`, `memory_get`
- `skills/` — workspace-specific skills, modelo lee via `read` tool
- `canvas/` — Canvas UI files

### Limites de tamano

| Constraint | Valor | Config key |
|-----------|-------|-----------|
| Max chars por archivo bootstrap | 20,000 | `agents.defaults.bootstrapMaxChars` |
| Max chars total bootstrap | 150,000 | `agents.defaults.bootstrapTotalMaxChars` |
| Truncation warning | once (default) | `agents.defaults.bootstrapPromptTruncationWarning` |

Archivos vacios se omiten. Archivos grandes se truncan con marker.

## Skills

### Formato SKILL.md

```yaml
---
name: skill-name-kebab-case
description: Descripcion breve del skill
user-invocable: true
metadata:
  {
    "openclaw": {
      "emoji": "emoji",
      "requires": { "bins": ["uv"], "env": ["API_KEY"], "config": ["browser.enabled"] },
      "primaryEnv": "API_KEY",
      "always": false,
      "os": ["darwin", "linux"]
    }
  }
---

# Skill Name

Instrucciones del skill en Markdown.
{baseDir} referencia la carpeta del skill.
```

**Nota formato**: Parser soporta SOLO single-line frontmatter keys. `metadata` DEBE ser single-line JSON object.

### Campos frontmatter opcionales

| Campo | Uso |
|-------|-----|
| homepage | URL visible como "Website" en UI macOS |
| user-invocable | true/false (default true). Si true, expuesto como slash command |
| disable-model-invocation | true/false (default false). Si true, excluido del prompt modelo |
| command-dispatch | `tool` — slash command bypasa modelo y dispatch directo a tool |
| command-tool | tool name a invocar cuando command-dispatch: tool |
| command-arg-mode | `raw` (default). Forward raw args string |

### Gating (filtro en load-time)

| Campo | Funcion |
|-------|---------|
| `requires.bins` | Lista de binarios que DEBEN existir en PATH |
| `requires.anyBins` | Lista donde AL MENOS UNO debe existir |
| `requires.env` | Variables de ambiente requeridas (o provistas en config) |
| `requires.config` | Rutas de openclaw.json que deben ser truthy |
| `os` | Lista de plataformas elegibles: darwin, linux, win32 |
| `always` | true = siempre incluir (skip otras gates) |
| `primaryEnv` | Env var asociada con skills.entries.name.apiKey |
| `install` | Array de installer specs (brew/node/go/uv/download) |

Sin `metadata.openclaw`, skill siempre elegible (a menos que deshabilitada en config).

### Precedencia (highest to lowest)

1. `<workspace>/skills` (workspace-specific, per-agent)
2. `~/.openclaw/skills` (managed/local, compartidas)
3. Bundled skills (shipped con install)
4. `skills.load.extraDirs` (lowest)

En name conflicts, workspace wins.

### Config overrides (openclaw.json)

```json5
{
  skills: {
    allowBundled: ["gemini", "peekaboo"],  // whitelist bundled
    entries: {
      "skill-name": {
        enabled: true,          // false deshabilita incluso si bundled
        apiKey: "...",          // o { source: "env", provider, id }
        env: { API_KEY: "..." }, // inyectado solo si no set en proceso
        config: { endpoint: "..." }  // custom per-skill fields
      }
    },
    load: {
      extraDirs: ["~/Projects/skills"],
      watch: true,              // auto-refresh cuando SKILL.md cambia
      watchDebounceMs: 250
    }
  }
}
```

### Token Impact

Base overhead (≥1 skill): 195 caracteres. Per skill: 97 + len(name) + len(description) + len(location).

```
total_chars = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + len(location_escaped))
```

XML escaping expande `& < > " '`. Estimacion ~4 chars/token → 97 chars ≈ 24 tokens per skill.

### Inyeccion en system prompt

Skills elegibles se inyectan como XML compacto:
```xml
<available_skills>
  <skill>
    <name>...</name>
    <description>...</description>
    <location>...</location>
  </skill>
</available_skills>
```

Modelo usa `read` tool para cargar SKILL.md de la location listada.

### Session snapshot

Skills snapshot cuando session comienza. Cambios toman efecto en proxima session nueva (o via hot reload si watcher enabled).

### ClawHub

Registro publico: https://clawhub.com. Install: `clawhub install <slug>`. Update: `clawhub update --all`.

## Sub-agents

### Spawn

Via `sessions_spawn` tool (non-blocking, retorna runId).

Params: task (required), label, agentId, model, thinking, runTimeoutSeconds, thread, mode (run|session), cleanup (delete|keep), sandbox (inherit|require).

### Nesting y profundidad

| Depth | Role | Can spawn? | Tools |
|-------|------|-----------|-------|
| 0 | Main agent | Siempre | Todos |
| 1 | Sub-agent (u orchestrator si depth 2) | Solo si maxSpawnDepth ≥ 2 | Todos excepto session tools (orchestrator: +sessions_spawn) |
| 2 | Leaf worker | Nunca | Todos excepto session tools |

Config:
```json5
{
  agents: {
    defaults: {
      subagents: {
        maxSpawnDepth: 1,          // default (max: 5)
        maxChildrenPerAgent: 5,    // max children activos por session
        maxConcurrent: 8,          // global concurrency lane
        runTimeoutSeconds: 900,    // timeout (0 = sin timeout)
        archiveAfterMinutes: 60,   // auto-archive
        model: "provider/model",   // override modelo sub-agents
        thinking: "low"            // override thinking level
      }
    }
  }
}
```

### Announce protocol

Results fluyen hacia arriba:
1. Depth-2 worker termina → anuncia a parent (depth-1 orchestrator)
2. Depth-1 orchestrator recibe, sintetiza → anuncia a main
3. Main recibe y entrega a usuario

Cada nivel solo ve announces de hijos directos.

Announce payload incluye: status (success/error/timeout), result content, runtime stats, token usage, sessionKey, transcript path.

### Tool policy sub-agents

Default: todos tools excepto session tools. Orchestrators (depth-1 cuando maxSpawnDepth ≥ 2) adicionalmente reciben sessions_spawn, subagents, sessions_list, sessions_history.

Override via:
```json5
{ tools: { subagents: { tools: { deny: ["gateway", "cron"] } } } }
```

### Cascade stop

`/stop` en main cascadea a todos sub-agents y sus hijos. `/subagents kill <id>` cascadea a hijos del target.

### Limitaciones

- Announce es best-effort (perdido si gateway reinicia)
- Sub-agents comparten proceso gateway
- `sessions_spawn` siempre non-blocking
- Sub-agent context solo inyecta AGENTS.md + TOOLS.md
- Max nesting: 5 (recomendado: 2)

## Config Snippet (agents.list entry)

```json5
{
  id: "agent-id",
  name: "Nombre Legible",
  default: true,
  workspace: "~/.openclaw/workspace-id",
  agentDir: "~/.openclaw/agents/id/agent",
  model: "anthropic/claude-sonnet-4-5",  // o { primary, fallbacks }
  identity: {
    name: "Nombre",
    emoji: "emoji",
    theme: "tema",
    avatar: "path/to/avatar.png"
  },
  sandbox: {
    mode: "off",        // off | non-main | all
    scope: "agent"      // session | agent | shared
  },
  tools: {
    profile: "coding",  // minimal | coding | messaging | full
    allow: ["browser"],
    deny: ["canvas"],
    elevated: { enabled: true }
  },
  subagents: {
    maxSpawnDepth: 1,
    maxChildrenPerAgent: 5,
    model: "provider/model",
    allowAgents: ["*"]  // agent ids permitidos para sessions_spawn
  },
  groupChat: {
    mentionPatterns: ["@agent"]
  }
}
```

### Tool profiles

| Profile | Incluye |
|---------|---------|
| minimal | session_status solamente |
| coding | group:fs, group:runtime, group:sessions, group:memory, image |
| messaging | group:messaging, sessions_list/history/send, session_status |
| full | Sin restriccion |

### Tool groups

| Group | Tools |
|-------|-------|
| group:runtime | exec, process |
| group:fs | read, write, edit, apply_patch |
| group:sessions | sessions_list/history/send/spawn, session_status |
| group:memory | memory_search, memory_get |
| group:web | web_search, web_fetch |
| group:ui | browser, canvas |
| group:automation | cron, gateway |

## System Prompt Assembly

### Secciones (en orden)

1. Tooling (tool list + descriptions)
2. Safety (guardrail advisory)
3. Skills (XML list cuando ≥1 eligible)
4. OpenClaw Self-Update
5. Workspace (cwd)
6. Documentation (path a docs locales)
7. Workspace Files (bootstrap injection)
8. Sandbox (si enabled)
9. Current Date/Time (timezone only, cache-stable)
10. Reply Tags (channel-specific)
11. Heartbeats
12. Runtime (host, OS, model, thinking level)
13. Reasoning (visibility + toggle hint)

### Prompt modes

| Mode | Uso | Incluye |
|------|-----|---------|
| full | Agentes principales | Todas las secciones |
| minimal | Sub-agents | Tooling, Safety, Workspace, Sandbox, Date/Time, Runtime. Omite Skills, Memory, Self-Update, Reply Tags, Heartbeats |
| none | Solo identity line | Base identity |

## Multi-agent Routing

```json5
{
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "telegram" } }
  ]
}
```

Orden deterministico: peer > guildId > teamId > accountId-exact > accountId-wildcard > default.

## Sandboxing

| Mode | Descripcion |
|------|-------------|
| off | Sin sandbox |
| non-main | Solo sesiones no-main |
| all | Todas las sesiones |

Scopes: session (per-session), agent (per-agent, default), shared (compartido).

## Reglas de Mapeo KORA → OpenClaw

1. Frontmatter KORA DEBE eliminarse de todos los archivos.
2. `_manifest` KORA no tiene equivalente; se omite.
3. config.json KORA → config-snippet.json5 para agents.list.
4. TOOLS.md KORA se reduce a notas; control real via config tools.allow/deny y tool profiles.
5. Skills KORA: renombrar CM-* a kebab-case, adaptar frontmatter a formato OpenClaw single-line JSON metadata.
6. SOUL.md KORA se split: identidad visual → IDENTITY.md (name, emoji, theme), resto → SOUL.md.
7. Wiring KORA (sub-agentes) → subagents config (maxSpawnDepth, maxChildrenPerAgent, allowAgents).
8. Co-induccion KORA → preservar como instrucciones en AGENTS.md.
9. Sub-agents solo inyectan AGENTS.md + TOOLS.md; no generar archivos innecesarios para sub-agents.
10. Metadata de skills KORA (CM Core) → preservar Proposito, Input/Output, Procedimiento, Signature Output.
11. Skills extendidos KORA (con scripts/, references/, assets/) → copiar fibras adjuntas bajo skills/ del workspace.

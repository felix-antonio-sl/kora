---
_manifest:
  urn: urn:agengai:kb:openclaw-integration
  provenance:
    created_by: kora/transmutador
    created_at: '2026-03-14'
    source: openclaw/docs (snapshot 2026-03)
version: 1.0.0
status: published
tags:
- openclaw
- platform
- integration
- transmutacion
- agentes
lang: es
extensions:
  kora:
    family: reference
    snapshot_date: '2026-03-14'
    disclaimer: Snapshot versionado. Para info actualizada consultar documentacion
      oficial OpenClaw.
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:openclaw-integration
---

# OpenClaw Integration Guide

Guia de integracion KORA → OpenClaw. Snapshot de documentacion oficial para uso del transmutador.

## Modelo de Agente

OpenClaw es una plataforma agentic que funciona como gateway WebSocket multi-canal (WhatsApp, Telegram, Discord, Signal, Slack, etc.) con motor de agentes embebido. Agentes se definen en `openclaw.json` (JSON5) con workspace de archivos Markdown.

## Workspace y Bootstrap

### Archivos bootstrap (inyectados en system prompt)

| Archivo | Inyectado | En sub-agents | Proposito |
|---------|----------|---------------|----------|
| AGENTS.md | Siempre | Si | Instrucciones operativas |
| SOUL.md | Siempre | No | Persona, tono, boundaries |
| USER.md | Siempre | No | Perfil del usuario |
| IDENTITY.md | Siempre | No | Nombre, emoji, tema, avatar |
| TOOLS.md | Siempre | Si | Notas sobre herramientas |
| HEARTBEAT.md | Siempre | No | Checklist heartbeats |
| BOOTSTRAP.md | Solo primera vez | No | Ritual onboarding |
| MEMORY.md | Si existe (solo main/private) | No | Memoria largo plazo curada |

Sub-agents solo inyectan AGENTS.md + TOOLS.md para mantener contexto reducido.

### Limites

| Constraint | Valor default | Config key |
|-----------|---------------|-----------|
| Max chars por archivo | 20,000 | bootstrapMaxChars |
| Max chars total | 150,000 | bootstrapTotalMaxChars |
| Max subagent depth | 5 (recomendado: 2) | subagents.maxSpawnDepth |
| Max children por agent | 5 | subagents.maxChildrenPerAgent |
| Max concurrent global | 8 | subagents.maxConcurrent |
| Agent timeout | 600s | timeoutSeconds |
| Auto-archive sub-agents | 60 min | subagents.archiveAfterMinutes |

## Skills

### Formato SKILL.md

```yaml
---
name: skill-name-kebab-case
description: Que hace y cuando usarla
user-invocable: true
disable-model-invocation: false
metadata:
 { "openclaw": { "emoji": "emoji", "requires": { "bins": [], "env": [], "config": [] }, "primaryEnv": "ENV_VAR", "always": false, "os": ["darwin", "linux"] } }
---
```

Parser soporta SOLO single-line frontmatter keys. metadata DEBE ser single-line JSON.

### Gating

| Campo | Funcion |
|-------|---------|
| requires.bins | Binarios que DEBEN existir en PATH |
| requires.anyBins | Al menos uno debe existir |
| requires.env | Variables de ambiente requeridas |
| requires.config | Rutas openclaw.json truthy |
| os | Plataformas elegibles: darwin, linux, win32 |
| always | true = skip todas las gates |

### Precedencia

1. `<workspace>/skills` (per-agent, highest)
2. `~/.openclaw/skills` (managed/local)
3. Bundled skills
4. `skills.load.extraDirs` (lowest)

### Token impact

```
total_chars = 195 + Σ (97 + len(name) + len(description) + len(location))
```

~4 chars/token. Skills inyectadas como XML compacto en system prompt.

### Config overrides

```json5
{
 skills: {
 allowBundled: ["skill1"],
 entries: {
 "skill-name": {
 enabled: true,
 apiKey: "...",
 env: { KEY: "value" },
 config: { endpoint: "..." }
 }
 },
 load: { extraDirs: [], watch: true, watchDebounceMs: 250 }
 }
}
```

## Sub-agents

### Spawn

Via `sessions_spawn` tool (non-blocking). Params: task (required), label, agentId, model, thinking, runTimeoutSeconds, thread (boolean), mode (run|session), cleanup (delete|keep), sandbox (inherit|require).

### Nesting

| Depth | Role | Puede spawn? | Tools |
|-------|------|-------------|-------|
| 0 | Main | Siempre | Todos |
| 1 | Sub-agent / orchestrator | Solo si maxSpawnDepth ≥ 2 | Todos excepto session tools |
| 2 | Leaf worker | Nunca | Todos excepto session tools |

### Announce protocol

Results fluyen arriba: depth-2 → depth-1 → main → usuario. Cada nivel solo ve announces de hijos directos. Payload: status, result, runtime stats, tokens, sessionKey, transcript path.

### Tool policy

Default sub-agents: todos tools excepto session tools. Orchestrators (depth-1 con maxSpawnDepth ≥ 2): adicionalmente sessions_spawn, subagents, sessions_list, sessions_history.

## Agent Config Schema

```json5
{
 agents: {
 defaults: {
 workspace: "~/.openclaw/workspace",
 model: "anthropic/claude-sonnet-4-5",
 sandbox: { mode: "off", scope: "agent" },
 subagents: {
 maxSpawnDepth: 1,
 maxChildrenPerAgent: 5,
 maxConcurrent: 8,
 model: "provider/model",
 thinking: "low"
 }
 },
 list: [
 {
 id: "agent-id",
 name: "Nombre",
 default: true,
 workspace: "path",
 model: "provider/model",
 identity: { name: "N", emoji: "e", theme: "t" },
 sandbox: { mode: "off" },
 tools: { profile: "coding", allow: [], deny: [] },
 subagents: { maxSpawnDepth: 1, allowAgents: ["*"] }
 }
 ]
 }
}
```

### Tool profiles

| Profile | Incluye |
|---------|---------|
| minimal | session_status |
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

Tooling → Safety → Skills (XML) → Self-Update → Workspace → Documentation → Bootstrap Files → Sandbox → Date/Time → Reply Tags → Heartbeats → Runtime → Reasoning

### Prompt modes

| Mode | Uso | Diferencia |
|------|-----|-----------|
| full | Agentes principales | Todas las secciones |
| minimal | Sub-agents | Omite Skills, Memory, Self-Update, Reply Tags, Heartbeats |
| none | Solo identity | Base identity line |

## Multi-agent Routing

Bindings mapean channel + account + peer a agent id. Orden deterministico: peer > guildId > teamId > accountId-exact > accountId-wildcard > default.

```json5
{
 bindings: [
 { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
 { agentId: "home", match: { channel: "telegram" } }
 ]
}
```

## Sandboxing

| Mode | Descripcion |
|------|-------------|
| off | Sin sandbox |
| non-main | Solo sesiones no-main |
| all | Todas las sesiones |

Scopes: session (per-session container), agent (per-agent, default), shared.

Docker config incluye: image, containerPrefix, workdir, readOnlyRoot, tmpfs, network, user, capDrop, env, setupCommand, pidsLimit, memory, cpus, ulimits, seccompProfile.

## Seguridad

- Tratar skills de terceros como codigo no confiable
- Preferir sandbox para inputs no confiados
- Skill discovery solo acepta realpath dentro de roots configurados
- secrets via skills.entries.*.env inyectados en proceso host (no sandbox)
- Auth sub-agents resuelto por agent id con merge de profiles del main como fallback

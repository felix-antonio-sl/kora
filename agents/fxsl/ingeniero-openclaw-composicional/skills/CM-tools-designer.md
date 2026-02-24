---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-openclaw-composicional-cm-tools-designer:1.1.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Seleccionar tools, tool profiles y configurar multi-agent routing. Inventario dinamico — verificar docs.openclaw.ai/tools.

## Input/Output

- **Input:** Requisitos de herramientas y agentes desde S-TOOLS-DESIGN
- **Output:** Seccion tools y agents de openclaw.json con profiles, allow/deny, multi-agent config

## Procedimiento

1. Identificar caso de uso del agente
2. Seleccionar tool profile adecuado
3. Configurar tools.allow/deny segun plataforma y restricciones
4. Disenar multi-agent routing con agents.list[] si aplica
5. Generar seccion tools+agents de openclaw.json

### Tool Profiles

| Profile | Incluye |
|---------|---------|
| minimal | session_status only |
| coding | group:fs, group:runtime, group:sessions, group:memory, image |
| messaging | group:messaging, sessions_list, sessions_history, sessions_send, session_status |
| full | sin restriccion (default si no se configura) |

### Known Tools (verificar docs para estado actualizado)

apply_patch, exec, process, browser, canvas, web_search, web_fetch, image, message, cron, gateway, sessions_list/history/send/spawn/status, agents_list, loop-detection.

### Config Patterns

```json
// Deny browser
{ "tools": { "deny": ["browser"] } }

// Coding profile
{ "tools": { "profile": "coding" } }

// Per-agent tools
{
  "agents": { "list": [{
    "id": "support",
    "tools": { "profile": "messaging", "allow": ["slack"] }
  }] }
}
```

### Multi-Agent

docs.openclaw.ai/concepts/multi-agent — agents.list[] con workspace aislado por agente.

## Signature Output

```json
{
  "tools": { "profile": "...", "allow": [], "deny": [] },
  "agents": { "list": [{ "id": "...", "workspace": "...", "tools": {} }] }
}
```

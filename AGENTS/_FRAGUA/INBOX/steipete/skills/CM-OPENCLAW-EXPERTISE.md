---
_manifest:
  urn: urn:dev:skill:openclaw-expertise:1.1.1
  type: lazy_load_endofunctor
---

## Proposito

Responder sobre cualquier aspecto de OpenClaw con precision tecnica. Configuracion, arquitectura, deployment, channels, tools, skills, plugins, seguridad, troubleshooting.

## Input/Output

- **Input:** Pregunta o tarea relacionada con OpenClaw (configuracion, deployment, troubleshooting, diseno de workspace, channel setup, tool policy, etc.)
- **Output:** Respuesta autoritativa con referencia a la documentacion oficial, snippets de configuracion concretos, y recomendaciones de best practices.

## Procedimiento

1. Clasificar el dominio de la pregunta: gateway, channels, tools, providers, concepts, install, plugins, skills, security, automation.
2. Consultar `search_openclaw` con section filter apropiado.
3. Para configuracion: proveer snippet JSON5 concreto para `openclaw.json`, copy-pasteable.
4. Para troubleshooting: referir a `openclaw doctor`, `openclaw status --all`, logs del gateway.
5. Para arquitectura: explicar desde la topologia (gateway WebSocket -> channels -> agent runtime -> tool execution -> response delivery).
6. Para channels: incluir setup especifico (botToken, allowFrom, dmPolicy, groupPolicy, mentionPatterns).
7. Para tools: incluir profiles (minimal/messaging/coding/full), allow/deny patterns, sandbox config.
8. Para multi-agent: explicar bindings, routing, session scoping.
9. Si la pregunta toca seguridad: ser exhaustivo (pairing, allowlists, sandbox Docker, elevated mode, secrets).

## Signature Output

```
## OpenClaw: [topic]
[Respuesta tecnica]

### Config
\```json5
// snippet concreto
\```

### Referencia
[docs consultados]
```

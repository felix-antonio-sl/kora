---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-openclaw-composicional-cm-session-designer:1.1.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Disenar workspace, bootstrap files, sesiones y nodos para OpenClaw.

## Input/Output

- **Input:** Requisitos de workspace y sesiones desde S-SESSION-DESIGN
- **Output:** Estructura workspace con bootstrap files, config nodos y pairing

## Procedimiento

1. Configurar workspace path (default ~/.openclaw/workspace, configurable via agents.defaults.workspace)
2. Disenar bootstrap files segun caso de uso
3. Configurar memoria y sesiones
4. Definir pairing y nodos si aplica

### Bootstrap Files Comunes

- AGENTS.md: instrucciones operativas del agente
- SOUL.md: persona y tono
- USER.md: identidad del usuario
- TOOLS.md: guias de herramientas
- IDENTITY.md: nombre y emoji del agente
- HEARTBEAT.md: recordatorios periodicos (si aplica)
- memory/YYYY-MM-DD.md: logs diarios de memoria

### Nodos

- iOS node: pairing + Canvas surface (docs.openclaw.ai/nodes)
- Android node: pairing, Canvas, chat, camara (docs.openclaw.ai/nodes)
- macOS companion app: menu bar + Control UI (docs.openclaw.ai/platforms)
- Headless: sin UI, solo Gateway

### Pairing

docs.openclaw.ai/channels/pairing — DM safety y approval flows

## Signature Output

```
workspace/
  AGENTS.md
  SOUL.md
  USER.md
  TOOLS.md
  IDENTITY.md
  memory/
```

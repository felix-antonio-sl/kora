---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-openclaw-composicional-cm-gateway-architect:1.1.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Disenar configuracion Gateway en openclaw.json. Definir bind, auth, acceso y multi-agent routing.

## Input/Output

- **Input:** Requisitos capturados desde S-REQUIREMENTS (plataforma, canales, acceso, provider)
- **Output:** Seccion gateway de openclaw.json con bind, auth, tailscale y agents config

## Procedimiento

1. Determinar BIND: loopback (127.0.0.1:18789) o remoto? Puerto personalizado?
2. Determinar AUTH: local-only, password, Tailscale Serve/Funnel?
3. Determinar TAILSCALE: off, serve (tailnet), o funnel (publico)?
4. Determinar MULTI-AGENT: single agent (default) o agents.list[] con workspaces aislados?
5. Determinar MODEL: provider/model (venice/llama-3.3-70b default)
6. Generar openclaw.json con secciones configuradas

### Constraints

- Loopback + Tailscale Serve = seguro para tailnet
- Funnel requiere password auth
- Multi-agent: workspaces aislados recomendado
- Referencia: docs.openclaw.ai/gateway/configuration

### Config Referencia Minima

```json
{
  "agents": { "defaults": { "workspace": "~/.openclaw/workspace" } },
  "channels": { "whatsapp": { "allowFrom": ["+15555550123"] } }
}
```

## Signature Output

```json
// ~/.openclaw/openclaw.json — seccion gateway
{
  "gateway": { "bind": "...", "port": "..." },
  "agents": { "defaults": { "workspace": "...", "model": { "primary": "..." } } }
}
```

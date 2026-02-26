---
_manifest:
  urn: "urn:kora:skill:clawmaster-configurator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONFIGURATOR

## Proposito
Configura instancias OpenClaw cubriendo todos los dominios de configuracion: gateway, channels, models, agents, security, automation, multi-agent, sandbox, memory, skills.

## I/O

- **Input:** scope: string (dominio de configuracion), config_actual: object | null
- **Output:** ConfigReport (ver Signature Output)

## Procedimiento

### Paso 1: Identificar Scope

| Scope | Config Location | Referencia |
|-------|----------------|------------|
| Gateway (puerto, bind, auth) | openclaw.json → gateway | Cap 1, docs/gateway/configuration |
| Channels (WhatsApp, Telegram, etc.) | openclaw.json → channels | docs/channels/ |
| Models (provider, failover, auth) | openclaw.json → agent.model + auth profiles | Cap 4, docs/providers/ |
| Multi-agent (routing, bindings) | openclaw.json → agents.list[] | Cap 6, docs/concepts/multi-agent |
| Security (DM policy, sandbox, tool policy) | openclaw.json → gateway.auth + channels.*.allowFrom + agents.*.sandbox | Cap 7, 18 |
| Automation (heartbeat, cron, hooks) | openclaw.json + HEARTBEAT.md + hooks/ | Cap 12-16 |
| Memory (embedding, vector, QMD) | openclaw.json → memory | Cap 5 |
| Skills | workspace/skills/ + openclaw.json → skills | Cap 2 §2.5, docs/tools/skills |
| Workspace (AGENTS.md, SOUL.md, etc.) | workspace/ | Cap 2 §2.3 |

### Paso 2: Leer Config Actual
- `openclaw config --json` o leer ~/.openclaw/openclaw.json directamente
- Identificar lo que ya esta configurado vs lo que falta

### Paso 3: Aplicar Configuracion
- Generar config JSON5 con comentarios explicativos
- Para channels: guiar pairing flow (QR para WhatsApp, bot token para Telegram, etc.)
- Para multi-agent: disenar bindings segun patron (Cap 6 §6.3, Cap 20)
- Para security: aplicar hardened baseline (Cap 18 §18.7)
- Para automation: elegir entre heartbeat/cron/hooks segun arbol de decision (Cap 14)

### Paso 4: Validar
```
openclaw doctor          # config valida
openclaw status          # servicios ok
openclaw security audit  # sin vulnerabilidades
```

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| scope | string | Dominio de configuracion aplicado |
| cambios_realizados | string[] | Lista de cambios aplicados |
| config_generada | string | Config JSON5 generada |
| validacion | string | Resultado de openclaw doctor |

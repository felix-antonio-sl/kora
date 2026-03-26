---
name: agent-config
description: Derive, assemble, validate, and emit OpenClaw configuration fragments including openclaw.json, bootstrap files, channels, tools policy, sandbox, sessions, heartbeat, cron, and plugins. Use when the user needs to configure an agent or manage its config surface.
---

## Proposito

Producir configuracion OpenClaw correcta, completa y validada — desde fragmentos de `openclaw.json` hasta archivos bootstrap y setup de plugins.

## Cuando se activa

- El usuario necesita configurar un agente: modelo, canales, sessions, tools policy, sandbox.
- Se requiere ensamblar `openclaw.json` desde cero o extender uno existente.
- Hay que configurar heartbeat, cron, plugins, bundles, o skills entries.
- Se necesita validar que una config es correcta antes de aplicarla.

## Procedimiento

1. **Recopilar requisitos.** Que necesita el agente: modelo, canales, tools, sandbox, sessions, plugins.
2. **Derivar config.** Traducir requisitos a campos de `openclaw.json` usando el schema oficial.
3. **Validar contra docs.** Verificar que cada campo existe en el schema y tiene el tipo correcto.
4. **Verificar colisiones.** Asegurar que no hay conflictos entre config de canales, skills, tools policy.
5. **Emitir fragmento.** Entregar el JSON5 listo para aplicar, con comentarios donde haya decisiones no triviales.

## Alcance

Este skill cubre toda la superficie de configuracion:

- **Modelo y provider:** `agents.defaults.model`, `agents.defaults.provider`, API keys.
- **Canales:** Telegram, WhatsApp, Slack, web — config de cada adapter.
- **Sessions:** `sessions.mode`, TTL, storage.
- **Tools policy:** `tools.allow`, `tools.deny`, approval modes.
- **Sandbox:** `agents.defaults.sandbox` — modo, imagen, setup.
- **Heartbeat y cron:** scheduling, health checks.
- **Plugins y bundles:** registro, habilitacion, config de skills asociados.
- **Skills entries:** `skills.entries.*` — enabled, env, apiKey, config.

## Reglas

- **Schema first.** No inventar campos. Todo debe existir en el schema oficial.
- **Comentar decisiones.** Si un valor no es obvio, explicar por que.
- **Secrets separados.** API keys y tokens van como referencia (`{ source, provider, id }`), nunca en texto plano.
- **Fragmentos, no monolitos.** Emitir solo lo relevante, no un `openclaw.json` completo si no se pide.

## Formato de salida

```
**Requisitos cubiertos:** <lista>
**Fragmento config (JSON5):**
<bloque de codigo>
**Validacion:** <resultado de chequeo contra schema>
**Advertencias:** <si las hay>
```

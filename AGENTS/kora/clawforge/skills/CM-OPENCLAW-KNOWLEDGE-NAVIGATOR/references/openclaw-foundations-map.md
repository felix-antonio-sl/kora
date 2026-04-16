# OpenClaw Foundations Map

Mapa curado de la documentacion oficial OpenClaw que `kora/clawforge` debe tratar como referencia factual primaria.

## 1. Identidad del agente y workspace

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/agent.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/agent-workspace.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/context.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/system-prompt.md`

Usar para:

- bootstrap files
- workspace root
- `agentDir`
- session context
- prompt assembly

## 2. Configuracion y surfaces nativas

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/configuration.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/configuration-reference.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/cli/config.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/help/faq.md`

Usar para:

- `agents.defaults`
- `agents.list[]`
- `tools.*`
- `sandbox.*`
- `gateway.*`
- `channels.*`
- `SecretRef`

## 3. Sandboxing, tools y subagentes

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/sandboxing.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/sandbox-vs-tool-policy-vs-elevated.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/subagents.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/multi-agent-sandbox-tools.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/multi-agent.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/delegate-architecture.md`

Usar para:

- `tools.profile`
- `tools.allow/deny`
- `tools.elevated`
- `sessions_spawn`
- `subagents.allowAgents`
- `ssh` / `openshell`

## 4. Skills, plugins y bundles

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/skills.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/cli/skills.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/plugin.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/cli/plugins.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/clawhub.md`

Usar para:

- `managed_installs.skills`
- `managed_installs.plugins`
- `managed_installs.bundles`
- precedence entre workspace skills, managed skills y bundled components

## 5. Browser y sesiones existentes

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/browser.md`

Usar para:

- `existing-session`
- `userDataDir`
- CDP / MCP
- browser profiles

## 6. Gateway, redes y topologia

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/index.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/multiple-gateways.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/remote.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/trusted-proxy-auth.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/doctor.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/install/migrating.md`

Usar para:

- topologia `single-gateway-multi-agent`
- `--profile`
- `OPENCLAW_STATE_DIR`
- `OPENCLAW_CONFIG_PATH`
- `gateway.bind`
- `trusted-proxy`
- `controlUi.allowedOrigins`
- verificacion y migracion

## 7. Canales y automatizacion

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/channels/telegram.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/automation/hooks.md`

Usar para:

- `dmPolicy`
- `allowFrom`
- `groupAllowFrom`
- `silentErrorReplies`
- `chunkMode`
- webhook mode
- hooks y automatizacion runtime

## Regla de uso

1. Hecho OpenClaw -> documentacion oficial local primero.
2. Interpretacion normativa KORA -> specs KORA y `openclaw-runtime-extension`.
3. Si la documentacion oficial y KORA difieren, la respuesta debe explicitar: hecho, norma, tension y salida recomendada.

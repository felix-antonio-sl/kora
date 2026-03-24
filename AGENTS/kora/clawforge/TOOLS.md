---
_manifest:
  urn: "urn:kora:agent-bootstrap:clawforge-tools:1.0.0"
  type: "bootstrap_tools"
---

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Resolver spec o base doctrinal para decisiones de ciclo de vida OpenClaw.
- **Cuando NO usar:** Tema ya mapeado en el turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Gobernanza, precedencia, limites constitucionales | urn:kora:kb:gobernanza |
| Agent spec, 5 componentes, segregacion, FSM | urn:kora:kb:agent-spec-md |
| Skill spec, lazy-load, CM Core | urn:kora:kb:skill-spec-md |
| Runtime, wrappers, equivalencia, transmutacion | urn:kora:kb:runtime-spec-md |
| OpenClaw native-first, contrato estructurado, topologias | urn:agengai:kb:openclaw-runtime-extension |
| OpenClaw, workspace, config, sub-agents, gating, channels | urn:agengai:kb:openclaw-integration |
| Deploy de agentes KORA en OpenClaw | urn:ops:kb:deploy-agente-kora-en-openclaw |
| Principios de transmutacion KORA-OpenClaw | urn:ops:kb:principios-transmutacion-kora-openclaw |
| Arquitectura del stack kora OpenClaw | urn:ops:kb:arquitectura-stack-kora |
| Federacion kora v2 sobre OpenClaw | urn:ops:kb:federacion-kora-v2 |
| UX Telegram OpenClaw | urn:ops:kb:ux-telegram-openclaw |

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Resolver URNs de specs o KBs a rutas fisicas consultables.
- **Cuando NO usar:** La ruta ya fue resuelta en el turno actual.

## workspace_read

- **Firma:** agent_path: string -> AgentComponents
- **Cuando usar:** Leer un workspace KORA/OpenClaw-oriented existente para auditar, operar o evolucionar.
- **Cuando NO usar:** Si solo se necesita un componente puntual.

## workspace_write

- **Firma:** {componente: string, contenido: string, agent_path: string} -> result: string
- **Cuando usar:** Materializar o corregir componentes del workspace.
- **Cuando NO usar:** Si no hay cambios a persistir.

## spec_consult

- **Firma:** spec_name: string -> content: string
- **Cuando usar:** Consultar specs fundacionales o la extension OpenClaw para decisiones normativas.
- **Cuando NO usar:** La regla ya esta en contexto.

## health_check

- **Firma:** agent_path: string -> HealthReport
- **Cuando usar:** Validar conformidad mecanica de un workspace KORA.
- **Cuando NO usar:** Para auditorias puramente conceptuales.

## artifact_read

- **Firma:** path: string -> content: string
- **Cuando usar:** Leer wrappers, staging outputs o manifests de transmutacion.
- **Cuando NO usar:** Si el artefacto aun no existe.

## artifact_write

- **Firma:** {path: string, content: string} -> result: string
- **Cuando usar:** Emitir artefactos derivados y handoffs en staging.
- **Cuando NO usar:** Para tocar el workspace fuente KORA.


## diff_compute

- **Firma:** {source_path: string, derived_path: string} -> DiffReport
- **Cuando usar:** Detectar drift entre fuente, target OpenClaw y artefactos derivados.
- **Cuando NO usar:** Si no existe comparando previo.

## agent_list

- **Firma:** namespace: string? -> agents[]
- **Cuando usar:** Buscar patrones, nombres disponibles y agentes relacionados.
- **Cuando NO usar:** Si la ruta exacta ya es conocida.

## oc_cli

- **Firma:** command: string -> output: string
- **Cuando usar:** Operar runtime OpenClaw, config, doctor, status, skills y plugins.
- **Cuando NO usar:** Para comandos host o Docker.
- **Notas:** Usar para `config set`, `gateway call config.patch`, `doctor`, `status --deep` y verificaciones post-cambio.

## oc_docs_search

- **Firma:** query: string -> SearchResult[]
- **Cuando usar:** Buscar detalle puntual en la documentacion oficial OpenClaw. Es la fuente factual primaria para config, runtime, tools, sandbox, plugins, channels y troubleshooting de OpenClaw.
- **Cuando NO usar:** Cuando la pregunta es puramente normativa KORA y ya esta gobernada por specs/KB locales.
- **Notas:** Componentes base a consultar prioritariamente:
  - `concepts/agent.md`, `concepts/agent-workspace.md`, `concepts/multi-agent.md`, `concepts/context.md`, `concepts/system-prompt.md`
  - `gateway/configuration.md`, `gateway/configuration-reference.md`, `gateway/sandboxing.md`, `gateway/sandbox-vs-tool-policy-vs-elevated.md`, `gateway/multiple-gateways.md`, `gateway/doctor.md`, `gateway/remote.md`, `gateway/trusted-proxy-auth.md`
  - `cli/config.md`, `cli/skills.md`, `cli/plugins.md`
  - `tools/skills.md`, `tools/plugin.md`, `tools/clawhub.md`, `tools/browser.md`, `tools/subagents.md`, `tools/multi-agent-sandbox-tools.md`
  - `channels/telegram.md`, `automation/hooks.md`, `install/migrating.md`, `help/faq.md`

## host_exec

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar operaciones host para deploy, mantenimiento o diagnostico del stack OpenClaw.
- **Cuando NO usar:** Para acciones semanticas propias del gateway si existe `oc_cli`.

## docker_exec

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar build, run, inspect y compose sobre el stack containerizado OpenClaw.
- **Cuando NO usar:** Si la accion es puramente logica dentro del gateway.

---
_manifest:
  urn: "urn:kora:agent-bootstrap:clawforge-tools:2.0.0"
  type: "bootstrap_tools"
---

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Resolver spec o base doctrinal para decisiones de ciclo de vida OpenClaw o de operacion de stack.
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
| Arquitectura gateway, agent loop, wire protocol | urn:agengai:kb:01-arquitectura-gateway |
| Agente como unidad, workspace, agentDir | urn:agengai:kb:02-agente-unidad-fundamental |
| Sesiones, compaction, persistencia | urn:agengai:kb:03-sesiones |
| Modelos, failover, auth profiles | urn:agengai:kb:04-modelos-failover |
| Memoria, embeddings, busqueda hibrida | urn:agengai:kb:05-memoria |
| Multi-agent routing, bindings | urn:agengai:kb:06-multi-agent-routing |
| Aislamiento, seguridad, sandbox, tool policy | urn:agengai:kb:07-aislamiento-seguridad |
| Sub-agentes, sessions_spawn, concurrency | urn:agengai:kb:09-sub-agentes |
| Heartbeats, periodic agent turns | urn:agengai:kb:12-heartbeats |
| Cron jobs, schedule, delivery | urn:agengai:kb:13-cron-jobs |
| Hooks, event-driven automation | urn:agengai:kb:15-hooks |
| Webhooks, HTTP triggers | urn:agengai:kb:16-webhooks |
| Modelo de seguridad, threat model | urn:agengai:kb:18-modelo-seguridad |
| Operaciones, status, doctor, maintenance | urn:agengai:kb:19-operaciones |
| Patrones de diseno, orchestrator | urn:agengai:kb:20-patrones-diseno |
| Multi-gateway dockerizado, federacion | urn:agengai:kb:22-multi-gateway-docker-federation |
| Cheatsheet, referencia rapida | urn:agengai:kb:cheatsheet |

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
- **Cuando usar:** Emitir artefactos derivados, handoffs y contratos en staging.
- **Cuando NO usar:** Para tocar el workspace fuente KORA.

## diff_compute

- **Firma:** {source_path: string, derived_path: string} -> DiffReport
- **Cuando usar:** Detectar drift entre fuente KORA, target OpenClaw y artefactos derivados.
- **Cuando NO usar:** Si no existe comparando previo.

## agent_list

- **Firma:** namespace: string? -> agents[]
- **Cuando usar:** Buscar patrones, nombres disponibles y agentes relacionados.
- **Cuando NO usar:** Si la ruta exacta ya es conocida.

## oc_cli

- **Firma:** command: string -> output: string
- **Cuando usar:** Verificar runtime OpenClaw, config, doctor, status, skills y plugins. Tambien para operaciones post-deploy: config set, gateway call, doctor --fix.
- **Cuando NO usar:** Para comandos host o Docker (usar host_exec o docker_exec).
- **Notas:** Comandos frecuentes: `status`, `status --deep`, `doctor`, `doctor --fix`, `config get/set`, `health --json`, `sessions`, `pairing list/approve`.

## oc_docs_search

- **Firma:** query: string -> SearchResult[]
- **Cuando usar:** Buscar detalle puntual en la documentacion oficial OpenClaw. Fuente factual primaria para config, runtime, tools, sandbox, plugins, channels y troubleshooting.
- **Cuando NO usar:** Cuando la pregunta es puramente normativa KORA y ya esta gobernada por specs/KB locales.

## host_exec

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar comandos en el host Unix para diagnostico, configuracion o mantenimiento del sistema operativo.
- **Cuando NO usar:** Para operaciones OpenClaw (usar oc_cli) o Docker (usar docker_exec).
- **Comandos frecuentes:** `systemctl`, `journalctl`, `df -h`, `free -h`, `uptime`, `ss -tlnp`, `ufw status`, `dmesg | tail`.

## docker_exec

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar comandos Docker para gestionar contenedores, imagenes, redes y volumes.
- **Cuando NO usar:** Para operaciones host (usar host_exec) o OpenClaw (usar oc_cli).
- **Comandos frecuentes:** `docker ps -a`, `docker compose ps/up/restart/logs`, `docker stats`, `docker inspect`, `docker network ls/inspect`, `docker volume ls`, `docker system df`, `docker image prune`.

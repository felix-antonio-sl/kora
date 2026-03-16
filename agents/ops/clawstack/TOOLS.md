---
_manifest:
  urn: urn:ops:agent-bootstrap:clawstack-tools:1.0.0
  type: bootstrap_tools
---

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema y resolver URN antes de acceder KB. Jerarquia: manual KORA > docs oficiales > conocimiento general.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| TOC, indice, estructura del manual | urn:kora:kb:00-toc |
| Fundamentos LLMs, tool use, arquitectura cliente-servidor | urn:kora:kb:00-fundamentos-previos |
| Arquitectura gateway, agent loop, wire protocol, prompt assembly | urn:kora:kb:01-arquitectura-gateway |
| Agente como unidad, workspace, agentDir, bootstrap files | urn:kora:kb:02-agente-unidad-fundamental |
| Sesiones, session keys, DM scope, compaction, persistencia | urn:kora:kb:03-sesiones |
| Modelos, failover, auth profiles, fallback chains | urn:kora:kb:04-modelos-failover |
| Memoria, MEMORY.md, daily logs, busqueda hibrida, embeddings | urn:kora:kb:05-memoria |
| Multi-agent routing, bindings, aislamiento | urn:kora:kb:06-multi-agent-routing |
| Aislamiento, seguridad por agente, sandbox, tool policy, elevated | urn:kora:kb:07-aislamiento-seguridad |
| Patrones multi-tenant, un canal multiples personas | urn:kora:kb:08-patrones-multitenant |
| Sub-agentes, sessions_spawn, tool policy, concurrency | urn:kora:kb:09-sub-agentes |
| Sub-agentes anidados, maxSpawnDepth, orchestrator pattern | urn:kora:kb:10-sub-agentes-anidados |
| Comunicacion inter-sesion, sessions_send, agent-to-agent | urn:kora:kb:11-comunicacion-inter-sesion |
| Heartbeats, periodic agent turns, config | urn:kora:kb:12-heartbeats |
| Cron jobs, schedule, payload, delivery | urn:kora:kb:13-cron-jobs |
| Cron vs heartbeat, arbol de decision | urn:kora:kb:14-cron-vs-heartbeat |
| Hooks, event-driven automation, TypeScript handlers | urn:kora:kb:15-hooks |
| Webhooks, HTTP triggers, session key policy | urn:kora:kb:16-webhooks |
| Lobster, workflow runtime, DSL, approval gates | urn:kora:kb:17-lobster |
| Modelo de seguridad, threat model, DM/group policies | urn:kora:kb:18-modelo-seguridad |
| Operaciones, status, doctor, maintenance, backup | urn:kora:kb:19-operaciones |
| Patrones de diseno, single agent, agent per concern, orchestrator | urn:kora:kb:20-patrones-diseno |
| Decisiones de arquitectura, decision records | urn:kora:kb:21-decisiones-arquitectura |
| Multi-gateway dockerizado, federacion, hub-and-spoke | urn:kora:kb:22-multi-gateway-docker-federation |
| Apendices, config reference, glosario, checklists | urn:kora:kb:apendices |
| Cheatsheet, referencia rapida | urn:kora:kb:cheatsheet |
| Agent spec KORA, componentes, FSM | urn:kora:kb:agent-spec-md |
| Gobernanza KORA, precedencia | urn:kora:kb:gobernanza |

## oc_cli

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar comandos OpenClaw CLI para operar gateway e instancias.
- **Cuando NO usar:** Para comandos host o Docker (usar host_exec o docker_exec).
- **Comandos frecuentes:** status, status --deep, doctor, doctor --fix, security audit, health --json, sessions, config get/set, onboard, update, logs.

## oc_docs_search

- **Firma:** query: string -> SearchResult[]
- **Cuando usar:** Buscar en documentacion oficial OpenClaw (KNOWLEDGE/agengai/openclaw/documentacion-oficial/) para detalle de API, config reference, platform-specific, troubleshooting puntual.
- **Cuando NO usar:** Para conceptos arquitectonicos (usar manual via kb_route primero).

## host_exec

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar comandos en el host Unix para diagnostico, configuracion o mantenimiento del sistema operativo.
- **Cuando NO usar:** Para operaciones OpenClaw (usar oc_cli) o Docker (usar docker_exec).
- **Comandos frecuentes:** systemctl status/start/stop/restart, apt update/upgrade, ufw status/allow/deny, ss -tlnp, journalctl, df -h, free -h, uptime, cat /etc/os-release.

## docker_exec

- **Firma:** command: string -> output: string
- **Cuando usar:** Ejecutar comandos Docker para gestionar contenedores, imagenes, redes y volumes.
- **Cuando NO usar:** Para operaciones host (usar host_exec) o OpenClaw (usar oc_cli).
- **Comandos frecuentes:** docker ps, docker logs, docker stats, docker compose up/down/ps, docker images, docker system df, docker inspect.

## spec_consult

- **Firma:** spec_name: string -> content: string
- **Cuando usar:** Consultar specs KORA fundacionales para verificar conformidad de decisiones arquitectonicas.
- **Cuando NO usar:** Si la informacion ya esta en contexto de sesion.

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Resolver URN a path fisico via catalogo.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.

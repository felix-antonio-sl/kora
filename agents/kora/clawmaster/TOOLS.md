---
_manifest:
  urn: "urn:kora:agent-bootstrap:clawmaster-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN → buscar catalog → extraer file → retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema OpenClaw → resolver URN del manual KORA → priorizar KB.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| TOC, indice, estructura manual | urn:kora:kb:00-toc |
| Fundamentos previos, prerequisitos | urn:kora:kb:00-fundamentos-previos |
| Arquitectura gateway, componentes, agent loop, wire protocol, prompt assembly, context window | urn:kora:kb:01-arquitectura-gateway |
| Agente, workspace, bootstrap files, skills, tools, tool policy, plugins | urn:kora:kb:02-agente-unidad-fundamental |
| Sesiones, session keys, DM scope, identity links, compaction, pruning, send policy | urn:kora:kb:03-sesiones |
| Modelos, failover, auth profiles, rotacion, billing, model fallback chain | urn:kora:kb:04-modelos-failover |
| Memoria, MEMORY.md, memory_search, embeddings, vector search, QMD, session memory | urn:kora:kb:05-memoria |
| Multi-agent routing, agents.list, bindings, auth isolation | urn:kora:kb:06-multi-agent-routing |
| Aislamiento, seguridad por agente, sandbox, tool restrictions, elevated, tool policy precedence | urn:kora:kb:07-aislamiento-seguridad |
| Multi-tenant, DM split, channel×model routing, family/work profiles, multiple gateways | urn:kora:kb:08-patrones-multitenant |
| Sub-agentes, sessions_spawn, announce, tool policy sub-agents, concurrency, auto-archive | urn:kora:kb:09-sub-agentes |
| Sub-agentes anidados, orchestrator pattern, maxSpawnDepth, cascade stop | urn:kora:kb:10-sub-agentes-anidados |
| Comunicacion inter-sesion, sessions_send, sessions_list, agent-to-agent | urn:kora:kb:11-comunicacion-inter-sesion |
| Heartbeats, intervalo, HEARTBEAT.md, response contract, visibility | urn:kora:kb:12-heartbeats |
| Cron jobs, schedule kinds, payload shapes, delivery modes, stagger, retry | urn:kora:kb:13-cron-jobs |
| Cron vs heartbeat, arbol de decision, patrones combinados, cost considerations | urn:kora:kb:14-cron-vs-heartbeat |
| Hooks, event types, hook structure, discovery, bundled hooks, plugin hooks | urn:kora:kb:15-hooks |
| Webhooks, /hooks/wake, /hooks/agent, session key policy, auth, security | urn:kora:kb:16-webhooks |
| Lobster, workflow runtime, DSL, resume tokens, llm-task, safety | urn:kora:kb:17-lobster |
| Modelo seguridad, threat model, DM policies, group policies, prompt injection, hardened config | urn:kora:kb:18-modelo-seguridad |
| Operaciones, status, doctor, security audit, logging, incident response, backup | urn:kora:kb:19-operaciones |
| Patrones diseno, single agent, agent per persona/concern, orchestrator+workers, reader agent | urn:kora:kb:20-patrones-diseno |
| Decisiones arquitectura, cuantos agentes, sandbox on/off, sub-agents vs cron, memory arch | urn:kora:kb:21-decisiones-arquitectura |
| Multi-gateway docker, federacion, compose, conocimiento compartido, orquestacion, scaling | urn:kora:kb:22-multi-gateway-docker-federation |
| Referencia rapida config, glosario, checklists setup/seguridad, mapeo KODA→OpenClaw | urn:kora:kb:apendices |
| Cheatsheet completo, referencia rapida integral | urn:kora:kb:cheatsheet |
| README, introduccion general, vision global, indice principal | urn:kora:kb:readme |

## oc_docs_search

- **Firma:** query: string → {file: string, section: string, content: string}[]: SearchResult[]
- **Cuando usar:** Buscar en documentacion oficial de OpenClaw (GitHub docs/) cuando el manual KORA no cubre el tema o se necesita detalle adicional (config reference, channel-specific setup, provider setup, CLI reference, platform guides).
- **Cuando NO usar:** Si el manual KORA ya responde la consulta con suficiente detalle.
- **Notas:** Docs organizados en: start/, install/, gateway/, channels/, concepts/, tools/, automation/, nodes/, platforms/, web/, cli/, providers/, reference/, plugins/, security/. Formato Mintlify markdown.

## oc_repo_search

- **Firma:** query: string → {file: string, line: number, content: string}[]: CodeResult[]
- **Cuando usar:** Buscar en codigo fuente de OpenClaw cuando se necesita entender implementacion, diagnosticar bugs, o preparar contribuciones. TypeScript ESM monorepo.
- **Cuando NO usar:** Para consultas de uso/configuracion (usar docs primero). Solo cuando se necesita el codigo.
- **Notas:** Estructura: src/ (core), extensions/ (plugins), skills/ (bundled), ui/ (web components Lit), apps/ (native Swift/Kotlin). Build: pnpm + tsdown. Tests: vitest.

## oc_cli

- **Firma:** command: string → output: string
- **Cuando usar:** Ejecutar comandos OpenClaw CLI para diagnosticar (status, doctor, security audit, sessions, health), configurar (config, configure), o gestionar (update, cron, hooks, skills, plugins, nodes).
- **Cuando NO usar:** Comandos destructivos (reset, uninstall) sin confirmacion explicita del usuario. Nunca en modo automatico sin supervision.
- **Notas:** CLI entry: openclaw.mjs. Principales: gateway, agent, agents, onboard, message, sessions, channels, config, configure, models, browser, cron, doctor, health, status, skills, plugins, nodes, hooks, memory, logs, sandbox, security, update, reset, uninstall. Flags comunes: --json (output maquina), --all (detallado).

## spec_consult

- **Firma:** spec_name: string → content: string
- **Cuando usar:** Consultar specs KORA para verificar conformidad o entender el modelo de agentes.
- **Cuando NO usar:** Para temas puramente OpenClaw (usar kb_route/oc_docs_search).
- **Notas:** Specs disponibles: agent-spec-md (modelo agentes), md-spec, spec-md, gobernanza.

---
_manifest:
  urn: urn:kora:kb:00-toc
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '00'
- toc
lang: es
---

# Manual de Agentes, Multi-Agentes y Automatización en OpenClaw

## Tabla de Contenidos

- ───


### Parte I — Fundamentos Arquitectónicos

1. Arquitectura del Gateway

- 1.1 Componentes: Gateway daemon, clients (WS), nodes, WebChat
- 1.2 Wire protocol (WebSocket JSON, connect handshake, auth)
- 1.3 Agent loop: intake → context assembly → model inference → tool execution → streaming → persistence
- 1.4 Prompt assembly y system prompt (estructura, secciones, inyección de bootstrap files)
- 1.5 Context window: qué cuenta, cómo inspeccionarlo (/context list, /context detail)

2. El Agente como Unidad Fundamental

- 2.1 Anatomía de un Agente: workspace + agentDir + session store + auth profiles
- 2.2 Agente, Sesión Main y Sub-Agentes: diferencias y relaciones
- 2.3 Workspace contract: bootstrap files (AGENTS.md, SOUL.md, USER.md, IDENTITY.md, TOOLS.md, HEARTBEAT.md, MEMORY.md)
- 2.4 Ciclo de vida de un agente: bootstrap → sesiones → compaction → memoria
- 2.5 Skills: descubrimiento, precedencia (bundled → managed → workspace), gating por env/bins/config
- 2.6 Tools: built-in vs skills vs plugins; tool schemas y su costo en contexto
- 2.7 Tool policy: profiles, allow/deny, por proveedor, por agente, por sandbox
- 2.8 Skills + Tools + Plugins: el modelo mental integrado

3. Sesiones

- 3.1 Session keys: cómo se construyen (DM, group, channel, cron, webhook, subagent)
- 3.2 DM scope: main vs per-peer vs per-channel-peer vs per-account-channel-peer
- 3.3 Identity links (colapsar identidades cross-channel)
- 3.4 Ciclo de vida: reset diario, idle reset, resetByType, resetByChannel
- 3.5 Persistencia: sessions.json + transcripts JSONL
- 3.6 Compaction: auto-compaction, memory flush pre-compaction, /compact
- 3.7 Session pruning (tool results viejos)
- 3.8 Send policy (bloquear delivery por tipo/canal)

4. Modelos y Failover

- 4.1 Model refs (provider/model), aliases
- 4.2 Auth profiles: API keys vs OAuth, profile IDs, storage
- 4.3 Rotación de perfiles: round-robin, session stickiness, cooldowns
- 4.4 Billing disables y backoff exponencial
- 4.5 Model fallback chain (primary → fallbacks[])
- 4.6 Overrides por sesión (/model), por cron job, por sub-agente

5. Memoria

- 5.1 Memory files: memory/YYYY-MM-DD.md (daily) + MEMORY.md (curada)
- 5.2 Memory tools: memory_search (vector + BM25 hybrid) y memory_get
- 5.3 Búsqueda híbrida: pesos vector/text, candidate multiplier
- 5.4 Post-procesamiento: MMR (diversidad) y Temporal Decay (recency boost)
- 5.5 Embedding providers: OpenAI, Gemini, Voyage, local (GGUF), custom endpoint
- 5.6 Embedding cache, batch indexing, sqlite-vec acceleration
- 5.7 QMD backend (experimental): BM25 + vectors + reranking local
- 5.8 Session memory search (experimental): indexar transcripts
- 5.9 Extra memory paths y scope (restringir por tipo de sesión)
- 5.10 Memory flush automático pre-compaction

- ───


### Parte II — Multi-Agente

6. Multi-Agent Routing

- 6.1 Concepto: un gateway, múltiples "cerebros" aislados
- 6.2 Configuración: agents.list[] con workspace, agentDir, model, identity
- 6.3 Bindings: reglas de ruteo determinísticas (peer > parentPeer > guildId+roles > accountId > channel > default)
- 6.4 Ejemplos: agentes por canal, por peer, por cuenta, por grupo
- 6.5 Auth isolation: auth profiles son per-agent, no compartidos

7. Aislamiento y Seguridad por Agente

- 7.1 Sandbox per-agent: mode, scope, workspaceAccess, Docker config
- 7.2 Tool restrictions per-agent: allow/deny, tool groups (group:runtime, group:fs, etc.)
- 7.3 Tool policy precedence: profile → global → provider → agent → sandbox → subagent
- 7.4 Elevated mode: global baseline + per-agent restriction
- 7.5 Patrones de acceso: full access, read-only, communication-only, no-fs
- 7.6 setupCommand (one-time container setup)
- 7.7 Custom bind mounts

8. Patrones Multi-Tenant

- 8.1 Un WhatsApp number → múltiples personas (DM split por peer)
- 8.2 Múltiples cuentas/números → múltiples agentes
- 8.3 Channel × model routing (WhatsApp=fast sonnet, Telegram=deep opus)
- 8.4 Family/work/public agent profiles
- 8.5 Secure DM mode: per-channel-peer obligatorio en multi-user
- 8.6 Multiple gateways en un host (profiles, ports, isolation checklist)

- ───


### Parte III — Orquestación de Sub-Agentes

9. Sub-Agentes (sessions_spawn)

- 9.1 Concepto: runs aislados en agent:<id>:subagent:<uuid>
- 9.2 Tool params: task, label, agentId, model, thinking, runTimeoutSeconds, cleanup
- 9.3 Announce flow: cómo los resultados llegan de vuelta al chat requester
- 9.4 Tool policy en sub-agentes: qué tools reciben y cuáles no
- 9.5 Concurrency: lane dedicada, maxConcurrent
- 9.6 Auto-archive: archiveAfterMinutes, cleanup modes
- 9.7 Discovery: agents_list para ver agentIds permitidos

10. Sub-Agentes Anidados (Orchestrator Pattern)

- 10.1 maxSpawnDepth: 1 (flat) vs 2 (main → orchestrator → workers)
- 10.2 Depth levels: quién puede spawn, qué tools recibe cada nivel
- 10.3 Announce chain: depth-2 → depth-1 → main
- 10.4 maxChildrenPerAgent: límite de fan-out por sesión
- 10.5 Cascade stop: /stop propaga a toda la cadena
- 10.6 Caso de uso: investigación paralela, coding distribuido, análisis multi-fuente

11. Comunicación Inter-Sesión

- 11.1 sessions_send: enviar mensajes a otra sesión (sessionKey o label)
- 11.2 sessions_list y sessions_history: inspección de sesiones
- 11.3 subagents tool: list, steer, kill
- 11.4 Agent-to-agent messaging (tools.agentToAgent)
- 11.5 openclaw agent CLI: runs directos sin mensaje inbound

- ───


### Parte IV — Automatización

12. Heartbeats

- 12.1 Concepto: agent turns periódicos en sesión main
- 12.2 Configuración: intervalo, modelo, target, activeHours, prompt
- 12.3 HEARTBEAT.md: checklist ligera, actualizable por el agente
- 12.4 Response contract: HEARTBEAT_OK vs alertas
- 12.5 Visibility controls por canal: showOk, showAlerts, useIndicator
- 12.6 Per-agent heartbeats
- 12.7 Manual wake: openclaw system event
- 12.8 Reasoning delivery (transparencia opcional)

13. Cron Jobs

- 13.1 Schedule kinds: at (one-shot), every (intervalo), cron (expresión)
- 13.2 Main session jobs vs isolated jobs
- 13.3 Payload shapes: systemEvent vs agentTurn
- 13.4 Delivery modes: announce, webhook, none
- 13.5 Model y thinking overrides por job
- 13.6 Agent binding (multi-agent cron)
- 13.7 Stagger (load spreading), retry backoff
- 13.8 Storage: jobs.json + runs JSONL
- 13.9 CLI quickstart y tool-call equivalents

14. Cron vs Heartbeat: Árbol de Decisión

- 14.1 Cuándo usar heartbeat (batching, contexto, low-overhead)
- 14.2 Cuándo usar cron (precisión, aislamiento, model override)
- 14.3 Flowchart de decisión
- 14.4 Patrón combinado: heartbeat para monitoring + cron para schedules
- 14.5 Cost considerations

15. Hooks (Event-Driven Automation)

- 15.1 Concepto: scripts que responden a eventos del gateway
- 15.2 Event types: command (new/reset/stop), agent:bootstrap, gateway:startup, message (received/sent)
- 15.3 Hook structure: HOOK.md (frontmatter) + handler.ts
- 15.4 Discovery: workspace → managed → bundled (precedencia)
- 15.5 Hooks bundled: session-memory, bootstrap-extra-files, command-logger, boot-md
- 15.6 Hook packs (npm packages)
- 15.7 Plugin hooks: before_model_resolve, before_prompt_build, before/after_tool_call, tool_result_persist
- 15.8 Crear hooks custom

16. Webhooks (External Triggers)

- 16.1 /hooks/wake: system event + heartbeat trigger
- 16.2 /hooks/agent: isolated agent turn con delivery
- 16.3 /hooks/<name>: mapped hooks con transforms
- 16.4 Session key policy: defaultSessionKey, allowRequestSessionKey, prefixes
- 16.5 Auth: bearer token, rate limiting
- 16.6 Security: loopback, dedicated token, content safety wrappers
- 16.7 Caso de uso: Gmail Pub/Sub → webhook → agente

17. Lobster (Workflow Runtime)

- 17.1 Concepto: pipelines determinísticas con approval gates
- 17.2 DSL: exec | exec | approve → JSON pipes
- 17.3 Resume tokens: pause → approve → continue
- 17.4 llm-task: LLM steps JSON-only dentro de workflows
- 17.5 Integración con cron y heartbeat como triggers
- 17.6 Safety: timeouts, output caps, sandbox checks

- ───


### Parte V — Seguridad y Operaciones

18. Modelo de Seguridad

- 18.1 Threat model: shell access + messaging surfaces + prompt injection
- 18.2 Access control antes que inteligencia: identity → scope → model
- 18.3 DM policies: pairing, allowlist, open, disabled
- 18.4 Group policies: allowlists, mention gating, groupAllowFrom
- 18.5 Prompt injection: superficies de ataque (DM, contenido web, emails, attachments)
- 18.6 Model strength y su relación con seguridad
- 18.7 Hardened baseline config (copy-paste)
- 18.8 openclaw security audit (y --deep)

19. Operaciones

- 19.1 openclaw status, openclaw doctor, openclaw sessions
- 19.2 Logging: redaction, retention, patterns
- 19.3 Incident response: contain → rotate → audit → report
- 19.4 Backup strategy: config, credentials, workspace, memory
- 19.5 Gateway restart y hot-reload de config

- ───


### Parte VI — Patrones de Diseño y Decisiones Arquitectónicas

20. Patrones de Diseño para Agentes OpenClaw

- 20.1 Single agent + multiple channels (el setup más simple)
- 20.2 Agent per persona (work/personal/family)
- 20.3 Agent per concern (coding, ops, alerts)
- 20.4 Orchestrator + workers (sub-agentes anidados depth-2)
- 20.5 Reader agent (sandboxed) → main agent (trusted): contenido externo hostil
- 20.6 Cron + webhook pipeline (Gmail → hook → agente → announce)
- 20.7 KODA → OpenClaw mapping (Tier 1 persistentes, Tier 2 on-demand)

21. Decisiones de Arquitectura (Decision Records)

- 21.1 ¿Cuántos agentes necesito? (criterios de split)
- 21.2 ¿Sandbox on/off? (trade-off acceso nativo vs seguridad)
- 21.3 ¿Sub-agentes vs cron aislado? (cuándo spawn vs cuándo schedule)
- 21.4 ¿Un gateway o múltiples? (isolation vs complejidad operativa)
- 21.5 ¿Heartbeat vs cron? (batching vs precisión)
- 21.6 ¿Modelo por agente o fallback chain compartida?
- 21.7 ¿Tools.elevated: cuándo y para quién?
- 21.8 Memory architecture: cuándo MEMORY.md, cuándo daily, cuándo QMD

- ───


### Parte VII — Arquitectura Avanzada

- **22.
- Multi-Gateway Dockerizado:
- Federación de Agentes**

- 22.1 Por qué multi-gateway (y no solo multi-agent): tabla de limitaciones de single-process
- 22.2 Arquitectura: Docker Compose multi-gateway con red compartida
- 22.3 Docker Compose: configuración base con YAML template y estructura de directorios
- 22.4 Conocimiento compartido: bind mounts :ro, QMD sidecar compartido, git sync
- 22.5 Comunicación inter-gateway: webhook relay, buzón de archivos, Docker network directo
- 22.6 Orquestación: hub-and-spoke, mesh, hub + selective spokes
- 22.7 Configuración de cada gateway: hub (Korax), spoke webhook-only (GoreOS), spoke + canal (Médico)
- 22.8 Skill federation-delegate: encapsulación de lógica de delegación
- 22.9 Seguridad: tokens dedicados, red interna, content wrapping, anti-loop
- 22.10 Operaciones: startup/shutdown, health checks, monitoring, backup, rolling updates
- 22.11 Scaling: de 3 a N gateways, límites prácticos de recursos

### Apéndices

- A.
- Referencia rápida de configuración (campos clave con ejemplos mínimos) B.
- Glosario (agentId, accountId, binding, sessionKey, mainKey, dmScope, tool profile, etc.) C.
- Checklist de setup multi-agente (paso a paso) D.
- Checklist de seguridad (auditoría express) E.
- Mapeo KODA → OpenClaw (tabla de equivalencias para migración)


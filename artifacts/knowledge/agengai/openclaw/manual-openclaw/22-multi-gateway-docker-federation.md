---
_manifest:
  urn: urn:agengai:kb:22-multi-gateway-docker-federation
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '22'
- multi
- gateway
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:22-multi-gateway-docker-federation
---

# Capítulo 22 — Multi-Gateway Dockerizado: Federación de Agentes

> **Propósito:** Diseñar una arquitectura donde múltiples instancias de OpenClaw Gateway corren en containers Docker sobre un servidor dedicado, compartiendo red y repositorios de conocimiento, con capacidad de comunicación inter-agente. Este capítulo explora patrones que van más allá de lo single-gateway y multi-agent, usando mecanismos nativos y canónicos de OpenClaw.

- ---

## 22.1 Por Qué Multi-Gateway (y No Solo Multi-Agent)

### Lo que multi-agent resuelve dentro de un gateway

- Un solo gateway con `agents.list[]` (Cap.
- 6-8) te da:

- Múltiples "cerebros" con workspaces, auth y sesiones aisladas
- Bindings para ruteo determinístico
- Tool policy y sandbox per-agent
- Agent-to-agent messaging (opt-in)

### Lo que multi-agent NO resuelve

| Limitación | Consecuencia |
|-----------|-------------|
| **Single process** | Si el gateway cae, TODOS los agentes caen |
| **Shared runtime** | Un agent turn pesado (Opus + 20 tools) afecta latencia de todos |
| **Shared config** | Un cambio en openclaw.json requiere restart que afecta a todos |
| **Shared channel connections** | Una desconexión de WhatsApp afecta a todos los agentes del gateway |
| **Shared model rotation** | Cooldowns y rate limits de auth profiles son per-gateway |
| **Update coupling** | Actualizar OpenClaw requiere downtime para todos los agentes |
| **Resource isolation** | No hay limits de CPU/RAM por agente (solo por sandbox container) |

### Cuándo escalar a multi-gateway

```
¿Necesitas aislamiento de proceso?
├── SÍ → Multi-gateway
│ ├── Agentes con SLAs diferentes (uno puede caer, otro no)
│ ├── Agentes con diferentes versiones de OpenClaw
│ ├── Resource isolation real (CPU/RAM por gateway)
│ ├── Update rolling (actualizar uno sin tocar otro)
│ └── Fault domains separados
│
└── NO → Multi-agent en un gateway es suficiente
```

- ---

## 22.2 Arquitectura: Docker Compose Multi-Gateway

### Diagrama

```
┌─────────────────────────────────────────────────────────────────────┐
│ SERVIDOR DEDICADO (64GB RAM, 1TB SSD) │
│ │
│ ┌────────────── Docker Network: openclaw-federation ──────────────┐ │
│ │ │ │
│ │ ┌─────────────────┐ ┌─────────────────┐ ┌────────────────┐ │ │
│ │ │ GW: korax-main │ │ GW: goreos-arch │ │ GW: medico-ai │ │ │
│ │ │ Port: 18789 │ │ Port: 18809 │ │ Port: 18829 │ │ │
│ │ │ │ │ │ │ │ │ │
│ │ │ Agent: main │ │ Agent: goreos │ │ Agent: medico │ │ │
│ │ │ Model: Sonnet │ │ Model: Opus │ │ Model: Sonnet │ │ │
│ │ │ Channels: │ │ Channels: │ │ Channels: │ │ │
│ │ │ Telegram @Korax │ │ (webhook only) │ │ Telegram @Med │ │ │
│ │ │ WhatsApp │ │ │ │ │ │ │
│ │ │ │ │ │ │ │ │ │
│ │ │ Sandbox: off │ │ Sandbox: all │ │ Sandbox: all │ │ │
│ │ └────────┬─────────┘ └────────┬─────────┘ └───────┬────────┘ │ │
│ │ │ │ │ │ │
│ │ ┌────────┴─────────────────────┴─────────────────────┴────────┐ │ │
│ │ │ SHARED VOLUMES (bind mounts) │ │ │
│ │ │ │ │ │
│ │ │ /srv/koda/knowledge/ (read-only) ← KODA KB compartida │ │ │
│ │ │ /srv/shared-memory/ (read-only) ← docs compartidos │ │ │
│ │ │ /srv/comms/ (read-write) ← buzón inter-gateway │ │ │
│ │ └──────────────────────────────────────────────────────────────┘ │ │
│ │ │ │
│ └──────────────────────────────────────────────────────────────────┘ │
│ │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │ Tailscale (mesh VPN) │ │
│ │ Caddy / Traefik (reverse proxy, optional) │ │
│ └─────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### Principios de diseño

1. **Cada gateway es un container Docker independiente** con su propio config, state dir, workspace, y puerto
2. **Red compartida** (Docker bridge network) permite comunicación HTTP entre gateways
3. **Volúmenes compartidos** (read-only) dan acceso a repositorios de conocimiento comunes
4. **Comunicación inter-gateway** via webhooks HTTP (mecanismo nativo de OpenClaw)
5. **Cada gateway maneja sus propios canales** (un bot Telegram por gateway, o webhook-only)

- ---

## docker-compose.yml

```yaml
version: "3.8"

networks:
 openclaw-federation:
 driver: bridge

volumes:
 korax-state:
 goreos-state:
 medico-state:

x-openclaw-base: &openclaw-base
 image: openclaw:local
 restart: unless-stopped
 networks:
 - openclaw-federation
 volumes:
 # Shared knowledge (read-only para todos)
 - /srv/koda/knowledge:/shared/koda:ro
 - /srv/shared-docs:/shared/docs:ro
 # Comms bus (read-write para inter-gateway messaging)
 - /srv/comms:/shared/comms:rw

services:
 # ═══════════════════════════════════════
 # GATEWAY 1: Korax (main, personal)
 # ═══════════════════════════════════════
 korax-gateway:
 <<: *openclaw-base
 container_name: korax-gateway
 ports:
 - "127.0.0.1:18789:18789"
 environment:
 - OPENCLAW_GATEWAY_PORT=18789
 - OPENCLAW_GATEWAY_TOKEN=${KORAX_GATEWAY_TOKEN}
 - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
 - OPENAI_API_KEY=${OPENAI_API_KEY}
 - TELEGRAM_BOT_TOKEN=${TG_TOKEN_KORAX}
 volumes:
 - korax-state:/home/node/.openclaw
 - ./workspaces/korax:/home/node/.openclaw/workspace
 - /srv/koda/knowledge:/shared/koda:ro
 - /srv/shared-docs:/shared/docs:ro
 - /srv/comms:/shared/comms:rw
 healthcheck:
 test: ["CMD", "node", "dist/index.js", "health", "--token", "${KORAX_GATEWAY_TOKEN}"]
 interval: 30s
 timeout: 10s
 retries: 3

 # ═══════════════════════════════════════
 # GATEWAY 2: GoreOS Architect (specialist)
 # ═══════════════════════════════════════
 goreos-gateway:
 <<: *openclaw-base
 container_name: goreos-gateway
 ports:
 - "127.0.0.1:18809:18809"
 environment:
 - OPENCLAW_GATEWAY_PORT=18809
 - OPENCLAW_GATEWAY_TOKEN=${GOREOS_GATEWAY_TOKEN}
 - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
 - OPENCLAW_HOOKS_TOKEN=${GOREOS_HOOKS_TOKEN}
 volumes:
 - goreos-state:/home/node/.openclaw
 - ./workspaces/goreos:/home/node/.openclaw/workspace
 - /srv/koda/knowledge:/shared/koda:ro
 - /srv/koda/repos:/shared/repos:ro
 - /srv/shared-docs:/shared/docs:ro
 - /srv/comms:/shared/comms:rw

 # ═══════════════════════════════════════
 # GATEWAY 3: Médico AI (specialist)
 # ═══════════════════════════════════════
 medico-gateway:
 <<: *openclaw-base
 container_name: medico-gateway
 ports:
 - "127.0.0.1:18829:18829"
 environment:
 - OPENCLAW_GATEWAY_PORT=18829
 - OPENCLAW_GATEWAY_TOKEN=${MEDICO_GATEWAY_TOKEN}
 - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
 - OPENCLAW_HOOKS_TOKEN=${MEDICO_HOOKS_TOKEN}
 volumes:
 - medico-state:/home/node/.openclaw
 - ./workspaces/medico:/home/node/.openclaw/workspace
 - /srv/shared-docs:/shared/docs:ro
 - /srv/comms:/shared/comms:rw
```

## Estructura de directorios en el host

```
/srv/
├── koda/
│ ├── knowledge/ ← KODA KB compilada (YAML/MD, read-only)
│ └── repos/ ← Repos KODA (git clones, read-only)
├── shared-docs/ ← Documentos compartidos (cabinet global)
├── comms/ ← Buzón inter-gateway (archivos JSON)
└── openclaw/
 └── workspaces/
 ├── korax/ ← Workspace de Korax
 │ ├── AGENTS.md, SOUL.md, etc.
 │ ├── memory/
 │ └── skills/
 ├── goreos/ ← Workspace de GoreOS Architect
 │ ├── AGENTS.md
 │ ├── memory/
 │ └── skills/
 └── medico/ ← Workspace de Médico AI
 ├── AGENTS.md
 ├── memory/
 └── skills/
```

- ---

## 22.4 Conocimiento Compartido: Patrones

### Patrón 1: Bind Mounts Read-Only (recomendado)

```yaml
volumes:
 - /srv/koda/knowledge:/shared/koda:ro # todos leen, nadie escribe
```

- Cada gateway puede referenciar la KB compartida en su config:

```json5
// openclaw.json de goreos-gateway
{
 agents: {
 defaults: {
 memorySearch: {
 extraPaths: ["/shared/koda", "/shared/docs"]
 }
 }
 }
}
```

- **Ventajas:**

- Un solo lugar para mantener la KB
- Actualización atómica: editas en el host → todos los gateways lo ven
- Read-only previene que un gateway corrupto modifique la KB

- **Limitaciones:**

- Los gateways indexan la KB independientemente (cada uno tiene su propio SQLite de embeddings)
- Si la KB es grande (>10K archivos), el re-indexado post-cambio puede ser pesado

### Patrón 2: QMD Sidecar Compartido

- Si la KB es muy grande, un QMD sidecar compartido evita indexación duplicada:

```yaml
services:
 qmd-server:
 image: qmd:latest
 container_name: qmd-shared
 networks:
 - openclaw-federation
 volumes:
 - /srv/koda/knowledge:/data:ro
 ports:
 - "127.0.0.1:9876:9876"
```

```json5
// Cada gateway apunta al QMD compartido
{
 memory: {
 backend: "qmd",
 qmd: {
 endpoint: "http://qmd-shared:9876"
 }
 }
}
```

- **Ventaja:** Un solo índice vectorial.
- N gateways consultando el mismo search. **Trade-off:** Dependencia adicional.
- Si el QMD cae, memory search falla (con fallback a SQLite local).

### Patrón 3: Git Sync para KB

```bash
# Cron del host que actualiza la KB compartida
*/30 * * * * cd /srv/koda/knowledge && git pull --quiet
```

- Los gateways ven los cambios en el próximo sync de su watcher (debounce ~1.5s post-write).

- ---

## 22.5 Comunicación Inter-Gateway: Patrones Nativos

- OpenClaw no tiene un protocolo nativo de gateway-to-gateway.
- Pero tiene **webhooks** (Cap.
- 16) y **exec** (para HTTP calls).
- Estos son los bloques canónicos para construir comunicación.

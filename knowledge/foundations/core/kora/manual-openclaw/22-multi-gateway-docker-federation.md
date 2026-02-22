# Capítulo 22 — Multi-Gateway Dockerizado: Federación de Agentes

> **Propósito:** Diseñar una arquitectura donde múltiples instancias de OpenClaw Gateway corren en containers Docker sobre un servidor dedicado, compartiendo red y repositorios de conocimiento, con capacidad de comunicación inter-agente. Este capítulo explora patrones que van más allá de lo single-gateway y multi-agent, usando mecanismos nativos y canónicos de OpenClaw.

---

## 22.1 Por Qué Multi-Gateway (y No Solo Multi-Agent)

### Lo que multi-agent resuelve dentro de un gateway

Un solo gateway con `agents.list[]` (Cap. 6-8) te da:
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
│   ├── Agentes con SLAs diferentes (uno puede caer, otro no)
│   ├── Agentes con diferentes versiones de OpenClaw
│   ├── Resource isolation real (CPU/RAM por gateway)
│   ├── Update rolling (actualizar uno sin tocar otro)
│   └── Fault domains separados
│
└── NO → Multi-agent en un gateway es suficiente
```

---

## 22.2 Arquitectura: Docker Compose Multi-Gateway

### Diagrama

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SERVIDOR DEDICADO (64GB RAM, 1TB SSD)             │
│                                                                      │
│  ┌────────────── Docker Network: openclaw-federation ──────────────┐ │
│  │                                                                  │ │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────┐  │ │
│  │  │ GW: korax-main   │  │ GW: goreos-arch  │  │ GW: medico-ai  │  │ │
│  │  │ Port: 18789      │  │ Port: 18809      │  │ Port: 18829    │  │ │
│  │  │                  │  │                  │  │                │  │ │
│  │  │ Agent: main      │  │ Agent: goreos    │  │ Agent: medico  │  │ │
│  │  │ Model: Sonnet    │  │ Model: Opus      │  │ Model: Sonnet  │  │ │
│  │  │ Channels:        │  │ Channels:        │  │ Channels:      │  │ │
│  │  │  Telegram @Korax │  │  (webhook only)  │  │  Telegram @Med │  │ │
│  │  │  WhatsApp        │  │                  │  │                │  │ │
│  │  │                  │  │                  │  │                │  │ │
│  │  │ Sandbox: off     │  │ Sandbox: all     │  │ Sandbox: all   │  │ │
│  │  └────────┬─────────┘  └────────┬─────────┘  └───────┬────────┘  │ │
│  │           │                     │                     │           │ │
│  │  ┌────────┴─────────────────────┴─────────────────────┴────────┐  │ │
│  │  │              SHARED VOLUMES (bind mounts)                    │  │ │
│  │  │                                                              │  │ │
│  │  │  /srv/koda/knowledge/  (read-only)   ← KODA KB compartida  │  │ │
│  │  │  /srv/shared-memory/   (read-only)   ← docs compartidos    │  │ │
│  │  │  /srv/comms/           (read-write)  ← buzón inter-gateway │  │ │
│  │  └──────────────────────────────────────────────────────────────┘  │ │
│  │                                                                  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ Tailscale (mesh VPN)                                            │  │
│  │ Caddy / Traefik (reverse proxy, optional)                       │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### Principios de diseño

1. **Cada gateway es un container Docker independiente** con su propio config, state dir, workspace, y puerto
2. **Red compartida** (Docker bridge network) permite comunicación HTTP entre gateways
3. **Volúmenes compartidos** (read-only) dan acceso a repositorios de conocimiento comunes
4. **Comunicación inter-gateway** via webhooks HTTP (mecanismo nativo de OpenClaw)
5. **Cada gateway maneja sus propios canales** (un bot Telegram por gateway, o webhook-only)

---

## 22.3 Docker Compose: Configuración Base

### docker-compose.yml

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

### Estructura de directorios en el host

```
/srv/
├── koda/
│   ├── knowledge/          ← KODA KB compilada (YAML/MD, read-only)
│   └── repos/              ← Repos KODA (git clones, read-only)
├── shared-docs/            ← Documentos compartidos (cabinet global)
├── comms/                  ← Buzón inter-gateway (archivos JSON)
└── openclaw/
    └── workspaces/
        ├── korax/          ← Workspace de Korax
        │   ├── AGENTS.md, SOUL.md, etc.
        │   ├── memory/
        │   └── skills/
        ├── goreos/         ← Workspace de GoreOS Architect
        │   ├── AGENTS.md
        │   ├── memory/
        │   └── skills/
        └── medico/         ← Workspace de Médico AI
            ├── AGENTS.md
            ├── memory/
            └── skills/
```

---

## 22.4 Conocimiento Compartido: Patrones

### Patrón 1: Bind Mounts Read-Only (recomendado)

```yaml
volumes:
  - /srv/koda/knowledge:/shared/koda:ro    # todos leen, nadie escribe
```

Cada gateway puede referenciar la KB compartida en su config:

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

**Ventajas:**
- Un solo lugar para mantener la KB
- Actualización atómica: editas en el host → todos los gateways lo ven
- Read-only previene que un gateway corrupto modifique la KB

**Limitaciones:**
- Los gateways indexan la KB independientemente (cada uno tiene su propio SQLite de embeddings)
- Si la KB es grande (>10K archivos), el re-indexado post-cambio puede ser pesado

### Patrón 2: QMD Sidecar Compartido

Si la KB es muy grande, un QMD sidecar compartido evita indexación duplicada:

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

**Ventaja:** Un solo índice vectorial. N gateways consultando el mismo search.
**Trade-off:** Dependencia adicional. Si el QMD cae, memory search falla (con fallback a SQLite local).

### Patrón 3: Git Sync para KB

```bash
# Cron del host que actualiza la KB compartida
*/30 * * * * cd /srv/koda/knowledge && git pull --quiet
```

Los gateways ven los cambios en el próximo sync de su watcher (debounce ~1.5s post-write).

---

## 22.5 Comunicación Inter-Gateway: Patrones Nativos

OpenClaw no tiene un protocolo nativo de gateway-to-gateway. Pero tiene **webhooks** (Cap. 16) y **exec** (para HTTP calls). Estos son los bloques canónicos para construir comunicación.

### Patrón A: Webhook Relay (recomendado)

```
Korax (GW1) necesita que GoreOS (GW2) analice algo
      │
      ▼
Tool call: exec("curl -X POST http://goreos-gateway:18809/hooks/agent ...")
      │
      ▼
GoreOS (GW2) recibe webhook → agent turn aislado
      │
      ▼
GoreOS completa → delivery via announce a canal
      │                     ó
      ▼
GoreOS completa → POST resultado a http://korax-gateway:18789/hooks/wake
```

**Implementación concreta:**

GW1 (Korax) llama a GW2 (GoreOS):
```json
{
  "tool": "exec",
  "params": {
    "command": "curl -sX POST http://goreos-gateway:18809/hooks/agent -H 'Authorization: Bearer GOREOS_TOKEN' -H 'Content-Type: application/json' -d '{\"message\":\"Analiza la propuesta de GORE para el sistema de actas\",\"deliver\":false,\"model\":\"anthropic/claude-opus-4-6\"}'"
  }
}
```

GW2 (GoreOS) responde via webhook de vuelta:
```json5
// En AGENTS.md de goreos-gateway:
// "Al terminar un análisis, envía el resultado a Korax via:
//  curl -sX POST http://korax-gateway:18789/hooks/wake
//    -H 'Authorization: Bearer KORAX_HOOKS_TOKEN'
//    -d '{\"text\":\"GoreOS analysis complete: ...\"}'"
```

### Patrón B: Buzón de Archivos (fire-and-forget)

Comunicación asíncrona via archivos en un volumen compartido:

```
/srv/comms/
├── korax-to-goreos/
│   ├── 2026-02-20T22-30-00Z-analyze-actas.json
│   └── 2026-02-20T23-00-00Z-review-model.json
├── goreos-to-korax/
│   ├── 2026-02-20T22-45-00Z-analysis-result.json
│   └── ...
└── medico-to-korax/
    └── ...
```

```json
// Archivo de mensaje
{
  "from": "goreos",
  "to": "korax",
  "timestamp": "2026-02-20T22:45:00Z",
  "type": "analysis-result",
  "payload": {
    "summary": "La propuesta tiene 3 gaps...",
    "details": "..."
  },
  "status": "pending"  // pending → read → processed
}
```

Cada gateway tiene un heartbeat que revisa su buzón:

```markdown
# HEARTBEAT.md de korax-gateway
- Revisar /shared/comms/goreos-to-korax/ por mensajes pending
- Revisar /shared/comms/medico-to-korax/ por mensajes pending
- Si hay mensajes, leerlos y procesar
```

**Ventajas:** Simple, sin dependencias de red, auditable (archivos en disco), tolerante a fallos (si un gateway está caído, los mensajes esperan).

**Desventajas:** Latencia (depende del intervalo del heartbeat). No es real-time.

### Patrón C: Docker Network + Direct Webhook (real-time)

```yaml
networks:
  openclaw-federation:
    driver: bridge
```

Los containers se resuelven por nombre (`goreos-gateway`, `korax-gateway`) dentro de la red Docker. No necesitan IPs estáticas.

```bash
# Desde korax-gateway, GoreOS es alcanzable:
curl http://goreos-gateway:18809/health
```

**Seguridad:** La red Docker bridge es internal — no expuesta a internet. Pero dentro de la red, cualquier container puede alcanzar a cualquier otro. Si necesitas aislamiento:

```yaml
networks:
  korax-goreos:  # solo estos dos pueden hablar
    driver: bridge
  korax-medico:  # solo estos dos
    driver: bridge
```

### Comparativa de patrones

| | Webhook Relay | Buzón de Archivos | Direct Network |
|--|--------------|-------------------|----------------|
| **Latencia** | ~1-5s | ~30s-30min (heartbeat) | ~1-5s |
| **Complejidad** | Media (tokens, curl) | Baja (archivos) | Media (network config) |
| **Tolerancia a fallos** | Baja (si GW2 caído, falla) | Alta (mensajes persisten) | Baja |
| **Auditabilidad** | Logs de webhook | Archivos en disco | Logs de webhook |
| **Real-time** | ✅ | ❌ | ✅ |
| **Mecanismo OpenClaw** | /hooks/agent + /hooks/wake | Heartbeat + read/exec | /hooks/agent |

**Recomendación:** Webhook relay para comunicación real-time + buzón de archivos como fallback para tolerancia a fallos.

---

## 22.6 Orquestación: Quién Coordina a Quién

### Patrón Hub-and-Spoke

```
                    ┌──────────┐
         ┌─────────┤  KORAX   ├─────────┐
         │         │  (hub)   │         │
         │         └────┬─────┘         │
         │              │               │
         ▼              ▼               ▼
  ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ GoreOS   │   │ Médico   │   │ Research │
  │ (spoke)  │   │ (spoke)  │   │ (spoke)  │
  └──────────┘   └──────────┘   └──────────┘
```

Korax es el hub: recibe mensajes del usuario, decide si necesita delegar a un especialista, y consolida resultados.

**Implementación:**
- Korax tiene un skill `delegate-to-specialist` que sabe hacer POST a los webhooks de cada spoke
- Los spokes tienen webhooks habilitados + tokens dedicados
- Los spokes retornan resultados via webhook de vuelta a Korax (o via buzón de archivos)

### Patrón Mesh (peer-to-peer)

```
  ┌──────────┐     ┌──────────┐
  │ Korax    │◄───►│ GoreOS   │
  │          │     │          │
  └────┬─────┘     └────┬─────┘
       │                │
       │    ┌──────────┐│
       └───►│ Médico   │◄┘
            │          │
            └──────────┘
```

Todos pueden hablar con todos. Más flexible pero más complejo.

**Implementación:**
- Cada gateway tiene tokens de webhook de todos los demás
- Cada AGENTS.md incluye instrucciones sobre cuándo contactar a qué gateway
- Riesgo de loops: A → B → A → B... Mitigar con headers de "origin" o message IDs

### Patrón Recomendado: Hub + Selective Spokes

```
Korax (hub):
  - Recibe TODO del usuario
  - Decide si procesar localmente o delegar
  - Tiene webhook tokens de todos los spokes
  - Consolida resultados

GoreOS (spoke):
  - Solo recibe via webhook (no channels directos)
  - Procesa y retorna a Korax
  - Puede contactar a Korax (bidireccional) para clarificaciones
  - NO contacta directamente a Médico

Médico (spoke):
  - Solo recibe via webhook
  - Procesa y retorna a Korax
  - NO contacta a otros spokes
```

---

## 22.7 Configuración de Cada Gateway

### Korax (hub)

```json5
{
  gateway: { port: 18789, auth: { mode: "token", token: "${KORAX_GATEWAY_TOKEN}" } },
  channels: {
    telegram: { botToken: "${TG_TOKEN_KORAX}", dmPolicy: "allowlist", allowFrom: ["tg:7192195698"] }
  },
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-sonnet-4-6", fallbacks: ["openai-codex/gpt-5.2"] },
      sandbox: { mode: "off" },
      memorySearch: { extraPaths: ["/shared/koda", "/shared/docs"] }
    },
    list: [{ id: "main", default: true }]
  },
  hooks: {
    enabled: true,
    token: "${KORAX_HOOKS_TOKEN}",
    defaultSessionKey: "hook:federation",
    allowRequestSessionKey: false
  }
}
```

### GoreOS (spoke, webhook-only)

```json5
{
  gateway: { port: 18809, auth: { mode: "token", token: "${GOREOS_GATEWAY_TOKEN}" } },
  // Sin channels de messaging — solo recibe via webhooks
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-opus-4-6" },
      sandbox: { mode: "all", scope: "agent", workspaceAccess: "rw",
        docker: { network: "bridge" }
      },
      memorySearch: {
        extraPaths: ["/shared/koda", "/shared/repos", "/shared/docs"]
      }
    },
    list: [{ id: "goreos", default: true }]
  },
  hooks: {
    enabled: true,
    token: "${GOREOS_HOOKS_TOKEN}",
    defaultSessionKey: "hook:goreos",
    allowRequestSessionKey: false
  }
}
```

### Médico (spoke, webhook + Telegram dedicado)

```json5
{
  gateway: { port: 18829, auth: { mode: "token", token: "${MEDICO_GATEWAY_TOKEN}" } },
  channels: {
    telegram: { botToken: "${TG_TOKEN_MEDICO}", dmPolicy: "allowlist", allowFrom: ["tg:7192195698"] }
  },
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-sonnet-4-6" },
      sandbox: { mode: "all", scope: "agent", workspaceAccess: "ro" },
      memorySearch: { extraPaths: ["/shared/docs"] }
    },
    list: [{ id: "medico", default: true }]
  },
  hooks: {
    enabled: true,
    token: "${MEDICO_HOOKS_TOKEN}",
    defaultSessionKey: "hook:medico",
    allowRequestSessionKey: false
  }
}
```

---

## 22.8 Skill: Federation Delegate

Un skill en el workspace de Korax que encapsula la lógica de delegación:

```markdown
# skills/federation-delegate/SKILL.md
---
name: federation-delegate
description: "Delegar tareas a gateways especializados de la federación (GoreOS, Médico, Research)"
---

# Federation Delegate

## Gateways disponibles

| Gateway | Endpoint | Dominio | Modelo |
|---------|----------|---------|--------|
| goreos | http://goreos-gateway:18809 | GORE Ñuble, GoreOS, ORKO, transformación digital | Opus |
| medico | http://medico-gateway:18829 | Medicina de urgencia, protocolos clínicos | Sonnet |

## Cómo delegar

```bash
curl -sX POST http://<gateway>:<port>/hooks/agent \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"message":"<TAREA>","deliver":false,"model":"<MODEL>"}'
```

## Cuándo delegar

- Análisis profundo de GoreOS / GORE Ñuble → goreos
- Consulta clínica / protocolo médico → medico
- Tarea que requiere Opus y es de larga duración → goreos (tiene Opus como primary)

## Cuándo NO delegar

- Tareas simples (responder directamente)
- Tareas que necesitan contexto conversacional reciente
- Cuando el usuario pidió explícitamente que TÚ lo hagas

## Resultado

El spoke procesa y puede:
1. Retornar via webhook a /hooks/wake (real-time)
2. Dejar resultado en /shared/comms/<spoke>-to-korax/ (async)

Revisar /shared/comms/ si el webhook no llegó.
```

---

## 22.9 Seguridad de la Federación

### Principios

| Principio | Implementación |
|-----------|---------------|
| **Tokens dedicados por gateway** | Cada webhook endpoint tiene su propio token |
| **Red interna** | Docker bridge, no expuesto a internet |
| **Read-only KB** | Volúmenes compartidos montados `:ro` |
| **Sandbox en spokes** | Spokes corren sandboxed; solo el hub tiene host access |
| **Content wrapping** | Webhooks tratan payloads como untrusted por default |
| **No session key override** | `allowRequestSessionKey: false` en todos |
| **No channel público en spokes** | Spokes sin channels o con allowlist estricto |

### Threat model adicional

| Amenaza | Mitigación |
|---------|-----------|
| Spoke comprometido envía webhook malicioso al hub | Content safety wrapper + hub trata como untrusted |
| Hub comprometido envía instrucciones a spoke | Spoke sandbox limita blast radius |
| KB compartida modificada | Montada `:ro`; solo el host puede editar |
| Spoke accede a KB de otro dominio | Montar solo las KB relevantes por spoke |
| Loop de webhooks (A→B→A→B...) | Message ID tracking + max-depth header |

### Anti-loop

Incluir un header `X-Federation-Depth` en las llamadas inter-gateway:

```bash
curl -H "X-Federation-Depth: 1" ...
```

En AGENTS.md del spoke:
```markdown
Si recibes un mensaje con depth ≥ 2, NO reenvíes a otro gateway. Procesa localmente.
```

---

## 22.10 Operaciones

### Startup / Shutdown

```bash
# Levantar toda la federación
docker compose up -d

# Levantar solo un gateway
docker compose up -d goreos-gateway

# Detener un gateway sin afectar otros
docker compose stop medico-gateway

# Rolling update de un spoke
docker compose pull goreos-gateway
docker compose up -d --no-deps goreos-gateway

# Logs de un gateway específico
docker compose logs -f korax-gateway
```

### Health checks

```bash
# Todos a la vez
for gw in korax goreos medico; do
  echo -n "$gw: "
  curl -sf "http://127.0.0.1:$(case $gw in korax) echo 18789;; goreos) echo 18809;; medico) echo 18829;; esac)/health" && echo "OK" || echo "FAIL"
done
```

### Monitoring

```yaml
# docker-compose.override.yml (opcional)
services:
  healthcheck:
    image: alpine/curl
    container_name: federation-healthcheck
    networks:
      - openclaw-federation
    entrypoint: /bin/sh
    command: -c 'while true; do
      for gw in korax-gateway:18789 goreos-gateway:18809 medico-gateway:18829; do
        curl -sf http://$$gw/health > /dev/null || echo "$$(date) FAIL: $$gw";
      done;
      sleep 60;
    done'
    restart: unless-stopped
```

### Backup

```bash
# Backup de TODA la federación
tar -czvf ~/backups/federation-$(date +%Y%m%d).tar.gz \
  /srv/openclaw/workspaces/ \
  /srv/koda/knowledge/ \
  /srv/shared-docs/ \
  docker-compose.yml \
  .env
```

Para state (auth profiles, sessions): los Docker named volumes se backupean con:
```bash
docker run --rm -v korax-state:/data -v ~/backups:/backup alpine \
  tar -czf /backup/korax-state-$(date +%Y%m%d).tar.gz -C /data .
```

---

## 22.11 Scaling: De 3 a N Gateways

### Agregar un nuevo spoke

1. Crear workspace: `mkdir -p /srv/openclaw/workspaces/new-spoke`
2. Crear bootstrap files: `AGENTS.md`, `SOUL.md` mínimos
3. Agregar servicio en `docker-compose.yml` (copiar template)
4. Generar tokens: gateway + hooks
5. `docker compose up -d new-spoke-gateway`
6. Agregar endpoint al skill `federation-delegate` de Korax
7. Test: `curl http://new-spoke-gateway:<port>/health`

### Límites prácticos

| Recurso | Por gateway | 10 gateways |
|---------|-----------|-------------|
| RAM (idle) | ~200-400 MB | ~2-4 GB |
| RAM (active, con sandbox) | ~500 MB-1 GB | ~5-10 GB |
| CPU (idle) | <1% | <5% |
| Puertos | 1 base + ~20 derived | 10 base + ~200 derived |
| Disco (state) | ~50-500 MB | ~0.5-5 GB |

Un servidor de 64GB RAM puede hospedar cómodamente **20-30 gateways** con sandboxes ligeros.

---

## Resumen del Capítulo

| Concepto | Decisión de diseño |
|----------|-------------------|
| **Container per gateway** | Aislamiento de proceso real (fault domain, resources, updates) |
| **Docker bridge network** | Comunicación inter-gateway sin exponer a internet |
| **Bind mounts :ro** | KB compartida sin riesgo de corrupción |
| **Webhook relay** | Comunicación real-time usando mecanismo nativo de OpenClaw |
| **Buzón de archivos** | Fallback tolerante a fallos para comunicación async |
| **Hub-and-spoke** | Korax como orquestador, spokes como especialistas |
| **Tokens dedicados** | Blast radius: token de spoke comprometido ≠ acceso al hub |
| **Skill federation-delegate** | Encapsula lógica de delegación en un skill reutilizable |
| **Rolling updates** | Actualizar un spoke sin tocar el hub ni otros spokes |
| **Content wrapping** | Todo lo que viene de otro gateway se trata como untrusted |

### Cuándo usar este patrón vs multi-agent en un gateway

```
¿Necesitas fault isolation real?
├── NO → Multi-agent en un gateway (Cap. 6-8)
│
└── SÍ → ¿Cuántos "cerebros" especializados?
         ├── 2-3 → Multi-gateway Docker Compose (este capítulo)
         └── 10+ → Kubernetes o similar (fuera de scope)
```

---

*Este capítulo extiende la Parte VI del manual con patrones avanzados de deployment.*

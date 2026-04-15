---
_manifest:
  urn: urn:ops:kb:arquitectura-stack-kora
  provenance:
    created_by: ops/clawstack + kora/curator
    created_at: '2026-03-23'
    source: Estado operacional del stack desplegado en Hetzner i7-7700 62GB Ubuntu
      24.04
version: 1.0.0
status: published
tags:
- arquitectura
- stack
- docker
- containers
- redes
- inventario
- produccion
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:ops:kb:arquitectura-stack-kora
relations:
  cites:
  - urn:ops:kb:deploy-agente-kora-en-openclaw
  - urn:ops:kb:federacion-kora-v2
  - urn:ops:kb:principios-transmutacion-kora-openclaw
  - urn:ops:kb:ux-telegram-openclaw
---


# Arquitectura del stack KORA — Estado operacional

Vista completa del stack de producción desplegado en servidor Hetzner (i7-7700, 62GB RAM, Ubuntu 24.04, IP 138.201.53.205).

---

## Diagrama de red

```
Internet (138.201.53.205, *.sanixai.com Cloudflare DNS-only)
 │
 │ :80/:443
 ▼
┌──────────────────────────────────────────────┐
│ RED: web (Traefik routing) │
│ │
│ traefik reverse proxy + TLS auto │
│ crowdsec WAF + IP reputation │
│ traefik-bouncer bouncer middleware │
│ netdata monitor.sanixai.com │
│ kora-panel kora.sanixai.com │◄── dual-homed
│ opmodel-dev opmodel.sanixai.com │
└──────────────────────────────────────────────┘
 (redes aisladas, sin puente)
┌──────────────────────────────────────────────┐
│ RED: kora-federation (bridge Docker) │
│ │
│ kora-personal :18789 korax 🦴 │
│ kora-pca :8100 sidecar PCA │
│ kora-steipete :18810 steipete 🏗️ │
│ kora-salubrista :18830 salubrista 🏥 │
│ kora-panel :3000 panel web │◄── dual-homed
│ │
│ Comunicación: hooks HTTP + DNS interno │
│ Gateways: bind=lan (0.0.0.0 en container) │
│ Host ports: 127.0.0.1 only (no publico) │
└──────────────────────────────────────────────┘
```

---

## Inventario de containers

| Container | Imagen | Red | Puerto | Función | RAM |
|---|---|---|---|---|---|
| traefik | traefik:latest | web | :80/:443 | Reverse proxy, TLS, routing | ~20MB |
| crowdsec | crowdsecurity/crowdsec | web | — | WAF, ban lists | ~30MB |
| traefik-bouncer | fbonalair/traefik-crowdsec-bouncer | web | — | Middleware bouncer | ~6MB |
| netdata | netdata/netdata:stable | web | — | Monitoring (monitor.sanixai.com) | ~270MB |
| watchtower | containrrr/watchtower | — | — | Auto-update infra containers | ~7MB |
| kora-personal | kora-personal:latest | federation | :18789 | Gateway korax (OpenClaw v2026.3.22) | ~400MB / 2GB |
| kora-pca | kora-pca:latest | federation | :8100 | Sidecar PCA (Python, SQLite) | ~115MB / 128MB |
| kora-steipete | openclaw-local:latest | federation | :18810 | Gateway steipete (OpenClaw v2026.3.22) | ~400MB / 2GB |
| kora-salubrista | openclaw-local:latest | federation | :18830 | Gateway salubrista-hah (OpenClaw v2026.3.22) | ~410MB / 2GB |
| kora-panel | kora-panel:latest | web + federation | :3000 | Panel web (kora.sanixai.com) | ~50MB / 256MB |
| opmodel-dev | opmodel-opmodel-dev | web | :5173 | Dev container opmodel | ~145MB |

Total: 11 containers. RAM estimada en uso: ~1.9GB de 62GB disponibles.

---

## Inventario de agentes OpenClaw

| Agente | Namespace | Puerto | Bot Telegram | Modelo | Arquitectura | KBs |
|---|---|---|---|---|---|---|
| korax | korvo | 18789 | @korax_kv_bot | claude-opus-4-6 | Caso B (+ sidecar PCA) | korvo/ (2 archivos) |
| steipete | dev | 18810 | @stiepe_kv_bot | claude-opus-4-6 | Caso A (puro, workers exec) | dev/ (20+ archivos) |
| salubrista-hah | salud | 18830 | @hah_kv_bot | claude-opus-4-6 | Caso A (puro, 9 skills) | salud/ (13 archivos, 623K chars) |

Port spacing: mínimo 20 (siguiente disponible: 18850).

---

## Subdominios activos

| Subdominio | Servicio | Auth | TLS |
|---|---|---|---|
| `traefik.sanixai.com` | Dashboard Traefik | Basic auth | Let's Encrypt auto |
| `monitor.sanixai.com` | Netdata | Sin auth (CrowdSec protege) | Let's Encrypt auto |
| `kora.sanixai.com` | Panel federación | Basic auth (admin:kora2026) | Let's Encrypt auto |

Wildcard DNS `*.sanixai.com` → 138.201.53.205. TLS via Let's Encrypt TLS-ALPN-01 (automático por Traefik).

---

## Volúmenes

| Volumen | Propósito | Container |
|---|---|---|
| `compose_kora-personal-data` | State OpenClaw korax (config, auth, sessions) | kora-personal |
| `compose_kora-pca-data` | SQLite PCA | kora-pca |
| `compose-steipete_kora-steipete-data` | State OpenClaw steipete | kora-steipete |
| `compose-salubrista_kora-salubrista-data` | State OpenClaw salubrista | kora-salubrista |

Named volumes para state OpenClaw (config vive aquí, no en bind mount — atomic rename). Workspaces son bind mounts directos.

---

## Paths de producción

```
/srv/kora/
├── compose/ ← korax gateway
├── compose-steipete/ ← steipete gateway
├── compose-salubrista/ ← salubrista gateway
├── config/{personal,steipete,salubrista}/ ← openclaw.json5 fuente
├── workspaces/ ← workspaces transmutados (bind mount RW)
│ ├── personal/agents/korax/
│ ├── steipete/agents/steipete/
│ └── salubrista/agents/salubrista-hah/
├── knowledge/ ← KBs compartidas (mount RO)
│ ├── korvo/
│ ├── dev/
│ └── salud/
├── shared/ ← storage federation v2
│ ├── federation/ ← directorio agentes (RO todos)
│ ├── korax/ ← propio korax (RW)
│ ├── steipete/ ← propio steipete (RW)
│ └── salubrista-hah/ ← propio salubrista (RW)
├── scripts/
│ ├── sync-config.sh ← merge config host→volume
│ └── federation-health.sh ← health check centralizado
└── backups/

~/projects/
├── kora-panel/ ← source del panel web
├── openclaw/ ← source OpenClaw (checkout v2026.3.22)
├── docker-stacks/ ← infra (traefik, security, monitoring)
├── pca/ ← PCA source
└── opmodel/ ← proyecto activo
```

---

## Flujos de comunicación

### Usuario → Agente (normal)

```
Telegram → Bot API → kora-{gateway} :port → OpenClaw → Anthropic API → respuesta → Telegram
```

### Derivación cross-gateway

```
agente-A → web_fetch POST http://kora-B:{port}/hooks/agent → agente-B responde en su Telegram
```

Requiere: `hooks.enabled: true`, `bind: "lan"`, token compartido. La respuesta aparece en el bot Telegram del destino.

### Panel → Gateways

```
kora-panel → HTTP /api/* → kora-{gateway}:{port} (health, hooks, WS proxy)
kora-panel → Docker socket (RO) → estado containers, restart
```

### Sync config

```
operador edita config/*/openclaw.json5
 → sync-config.sh (merge host + runtime keys)
 → docker compose restart
```

---

## Referencias

- Federación cross-gateway y hooks: `urn:ops:kb:federacion-kora-v2`
- Config de comportamiento de agentes: `urn:ops:kb:ux-telegram-openclaw`
- Tutorial de deploy paso a paso: `urn:ops:kb:deploy-agente-kora-en-openclaw`
- Principios de transmutación: `urn:ops:kb:principios-transmutacion-kora-openclaw`

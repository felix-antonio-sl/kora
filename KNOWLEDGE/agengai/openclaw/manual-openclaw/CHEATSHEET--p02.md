---
_manifest:
  urn: urn:agengai:kb:cheatsheet-p02
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- cheatsheet
lang: es
extensions:
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:agengai:kb:cheatsheet
---

# OpenClaw — Cheatsheet Definitivo - Parte 02

## ⏰ AUTOMATIZACIÓN

### Heartbeat vs Cron — Árbol de Decisión

```
¿Timing exacto?
├── SÍ → CRON (--cron "0 7 * * *")
└── NO → ¿Se batchea con otros checks?
 ├── SÍ → HEARTBEAT (agregar a HEARTBEAT.md)
 └── NO → ¿Model override / aislamiento?
 ├── SÍ → CRON isolated
 └── NO → HEARTBEAT
```

### Heartbeat

```json5
{ heartbeat: { every: "30m", model: "haiku", target: "last", activeHours: { start: "08:00", end: "23:00" } } }
```

- `HEARTBEAT_OK` → suprimido.
- Alerta → delivery. ~$2.70/mes con Haiku.

### Cron Jobs

| Kind | Ejemplo |
|------|---------|
| `at` | `--at "20m"` (one-shot, auto-delete) |
| `every` | `--every 3600000` (1h interval) |
| `cron` | `--cron "0 7 * * *"` (expresión) |

- `current` = job amarrado a la sesión actual.
- `session:<id>` = sesión persistente nombrada.
- One-shot retry: 30s → 1m → 5m para fallos transitorios.

| Session | Payload | Cuándo |
|---------|---------|--------|
| `main` | `systemEvent` (inyecta en main) | Reminders, con contexto conversacional |
| `isolated` | `agentTurn` (sesión fresh) | Reportes, análisis, model override |

| Delivery | Efecto |
|----------|--------|
| `announce` | Envía a canal de messaging |
| `webhook` | POST a URL |
| `none` | Solo internal |

### Hooks (código, sin LLM, gratis)

```
Events: command:new | agent:bootstrap | gateway:startup | message:received | message:sent
Bundled: session-memory | bootstrap-extra-files | command-logger | boot-md
```

- Hooks = TypeScript determinístico. **0 tokens.**

### Webhooks (HTTP ingress)

```
POST /hooks/wake → System event en main session (ligero)
POST /hooks/agent → Agent turn aislado con delivery (completo)
POST /hooks/<name> → Mapped hook con transforms (custom)
```

- Auth: `Authorization:
- Bearer <token>`.
- Siempre loopback/tailnet.

### Lobster (workflows determinísticos)

```
pipeline: "cmd1 | cmd2 | approve --prompt 'OK?' | cmd3"
```

- → 1 tool call = workflow completo.
- Approval gates con resume tokens. `llm-task` para LLM steps JSON-only.

- ---

## 🔧 OPERACIONES

```bash
openclaw status --all # diagnóstico general
openclaw doctor --fix # fixes automáticos
openclaw security audit --deep # auditoría completa
openclaw sessions --active 60 # sesiones activas
openclaw sandbox explain --agent X # tools resueltos
openclaw cron list # jobs programados
openclaw agents list --bindings # routing de agentes
```

### Gateway (systemd)

```bash
sudo systemctl status|restart openclaw-gateway
sudo journalctl -u openclaw-gateway -f
curl -s http://localhost:18789/health
```

### Backup (lo crítico)

```bash
tar -czvf ~/backups/openclaw-$(date +%Y%m%d).tar.gz \
 ~/.openclaw/openclaw.json ~/.openclaw/.env \
 ~/.openclaw/agents/*/agent/auth-profiles.json \
 ~/.openclaw/credentials/ ~/.openclaw/cron/jobs.json \
 ~/clawd/
```

- ---

## 📐 PATRONES RÁPIDOS

| Patrón | Config clave |
|--------|-------------|
| **Single + multi-channel** | 1 agente, `dmScope: main` |
| **Agent per persona** | `agents.list[]` + bindings por peer |
| **Orchestrator + workers** | `maxSpawnDepth: 2` |
| **Reader agent** | Sandbox + deny exec/write → summary → main |
| **Cron + webhook pipeline** | Cron isolated + /hooks/agent |
| **Minimal viable** | 1 canal + 1 agente + token |

- ---

## ⚡ REGLAS DE ORO

1. **Cada char en bootstrap se paga en cada turn** → MEMORY.md < 10KB
2. **Tool schemas son invisibles pero costosos** → menos tools = menos tokens
3. **Deny siempre gana** → nunca se re-habilita en capas posteriores
4. **Session key determina aislamiento** → mismo key = mismo contexto
5. **>1 persona + dmScope:main = leak** → per-channel-peer obligatorio
6. **Identity first, model last** → allowlists > prompt hardening
7. **Content = attack surface** → no solo los senders, todo lo que el agente lee
8. **Si no está escrito, no existe** → archivos > RAM
9. **Non-main es el sweet spot** → DMs en host, grupos en sandbox
10. **Diversidad de provider en fallbacks** → si uno cae, otro toma

- ---

- ---

## 🌐 FEDERACIÓN MULTI-GATEWAY (Docker)

- **Cuándo:** Fault isolation real, rolling updates, resource limits per-agent, diferentes versiones.

```
Docker Compose + bridge network + shared volumes (:ro) + webhooks
```

| Patrón | Comunicación | Latencia | Tolerancia |
|--------|-------------|----------|-----------|
| **Webhook relay** | POST /hooks/agent | ~1-5s | Baja (GW destino debe estar up) |
| **Buzón de archivos** | Volumen compartido + heartbeat | ~30s-30min | Alta (mensajes persisten) |
| **Docker network** | HTTP directo por nombre de container | ~1-5s | Baja |

- **Topología recomendada:** Hub (Korax) + Spokes (especialistas webhook-only)

```yaml
# Template: spoke en docker-compose.yml
spoke-gateway:
 image: openclaw:local
 networks: [openclaw-federation]
 ports: ["127.0.0.1:18809:18809"]
 volumes:
 - spoke-state:/home/node/.openclaw
 - ./workspaces/spoke:/home/node/.openclaw/workspace
 - /srv/koda/knowledge:/shared/koda:ro # KB compartida
 - /srv/comms:/shared/comms:rw # buzón inter-gateway
```

- **Seguridad:** Tokens dedicados por gateway · Red Docker internal · KB en :ro · Content wrapping · Anti-loop con depth header

- ---

- *`cabinet/docs/manual-openclaw/` — 22 capítulos + 5 apéndices — ~395KB — Feb 2026*

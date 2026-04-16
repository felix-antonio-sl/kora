# Infraestructura del Host (Korax)

*Referencia técnica. Verificar con comandos vivos para datos dinámicos (disco, RAM, versiones).*

---

## Servidor

- **Proveedor:** Hetzner Cloud (vServer KVM)
- **Hostname:** `clawdbot-hetzner`
- **Usuario:** `clawdbot` (UID 1000)
- **OS:** Ubuntu 24.04 LTS (Noble Numbat)
- **CPU:** AMD EPYC-Genoa, 4 cores
- **RAM:** 7.6 GB
- **Disco:** 150 GB SSD
- **Swap:** 4.0 GB

## Red

| Interfaz | IP | Descripción |
|----------|-----|-------------|
| **eth0** | `157.180.121.173` | IP pública (Hetzner) |
| **tailscale0** | `100.99.32.96` | IP Tailscale (tailnet) |
| **docker0** | `172.17.0.1/16` | Red Docker default |

**Tailscale:**
- Hostname: `clawdbot-hetzner`
- Funnel URL: `https://clawdbot-hetzner.tail84b159.ts.net`
- `/` → `http://127.0.0.1:18789` (gateway, Funnel on)
- `/gmail-pubsub` → `http://127.0.0.1:8788` (gog-gmail-watch, Funnel on)
- Nota: Funnel es per-port (443), ambos paths son públicos. Decisión consciente — ver AGENTS.md.

## Servicios Systemd

**Activos:**
- `openclaw-gateway.service` — gateway nativo, puerto 18789
- `gog-gmail-watch.service` — Gmail Pub/Sub → webhook, puerto 8788
- `docker.service`
- `tailscaled.service`
- `ssh.service`
- `netfilter-persistent.service` — reglas iptables persistentes

**Maskeados:**
- `cups.service` / `cups.socket` / `cups-browsed.service`

## Reglas iptables

- `DOCKER-USER -i eth0 -j DROP` — bloquea acceso externo a todos los containers Docker (persistente)

## Estructura de directorios

```
/home/clawdbot/
├── .openclaw/              # Configuración OpenClaw
│   ├── openclaw.json       # Config principal (API keys via ${VAR})
│   ├── .env                # Todos los secrets y API keys
│   ├── agents/             # Sesiones de agentes
│   ├── cron/               # Jobs programados
│   └── memory/             # Memoria persistente (main.sqlite)
├── .config/gog/            # Credenciales Google OAuth
├── clawd/                  # Workspace del agente Korax
│   ├── [7 bootstrap files] # AGENTS, SOUL, USER, IDENTITY, TOOLS, HEARTBEAT, MEMORY
│   ├── CLAUDE.md           # Dev file para Claude Code (no se inyecta)
│   ├── memory/             # Memoria diaria + GTD
│   ├── skills/             # Skills custom (inbox, rol)
│   ├── scripts/            # Scripts operativos
│   ├── cabinet/            # Gabinete documental
│   └── canvas/             # Webchat UI
└── clawdbot/               # OpenClaw source code
```

## Software principal

| Software | Ubicación |
|----------|-----------|
| Node.js | Runtime principal |
| Docker | Containerización |
| Docker Compose | Orquestación |
| Git | Control versiones |
| gog | Google OAuth CLI (`/usr/local/bin/gog`) |
| Tailscale | VPN mesh |

*Versiones exactas: verificar con `node -v`, `docker -v`, `gog --version`, `openclaw --version`.*

## Nodo `air` (Mac)

**Conexión:** OpenClaw node host → VPS gateway vía Tailscale Funnel (wss://clawdbot-hetzner.tail84b159.ts.net:443).

**Servicio:** LaunchAgent `ai.openclaw.node.plist` (NO gateway — el Mac corre como nodo, no como gateway standalone).

**Config:** `~/.openclaw/node.json`:
```json
{
  "version": 1,
  "nodeId": "d98565a1-46c0-49cb-8267-61ad4e37b87b",
  "displayName": "air",
  "gateway": {
    "host": "clawdbot-hetzner.tail84b159.ts.net",
    "port": 443,
    "tls": true
  }
}
```

**Capacidades:** `system.run`, `system.which`, `browser.proxy`.

### Network Modes (korax-switch)

Script: `~/.korax-switch.sh` (sourced desde `.zshrc`).
Comando: `korax <modo>`.

| Modo | Comando | Red | /etc/hosts | Tailscale | DAU/SGH |
|------|---------|-----|-----------|-----------|---------|
| **minsal** | `korax minsal` | Hospital San Carlos (MINSAL) | Override: `185.40.234.37 clawdbot-hetzner...` (Funnel IP) | Bloqueado por Fortinet DPI | ✅ Accesibles (10.6.85.x) |
| **normal** | `korax normal` | Cualquier otra (casa/GORE/móvil) | Sin override | Activo, MagicDNS resuelve | ❌ No accesibles |

**¿Por qué se necesita el override en MINSAL?**
- Fortinet bloquea Tailscale (WireGuard protocol) → MagicDNS no funciona
- Pero Funnel es HTTPS puro en puerto 443 → Fortinet lo deja pasar
- `/etc/hosts` fuerza resolución del hostname del gateway a la IP pública del Funnel (185.40.234.37)
- Sin override, el hostname no resuelve (MagicDNS muerto) y el nodo no conecta

**Acciones de cada modo:**
1. Modifica `/etc/hosts` (requiere sudo interactivo)
2. Flush DNS cache (dscacheutil + mDNSResponder)
3. Verifica: DNS resolución → Gateway HTTP → (MINSAL: DAU + SGH)
4. `openclaw node restart`
5. En modo normal: abre Tailscale.app si estaba detenido

**Desde Korax (VPS) el acceso a DAU/SGH es vía:**
```
Korax → nodes run (air) → curl http://10.6.85.218/dau/... (red MINSAL local)
Korax → nodes run (air) → curl http://10.6.85.228:8085/SGH/... (red MINSAL local)
```
El gateway no toca la red MINSAL directamente — todo pasa por el nodo `air` como proxy de ejecución.

### Problema conocido post-update

`openclaw update` solo reinicia el gateway service (inexistente en Mac). El node service queda caído.

**Procedimiento post-update Mac:**
```bash
oc-update    # alias: openclaw update --no-restart && openclaw node restart
openclaw node status   # verificar
```

### Monitoreo

Cron `node-air-watchdog` en VPS (cada 30 min). Alerta por Telegram si `air` desconectado.

### Diagnóstico rápido
```bash
# Desde VPS (Korax):
nodes status

# Desde Mac (Korvo):
openclaw node status
openclaw node restart
korax status          # verifica modo, DNS, gateway, DAU/SGH
tail -50 ~/.openclaw/logs/node.log
```

### Reconexión paso a paso (si air desconectado)

1. Korvo abre terminal en Mac
2. `korax status` → verificar modo y conectividad
3. Si en MINSAL y no conecta: `korax minsal` (re-aplica override + restart)
4. Si en otra red: `korax normal` (quita override + inicia Tailscale + restart)
5. Si nodo no conecta tras switch: `openclaw node restart`
6. Si persiste: `tail -50 ~/.openclaw/logs/node.log` → diagnosticar
7. Si todo falla: foreground mode `OPENCLAW_GATEWAY_TOKEN=xxx openclaw node run`

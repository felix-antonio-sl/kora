# Infraestructura completa — 2026-03-31 (verificado 2026-04-06)

## Genealogía de despliegues

Tres generaciones de agentes OpenClaw de Felix Sanhueza (korvo):

| Gen | Nombre | Infra | Host | Modelo default | Estado |
|-----|--------|-------|------|----------------|--------|
| 1a | korvo | Gateway nativo systemd | clawdbot-hetzner (157.180.121.173) | anthropic/claude-opus-4-6 | Legacy — 5 agentes |
| 2a | kora (federación) | Multi-gateway Docker | hetzner2897261 (138.201.53.205) | varios | Coexiste con 3a — 4 containers healthy |
| 3a | Clawforge | Gateway nativo systemd | hetzner2897261 (138.201.53.205) | anthropic/claude-opus-4-6 | **Vigente** — 6 agentes |

**Hecho clave:** hetzner2897261 aloja la 2a gen (Docker) y la 3a gen (nativo systemd) en paralelo. Sin conflicto de puertos (Docker usa 18789-18850, nativo usa 18790).

Clawforge (3a gen, main) administra ambos VPS: hetzner2897261 (local) y clawdbot-hetzner (remoto vía SSH).

## Mapa completo de agentes y bots Telegram

### 1a gen — korvo (clawdbot-hetzner, 157.180.121.173)

Infra: gateway nativo systemd (NO Docker). Loopback :18789.

| Agente | Emoji | Bot Telegram | Modelo | Heartbeat | Últ. actividad |
|---|---|---|---|---|---|
| main (Korax) | 🪶 | @Clawd_fx_bot | claude-opus-4-6 | disabled | Hook activo |
| clawmaster | 🔧 | @klawmonster_bot | claude-opus-4-6 | 6h | 4h |
| pensador (Korpensulo) | 🔮 | @korpensulo_bot | claude-opus-4-6 | disabled | 6 días |
| salubrista (HaH) | 🏠 | @hospidomibot | claude-opus-4-6 | disabled | 3 días |
| urgencista | 🏥 | @klinikurgo_bot | claude-opus-4-6 | disabled | 2 días |

Canal adicional: Slack (1 cuenta, bot @korax en workspace Korvo-WS).
RAM host: 7.6G (1.4G usada), swap 4G (564M usada). Gateway healthy.

### 2a gen — kora (Docker, hetzner2897261)

| Contenedor | Imagen | Agente(s) | Emoji | Bot Telegram | Puerto | Estado |
|---|---|---|---|---|---|---|
| kora-personal | kora-personal:latest | korax | 🦴 | @korax_kv_bot | :18789 | Up 3d (healthy) |
| kora-clawforge | kora-clawforge:latest | clawforge, curator | ⚒️ 📚 | @clawforge_kv_bot | :18850 | Up 3d (healthy) |
| kora-steipete | openclaw-local:latest | steipete | 🏗️ | @stiepe_kv_bot | :18810 | Up 3d (healthy) |
| kora-salubrista | openclaw-local:latest | salubrista-hah | 🏥 | @hah_kv_bot | :18830 | Up 3d (healthy) |
| kora-pca | kora-pca:latest | — (app PCA) | — | — | :8100 | Up 7d (healthy) |
| kora-panel | kora-panel-kora-panel:latest | — (panel UI) | — | — | 3000/tcp | Up 13d (healthy) |

Red Docker: `kora-federation` (bridge). Volúmenes: `compose-*_kora-*-data`.
Compose dirs: `/srv/kora/compose*`.
Fix 2026-03-31: NODE_OPTIONS 1536→3072 MB en kora-steipete y kora-salubrista (OOM crash loop).

Contenedores compartidos en hetzner2897261:

| Contenedor | Función | Estado |
|---|---|---|
| traefik | Reverse proxy (puertos 80/443 expuestos al host) | Up 4d |
| crowdsec + traefik-bouncer | Security / IPS | Up 2 semanas |
| netdata | Monitoring | Up 7d (healthy) |
| watchtower | Auto-update containers | Up 2 semanas |
| openclaw-sandbox (×2) | Sandbox salubrista, gtd-integral | Up 7-10d |
| dau-board | nginx:alpine | Up 4d |
| hdos-web | Dashboard | Up 10d |
| opmodel-dev | Model UI | Up 12d |

### 3a gen — Clawforge (nativo systemd, hetzner2897261)

Gateway: systemd, v2026.4.2, bind 127.0.0.1:18790. Node.js v24.13.1.

| Agente | Emoji | Bot Telegram | Modelo sesión | Heartbeat | Exec | Sesiones | Últ. actividad |
|---|---|---|---|---|---|---|---|
| main (Clawforge) ✦ | ⚒️ | @fragua_kv_bot | qwen3.6-plus:free | 15m | full | 9 | Ahora |
| mente-omega | Ω | @tensario_kv_bot | qwen3.6-plus:free | disabled | allowlist | 10 | 2h |
| salubrista | 🏥 | @vector_kv_bot | claude-opus-4-6 | 0m | — | 3 | 2h |
| steipete | ⚡ | @filo_kv_bot | glm-5.1 | 0m | full | 3 | 2h |
| gtd-integral | 🔭 | @david_kv_bot | glm-5.1 | 30m | allowlist | 3 | 16m |
| allan-kelly | 🏗️ | @telos_kv_bot | qwen3.6-plus:free | disabled | allowlist | 2 | 3 días |

Modelo default gateway: claude-opus-4-6. Fallbacks: minimax/MiniMax-M2.7-highspeed, zai/glm-5.1.
RAM host: 62G (10G usada). Disco: 49G (64% usado). Uptime: 19 días.
Memory: 24 ficheros, 580 chunks, vector+fts ready, cache 528.
Security: 3 warnings (trustedProxies vacío, approve-all, exec=full en todos).

## VPS secundario — clawdbot-hetzner

- Acceso: `ssh clawdbot@157.180.121.173` (clave ed25519 autorizada)
- OpenClaw: PATH: `export PATH="$HOME/.npm-global/bin:$PATH"`
- Gateway: systemd, loopback :18789
- OS: Ubuntu, kernel 6.8.0-100-generic
- Usuario: clawdbot (no felix)
- Warnings conocidos: plugins stale (cosméticos)
- Fix 2026-03-31: eliminado campo invalido `messages.tts.edge`, provider→microsoft
- steipete y allan-kelly tienen acceso SSH documentado en sus TOOLS.md

## Totales

- **16 agentes** en 3 generaciones
- **15 bots Telegram** únicos, 0 conflictos
- **2 VPS** (hetzner2897261 + clawdbot-hetzner)
- **2 gateways** (uno por VPS)

---
_manifest:
  urn: "urn:ops:kb:tres-generaciones-agentes-kora"
  provenance:
    created_by: "ops/clawforge + kora/curator"
    created_at: "2026-04-02"
    source: "Taxonomía operacional de las tres generaciones del ecosistema de agentes KORA"
version: "1.0.0"
status: published
tags: [arquitectura, generaciones, korvo, federacion, clawforge, openclaw, docker, systemd, evolucion]
lang: es
---

# Tres generaciones del ecosistema de agentes KORA

Taxonomía de las tres generaciones que componen el ecosistema de agentes IA de Felix, diferenciadas por host, modelo base y paradigma de deployment.

---

## Resumen comparativo

| | 1ª generación | 2ª generación | 3ª generación |
|---|---|---|---|
| **Nombre** | korvo | Federación KORA | Clawforge |
| **Host** | clawdbot-hetzner (157.180.121.173) | hetzner2897261 (Docker) | hetzner2897261 (systemd nativo) |
| **Modelo default** | minimax/MiniMax-M2.7-highspeed | zai/glm-5.1 | anthropic/claude-opus-4-6 |
| **Deployment** | Standalone | Contenedores Docker multi-gateway | Servicio systemd de usuario |
| **Agente principal** | korax | korax · steipete · salubrista-hah | Clawforge (main) |
| **Versión OpenClaw** | legacy | v2026.3.x | v2026.4.x |

---

## 1ª Generación — korvo

**Host**: clawdbot-hetzner (`157.180.121.173`) — servidor Hetzner separado.

**Agente**: korax (`@korax_kv_bot`)
- Workspace: `AGENTS/korvo/korax/`
- Knowledge: `KNOWLEDGE/korvo/`
- Modelo: `minimax/MiniMax-M2.7-highspeed`

**Características**:
- Infraestructura más antigua del ecosistema
- Separada físicamente del stack principal
- Knowledge base orientada al dominio personal/filosófico de korvo (`dan-koe-filosofia-creador.md`, `manual-de-vida.md`)

---

## 2ª Generación — Federación KORA

**Host**: hetzner2897261, capa Docker (`kora-federation` bridge network).

**Agentes en la federación**:
- **korax** (`kora-personal`, puerto 18789) — gateway personal con sidecar PCA
- **steipete** (`kora-steipete`, puerto 18810) — especialista en desarrollo
- **salubrista-hah** (`kora-salubrista`, puerto 18830) — dominio de salud

**Modelo default**: `zai/glm-5.1`

**Características clave**:
- Multi-gateway en bridge Docker (`kora-federation`)
- Comunicación cross-gateway via `POST /hooks/agent` + DNS Docker interno
- Storage compartido en `/srv/kora/shared/` con control de visibilidad por bind mounts
- Panel web de operación en `kora.sanixai.com` (React + Express, Docker socket RO)
- `gateway.bind: "lan"` obligatorio para alcanzabilidad inter-container
- Transmutación KORA → OpenClaw vía strip de frontmatter (sin modificar contenido operacional)

**Arquitectura de red**:
```
Red web (Traefik, *.sanixai.com)
  traefik · crowdsec · netdata · kora-panel · opmodel-dev

Red kora-federation (bridge Docker)
  kora-personal :18789 · kora-steipete :18810 · kora-salubrista :18830
  kora-panel (dual-homed: web + federation)
```

**Documentación de referencia**:
- `urn:ops:kb:arquitectura-stack-kora` — inventario completo
- `urn:ops:kb:federacion-kora-v2` — federación cross-gateway y storage
- `urn:ops:kb:principios-transmutacion-kora-openclaw` — principios de deploy
- `urn:ops:kb:deploy-agente-kora-en-openclaw` — tutorial paso a paso

---

## 3ª Generación — Clawforge

**Host**: hetzner2897261, systemd nativo (sin Docker).

**Agente principal**: Clawforge (`@fragua_kv_bot`)
- Workspace: `~/.openclaw/workspace/`
- Servicio: `systemctl --user openclaw-gateway`
- Versión: OpenClaw 2026.4.x (actualización continua via `npm install -g openclaw@latest`)

**Agentes dependientes** (mismo gateway, modelos propios):
| Agente | Bot Telegram | Modelo |
|---|---|---|
| mente-omega | @tensario_kv_bot | anthropic/claude-opus-4-6 |
| salubrista | @vector_kv_bot | anthropic/claude-opus-4-6 |
| steipete | @filo_kv_bot | openai-codex/gpt-5.4 |
| gtd-integral | @david_kv_bot | anthropic/claude-opus-4-6 |
| allan-kelly | @telos_kv_bot | anthropic/claude-opus-4-6 |

**Características clave**:
- Un solo proceso gateway sirve 6 agentes (hub-and-spoke)
- Sin Docker — acceso directo al filesystem del host, herramientas exec nativas
- Puertos: 18789 (RPC), 18790 (health/websocket)
- Configuración en `~/.openclaw/openclaw.json` — modificar via `openclaw config set` o `gateway → config.patch`, nunca write directo
- `acp.runtime.ttlMinutes: 240` — kill automático de sesiones colgadas tras 4h
- `diagnostics.stuckSessionWarnMs: 300000` — warning a los 5min de sesión atascada

---

## Evolución y coexistencia

Las tres generaciones coexisten activamente. No hay migración total de una a otra — cada generación cubre un rol distinto:

- **1ª gen (korvo)**: conocimiento personal / filosófico, modelo económico
- **2ª gen (federación)**: dominio de salud, desarrollo, con federación cross-gateway
- **3ª gen (Clawforge)**: operaciones del stack, arquitectura, coordinación, modelo de máxima capacidad

La 3ª generación (Clawforge) actúa como **capa de gobernanza operacional** sobre el ecosistema completo — incluyendo operar, diagnosticar y mantener las generaciones anteriores.

---

## Sesiones inter-generacionales

En el `sessions.json` de Clawforge pueden aparecer sesiones con modelos `MiniMax-M2.7-highspeed` o `glm-5.1` — son artefactos de coordinación o derivaciones hacia agentes de 1ª y 2ª generación, no errores de configuración.

---

## Referencias

- Arquitectura Docker 2ª gen: `urn:ops:kb:arquitectura-stack-kora`
- Federación cross-gateway: `urn:ops:kb:federacion-kora-v2`
- Manual operativo Clawforge: `KNOWLEDGE/OMEGA/openclaw-manual-integral.md`

---
_manifest:
  urn: urn:agengai:kb:01-arquitectura-gateway
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '01'
- arquitectura
- gateway
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:01-arquitectura-gateway
---

# Capítulo 1 — Arquitectura del Gateway

> **Propósito:** Entender cómo funciona OpenClaw desde adentro — sus componentes, su protocolo, el ciclo de vida de un request, cómo se construye lo que el modelo "ve", y qué cuenta como contexto. Este conocimiento es prerequisito para toda decisión de diseño posterior.

- ---

## 1.1 Componentes del Sistema

- OpenClaw es un **gateway de agentes IA** que conecta modelos de lenguaje con superficies de mensajería (Telegram, WhatsApp, Discord, Slack, Signal, iMessage, etc.) y herramientas (shell, filesystem, browser, APIs).
- Todo corre como un **único proceso daemon** de larga vida.

### Diagrama Mental de Componentes

```
┌─────────────────────────────────────────────────────────────────┐
│ GATEWAY (daemon) │
│ │
│ ┌──────────────┐ ┌──────────────┐ ┌───────────────────────┐ │
│ │ Channel │ │ Agent │ │ Automation │ │
│ │ Connectors │ │ Runtime │ │ Engine │ │
│ │ │ │ (pi-mono) │ │ │ │
│ │ • Telegram │ │ │ │ • Cron scheduler │ │
│ │ • WhatsApp │ │ • Model │ │ • Heartbeat runner │ │
│ │ • Discord │ │ inference │ │ • Hook dispatcher │ │
│ │ • Slack │ │ • Tool exec │ │ • Webhook ingress │ │
│ │ • Signal │ │ • Session │ │ │ │
│ │ • iMessage │ │ mgmt │ │ │ │
│ │ • WebChat │ │ • Streaming │ │ │ │
│ └──────┬───────┘ └──────┬───────┘ └───────────┬───────────┘ │
│ │ │ │ │
│ ┌──────┴─────────────────┴───────────────────────┴───────────┐ │
│ │ Session Store (JSONL) │ │
│ │ ~/.openclaw/agents/<id>/sessions/ │ │
│ └────────────────────────────────────────────────────────────┘ │
│ │
│ ┌────────────────────────────────────────────────────────────┐ │
│ │ WebSocket API (port 18789 default) │ │
│ │ + HTTP: Control UI, Canvas host, Hooks │ │
│ └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
 ▲ ▲ ▲
 │ │ │
 ┌────┴────┐ ┌─────┴─────┐ ┌────┴────┐
 │ Clients │ │ Nodes │ │ External│
 │ (WS) │ │ (WS) │ │ Webhooks│
 │ │ │ │ │ (HTTP) │
 │ • CLI │ │ • macOS │ │ │
 │ • macOS │ │ • iOS │ │ • Gmail │
 │ app │ │ • Android │ │ • CI/CD │
 │ • WebUI │ │ • headless│ │ • custom│
 └─────────┘ └───────────┘ └─────────┘
```

### Los cuatro tipos de actor

| Actor | Qué es | Cómo conecta | Para qué |
|-------|--------|--------------|----------|
| **Gateway** | El daemon central. Único por host (o por profile). | Escucha en un puerto (default 18789) | Orquesta todo: canales, agent runtime, sessions, cron, hooks |
| **Clients** | Operadores humanos o UIs | WebSocket al gateway | Enviar mensajes, ver status, administrar. CLI (`openclaw`), macOS app, Control UI web |
| **Nodes** | Dispositivos remotos (Mac, iPhone, Android) | WebSocket con `role: node` | Exponen capacidades: cámara, pantalla, localización, ejecución remota, browser relay |
| **Channel Connectors** | Adaptadores de mensajería | Conexiones salientes (Telegram Bot API, WhatsApp Baileys, etc.) | Recibir y enviar mensajes en cada plataforma |

### Decisiones de diseño clave

1. **Un solo proceso, múltiples canales.** No hay un proceso por canal ni microservicios — todo corre en un Node.js. Esto simplifica el deployment pero significa que si el gateway cae, todo cae. Mitigación: systemd con restart automático.

2. **El gateway es el source of truth de state.** Sessions, auth profiles, cron jobs — todo vive en el gateway host. Los clients son stateless; consultan al gateway para cualquier dato.

3. **HTTP y WebSocket comparten puerto.** El mismo puerto sirve:
 - WebSocket API (protocol typed con JSON frames)
 - HTTP: Control UI (SPA), Canvas host (`/__openclaw__/canvas/`), webhook endpoints (`/hooks/*`)
 - Implicación de seguridad: si expones el puerto, expones todo.

4. **Binding loopback by default.** El gateway escucha solo en `127.0.0.1`. El acceso remoto se resuelve con Tailscale Serve/Funnel o SSH tunnel — nunca exponiendo el puerto directamente.

- ---

## 1.2 Wire Protocol

- El protocolo entre clients/nodes y el gateway es **WebSocket con frames JSON en texto plano**.

### Handshake obligatorio

- La primera frame **debe** ser un `connect`:

```json
{
 "type": "req",
 "id": "1",
 "method": "connect",
 "params": {
 "auth": { "token": "your-gateway-token" },
 "role": "client",
 "deviceId": "...",
 "caps": [...]
 }
}
```

- Si la primera frame no es `connect`, o la auth falla → socket cerrado inmediatamente.

### Tipos de frame

| Dirección | Tipo | Estructura | Ejemplo |
|-----------|------|-----------|---------|
| Client → Gateway | **Request** | `{type:"req", id, method, params}` | `{type:"req", id:"2", method:"agent", params:{message:"hola"}}` |
| Gateway → Client | **Response** | `{type:"res", id, ok, payload\|error}` | `{type:"res", id:"2", ok:true, payload:{runId:"...", status:"accepted"}}` |
| Gateway → Client | **Event** | `{type:"event", event, payload, seq?}` | `{type:"event", event:"agent", payload:{stream:"assistant", ...}}` |

### Autenticación

- Tres modos disponibles:

| Modo | Config | Cuándo usar |
|------|--------|-------------|
| `token` | `gateway.auth.mode: "token"` | Default recomendado. Token compartido en `connect.params.auth.token` |
| `password` | `gateway.auth.mode: "password"` | Alternativa al token |
| `trusted-proxy` | `gateway.auth.mode: "trusted-proxy"` | Detrás de un reverse proxy que ya autenticó |

- **Sin auth configurada = gateway rechaza conexiones** (fail-closed by default).

### Device Pairing

- Cada client/node incluye un `deviceId` en el connect.
- El gateway mantiene un registro de dispositivos aprobados:

- **Local** (loopback o dirección tailnet propia): auto-approved
- **Remoto**: requiere aprobación explícita (challenge-response con nonce)

- Esto significa que incluso con el token correcto, un dispositivo nuevo desde una IP remota necesita aprobación.

### Idempotency

- Los métodos con side effects (`send`, `agent`) requieren un idempotency key.
- El gateway mantiene un cache corto de dedup para permitir reintentos seguros.

### Implicación para arquitectura

- El protocolo es **deliberadamente simple**:
- JSON sobre WebSocket, sin gRPC, sin REST elaborado.
- Esto permite:

- Implementar clients en cualquier lenguaje (Swift para macOS app, JS para WebChat)
- Debugging trivial (inspeccionar frames con cualquier WebSocket tool)
- Pero también significa: no hay binary framing, no hay multiplexing avanzado, no hay backpressure formal

- ---

## 1.3 Agent Loop: El Ciclo Completo de un Request

- Cuando un mensaje llega (desde Telegram, WhatsApp, CLI, webhook, heartbeat, o cron), atraviesa este pipeline:

## Pipeline completo

```
INBOUND MESSAGE
 │
 ▼
┌─────────────────┐
│ 1. INTAKE │ Channel connector recibe el mensaje
│ & ROUTING │ → Determina agentId (via bindings)
│ │ → Determina sessionKey (via dmScope, grupo, etc.)
│ │ → Aplica DM policy / group policy / allowlists
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 2. QUEUE │ Serialización por sesión + lane global
│ & STEERING │ → Un solo run activo por sesión
│ │ → Mensajes entrantes durante run: steer/collect/followup
│ │ → Typing indicator inmediato
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 3. SESSION │ Adquirir write lock de sesión
│ PREPARATION │ → Cargar/crear sesión (SessionManager)
│ │ → Resolver modelo + auth profile
│ │ → Cargar skills snapshot
│ │ → Preparar sandbox (si aplica)
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 4. PROMPT │ Construir system prompt completo:
│ ASSEMBLY │ → Base prompt (tools, safety, skills list)
│ │ → Bootstrap files (AGENTS.md, SOUL.md, etc.)
│ │ → Runtime metadata (host, model, time)
│ │ → Conversation history (del JSONL)
│ │ → El mensaje actual del usuario
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 5. MODEL │ Enviar todo al provider de LLM
│ INFERENCE │ → Auth profile rotation si falla
│ │ → Model fallback si todos los profiles fallan
│ │ → Streaming de tokens (deltas)
│ │ → Timeout enforcement (default 600s)
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 6. TOOL │ Si el modelo pidió tool calls:
│ EXECUTION │ → Ejecutar cada tool (exec, read, browser, etc.)
│ │ → Emitir tool events al stream
│ │ → Sanitizar resultados (tamaño, imágenes)
│ │ → Volver a paso 5 con resultados
│ │ (loop hasta que el modelo no pida más tools)
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 7. REPLY │ Ensamblar payloads finales:
│ SHAPING │ → Filtrar NO_REPLY
│ │ → Dedup messaging tool sends
│ │ → Block streaming / chunking
│ │ → Reply tags para quote/reply nativo
└────────┬────────┘
 │
 ▼
┌─────────────────┐
│ 8. PERSISTENCE │ Guardar todo en disco:
│ & DELIVERY │ → Append al JSONL de sesión
│ │ → Actualizar sessions.json (metadata)
│ │ → Entregar respuesta al canal
│ │ → Emitir lifecycle end event
└─────────────────┘
```

## Conceptos clave del loop

### Serialización por sesión

- **Solo un run activo por sesión a la vez.** Esto es fundamental: evita race conditions en el historial de sesión, previene que dos respuestas se escriban simultáneamente al JSONL.

- Si llega un segundo mensaje mientras hay un run activo, el **queue mode** decide qué pasa:

| Queue Mode | Comportamiento |
|------------|---------------|
| `collect` (default) | Acumula mensajes; cuando el run actual termina, arranca otro turn con todos los mensajes acumulados |
| `steer` | Inyecta el mensaje en el run actual (cancela tool calls pendientes tras el próximo boundary) |
| `followup` | Encola para un turn separado después del run actual |
| `steer-backlog` | Steer + preserva para followup |

### Lane global de concurrencia

- Además de serializar por sesión, hay una **lane global** (`main`) con concurrencia configurable (`agents.defaults.maxConcurrent`, default 4).
- Esto limita cuántos agent runs pueden estar activos simultáneamente en todo el gateway.

- ¿Por qué?
- Rate limits de providers, uso de memoria, coherencia.
- Si tienes 50 grupos activos y todos mandan mensaje al mismo segundo, no quieres 50 inference calls simultáneos.

### El loop tool es iterativo

- El modelo puede pedir múltiples tool calls en una sola respuesta.
- OpenClaw las ejecuta todas, envía los resultados de vuelta al modelo, y el modelo decide si necesita más tools o si ya tiene la respuesta final.
- Esto puede iterar muchas veces (un agent "pensando" y actuando en ciclos).

- El timeout global (default 600s = 10 minutos) es el backstop: si el loop no termina en ese tiempo, se aborta.

### Abort points

- El loop puede terminar temprano por:

- **Timeout** del agente (600s default)
- **AbortSignal** (cancelación, e.g. `/stop`)
- **Desconexión** del gateway o timeout del RPC
- **Auto-compaction**: si el contexto excede la ventana, se compacta y se reintenta

- ---

## 1.4 Prompt Assembly y System Prompt

- El system prompt es **la pieza más importante de la arquitectura** desde la perspectiva de diseño.
- Es lo que define el comportamiento, las capacidades, y los límites del agente.
- OpenClaw lo construye dinámicamente en cada run.

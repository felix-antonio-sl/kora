---
_manifest:
  urn: urn:kora:kb:01-arquitectura-gateway
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
│                        GATEWAY (daemon)                         │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │  Channel      │  │  Agent       │  │  Automation           │ │
│  │  Connectors   │  │  Runtime     │  │  Engine               │ │
│  │              │  │  (pi-mono)   │  │                       │ │
│  │  • Telegram   │  │              │  │  • Cron scheduler     │ │
│  │  • WhatsApp   │  │  • Model     │  │  • Heartbeat runner   │ │
│  │  • Discord    │  │    inference │  │  • Hook dispatcher    │ │
│  │  • Slack      │  │  • Tool exec │  │  • Webhook ingress    │ │
│  │  • Signal     │  │  • Session   │  │                       │ │
│  │  • iMessage   │  │    mgmt     │  │                       │ │
│  │  • WebChat    │  │  • Streaming │  │                       │ │
│  └──────┬───────┘  └──────┬───────┘  └───────────┬───────────┘ │
│         │                 │                       │             │
│  ┌──────┴─────────────────┴───────────────────────┴───────────┐ │
│  │                   Session Store (JSONL)                     │ │
│  │              ~/.openclaw/agents/<id>/sessions/              │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │            WebSocket API (port 18789 default)              │ │
│  │          + HTTP: Control UI, Canvas host, Hooks            │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
         ▲              ▲                    ▲
         │              │                    │
    ┌────┴────┐   ┌─────┴─────┐        ┌────┴────┐
    │ Clients │   │   Nodes   │        │ External│
    │ (WS)    │   │   (WS)    │        │ Webhooks│
    │         │   │           │        │ (HTTP)  │
    │ • CLI   │   │ • macOS   │        │         │
    │ • macOS │   │ • iOS     │        │ • Gmail │
    │   app   │   │ • Android │        │ • CI/CD │
    │ • WebUI │   │ • headless│        │ • custom│
    └─────────┘   └───────────┘        └─────────┘
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


### Pipeline completo

```
INBOUND MESSAGE
      │
      ▼
┌─────────────────┐
│ 1. INTAKE       │  Channel connector recibe el mensaje
│    & ROUTING    │  → Determina agentId (via bindings)
│                 │  → Determina sessionKey (via dmScope, grupo, etc.)
│                 │  → Aplica DM policy / group policy / allowlists
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. QUEUE        │  Serialización por sesión + lane global
│    & STEERING   │  → Un solo run activo por sesión
│                 │  → Mensajes entrantes durante run: steer/collect/followup
│                 │  → Typing indicator inmediato
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. SESSION      │  Adquirir write lock de sesión
│    PREPARATION  │  → Cargar/crear sesión (SessionManager)
│                 │  → Resolver modelo + auth profile
│                 │  → Cargar skills snapshot
│                 │  → Preparar sandbox (si aplica)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. PROMPT       │  Construir system prompt completo:
│    ASSEMBLY     │  → Base prompt (tools, safety, skills list)
│                 │  → Bootstrap files (AGENTS.md, SOUL.md, etc.)
│                 │  → Runtime metadata (host, model, time)
│                 │  → Conversation history (del JSONL)
│                 │  → El mensaje actual del usuario
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. MODEL        │  Enviar todo al provider de LLM
│    INFERENCE    │  → Auth profile rotation si falla
│                 │  → Model fallback si todos los profiles fallan
│                 │  → Streaming de tokens (deltas)
│                 │  → Timeout enforcement (default 600s)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 6. TOOL         │  Si el modelo pidió tool calls:
│    EXECUTION    │  → Ejecutar cada tool (exec, read, browser, etc.)
│                 │  → Emitir tool events al stream
│                 │  → Sanitizar resultados (tamaño, imágenes)
│                 │  → Volver a paso 5 con resultados
│                 │  (loop hasta que el modelo no pida más tools)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 7. REPLY        │  Ensamblar payloads finales:
│    SHAPING      │  → Filtrar NO_REPLY
│                 │  → Dedup messaging tool sends
│                 │  → Block streaming / chunking
│                 │  → Reply tags para quote/reply nativo
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 8. PERSISTENCE  │  Guardar todo en disco:
│    & DELIVERY   │  → Append al JSONL de sesión
│                 │  → Actualizar sessions.json (metadata)
│                 │  → Entregar respuesta al canal
│                 │  → Emitir lifecycle end event
└─────────────────┘
```

### Conceptos clave del loop

#### Serialización por sesión

- **Solo un run activo por sesión a la vez.** Esto es fundamental: evita race conditions en el historial de sesión, previene que dos respuestas se escriban simultáneamente al JSONL.


- Si llega un segundo mensaje mientras hay un run activo, el **queue mode** decide qué pasa:


| Queue Mode | Comportamiento |
|------------|---------------|
| `collect` (default) | Acumula mensajes; cuando el run actual termina, arranca otro turn con todos los mensajes acumulados |
| `steer` | Inyecta el mensaje en el run actual (cancela tool calls pendientes tras el próximo boundary) |
| `followup` | Encola para un turn separado después del run actual |
| `steer-backlog` | Steer + preserva para followup |

#### Lane global de concurrencia

- Además de serializar por sesión, hay una **lane global** (`main`) con concurrencia configurable (`agents.defaults.maxConcurrent`, default 4).
- Esto limita cuántos agent runs pueden estar activos simultáneamente en todo el gateway.


- ¿Por qué?
- Rate limits de providers, uso de memoria, coherencia.
- Si tienes 50 grupos activos y todos mandan mensaje al mismo segundo, no quieres 50 inference calls simultáneos.


#### El loop tool es iterativo

- El modelo puede pedir múltiples tool calls en una sola respuesta.
- OpenClaw las ejecuta todas, envía los resultados de vuelta al modelo, y el modelo decide si necesita más tools o si ya tiene la respuesta final.
- Esto puede iterar muchas veces (un agent "pensando" y actuando en ciclos).


- El timeout global (default 600s = 10 minutos) es el backstop: si el loop no termina en ese tiempo, se aborta.


#### Abort points

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


### Estructura del System Prompt

- El prompt se ensambla en secciones fijas, en este orden:


```
┌───────────────────────────────────────────────┐
│              SYSTEM PROMPT                     │
│                                                │
│  1. TOOLING                                    │
│     Lista de tools disponibles + descripciones │
│     (+ JSON schemas enviados al modelo)        │
│                                                │
│  2. SAFETY                                     │
│     Guardrails: no self-replication,           │
│     no power-seeking, human oversight          │
│                                                │
│  3. SKILLS (si hay elegibles)                  │
│     Lista compacta: nombre + descripción       │
│     + ruta al SKILL.md (para read on-demand)   │
│                                                │
│  4. MEMORY RECALL                              │
│     Instrucción de usar memory_search/get      │
│     antes de responder sobre el pasado         │
│                                                │
│  5. MODEL ALIASES                              │
│     Tabla de alias → provider/model            │
│                                                │
│  6. WORKSPACE                                  │
│     Directorio de trabajo del agente           │
│                                                │
│  7. DOCUMENTATION                              │
│     Ruta a docs locales de OpenClaw            │
│                                                │
│  8. USER IDENTITY                              │
│     Owner numbers (para verificar sender)      │
│                                                │
│  9. CURRENT DATE & TIME                        │
│     Timezone (sin reloj dinámico)              │
│                                                │
│ 10. PROJECT CONTEXT (bootstrap files)          │
│     Contenido inyectado de:                    │
│     • AGENTS.md                                │
│     • SOUL.md                                  │
│     • TOOLS.md                                 │
│     • IDENTITY.md                              │
│     • USER.md                                  │
│     • HEARTBEAT.md                             │
│     • MEMORY.md                                │
│                                                │
│ 11. REPLY TAGS                                 │
│     Sintaxis para reply/quote nativo           │
│                                                │
│ 12. MESSAGING                                  │
│     Reglas de routing de mensajes              │
│                                                │
│ 13. SILENT REPLIES                             │
│     Contrato de NO_REPLY                       │
│                                                │
│ 14. HEARTBEATS                                 │
│     Prompt de heartbeat + reglas de ack        │
│                                                │
│ 15. RUNTIME                                    │
│     host, OS, node, model, thinking level      │
│                                                │
│ 16. INBOUND CONTEXT                            │
│     Metadata del mensaje actual (JSON)         │
│     chat_id, channel, chat_type, flags         │
└───────────────────────────────────────────────┘
```

### Bootstrap Files: el alma del agente

- Los bootstrap files son la **personalidad persistente** del agente.
- Se inyectan en cada turn, lo que significa que el modelo los "ve" siempre, sin necesidad de leerlos con herramientas:


| Archivo | Propósito | Tamaño típico |
|---------|-----------|---------------|
| `AGENTS.md` | Instrucciones operativas, reglas, convenciones | 2-5 KB |
| `SOUL.md` | Personalidad, tono, boundaries | 1-3 KB |
| `USER.md` | Perfil del usuario, preferencias, rutina | 2-4 KB |
| `IDENTITY.md` | Nombre, vibe, emoji del agente | 0.5-1 KB |
| `TOOLS.md` | Notas locales sobre herramientas y setup | 2-5 KB |
| `HEARTBEAT.md` | Checklist para heartbeats | 0.3-1 KB |
| `MEMORY.md` | Memoria curada de largo plazo | 5-20 KB |

- **Truncation:** Cada archivo se trunca individualmente a `bootstrapMaxChars` (default 20,000 chars).
- El total de todos los bootstrap files se limita a `bootstrapTotalMaxChars` (default 150,000 chars).


- **Sub-agentes:** Solo reciben `AGENTS.md` + `TOOLS.md` (los demás se filtran para mantener su contexto pequeño).


### Lo que NO se inyecta automáticamente

- **`memory/*.md`** (daily logs): requieren `memory_get` explícito. No cuentan contra la ventana de contexto a menos que el modelo los lea.
- **`SKILL.md`** de cada skill: solo se inyecta la lista (nombre + descripción + ruta). El modelo debe hacer `read` del archivo cuando necesita usarlo.

- Esta decisión es **crítica para el diseño**: mantiene el system prompt lean.
- Si tuvieras 12 skills con instrucciones de 3KB cada una, serían 36KB inyectados en cada turn — un desperdicio enorme.


### Prompt Modes

| Modo | Contexto | Usado por |
|------|----------|-----------|
| `full` | Todo lo de arriba | Sesiones normales (main, DM, grupos) |
| `minimal` | Solo tooling, safety, workspace, sandbox, runtime. Sin skills, memory recall, aliases, user identity, reply tags, messaging, heartbeats | Sub-agentes |
| `none` | Solo línea base de identidad | (Reservado) |

### Implicación de diseño

- **Cada carácter en un bootstrap file se paga en cada turn.** Si tu `MEMORY.md` crece a 20KB, esos ~5,000 tokens se consumen en cada interacción.
- Esto lleva a compaction más frecuente y mayor costo.


- **Regla de oro:** Bootstrap files = información que el agente necesita en TODA interacción.
- Si es contextual o histórico, va en `memory/*.md` (acceso on-demand via tools).


- ---


## 1.5 Context Window: Qué Cuenta y Cómo Inspeccionarlo

- La **context window** es el límite duro del modelo: la cantidad máxima de tokens que puede "ver" simultáneamente.
- Todo lo que OpenClaw envía al modelo cuenta contra esta ventana.


### Qué consume contexto

```
Context Window (ejemplo: 200K tokens para Claude Sonnet)
├── System Prompt (~8-12K tokens típico)
│   ├── Secciones fijas (~2-3K)
│   ├── Tool schemas JSON (~5-8K)       ← invisible pero costoso
│   ├── Skills list (~0.5-1K)
│   └── Bootstrap files (~3-6K)
│       ├── AGENTS.md
│       ├── SOUL.md
│       ├── MEMORY.md                    ← puede crecer mucho
│       └── ... (rest)
│
├── Conversation History (crece con cada turn)
│   ├── User messages
│   ├── Assistant messages
│   ├── Tool calls (request)
│   └── Tool results (response)          ← el mayor consumidor
│
└── Overhead del provider (headers, wrappers, etc.)
```

### Los consumidores ocultos

- **Tool schemas:** Aunque no los ves como texto en el prompt, el modelo los recibe como JSON para saber cómo llamar cada tool.
- El tool `browser` solo puede consumir ~2,500 tokens en schema.
- Si tienes 15 tools activos, los schemas pueden sumar 8,000+ tokens.


- **Tool results:** Un `exec` que devuelve 500 líneas de output, o un `read` de un archivo largo, consume proporcionalmente.
- OpenClaw trunca resultados grandes, pero la acumulación en una sesión larga es el principal driver de compaction.


- **Imágenes/attachments:** Las imágenes se envían como attachments al modelo y consumen tokens significativos (una imagen puede costar 1,000-5,000 tokens dependiendo del tamaño).


### Mecanismos de gestión

- OpenClaw tiene tres mecanismos para mantener la ventana de contexto bajo control:


#### 1. Session Pruning (in-memory, no destructivo)

- **Qué hace:** Antes de cada llamada al modelo, recorta `toolResult` messages viejos del contexto in-memory.
- NO modifica el JSONL en disco.


- **Cuándo:** Solo para Anthropic.
- Se activa cuando la última llamada es más vieja que el TTL (default 5 minutos).
- Alineado con prompt caching de Anthropic.


- **Qué NO toca:** Mensajes de usuario, mensajes del asistente, resultados de tools con imágenes, los últimos N mensajes del asistente.


#### 2. Compaction (persistente)

- **Qué hace:** Cuando la sesión se acerca al límite de la ventana, el modelo genera un resumen de la conversación antigua.
- El resumen se persiste en el JSONL y reemplaza los mensajes originales para el contexto futuro.


- **Flujo:**

1. Detección de proximidad al límite (via `reserveTokensFloor`)
2. **Memory flush** (opcional): turn silencioso para que el modelo escriba notas durables a disco antes de perder acceso al contexto
3. Compaction: el modelo resume la conversación antigua
4. Retry del request original con el contexto compactado

- **Manual:** `/compact [instrucciones]` fuerza una compaction con instrucciones opcionales.


#### 3. Reset (`/new`, `/reset`)

- Nuclear: descarta toda la sesión y empieza fresh.
- Hooks como `session-memory` pueden salvar contexto antes del reset.


### Inspeccionar tu contexto

- OpenClaw ofrece dos comandos de chat para entender qué está pasando:


#### `/context list` — Vista rápida

- Muestra:

- Tamaño del system prompt (chars y tokens estimados)
- Cada bootstrap file: estado (OK/TRUNCATED/MISSING), tamaño raw vs inyectado
- Skills list: tamaño total
- Tool list: tamaño texto + tamaño schemas JSON (esto es clave — los schemas son invisibles pero costosos)
- Tokens de sesión (cached)

```
🧠 Context breakdown
System prompt (run): 38,412 chars (~9,603 tok)
  Project Context: 23,901 chars (~5,976 tok)

Injected workspace files:
- AGENTS.md:    OK        | raw 1,742 → injected 1,742 (~436 tok)
- TOOLS.md:     TRUNCATED | raw 54,210 → injected 20,962 (~5,241 tok)
- MEMORY.md:    OK        | raw 12,800 → injected 12,800 (~3,200 tok)

Tool schemas (JSON): 31,988 chars (~7,997 tok)
Session tokens: 14,250 / ctx=200,000
```

#### `/context detail` — Breakdown por componente

- Agrega:

- Top skills por tamaño de entry en el prompt
- Top tools por tamaño de schema (identifica qué tools dominan el costo)

#### `/status` — Estado de sesión

- Muestra tokens usados vs disponibles, compactions realizadas, modelo actual, thinking/verbose state.


### Decisiones de arquitectura que impactan el contexto

| Decisión | Impacto en contexto | Recomendación |
|----------|---------------------|---------------|
| Tamaño de MEMORY.md | Se inyecta completo cada turn | Mantener <10KB; mover detalles a daily logs |
| Cantidad de skills activos | Cada entry ~100-400 chars en prompt | Solo habilitar los que se usan |
| Cantidad de tools | Cada schema ~500-2500 tokens | Usar tool profiles para restringir |
| Frecuencia de tool calls | Cada result se acumula en historial | Sesiones tool-heavy se compactan más rápido |
| Modelo elegido | Ventana varía: 128K-1M tokens | Modelos con ventana grande toleran más acumulación |
| bootstrapMaxChars | Trunca archivos grandes | Bajar si tus bootstrap files son excesivos |

### Regla práctica

> **Si tu `/context list` muestra que el system prompt consume más del 15-20% de tu ventana de contexto, algo está mal.** Típicamente debería estar entre 5-10%.

- Los principales sospechosos son siempre:
- MEMORY.md inflado, TOOLS.md largo, demasiados tool schemas, o skills innecesarios.


- ---


## Resumen del Capítulo

| Concepto | Implicación para diseño |
|----------|------------------------|
| **Gateway = proceso único** | Single point of failure; mitigado con systemd restart. Simplifica deployment pero requiere estabilidad. |
| **Binding loopback default** | Seguridad by default. Acceso remoto siempre via tunnel (Tailscale/SSH). |
| **Protocol = JSON/WS simple** | Fácil de debuggear e implementar clients. Sin overhead de serialización binaria. |
| **Serialización por sesión** | Garantiza consistencia pero limita throughput a 1 run por sesión. Queue modes compensan. |
| **Lane global de concurrencia** | Protege contra rate limits y saturación. Ajustar `maxConcurrent` según tu provider plan. |
| **System prompt dinámico** | Cada bootstrap file se paga en cada turn. Mantenerlos lean es crítico. |
| **Tool schemas invisibles** | Cuestan tokens sin que los veas. `/context detail` los expone. |
| **Tres niveles de gestión de contexto** | Pruning (automatic, non-destructive) → Compaction (persistent summary) → Reset (nuclear). |
| **MEMORY.md vs memory/*.md** | Inyectado vs on-demand. Esta distinción es la clave de la arquitectura de memoria. |
| **Prompt mode minimal para sub-agentes** | Reduce overhead; sub-agentes son lean by design. |

- ---


- *Siguiente: [Capítulo 2 — El Agente como Unidad Fundamental](02-agente-unidad-fundamental.md)*


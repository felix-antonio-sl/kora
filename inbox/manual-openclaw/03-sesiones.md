---
_manifest:
  urn: urn:kora:kb:03-sesiones
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '03'
- sesiones
lang: es
---

# Capítulo 3 — Sesiones

> **Propósito:** Entender cómo OpenClaw organiza las conversaciones en sesiones, cómo las identifica, cuándo las resetea, cómo persiste su estado, y los mecanismos de gestión de contexto (compaction, pruning). Las sesiones son el concepto que conecta agentes con canales, y dominar su lógica es prerequisito para multi-agente, automatización y seguridad.

- ---


## 3.1 Session Keys: El Sistema de Direcciones

- Cada conversación en OpenClaw tiene un **session key** — un identificador estable que determina dónde se almacena el historial, qué contexto ve el modelo, y cómo se aísla de otras conversaciones.


### Anatomía de un session key

```
agent:<agentId>:<rest>
  │       │        │
  │       │        └── Identificador de la conversación
  │       └────────── Agente que maneja esta sesión
  └────────────────── Prefijo fijo
```

### Cómo se construye el key según el origen

| Origen | Session Key | Ejemplo |
|--------|------------|---------|
| **DM (dmScope=main)** | `agent:<id>:<mainKey>` | `agent:main:main` |
| **DM (per-peer)** | `agent:<id>:dm:<peerId>` | `agent:main:dm:7192195698` |
| **DM (per-channel-peer)** | `agent:<id>:<channel>:dm:<peerId>` | `agent:main:telegram:dm:7192195698` |
| **DM (per-account-channel-peer)** | `agent:<id>:<channel>:<accountId>:dm:<peerId>` | `agent:main:telegram:bot1:dm:7192195698` |
| **Grupo WhatsApp** | `agent:<id>:whatsapp:group:<groupId>` | `agent:main:whatsapp:group:120363...@g.us` |
| **Grupo Telegram** | `agent:<id>:telegram:group:<chatId>` | `agent:main:telegram:group:-1001234567890` |
| **Topic Telegram** | `agent:<id>:telegram:group:<chatId>:topic:<threadId>` | `agent:main:telegram:group:-100...:topic:42` |
| **Canal Discord** | `agent:<id>:discord:channel:<channelId>` | `agent:main:discord:channel:1234567890` |
| **Thread Discord/Slack** | Similar, con `:thread:<id>` | — |
| **Cron job** | `cron:<jobId>` | `cron:morning-brief` |
| **Webhook** | `hook:<uuid>` | `hook:abc123` |
| **Sub-agente** | `agent:<id>:subagent:<uuid>` | `agent:main:subagent:f8a2...` |

### Implicaciones de diseño

- **1.
- El key determina el aislamiento.** Dos mensajes con el mismo session key comparten historial.
- Dos mensajes con keys distintos NO se ven entre sí.
- Esto es la base de toda la seguridad de contexto.


- **2.
- Los DMs son el caso más sutil.** Con `dmScope: "main"`, todos los DMs (desde cualquier canal, cualquier número) llegan a la misma sesión.
- Esto da continuidad pero puede filtrar contexto si múltiples personas pueden enviar DMs.


- **3.
- Grupos siempre tienen su propio key.** No hay opción de "colapsar" grupos a la sesión main.
- Esto es un invariante de seguridad.


- **4.
- Cron y webhooks siempre son aislados.** Cada cron job y cada webhook run tienen su propia sesión.
- Los cron jobs aislados crean un sessionId fresh en cada ejecución (sin carry-over de historial).


- **5.
- Session key ≠ session ID.** El key es estable (e.g., `agent:main:main` siempre existe).
- El ID es un UUID que cambia con cada `/new` o `/reset`.
- Mismo key, nuevo ID = nueva conversación dentro del mismo "canal lógico".


- ---


## 3.2 DM Scope: La Decisión de Aislamiento más Importante

- La configuración `session.dmScope` determina cómo se agrupan los mensajes directos.
- Es **la primera decisión de seguridad** al configurar un agente que recibe DMs de más de una persona.


### Los cuatro modos

```
┌──────────────────────────────────────────────────────────────────┐
│                     dmScope: "main" (default)                    │
│                                                                  │
│  Korvo (Telegram) ──────┐                                        │
│  Korvo (WhatsApp) ──────┤──► agent:main:main ──► UNA sesión      │
│  Ariel (Telegram) ──────┘       (todo junto)                     │
│                                                                  │
│  ⚠ Ariel ve contexto de Korvo (y viceversa)                     │
│  ✓ Máxima continuidad para usuario único                         │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                     dmScope: "per-peer"                           │
│                                                                  │
│  Korvo (Telegram) ──────┐──► agent:main:dm:korvo ──► sesión Korvo│
│  Korvo (WhatsApp) ──────┘                                        │
│  Ariel (Telegram) ─────────► agent:main:dm:ariel ──► sesión Ariel│
│                                                                  │
│  ✓ Aislamiento por persona                                       │
│  ✓ Cross-channel: misma sesión si es la misma persona            │
│  ⚠ Requiere identity resolution cross-channel                   │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│               dmScope: "per-channel-peer" (recomendado)          │
│                                                                  │
│  Korvo (Telegram) ──► agent:main:telegram:dm:korvo               │
│  Korvo (WhatsApp) ──► agent:main:whatsapp:dm:korvo               │
│  Ariel (Telegram) ──► agent:main:telegram:dm:ariel               │
│                                                                  │
│  ✓ Aislamiento por persona + canal                               │
│  ✓ Sin ambigüedad de identidad                                   │
│  ⚠ Korvo tiene sesiones separadas por canal                     │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│           dmScope: "per-account-channel-peer"                    │
│                                                                  │
│  Bot1 Telegram: Korvo ──► agent:main:telegram:bot1:dm:korvo      │
│  Bot2 Telegram: Korvo ──► agent:main:telegram:bot2:dm:korvo      │
│                                                                  │
│  ✓ Para multi-cuenta en un mismo canal                           │
└──────────────────────────────────────────────────────────────────┘
```

### Matriz de decisión

| Situación | dmScope recomendado |
|-----------|-------------------|
| Solo tú usas el agente | `main` (default, máxima continuidad) |
| Tú + familiares/amigos | `per-channel-peer` |
| Bot público (pairing abierto) | `per-channel-peer` |
| Múltiples bots Telegram | `per-account-channel-peer` |
| Misma persona en múltiples canales, quieres unificar | `per-peer` + `identityLinks` |

### Identity Links: Unificar identidades cross-channel

- Si usas `per-peer` o `per-channel-peer` y quieres que Korvo-en-Telegram y Korvo-en-WhatsApp compartan sesión:


```json5
{
  session: {
    dmScope: "per-channel-peer",
    identityLinks: {
      korvo: ["telegram:7192195698", "whatsapp:+56912345678"],
      ariel: ["telegram:1234567890", "whatsapp:+56987654321"]
    }
  }
}
```

- Con esto, ambos identificadores de Korvo resuelven al canonical key `korvo`, y comparten sesión aunque vengan de canales distintos.


- ---


## 3.3 Ciclo de Vida de una Sesión

### Creación

- Una sesión se crea **lazily** cuando llega el primer mensaje para un session key que no existe.
- No hay "pre-creación" de sesiones.


### Reset: cuándo se reinicia una sesión

- OpenClaw evalúa si una sesión está "stale" **en cada mensaje inbound**.
- Si la sesión expiró, se genera un nuevo sessionId (el session key se mantiene).


#### Reset diario (default)

```
Hora de reset: 04:00 AM (hora local del gateway host)

Timeline:
  03:59  → Mensaje llega → sesión existente se reutiliza
  04:01  → Mensaje llega → sesión expirada → nuevo sessionId
```

- El agente "amanece" cada día con una sesión fresh.
- Pero los bootstrap files y la memoria en disco persisten — solo se pierde el contexto conversacional.


#### Reset por inactividad (idle)

```json5
{ session: { reset: { mode: "daily", atHour: 4, idleMinutes: 120 } } }
```

- Si han pasado 120 minutos sin actividad **Y** ya pasó la hora de reset diario → la sesión se resetea. **Whichever expires first wins.**


#### Overrides por tipo y canal

```json5
{
  session: {
    reset: { mode: "daily", atHour: 4 },
    resetByType: {
      direct: { mode: "idle", idleMinutes: 240 },     // DMs: 4h de idle
      group:  { mode: "idle", idleMinutes: 120 },      // Grupos: 2h
      thread: { mode: "daily", atHour: 4 }             // Threads: diario
    },
    resetByChannel: {
      discord: { mode: "idle", idleMinutes: 10080 }    // Discord: 1 semana
    }
  }
}
```

- **Precedencia:** `resetByChannel` > `resetByType` > `reset` (global).


- Esto permite políticas diferentes:
- Discord puede mantener sesiones largas (threads son persistentes), mientras que WhatsApp resetea diariamente.


#### Reset manual

| Comando | Efecto |
|---------|--------|
| `/new` | Nuevo sessionId. Opcional: `/new opus` para cambiar modelo. |
| `/reset` | Igual que `/new`. |
| Borrar entry de sessions.json | Recreación automática en próximo mensaje. |
| Borrar archivo JSONL | Sesión pierde historial; se recrea. |

### Casos especiales

- **Cron jobs aislados:** Siempre crean un sessionId fresh por ejecución. Sin carry-over.
- **Sub-agentes:** Sesión efímera (`agent:<id>:subagent:<uuid>`). Se archivan o borran según `cleanup` config.
- **Webhooks:** Session key configurable; por default `hook:<uuid>` es fresh cada vez.

- ---


## 3.4 Persistencia: Dónde Vive Todo

### Dos archivos por agente

```
~/.openclaw/agents/<agentId>/sessions/
├── sessions.json              ← Metadata de TODAS las sesiones
│                                 (map: sessionKey → {sessionId, updatedAt, ...})
│
├── <sessionId-1>.jsonl        ← Transcript de sesión 1
├── <sessionId-2>.jsonl        ← Transcript de sesión 2
├── <sessionId-3>.jsonl        ← Transcript de sesión 3
└── ...
```

### sessions.json: el índice

```json
{
  "agent:main:main": {
    "sessionId": "a1b2c3d4-...",
    "updatedAt": 1708444800000,
    "inputTokens": 15420,
    "outputTokens": 8230,
    "totalTokens": 23650,
    "contextTokens": 45000,
    "compactions": 2,
    "model": "anthropic/claude-sonnet-4-6",
    "origin": {
      "label": "Korvo (Telegram)",
      "provider": "telegram",
      "from": "7192195698"
    }
  },
  "agent:main:telegram:group:-1001234567890": {
    "sessionId": "e5f6g7h8-...",
    "updatedAt": 1708440000000,
    "displayName": "Equipo GORE",
    "channel": "telegram",
    "subject": "Grupo de trabajo"
  }
}
```

- Puntos clave:

- **Es seguro borrar entries.** Se recrean en el próximo mensaje.
- **Token counts vienen de aquí.** Los UIs (CLI, macOS app, WebChat) consultan este archivo, no parsean JSONLs.
- **`compactions` es un counter.** Indica cuántas veces se ha compactado la sesión. Útil para diagnosticar sesiones que compactan mucho (MEMORY.md muy grande, tool calls excesivos).

### Transcripts JSONL: la conversación completa

- Cada línea del JSONL es un mensaje (user, assistant, tool_call, tool_result, system, compaction_summary):


```jsonl
{"role":"system","content":"[system prompt...]","timestamp":1708444800000}
{"role":"user","content":"hola, qué tal","timestamp":1708444801000}
{"role":"assistant","content":"¡Hola! Todo bien...","timestamp":1708444805000}
{"role":"assistant","tool_calls":[{"name":"exec","args":{"command":"date"}}]}
{"role":"tool","tool_call_id":"tc_1","content":"Thu Feb 20 17:00:00 UTC 2026"}
```

- Puntos clave:

- **Append-only durante la sesión.** Nunca se editan líneas existentes (excepto compaction, que reescribe).
- **Pruning NO toca este archivo.** Pruning solo afecta lo que se envía al modelo in-memory.
- **Compaction SÍ reescribe.** El summary reemplaza mensajes antiguos en el JSONL.
- **Legible con `jq`.** `cat session.jsonl | jq -r '.content' | head` para ver rápido.
- **Topics de Telegram:** Usan nombre especial `<sessionId>-topic-<threadId>.jsonl`.

### Implicaciones operativas

| Escenario | Qué hacer |
|-----------|-----------|
| Sesión corrupta | Borrar el JSONL; se recrea en el próximo mensaje |
| Demasiadas sesiones ocupando disco | `openclaw sessions --active 1440` para ver activas en las últimas 24h; borrar las viejas |
| Quieres auditar qué dijo el agente | Leer el JSONL directamente o usar `sessions_history` |
| Backup | Incluir `~/.openclaw/agents/*/sessions/` en tu backup strategy |

- ---


## 3.5 Compaction: Cómo el Agente Sobrevive Conversaciones Largas

- La compaction es el mecanismo que permite sesiones indefinidamente largas dentro de una ventana de contexto finita.


### El problema

```
Turn 1:   System prompt (10K tokens) + User msg (100 tokens)
Turn 10:  System prompt + 10 user msgs + 10 assistant msgs + tool results
Turn 50:  System prompt + 50 exchanges + hundreds of tool results
          → Contexto: 180K / 200K tokens  ← ¡peligro!
Turn 51:  → NO CABE. ¿Qué hacer?
```

### La solución: resumir lo viejo

```
ANTES de compaction:
┌────────────────────────────────────────────────────┐
│ System Prompt (10K)                                 │
│ Turn 1: user + assistant + tools (3K)               │
│ Turn 2: user + assistant + tools (5K)               │
│ ...                                                 │
│ Turn 45: user + assistant + tools (4K)              │
│ Turn 46-50: mensajes recientes (20K)                │
│                                              ≈180K │
└────────────────────────────────────────────────────┘

DESPUÉS de compaction:
┌────────────────────────────────────────────────────┐
│ System Prompt (10K)                                 │
│ [Compaction Summary] (2K)                           │
│   "En esta sesión discutimos X, decidimos Y,        │
│    el usuario pidió Z, los resultados fueron..."    │
│ Turn 46-50: mensajes recientes (20K)                │
│                                              ≈32K  │
└────────────────────────────────────────────────────┘
```

### Flujo detallado

```
Contexto se acerca al límite
      │
      ▼
¿Memory flush habilitado?
├── SÍ → Turn silencioso:
│        "Session nearing compaction. Store durable memories now."
│        → El modelo escribe a memory/YYYY-MM-DD.md
│        → Responde NO_REPLY (invisible para el usuario)
│
└── Continúa
      │
      ▼
Compaction run:
  → El modelo resume turns 1-45 en un summary
  → Summary se persiste en el JSONL
  → Mensajes originales (1-45) se eliminan del JSONL
  → Counter `compactions` se incrementa en sessions.json
      │
      ▼
Retry del request original
  → Ahora el contexto cabe (summary + recientes)
  → El usuario no nota nada
```

### Qué se pierde en compaction

- La compaction es un **resumen**, no una copia.
- Se pierden:


- **Detalles finos** de tool outputs (el resumen dice "ejecutó un comando que mostró X" pero no incluye las 500 líneas de output)
- **Nuances conversacionales** (bromas, tangentes, tonos sutiles)
- **Datos exactos** (IPs, hashes, paths completos) a menos que el modelo los considere importantes

- **Por eso el memory flush es crítico:** antes de perder acceso al contexto completo, el agente tiene una oportunidad de escribir lo importante a disco.
- Lo que está en `memory/*.md` sobrevive a cualquier compaction.


### Compaction manual

```
/compact                              ← compacta con criterio del modelo
/compact Focus on decisions only      ← instrucciones para el resumen
/compact Keep all code snippets       ← preservar código
```

### Configuración

```json5
{
  agents: {
    defaults: {
      compaction: {
        reserveTokensFloor: 20000,       // margen antes de auto-compaction
        memoryFlush: {
          enabled: true,                  // turn silencioso pre-compaction
          softThresholdTokens: 4000,      // trigger threshold
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply NO_REPLY."
        }
      }
    }
  }
}
```

### Anti-patrón: compaction loops

- Si tu system prompt + bootstrap files consumen 50K tokens en un modelo con 128K de ventana, la sesión se compacta constantemente porque queda poco espacio para historial.
- Síntomas:


- `compactions` crece rápido en sessions.json
- El agente "olvida" cosas que le dijiste hace 5 minutos
- Cada respuesta es más lenta (overhead de compaction)

- **Solución:** Reducir bootstrap files, cambiar a un modelo con ventana más grande, o usar menos tools (schemas más pequeños).


- ---


## 3.6 Session Pruning: Limpieza In-Memory

- Pruning es diferente de compaction: no es un resumen narrativo sino una **poda técnica** de tool results viejos.


### Compaction vs Pruning

| | Compaction | Pruning |
|--|-----------|---------|
| **Qué hace** | Resume conversación antigua | Recorta tool results viejos |
| **Persiste** | Sí (reescribe JSONL) | No (solo in-memory, por request) |
| **Afecta** | Todo (user, assistant, tools) | Solo `toolResult` messages |
| **Cuándo** | Cerca del límite de contexto | Cada request (si TTL expiró) |
| **Quién** | El modelo genera el resumen | El gateway recorta mecánicamente |
| **Provider** | Todos | Solo Anthropic (alineado con prompt caching) |

### Cómo funciona (mode: cache-ttl)

```
Último llamado Anthropic: hace 6 minutos
TTL configurado: 5 minutos
      │
      ▼
TTL expirado → activar pruning
      │
      ▼
Recorrer tool results del historial (excepto últimos N assistants):
  │
  ├── Tool result > 50K chars → SOFT TRIM
  │   Mantener head (1500 chars) + tail (1500 chars)
  │   Insertar "..." en medio
  │   Agregar nota con tamaño original
  │
  └── Tool result en zona de hard-clear → HARD CLEAR
      Reemplazar todo con "[Old tool result content cleared]"
      │
      ▼
Enviar contexto podado al modelo
(JSONL en disco no se modifica)
```

### ¿Por qué alinearlo con prompt caching?

- Anthropic cachea el prompt por un TTL (default ~5 min).
- Mientras el cache es válido, no pagas cache-write.
- Cuando expira, la próxima request re-cachea todo.


- Si podas los tool results antes de ese re-cache, el cache-write es más pequeño → **más barato**.
- Si no podas, re-cacheas 200K tokens de tool results que ya no importan.


### Qué nunca se poda

- Mensajes de usuario
- Mensajes del asistente
- Tool results con imágenes (podrían ser referenciados)
- Los últimos `keepLastAssistants` (default 3) bloques de asistente + sus tool results

- ---


## 3.7 Send Policy: Control de Delivery

- La send policy permite bloquear el envío de mensajes a ciertos tipos de sesión sin listar IDs individuales.


### Casos de uso

| Necesidad | Regla |
|-----------|-------|
| No enviar a grupos de Discord | `{ action: "deny", match: { channel: "discord", chatType: "group" } }` |
| No enviar desde cron jobs | `{ action: "deny", match: { keyPrefix: "cron:" } }` |
| Solo enviar a sesiones main | `{ default: "deny", rules: [{ action: "allow", match: { chatType: "direct" } }] }` |
| Bloquear un agente específico en Discord | `{ action: "deny", match: { rawKeyPrefix: "agent:main:discord:" } }` |

### Configuración

```json5
{
  session: {
    sendPolicy: {
      default: "allow",   // o "deny" para whitelist approach
      rules: [
        { action: "deny", match: { channel: "discord", chatType: "group" } },
        { action: "deny", match: { keyPrefix: "cron:" } },
        // rawKeyPrefix incluye el prefijo agent:<id>:
        { action: "deny", match: { rawKeyPrefix: "agent:public:discord:" } }
      ]
    }
  }
}
```

### Override por sesión

- El owner puede override la policy por sesión con comandos de chat:


```
/send on        ← permitir en esta sesión (override)
/send off       ← denegar en esta sesión (override)
/send inherit   ← limpiar override, volver a reglas de config
```

### keyPrefix vs rawKeyPrefix

- `keyPrefix` matchea el key **normalizado** (sin `agent:<id>:`). Ejemplo: `discord:channel:` matchea `agent:main:discord:channel:123`.
- `rawKeyPrefix` matchea el key **completo**. Ejemplo: `agent:main:discord:` solo matchea el agente `main` en Discord, no el agente `work`.

- ---


## 3.8 Inspección y Debugging de Sesiones

### Comandos de chat

| Comando | Qué muestra |
|---------|-------------|
| `/status` | Tokens usados/disponibles, modelo, compactions, thinking/verbose state |
| `/context list` | System prompt breakdown, bootstrap files, tool schemas |
| `/context detail` | Top skills y tools por costo |
| `/compact` | Fuerza compaction (con instrucciones opcionales) |
| `/new` | Reset de sesión (nuevo sessionId) |
| `/stop` | Aborta run actual + sub-agentes |

### CLI

```bash
# Listar sesiones activas
openclaw sessions --json
openclaw sessions --active 60    # activas en la última hora

# Ver status general
openclaw status

# Inspeccionar sandbox + tools
openclaw sandbox explain --session agent:main:main

# Llamada directa al gateway
openclaw gateway call sessions.list --params '{}'
```

### Herramientas del agente

| Tool | Uso |
|------|-----|
| `sessions_list` | Listar sesiones (con filtros) |
| `sessions_history` | Ver historial de otra sesión |
| `sessions_send` | Enviar mensaje a otra sesión |
| `session_status` | Ver status de la sesión actual |

- ---


## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Session key = dirección estable** | Aislamiento determinístico. El key define quién ve qué. |
| **dmScope** | La decisión más importante de seguridad para DMs multi-usuario. Default `main` es para usuario único. |
| **Identity links** | Unificar una persona cross-channel sin perder aislamiento de otros |
| **Reset diario a las 4 AM** | Sesiones fresh cada día; memoria en disco persiste |
| **resetByType / resetByChannel** | Políticas diferenciadas: Discord = semanas, WhatsApp = diario |
| **sessions.json = índice borrable** | Se recrea automáticamente. Safe to clean up. |
| **JSONL = append-only** | Auditable, legible con jq, recoverable |
| **Compaction = resumen persistente** | Sesiones largas sin romper ventana de contexto |
| **Memory flush pre-compaction** | Seguro contra pérdida de datos: escribir a disco antes de resumir |
| **Pruning = poda in-memory** | Optimización de costos (prompt cache), no destructiva |
| **Send policy** | Control granular de delivery sin listar IDs |
| **Session key ≠ session ID** | Key es estable (canal lógico), ID cambia con cada reset |

### Diagrama de relaciones

```
                     ┌────────────────────┐
                     │   openclaw.json     │
                     │                    │
                     │  session.dmScope   │──── determina ────┐
                     │  session.reset     │                   │
                     │  session.sendPolicy│                   │
                     └────────┬───────────┘                   │
                              │                               │
                              ▼                               ▼
┌──────────┐         ┌───────────────┐              ┌────────────────┐
│ Inbound  │────────►│  Session Key  │─────────────►│  sessions.json │
│ Message  │         │  Resolution   │              │  (metadata)    │
└──────────┘         └───────┬───────┘              └────────────────┘
                             │
                             ▼
                     ┌───────────────┐
                     │  Session ID   │─────────────►  <sessionId>.jsonl
                     │  (UUID)       │                (transcript)
                     └───────┬───────┘
                             │
                    ┌────────┼────────┐
                    │        │        │
                    ▼        ▼        ▼
               Normal    Compaction  Pruning
               turns     (persist)  (in-memory)
```

- ---


- *Siguiente: [Capítulo 4 — Modelos y Failover](04-modelos-failover.md)*


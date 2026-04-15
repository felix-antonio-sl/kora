---
_manifest:
  urn: urn:agengai:kb:03-sesiones
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '03'
- sesiones
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:03-sesiones
---

# Capítulo 3 — Sesiones

> **Propósito:** Entender cómo OpenClaw organiza las conversaciones en sesiones, cómo las identifica, cuándo las resetea, cómo persiste su estado, y los mecanismos de gestión de contexto (compaction, pruning). Las sesiones son el concepto que conecta agentes con canales, y dominar su lógica es prerequisito para multi-agente, automatización y seguridad.

- ---

## 3.1 Session Keys: El Sistema de Direcciones

- Cada conversación en OpenClaw tiene un **session key** — un identificador estable que determina dónde se almacena el historial, qué contexto ve el modelo, y cómo se aísla de otras conversaciones.

### Anatomía de un session key

```
agent:<agentId>:<rest>
 │ │ │
 │ │ └── Identificador de la conversación
 │ └────────── Agente que maneja esta sesión
 └────────────────── Prefijo fijo
```

### Cómo se construye el key según el origen

| Origen | Session Key | Ejemplo |
|--------|------------|---------|
| **DM (dmScope=main)** | `agent:<id>:<mainKey>` | `agent:main:main` |
| **DM (per-peer)** | `agent:<id>:direct:<peerId>` | `agent:main:direct:7192195698` |
| **DM (per-channel-peer)** | `agent:<id>:<channel>:direct:<peerId>` | `agent:main:telegram:direct:7192195698` |
| **DM (per-account-channel-peer)** | `agent:<id>:<channel>:<accountId>:direct:<peerId>` | `agent:main:telegram:bot1:direct:7192195698` |
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
│ dmScope: "main" (default) │
│ │
│ Korvo (Telegram) ──────┐ │
│ Korvo (WhatsApp) ──────┤──► agent:main:main ──► UNA sesión │
│ Ariel (Telegram) ──────┘ (todo junto) │
│ │
│ ⚠ Ariel ve contexto de Korvo (y viceversa) │
│ ✓ Máxima continuidad para usuario único │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ dmScope: "per-peer" │
│ │
│ Korvo (Telegram) ──────┐──► agent:main:direct:korvo ──► sesión Korvo│
│ Korvo (WhatsApp) ──────┘ │
│ Ariel (Telegram) ─────────► agent:main:direct:ariel ──► sesión Ariel│
│ │
│ ✓ Aislamiento por persona │
│ ✓ Cross-channel: misma sesión si es la misma persona │
│ ⚠ Requiere identity resolution cross-channel │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ dmScope: "per-channel-peer" (recomendado) │
│ │
│ Korvo (Telegram) ──► agent:main:telegram:direct:korvo │
│ Korvo (WhatsApp) ──► agent:main:whatsapp:direct:korvo │
│ Ariel (Telegram) ──► agent:main:telegram:direct:ariel │
│ │
│ ✓ Aislamiento por persona + canal │
│ ✓ Sin ambigüedad de identidad │
│ ⚠ Korvo tiene sesiones separadas por canal │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ dmScope: "per-account-channel-peer" │
│ │
│ Bot1 Telegram: Korvo ──► agent:main:telegram:bot1:direct:korvo │
│ Bot2 Telegram: Korvo ──► agent:main:telegram:bot2:direct:korvo │
│ │
│ ✓ Para multi-cuenta en un mismo canal │
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
- La forma canónica actual en la documentación oficial es `direct`, no `dm`. Si ves `dm` en ejemplos legacy, trátalo como nomenclatura histórica.

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
 03:59 → Mensaje llega → sesión existente se reutiliza
 04:01 → Mensaje llega → sesión expirada → nuevo sessionId
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
 direct: { mode: "idle", idleMinutes: 240 }, // DMs: 4h de idle
 group: { mode: "idle", idleMinutes: 120 }, // Grupos: 2h
 thread: { mode: "daily", atHour: 4 } // Threads: diario
 },
 resetByChannel: {
 discord: { mode: "idle", idleMinutes: 10080 } // Discord: 1 semana
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

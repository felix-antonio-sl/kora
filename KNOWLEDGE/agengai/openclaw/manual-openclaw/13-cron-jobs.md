---
_manifest:
  urn: urn:agengai:kb:13-cron-jobs
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '13'
- cron
- jobs
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:13-cron-jobs
---

# Capítulo 13 — Cron Jobs

> **Propósito:** Entender el scheduler integrado del gateway: cómo programar tareas one-shot y recurrentes, las dos modalidades de ejecución (main vs isolated), los modos de delivery, y cómo combinar cron con heartbeats y sub-agentes para automatización completa.

- ---

## 13.1 Concepto: Scheduler Integrado

- Los cron jobs son **tareas programadas** que corren dentro del proceso del gateway.
- No dependen del crontab del OS ni de servicios externos — el gateway es el scheduler.

```
┌──────────────────────────────────────────────────────────┐
│ GATEWAY SCHEDULER │
│ │
│ jobs.json │
│ ├── job "Morning brief" ─── cron: "0 7 * * *" │
│ ├── job "Reminder" ─── at: "2026-02-21T16:00Z" │
│ └── job "Check health" ─── every: 3600000ms │
│ │
│ Cada tick: │
│ ¿Job due? → Ejecutar payload → Delivery (opcional) │
│ │
│ Persistencia: ~/.openclaw/cron/jobs.json │
│ Historial: ~/.openclaw/cron/runs/<jobId>.jsonl │
└──────────────────────────────────────────────────────────┘
```

### Los tres tipos de schedule

| Kind | CLI flag | Uso | Ejemplo |
|------|----------|-----|---------|
| `at` | `--at` | One-shot: corre una vez a la hora especificada | `--at "2026-02-21T16:00:00Z"` o `--at "20m"` |
| `every` | `--every` | Intervalo fijo en milisegundos | `--every 3600000` (1 hora) |
| `cron` | `--cron` | Expresión cron estándar (5 o 6 campos) | `--cron "0 7 * * *"` (7 AM diario) |

- **Timezone:** Para `cron` expressions, se usa la timezone del host si no se especifica `--tz`.
- Para `at`, ISO 8601 sin timezone se trata como UTC.

### Stagger (load spreading)

- Expresiones cron "top of hour" como `0 * * * *` reciben un stagger automático de hasta 5 minutos para evitar picos de carga.
- Expresiones de hora fija como `0 7 * * *` no se alteran.

```bash
# Forzar timing exacto
openclaw cron add --name "Exact" --cron "0 * * * *" --exact ...

# Stagger explícito de 30 segundos
openclaw cron add --name "Staggered" --cron "0 * * * *" --stagger 30s ...
```

- ---

## 13.2 Dos Modalidades de Ejecución

### Main Session: System Events

- El job inyecta un **system event** en la sesión main y opcionalmente trigger un heartbeat.

```
Job fires → System event enqueued
 │
 ▼
wakeMode?
├── "now" → Heartbeat inmediato con el event
└── "next-heartbeat" → Event espera al próximo heartbeat programado
 │
 ▼
Heartbeat run en sesión main
(el agente ve el event + contexto conversacional)
```

```json
{
 "name": "Calendar check",
 "schedule": { "kind": "at", "at": "2026-02-21T09:00:00-03:00" },
 "sessionTarget": "main",
 "wakeMode": "now",
 "payload": { "kind": "systemEvent", "text": "Check calendar for today's meetings." },
 "deleteAfterRun": true
}
```

- **Cuándo usar main session:**

- Quieres que el agente tenga **contexto conversacional** (historial reciente)
- La tarea es simple (un reminder, un check rápido)
- Quieres que se integre con el heartbeat flow normal
- También sirve para jobs `delivery.mode: "webhook"` cuando quieres usar el contexto main pero entregar el resultado fuera de OpenClaw.

### Isolated: Dedicated Agent Turn

- El job corre un **agent turn dedicado** en su propia sesión `cron:<jobId>`, sin historial previo.

```
Job fires → Sesión cron:<jobId> creada (fresh)
 │
 ▼
Agent turn completo:
 System prompt + payload.message
 Tool calls, inference, etc.
 │
 ▼
delivery.mode?
├── "announce" → Entrega output al canal + summary a main session
├── "webhook" → POST a delivery.to
└── "none" → Interno (nada se envía)
```

```json
{
 "name": "Morning brief",
 "schedule": { "kind": "cron", "expr": "0 7 * * *", "tz": "America/Santiago" },
 "sessionTarget": "isolated",
 "payload": {
 "kind": "agentTurn",
 "message": "Summarize: unread emails, today's calendar, pending inbox items.",
 "model": "anthropic/claude-haiku-4-5",
 "thinking": "low"
 },
 "delivery": {
 "mode": "announce",
 "channel": "telegram",
 "to": "7192195698"
 }
}
```

- **Cuándo usar isolated:**

- Tareas pesadas o largas que no deben contaminar main session
- Output específico que necesita delivery a un canal
- Model/thinking overrides sin afectar main
- Tareas que no necesitan contexto conversacional
- Tareas que se benefician de `lightContext: true` para evitar bootstrap pesado

### Comparativa

| | Main Session | Isolated |
|--|-------------|---------|
| **Sesión** | Main (historial compartido) | `cron:<jobId>` (fresh cada vez) |
| **Payload** | `systemEvent` (texto inyectado) | `agentTurn` (prompt completo) |
| **Contexto** | Ve conversación reciente | Bootstrap files o `lightContext` vacío |
| **Delivery** | Via heartbeat (al canal del heartbeat) | Configurable (announce/webhook/none) |
| **Model override** | ⚠ Cambia el modelo de main session | ✅ Solo para este run |
| **Costo** | Parte del heartbeat turn | Turn independiente |

### Current Session y Custom Session

- La documentación oficial actual agrega dos targets útiles:

```json5
{ "sessionTarget": "current" }
```

- `current` fija el job a la sesión donde fue creado.

```json5
{ "sessionTarget": "session:project-alpha-monitor" }
```

- `session:<custom-id>` mantiene contexto persistente entre runs del mismo job.

- ---

## 13.3 Delivery Modes

### announce

- Entrega el output del job a un canal de messaging.

```json5
delivery: {
 mode: "announce",
 channel: "telegram", // o "whatsapp", "discord", "slack", "last"
 to: "7192195698", // recipient (channel-specific)
 bestEffort: true // no falla el job si delivery falla
}
```

- **Flujo:**

1. Job isolated termina → output generado
2. Si output es `HEARTBEAT_OK` → no se entrega (suprimido)
3. Si el job ya envió un mensaje via `message` tool al mismo target → skip (evitar duplicados)
4. Delivery directa via channel adapters (no pasa por main agent)
5. Summary corto posted a main session (controlado por `wakeMode`)

- **Targets de Telegram con topics:** ``` "-1001234567890" → chat sin topic "-1001234567890:topic:123" → topic específico "telegram:group:-100...:topic:123" → prefixed form ```

### webhook

- POST del evento de completion a una URL.

```json5
delivery: {
 mode: "webhook",
 to: "https://api.example.com/cron-results"
}
```

- Si `cron.webhookToken` está configurado → header `Authorization: Bearer <token>`
- No se intenta channel delivery
- No se postea summary a main session
- Es válido tanto para jobs `main` como `isolated`.

### none

- Internal only.
- El job corre, pero nada se envía.
- Útil para jobs que hacen side effects (escribir archivos, actualizar state) sin necesitar output visible.

- ---

## 13.4 Model y Thinking Overrides

- Solo para jobs isolated (`agentTurn`):

```json5
payload: {
 kind: "agentTurn",
 message: "Deep weekly analysis...",
 model: "anthropic/claude-opus-4-6", // o alias: "opus"
 thinking: "high", // off|minimal|low|medium|high|xhigh
 timeoutSeconds: 600 // timeout del run
}
```

- **Resolución de modelo:**

1. Payload override (mayor prioridad)
2. Hook-specific defaults (e.g., `hooks.gmail.model`)
3. Agent config default

- **⚠ Para main session jobs:** Model override cambia el modelo de la sesión main compartida.
- Evitar — usar isolated jobs para model overrides.

### Lightweight bootstrap context

- Para chores programados que no necesitan bootstrap files, la doc oficial actual expone `lightContext: true`.

```json5
payload: {
 kind: "agentTurn",
 message: "Run housekeeping checks",
 lightContext: true
}
```

- ---

## 13.5 Agent Binding (Multi-Agent)

- En setups multi-agent, cada job puede correr bajo un agente específico:

```bash
# Crear job bajo agente "ops"
openclaw cron add --name "Ops sweep" --cron "0 6 * * *" \
 --session isolated --message "Check ops queue" --agent ops

# Cambiar agente de un job existente
openclaw cron edit <jobId> --agent ops

# Limpiar binding (vuelve a default)
openclaw cron edit <jobId> --clear-agent
```

- Si el `agentId` especificado no existe, el gateway hace fallback al agente default.

- ---

## 13.6 Retry y Backoff

### Recurring jobs

- Si un job recurring falla, OpenClaw aplica backoff exponencial:

```
1er fallo → retry en 30 segundos
2do fallo → retry en 1 minuto
3er fallo → retry en 5 minutos
4to fallo → retry en 15 minutos
5to+ fallo → retry en 60 minutos (cap)
```

- El backoff se resetea automáticamente después de un run exitoso.

### One-shot jobs

- En la documentación oficial actual, jobs `at` **sí** retrian errores transitorios:

```
1er fallo transitorio → retry en 30 segundos
2do fallo transitorio → retry en 1 minuto
3er fallo transitorio → retry en 5 minutos
4to fallo transitorio → disable
```

- Errores permanentes (auth/config/validation) deshabilitan inmediatamente.
- Después de un run terminal exitoso o skipped:

- Default: se auto-borran (`deleteAfterRun: true`)
- Si `deleteAfterRun: false`: se deshabilitan (quedan en jobs.json como record)

- ---

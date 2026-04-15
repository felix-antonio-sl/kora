---
_manifest:
  urn: urn:agengai:kb:09-sub-agentes
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- 09
- sub
- agentes
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:09-sub-agentes
---

# Capítulo 9 — Sub-Agentes (sessions_spawn)

> **Propósito:** Entender cómo un agente puede delegar trabajo a runs aislados en background, cómo se orquestan, qué tools reciben, y cómo los resultados fluyen de vuelta. Los sub-agentes transforman un agente individual en un sistema capaz de paralelismo y división del trabajo.

- ---

## 9.1 Concepto: Runs Aislados en Background

- Un sub-agente es un **run de agente independiente** que:

1. Corre en su propia sesión (`agent:<id>:subagent:<uuid>`)
2. Tiene su propio contexto (no ve el historial del parent)
3. Ejecuta una tarea (el `task`) con sus propios tool calls
4. Al terminar, **anuncia** el resultado de vuelta al chat del requester

```
┌─────────────────────────────────────────────────────────┐
│ MAIN SESSION (conversación con usuario) │
│ │
│ Usuario: "Investiga X, Y, Z en paralelo" │
│ │ │
│ ▼ │
│ Agente principal ejecuta: │
│ sessions_spawn(task: "Investiga X") → Sub-agent A │
│ sessions_spawn(task: "Investiga Y") → Sub-agent B │
│ sessions_spawn(task: "Investiga Z") → Sub-agent C │
│ │ │
│ ▼ │
│ (no bloqueante — main sigue disponible) │
│ │
│ ... tiempo pasa ... │
│ │
│ [System] Sub-agent A completed: │
│ Result: "X es..." Status: success │
│ [System] Sub-agent B completed: │
│ Result: "Y es..." Status: success │
│ [System] Sub-agent C completed: │
│ Result: "Z es..." Status: success │
│ │
│ Agente principal sintetiza y responde al usuario │
└─────────────────────────────────────────────────────────┘
```

### ¿Por qué sub-agentes y no tool calls secuenciales?

| | Tool calls normales | Sub-agentes |
|--|-------------------|------------|
| **Ejecución** | Secuencial dentro del mismo run | Paralela en background |
| **Contexto** | Comparte contexto del parent (acumula tokens) | Contexto propio (no contamina el parent) |
| **Bloqueo** | Bloquea la sesión hasta terminar | Non-blocking: main disponible inmediatamente |
| **Modelo** | Mismo modelo del parent | Override posible (modelo más barato/capaz) |
| **Timeout** | Timeout global de la sesión | Timeout independiente por sub-agent |
| **Costo** | Todo en un context window | Cada sub-agent tiene su propia ventana |

- **Caso de uso ideal:** Tareas que son independientes entre sí, toman tiempo (>30s), o generan mucho output que contaminaría el contexto del parent.

- ---

## 9.2 Tool: sessions_spawn

### Parámetros

```json
{
 "task": "Analiza el repositorio X y genera un informe de código",
 "label": "code-review-X",
 "agentId": "coding",
 "model": "opus",
 "thinking": "high",
 "runTimeoutSeconds": 300,
 "cleanup": "keep"
}
```

| Parámetro | Requerido | Default | Propósito |
|-----------|-----------|---------|-----------|
| `task` | ✅ | — | Instrucciones para el sub-agente. Es su "system message" |
| `label` | No | — | Nombre human-readable para identificar en `/subagents list` |
| `agentId` | No | Mismo que el caller | Ejecutar bajo otro agente (si permitido por allowlist) |
| `model` | No | Hereda del caller o `subagents.model` | Override de modelo |
| `thinking` | No | Hereda del caller o `subagents.thinking` | Nivel de reasoning |
| `runTimeoutSeconds` | No | 0 (sin timeout) | Abortar después de N segundos |
| `thread` | No | `false` | Solicita binding persistente a un thread/canal soportado |
| `mode` | No | `run` (o `session` si `thread:true`) | `run` = one-shot; `session` = sesión persistente ligada a thread |
| `cleanup` | No | `"keep"` | `"delete"` archiva inmediatamente post-announce |
| `sandbox` | No | `"inherit"` | `"require"` rechaza el spawn si el child no quedaría sandboxed |

### Retorno inmediato (non-blocking)

```json
{
 "status": "accepted",
 "runId": "run_abc123",
 "childSessionKey": "agent:main:subagent:f8a2b3c4-..."
}
```

- El tool retorna inmediatamente.
- El sub-agente corre en background.
- El resultado llega como un mensaje de sistema al chat del requester cuando termina.

### Thread-bound sessions

- La documentación oficial actual introduce sub-agentes ligados a un thread persistente.
- Hoy el canal soportado explícitamente es **Discord**.

```json
{
 "task": "Investiga este bug y mantén el hilo actualizado",
 "thread": true,
 "mode": "session",
 "cleanup": "keep"
}
```

- Flujo:
1. `sessions_spawn(thread: true)` crea o reutiliza un thread
2. el thread queda enfocado a la sesión del sub-agente
3. replies posteriores en ese thread vuelven al mismo child session
4. `/unfocus` corta el binding manualmente

- Slash commands relacionados:
- `/focus <target>`
- `/unfocus`
- `/agents`
- `/session idle <duración|off>`
- `/session max-age <duración|off>`

### Discovery: agents_list

```json
{ "tool": "agents_list" }
→ ["main", "coding", "ops"] // agentIds permitidos para spawn
```

- Controlado por `agents.list[].subagents.allowAgents`:

```json5
{
 agents: {
 list: [{
 id: "main",
 subagents: {
 allowAgents: ["main", "coding"] // main puede spawn bajo main o coding
 // ["*"] permite cualquier agentId
 }
 }]
 }
}
```

- ---

## 9.3 Announce: Cómo los Resultados Fluyen de Vuelta

### Flujo de announce

```
Sub-agente termina
 │
 ▼
Announce step (corre dentro de la sesión del sub-agente)
 │
 ├── Sub-agente responde "ANNOUNCE_SKIP"
 │ → Nada se postea al requester
 │
 └── Sub-agente genera respuesta
 │
 ▼
 Normalización a template:
 ┌───────────────────────────────────────────────┐
 │ Status: completed successfully │
 │ Result: [resumen generado por el sub-agente] │
 │ Notes: (si hay errores o contexto) │
 │ │
 │ runtime 2m34s | 12.4K in / 3.2K out / 15.6K │
 │ sessionKey: agent:main:subagent:f8a2... │
 │ transcript: ~/.openclaw/agents/main/sessions/ │
 │ f8a2b3c4.jsonl │
 └───────────────────────────────────────────────┘
 │
 ▼
 Delivery al chat del requester
 (preserva thread/topic routing)
```

### Status values

| Status | Significado |
|--------|------------|
| `completed successfully` | El sub-agente terminó su run sin errores |
| `failed` | Error durante ejecución (model error, tool error) |
| `timed out` | `runTimeoutSeconds` expiró |
| `unknown` | No se pudo determinar el outcome |

- **Status NO se infiere del contenido.** Viene del runtime — si el model call terminó sin excepciones, es success, incluso si el modelo dice "no pude encontrar nada".

### Delivery resiliente

- El announce usa un mecanismo de delivery con fallbacks:

1. Delivery directa al chat channel (idempotency key estable)
2. Si falla → fallback a queue routing
3. Si falla → retry con backoff exponencial
4. Si todo falla → give-up (best-effort)

- **Los announces son best-effort.** Si el gateway se reinicia antes de que un sub-agente termine, el announce se pierde.
- El transcript en disco sigue existiendo.

- ---

## 9.4 Tool Policy en Sub-Agentes

- Los sub-agentes tienen una policy de tools **más restrictiva** que el parent por defecto.

### Default: todo excepto session tools

```
Sub-agente (depth 1, leaf) recibe:
✅ read, write, edit, apply_patch (filesystem)
✅ exec, process (runtime)
✅ browser, canvas (UI)
✅ web_search, web_fetch (web)
✅ memory_search, memory_get (memoria)
✅ message (messaging)
✅ nodes, image, tts (periféricos)

❌ sessions_list (session tools)
❌ sessions_history
❌ sessions_send
❌ sessions_spawn (no puede spawn hijos)
❌ subagents
❌ cron, gateway (control plane)
```

### Override global

```json5
{
 tools: {
 subagents: {
 tools: {
 deny: ["browser", "canvas", "gateway", "cron"],
 // allow: ["read", "exec", "process", "web_search"] // allowlist restrictivo
 }
 }
 }
}
```

### Contexto inyectado

- Sub-agentes reciben un **prompt minimal**:

| Archivo | ¿Inyectado en sub-agente? |
|---------|--------------------------|
| AGENTS.md | ✅ Sí |
| TOOLS.md | ✅ Sí |
| SOUL.md | ❌ No |
| USER.md | ❌ No |
| IDENTITY.md | ❌ No |
| HEARTBEAT.md | ❌ No |
| MEMORY.md | ❌ No |

- Esto mantiene el contexto del sub-agente **lean**: sin personalidad, sin info del usuario, sin memoria inyectada.
- Si necesita contexto, se pasa en el `task`.

- La doc oficial actual lo explicita así: sub-agentes inyectan solo `AGENTS.md` + `TOOLS.md`.
- No reciben `SOUL.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, `BOOTSTRAP.md` ni `MEMORY.md`.

- ---

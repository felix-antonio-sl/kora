---
_manifest:
  urn: urn:kora:kb:09-sub-agentes
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- 09
- sub
- agentes
lang: es
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
│                MAIN SESSION (conversación con usuario)    │
│                                                          │
│  Usuario: "Investiga X, Y, Z en paralelo"               │
│       │                                                  │
│       ▼                                                  │
│  Agente principal ejecuta:                               │
│    sessions_spawn(task: "Investiga X")  → Sub-agent A    │
│    sessions_spawn(task: "Investiga Y")  → Sub-agent B    │
│    sessions_spawn(task: "Investiga Z")  → Sub-agent C    │
│       │                                                  │
│       ▼                                                  │
│  (no bloqueante — main sigue disponible)                 │
│                                                          │
│  ... tiempo pasa ...                                     │
│                                                          │
│  [System] Sub-agent A completed:                         │
│    Result: "X es..."   Status: success                   │
│  [System] Sub-agent B completed:                         │
│    Result: "Y es..."   Status: success                   │
│  [System] Sub-agent C completed:                         │
│    Result: "Z es..."   Status: success                   │
│                                                          │
│  Agente principal sintetiza y responde al usuario        │
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
| `cleanup` | No | `"keep"` | `"delete"` archiva inmediatamente post-announce |

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


### Discovery: agents_list

```json
{ "tool": "agents_list" }
→ ["main", "coding", "ops"]   // agentIds permitidos para spawn
```

- Controlado por `agents.list[].subagents.allowAgents`:


```json5
{
  agents: {
    list: [{
      id: "main",
      subagents: {
        allowAgents: ["main", "coding"]  // main puede spawn bajo main o coding
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
      │   → Nada se postea al requester
      │
      └── Sub-agente genera respuesta
          │
          ▼
     Normalización a template:
     ┌───────────────────────────────────────────────┐
     │ Status: completed successfully                │
     │ Result: [resumen generado por el sub-agente]  │
     │ Notes: (si hay errores o contexto)            │
     │                                               │
     │ runtime 2m34s | 12.4K in / 3.2K out / 15.6K  │
     │ sessionKey: agent:main:subagent:f8a2...       │
     │ transcript: ~/.openclaw/agents/main/sessions/ │
     │             f8a2b3c4.jsonl                    │
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
✅ read, write, edit, apply_patch          (filesystem)
✅ exec, process                            (runtime)
✅ browser, canvas                          (UI)
✅ web_search, web_fetch                    (web)
✅ memory_search, memory_get                (memoria)
✅ message                                  (messaging)
✅ nodes, image, tts                        (periféricos)

❌ sessions_list                            (session tools)
❌ sessions_history
❌ sessions_send
❌ sessions_spawn                           (no puede spawn hijos)
❌ subagents
❌ cron, gateway                            (control plane)
```

### Override global

```json5
{
  tools: {
    subagents: {
      tools: {
        deny: ["browser", "canvas", "gateway", "cron"],
        // allow: ["read", "exec", "process", "web_search"]  // allowlist restrictivo
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


- ---


## 9.5 Concurrencia y Límites

### Lane dedicada

- Los sub-agentes corren en una **lane de queue separada** del main:


```
Queue Lanes:
  main      → concurrency: 4 (default)    ← sesiones normales
  subagent  → concurrency: 8 (default)    ← sub-agentes
```

- Esto significa que los sub-agentes NO compiten con las sesiones normales por queue slots.
- Puedes tener 4 sesiones normales + 8 sub-agentes corriendo simultáneamente.


### Configuración

```json5
{
  agents: {
    defaults: {
      subagents: {
        maxConcurrent: 8,           // global lane cap
        maxChildrenPerAgent: 5,     // max hijos activos por sesión parent
        archiveAfterMinutes: 60,    // auto-archive post-completion
        model: "anthropic/claude-haiku-4-5",  // modelo default para sub-agentes
        thinking: "low"             // thinking default
      }
    }
  }
}
```

### Límites

| Límite | Default | Rango | Propósito |
|--------|---------|-------|-----------|
| `maxConcurrent` | 8 | — | Max sub-agentes corriendo simultáneamente en todo el gateway |
| `maxChildrenPerAgent` | 5 | 1-20 | Max hijos activos por sesión parent |
| `maxSpawnDepth` | 1 | 1-5 | Niveles de nesting permitidos |
| `archiveAfterMinutes` | 60 | — | Tiempo hasta auto-archive post-completion |

### Auto-archive

- Después de completar, los sub-agentes se archivan automáticamente:


```
Sub-agente completa → espera archiveAfterMinutes (60 min)
      │
      ▼
sessions.delete: borra entry de sessions.json
Transcript: renombra a *.deleted.<timestamp> (preservado en disco)
```

- `cleanup: "delete"` en el spawn archiva **inmediatamente** post-announce
- `cleanup: "keep"` espera el auto-archive timer
- Si el gateway se reinicia, timers pendientes se pierden (best-effort)

- ---


## 9.6 Modelo y Costo

### Estrategia de costo para sub-agentes

- Cada sub-agente tiene su **propio context window** y su propio consumo de tokens.
- Si spawns 5 sub-agentes con Opus, pagas 5 context windows de Opus.


- **Patrón recomendado:**


```
Main agent:     Sonnet (calidad + prompt cache para conversación)
Sub-agentes:    Haiku (barato para tareas paralelas)
Special tasks:  Opus via model override (cuando necesitas calidad máxima)
```

```json5
{
  agents: {
    defaults: {
      model: { primary: "anthropic/claude-sonnet-4-6" },
      subagents: {
        model: "anthropic/claude-haiku-4-5"     // default barato
      }
    }
  }
}
```

```json
// Spawn específico con modelo caro cuando se necesita:
{
  "task": "Análisis profundo de arquitectura...",
  "model": "opus",
  "thinking": "high"
}
```

### Jerarquía de resolución de modelo

```
1. model explícito en sessions_spawn       (mayor prioridad)
2. agents.list[].subagents.model           (per-agent default)
3. agents.defaults.subagents.model         (global default)
4. Modelo del caller                       (herencia, menor prioridad)
```

- ---


## 9.7 Auth en Sub-Agentes

### Merge de auth profiles

```
Sub-agente agent:main:subagent:xyz
      │
      ▼
Cargar auth-profiles.json de agentId target
      │
      ▼
Merge: perfiles del target agent + perfiles del main (como fallback)
      │
      ▼
Si conflicto en profile ID → gana el target agent
```

- Si el sub-agente se spawna bajo `agentId: "coding"`, usa los auth profiles de `coding` con los de `main` como fallback.
- Esto asegura que:


- Sub-agentes bajo otro agentId usan las credenciales de ese agente
- Si ese agente no tiene credenciales para un provider, las del main sirven de backup
- El merge es aditivo (nunca se pierden perfiles)

- ---


## 9.8 Patrones de Uso

### Patrón 1: Investigación paralela

```
"Investiga el mercado de IA en salud. Paraleliza:
 1. Competidores principales
 2. Regulaciones por país
 3. Tendencias tecnológicas"

→ 3 sub-agentes (haiku, web_search + web_fetch)
→ Resultados fluyen al main
→ Main sintetiza en un informe
```

### Patrón 2: Code review distribuido

```
"Revisa este PR. Divide por archivos."

→ Sub-agent A: review de backend/api.py
→ Sub-agent B: review de frontend/App.tsx
→ Sub-agent C: review de tests/
→ Main consolida los findings
```

### Patrón 3: Tarea larga no-bloqueante

```
"Genera un informe de estado del servidor. No me bloquees."

→ 1 sub-agente (exec, read)
→ Main responde "En proceso, te aviso cuando termine"
→ Sub-agente corre 5 minutos recolectando métricas
→ Announce con el informe completo
```

### Patrón 4: Diferentes modelos para diferentes subtareas

```
→ Sub-agent A (haiku): "Busca y resume artículos"        // rápido + barato
→ Sub-agent B (opus): "Analiza y critica la evidencia"   // profundo + caro
→ Sub-agent C (kimi): "Genera draft largo (100K ctx)"    // contexto amplio
```

- ---


## 9.9 Slash Commands para Sub-Agentes

### Desde el chat del requester

| Comando | Qué hace |
|---------|----------|
| `/subagents list` | Lista sub-agentes activos y recientes de esta sesión |
| `/subagents info <id\|#>` | Metadata: status, timestamps, sessionId, transcript path |
| `/subagents log <id\|#> [limit] [tools]` | Ver las últimas N líneas del transcript (incluir tools opcionalmente) |
| `/subagents send <id\|#> <msg>` | Enviar mensaje al sub-agente (crea un nuevo turn en su sesión) |
| `/subagents steer <id\|#> <msg>` | Inyectar en el run activo (steer, no followup) |
| `/subagents kill <id\|#\|all>` | Matar sub-agente(s) + cascade a hijos |
| `/subagents spawn <agentId> <task>` | Spawn desde slash command (no desde tool call) |

### Desde tools del agente

| Tool | Propósito |
|------|-----------|
| `sessions_spawn` | Crear sub-agente |
| `subagents(action: "list")` | Listar activos |
| `subagents(action: "steer", target, message)` | Inyectar en run activo |
| `subagents(action: "kill", target)` | Matar sub-agente |
| `sessions_history(sessionKey)` | Leer transcript de sub-agente completado |

### `/stop` cascade

```
/stop en chat del requester
      │
      ▼
Aborta run de la sesión actual
      │
      ▼
Detecta sub-agentes spawneados desde esta sesión
      │
      ▼
Kill de cada sub-agente
      │
      ▼
(Si depth-2) Kill de sub-sub-agentes de cada uno
```

- ---


## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Sesión aislada per sub-agent** | Contexto limpio, sin contaminación del parent |
| **Non-blocking spawn** | Main disponible inmediatamente; paralelismo real |
| **Announce automático** | Resultados fluyen de vuelta sin polling |
| **Default: sin session tools** | Sub-agentes no pueden spawnar hijos ni leer sesiones ajenas |
| **Lane dedicada** | Sub-agentes no compiten con sesiones normales |
| **maxChildrenPerAgent** | Previene fan-out descontrolado |
| **Model override per-spawn** | Optimización de costo: haiku para tareas simples, opus para complejas |
| **Prompt minimal** | Solo AGENTS.md + TOOLS.md → contexto lean, cost-efficient |
| **Auto-archive** | Cleanup automático post-completion |
| **Auth merge** | Sub-agentes bajo otro agentId heredan auth del parent como fallback |
| **Best-effort announce** | Trade-off: simplicidad operativa vs garantía de delivery |

- ---


- *Siguiente: [Capítulo 10 — Sub-Agentes Anidados (Orchestrator Pattern)](10-sub-agentes-anidados.md)*


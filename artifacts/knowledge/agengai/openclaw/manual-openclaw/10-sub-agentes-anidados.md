---
_manifest:
  urn: urn:agengai:kb:10-sub-agentes-anidados
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '10'
- sub
- agentes
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:10-sub-agentes-anidados
---

# Capítulo 10 — Sub-Agentes Anidados (Orchestrator Pattern)

> **Propósito:** Entender cómo habilitar y diseñar orquestación multi-nivel: un agente principal que delega a un orquestador, que a su vez distribuye trabajo a workers. Este capítulo construye sobre el Cap. 9 y añade la dimensión de profundidad.

- ---

## 10.1 Concepto: Depth > 1

- Por default, los sub-agentes son **flat** (`maxSpawnDepth:
- 1`): el main puede spawn sub-agentes, pero esos sub-agentes no pueden spawn hijos.
- El orchestrator pattern habilita **un nivel adicional** de nesting:

```
maxSpawnDepth: 1 (default — flat)
──────────────────────────────────
Main ──► Sub-A
 ──► Sub-B (Sub-A y Sub-B son leaves: no pueden spawn)
 ──► Sub-C

maxSpawnDepth: 2 (orchestrator pattern)
──────────────────────────────────────
Main ──► Orchestrator (depth 1)
 │
 ├──► Worker-1 (depth 2, leaf)
 ├──► Worker-2 (depth 2, leaf)
 └──► Worker-3 (depth 2, leaf)
```

### ¿Por qué no spawn directo desde main?

| | Main → N workers (flat) | Main → Orchestrator → N workers (nested) |
|--|------------------------|------------------------------------------|
| **Quién coordina** | El main, entre turns de conversación | El orchestrator, dedicado a coordinar |
| **Bloqueo del main** | Main disponible pero debe procesar N announces | Main recibe 1 announce final (síntesis) |
| **Complejidad del main** | Main acumula N resultados en su contexto | Main recibe resumen pre-sintetizado |
| **Costo de contexto** | N announces → N system messages en historial del main | 1 announce → 1 system message |
| **Flexibilidad** | Main debe saber dividir la tarea | Orchestrator especializado en dividir y sintetizar |

- **El orchestrator pattern brilla cuando:**

- La tarea requiere **dividir, distribuir, esperar, y sintetizar** — y ese flujo es complejo
- Quieres evitar contaminar el contexto del main con N resultados intermedios
- El orchestrator puede usar un modelo diferente (más barato para coordinación)

- ---

## 10.2 Configuración

### Habilitar nesting

```json5
{
 agents: {
 defaults: {
 subagents: {
 maxSpawnDepth: 2, // permitir depth-1 → depth-2
 maxChildrenPerAgent: 5, // max workers por orchestrator
 maxConcurrent: 8 // global lane cap
 }
 }
 }
}
```

### Depth levels y session keys

| Depth | Session Key | Rol | ¿Puede spawn? |
|-------|------------|-----|----------------|
| 0 | `agent:main:main` | Main agent | ✅ Siempre |
| 1 | `agent:main:subagent:<uuid-A>` | Orchestrator | ✅ Si `maxSpawnDepth ≥ 2` |
| 2 | `agent:main:subagent:<uuid-A>:subagent:<uuid-B>` | Worker (leaf) | ❌ Nunca |

- **Depth 2 es siempre leaf.** No importa si configuras `maxSpawnDepth:
- 5` — en la práctica, depth 2 es el pattern recomendado.
- Depths mayores agregan latencia y complejidad sin beneficio claro.

- ---

## 10.3 Tool Policy por Depth

- La tool policy cambia según el depth y el modo:

### Depth 1 cuando maxSpawnDepth = 1 (leaf mode, default)

```
✅ Todos los tools normales (read, exec, browser, web_*, etc.)
❌ sessions_spawn ← no puede crear hijos
❌ subagents ← no puede gestionar hijos
❌ sessions_list ← no puede ver otras sesiones
❌ sessions_history ← no puede leer transcripts ajenos
❌ sessions_send ← no puede enviar a otras sesiones
```

### Depth 1 cuando maxSpawnDepth ≥ 2 (orchestrator mode)

```
✅ Todos los tools normales
✅ sessions_spawn ← PUEDE crear workers (depth 2)
✅ subagents ← PUEDE gestionar sus workers
✅ sessions_list ← PUEDE ver sus sesiones hijas
✅ sessions_history ← PUEDE leer transcripts de hijos
❌ sessions_send ← NO puede enviar a sesiones arbitrarias
```

### Depth 2 (siempre leaf)

```
✅ Todos los tools normales
❌ sessions_spawn ← SIEMPRE denied en depth 2
❌ subagents
❌ sessions_list
❌ sessions_history
❌ sessions_send
```

### Tabla resumen

| Tool | Depth 0 (main) | Depth 1 (leaf) | Depth 1 (orch) | Depth 2 (leaf) |
|------|----------------|----------------|-----------------|----------------|
| `sessions_spawn` | ✅ | ❌ | ✅ | ❌ |
| `subagents` | ✅ | ❌ | ✅ | ❌ |
| `sessions_list` | ✅ | ❌ | ✅ | ❌ |
| `sessions_history` | ✅ | ❌ | ✅ | ❌ |
| `sessions_send` | ✅ | ❌ | ❌ | ❌ |
| Tools normales | ✅ | ✅ | ✅ | ✅ |

- **Observación clave:** El orchestrator en depth 1 recibe session tools **solo porque** `maxSpawnDepth ≥ 2`.
- Si vuelves a poner `maxSpawnDepth:
- 1`, pierde esos tools automáticamente.

- ---

## 10.4 Announce Chain: Flujo de Resultados Multi-Nivel

```
┌─────────────────────────────────────────────────────────────┐
│ Depth 0: MAIN │
│ │
│ 1. spawn Orchestrator (depth 1) │
│ task: "Investiga X en profundidad, divide en subtareas" │
│ │
│ ... main libre para otros mensajes ... │
│ │
│ 8. Recibe announce del Orchestrator: │
│ "Investigación completa. Resumen: ..." │
│ │
│ 9. Main procesa y responde al usuario │
└──────────────────────────┬──────────────────────────────────┘
 │
┌──────────────────────────┴──────────────────────────────────┐
│ Depth 1: ORCHESTRATOR │
│ │
│ 2. Analiza la tarea, divide: │
│ spawn Worker-A: "Investiga aspecto 1" │
│ spawn Worker-B: "Investiga aspecto 2" │
│ spawn Worker-C: "Investiga aspecto 3" │
│ │
│ ... orchestrator espera announces de workers ... │
│ │
│ 6. Recibe 3 announces: │
│ Worker-A: "Aspecto 1 es..." │
│ Worker-B: "Aspecto 2 es..." │
│ Worker-C: "Aspecto 3 es..." │
│ │
│ 7. Sintetiza todo en un informe consolidado │
│ → Su propio announce sube a Main (depth 0) │
└──────────────────────────┬──────────────────────────────────┘
 │
┌──────────────────────────┴──────────────────────────────────┐
│ Depth 2: WORKERS (3 paralelos) │
│ │
│ 3. Worker-A ejecuta: web_search, read, exec │
│ 4. Worker-B ejecuta: web_fetch, memory_search │
│ 5. Worker-C ejecuta: browser, exec │
│ │
│ Cada worker termina → announce a Orchestrator (depth 1) │
│ (NO a Main directamente) │
└─────────────────────────────────────────────────────────────┘
```

### Regla: cada nivel solo ve announces de sus hijos directos

- Workers (depth 2) anuncian a su parent: el Orchestrator (depth 1)
- El Orchestrator anuncia a SU parent: Main (depth 0)
- Main **nunca** recibe announces directos de los workers

- Esto mantiene la abstracción limpia:
- Main delega al Orchestrator, el Orchestrator se encarga del detalle.

- ---

## 10.5 Fan-Out Control: maxChildrenPerAgent

- Cada sesión (en cualquier depth) puede tener como máximo `maxChildrenPerAgent` hijos activos simultáneamente.

```json5
{
 agents: {
 defaults: {
 subagents: {
 maxChildrenPerAgent: 5 // default
 }
 }
 }
}
```

### ¿Qué pasa si se excede?

- El `sessions_spawn` retorna error — el modelo debe esperar a que un hijo termine antes de spawnar otro.

### Fan-out total

```
Main (depth 0):
 └── Orchestrator-A (depth 1) ← 1 child de Main
 ├── Worker-1 (depth 2) ← 5 children max de Orch-A
 ├── Worker-2
 ├── Worker-3
 ├── Worker-4
 └── Worker-5

 └── Orchestrator-B (depth 1) ← 2nd child de Main
 ├── Worker-6
 └── Worker-7

Fan-out total: 2 orchestrators + 7 workers = 9 sub-agentes
Limitado por: maxChildrenPerAgent (5 per orch) × children de main (5 max)
 + global maxConcurrent (8 default)
```

- **maxConcurrent es el hard cap global.** Aunque puedas tener 5 orchestrators × 5 workers = 25 sub-agentes en teoría, solo 8 corren simultáneamente.
- El resto se encola.

- ---

## 10.6 Cascade Stop

### `/stop` en el chat del main

```
/stop
 │
 ├── Aborta run actual de main session
 │
 ├── Detecta sub-agentes spawneados desde main:
 │ ├── Orchestrator-A → KILL
 │ │ ├── Worker-1 → KILL (cascade)
 │ │ ├── Worker-2 → KILL (cascade)
 │ │ └── Worker-3 → KILL (cascade)
 │ │
 │ └── Orchestrator-B → KILL
 │ └── Worker-4 → KILL (cascade)
 │
 └── Todo el árbol detenido
```

### `/subagents kill <id>`

- Kill selectivo: mata un sub-agente específico y **todos sus descendientes**.

```
/subagents kill Orchestrator-A
 │
 ├── Orchestrator-A → KILL
 ├── Worker-1 → KILL (cascade)
 ├── Worker-2 → KILL (cascade)
 └── Worker-3 → KILL (cascade)

(Orchestrator-B y sus workers NO se afectan)
```

- ---

# Capítulo 10 — Sub-Agentes Anidados (Orchestrator Pattern)

> **Propósito:** Entender cómo habilitar y diseñar orquestación multi-nivel: un agente principal que delega a un orquestador, que a su vez distribuye trabajo a workers. Este capítulo construye sobre el Cap. 9 y añade la dimensión de profundidad.

---

## 10.1 Concepto: Depth > 1

Por default, los sub-agentes son **flat** (`maxSpawnDepth: 1`): el main puede spawn sub-agentes, pero esos sub-agentes no pueden spawn hijos. El orchestrator pattern habilita **un nivel adicional** de nesting:

```
maxSpawnDepth: 1 (default — flat)
──────────────────────────────────
Main ──► Sub-A
     ──► Sub-B        (Sub-A y Sub-B son leaves: no pueden spawn)
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

**El orchestrator pattern brilla cuando:**
- La tarea requiere **dividir, distribuir, esperar, y sintetizar** — y ese flujo es complejo
- Quieres evitar contaminar el contexto del main con N resultados intermedios
- El orchestrator puede usar un modelo diferente (más barato para coordinación)

---

## 10.2 Configuración

### Habilitar nesting

```json5
{
  agents: {
    defaults: {
      subagents: {
        maxSpawnDepth: 2,          // permitir depth-1 → depth-2
        maxChildrenPerAgent: 5,    // max workers por orchestrator
        maxConcurrent: 8           // global lane cap
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

**Depth 2 es siempre leaf.** No importa si configuras `maxSpawnDepth: 5` — en la práctica, depth 2 es el pattern recomendado. Depths mayores agregan latencia y complejidad sin beneficio claro.

---

## 10.3 Tool Policy por Depth

La tool policy cambia según el depth y el modo:

### Depth 1 cuando maxSpawnDepth = 1 (leaf mode, default)

```
✅ Todos los tools normales (read, exec, browser, web_*, etc.)
❌ sessions_spawn       ← no puede crear hijos
❌ subagents            ← no puede gestionar hijos
❌ sessions_list        ← no puede ver otras sesiones
❌ sessions_history     ← no puede leer transcripts ajenos
❌ sessions_send        ← no puede enviar a otras sesiones
```

### Depth 1 cuando maxSpawnDepth ≥ 2 (orchestrator mode)

```
✅ Todos los tools normales
✅ sessions_spawn       ← PUEDE crear workers (depth 2)
✅ subagents            ← PUEDE gestionar sus workers
✅ sessions_list        ← PUEDE ver sus sesiones hijas
✅ sessions_history     ← PUEDE leer transcripts de hijos
❌ sessions_send        ← NO puede enviar a sesiones arbitrarias
```

### Depth 2 (siempre leaf)

```
✅ Todos los tools normales
❌ sessions_spawn       ← SIEMPRE denied en depth 2
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

**Observación clave:** El orchestrator en depth 1 recibe session tools **solo porque** `maxSpawnDepth ≥ 2`. Si vuelves a poner `maxSpawnDepth: 1`, pierde esos tools automáticamente.

---

## 10.4 Announce Chain: Flujo de Resultados Multi-Nivel

```
┌─────────────────────────────────────────────────────────────┐
│ Depth 0: MAIN                                                │
│                                                              │
│  1. spawn Orchestrator (depth 1)                             │
│     task: "Investiga X en profundidad, divide en subtareas"  │
│                                                              │
│  ... main libre para otros mensajes ...                      │
│                                                              │
│  8. Recibe announce del Orchestrator:                         │
│     "Investigación completa. Resumen: ..."                   │
│                                                              │
│  9. Main procesa y responde al usuario                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────┴──────────────────────────────────┐
│ Depth 1: ORCHESTRATOR                                        │
│                                                              │
│  2. Analiza la tarea, divide:                                │
│     spawn Worker-A: "Investiga aspecto 1"                    │
│     spawn Worker-B: "Investiga aspecto 2"                    │
│     spawn Worker-C: "Investiga aspecto 3"                    │
│                                                              │
│  ... orchestrator espera announces de workers ...            │
│                                                              │
│  6. Recibe 3 announces:                                      │
│     Worker-A: "Aspecto 1 es..."                              │
│     Worker-B: "Aspecto 2 es..."                              │
│     Worker-C: "Aspecto 3 es..."                              │
│                                                              │
│  7. Sintetiza todo en un informe consolidado                 │
│     → Su propio announce sube a Main (depth 0)               │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────┴──────────────────────────────────┐
│ Depth 2: WORKERS (3 paralelos)                               │
│                                                              │
│  3. Worker-A ejecuta: web_search, read, exec                │
│  4. Worker-B ejecuta: web_fetch, memory_search               │
│  5. Worker-C ejecuta: browser, exec                          │
│                                                              │
│  Cada worker termina → announce a Orchestrator (depth 1)     │
│  (NO a Main directamente)                                    │
└─────────────────────────────────────────────────────────────┘
```

### Regla: cada nivel solo ve announces de sus hijos directos

- Workers (depth 2) anuncian a su parent: el Orchestrator (depth 1)
- El Orchestrator anuncia a SU parent: Main (depth 0)
- Main **nunca** recibe announces directos de los workers

Esto mantiene la abstracción limpia: Main delega al Orchestrator, el Orchestrator se encarga del detalle.

---

## 10.5 Fan-Out Control: maxChildrenPerAgent

Cada sesión (en cualquier depth) puede tener como máximo `maxChildrenPerAgent` hijos activos simultáneamente.

```json5
{
  agents: {
    defaults: {
      subagents: {
        maxChildrenPerAgent: 5    // default
      }
    }
  }
}
```

### ¿Qué pasa si se excede?

El `sessions_spawn` retorna error — el modelo debe esperar a que un hijo termine antes de spawnar otro.

### Fan-out total

```
Main (depth 0):
  └── Orchestrator-A (depth 1)         ← 1 child de Main
       ├── Worker-1 (depth 2)          ← 5 children max de Orch-A
       ├── Worker-2
       ├── Worker-3
       ├── Worker-4
       └── Worker-5

  └── Orchestrator-B (depth 1)         ← 2nd child de Main
       ├── Worker-6
       └── Worker-7

Fan-out total: 2 orchestrators + 7 workers = 9 sub-agentes
Limitado por: maxChildrenPerAgent (5 per orch) × children de main (5 max)
                + global maxConcurrent (8 default)
```

**maxConcurrent es el hard cap global.** Aunque puedas tener 5 orchestrators × 5 workers = 25 sub-agentes en teoría, solo 8 corren simultáneamente. El resto se encola.

---

## 10.6 Cascade Stop

### `/stop` en el chat del main

```
/stop
  │
  ├── Aborta run actual de main session
  │
  ├── Detecta sub-agentes spawneados desde main:
  │   ├── Orchestrator-A → KILL
  │   │   ├── Worker-1 → KILL (cascade)
  │   │   ├── Worker-2 → KILL (cascade)
  │   │   └── Worker-3 → KILL (cascade)
  │   │
  │   └── Orchestrator-B → KILL
  │       └── Worker-4 → KILL (cascade)
  │
  └── Todo el árbol detenido
```

### `/subagents kill <id>`

Kill selectivo: mata un sub-agente específico y **todos sus descendientes**.

```
/subagents kill Orchestrator-A
  │
  ├── Orchestrator-A → KILL
  ├── Worker-1 → KILL (cascade)
  ├── Worker-2 → KILL (cascade)
  └── Worker-3 → KILL (cascade)

(Orchestrator-B y sus workers NO se afectan)
```

---

## 10.7 Diseño de un Orchestrator Efectivo

### El task del orchestrator

El `task` que pasas al orchestrator debe ser **prescriptivo sobre el patrón**, no solo sobre la tarea:

```
❌ Malo:
"Investiga el mercado de IA en salud"
(El orchestrator no sabe que debe dividir y delegar)

✅ Bueno:
"Eres un orchestrator. Tu tarea: investigar el mercado de IA en salud.

Patrón de trabajo:
1. Analiza la tarea y divídela en 3-5 subtareas independientes
2. Usa sessions_spawn para crear un worker por subtarea
3. Cada worker debe usar web_search y web_fetch para investigar
4. Espera los announces de todos los workers
5. Sintetiza los resultados en un informe consolidado
6. Tu announce final debe ser el informe completo

Modelo para workers: haiku (usa model='anthropic/claude-haiku-4-5')
Timeout por worker: 120 segundos"
```

### Modelo del orchestrator

El orchestrator no hace trabajo pesado — divide, delega, espera, y sintetiza. Un modelo de tier medio es suficiente:

```
Main:          Sonnet (conversación con usuario)
Orchestrator:  Sonnet o Haiku (coordinación, no necesita Opus)
Workers:       Haiku (ejecución, barato)
Special worker: Opus (si una subtarea requiere análisis profundo)
```

### Error handling

El orchestrator debe manejar la posibilidad de que un worker falle o timeout:

```
✅ En el task del orchestrator:
"Si un worker falla o timeout, reporta qué subtarea falló y con qué
resultado parcial. No reintentas automáticamente. Incluye los fallos
en el informe final con status claro."
```

### Anti-patrones

| Anti-patrón | Por qué es malo | Qué hacer |
|-------------|-----------------|-----------|
| Orchestrator spawna 20 workers | `maxChildrenPerAgent` lo bloquea (default 5); waste de queue | Dividir en 3-5 subtareas significativas |
| Workers que spawnean (depth 3+) | Complejidad exponencial, latencia acumulada | Mantener depth 2; diseñar workers como leaf |
| Orchestrator con Opus | Caro para solo coordinar | Haiku o Sonnet para orchestration |
| Task sin instrucción de patrón | Orchestrator no sabe que debe dividir/delegar | Ser explícito sobre el workflow |
| Sin timeout en workers | Workers zombie que nunca terminan | Siempre usar `runTimeoutSeconds` |
| Orchestrator no sintetiza | Cada announce del worker llega raw al main | Task debe incluir "sintetiza antes de anunciar" |

---

## 10.8 Caso de Uso Completo: Research Pipeline

### Trigger

```
Usuario: "Necesito un análisis completo del marco regulatorio de IA en Chile,
Argentina y México. Incluye legislación vigente, proyectos en trámite, y
comparativa."
```

### Main agent decide spawnar orchestrator

```json
{
  "task": "Eres un orchestrator de investigación. Tarea: análisis regulatorio de IA en Chile, Argentina y México.\n\nPatrón:\n1. Spawn 3 workers, uno por país\n2. Cada worker debe buscar: legislación vigente + proyectos en trámite + entidad reguladora\n3. Usa model='anthropic/claude-haiku-4-5' y runTimeoutSeconds=180 por worker\n4. Espera los 3 announces\n5. Sintetiza en tabla comparativa + resumen ejecutivo\n6. Tu announce final es el informe completo",
  "label": "ai-regulation-latam",
  "model": "sonnet"
}
```

### Orchestrator ejecuta

```
Orchestrator recibe task
      │
      ▼
Analiza: 3 subtareas (Chile, Argentina, México)
      │
      ├── spawn Worker-Chile:
      │   task: "Investiga marco regulatorio de IA en Chile..."
      │   model: haiku, timeout: 180s
      │
      ├── spawn Worker-Argentina:
      │   task: "Investiga marco regulatorio de IA en Argentina..."
      │   model: haiku, timeout: 180s
      │
      └── spawn Worker-Mexico:
          task: "Investiga marco regulatorio de IA en México..."
          model: haiku, timeout: 180s
      │
      ▼
  Espera announces (3 workers corren en paralelo)
      │
      ▼
  Worker-Chile: "Chile: Ley 21.719 sobre datos personales..."
  Worker-Argentina: "Argentina: Proyecto de ley S-2257/2023..."
  Worker-Mexico: "México: Ley Federal de Protección de Datos..."
      │
      ▼
  Orchestrator sintetiza:
  - Tabla comparativa
  - Resumen ejecutivo
  - Gaps identificados
      │
      ▼
  Announce → Main
```

### Main recibe y entrega

```
[System] Sub-agent "ai-regulation-latam" completed:
Status: completed successfully
Result: "## Análisis Regulatorio de IA en Latinoamérica

### Tabla Comparativa
| País | Ley vigente | Proyecto en trámite | Entidad |
| Chile | Ley 21.719 | ... | ... |
..."

runtime 3m42s | 45.2K in / 12.8K out
```

Main puede entregar directamente al usuario o agregar contexto/opinión.

---

## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **maxSpawnDepth: 2** | Orchestrator pattern sin complejidad excesiva |
| **Tool policy por depth** | Orchestrators coordinan; workers ejecutan; nadie escala más |
| **Announce chain** | Resultados fluyen level-by-level, no cross-level |
| **maxChildrenPerAgent** | Previene fan-out descontrolado por orchestrator |
| **maxConcurrent como hard cap** | Protección global contra resource exhaustion |
| **Cascade stop** | Un `/stop` limpia todo el árbol |
| **Depth 2 = siempre leaf** | Invariante de seguridad: no hay recursión infinita |
| **Task prescriptivo** | El orchestrator necesita instrucciones explícitas sobre el patrón |

### Cuándo usar flat vs orchestrator

```
¿Cuántas subtareas?
├── 1-3 → Flat (main spawna directamente)
│         Main puede procesar 1-3 announces sin problema
│
├── 4-8 → Depende:
│         ¿Main necesita sintetizar los resultados? → Orchestrator
│         ¿Solo recolectar? → Flat puede servir
│
└── 8+  → Orchestrator
          Main no debería procesar 8+ announces crudos
          El orchestrator sintetiza antes de anunciar
```

---

*Siguiente: [Capítulo 11 — Comunicación Inter-Sesión](11-comunicacion-inter-sesion.md)*

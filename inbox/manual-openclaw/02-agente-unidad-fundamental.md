---
_manifest:
  urn: urn:kora:kb:02-agente-unidad-fundamental
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '02'
- agente
- unidad
lang: es
---

# Capítulo 2 — El Agente como Unidad Fundamental

> **Propósito:** Entender qué constituye un "agente" en OpenClaw — no como abstracción filosófica, sino como unidad concreta con workspace, sesiones, auth, skills y tools. Este capítulo establece el vocabulario y los mecanismos que todas las decisiones multi-agente y de automatización presuponen.

- ---


## 2.1 Anatomía de un Agente

- Un agente en OpenClaw no es un modelo de IA ni un prompt.
- Es una **unidad operacional** compuesta por cuatro piezas concretas en disco:


```
Agente "main"
├── 1. WORKSPACE (~/.openclaw/workspace o custom)
│   ├── AGENTS.md, SOUL.md, USER.md, IDENTITY.md   ← personalidad
│   ├── TOOLS.md, HEARTBEAT.md                      ← operaciones
│   ├── MEMORY.md                                    ← memoria curada
│   ├── memory/YYYY-MM-DD.md                         ← logs diarios
│   ├── skills/                                      ← skills custom
│   └── ...                                          ← scripts, projects, etc.
│
├── 2. AGENT DIR (~/.openclaw/agents/<agentId>/)
│   ├── agent/
│   │   └── auth-profiles.json                       ← API keys + OAuth tokens
│   ├── sessions/
│   │   ├── sessions.json                            ← metadata de todas las sesiones
│   │   └── *.jsonl                                  ← transcripts de cada sesión
│   └── qmd/ (opcional)
│       └── (QMD sidecar state)
│
├── 3. CONFIG (referencia en openclaw.json)
│   └── agents.list[].{id, workspace, sandbox, tools, heartbeat, ...}
│
└── 4. IDENTITY RUNTIME
    ├── Modelo asignado (primary + fallbacks)
    ├── Skills elegibles (snapshot por sesión)
    └── Tools permitidos (policy resuelta)
```

### Las cuatro piezas y su rol

| Pieza | Persistencia | Compartible | Propósito |
|-------|-------------|-------------|-----------|
| **Workspace** | Disco, versionable en git | NO entre agentes | Personalidad, memoria, skills custom. Es el "hogar" del agente |
| **Agent Dir** | Disco, internal | NO entre agentes | Auth credentials, session transcripts. Nunca en git |
| **Config** | openclaw.json | — | Declaración del agente: modelo, sandbox, tools, heartbeat |
| **Identity Runtime** | In-memory, por sesión | — | Skills snapshot, tool policy resuelta, modelo elegido |

### ¿Por qué importa la separación?

- **Workspace vs AgentDir:** El workspace es "lo que el agente sabe y quién es" — versionable, portable, recuperable desde git.
- El agentDir es "credenciales y state operativo" — nunca en git, nunca compartido.
- Si pierdes el agentDir, re-autenticas.
- Si pierdes el workspace, pierdes la personalidad y la memoria.


- **Auth isolation:** Cada agente tiene su propio `auth-profiles.json`.
- Las credenciales NO se comparten entre agentes.
- Si quieres que dos agentes usen la misma API key, copias manualmente el archivo — pero nunca comparten referencia.
- Esto es un invariante de seguridad: un agente comprometido no expone las credenciales de otro.


- **Config como declaración:** El agente no "existe" hasta que está declarado en `agents.list[]` (o es el `default` implícito).
- La config define qué modelo usa, dónde vive su workspace, si corre en sandbox, qué tools tiene disponibles.


- ---


## 2.2 Agente, Sesión Main y Sub-Agentes

- OpenClaw usa el término "agente" en tres contextos distintos.
- Confundirlos lleva a decisiones de diseño incorrectas — sobre todo al configurar tools, bootstrap files y sesiones.


### Los tres conceptos

| Concepto | Qué es | Session key | Persistencia |
|----------|--------|-------------|-------------|
| **Agente** | Unidad declarada en `agents.list[]` con workspace, auth y config propios | — | Permanente (disco) |
| **Sesión main** | La sesión DM del agente — donde conversa directamente con el usuario | `agent:<id>:main` | Long-lived (compaction automática) |
| **Sub-agente** | Worker temporal spawneado para ejecutar una tarea en background | `agent:<id>:subagent:<uuid>` | Efímero (auto-archived) |

### Agente: la unidad declarada

- Un **agente** es todo lo descrito en §2.1: workspace + agentDir + config + identity runtime.
- Cada entrada en `agents.list[]` declara un agente distinto:


```json5
{
  agents: {
    list: [
      { id: "main", default: true, workspace: "~/clawd" },
      { id: "work", workspace: "~/.openclaw/workspace-work" },
      { id: "family", workspace: "~/.openclaw/workspace-family" }
    ]
  }
}
```

- Cada agente tiene **su propio** workspace (personalidad, memoria), agentDir (credenciales, sesiones) y configuración de tools/sandbox.
- Las credenciales NO se comparten entre agentes — un agente comprometido no expone las API keys de otro.


- **Default agent:** El agente marcado con `default: true` (o el primero de la lista si ninguno lo tiene) recibe los mensajes que no matchean ningún binding explícito.
- En un setup single-agent, el default es el único agente.


- **Multi-agent:** Cuando hay varios agentes, **bindings** en openclaw.json enrutan mensajes al agente correcto según canal, peer, guild o account.
- Ver [Capítulo 6 — Multi-Agent Routing](06-multi-agent-routing.md).


### Sesión main: el canal DM del agente

- Cada agente tiene una **sesión principal** (main) que es el canal directo de comunicación con el usuario:


```
Session key: agent:<agentId>:main
Ejemplo:     agent:main:main
```

- Esta sesión es especial por cuatro razones:


1. **Recibe todos los DMs** de todos los canales (Telegram, WhatsApp, Webchat) — a menos que `session.dmScope` cambie la agrupación.
2. **Inyecta todos los bootstrap files** — los 7 archivos (AGENTS.md, SOUL.md, USER.md, IDENTITY.md, TOOLS.md, HEARTBEAT.md, MEMORY.md).
3. **Es el único contexto donde se inyecta MEMORY.md** — por diseño de privacidad; en grupos o sesiones compartidas, MEMORY.md no se carga.
4. **Es persistente** — acumula historial, se compacta automáticamente, sobrevive entre mensajes y reinicios del gateway.

- La sesión main no es la única sesión de un agente.
- Cada grupo, canal o thread genera su propia sesión:


```
agent:main:main                          ← DM (sesión main)
agent:main:telegram:group:-100123456     ← Grupo Telegram
agent:main:whatsapp:group:456@g.us       ← Grupo WhatsApp
agent:main:discord:guild:789:channel:101 ← Canal Discord
```

- **`session.dmScope`** controla cómo se agrupan los DMs:


| Valor | Comportamiento | Session key |
|-------|---------------|-------------|
| `"main"` (default) | Todos los DMs → una sesión única | `agent:<id>:main` |
| `"per-peer"` | Una sesión por persona (aisladas) | `agent:<id>:dm:<peerId>` |
| `"per-channel-peer"` | Una sesión por persona por canal | `agent:<id>:telegram:<peerId>` |
| `"per-account-channel-peer"` | Máximo aislamiento | `agent:<id>:<accountId>:<channel>:<peerId>` |

### Sub-agente: worker temporal y aislado

- Un **sub-agente** es un run de background spawneado por un agente (o por otro sub-agente, si la profundidad lo permite). **No** es un agente independiente — vive dentro del árbol de sesiones de su padre y comparte su workspace.


```
Agente "main"
├── agent:main:main                    ← sesión main (profundidad 0)
│   └── spawns:
│       ├── agent:main:subagent:uuid-1 ← sub-agente (profundidad 1)
│       └── agent:main:subagent:uuid-2 ← sub-agente (profundidad 1)
│           └── spawns:                   (solo si maxSpawnDepth ≥ 2)
│               └── agent:main:subagent:uuid-2:subagent:uuid-3  ← profundidad 2
```

- **Spawn** — vía tool `sessions_spawn` o comando `/subagents spawn`:


```json5
// Tool call desde el agente principal
sessions_spawn({
  task: "Investiga las últimas actualizaciones de KODA y resume hallazgos",
  model: "anthropic/claude-sonnet-4-6",    // opcional, hereda del padre
  thinking: "medium",                       // opcional
  runTimeoutSeconds: 300,                   // timeout del run
  cleanup: "keep"                           // "keep" o "delete"
})
// Retorna inmediato: { status: "accepted", runId, childSessionKey }
```

- **Ciclo de vida completo:**


```
1. SPAWN → no-bloqueante, retorna { runId, childSessionKey }
       │
2. EJECUCIÓN → corre en sesión propia, ventana de contexto aislada
       │         ve solo AGENTS.md + TOOLS.md como bootstrap
       │         accede al mismo workspace (memory_search, read, etc.)
       │
3. ANNOUNCE → al terminar, genera resumen (prompt especial de announce)
       │         el resumen se entrega al canal del requester
       │
4. ARCHIVE → después de archiveAfterMinutes (default 60), la sesión se borra
```

### Qué ve cada uno

- Esta tabla es fundamental para diseñar bootstrap files y entender por qué sub-agentes son "lean by design":


| Aspecto | Sesión main | Sub-agente | Sesión de grupo |
|---------|-------------|------------|-----------------|
| **AGENTS.md** | ✅ | ✅ | ✅ |
| **TOOLS.md** | ✅ | ✅ | ✅ |
| **SOUL.md** | ✅ | ❌ | ✅ |
| **USER.md** | ✅ | ❌ | ✅ |
| **IDENTITY.md** | ✅ | ❌ | ✅ |
| **HEARTBEAT.md** | ✅ | ❌ | ❌ (solo heartbeats) |
| **MEMORY.md** | ✅ | ❌ | ❌ |
| **memory_search** | ✅ | ✅ (mismo workspace) | ✅ |
| **Tools de sesión** | ✅ todos | ❌ (excepto orchestrators) | ✅ |
| **Persistencia** | Long-lived, compaction | One-shot, auto-archived | Long-lived |
| **Heartbeats** | ✅ (si configurado) | ❌ | ❌ |

- **Implicación directa para AGENTS.md y TOOLS.md:** Dado que son los únicos bootstrap files que un sub-agente recibe, deben contener todas las instrucciones operativas que un worker necesita (convenciones, reglas de memoria, restricciones).
- Las instrucciones de personalidad (SOUL.md) o contexto del usuario (USER.md) no están disponibles — si un sub-agente necesita ese contexto, debe pasarse en el `task` del spawn.


### Profundidad y límites de spawn

```json5
{
  agents: {
    defaults: {
      subagents: {
        maxSpawnDepth: 1,         // 1 = sub-agentes simples (sin nesting)
                                  // 2 = patrón orchestrator → workers
        maxChildrenPerAgent: 5,   // Máximo hijos activos por sesión
        maxConcurrent: 8,         // Cap global de sub-agentes concurrentes
        archiveAfterMinutes: 60   // Auto-cleanup post-announce
      }
    }
  }
}
```

- La profundidad se calcula contando los segmentos `:subagent:` en el session key:


| Profundidad | Session key | Rol | ¿Puede spawnear? |
|-------------|-------------|-----|-------------------|
| 0 | `agent:main:main` | Agente principal | Siempre |
| 1 | `agent:main:subagent:<uuid>` | Sub-agente (leaf o orchestrator) | Solo si `maxSpawnDepth ≥ 2` |
| 2 | `...:subagent:<uuid>:subagent:<uuid>` | Worker leaf | Nunca |

- **Patrón orchestrator** (`maxSpawnDepth:
- 2`):
- Un sub-agente de profundidad 1 actúa como coordinador — recibe los tools de sesión (`sessions_spawn`, `subagents`, `sessions_list`, `sessions_history`) y puede spawnear workers de profundidad 2, que ya son hojas terminales sin capacidad de spawn.


### Tool policy para sub-agentes

- Los sub-agentes heredan la tool policy del agente padre con una capa adicional de restricción:


```json5
{
  tools: {
    subagents: {
      tools: {
        deny: ["gateway", "cron"],  // Sub-agentes no pueden modificar el gateway ni crear cron jobs
        // allow: ["read", "exec"]  // Alternativamente, allowlist explícito
      }
    }
  }
}
```

- Esta es la Layer 8 de la tool policy (ver §2.7).
- Aplica **después** de todas las demás capas — solo puede restringir más, nunca re-habilitar un tool denegado en capas anteriores.


### Cuándo usar sub-agentes

| Situación | ¿Sub-agente? | Por qué |
|-----------|-------------|---------|
| Tarea larga (>5 min) que puede correr sin supervisión | ✅ | No bloquea la conversación |
| Investigación que necesita contexto limpio | ✅ | Ventana de contexto propia, sin historial previo |
| Tareas paralelas independientes | ✅ | Múltiples sub-agentes concurrentes |
| Tarea que necesita personalidad completa del agente | ❌ | Solo ve AGENTS.md + TOOLS.md |
| Interacción iterativa con el usuario | ❌ | No tiene acceso al canal |
| Tarea trivial (<1 min) | ❌ | Overhead de spawn > beneficio |

### Resumen visual

```
┌──────────────────────────────────────────────────────────────────┐
│                     GATEWAY (openclaw.json)                       │
│                                                                   │
│  agents.list[]                                                    │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  AGENTE "main" (default)                                   │  │
│  │  workspace: ~/clawd                                        │  │
│  │  ┌─────────────────────────────────┐                       │  │
│  │  │ SESIÓN MAIN (agent:main:main)   │ ← todos los DMs      │  │
│  │  │ • 7 bootstrap files inyectados  │                       │  │
│  │  │ • tools completos               │                       │  │
│  │  │ • persistente, compaction auto  │                       │  │
│  │  │                                 │                       │  │
│  │  │  spawns ──► SUB-AGENTE (uuid-1) │                       │  │
│  │  │             • AGENTS.md + TOOLS │                       │  │
│  │  │             • tools restringidos│                       │  │
│  │  │             • efímero           │                       │  │
│  │  │             • announce → main   │                       │  │
│  │  │                                 │                       │  │
│  │  │  spawns ──► SUB-AGENTE (uuid-2) │                       │  │
│  │  │             • ...               │                       │  │
│  │  └─────────────────────────────────┘                       │  │
│  │  ┌─────────────────────────────────┐                       │  │
│  │  │ SESIÓN GRUPO (telegram:group:X) │                       │  │
│  │  │ • sin MEMORY.md ni HEARTBEAT.md │                       │  │
│  │  └─────────────────────────────────┘                       │  │
│  └────────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │  AGENTE "work"                                             │  │
│  │  workspace: ~/.openclaw/workspace-work                     │  │
│  │  (workspace, auth, sesiones completamente independientes)  │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

- ---


## 2.3 Workspace Contract: Los Bootstrap Files

- El workspace contiene los **bootstrap files** — archivos Markdown que definen al agente y se inyectan en cada turn del system prompt.
- Son el contrato entre tú (el operador) y el agente.


### Mapa de bootstrap files

| Archivo | Inyectado en | Propósito | Guía de contenido |
|---------|-------------|-----------|-------------------|
| **AGENTS.md** | Main + Sub-agentes | Instrucciones operativas, reglas, convenciones, cómo usar memoria | Reglas que el agente debe seguir SIEMPRE. Estilo imperativo. |
| **SOUL.md** | Solo Main | Personalidad, tono, boundaries, contrato de comunicación | Define QUIÉN es el agente. Estilo descriptivo/narrativo. |
| **USER.md** | Solo Main | Perfil del usuario: roles, rutina, preferencias, modelo de decisiones | Lo que el agente necesita saber sobre TI. |
| **IDENTITY.md** | Solo Main | Nombre del agente, vibe, emoji, infraestructura donde corre | Tarjeta de identidad. Breve. |
| **TOOLS.md** | Main + Sub-agentes | Notas locales sobre herramientas, comandos, troubleshooting | Cheat sheet operativo. NO controla qué tools están disponibles. |
| **HEARTBEAT.md** | Solo Main | Checklist para heartbeats periódicos | Pequeño. Se lee en cada heartbeat → optimizar tokens. |
| **BOOTSTRAP.md** | Solo Main (una vez) | Ritual de primer arranque. Se borra después. | Auto-destrucción after setup. |
| **MEMORY.md** | Solo Main | Memoria curada de largo plazo | Hechos durables, decisiones, historial. Crece con el tiempo. |

### Reglas de diseño para bootstrap files

- **1.
- Todo lo inyectado se paga en cada turn.**


- Si AGENTS.md tiene 5,000 chars (~1,250 tokens) y el agente hace 20 turns en una sesión, esos 1,250 tokens se envían 20 veces al modelo.
- No se cobran 20 veces (prompt caching ayuda), pero sí cuentan contra la ventana de contexto y contra el cache write cuando se invalida.


- **2.
- Sub-agentes solo reciben AGENTS.md + TOOLS.md.**


- Esto es una decisión de diseño deliberada: los sub-agentes son workers aislados.
- No necesitan saber quién eres (USER.md), cómo se llama el agente principal (IDENTITY.md), ni su personalidad (SOUL.md).
- Si un sub-agente necesita contexto específico, se pasa en el `task` del spawn.


- **3.
- MEMORY.md solo se inyecta en sesión main (privada).**


- Nunca en grupos, nunca en sesiones compartidas.
- Contiene información personal que no debe filtrarse a otros participantes.
- Los daily logs (`memory/*.md`) no se inyectan nunca — se acceden on-demand via `memory_search` y `memory_get`.


- **4.
- Archivos faltantes no rompen nada.**


- Si un bootstrap file no existe, OpenClaw inyecta un marcador `[MISSING]` y continúa.
- Esto permite bootstraps incrementales.


- **5.
- Truncation es silenciosa.**


- Si un archivo excede `bootstrapMaxChars` (default 20,000), se trunca con un marcador `[...truncated]`.
- El agente no se entera de qué se perdió.
- Implicación: si tu TOOLS.md tiene 50KB de notas, el modelo solo ve los primeros ~20KB.


### Anti-patrones comunes

| Anti-patrón | Por qué es malo | Qué hacer |
|-------------|-----------------|-----------|
| MEMORY.md de 30KB | Se trunca a 20KB; 5,000+ tokens en cada turn | Mover detalles a daily logs; MEMORY.md = solo facts durables |
| TOOLS.md con historial completo de troubleshooting | Se trunca; tokens desperdiciados | Mover a `cabinet/docs/`; solo dejar cheat sheet |
| Instrucciones duplicadas en AGENTS.md y SOUL.md | Tokens desperdiciados, posibles contradicciones | AGENTS.md = reglas operativas; SOUL.md = personalidad |
| Datos sensibles en HEARTBEAT.md | Se inyecta en el prompt periódicamente | Nunca API keys, passwords, ni PII en HEARTBEAT.md |
| AGENTS.md con 10KB de instrucciones detalladas | Overhead en cada turn | Mover instrucciones situacionales a skills |

- ---


## 2.4 Ciclo de Vida de un Agente

- Un agente no es un proceso — es state en disco que se activa cuando llega un mensaje.
- Su ciclo de vida tiene cuatro fases:


### Fase 1: Bootstrap (una sola vez)

```
openclaw onboard / openclaw setup
         │
         ▼
  Crear workspace + bootstrap files
  Crear agentDir + auth-profiles.json
  Si BOOTSTRAP.md existe → el primer run lo ejecuta
  BOOTSTRAP.md se borra → nunca más
```

- El agente "nace" cuando su workspace se crea y sus bootstrap files se pueblan. `BOOTSTRAP.md` es el ritual de primer arranque — el agente lo lee, ejecuta las instrucciones (definir nombre, personalidad), y lo borra.


### Fase 2: Sesiones (ciclo continuo)

```
Mensaje inbound
      │
      ▼
  ¿Sesión existe?
  ├── SÍ → Cargar transcript JSONL + metadata
  │        Reusar skills snapshot (a menos que haya refresh)
  │        Continuar conversación
  │
  └── NO → Crear sesión nueva
           Generar sessionId
           Crear JSONL vacío
           Snapshot de skills elegibles
           Primera inyección de bootstrap files
```

- Cada sesión tiene:


- **Session Key**: identificador estable (e.g. `agent:main:main`, `agent:main:telegram:7192195698`)
- **Session ID**: UUID que cambia con cada `/new` o `/reset` (mismo key, nuevo ID)
- **Transcript**: archivo JSONL con toda la conversación
- **Metadata**: en `sessions.json` — modelo, último canal, timestamps, compaction count

### Fase 3: Compaction (mantenimiento automático)

```
Sesión larga → contexto crece → se acerca al límite
      │
      ▼
  Memory flush (turn silencioso)
  → El modelo escribe notas durables a memory/*.md
      │
      ▼
  Compaction
  → El modelo resume la conversación antigua
  → Summary se persiste en JSONL
  → Mensajes antiguos se reemplazan por el summary
  → Request original se reintenta con contexto compactado
```

- La compaction es transparente para el usuario.
- El agente no "olvida" — resume.
- Pero la calidad del resumen depende del modelo: detalles finos se pueden perder.
- Por eso el memory flush es importante: antes de compactar, el agente tiene la oportunidad de escribir lo importante a disco.


### Fase 4: Memoria (acumulación y curación)

```
Daily logs (memory/YYYY-MM-DD.md)
├── Se escriben durante sesiones (por instrucción o automáticamente)
├── Acceso on-demand via memory_search / memory_get
├── Indexados por vector search (embeddings) + BM25
└── No cuentan contra context window hasta que se leen

MEMORY.md (curado)
├── Actualizado periódicamente (manual o durante heartbeats)
├── Inyectado en cada turn de sesión main
├── Datos que el agente necesita siempre: quién es el usuario,
│   proyectos activos, decisiones, preferencias
└── Tradeoff: más contenido = más tokens por turn
```

### Reset vs Continuidad

| Acción | Efecto en sesión | Efecto en memoria |
|--------|-----------------|-------------------|
| `/new` o `/reset` | Nuevo sessionId, transcript limpio | Sin efecto (memory files intactos) |
| `/compact` | Misma sesión, historial resumido | Sin efecto |
| Compaction auto | Igual que `/compact` | Memory flush pre-compaction |
| Borrar workspace | — | **Pérdida total de personalidad y memoria** |

- El agente sobrevive resets porque su identidad está en los bootstrap files y su memoria en los memory files.
- Lo que se pierde con cada reset es el **contexto conversacional** — la sesión activa.


- ---


## 2.5 Skills: Capacidades On-Demand

- Los skills son **instrucciones empaquetadas** que el modelo carga bajo demanda.
- NO son plugins ni código ejecutable — son Markdown con metadatos que le dicen al modelo qué hacer y cómo hacerlo.


### Arquitectura de skills

```
                        ┌─────────────────────┐
                        │   System Prompt      │
                        │                      │
                        │   <available_skills> │
                        │     • skill-A        │
   Inyectado siempre ──►│       name + desc   │
   (solo metadatos)     │       + location     │
                        │     • skill-B        │
                        │       ...            │
                        │   </available_skills>│
                        └──────────┬───────────┘
                                   │
                           El modelo decide
                           "necesito skill-A"
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   read(SKILL.md)     │
   Cargado on-demand ──►│                      │
   (solo cuando se usa) │   Instrucciones      │
                        │   completas del      │
                        │   skill              │
                        └─────────────────────┘
```

### Precedencia (resolución de conflictos por nombre)

```
Workspace skills      (mayor precedencia)
  <workspace>/skills/my-skill/SKILL.md
       ▼ overrides
Managed skills
  ~/.openclaw/skills/my-skill/SKILL.md
       ▼ overrides
Bundled skills
  <openclaw>/dist/skills/bundled/my-skill/SKILL.md
       ▼ overrides
Extra dirs
  skills.load.extraDirs[]/my-skill/SKILL.md
```

- Si tienes un skill `weather` bundled y creas uno en tu workspace con el mismo nombre, el del workspace gana.


### Gating: cuándo un skill es elegible

- OpenClaw filtra skills **al cargar la sesión** (no en cada turn).
- Un skill es elegible si:


| Gate | Campo en SKILL.md frontmatter | Ejemplo |
|------|-------------------------------|---------|
| **Binarios requeridos** | `requires.bins: ["uv"]` | Solo si `uv` está en PATH del host |
| **Al menos uno** | `requires.anyBins: ["gemini", "claude"]` | Si al menos uno está en PATH |
| **Variables de entorno** | `requires.env: ["GEMINI_API_KEY"]` | Si la env var existe o está en config |
| **Config truthy** | `requires.config: ["browser.enabled"]` | Si ese path en openclaw.json es truthy |
| **OS** | `os: ["darwin", "linux"]` | Solo en esos sistemas operativos |
| **Siempre** | `always: true` | Bypass de todos los gates |
| **Deshabilitado** | `skills.entries.name.enabled: false` | Explícitamente desactivado en config |

### Costo en tokens

- Cada skill elegible agrega al system prompt:


```
~97 chars base + len(nombre) + len(descripción) + len(ruta) ≈ 150-400 chars por skill
```

- Con 12 skills elegibles → ~2,000-4,800 chars → ~500-1,200 tokens.
- Es significativo pero no catastrófico.
- El costo real viene cuando el modelo hace `read` del SKILL.md — esos contenidos entran al historial de la sesión.


### Skills snapshot y hot reload

- El snapshot de skills elegibles se toma **al inicio de la sesión** y se reutiliza en turns posteriores.
- Si cambias un SKILL.md, el **watcher** puede refrescar el snapshot en el próximo turn (sin reiniciar el gateway).
- Si un nodo macOS se conecta y trae skills macOS-only, esos skills se agregan al snapshot.

### Skills vs Plugins: la distinción clave

| | Skills | Plugins |
|--|--------|---------|
| **Qué son** | Markdown con instrucciones | Código TypeScript ejecutable |
| **Quién los ejecuta** | El modelo (via tools existentes) | El gateway (in-process) |
| **Qué pueden hacer** | Guiar al modelo para usar tools (exec, browser, etc.) | Registrar nuevos tools, RPCs, HTTP handlers, CLI commands |
| **Aislamiento** | No ejecutan código propio | Corren en el proceso del gateway |
| **Riesgo** | Bajo (solo texto) | Alto (código arbitrario in-process) |
| **Distribución** | ClawHub, workspace, managed | npm packages |

- **Regla:** Si necesitas enseñarle al modelo a usar una herramienta existente → Skill.
- Si necesitas crear una herramienta nueva o extender el gateway → Plugin.


- ---


## 2.6 Tools: La Surface de Acción del Agente

- Los tools son **las manos del agente** — las acciones concretas que puede ejecutar.
- OpenClaw tiene tres fuentes de tools:


### Fuentes de tools

```
┌─────────────────────────────────────────────────────┐
│                TOOLS DISPONIBLES                     │
│                                                      │
│  1. BUILT-IN (siempre disponibles, controlados       │
│     por tool policy)                                 │
│     • read, write, edit, apply_patch                 │
│     • exec, process (bash)                           │
│     • browser, canvas                                │
│     • message (Telegram, WhatsApp, etc.)             │
│     • web_search, web_fetch                          │
│     • memory_search, memory_get                      │
│     • sessions_list, sessions_history,               │
│       sessions_send, sessions_spawn                  │
│     • session_status, subagents                      │
│     • nodes, image, tts                              │
│     • cron, gateway (control plane)                  │
│     • agents_list                                    │
│                                                      │
│  2. PLUGIN TOOLS (registrados por plugins)           │
│     • lobster (workflows)                            │
│     • llm-task (JSON-only LLM steps)                 │
│     • voice-call (llamadas)                          │
│     • (cualquier plugin puede registrar tools)       │
│                                                      │
│  3. SKILL-TAUGHT (no son tools nuevos — los skills   │
│     enseñan al modelo a usar los built-in y plugins  │
│     de formas específicas)                           │
└─────────────────────────────────────────────────────┘
```

### El costo invisible: tool schemas

- Cada tool disponible tiene un **JSON Schema** que se envía al modelo para que sepa cómo llamarlo.
- Este schema consume tokens aunque nunca lo veas en el prompt como texto.


- Algunos ejemplos de costo:


| Tool | Schema size (chars) | ~Tokens |
|------|-------------------|---------|
| `browser` | ~9,800 | ~2,450 |
| `exec` | ~6,200 | ~1,560 |
| `nodes` | ~4,500 | ~1,125 |
| `message` | ~3,800 | ~950 |
| `read` | ~800 | ~200 |
| `write` | ~600 | ~150 |

- Si tienes 15 tools activos, los schemas pueden sumar 30,000+ chars → ~7,500 tokens.
- Eso es **más que muchos bootstrap files**. `/context detail` desglosa esto por tool.


### Implicación para diseño

- **Cada tool que habilitas cuesta tokens.** Si un agente es "messaging-only" (solo envía mensajes, no necesita browser ni exec), restringir sus tools no es solo seguridad — es eficiencia de contexto.


- ---


## 2.7 Tool Policy: Quién Puede Hacer Qué

- La tool policy es el sistema de permisos que controla qué tools están disponibles para cada agente, en cada contexto.
- Es **el mecanismo de seguridad más importante** después de los channel allowlists.


### Capas de filtrado (en orden de evaluación)

```
Mensaje inbound
      │
      ▼
Layer 1: TOOL PROFILE
   tools.profile (global) o agents.list[].tools.profile (per-agent)
   Presets: minimal | coding | messaging | full
   Define la base allowlist
      │
      ▼
Layer 2: PROVIDER TOOL PROFILE
   tools.byProvider[provider].profile
   Puede restringir tools por provider/modelo
      │
      ▼
Layer 3: GLOBAL TOOL POLICY
   tools.allow / tools.deny
   allow = allowlist (si no vacío, todo lo demás bloqueado)
   deny = denylist (siempre gana sobre allow)
      │
      ▼
Layer 4: PROVIDER TOOL POLICY
   tools.byProvider[provider].allow / .deny
   Más restricciones por provider/modelo
      │
      ▼
Layer 5: AGENT TOOL POLICY
   agents.list[].tools.allow / .deny
   Per-agent overrides
      │
      ▼
Layer 6: AGENT PROVIDER POLICY
   agents.list[].tools.byProvider[provider].allow / .deny
      │
      ▼
Layer 7: SANDBOX TOOL POLICY
   tools.sandbox.tools.allow / .deny  (o agents.list[].tools.sandbox.tools.*)
   Solo aplica cuando el agente corre en sandbox
      │
      ▼
Layer 8: SUBAGENT TOOL POLICY
   tools.subagents.tools.deny / .allow
   Solo aplica a sub-agentes
      │
      ▼
  TOOLS FINALES DISPONIBLES PARA ESTE RUN
```

### Regla cardinal: deny siempre gana

- En cualquier capa, si un tool está en `deny`, queda bloqueado permanentemente.
- Las capas posteriores **solo pueden restringir más**, nunca re-habilitar un tool denegado en una capa anterior.


### Tool Groups (shorthands)

- En lugar de listar tools individuales, puedes usar grupos:


| Grupo | Se expande a |
|-------|-------------|
| `group:runtime` | `exec`, `bash`, `process` |
| `group:fs` | `read`, `write`, `edit`, `apply_patch` |
| `group:sessions` | `sessions_list`, `sessions_history`, `sessions_send`, `sessions_spawn`, `session_status` |
| `group:memory` | `memory_search`, `memory_get` |
| `group:ui` | `browser`, `canvas` |
| `group:automation` | `cron`, `gateway` |
| `group:messaging` | `message` |
| `group:nodes` | `nodes` |
| `group:openclaw` | Todos los tools built-in (excluye plugins) |

### Tool Profiles (presets)

- Los profiles son atajos para configuraciones comunes:


| Profile | Tools incluidos | Caso de uso |
|---------|----------------|-------------|
| `minimal` | Solo `session_status` | Agentes que solo conversan, sin tools |
| `coding` | `group:fs`, `group:runtime`, `group:sessions`, `group:memory`, `image` | Agentes de desarrollo |
| `messaging` | `group:messaging`, `sessions_list`, `sessions_history`, `sessions_send`, `session_status` | Agentes de comunicación |
| `full` | Sin restricción (todos los tools) | Agentes con acceso total |

### Elevated Mode: el escape hatch

- Cuando un agente corre en sandbox (Docker), `exec` ejecuta dentro del container. **Elevated mode** es el mecanismo para escapar al host:


```
                Normal (sandboxed)         Elevated (host)
                ──────────────────         ───────────────
exec            → Docker container         → Gateway host
Disponible      Siempre (si tool          Solo si:
                no está denied)            • tools.elevated.enabled = true
                                           • Sender en allowFrom
                                           • Per-agent gate pasa
Modos           —                          on/ask: host + approvals
                                           full: host + auto-approve
                                           off: vuelve al sandbox
```

- **¿Cuándo usar elevated?**


- Un agente sandboxed necesita instalar algo en el host
- Un agente sandboxed necesita acceder a un servicio local del host
- Debugging / troubleshooting del host desde un agente sandboxed

- **¿Cuándo NO usar?**


- Si el agente no está sandboxed (ya corre en el host — elevated es no-op)
- Para tareas rutinarias (mejor montar los paths necesarios como bind mounts)

### Patrones de configuración comunes

#### Agente personal con acceso total (sin sandbox)

```json5
{
  agents: {
    list: [{
      id: "main",
      default: true,
      sandbox: { mode: "off" }
      // tools: sin restricciones (full por defecto)
    }]
  }
}
```

#### Agente familiar: sandbox + read-only

```json5
{
  agents: {
    list: [{
      id: "family",
      workspace: "~/.openclaw/workspace-family",
      sandbox: { mode: "all", scope: "agent", workspaceAccess: "ro" },
      tools: {
        allow: ["read", "group:memory", "group:messaging"],
        deny: ["exec", "write", "edit", "apply_patch", "browser", "cron", "gateway"]
      }
    }]
  }
}
```

#### Agente público: sin filesystem, solo messaging

```json5
{
  agents: {
    list: [{
      id: "public",
      sandbox: { mode: "all", scope: "agent", workspaceAccess: "none" },
      tools: {
        profile: "messaging",
        sessions: { visibility: "tree" },
        deny: ["group:fs", "group:runtime", "group:ui", "group:nodes",
               "group:automation", "image"]
      }
    }]
  }
}
```

#### Coding agent con tools por provider

```json5
{
  tools: {
    profile: "coding",
    byProvider: {
      "anthropic/claude-sonnet-4-6": {
        // Sonnet puede usar browser
      },
      "moonshot/kimi-k2.5": {
        deny: ["browser", "canvas"]  // Kimi no maneja browser bien
      }
    }
  }
}
```

### Debugging: ¿por qué este tool está bloqueado?

```bash
openclaw sandbox explain
openclaw sandbox explain --agent family
openclaw sandbox explain --session agent:family:whatsapp:+1234567890
```

- Este comando muestra la policy resuelta: qué tools están disponibles, cuáles bloqueados, y en qué capa se bloquearon.


- ---


## 2.8 Skills + Tools + Plugins: El Modelo Mental Integrado

- Estos tres conceptos son ortogonales pero se complementan:


```
┌──────────────────────────────────────────────────────────────┐
│                     MODELO DE IA                              │
│                                                               │
│  Ve en su system prompt:                                      │
│  ┌──────────┐  ┌──────────────┐  ┌────────────────────────┐  │
│  │ Tool      │  │ Skills       │  │ Bootstrap files        │  │
│  │ Schemas   │  │ List         │  │ (AGENTS.md, etc.)      │  │
│  │ (JSON)    │  │ (XML)        │  │ (Markdown)             │  │
│  │           │  │              │  │                        │  │
│  │ "Qué      │  │ "Qué        │  │ "Quién soy, cómo      │  │
│  │  puedo    │  │  instruccio- │  │  comportarme, quién    │  │
│  │  hacer"   │  │  nes puedo   │  │  es mi usuario"        │  │
│  │           │  │  cargar"     │  │                        │  │
│  └──────────┘  └──────────────┘  └────────────────────────┘  │
│                                                               │
│  Cuando el modelo necesita actuar:                            │
│                                                               │
│  1. Lee el skill relevante (read SKILL.md) ← instrucciones   │
│  2. Llama un tool (exec, browser, etc.)    ← acción          │
│  3. El gateway ejecuta (host o sandbox)    ← runtime         │
│  4. Resultado vuelve al modelo             ← feedback        │
│                                                               │
│  Plugins extienden el gateway:                                │
│  • Registran nuevos tools (lobster, llm-task, voice-call)     │
│  • Registran nuevos RPCs y HTTP handlers                      │
│  • Pueden traer sus propios skills                            │
└──────────────────────────────────────────────────────────────┘
```

### Cómo fluye la decisión

```
Usuario pide: "genera una imagen con Gemini"
      │
      ▼
Modelo busca en skills list → encuentra "nano-banana-pro"
      │
      ▼
Modelo hace read("/path/to/nano-banana-pro/SKILL.md")
      │
      ▼
SKILL.md dice: "usa exec para correr el script generate.py con estos params..."
      │
      ▼
Modelo hace tool call: exec({ command: "python generate.py ..." })
      │
      ▼
Gateway ejecuta el comando (host o sandbox según policy)
      │
      ▼
Resultado vuelve al modelo → modelo procesa y responde
```

### Tabla de responsabilidades

| Capa | Responsable de | Ejemplo |
|------|---------------|---------|
| **Bootstrap files** | Identidad, reglas, contexto permanente | "Soy Korax, respondo en español, sigo estas convenciones..." |
| **Skills** | Instrucciones específicas para tareas | "Para generar imágenes, corre este script con estos parámetros..." |
| **Tools** | Ejecución de acciones atómicas | exec(), read(), browser.navigate(), message.send() |
| **Tool Policy** | Permisos y seguridad | "Este agente no puede usar exec ni browser" |
| **Plugins** | Extensión del gateway con nuevas capacidades | Nuevo tool `lobster` para workflows, nuevo channel `matrix` |
| **Sandbox** | Aislamiento de ejecución | Tools corren en Docker en vez del host |

- ---


## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Workspace = hogar versionable** | Backup via git, migración entre hosts, recuperabilidad |
| **Agente ≠ sesión main ≠ sub-agente** | Cada scope tiene contexto, tools y lifecycle distintos; claridad en diseño multi-agent |
| **AgentDir = credenciales aisladas** | Auth per-agent, no shared credentials, seguridad por defecto |
| **Bootstrap files inyectados** | Personalidad persistente sin necesidad de memoria conversacional |
| **Sub-agentes solo ven AGENTS.md + TOOLS.md** | Contexto lean, cost-efficient, sin leak de info personal |
| **MEMORY.md solo en main** | Privacy by default en grupos y sesiones compartidas |
| **Skills = instrucciones lazy-loaded** | System prompt lean; costo de tokens solo cuando se usa |
| **Tool schemas = costo invisible** | Menos tools habilitados = menos tokens por turn |
| **Tool policy = 8 capas, deny gana** | Seguridad en profundidad, granularidad per-agent/provider |
| **Elevated = escape hatch explícito** | Balance sandbox↔utilidad sin comprometer el modelo de seguridad |
| **Plugins ≠ skills** | Skills = texto, bajo riesgo. Plugins = código, alto riesgo. Separación clara. |

- ---


- *Siguiente: [Capítulo 3 — Sesiones](03-sesiones.md)*


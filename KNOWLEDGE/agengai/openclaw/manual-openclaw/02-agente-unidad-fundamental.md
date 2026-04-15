---
_manifest:
  urn: urn:agengai:kb:02-agente-unidad-fundamental
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '02'
- agente
- unidad
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:02-agente-unidad-fundamental
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
│ ├── AGENTS.md, SOUL.md, USER.md, IDENTITY.md ← personalidad
│ ├── TOOLS.md, HEARTBEAT.md ← operaciones
│ ├── MEMORY.md ← memoria curada
│ ├── memory/YYYY-MM-DD.md ← logs diarios
│ ├── skills/ ← skills custom
│ └── ... ← scripts, projects, etc.
│
├── 2. AGENT DIR (~/.openclaw/agents/<agentId>/)
│ ├── agent/
│ │ └── auth-profiles.json ← API keys + OAuth tokens
│ ├── sessions/
│ │ ├── sessions.json ← metadata de todas las sesiones
│ │ └── *.jsonl ← transcripts de cada sesión
│ └── qmd/ (opcional)
│ └── (QMD sidecar state)
│
├── 3. CONFIG (referencia en openclaw.json)
│ └── agents.list[].{id, workspace, sandbox, tools, heartbeat, ...}
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

- **Runtime real:** OpenClaw reutiliza piezas de `pi-mono` para modelos y tools, pero **session management, discovery y tool wiring son OpenClaw-owned**.
- No consulta `~/.pi/agent` ni `<workspace>/.pi`.
- La verdad operativa vive en `openclaw.json`, el workspace del agente y su `agentDir`.

- ---

## 2.2 Agente, Sesión Main y Sub-Agentes

- OpenClaw usa el término "agente" en tres contextos distintos.
- Confundirlos lleva a decisiones de diseño incorrectas — sobre todo al configurar tools, bootstrap files y sesiones.

## Los tres conceptos

| Concepto | Qué es | Session key | Persistencia |
|----------|--------|-------------|-------------|
| **Agente** | Unidad declarada en `agents.list[]` con workspace, auth y config propios | — | Permanente (disco) |
| **Sesión main** | La sesión DM del agente — donde conversa directamente con el usuario | `agent:<id>:main` | Long-lived (compaction automática) |
| **Sub-agente** | Worker temporal spawneado para ejecutar una tarea en background | `agent:<id>:subagent:<uuid>` | Efímero (auto-archived) |

## Agente: la unidad declarada

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

## Sesión main: el canal DM del agente

- Cada agente tiene una **sesión principal** (main) que es el canal directo de comunicación con el usuario:

```
Session key: agent:<agentId>:main
Ejemplo: agent:main:main
```

- Esta sesión es especial por cuatro razones:

1. **Recibe todos los DMs** de todos los canales (Telegram, WhatsApp, Webchat) — a menos que `session.dmScope` cambie la agrupación.
2. **Inyecta todos los bootstrap files** — los 7 archivos (AGENTS.md, SOUL.md, USER.md, IDENTITY.md, TOOLS.md, HEARTBEAT.md, MEMORY.md).
3. **Es el único contexto donde se inyecta MEMORY.md** — por diseño de privacidad; en grupos o sesiones compartidas, MEMORY.md no se carga.
4. **Es persistente** — acumula historial, se compacta automáticamente, sobrevive entre mensajes y reinicios del gateway.

- La sesión main no es la única sesión de un agente.
- Cada grupo, canal o thread genera su propia sesión:

```
agent:main:main ← DM (sesión main)
agent:main:telegram:group:-100123456 ← Grupo Telegram
agent:main:whatsapp:group:456@g.us ← Grupo WhatsApp
agent:main:discord:guild:789:channel:101 ← Canal Discord
```

- **`session.dmScope`** controla cómo se agrupan los DMs:

| Valor | Comportamiento | Session key |
|-------|---------------|-------------|
| `"main"` (default) | Todos los DMs → una sesión única | `agent:<id>:main` |
| `"per-peer"` | Una sesión por persona (aisladas) | `agent:<id>:direct:<peerId>` |
| `"per-channel-peer"` | Una sesión por persona por canal | `agent:<id>:telegram:<peerId>` |
| `"per-account-channel-peer"` | Máximo aislamiento | `agent:<id>:<accountId>:<channel>:<peerId>` |

## Sub-agente: worker temporal y aislado

- Un **sub-agente** es un run de background spawneado por un agente (o por otro sub-agente, si la profundidad lo permite). **No** es un agente independiente — vive dentro del árbol de sesiones de su padre y comparte su workspace.

```
Agente "main"
├── agent:main:main ← sesión main (profundidad 0)
│ └── spawns:
│ ├── agent:main:subagent:uuid-1 ← sub-agente (profundidad 1)
│ └── agent:main:subagent:uuid-2 ← sub-agente (profundidad 1)
│ └── spawns: (solo si maxSpawnDepth ≥ 2)
│ └── agent:main:subagent:uuid-2:subagent:uuid-3 ← profundidad 2
```

- **Spawn** — vía tool `sessions_spawn` o comando `/subagents spawn`:

```json5
// Tool call desde el agente principal
sessions_spawn({
 task: "Investiga las últimas actualizaciones de KODA y resume hallazgos",
 model: "anthropic/claude-sonnet-4-6", // opcional, hereda del padre
 thinking: "medium", // opcional
 runTimeoutSeconds: 300, // timeout del run
 cleanup: "keep" // "keep" o "delete"
})
// Retorna inmediato: { status: "accepted", runId, childSessionKey }
```

- **Ciclo de vida completo:**

```
1. SPAWN → no-bloqueante, retorna { runId, childSessionKey }
 │
2. EJECUCIÓN → corre en sesión propia, ventana de contexto aislada
 │ ve solo AGENTS.md + TOOLS.md como bootstrap
 │ accede al mismo workspace (memory_search, read, etc.)
 │
3. ANNOUNCE → al terminar, genera resumen (prompt especial de announce)
 │ el resumen se entrega al canal del requester
 │
4. ARCHIVE → después de archiveAfterMinutes (default 60), la sesión se borra
```

## Qué ve cada uno

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

## Profundidad y límites de spawn

```json5
{
 agents: {
 defaults: {
 subagents: {
 maxSpawnDepth: 1, // 1 = sub-agentes simples (sin nesting)
 // 2 = patrón orchestrator → workers
 maxChildrenPerAgent: 5, // Máximo hijos activos por sesión
 maxConcurrent: 8, // Cap global de sub-agentes concurrentes
 archiveAfterMinutes: 60 // Auto-cleanup post-announce
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

## Tool policy para sub-agentes

- Los sub-agentes heredan la tool policy del agente padre con una capa adicional de restricción:

```json5
{
 tools: {
 subagents: {
 tools: {
 deny: ["gateway", "cron"], // Sub-agentes no pueden modificar el gateway ni crear cron jobs
 // allow: ["read", "exec"] // Alternativamente, allowlist explícito
 }
 }
 }
}
```

- Esta es la Layer 8 de la tool policy (ver §2.7).
- Aplica **después** de todas las demás capas — solo puede restringir más, nunca re-habilitar un tool denegado en capas anteriores.

## Cuándo usar sub-agentes

| Situación | ¿Sub-agente? | Por qué |
|-----------|-------------|---------|
| Tarea larga (>5 min) que puede correr sin supervisión | ✅ | No bloquea la conversación |
| Investigación que necesita contexto limpio | ✅ | Ventana de contexto propia, sin historial previo |
| Tareas paralelas independientes | ✅ | Múltiples sub-agentes concurrentes |
| Tarea que necesita personalidad completa del agente | ❌ | Solo ve AGENTS.md + TOOLS.md |
| Interacción iterativa con el usuario | ❌ | No tiene acceso al canal |
| Tarea trivial (<1 min) | ❌ | Overhead de spawn > beneficio |

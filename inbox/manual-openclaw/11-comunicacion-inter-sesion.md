---
_manifest:
  urn: urn:kora:kb:11-comunicacion-inter-sesion
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '11'
- comunicacion
- inter
lang: es
---

# Capítulo 11 — Comunicación Inter-Sesión

> **Propósito:** Entender los mecanismos para que sesiones, agentes y procesos externos se comuniquen entre sí dentro de un gateway. Esto completa el toolkit de orquestación: Cap. 9-10 cubren delegación vertical (parent→child), este capítulo cubre comunicación horizontal (sesión↔sesión, agente↔agente, CLI→sesión).

- ---


## 11.1 Mapa de Mecanismos

```
┌─────────────────────────────────────────────────────────────────┐
│                  COMUNICACIÓN INTER-SESIÓN                       │
│                                                                  │
│  1. sessions_send        Mensaje directo a otra sesión           │
│  2. sessions_list        Descubrir sesiones existentes           │
│  3. sessions_history     Leer transcript de otra sesión          │
│  4. subagents tool       Listar, steer, kill sub-agentes        │
│  5. agent-to-agent       Messaging entre agentes diferentes     │
│  6. openclaw agent CLI   Run directo sin mensaje inbound        │
│                                                                  │
│  Cada uno tiene reglas de acceso y visibilidad diferentes       │
└─────────────────────────────────────────────────────────────────┘
```

### ¿Cuándo usar cuál?

| Necesidad | Mecanismo |
|-----------|-----------|
| Enviar resultado de un proceso a una sesión activa | `sessions_send` |
| Ver qué sesiones existen y están activas | `sessions_list` |
| Leer el historial de un sub-agente completado | `sessions_history` |
| Inyectar instrucciones en un sub-agente corriendo | `subagents(action: "steer")` |
| Que un agente "work" notifique al agente "main" | agent-to-agent |
| Trigger externo (cron del OS, script, CI/CD) | `openclaw agent` CLI |

- ---


## 11.2 sessions_send: Enviar Mensaje a Otra Sesión

### Qué hace

- Inyecta un mensaje en otra sesión como si fuera un mensaje inbound.
- Esto **trigger un agent run** en esa sesión.


```json
{
  "tool": "sessions_send",
  "params": {
    "sessionKey": "agent:main:main",
    "message": "El análisis de red está completo. Resumen: ..."
  }
}
```

- O usando label:


```json
{
  "tool": "sessions_send",
  "params": {
    "label": "code-review",
    "message": "PR revisado, 3 issues encontrados"
  }
}
```

### Identificación del target

| Parámetro | Cómo matchea |
|-----------|-------------|
| `sessionKey` | Match exacto del key (e.g., `agent:main:main`) |
| `label` | Match por label del sub-agente (e.g., `code-review`) |

- **Solo uno de los dos.** Si ambos se proporcionan, `sessionKey` tiene precedencia.


### Visibilidad: qué sesiones puedes alcanzar

- La visibilidad se controla con `tools.sessions.visibility`:


| Valor | Sesiones alcanzables |
|-------|---------------------|
| `"self"` | Solo la sesión actual |
| `"tree"` (default) | Sesión actual + sub-agentes spawneados desde ella |
| `"agent"` | Todas las sesiones del mismo agentId |
| `"all"` | Todas las sesiones del gateway |

```json5
{
  tools: {
    sessions: { visibility: "tree" }    // default
  },
  // Per-agent override:
  agents: {
    list: [{
      id: "public",
      tools: { sessions: { visibility: "self" } }    // public no ve nada más
    }]
  }
}
```

### Implicaciones de seguridad

- `sessions_send` es poderoso: puede inyectar mensajes en cualquier sesión visible.
- Un agente comprometido con `visibility: "all"` podría enviar instrucciones a otra sesión.


- **Mitigaciones:**

- Default `"tree"` limita a la cadena de sub-agentes
- Sub-agentes depth 1 (leaf) no tienen `sessions_send` en sus tools
- `"self"` para agentes de bajo trust

- ---


## 11.3 sessions_list: Descubrir Sesiones

### Qué retorna

```json
{
  "tool": "sessions_list",
  "params": {
    "activeMinutes": 60,
    "limit": 10,
    "messageLimit": 2,
    "kinds": ["subagent"]
  }
}
```

| Parámetro | Propósito |
|-----------|-----------|
| `activeMinutes` | Solo sesiones con actividad en los últimos N minutos |
| `limit` | Max sesiones a retornar |
| `messageLimit` | Incluir los últimos N mensajes de cada sesión (0 = solo metadata) |
| `kinds` | Filtrar por tipo: `["subagent"]`, `["direct"]`, `["group"]`, etc. |

### Retorno

```json
[
  {
    "sessionKey": "agent:main:subagent:f8a2...",
    "label": "code-review",
    "status": "completed",
    "agentId": "main",
    "updatedAt": 1708444800000,
    "lastMessages": [
      { "role": "assistant", "content": "PR revisado..." }
    ]
  }
]
```

### Uso típico

- El agente main usa `sessions_list` para **monitorear** sub-agentes sin polling:


```
Agente: "¿Cómo van los sub-agentes?"
→ sessions_list({ kinds: ["subagent"], activeMinutes: 120, messageLimit: 1 })
→ "Hay 2 activos y 1 completado. El completado dice: '...'"
```

- **No hacer polling.** Los announces son push-based. `sessions_list` es para inspección on-demand, no para busy-waiting.


- ---


## 11.4 sessions_history: Leer Transcripts

### Qué hace

- Lee el historial de mensajes de otra sesión (sujeto a visibilidad).


```json
{
  "tool": "sessions_history",
  "params": {
    "sessionKey": "agent:main:subagent:f8a2...",
    "limit": 20,
    "includeTools": true
  }
}
```

| Parámetro | Default | Propósito |
|-----------|---------|-----------|
| `sessionKey` | (requerido) | Key de la sesión target |
| `limit` | 50 | Max mensajes a retornar |
| `includeTools` | false | Incluir tool calls y tool results |

### Caso de uso principal

- Después de que un sub-agente completa y anuncia un resumen, el main puede querer el **detalle completo**:


```
Main recibe announce: "PR revisado. 3 issues."
Main quiere detalle → sessions_history(subagent_key, includeTools: true)
→ Ve exactamente qué comandos corrió, qué archivos leyó, y los findings detallados
```

- ---


## 11.5 subagents Tool: Gestión de Sub-Agentes

- El tool `subagents` es la interfaz programática para gestionar sub-agentes desde dentro de una sesión.


### Acciones

| Acción | Parámetros | Qué hace |
|--------|-----------|----------|
| `list` | `recentMinutes?` | Lista sub-agentes de esta sesión |
| `steer` | `target`, `message` | Inyecta mensaje en un sub-agente corriendo |
| `kill` | `target` | Mata un sub-agente (con cascade) |

### Steer: intervención en tiempo real

```json
{
  "tool": "subagents",
  "params": {
    "action": "steer",
    "target": "code-review",
    "message": "También revisa el manejo de errores en auth.py"
  }
}
```

- **Steer inyecta el mensaje en el run activo** del sub-agente.
- El sub-agente lo ve como un mensaje del "usuario" que aparece durante su ejecución.
- El comportamiento depende del queue mode:


- Si el sub-agente está ejecutando tools → el steer se inyecta después del próximo tool boundary
- Si el sub-agente está generando texto → el steer interrumpe y se procesa

### Kill: terminación

```json
{
  "tool": "subagents",
  "params": {
    "action": "kill",
    "target": "code-review"
  }
}
```

- `target` puede ser: label, session key, run id, o `"all"`.


- ---


## 11.6 Agent-to-Agent Messaging

### Concepto

- Cuando tienes múltiples agentes (Cap.
- 6), pueden necesitar comunicarse.
- Por default, esto está **deshabilitado**:


```json5
{
  tools: {
    agentToAgent: {
      enabled: false     // default
    }
  }
}
```

### Habilitación

```json5
{
  tools: {
    agentToAgent: {
      enabled: true,
      allow: ["main", "work"]    // solo estos agentes pueden inter-comunicarse
    }
  }
}
```

### Cómo funciona

- Un agente usa `sessions_send` con un sessionKey de otro agente:


```json
{
  "tool": "sessions_send",
  "params": {
    "sessionKey": "agent:work:main",
    "message": "Alerta: el build de CI falló en el repo X"
  }
}
```

- Esto trigger un agent run en la sesión main del agente "work".


### Patrones

| Patrón | Flujo |
|--------|-------|
| **Notificación** | Agent "alerts" detecta evento → envía a agent "main" |
| **Delegación** | Agent "main" recibe tarea compleja → envía a agent "coding" |
| **Pipeline** | Agent "ingest" procesa email → envía resumen a agent "main" |

### Riesgos

- **Prompt injection inter-agente:** Un agente comprometido podría enviar instrucciones maliciosas a otro
- **Loops:** Agente A envía a B, B responde a A, A envía a B... → loop infinito

- **Mitigaciones:**

- Allowlist tight (solo los agentes que genuinamente necesitan comunicarse)
- Mantener deshabilitado por default
- Los agentes que reciben mensajes inter-agente deberían tratar el contenido como input no-confiable (similar a mensajes de grupo)

- ---


## 11.7 openclaw agent CLI: Runs Directos

### Concepto

- El comando `openclaw agent` permite trigger un agent run desde la línea de comandos, scripts, cron del OS, o CI/CD — **sin un mensaje inbound de un canal de messaging**.


```bash
# Enviar mensaje a la sesión main
openclaw agent --to +56912345678 --message "Status update"

# Target un agente específico
openclaw agent --agent ops --message "Summarize logs"

# Reusar una sesión existente
openclaw agent --session-id abc123 --message "Continue analysis"

# Con delivery a un canal
openclaw agent --agent ops --message "Report" --deliver --reply-channel telegram --reply-to "7192195698"
```

### Flags principales

| Flag | Propósito |
|------|-----------|
| `--to <dest>` | Deriva session key del destino |
| `--agent <id>` | Target un agente por su id |
| `--session-id <id>` | Reusar sesión existente |
| `--message <text>` | El mensaje (requerido) |
| `--deliver` | Enviar la respuesta a un canal |
| `--reply-channel` | Canal de delivery |
| `--reply-to` | Target de delivery |
| `--model <ref>` | Override de modelo |
| `--thinking <level>` | Override de thinking |
| `--local` | Forzar runtime local (no via gateway) |
| `--json` | Output estructurado |

### Cómo funciona

```
openclaw agent --message "..."
      │
      ├── ¿Gateway accesible?
      │   ├── SÍ → Run via gateway (mismas rules de auth, tools, sessions)
      │   └── NO → Fallback a embedded runtime local
      │
      ▼
  Run completo: prompt assembly → inference → tools → reply
      │
      ▼
  Output a stdout (texto o JSON)
  + Opcionalmente delivery a canal (--deliver)
```

### Casos de uso

| Escenario | Comando |
|-----------|---------|
| Cron del OS que trigger análisis semanal | `openclaw agent --agent ops --message "Weekly report" --deliver --reply-channel telegram` |
| Script de CI que notifica resultado | `openclaw agent --to +555... --message "Build passed" --deliver` |
| Testing de prompts/skills | `openclaw agent --message "use my new skill" --json` |
| Debugging de sesión | `openclaw agent --session-id abc --message "what happened?" --json` |

### Diferencia con cron de OpenClaw

| | `openclaw agent` (CLI) | Cron job de OpenClaw |
|--|----------------------|---------------------|
| **Trigger** | Externo (crontab, script) | Interno (scheduler del gateway) |
| **Sesión** | Configurable (--to, --agent, --session-id) | Configurada en el job |
| **Auth** | Requiere gateway auth o --local | Interno (sin auth extra) |
| **Delivery** | Opcional (--deliver) | Configurable (announce, webhook, none) |
| **Model** | Flag --model | Config del job |

- ---


## 11.8 Visibilidad: El Modelo de Seguridad

- Todos los mecanismos de comunicación inter-sesión están gated por **visibilidad**:


```
┌──────────────────────────────────────────────────────────┐
│ tools.sessions.visibility                                 │
│                                                          │
│  "self"   → Solo tu propia sesión                        │
│  "tree"   → Tu sesión + sub-agentes que spawneaste       │
│  "agent"  → Todas las sesiones de tu agentId             │
│  "all"    → Todas las sesiones del gateway               │
│                                                          │
│  Afecta: sessions_send, sessions_list, sessions_history  │
│  NO afecta: subagents tool (siempre ve sus propios hijos)│
└──────────────────────────────────────────────────────────┘
```

### Matriz de riesgo

| Visibility | Blast radius | Recomendado para |
|------------|-------------|-----------------|
| `"self"` | Mínimo | Agentes públicos, bots de soporte |
| `"tree"` | Moderado | Default. Agentes que usan sub-agentes |
| `"agent"` | Alto | Agentes que necesitan inspeccionar todas sus sesiones |
| `"all"` | Máximo | Solo agentes de confianza total (debugging, ops) |

### Per-agent visibility

```json5
{
  tools: {
    sessions: { visibility: "tree" }    // global default
  },
  agents: {
    list: [
      { id: "main", tools: { sessions: { visibility: "agent" } } },
      { id: "public", tools: { sessions: { visibility: "self" } } },
      { id: "ops", tools: { sessions: { visibility: "all" } } }
    ]
  }
}
```

- ---


## Resumen del Capítulo

| Mecanismo | Dirección | Gate principal | Caso de uso |
|-----------|-----------|---------------|-------------|
| `sessions_send` | Sesión → Sesión | `sessions.visibility` | Inyectar resultados, notificaciones |
| `sessions_list` | Read-only | `sessions.visibility` | Descubrir sesiones, monitoreo |
| `sessions_history` | Read-only | `sessions.visibility` | Inspeccionar transcripts |
| `subagents` | Parent → Child | Siempre (propios hijos) | Steer, kill, listar sub-agentes |
| `agent-to-agent` | Agente → Agente | `agentToAgent.allow` | Notificaciones inter-agente |
| `openclaw agent` | Externo → Sesión | Gateway auth | Scripts, CI/CD, testing |

### Principios de diseño

| Principio | Implementación |
|-----------|---------------|
| **Default cerrado** | `visibility: "tree"`, agent-to-agent disabled |
| **No polling** | Announces son push-based; `sessions_list` es on-demand |
| **Mínimo privilegio** | Cada nivel de visibility solo expone lo necesario |
| **Steer > kill** | Preferir redirección de sub-agentes sobre terminación |
| **CLI como escape hatch** | `openclaw agent` para integraciones externas sin tocar messaging |

- ---


- *Siguiente: [Capítulo 12 — Heartbeats](12-heartbeats.md) (Parte IV — Automatización)*


---
_manifest:
  urn: urn:agengai:kb:17-lobster
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.1.0
status: published
tags:
- kora
- manual-openclaw
- '17'
- lobster
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:17-lobster
---

# Capítulo 17 — Lobster (Workflow Runtime)

> **Propósito:** Entender cómo ejecutar pipelines determinísticas multi-paso con approval gates dentro de OpenClaw. Lobster cierra el gap entre "el agente hace todo via tool calls" y "scripts que no necesitan inteligencia": es orquestación determinística con checkpoints humanos, opcionalmente enriquecida con LLM steps.

- ---

## 17.1 El Problema que Resuelve

- Sin Lobster, un workflow multi-paso requiere múltiples tool calls del modelo:

```
SIN LOBSTER (múltiples roundtrips):

User: "Triagea mi email y envía replies a los urgentes"
 Model → tool: gmail.list (turn 1, tokens)
 Model → tool: gmail.read (×5) (turn 2-6, tokens)
 Model → razona qué es urgente (turn 7, tokens)
 Model → tool: gmail.draft (×2) (turn 8-9, tokens)
 Model → "¿Envío estos drafts?" (turn 10, tokens)
 User: "Sí"
 Model → tool: gmail.send (×2) (turn 11-12, tokens)

Total: ~12 roundtrips, ~50K tokens, 3 minutos
El modelo orquesta cada paso.
```

```
CON LOBSTER (un pipeline):

Model → tool: lobster({ pipeline: "email.triage --limit 20" })
 lobster ejecuta: list → categorize → draft → APPROVAL GATE
 
 Tool retorna: needs_approval, resumeToken, preview de 2 drafts
 Model: "Lobster quiere enviar 2 replies. ¿Apruebas?"
 User: "Sí"
 Model → tool: lobster({ action: "resume", token: "...", approve: true })
 lobster ejecuta: send drafts

Total: 2 tool calls, ~5K tokens, 30 segundos
Lobster orquesta los pasos.
```

### La diferencia

| | Sin Lobster | Con Lobster |
|--|-------------|-------------|
| **Orquestación** | El modelo (LLM tokens) | El runtime (código) |
| **Token cost** | Alto (cada paso es un turn) | Bajo (1-2 tool calls) |
| **Determinismo** | El modelo puede variar | Pipeline fija, reproducible |
| **Approvals** | Manual (el modelo pregunta) | Built-in con resume tokens |
| **Reanudabilidad** | Reempezar si se pierde contexto | Resume token persiste |
| **Auditabilidad** | Hay que leer el transcript | Pipeline es data (log, diff, replay) |

- ---

## 17.2 Cómo Funciona

- Lobster es un **CLI externo** que OpenClaw invoca como tool:

```
Agent loop
 │
 ▼
Model decide: "necesito correr un workflow"
 │
 ▼
Tool call: lobster({ action: "run", pipeline: "..." })
 │
 ▼
Gateway spawna: lobster --tool-mode
 │
 ▼
Lobster ejecuta pipeline step by step:
 step 1: exec command → output JSON
 step 2: pipe output → exec next command
 step 3: pipe output → APPROVAL GATE → PAUSE
 │
 ▼
Lobster retorna JSON envelope:
 { status: "needs_approval", resumeToken: "...", output: [...] }
 │
 ▼
Model recibe resultado, presenta al usuario
 │
 ▼
User aprueba → Model resume: lobster({ action: "resume", token, approve: true })
 │
 ▼
Lobster continúa desde el checkpoint:
 step 4: exec side effect → output
 │
 ▼
Retorna: { status: "ok", output: [...] }
```

- ---

### Instalación y habilitación

- La documentación oficial actual explicita dos prerequisitos operativos:

```bash
# Instalar lobster como CLI disponible para el gateway
# (según tu entorno: npm/pnpm/bun/homebrew o binario local)
```

```json5
// Habilitar el tool en OpenClaw
tools: { alsoAllow: ["lobster"] }
```

- Si Lobster no está en `PATH` o el tool no está permitido, el agente no podrá invocarlo aunque el workflow exista.

## 17.3 DSL: Pipelines y Pipes

### Inline pipeline (shell-like)

```
exec --json --shell 'inbox list' | exec --stdin json --shell 'inbox categorize' | approve --prompt 'Apply?'
```

- Cada `|` conecta stdout de un paso con stdin del siguiente.
- Es un pipe Unix con approval gates built-in.

### Workflow file (.lobster)

```yaml
name: inbox-triage
args:
 tag:
 default: "family"
steps:
 - id: collect
 command: inbox list --json
 - id: categorize
 command: inbox categorize --json
 stdin: $collect.stdout
 - id: review
 command: inbox apply --approve
 stdin: $categorize.stdout
 approval: required
 - id: execute
 command: inbox apply --execute
 stdin: $categorize.stdout
 condition: $review.approved
```

| Concepto | Sintaxis | Propósito |
|----------|---------|-----------|
| **Step** | `id`, `command` | Un paso del workflow |
| **Pipe** | `stdin: $step.stdout` | Conectar output de un paso a input de otro |
| **JSON pipe** | `stdin: $step.json` | Pasar solo el JSON parseado |
| **Approval** | `approval: required` | Pausar y pedir aprobación |
| **Condition** | `condition: $step.approved` | Ejecutar solo si el paso anterior fue aprobado |
| **Args** | `args.tag.default` | Parámetros del workflow con defaults |

### Patrón: CLIs pequeños + JSON pipes + approvals

- La filosofía de Lobster: construir **CLIs pequeños** que hablan JSON, y conectarlos:

```bash
# Cada CLI hace una cosa y retorna JSON
gog gmail search --json --query 'newer_than:1d' → [{ from, subject, snippet }]
email-classifier --json → [{ id, priority, draft }]
email-sender --json --dry-run → [{ id, to, subject, status }]
```

```
pipeline: "gog.gmail.search | email-classifier | approve --prompt 'Send?' | email-sender"
```

- ---

## 17.4 Resume Tokens: Pause → Approve → Continue

- El approval gate es la feature definitoria de Lobster:

```
Pipeline corriendo
 │
 ▼
Step con approval: required
 │
 ▼
PAUSA
 ├── Estado del workflow serializado
 ├── Resume token generado (compact key)
 ├── Estado guardado en disco (Lobster state dir)
 └── Tool retorna: { status: "needs_approval", resumeToken: "tok_abc..." }
 │
 ▼
... tiempo pasa (segundos, minutos, horas) ...
 │
 ▼
Resume con token:
 lobster({ action: "resume", token: "tok_abc...", approve: true })
 │
 ▼
Lobster carga estado → continúa desde el checkpoint
 │
 ▼
Pipeline termina: { status: "ok" }
```

### Approve vs Deny

```json
// Aprobar: continuar el pipeline
{ "action": "resume", "token": "tok_abc...", "approve": true }

// Denegar: cancelar el pipeline
{ "action": "resume", "token": "tok_abc...", "approve": false }
→ { "status": "cancelled" }
```

### Preview en approvals

```
approve --preview-from-stdin --limit 5 --prompt 'Send these drafts?'
```

- Adjunta las primeras 5 líneas de stdin como preview en la approval request.
- Así el usuario puede ver qué se va a ejecutar antes de aprobar.

- ---

## 17.5 llm-task: LLM Steps dentro de Workflows

- A veces un paso del pipeline necesita **inteligencia** (clasificar, resumir, generar). `llm-task` es un plugin tool que ejecuta un LLM call JSON-only:

```yaml
# Dentro de un pipeline Lobster:
openclaw.invoke --tool llm-task --action json --args-json '{
 "prompt": "Classify this email by urgency and intent",
 "input": { "subject": "...", "body": "..." },
 "schema": {
 "type": "object",
 "properties": {
 "urgency": { "enum": ["high", "medium", "low"] },
 "intent": { "type": "string" }
 },
 "required": ["urgency", "intent"]
 }
}'
```

### Características de llm-task

| | llm-task | Agent turn normal |
|--|---------|------------------|
| **Output** | JSON only (schema-validated) | Texto libre + tool calls |
| **Tools disponibles** | Ninguno | Todos los permitidos |
| **Propósito** | Clasificar, resumir, generar structured data | Razonar y actuar libremente |
| **Costo** | Bajo (prompt corto, sin tools) | Variable (context window completo) |

### Config

```json5
{
 plugins: {
 entries: {
 "llm-task": {
 enabled: true,
 config: {
 defaultProvider: "openai-codex",
 defaultModel: "gpt-5.2",
 allowedModels: ["openai-codex/gpt-5.2", "anthropic/claude-haiku-4-5"],
 maxTokens: 800,
 timeoutMs: 30000
 }
 }
 }
 },
 tools: { alsoAllow: ["llm-task"] }
}
```

### Seguridad

- JSON-only: el modelo NO puede ejecutar tool calls
- Sin tools expuestos al modelo
- Schema validation: output rechazado si no matchea el schema
- Tratar output como untrusted a menos que se valide

- ---

## 17.6 Integración con Cron y Heartbeat

- Lobster no se ejecuta solo — necesita un trigger.
- Los triggers son cron, heartbeat, o la conversación directa:

```
TRIGGER LOBSTER PIPELINE
─────── ────────────────
Cron job (isolated) → lobster({ pipeline: "weekly-review.lobster" })
Heartbeat → Agente decide correr pipeline si condición se cumple
Conversación → User pide "triagea mi email" → agente llama lobster
Webhook → /hooks/agent con message que trigger pipeline
```

### Cron + Lobster: automated with approval

```bash
openclaw cron add \
 --name "Email triage" \
 --cron "0 8 * * *" \
 --session isolated \
 --message "Run the email triage workflow using lobster. If approvals are needed, announce them to me." \
 --announce --channel telegram --to "7192195698"
```

- El cron job trigger un agent turn.
- El agente llama lobster.
- Si hay approval pending, lo anuncia al canal.
- El usuario aprueba (o no) en su próxima interacción.

- ---

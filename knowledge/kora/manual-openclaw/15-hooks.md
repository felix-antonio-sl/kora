# Capítulo 15 — Hooks (Event-Driven Automation)

> **Propósito:** Entender cómo extender el gateway con código que reacciona a eventos internos. Los hooks son el mecanismo para automatización que NO depende del modelo — son código TypeScript que corre cuando suceden cosas (comandos, bootstrap, mensajes, startup), sin consumir tokens.

---

## 15.1 Concepto: Scripts que Reaccionan a Eventos

Un hook es un **handler TypeScript** que se ejecuta cuando el gateway emite un evento. No involucra al modelo de IA — corre directamente en el proceso del gateway.

```
Evento del Gateway
      │
      ▼
┌─────────────────┐
│ Hook System      │
│                  │
│ ¿Hay hooks       │
│  registrados     │
│  para este       │
│  evento?         │
│                  │
│ SÍ → Ejecutar   │
│       cada uno   │
│                  │
│ NO → Continuar   │
└─────────────────┘
      │
      ▼
Procesamiento normal continúa
```

### Hooks vs otras automatizaciones

| | Hooks | Heartbeats | Cron Jobs | Sub-agentes |
|--|-------|-----------|-----------|-------------|
| **Trigger** | Eventos internos del gateway | Timer periódico | Schedule programado | Tool call del agente |
| **Ejecuta** | Código TypeScript | Agent turn (LLM) | Agent turn (LLM) | Agent turn (LLM) |
| **Consume tokens** | ❌ No | ✅ Sí | ✅ Sí | ✅ Sí |
| **Necesita modelo** | ❌ No | ✅ Sí | ✅ Sí | ✅ Sí |
| **Velocidad** | Milisegundos | Segundos-minutos | Segundos-minutos | Segundos-minutos |
| **Capacidad** | Lo que TypeScript puede hacer | Lo que el agente puede hacer | Lo que el agente puede hacer | Lo que el agente puede hacer |

**La distinción clave:** Los hooks son **determinísticos y gratuitos** (no LLM). Los demás mecanismos son **inteligentes pero costosos** (LLM).

---

## 15.2 Event Types

### Command Events

Se disparan cuando el usuario o el sistema emite un comando:

| Event | Cuándo |
|-------|--------|
| `command:new` | Al ejecutar `/new` (antes del reset) |
| `command:reset` | Al ejecutar `/reset` |
| `command:stop` | Al ejecutar `/stop` |
| `command` | Cualquier comando (general listener) |

### Agent Events

| Event | Cuándo |
|-------|--------|
| `agent:bootstrap` | Antes de inyectar bootstrap files en el prompt. El hook puede **mutar** `context.bootstrapFiles` |

### Gateway Events

| Event | Cuándo |
|-------|--------|
| `gateway:startup` | Después de que canales arrancan y hooks se cargan |

### Message Events

| Event | Cuándo | Contexto |
|-------|--------|----------|
| `message:received` | Mensaje inbound de cualquier canal | `from`, `content`, `channelId`, `metadata` |
| `message:sent` | Mensaje outbound enviado exitosamente | `to`, `content`, `success`, `channelId` |
| `message` | Ambos (general listener) | |

### Plugin Hooks (API especial)

| Hook | Tipo | Cuándo |
|------|------|--------|
| `tool_result_persist` | Síncrono | Antes de persistir tool results al transcript. Puede transformar el payload |

---

## 15.3 Hook Structure

Cada hook es un directorio con dos archivos:

```
my-hook/
├── HOOK.md          ← Metadata (YAML frontmatter) + documentación
└── handler.ts       ← Implementación del handler
```

### HOOK.md

```markdown
---
name: my-hook
description: "Guarda contexto de sesión al resetear"
metadata:
  openclaw:
    emoji: "💾"
    events: ["command:new"]
    requires:
      bins: ["node"]
      env: ["MY_API_KEY"]
      config: ["workspace.dir"]
      os: ["linux", "darwin"]
---

# My Hook

Documentación detallada del hook...
```

### handler.ts

```typescript
import type { HookHandler } from "../../src/hooks/hooks.js";

const handler: HookHandler = async (event) => {
  // Filtrar temprano
  if (event.type !== "command" || event.action !== "new") {
    return;
  }

  console.log(`[my-hook] Session reset: ${event.sessionKey}`);
  
  // Lógica custom
  // ...

  // Opcionalmente enviar mensaje al usuario
  event.messages.push("💾 Contexto guardado.");
};

export default handler;
```

### Event Context disponible

```typescript
event = {
  type: "command" | "session" | "agent" | "gateway" | "message",
  action: string,           // "new", "reset", "stop", "received", "sent"
  sessionKey: string,
  timestamp: Date,
  messages: string[],        // push para enviar mensajes al usuario
  context: {
    sessionEntry?: ...,      // metadata de la sesión
    sessionId?: string,
    sessionFile?: string,    // path al JSONL
    commandSource?: string,  // "telegram", "whatsapp", etc.
    senderId?: string,
    workspaceDir?: string,
    bootstrapFiles?: ...,    // mutable en agent:bootstrap
    cfg?: OpenClawConfig,
    // Message events:
    from?: string,
    to?: string,
    content?: string,
    channelId?: string,
    success?: boolean,
  }
}
```

---

## 15.4 Discovery y Precedencia

Los hooks se descubren automáticamente de tres directorios, en orden de **precedencia** (el primero gana si hay conflicto de nombres):

```
1. Workspace hooks      <workspace>/hooks/          (mayor precedencia)
2. Managed hooks        ~/.openclaw/hooks/           (user-installed)
3. Bundled hooks        <openclaw>/dist/hooks/bundled/   (shipped con OpenClaw)
```

Si tienes un hook `session-memory` en tu workspace y otro bundled con el mismo nombre, el del workspace gana.

---

## 15.5 Hooks Bundled

OpenClaw incluye 4 hooks de fábrica:

### 💾 session-memory

- **Event:** `command:new`
- **Qué hace:** Al ejecutar `/new`, extrae las últimas 15 líneas de conversación, genera un slug descriptivo via LLM, y guarda en `memory/YYYY-MM-DD-slug.md`
- **Por qué importa:** Red de seguridad contra pérdida de contexto al resetear

```bash
openclaw hooks enable session-memory
```

### 📎 bootstrap-extra-files

- **Event:** `agent:bootstrap`
- **Qué hace:** Inyecta archivos bootstrap adicionales desde paths/globs configurados. Útil para monorepos con AGENTS.md por módulo
- **Config:**
  ```json5
  hooks: { internal: { entries: {
    "bootstrap-extra-files": {
      enabled: true,
      paths: ["packages/*/AGENTS.md", "packages/*/TOOLS.md"]
    }
  }}}
  ```

### 📝 command-logger

- **Event:** `command` (todos)
- **Qué hace:** Escribe cada comando a `~/.openclaw/logs/commands.log` en JSONL
- **Para:** Auditoría, troubleshooting, compliance

### 🚀 boot-md

- **Event:** `gateway:startup`
- **Qué hace:** Lee `BOOT.md` del workspace y ejecuta sus instrucciones via agent runner al iniciar el gateway
- **Para:** Setup automático post-restart (enviar mensajes, verificar estado)

---

## 15.6 Hook Packs (npm)

Los hooks se pueden distribuir como paquetes npm:

```bash
openclaw hooks install @acme/my-hooks
```

El paquete declara hooks en `package.json`:

```json
{
  "name": "@acme/my-hooks",
  "openclaw": {
    "hooks": ["./hooks/my-hook", "./hooks/other-hook"]
  }
}
```

**Seguridad:** `npm install --ignore-scripts` (sin lifecycle scripts). Los hooks deben ser pure JS/TS.

---

## 15.7 Plugin Hooks

Los plugins (Cap. 2) pueden registrar hooks adicionales via la API interna:

| Hook | Tipo | Uso |
|------|------|-----|
| `before_model_resolve` | Síncrono | Modificar selección de modelo antes de inference |
| `before_prompt_build` | Síncrono | Modificar prompt antes de ensamblaje |
| `before_tool_call` | Síncrono | Interceptar tool call antes de ejecución |
| `after_tool_call` | Síncrono | Post-procesar resultado de tool call |
| `tool_result_persist` | Síncrono | Transformar tool result antes de persistir al JSONL |

Estos hooks son **in-process** con el gateway (código de plugin) — no son los hooks de directorio descritos arriba.

---

## 15.8 Crear un Hook Custom

### Paso a paso

```bash
# 1. Crear directorio
mkdir -p ~/clawd/hooks/my-hook

# 2. Crear HOOK.md
cat > ~/clawd/hooks/my-hook/HOOK.md << 'EOF'
---
name: my-hook
description: "Log de mensajes recibidos por canal"
metadata:
  openclaw:
    emoji: "📊"
    events: ["message:received"]
---
# My Hook
Loguea cada mensaje recibido con canal y sender.
EOF

# 3. Crear handler.ts
cat > ~/clawd/hooks/my-hook/handler.ts << 'EOF'
import type { HookHandler } from "../../src/hooks/hooks.js";

const handler: HookHandler = async (event) => {
  if (event.type !== "message" || event.action !== "received") return;
  
  const { from, channelId, content } = event.context;
  console.log(`[my-hook] ${channelId}:${from} → ${content?.slice(0, 50)}`);
};

export default handler;
EOF

# 4. Verificar descubrimiento
openclaw hooks list

# 5. Habilitar
openclaw hooks enable my-hook

# 6. Reiniciar gateway
sudo systemctl restart openclaw-gateway
```

### Best Practices

| Regla | Por qué |
|-------|---------|
| **Mantener handlers rápidos** | Corren durante procesamiento de comandos; bloquear = latencia |
| **Filtrar temprano** | `if (event.type !== "command") return;` — no procesar eventos irrelevantes |
| **Catch errors** | No lanzar — try/catch todo. Un error en un hook no debe romper el gateway |
| **Fire and forget para async pesado** | `void processInBackground(event);` — no awaitar cosas lentas |
| **Eventos específicos** | `["command:new"]` > `["command"]` — menos overhead |
| **Sin secretos en HOOK.md** | HOOK.md es metadata + docs, no config |

---

## 15.9 CLI de Hooks

```bash
# Listar todos los hooks
openclaw hooks list
openclaw hooks list --eligible      # solo elegibles
openclaw hooks list --verbose       # mostrar requisitos faltantes

# Info detallada de un hook
openclaw hooks info session-memory

# Check de elegibilidad
openclaw hooks check

# Habilitar/deshabilitar
openclaw hooks enable session-memory
openclaw hooks disable command-logger

# Instalar hook pack
openclaw hooks install @acme/my-hooks
```

---

## 15.10 Configuración

```json5
{
  hooks: {
    internal: {
      enabled: true,          // master switch
      entries: {
        "session-memory": { enabled: true },
        "command-logger": { enabled: true },
        "bootstrap-extra-files": {
          enabled: true,
          paths: ["packages/*/AGENTS.md"]
        },
        "my-hook": {
          enabled: true,
          env: { "MY_VAR": "value" }     // env vars custom
        }
      },
      load: {
        extraDirs: ["/path/to/more/hooks"]  // dirs adicionales
      }
    }
  }
}
```

---

## Resumen del Capítulo

| Concepto | Decisión de diseño que habilita |
|----------|--------------------------------|
| **Código, no LLM** | Automatización determinística sin consumir tokens |
| **Event-driven** | Reaccionar a lo que sucede, no a un schedule |
| **Discovery automática** | Tres directorios con precedencia; sin registro manual |
| **Gating por requisitos** | bins, env, config, OS — hooks inelegibles se ignoran silenciosamente |
| **4 hooks bundled** | session-memory, bootstrap-extra-files, command-logger, boot-md |
| **Hook packs** | Distribución npm para hooks compartidos |
| **Plugin hooks** | Interceptar model resolve, prompt build, tool calls |
| **Messages push** | `event.messages.push()` para enviar feedback al usuario |
| **agent:bootstrap mutable** | Hooks pueden modificar bootstrap files antes de inyección |

### Cuándo usar hooks vs otros mecanismos

```
¿La tarea es determinística (no necesita inteligencia)?
├── SÍ → ¿Reacciona a un evento del gateway?
│        ├── SÍ → HOOK
│        └── NO → Script/cron del OS
│
└── NO → ¿Necesita timing preciso?
         ├── SÍ → Cron job
         └── NO → ¿Se batchea con otros checks?
                  ├── SÍ → Heartbeat
                  └── NO → Cron isolated
```

---

*Siguiente: [Capítulo 16 — Webhooks (External Triggers)](16-webhooks.md)*

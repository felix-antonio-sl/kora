---
_manifest:
  urn: urn:kora:kb:07-aislamiento-seguridad
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: legacy-import
version: 2.0.0
status: published
tags:
- kora
- manual-openclaw
- '07'
- aislamiento
- seguridad
lang: es
---

# Capítulo 7 — Aislamiento y Seguridad por Agente

> **Propósito:** Entender los tres controles de seguridad per-agent (sandbox, tool policy, elevated) como un sistema integrado. Saber cuál resolver primero cuando algo está bloqueado, y diseñar perfiles de seguridad coherentes para cada agente.

- ---


## 7.1 Los Tres Controles: Vista Unificada

- OpenClaw tiene tres mecanismos de seguridad que trabajan en capas.
- Son **relacionados pero independientes**:


```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  1. SANDBOX                    "¿DÓNDE corren los tools?"      │
│     Docker container vs host                                   │
│     Controla: filesystem, red, procesos                        │
│                                                                │
│  2. TOOL POLICY                "¿QUÉ tools existen?"           │
│     Allow/deny por tool                                        │
│     Controla: qué tools ve el modelo                           │
│                                                                │
│  3. ELEVATED                   "¿PUEDE exec escapar al host?"  │
│     Escape hatch para exec                                     │
│     Controla: solo exec, solo desde sandbox                    │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Cómo interactúan

```
¿Tool permitido por policy?
├── NO → Bloqueado. Punto. (ni sandbox ni elevated importan)
│
└── SÍ → ¿Agente sandboxed?
         ├── NO → Tool corre en host directamente
         │
         └── SÍ → Tool corre en Docker container
                  │
                  └── ¿Es exec + elevated activado?
                       ├── SÍ → exec corre en host (escape)
                       └── NO → exec corre en container
```

- **Regla cardinal:** Tool policy es el gate principal.
- Si un tool está denied, no importa si estás en sandbox o en host, ni si elevated está activado — el tool no existe para el modelo.


### Debug rápido

```bash
openclaw sandbox explain
openclaw sandbox explain --agent work
openclaw sandbox explain --session agent:work:main
openclaw sandbox explain --json
```

- Muestra: sandbox mode/scope efectivo, si la sesión está sandboxed, tool allow/deny resuelto, elevated gates.


- ---


## 7.2 Sandbox: Dónde Corren los Tools

- El sandbox envuelve la ejecución de tools en **containers Docker** para limitar el blast radius de un modelo que hace algo "dumb".


### Modes

| Mode | Qué se sandbox | Cuándo usar |
|------|---------------|-------------|
| `"off"` | Nada — todo en host | Agente personal de confianza |
| `"non-main"` | Solo sesiones non-main (grupos, canales, cron, subagentes) | **El más útil:** DMs en host, grupos en sandbox |
| `"all"` | Toda sesión | Agentes de bajo trust o públicos |

- **"non-main" es basado en mainKey, no en agentId.** Grupos y canales siempre son non-main.
- Si tu agente main tiene heartbeats que corren en la sesión main, esos NO se sandboxean en modo `non-main`.


### Scope: cuántos containers

| Scope | Containers | Aislamiento | Uso |
|-------|-----------|-------------|-----|
| `"session"` (default) | Uno por sesión | Máximo | Grupos no se ven entre sí |
| `"agent"` | Uno por agente | Medio | Todas las sesiones de un agente comparten container |
| `"shared"` | Uno para todos | Mínimo | Todas las sesiones sandboxed comparten container |

- **Trade-off:** `"session"` es lo más seguro pero consume más recursos Docker. `"shared"` es más eficiente pero si una sesión deja archivos, otra los puede ver.


### Workspace Access

| Access | El sandbox ve | Writes | Cuándo |
|--------|--------------|--------|--------|
| `"none"` (default) | Sandbox workspace (`~/.openclaw/sandboxes/`) | Solo al sandbox workspace | Máximo aislamiento |
| `"ro"` | Agent workspace en `/agent` (read-only) | Bloqueados (write/edit/apply_patch disabled) | Agente que solo lee |
| `"rw"` | Agent workspace en `/workspace` (read-write) | Permitidos al workspace real | Agente que necesita escribir (coding) |

### Bind Mounts: perforaciones controladas

```json5
sandbox: {
  docker: {
    binds: [
      "/home/user/source:/source:ro",     // código fuente, solo lectura
      "/var/data/myapp:/data:ro"           // datos, solo lectura
    ]
  }
}
```

- **Los binds perforan el sandbox.** Lo que montas es visible dentro del container con el modo que configures (`:ro` o `:rw`).
- Default es read-write si omites el modo.


- **Seguridad:**

- OpenClaw bloquea binds peligrosos: `docker.sock`, `/etc`, `/proc`, `/sys`, `/dev`
- Preferir `:ro` siempre que sea posible
- `scope: "shared"` ignora per-agent binds (solo aplican los globales)
- Nunca montar `docker.sock` a menos que intencionalmente quieras dar control del host

### Network en sandbox

```json5
sandbox: {
  docker: {
    network: "none"    // default: sin red
  }
}
```

- Default: **sin network.** El container no puede hacer requests HTTP, instalar packages, ni conectarse a nada.
- Para skills que necesitan network:


```json5
sandbox: { docker: { network: "bridge" } }  // habilita red
```

### setupCommand: provisioning one-time

```json5
sandbox: {
  docker: {
    setupCommand: "apt-get update && apt-get install -y git curl jq",
    network: "bridge",        // necesario para apt-get
    // readOnlyRoot: false,   // necesario si el root FS es read-only
    // user: "0:0"            // necesario para apt-get (root)
  }
}
```

- Corre **una sola vez** después de crear el container.
- No en cada run.
- Pitfalls comunes:

- `network: "none"` + package install = fallo silencioso
- `readOnlyRoot: true` + writes = fallo
- Non-root user + apt-get = fallo

- ---


## 7.3 Tool Policy: Qué Tools Existen

- Recapitulación del Cap.
- 2 con foco en el contexto multi-agent.


### Las 8 capas de filtrado

```
Layer 1: Tool Profile        (base allowlist)
Layer 2: Provider Profile    (override por modelo/provider)
Layer 3: Global Policy       (tools.allow / tools.deny)
Layer 4: Provider Policy     (tools.byProvider[].allow/deny)
Layer 5: Agent Policy        (agents.list[].tools.allow/deny)
Layer 6: Agent Provider      (agents.list[].tools.byProvider[].allow/deny)
Layer 7: Sandbox Policy      (tools.sandbox.tools.allow/deny)
Layer 8: Subagent Policy     (tools.subagents.tools.allow/deny)
```

- **Cada capa solo puede restringir más.** Un tool denied en Layer 3 no se puede re-habilitar en Layer 5.


### Per-agent overrides

- La clave de multi-agent es que Layers 5-6 permiten **per-agent customization**:


```json5
{
  // Global: coding profile para todos
  tools: { profile: "coding" },

  agents: {
    list: [
      {
        id: "main",
        // Hereda coding profile, sin restricciones adicionales
      },
      {
        id: "work",
        tools: {
          profile: "coding",
          deny: ["browser", "canvas"]   // work no necesita browser
        }
      },
      {
        id: "family",
        tools: {
          profile: "messaging",          // override de profile completo
          allow: ["read", "slack"],      // solo estos + los del profile
          deny: ["exec", "process"]
        }
      },
      {
        id: "public",
        tools: {
          profile: "minimal"            // solo session_status
        }
      }
    ]
  }
}
```

### Sandbox tool policy (Layer 7)

- Cuando un agente corre en sandbox, una capa adicional de policy puede restringir qué tools funcionan **dentro del sandbox**:


```json5
{
  tools: {
    sandbox: {
      tools: {
        allow: ["group:runtime", "group:fs", "group:sessions", "group:memory"],
        deny: ["browser", "canvas", "cron", "gateway"]
      }
    }
  },

  // Per-agent override:
  agents: {
    list: [{
      id: "coding",
      tools: {
        sandbox: {
          tools: {
            allow: ["group:runtime", "group:fs", "group:memory", "group:ui"],
            // coding agent SÍ necesita browser en sandbox
          }
        }
      }
    }]
  }
}
```

- Si `agents.list[].tools.sandbox.tools` está definido, **reemplaza** (no merge) `tools.sandbox.tools` para ese agente.


### Provider-specific tool policy

- Puedes restringir tools según qué modelo/provider se esté usando:


```json5
{
  tools: {
    byProvider: {
      "moonshot/kimi-k2.5": {
        deny: ["browser", "canvas"]    // Kimi no maneja bien browser
      },
      "anthropic": {
        // Anthropic: sin restricciones adicionales
      }
    }
  }
}
```

- **Caso de uso:** Modelos más débiles podrían abusar de tools complejos (browser, exec).
- Restringir tools para modelos de menor capacidad es una mitigación de seguridad.


- ---


## 7.4 Elevated Mode: El Escape Hatch

- Elevated es un mecanismo **específico para exec** que permite escapar del sandbox al host.
- No afecta ningún otro tool.


### Qué hace cada nivel

| Nivel | exec en host | Approvals | Cuándo |
|-------|-------------|-----------|--------|
| `off` (default) | ❌ exec en sandbox | — | Normal operation |
| `on` / `ask` | ✅ exec en host | Respeta security/ask policy | Necesitas acceso al host desde sandbox |
| `full` | ✅ exec en host | Auto-approved | Debugging / emergencia |

### Gates (todo debe pasar)

```
¿tools.elevated.enabled = true?
├── NO → Elevated no disponible
│
└── SÍ → ¿Sender en tools.elevated.allowFrom?
         ├── NO → Elevated no disponible
         │
         └── SÍ → ¿Per-agent gate? (agents.list[].tools.elevated)
                  ├── enabled: false → Elevated no disponible para este agente
                  │
                  └── OK → ¿Sender en per-agent allowFrom?
                           ├── NO → Elevated no disponible
                           └── SÍ → Elevated disponible
```

- **Ambos gates deben pasar:** global Y per-agent.
- El per-agent solo puede restringir más, nunca expandir.


### Configuración

```json5
{
  tools: {
    elevated: {
      enabled: true,
      allowFrom: {
        telegram: ["7192195698"],         // global allowlist por canal
        whatsapp: ["+56912345678"]
      }
    }
  },
  agents: {
    list: [{
      id: "work",
      tools: {
        elevated: {
          enabled: true,                   // per-agent gate (puede ser false)
          allowFrom: {
            telegram: ["7192195698"]       // per-agent allowlist (intersección con global)
          }
        }
      }
    }, {
      id: "family",
      tools: {
        elevated: { enabled: false }       // family NUNCA puede usar elevated
      }
    }]
  }
}
```

### Cuándo usar elevated

| Situación | Elevated necesario |
|-----------|-------------------|
| Agente sin sandbox | ❌ No (ya corre en host) |
| Agente sandboxed que necesita instalar algo en el host | ✅ Sí (temporal, usar `on`) |
| Debugging de servicios del host desde agente sandboxed | ✅ Sí (`full` para velocidad) |
| Operación rutinaria que necesita path del host | ❌ No — usar bind mount |

- ---


## 7.5 Perfiles de Seguridad: Patrones Integrados

- Combinando sandbox + tool policy + elevated, estos son los perfiles coherentes más comunes:


### Perfil: Trust Total (personal)

```json5
{
  id: "main",
  sandbox: { mode: "off" },
  // tools: sin restricciones (full por defecto)
  // elevated: no relevante (ya en host)
}
```
- **Blast radius:** Máximo.
- El modelo tiene acceso total al host. **Cuándo:** Solo tú usas el agente.
- Confías en el modelo y en tu input.


### Perfil: Coding Agent (sandboxed con acceso a código)

```json5
{
  id: "coding",
  sandbox: {
    mode: "all",
    scope: "agent",
    workspaceAccess: "rw",
    docker: {
      binds: ["/home/user/projects:/projects:rw"],
      network: "bridge",
      setupCommand: "apt-get update && apt-get install -y git nodejs npm"
    }
  },
  tools: {
    profile: "coding",
    deny: ["cron", "gateway", "group:messaging"]
  }
}
```
- **Blast radius:** Limitado a container + workspace + /projects. **Cuándo:** Agente que edita código pero no debería tocar el host.


### Perfil: Read-Only Observer

```json5
{
  id: "observer",
  sandbox: { mode: "all", scope: "agent", workspaceAccess: "ro" },
  tools: {
    allow: ["read", "group:memory", "group:sessions", "web_search", "web_fetch"],
    deny: ["exec", "write", "edit", "apply_patch", "process", "browser",
           "canvas", "nodes", "cron", "gateway", "image"]
  }
}
```
- **Blast radius:** Mínimo.
- Solo puede leer y buscar. **Cuándo:** Agente que responde preguntas basándose en memoria y web, sin capacidad de acción.


### Perfil: Messaging-Only

```json5
{
  id: "support",
  sandbox: { mode: "all", scope: "agent", workspaceAccess: "none" },
  tools: {
    profile: "messaging",
    sessions: { visibility: "tree" },
    deny: ["group:fs", "group:runtime", "group:ui", "group:nodes",
           "group:automation", "image"]
  }
}
```
- **Blast radius:** Casi nulo.
- Solo puede enviar mensajes y ver sus propias sesiones. **Cuándo:** Bot de atención/soporte que solo conversa.


### Perfil: Grupo Público (máxima restricción)

```json5
{
  id: "public",
  sandbox: { mode: "all", scope: "session", workspaceAccess: "none" },
  tools: { profile: "minimal" },
  groupChat: { mentionPatterns: ["@bot"] }
}
```
- **Blast radius:** Prácticamente cero.
- Solo `session_status`, aislamiento total por sesión. **Cuándo:** Bot en un grupo público donde cualquiera puede enviar mensajes.


- ---


## 7.6 Precedencia de Config: Per-Agent vs Defaults

### Sandbox

```
agents.list[].sandbox.mode          > agents.defaults.sandbox.mode
agents.list[].sandbox.scope         > agents.defaults.sandbox.scope
agents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccess
agents.list[].sandbox.docker.*      > agents.defaults.sandbox.docker.*
agents.list[].sandbox.browser.*     > agents.defaults.sandbox.browser.*
```

- **Nota:** Per-agent `docker.*` y `browser.*` se ignoran cuando scope resuelve a `"shared"` (un solo container para todos).


### Tool Restrictions

```
Cada capa solo restringe más, nunca re-habilita:

tools.profile            → base allowlist
agents.list[].tools.profile → override completo de base
tools.deny               → global deny (siempre gana)
agents.list[].tools.deny → per-agent deny adicional
tools.sandbox.tools      → sandbox-specific restrictions
agents.list[].tools.sandbox.tools → per-agent sandbox override (reemplaza, no merge)
```

### Elevated

```
tools.elevated.enabled                    → global gate
agents.list[].tools.elevated.enabled      → per-agent gate (ambos deben pasar)
tools.elevated.allowFrom                  → global sender allowlist
agents.list[].tools.elevated.allowFrom    → per-agent allowlist (intersección)
```

- ---


## 7.7 Migración: Single Agent → Multi-Agent

### Antes (single agent implícito)

```json5
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      sandbox: { mode: "non-main" }
    }
  },
  tools: {
    sandbox: {
      tools: { allow: ["read", "write", "exec"], deny: [] }
    }
  }
}
```

### Después (multi-agent explícito)

```json5
{
  agents: {
    defaults: {
      sandbox: { mode: "non-main" }    // herencia para quien no overridea
    },
    list: [
      {
        id: "main",
        default: true,
        workspace: "~/.openclaw/workspace",
        sandbox: { mode: "off" }        // main: host access
      },
      {
        id: "work",
        workspace: "~/.openclaw/workspace-work",
        sandbox: { mode: "all", scope: "agent" },
        tools: { profile: "coding", deny: ["cron", "gateway"] }
      }
    ]
  }
}
```

- **`openclaw doctor` migra automáticamente** configs legacy `agent.*` a `agents.defaults` + `agents.list`.


- ---


## Resumen del Capítulo

| Control | Qué decide | Granularidad |
|---------|-----------|-------------|
| **Sandbox** | Dónde corren los tools (Docker vs host) | Per-agent mode/scope/workspaceAccess |
| **Tool Policy** | Qué tools existen para el modelo | 8 capas, per-agent/provider/sandbox/subagent |
| **Elevated** | Si exec puede escapar del sandbox al host | Global + per-agent gates, sender allowlists |

| Principio | Implicación |
|-----------|------------|
| **Tool policy es el gate principal** | Si denied, nada más importa |
| **Deny siempre gana** | Nunca se re-habilita en capas posteriores |
| **Sandbox ≠ tool restriction** | Sandbox cambia DÓNDE, no QUÉ |
| **Elevated ≠ tool grant** | Elevated solo afecta exec, no habilita tools nuevos |
| **Per-agent solo restringe** | Nunca puede expandir lo que el global denied |
| **`sandbox explain` es tu amigo** | Siempre verificar la policy resuelta |

### Flujo de diagnóstico: "¿por qué mi tool no funciona?"

```
Tool no disponible
      │
      ▼
openclaw sandbox explain --agent <id>
      │
      ├── "tool X blocked by tool policy"
      │   → Revisar tools.deny / agents.list[].tools.deny
      │   → Revisar tools.profile (¿es minimal/messaging?)
      │
      ├── "tool X blocked by sandbox tool policy"
      │   → Revisar tools.sandbox.tools.deny
      │   → O agregar a tools.sandbox.tools.allow
      │
      ├── "session is sandboxed, exec runs in container"
      │   → ¿Necesitas host access? Usar elevated o bind mount
      │   → ¿No debería estar sandboxed? Revisar sandbox.mode
      │
      └── "elevated not available"
          → tools.elevated.enabled = false?
          → Sender no en allowFrom?
          → Per-agent gate bloqueado?
```

- ---


- *Siguiente: [Capítulo 8 — Patrones Multi-Tenant](08-patrones-multitenant.md)*


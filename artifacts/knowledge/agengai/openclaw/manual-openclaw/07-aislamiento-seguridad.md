---
_manifest:
  urn: urn:agengai:kb:07-aislamiento-seguridad
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
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:agengai:kb:07-aislamiento-seguridad
---

# Capítulo 7 — Aislamiento y Seguridad por Agente

> **Propósito:** Entender los tres controles de seguridad per-agent (sandbox, tool policy, elevated) como un sistema integrado. Saber cuál resolver primero cuando algo está bloqueado, y diseñar perfiles de seguridad coherentes para cada agente.

- ---

## 7.1 Los Tres Controles: Vista Unificada

- OpenClaw tiene tres mecanismos de seguridad que trabajan en capas.
- Son **relacionados pero independientes**:

```
┌────────────────────────────────────────────────────────────────┐
│ │
│ 1. SANDBOX "¿DÓNDE corren los tools?" │
│ Docker container vs host │
│ Controla: filesystem, red, procesos │
│ │
│ 2. TOOL POLICY "¿QUÉ tools existen?" │
│ Allow/deny por tool │
│ Controla: qué tools ve el modelo │
│ │
│ 3. ELEVATED "¿PUEDE exec escapar al host?" │
│ Escape hatch para exec │
│ Controla: solo exec, solo desde sandbox │
│ │
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
 "/home/user/source:/source:ro", // código fuente, solo lectura
 "/var/data/myapp:/data:ro" // datos, solo lectura
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
 network: "none" // default: sin red
 }
}
```

- Default: **sin network.** El container no puede hacer requests HTTP, instalar packages, ni conectarse a nada.
- Para skills que necesitan network:

```json5
sandbox: { docker: { network: "bridge" } } // habilita red
```

### setupCommand: provisioning one-time

```json5
sandbox: {
 docker: {
 setupCommand: "apt-get update && apt-get install -y git curl jq",
 network: "bridge", // necesario para apt-get
 // readOnlyRoot: false, // necesario si el root FS es read-only
 // user: "0:0" // necesario para apt-get (root)
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

## Las 8 capas de filtrado

```
Layer 1: Tool Profile (base allowlist)
Layer 2: Provider Profile (override por modelo/provider)
Layer 3: Global Policy (tools.allow / tools.deny)
Layer 4: Provider Policy (tools.byProvider[].allow/deny)
Layer 5: Agent Policy (agents.list[].tools.allow/deny)
Layer 6: Agent Provider (agents.list[].tools.byProvider[].allow/deny)
Layer 7: Sandbox Policy (tools.sandbox.tools.allow/deny)
Layer 8: Subagent Policy (tools.subagents.tools.allow/deny)
```

- **Cada capa solo puede restringir más.** Un tool denied en Layer 3 no se puede re-habilitar en Layer 5.

## Per-agent overrides

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
 deny: ["browser", "canvas"] // work no necesita browser
 }
 },
 {
 id: "family",
 tools: {
 profile: "messaging", // override de profile completo
 allow: ["read", "slack"], // solo estos + los del profile
 deny: ["exec", "process"]
 }
 },
 {
 id: "public",
 tools: {
 profile: "minimal" // solo session_status
 }
 }
 ]
 }
}
```

## Sandbox tool policy (Layer 7)

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

## Provider-specific tool policy

- Puedes restringir tools según qué modelo/provider se esté usando:

```json5
{
 tools: {
 byProvider: {
 "moonshot/kimi-k2.5": {
 deny: ["browser", "canvas"] // Kimi no maneja bien browser
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

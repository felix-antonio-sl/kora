---
_manifest:
  urn: "urn:kora:skill:transmute-openclaw:1.0.0"
  type: lazy_load_endofunctor
name: transmute-openclaw
description: >-
  Transmuta un AGENT.md KORA a un workspace OpenClaw completo (AGENTS.md,
  SOUL.md, USER.md, TOOLS.md, config.json, skills/). Lee las 6 dimensiones
  categoricas del IR y compila cada una al formato nativo de OpenClaw,
  preservando maxima fidelidad. Usar cuando se necesite generar o regenerar
  un agente OpenClaw desde su fuente KORA.
allowed-tools: Read Glob Write Bash
metadata:
  kora:
    urn: "urn:kora:skill:transmute-openclaw:1.0.0"
    lifecycle:
      status: active
      created: "2026-04-14"
      updated: "2026-04-14"
    tools: ["Read", "Glob", "Write", "Bash"]
    knowledge: ["urn:kora:kb:agentfile-spec", "urn:kora:kb:transmutation-spec"]
    composable_with: []
    domain: ["transmutacion", "openclaw"]
    level: L2
---

# CM-TRANSMUTE-OPENCLAW

## Proposito

Transmutar un AGENT.md KORA (IR de 6 dimensiones categoricas) a un workspace
OpenClaw completo con archivos bootstrap separados. La transmutacion es un
funtor T: IR -> OpenClaw que preserva composicion e identidad con fidelidad
maxima, ya que OpenClaw soporta nativamente la estructura del workspace KORA.

## Input/Output

**Input:**
- Path a un directorio de agente KORA con AGENT.md
- Directorio de output (default: BUILD/openclaw/{namespace}/{agent-name}/)

**Output:**
- Workspace completo en BUILD/openclaw/{namespace}/{agent-name}/:
  - workspace/AGENTS.md
  - workspace/SOUL.md
  - workspace/USER.md
  - workspace/TOOLS.md
  - workspace/skills/ (skills referenciados copiados)
  - config/openclaw.json5
  - DEPLOY.md
- Archivo _transmutation.yml con registro de fidelidad

## Procedimiento

### 1. Leer fuente

Leer AGENT.md del agente. Parsear YAML frontmatter. Extraer las 6 dimensiones
bajo `agent.*` y los campos de identity/lifecycle. Leer tambien el body
markdown del AGENT.md (secciones ## despues del frontmatter).

### 2. Compilar workspace/AGENTS.md

Desde agent.plan (FSM) y agent.coalgebra:

```markdown
# {agent.name}

## 1. FSM

STATE: S-DISPATCHER
Act: {states[0].act}
Trans:
{para cada transicion en estados, ordenadas por priority:}
  - IF {condition} -> {target} [prioridad {priority}]

{repetir para cada estado}

STATE: S-END
Act: Emitir output final
Trans: (terminal)
```

Desde agent.plan (reglas, co-induccion, contexto):

```markdown
## 2. Reglas Duras

Dominio permitido: {agent.safety.hard_rules.scope.allowed}
Dominio prohibido: {agent.safety.hard_rules.scope.forbidden}
Rechazo: "{agent.safety.hard_rules.scope.rejection}"

{para cada constraint en agent.plan.hard_rules o agent.safety.hard_rules.constraints:}
- {constraint}

## 3. Co-induccion Terminal

{para cada check en agent.safety.co_induction.pre_output_checks:}
- **{check.id}**: {check.description}
  - Si falla: {check.on_fail}

## 4. Contexto Multi-turno

{contenido de agent.plan.multi_turn si existe, verbatim}

## 5. Wiring

Tipo: {agent.composition.type}
{si agent.composition.sub_agents existe:}
Sub-agentes:
{para cada sub_agent: "- {urn} ({role})"}
{si agent.composition.dependencies existe:}
Dependencias:
{para cada dep: "- {dep}"}
```

Si el AGENT.md tiene body con secciones ## Behavior, incluir su contenido
como seccion adicional (## 6. Comportamiento Operativo). Preservar verbatim.

### 3. Compilar workspace/SOUL.md

Desde agent.fibers.identity:

```markdown
# {agent.name}

## Identidad Dialectica

{agent.fibers.identity.dialectical_identity o description del coalgebra}

## Paradigma Cognitivo

{agent.fibers.identity.paradigm}

## Tono

{agent.fibers.identity.tone}

## Voz

{agent.fibers.identity.voice si existe}
```

### 4. Compilar workspace/USER.md

Desde agent.fibers.operator:

```markdown
# Operador

## Perfil

Rol: {agent.fibers.operator.role}

{agent.fibers.operator.context si existe}

## Preferencias de output

{agent.fibers.operator.output_preferences si existe}

## Rutinas

{agent.fibers.operator.routines si existe, como lista}
```

Si agent.fibers.operator no existe o esta vacio, crear USER.md minimo:

```markdown
# Operador

(sin contexto de operador declarado)
```

### 5. Compilar workspace/TOOLS.md

Desde agent.interface:

```markdown
# Tools

{para cada tool en agent.interface.tools:}
## {tool.name}

{tool.description}

**Firma:** {tool.signature si existe}
**Cuando usar:** {tool.when_to_use}
**Cuando NO usar:** {tool.when_not_to_use}

{si agent.interface.kb_routes existe:}
## Routing Map

| Topic | URN |
|-------|-----|
{para cada route: "| {topic} | {urn} |"}
```

### 6. Compilar workspace/skills/

Para cada CM-* referenciado en la FSM (agent.plan.states[].act):

1. Extraer nombre del skill (CM-{NAME})
2. Buscar en SKILLS/ del agente fuente: AGENTS/{ns}/{name}/skills/
3. Si existe, copiar el SKILL.md (o directorio completo si es extendido)
   a workspace/skills/
4. Si no existe en el agente, buscar en SKILLS/kora/ o SKILLS/{ns}/
5. Si no se encuentra, emitir warning pero no fallar

### 7. Compilar config/openclaw.json5

Desde agent.safety y agent.fibers.runtime:

```json5
{
  // Generated by KORA transmutation — do not edit manually
  "agent": "{ns}/{name}",
  "version": "{frontmatter.version}",
  "sandbox": {
    "mode": "{agent.safety.sandbox.mode}"
  },
  "tools": {
    "allow": ["{lista de agent.interface.tools[].name}"],
    "deny": ["{agent.safety.tools.deny si existe}"]
  },
  "runtime_capabilities": ["{agent.safety.runtime_capabilities}"],
  "limits": {
    // de agent.safety.limits si existe
  },
  "model_routing": {
    // de agent.fibers.runtime.model_routing si existe
  },
  "sub_agents": {
    // de agent.composition.sub_agents si existe
  }
}
```

### 8. Generar DEPLOY.md

Guia de deployment minima:

```markdown
# Deploy: {ns}/{name}

Workspace generado por transmutacion KORA.

## Instrucciones

1. Copiar contenido de `workspace/` al directorio del agente en el gateway
2. Copiar `config/openclaw.json5` a la config del gateway
3. Registrar agente en el gateway: `openclaw agent add {ns}/{name}`
4. Verificar: `openclaw doctor`

## Fuente

- IR: AGENTS/{ns}/{name}/AGENT.md
- Transmutado: {timestamp ISO-8601}
- Hash fuente: {sha256}
```

### 9. Escribir output

Escribir todos los archivos al directorio de output:

```
BUILD/openclaw/{ns}/{name}/
  workspace/
    AGENTS.md
    SOUL.md
    USER.md
    TOOLS.md
    skills/
      CM-*.md (o directorios)
  config/
    openclaw.json5
  DEPLOY.md
```

Crear directorios si no existen.

### 10. Registrar transmutacion

Escribir _transmutation.yml junto al directorio generado:

```yaml
source: AGENTS/{namespace}/{agent-name}/AGENT.md
source_hash: {sha256 del AGENT.md}
target: openclaw
target_path: BUILD/openclaw/{namespace}/{agent-name}/
adapter: CM-TRANSMUTE-OPENCLAW
timestamp: {ISO-8601}
version: {agent.version}
fidelity:
  dim_1_coalgebra: preserved
  dim_2_plan: preserved
  dim_3_interface: preserved
  dim_4_fibers:
    identity: preserved
    operator: preserved
    memory: preserved
    runtime: degraded
    knowledge: preserved
  dim_5_composition: preserved
  dim_6_safety: preserved
losses:
  - "dim_4.runtime: lifecycle (heartbeat, cron) y dissipation requieren config manual en openclaw.json5; no automatizables desde la IR"
```

## Signature Output

Directorio completo con workspace + config:

1. `BUILD/openclaw/{ns}/{name}/workspace/` — workspace bootstrap completo
   con AGENTS.md, SOUL.md, USER.md, TOOLS.md, skills/

2. `BUILD/openclaw/{ns}/{name}/config/openclaw.json5` — configuracion de
   plataforma compilada desde dimensions Safety y Runtime

3. `BUILD/openclaw/{ns}/{name}/DEPLOY.md` — guia de deployment

4. `BUILD/openclaw/{ns}/{name}._transmutation.yml` — registro de fidelidad
   con hashes, timestamp y perdidas documentadas

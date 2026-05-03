---
_manifest:
  urn: "urn:kora:skill:transmute-claude-code:1.0.0"
  type: lazy_load_endofunctor
name: transmute-claude-code
description: >-
  Transmuta un AGENT.md KORA a un archivo .md de Claude Code (persona o
  subagente). Lee las 6 dimensiones categoricas del IR y compila cada una
  al idiom de Claude Code, preservando maxima fidelidad. Usar cuando se
  necesite generar o regenerar un agente Claude Code desde su fuente KORA.
allowed-tools: Read Glob Write Bash
metadata:
  kora:
    urn: "urn:kora:skill:transmute-claude-code:1.0.0"
    lifecycle:
      status: active
      created: "2026-04-14"
      updated: "2026-04-14"
    tools: ["Read", "Glob", "Write", "Bash"]
    knowledge: ["urn:kora:kb:agentfile-spec", "urn:kora:kb:transmutation-spec"]
    composable_with: []
    domain: ["transmutacion", "claude-code"]
    level: L2
---

# CM-TRANSMUTE-CLAUDE-CODE

## Purpose

Transmutar un AGENT.md KORA (IR de 6 dimensiones categoricas) a un archivo
.md con YAML frontmatter consumible por Claude Code como persona o subagente.
La transmutacion es un funtor T: IR -> Claude Code que preserva composicion
e identidad, documentando explicitamente toda perdida de fidelidad.

## Input/Output

**Input:**
- Path a un directorio de agente KORA con AGENT.md
- Target mode: persona | subagent (default: persona)

**Output:**
- Archivo .md en BUILD/claude-code/{namespace}/{agent-name}.md
- Archivo _transmutation.yml con registro de fidelidad

## Procedure

### 1. Leer fuente

Leer AGENT.md del agente. Parsear YAML frontmatter. Extraer las 6 dimensiones
bajo `agent.*` y los campos de identity/lifecycle.

### 2. Generar YAML frontmatter Claude Code

```yaml
---
name: {agent.name, lowercase, sin namespace}
description: {agent.coalgebra.description}
tools: {lista de agent.interface.tools[].name}
model: {agent.fibers.runtime.model o "claude-sonnet-4-6"}
memory: {si agent.fibers.memory.mode == "session" -> "user", else omitir}
effort: high
---
```

Campos opcionales segun disponibilidad:
- `maxTurns`: de agent.fibers.runtime.limits.max_turns si existe
- `color`: de agent.extensions.claude.color si existe

### 3. Compilar body — seccion Identidad

Desde agent.fibers.identity:

```markdown
Eres **{name}** — {agent.coalgebra.description}.

{agent.fibers.identity.paradigm}

Tono: {agent.fibers.identity.tone}
```

Si agent.fibers.identity.voice existe, incluir como parrafo adicional.

### 4. Compilar body — seccion Behavior

Desde agent.plan (FSM):

Para cada estado en agent.plan.states (excepto terminal):
1. Crear un parrafo con heading implicito del act
2. Convertir transiciones a condicionales:
   - Ordenar por priority (1 = primero)
   - Cada transicion: "Si {condition} -> {descripcion de target.act}"
3. Preservar la logica completa, no simplificar

Si el AGENT.md tiene body `## Behavior`, incluir su contenido despues de la
FSM compilada. Preservar tal cual — no resumir.

### 5. Compilar body — seccion Knowledge

Desde agent.fibers.knowledge:

```markdown
## Corpus autorizado

Conocimiento primario:
{para cada urn en allowed_kb: "- `{urn}`"}

{Si kb_routes existe: tabla de routing topic -> URN}

NO tienes acceso a dominios fuera de {agent.safety.hard_rules.scope.allowed}.
```

### 6. Compilar body — seccion Tools

Desde agent.interface.tools:

Para cada tool, incluir:
```markdown
### {tool.name}
{tool.description}
- **Cuando usar:** {tool.when_to_use}
- **Cuando NO usar:** {tool.when_not_to_use}
```

### 7. Compilar body — seccion Safety

Desde agent.safety:

```markdown
## Reglas absolutas

Dominio permitido: {hard_rules.scope.allowed}
Dominio prohibido: {hard_rules.scope.forbidden}
Rechazo: "{hard_rules.scope.rejection}"

{Para cada constraint en hard_rules.constraints: "- {constraint}"}

## Antes de cada respuesta

{Para cada check en co_induction.pre_output_checks:
"- **{check.id}**: {check.description}. Si falla: {check.on_fail}."}
```

### 8. Compilar body — seccion Composition

Desde agent.composition:

Si hay sub_agents:
```markdown
## Delegacion
{Para cada sub_agent: "- Delegar a `{urn}` ({role}) cuando corresponda"}
```

### 9. Compilar body — seccion Context

Si el AGENT.md tiene body `## Context`, incluirlo tal cual.
Si agent.fibers.operator existe:
```markdown
## Contexto del operador
Rol: {operator.role}
{operator.context}
```

### 10. Escribir output

Escribir el .md compilado a BUILD/claude-code/{namespace}/{agent-name}.md.

Crear BUILD/claude-code/{namespace}/ si no existe.

### 11. Registrar transmutacion

Escribir _transmutation.yml junto al archivo generado:

```yaml
source: AGENTS/{namespace}/{agent-name}/AGENT.md
source_hash: {sha256 del AGENT.md}
target: claude-code
target_path: BUILD/claude-code/{namespace}/{agent-name}.md
timestamp: {ISO-8601}
version: {agent.version}
fidelity:
  dim_1_coalgebra: degraded
  dim_2_plan: degraded
  dim_3_interface: preserved
  dim_4_fibers:
    identity: preserved
    operator: preserved
    memory: partial
    runtime: partial
    knowledge: degraded
  dim_5_composition: degraded
  dim_6_safety: degraded
losses:
  - "FSM compilada a prosa — no verificable en runtime Claude Code"
  - "Knowledge boundaries como instruccion, no como enforcement server-side"
  - "Co-induccion checks como instrucciones, no enforcement"
  - "Composition como prosa descriptiva, sin contratos verificables"
```

## Signature Output

Dos archivos:

1. `BUILD/claude-code/{ns}/{name}.md` — archivo .md con YAML frontmatter
   Claude Code + body con behavior compilado

2. `BUILD/claude-code/{ns}/{name}._transmutation.yml` — registro de
   fidelidad con hashes, timestamp y perdidas documentadas

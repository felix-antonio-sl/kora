---
_manifest:
  urn: "urn:kora:kb:claude-code-runtime-extension"
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "harness-spec v1.0; transmutation-spec v1.0; revisión docs oficiales Claude Code (claude.ai/code) y marketplace de plugins"
version: "1.0.0"
status: publicado
tags: [spec, runtime, claude-code, extension, transmutacion, proyeccion]
lang: es
extensions:
  kora:
    precedence_tier: 4
    platform: "claude-code"
    baseline_docs_release: "2026.4"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
---

# KORA/Claude-Code-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el target **Claude Code**
(CLI desktop/web). Define el dominio de soporte, la matriz de fidelidad de
proyeccion, y la metadata de encaje runtime-especifica.

### 1.1 Alcance

Gobierna:

1. Proyeccion `T_{claude-code}: KORA_IR → Claude_Code` segun
   `transmutation-spec`.
2. Formas materiales soportadas por Claude Code (skill estandar,
   subagente Task, agente persona).
3. Metadata runtime-especifica (model, memory, color, max_turns,
   plugin.json, marketplace.json).
4. Encaje de agentskills.io (formato cross-runtime) + overlay Claude Code.

## 2. Formas materiales soportadas

| Forma material (atlas B) | Ubicacion runtime | Frontmatter |
|----------------------------|----------------------|--------------|
| Skill estandar | `~/.claude/skills/{name}/` o `./.claude/skills/` | `name, description, allowed-tools` |
| Subagente Task | `~/.claude/agents/{name}.md` | `name, description, tools, model, color, max_turns` |
| Agente persona principal | workspace con instrucciones | `name, description, tools, model, memory, effort, color, max_turns` |
| Plugin (bundle) | `.claude-plugin/plugin.json` + skills/commands/agents | segun plugin.json schema |

## 3. Matriz de preservacion por eje

Dominio soportado y fidelidad de `T_{claude-code}`:

### 3.1 Eje Π (plan)

```yaml
pi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 2, fidelity: partial, loss: "fixed-points se aplanan al FSM plano; recursion semantica puede no preservarse" }
```

### 3.2 Eje Μ (materia)

```yaml
mu:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "scratchpad via Task tool subagent" }
  "2": { projected: 2, fidelity: full, comment: "memory: user persiste cross-session" }
  "3": { projected: null, fidelity: none, loss: "Claude Code no soporta ambiente externo always-on. Usar openclaw para Μ=3." }
```

### 3.3 Eje Ξ (interaccion)

```yaml
xi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 2, fidelity: partial, loss: "protocolos multi-fase coreografiados no modelados explicitamente; se aplanan a lente polinomial simple" }
  "4": { projected: 2, fidelity: partial, loss: "operad dinamica (delegacion jerarquica con feedback) no soportada nativamente; se proyecta como persona con sub-agentes via Task" }
```

### 3.4 Eje Λ (nivel sociotecnico)

```yaml
lambda:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "workspace organizacional via project-scope" }
  "2": { projected: 1, fidelity: partial, loss: "ecosistema cross-org se proyecta como organizacional" }
  "3": { projected: null, fidelity: none, loss: "society-in-the-loop no tiene mecanismo runtime nativo" }
```

### 3.5 Eje Φ (acoplamiento humano-AI)

```yaml
phi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "tool metaphor — conversacion directa" }
  "2": { projected: 2, fidelity: full, comment: "conversacion colaborativa con liderazgo humano" }
  "3": { projected: 2, fidelity: partial, loss: "hybrid cognition no modelado nativamente; se proyecta como persona colaborativa" }
  "4": { projected: null, fidelity: none, loss: "co-evolutivo no soportado" }
```

### 3.6 Eje Σ (vector etico)

```yaml
sigma:
  safety_norm:
    max_supported: 3
    enforcement: "policy-based (hard_rules del agente, plan mode default)"
  fairness:
    max_supported: 2
    enforcement: "declarative (bias audits, no enforcement runtime)"
  transparency:
    max_supported: 3
    enforcement: "explainable-output (reasoning visible, thinking budget)"
  accountability:
    max_supported: 2
    enforcement: "conversation-history + git-log; no audit trail persistente cross-session salvo memory"
  sustainability:
    max_supported: 1
    enforcement: "declarative only"
```

## 4. Metadata de encaje runtime

Un artefacto KORA proyectado a Claude Code puede declarar metadata
especifica en `extensions.claude_code.*`:

```yaml
extensions:
  claude_code:
    # Modelo
    model: opus | sonnet | haiku
    # Razonamiento
    effort: xhigh | high | medium | low
    # UI y presentacion
    color: purple | blue | green | ...
    # Persistencia
    memory: user | project | none
    # Budget de turnos
    max_turns: 15
    # Herramientas declaradas (cross-runtime agentskills.io)
    tools: [Read, Write, Bash, WebSearch, ...]
    # Plan mode default
    permissions:
      defaultMode: plan | accept | review
    # Hooks
    hooks:
      preToolUse: "command to run before tool execution"
      postToolUse: "command to run after"
```

Campos soportados adicionales segun evolucion del runtime — consultar
documentacion oficial.

## 5. Protocolo ACP (Agent Client Protocol)

Claude Code es un ACP backend (`acp.allowedAgents[]` en openclaw
configuration). Un artefacto KORA que es ACP-compliant puede invocarse via
ACP desde OpenClaw gateway o equivalente.

Declaracion:

```yaml
extensions:
  kora:
    acp_compliant: true
    acp_backend: claude
```

## 6. Encaje con plugin marketplace

Claude Code soporta plugins via `.claude-plugin/plugin.json`. Un bundle de
artefactos KORA puede empaquetarse como plugin:

```json
{
  "name": "kora-meta-agents",
  "description": "Operating core agents del monorepo KORA",
  "version": "1.0.0",
  "author": { "name": "felix" },
  "homepage": "https://github.com/felix-antonio-sl/kora",
  "repository": "https://github.com/felix-antonio-sl/kora",
  "license": "MIT",
  "skills": "./skills",
  "agents": "./agents",
  "commands": "./commands"
}
```

La transmutacion a plugin es una composicion de `T_{claude-code}` por cada
artefacto + empaquetado como bundle. `_transmutation.yml` se emite por
artefacto individual.

## 7. Dominio de invocacion

Claude Code distingue tres modos de invocacion para los artefactos:

| Modo | Trigger | Forma material | Vector tipico |
|------|---------|----------------|----------------|
| Conversacion persona | Usuario abre conversacion | Agente persona | Π=2, Μ=2, Ξ=2, Φ=2 |
| Subagente Task | Tool `Task()` con `subagent_type` | Subagente | Π=2, Μ=1, Ξ=2, Φ=1 |
| Skill auto-activado | Description match | Skill estandar | Π≤2, Μ=0, Ξ=1 |
| Command slash | Usuario escribe `/cmd` | Skill con trigger explicito | Π≤2, Μ=0, Ξ=1 |

Cada modo consume distinta region del dominio soportado.

## 8. Reglas de transmutacion

Obligatorias:

1. Todo artefacto transmutado a Claude Code **DEBE** emitir
   `_transmutation.yml` conforme `transmutation-spec §6`.
2. El output vive en `{workspace}/_BUILD/claude-code/` (gitignored per
   runtime-spec-md).
3. Las leyes functoriales basicas (`transmutation-spec §3`) se preservan
   estrictamente.
4. Si el vector IR excede el dominio (p. ej. Μ=3), la transmutacion **debe
   fallar** con mensaje claro. No degradar silenciosamente.
5. Vectores que exceden el dominio se proyectan con perdida declarada en
   `_transmutation.yml`.

## 9. Ingesta inversa (`Lift_{claude-code}`)

Claude Code soporta ingesta parcial. Un subagente Claude Code
(`~/.claude/agents/*.md`) puede elevarse a `AGENT.md` KORA:

```bash
kora ingest --from claude-code --file ~/.claude/agents/polymath.md --namespace kora
```

### 9.1 Mapeo de campos

| Campo Claude Code | Destino KORA IR |
|-------------------|------------------|
| `name` | `_manifest.urn` slug |
| `description` | `_manifest.provenance.source` + `agent.profile.description` |
| `tools` | `agent.interface.allowed_tools` |
| `model` | `extensions.claude_code.model` |
| `memory: user` | proyecta a `harness_vector.mu: 2` |
| `memory: none/absent` | proyecta a `harness_vector.mu: 0` si Task subagent, `1` si default |
| `effort` | `extensions.claude_code.effort` |
| `color` | `extensions.claude_code.color` |
| `max_turns` | `extensions.claude_code.max_turns` + influye `harness_vector.mu` (≤5 efimero, >5 persistente si memory:user) |
| Body markdown | `agent.profile` + `agent.plan` (derivado) |

### 9.2 Limitaciones

- No todos los campos shape v2 son derivables automaticamente del archivo
  Claude Code.
- `harness_vector.pi` se infiere heuristicamente del body (ramificacion
  explicita).
- `harness_vector.sigma` se asigna valores por defecto
  `[1, 1, 2, 1, 0]` — el autor debe ajustar.
- `harness_vector.phi` default 1 (instrumental) — ajustar si
  colaborativo/hibrido.
- Adjuncion `Lift ⊣ T` es aproximada; no hay round-trip exacto.

## 10. Validacion

Checks aplicables:

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| Vector dentro del dominio | Vector IR ∈ `D_{claude-code}` | lint |
| `_transmutation.yml` presente | Output target incluye artifact | lint |
| Metadata runtime completa | `extensions.claude_code.*` coherente | lint |
| Matriz de preservacion vigente | Valor de matriz coincide con runtime version | manual |
| Plugin schema conforme | Si transmuta a plugin, `plugin.json` valido | lint |

## 11. Contrato vigente v1

- Claude Code soporta {Utilidad, Disciplina, Delegado, Persona} del atlas A.
- NO soporta {Servicio} — usar OpenClaw para Μ=3.
- Soporta Orquestador parcialmente — proyecta a Persona con sub-agentes Task.
- Approval modes: plan (default) / accept / review.
- Dominio completo: Π ≤ 2, Μ ≤ 2, Ξ ≤ 2, Λ ≤ 1, Φ ≤ 2, Σ variable.
- Ingesta inversa disponible para subagentes (`Lift` parcial).

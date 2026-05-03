---
_manifest:
  urn: "urn:kora:kb:gemini-runtime-extension"
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "harness-spec v1.0; transmutation-spec v1.0; Gemini CLI docs + agentskills-upstream/GEMINI.md; ClawHub publishing constraints"
version: "1.0.0"
status: publicado
tags: [spec, runtime, gemini, extension, transmutacion, proyeccion, clawhub]
lang: es
extensions:
  kora:
    family: spec
    precedence_tier: 4
    platform: "gemini"
    baseline_docs_release: "2026.4"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
---

# KORA/Gemini-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el target **Gemini CLI**
(Google). Define dominio de soporte, matriz de fidelidad, mecanismo
`activate_skill`, y encaje con ClawHub como registry de distribucion.

### 1.1 Alcance

Gobierna:

1. Proyeccion `T_{gemini}: KORA_IR → Gemini` segun `transmutation-spec`.
2. Skills invocables via `activate_skill(name)` de Gemini CLI.
3. Encaje con ClawHub registry (constraints de publicacion).
4. Agents y Commands con estructura analoga a Claude Code.

## 2. Formas materiales soportadas

| Forma material | Ubicacion | Frontmatter |
|----------------|------------|--------------|
| Skill con SKILL.md | carpeta de dominio (p. ej. `engineering-team/{skill}/SKILL.md`) | `name, description` |
| Agent (subagente persona) | `agents/{name}.md` | `name, description` + body |
| Command | `commands/{name}.md` | `name, description` |
| Plugin/Bundle | `.claude-plugin/plugin.json` (compatible) | schema plugin.json |

## 3. Matriz de preservacion por eje

### 3.1 Eje Π (plan)

```yaml
pi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 2, fidelity: partial, loss: "fixed-points no soportados nativamente" }
```

### 3.2 Eje Μ (materia)

```yaml
mu:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "scratchpad intra-invocacion" }
  "2": { projected: 1, fidelity: partial, loss: "Gemini CLI tiene conversation history pero memory: user transparente cross-session es limitado (requiere explicit resume o context-file)" }
  "3": { projected: null, fidelity: none, loss: "Gemini CLI no es daemon always-on" }
```

### 3.3 Eje Ξ (interaccion)

```yaml
xi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 2, fidelity: partial, loss: "protocolos multi-fase se aplanan" }
  "4": { projected: 2, fidelity: partial, loss: "operad dinamica no soportada" }
```

### 3.4 Eje Λ

```yaml
lambda:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 1, fidelity: partial }
  "3": { projected: null, fidelity: none }
```

### 3.5 Eje Φ

```yaml
phi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 2, fidelity: partial }
  "4": { projected: null, fidelity: none }
```

### 3.6 Eje Σ

```yaml
sigma:
  safety_norm:
    max_supported: 3
    enforcement: "policy-based + Google safety filters"
  fairness:
    max_supported: 2
    enforcement: "declarative"
  transparency:
    max_supported: 2
    enforcement: "reasoning output; limitado"
  accountability:
    max_supported: 1
    enforcement: "conversation logs; no audit trail cross-session transparente"
  sustainability:
    max_supported: 1
    enforcement: "declarative"
```

## 4. Metadata de encaje runtime

```yaml
extensions:
  gemini:
    # Modelo
    model: gemini-3.1-pro-preview | gemini-3.1-flash | ...
    # Auth
    auth_type: oauth-personal | api-key
    # Approval
    approval_mode: yolo | normal | strict
    # Skill activation
    activation: "activate_skill" | "slash-command"
    # UI preference
    theme: "Default Light" | "Default Dark"
    # Project context
    gemini_md: "GEMINI.md"  # analogo a CLAUDE.md
```

## 5. `activate_skill` como patron de invocacion

Gemini CLI usa `activate_skill(name)` como mecanismo explicito de carga de
skill, distinto del matching semantico puro. Esto es un modo de invocacion
formal que se proyecta como:

```yaml
invocation:
  semantic_match: true        # discovery por description
  explicit_activation: true   # activate_skill(name)
  slash_command: true         # /cmd equivalente
```

## 6. Encaje con ClawHub (registry de distribucion)

Skills Gemini pueden publicarse en **ClawHub** (clawhub.com) como registry
publico. El encaje con KORA requiere respetar constraints de publicacion:

### 6.1 Constraints ClawHub

- **Prefijo `cs-`** solo cuando hay conflicto de slug en el registry (no
  afecta repo local).
- **No paid/commercial dependencies** — skills no pueden requerir API keys
  pagas o servicios comerciales externos.
- **plugin.json minimo**: `{name, description, version, author, homepage,
  repository, license, skills: "./"}`.
- **Rate limit**: 5 new skills/hour; usar drip publishing para bulk.

### 6.2 Declaracion en vector

Un skill apto para ClawHub declara:

```yaml
extensions:
  distribution:
    clawhub_publishable: true
    plugin_json: ".claude-plugin/plugin.json"
    license: "MIT"
    no_paid_deps: true
```

### 6.3 Proyeccion a plugin

Un bundle de artefactos KORA se proyecta a plugin ClawHub-compatible:

```json
{
  "name": "kora-skills-pack",
  "description": "...",
  "version": "1.0.0",
  "author": { "name": "felix" },
  "homepage": "...",
  "repository": "...",
  "license": "MIT",
  "skills": "./"
}
```

## 7. Protocolo ACP

Gemini es ACP backend (`acp.allowedAgents[]`). Un artefacto KORA
ACP-compliant puede invocarse via Gemini desde OpenClaw gateway.

## 8. GEMINI.md como context file

Gemini CLI usa `GEMINI.md` como analogo a `CLAUDE.md` — contexto de proyecto.
Un repo KORA puede incluir `.gemini/GEMINI.md` o raiz `GEMINI.md` que
proyecta la semantica de `CLAUDE.md` al lenguaje Gemini.

No es parte del IR — es metadata de repo compartida con el runtime Gemini.

## 9. Dominio de invocacion

| Modo | Trigger | Vector tipico |
|------|---------|----------------|
| Skill activation | `activate_skill(name)` | Π≤2, Μ=0, Ξ=1 |
| Slash command | `/cmd` | Π≤2, Μ=0, Ξ=1 |
| Conversation | session CLI | Π=2, Μ=1, Ξ=2 |
| Agent invocation | invocar `agents/*.md` | Π=2, Μ=1 parcial, Ξ=2 |

## 10. Reglas de transmutacion

Obligatorias:

1. `_transmutation.yml` emitido.
2. Output en `{workspace}/_BUILD/gemini/`.
3. Si skill es ClawHub-destinado, validar constraints de publicacion (§6.1).
4. Progressive disclosure y estructura `scripts/references/assets`
   mantenidas (cross-runtime).

## 11. Ingesta inversa (`Lift_{gemini}`)

Skills Gemini elevables:

```bash
kora ingest --from gemini --file path/to/SKILL.md
```

Mapeo analogo al de Codex/Claude Code. Default `vector_ontologico` para
skills ingestados: `(Π=2, Μ=0, Ξ=1, Λ=0, Φ=1, Σ=[1,1,2,1,0])`.

### 11.1 Trace fidelity

```yaml
trace_fidelity:
  level: pendiente
  capture_mechanism: "por documentar en gemini-runtime-extension"
  notes: "no cerrar verificacion estricta de trazabilidad hasta completar mecanismo estable"
```

## 12. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| Vector dentro del dominio | Vector IR ∈ `D_{gemini}` | lint |
| `_transmutation.yml` presente | Output target incluye artifact | lint |
| ClawHub constraints | Si publishable, cumple §6.1 | lint |
| plugin.json valido | Schema minimo cumplido | schema |
| Progressive disclosure | Body ≤ 500 lineas | lint |

## 13. Contrato vigente v1.0.0

- Gemini CLI soporta {Utilidad, Disciplina, Delegado} completos.
- Soporta {Persona} parcial (session-limited).
- NO soporta {Orquestador, Servicio, Arquetipo} nativamente.
- Dominio completo: Π ≤ 2, Μ ≤ 1 (Μ=2 parcial), Ξ ≤ 2, Λ ≤ 1, Φ ≤ 2.
- ClawHub constraints aplicables si publishable.
- ACP-compliant como backend en OpenClaw.

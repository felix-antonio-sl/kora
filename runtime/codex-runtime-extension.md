---
_manifest:
  urn: "urn:kora:kb:codex-runtime-extension"
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "harness-spec v1.0; transmutation-spec v1.0; Codex skill-creator oficial (~/.codex/skills/.system/skill-creator/SKILL.md); OpenAI Codex CLI docs 2026.4"
version: "1.0.0"
status: publicado
tags: [spec, runtime, codex, extension, transmutacion, proyeccion]
lang: es
extensions:
  kora:
    precedence_tier: 4
    platform: "codex"
    baseline_docs_release: "2026.4"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
---

# KORA/Codex-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el target **OpenAI Codex
CLI** (`codex` binary). Define dominio de soporte, matriz de fidelidad,
modos de aprobacion y metadata de encaje runtime-especifica.

### 1.1 Alcance

Gobierna:

1. Proyeccion `T_{codex}: KORA_IR → Codex` segun `transmutation-spec`.
2. Skills estilo `~/.codex/skills/{name}/` con `scripts/references/assets`
   + `agents/openai.yaml` (UI metadata).
3. Agent mode de Codex (CLI subagent + session resumible).
4. Approval modes (`auto-suggest`, `auto-edit`, `auto-all`,
   `danger-full-access`) y trust levels por proyecto.

## 2. Formas materiales soportadas

| Forma material | Ubicacion runtime | Frontmatter |
|----------------|----------------------|--------------|
| Skill estandar | `~/.codex/skills/{name}/` o `./.codex/skills/` | `name, description` (minimo agentskills.io) |
| Skill con UI metadata | mismo + `agents/openai.yaml` | `display_name, short_description, default_prompt` |
| Agent mode CLI | via `codex exec` / `codex resume <id>` | session resumible, memoria acotada a resume |

Codex **NO soporta nativamente**:
- Personas persistentes cross-session transparentes (`memory: user` a la
  Claude Code).
- Orquestadores con golden_paths explicitos.
- Servicios always-on (no es daemon).
- Forgemaster/scaffold generator (parcial via skill-creator).

## 3. Matriz de preservacion por eje

### 3.1 Eje Π (plan)

```yaml
pi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: partial, loss: "Codex permite recursion via tool use pero con budget explicito; fixed-points profundos pueden exceder turns acotados" }
```

### 3.2 Eje Μ (materia)

```yaml
mu:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "scratchpad intra-invocacion via agent mode" }
  "2": { projected: 1, fidelity: partial, loss: "Codex tiene session-resumable via `codex resume <id>`, pero no memory: user transparente cross-session. Persistencia requiere session-id conocido." }
  "3": { projected: null, fidelity: none, loss: "Codex es CLI sincrono, no daemon. Μ=3 ambiental no soportado." }
```

### 3.3 Eje Ξ (interaccion)

```yaml
xi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 2, fidelity: partial, loss: "protocolos multi-fase se aplanan a lentes simples" }
  "4": { projected: 2, fidelity: partial, loss: "operad dinamica no soportada; composicion via `composable_with` en skills queda declarativa" }
```

### 3.4 Eje Λ (nivel sociotecnico)

```yaml
lambda:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "organizacional via project trust levels + skills compartidos" }
  "2": { projected: 1, fidelity: partial, loss: "ecosistema colapsa a organizacional" }
  "3": { projected: null, fidelity: none, loss: "society-in-the-loop no soportado" }
```

### 3.5 Eje Φ (acoplamiento humano-AI)

```yaml
phi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "tool metaphor — default" }
  "2": { projected: 2, fidelity: partial, comment: "collaborative via session-resumable + approval modes, pero sin identidad persistente transparente" }
  "3": { projected: 2, fidelity: partial, loss: "hybrid cognition no soportado nativamente" }
  "4": { projected: null, fidelity: none, loss: "co-evolutivo no soportado" }
```

### 3.6 Eje Σ (vector etico)

```yaml
sigma:
  safety_norm:
    max_supported: 3
    enforcement: "sandbox modes (danger-full-access a auto-suggest) + approval gates"
  fairness:
    max_supported: 2
    enforcement: "declarative"
  transparency:
    max_supported: 2
    enforcement: "output logs + conversation history"
  accountability:
    max_supported: 2
    enforcement: "session-id trackable + logs_2.sqlite; no audit trail cross-session transparente"
  sustainability:
    max_supported: 1
    enforcement: "declarative"
```

## 4. Approval modes y sandbox (dimension runtime ortogonal)

Codex introduce **approval modes** que afectan la ejecucion pero NO son
parte del vector IR. Viven como metadata runtime:

| Modo | Semantica | Trust requerido |
|------|-----------|-------------------|
| `auto-suggest` | Cada accion del agente requiere approval explicito del usuario | untrusted o trusted |
| `auto-edit` | Edits auto-aplicados; comandos bash requieren approval | trusted |
| `auto-all` | Totalmente autonomo, sin approval gates | trusted, proyectos aislados |
| `danger-full-access` | Sin sandbox, acceso completo al sistema | solo `trust_level: trusted` en proyecto |

La correspondencia con el eje H (human control) de Shneiderman (cuando
aplique):

- `auto-suggest` ↔ H-3 (HITL — aprobacion en cada paso).
- `auto-edit` ↔ H-2 (HOTL — supervision continua de bash).
- `auto-all` ↔ H-1 (override-on-demand).
- `danger-full-access` ↔ H-0 (sin control runtime).

## 5. Metadata de encaje runtime

```yaml
extensions:
  codex:
    # Modelo
    model: gpt-5.4 | gpt-4 | ...
    model_reasoning_effort: high | medium | low
    # Aprobacion
    approvals_reviewer: user | none
    approval_mode: auto-suggest | auto-edit | auto-all | danger-full-access
    sandbox_mode: auto-suggest | auto-edit | auto-all | danger-full-access
    # Trust
    trust_level: trusted | untrusted
    # Session management
    resume_capable: true | false
    resume_id: "<session-uuid>" # opcional, si es session-resumable
    # Skill metadata (si es skill)
    ui_metadata:
      display_name: "..."
      short_description: "..."
      default_prompt: "..."
      icon: "..."
      brand_color: "..."
    # Plugins
    plugins:
      - "github@openai-curated"
    # Personality preset
    personality: pragmatic | rigorous | ...
```

## 6. Degrees of freedom como invariante cross-runtime

Codex formalizo el patron *degrees of freedom* en su skill-creator oficial.
Esta dimension es **ortogonal** al vector IR — captura latitud de
interpretacion del runtime:

| DF level | Codex usage | Declarada en |
|----------|-------------|---------------|
| **High freedom** | text-based instructions; multiple approaches validos | `extensions.kora.skill_freedom: high` |
| **Medium freedom** | pseudocode o scripts parametrizados | `skill_freedom: medium` |
| **Low freedom** | specific scripts, few params, frague + critica consistency | `skill_freedom: low` |

Codex utiliza este campo para decidir cuanto interpretar libremente vs
seguir literalmente.

## 7. Progressive disclosure (invariante obligatorio)

Segun `skill-creator` oficial de Codex, los skills DEBEN seguir progressive
disclosure:

1. **Metadata** (name + description): ~100 words, siempre en contexto.
2. **SKILL.md body**: <5k words, cargado al trigger.
3. **Bundled resources** (`scripts/`, `references/`, `assets/`): bajo
   demanda, unlimited.

Habilidades KORA proyectadas a Codex **DEBEN** respetar este patron. Los
checks `progressive-disclosure` y `fidelidad-agentskills` (definidos en
`autoria-spec §5.1, §5.5, §14`) verifican que body ≤ 500 lineas y que la
transmutacion a paquete agentskills.io-compatible es sintacticamente valida.

## 8. Protocolo ACP

Codex es ACP backend (`acp.allowedAgents[]`). Un artefacto KORA ACP-compliant
puede invocarse via ACP desde OpenClaw gateway:

```yaml
extensions:
  kora:
    acp_compliant: true
    acp_backend: codex
```

## 9. Dominio de invocacion

| Modo | Trigger | Vector tipico |
|------|---------|----------------|
| Skill auto-activado | description match + slash command `/activate_skill` equivalent | Π≤2, Μ=0 |
| Agent mode | `codex exec "prompt"` o interactive session | Π=2, Μ=1, Ξ=2 |
| Session resumible | `codex resume <id>` | Π=2, Μ=1-2 (parcial), Ξ=2 |

## 10. Reglas de transmutacion

Obligatorias:

1. `_transmutation.yml` emitido conforme `transmutation-spec §6`.
2. Output vive en `{workspace}/_BUILD/codex/` (gitignored).
3. Si IR excede dominio (Μ=2 con requirement de `memory: user` transparente
   cross-session), transmutar a Codex **debe declarar perdida** de
   persistencia transparente.
4. Skills con `scripts/references/assets` se transmutan sin cambios
   estructurales (agentskills.io cross-runtime).
5. Si el vector declara `skill_freedom`, se propaga a metadata Codex.

## 11. Ingesta inversa (`Lift_{codex}`)

Codex skills pueden elevarse:

```bash
kora ingest --from codex --file ~/.codex/skills/my-skill/SKILL.md
```

Mapeo:

| Campo Codex | Destino KORA IR |
|--------------|------------------|
| `name` | `_manifest.urn` slug |
| `description` | `artefacto.perfil.descripcion` + `_manifest.provenance.source` |
| `metadata.short-description` | atlas descriptivo |
| body content | `artefacto.plan` (heuristico) |
| `scripts/`, `references/`, `assets/` | preservados tal cual (cross-runtime) |
| `agents/openai.yaml` | `extensions.codex.ui_metadata` |

Default `vector_ontologico` para skills ingestados: `(Π=2, Μ=0, Ξ=1, Λ=0,
Φ=1, Σ=[1,1,2,1,0])`. El autor debe ajustar si el skill tiene
caracteristicas distintas.

### 11.1 Trace fidelity

```yaml
trace_fidelity:
  level: pendiente
  capture_mechanism: "por documentar en codex-runtime-extension"
  notes: "no cerrar verificacion estricta de trazabilidad hasta completar mecanismo estable"
```

## 12. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| Vector dentro del dominio | Vector IR ∈ `D_{codex}` | lint |
| `_transmutation.yml` presente | Output target incluye artifact | lint |
| Metadata runtime completa | `extensions.codex.*` coherente con approval modes | lint |
| Progressive disclosure | body ≤ 500 lineas, description en rango | lint |
| Skill freedom declarado | `skill_freedom` presente si Codex target | lint |
| UI metadata consistente | `agents/openai.yaml` coincide con SKILL.md si presente | lint |

## 13. Contrato vigente v1.0.0

- Codex soporta {Utilidad, Disciplina, Delegado} completos.
- Soporta {Persona} parcial (session-resumable, no cross-session transparente).
- NO soporta {Orquestador, Servicio, Arquetipo} nativamente.
- Dominio completo: Π ≤ 3, Μ ≤ 1 (con Μ=2 parcial via resume), Ξ ≤ 2, Λ ≤ 1, Φ ≤ 2.
- Approval modes + sandbox + trust level son runtime-ortogonales.
- Progressive disclosure y degrees of freedom son invariantes obligatorios.
- Ingesta inversa disponible para skills; parcial para sessions.

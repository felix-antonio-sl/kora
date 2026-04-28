---
_manifest:
  urn: "urn:kora:kb:opencode-runtime-extension"
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "harness-spec v1.1; transmutation-spec v1.2; OpenCode oficial docs https://opencode.ai/docs/skills/ y https://opencode.ai/docs/agents/ snapshot 2026-04-28"
version: "1.0.0"
status: publicado
tags: [spec, runtime, opencode, extension, transmutacion, proyeccion]
lang: es
extensions:
  kora:
    family: spec
    precedence_tier: 4
    platform: "opencode"
    baseline_docs_release: "2026-04-28"
relations:
  depends:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:autoria-spec"
---

# KORA/OpenCode-Runtime-Extension v1.0.0

## 1. Definicion

Esta extension especializa `runtime-spec-md` para el target **OpenCode**
(`opencode` CLI multi-provider). Define dominio de soporte, matriz de
fidelidad, permission system runtime y metadata de encaje runtime-especifica.

### 1.1 Alcance

Gobierna:

1. Proyeccion `T_{opencode}: KORA_IR → OpenCode` segun
   `transmutation-spec`.
2. Skills estilo `.opencode/skills/{name}/SKILL.md` (compatibles
   agentskills.io: solo `name + description` minimos en frontmatter).
3. Agents en `.opencode/agents/*.md` o `~/.config/opencode/agents/*.md`
   con frontmatter Markdown, o JSON en `opencode.json`.
4. Permission system granular por key (read, edit, bash, skill, etc.)
   con `allow | deny | ask` y patrones glob.

### 1.2 Lo que NO gobierna

- Modelo subyacente (multi-provider: Anthropic, OpenAI, Z.AI, Ollama,
  MiniMax, etc.). Cada agente declara `model: provider/model-id`
  independientemente.
- Despliegue del binario `opencode` ni instalacion.
- Plugins, hooks o integraciones MCP que viven fuera del shape KORA.

## 2. Formas materiales soportadas

| Forma material | Ubicacion runtime | Frontmatter / shape |
|----------------|----------------------|----------------------|
| Skill estandar | `.opencode/skills/{name}/SKILL.md` o `~/.config/opencode/skills/{name}/SKILL.md` o (compat) `.claude/skills/`, `.agents/skills/` | `name` (slug) + `description` (1-1024 chars), opcionales `license`, `compatibility`, `metadata` |
| Subagente | `.opencode/agents/{name}.md` con `mode: subagent` | `description` + `mode: subagent`, opcional `model`, `permission`, `prompt`, `steps`, `color`, `hidden`, `disable` |
| Agente primary | `.opencode/agents/{name}.md` con `mode: primary` o `all` | `description` + `mode: primary` o `all`, opcional `model`, `permission`, `prompt`, `steps`, `color` |
| Agente JSON | `opencode.json` bajo `agent.{name}` | mismos campos en JSON |

OpenCode **NO soporta nativamente**:

- Servicios always-on (no es daemon; cada sesion CLI o TUI es de vida
  acotada).
- Personas persistentes cross-session transparentes (las sesiones tienen
  jerarquia parent/child con navegacion, pero no `memory: user`
  automatico).
- Operad dinamica completa (Ξ=4): subagentes accesibles via Task tool
  con permission gates, pero topologia dinamica completa queda en la
  app.
- Society-in-the-loop (Λ=3).

OpenCode **soporta como rasgos distintivos**:

- **Discovery multi-location** de skills: explora hacia arriba desde
  cwd hasta git worktree root, cargando `.opencode/skills/`,
  `.claude/skills/`, `.agents/skills/` simultaneamente.
- **Permission system granular** por key: `read, edit, glob, grep,
  list, bash, task, external_directory, todowrite, webfetch, websearch,
  codesearch, lsp, skill, question, doom_loop`.
- **Modo `all`**: agente que puede operar como primary y como subagent
  segun contexto.
- **Hidden agents**: subagentes invisibles en autocompletado pero
  invocables programaticamente.
- **Sessions jerarquicas**: navegacion `parent/child` para flujos
  multi-agente.

## 3. Matriz de preservacion por eje

### 3.1 Eje Π (plan)

```yaml
pi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: partial, loss: "OpenCode soporta agentes con steps acotados via campo `steps`; fixed-points profundos pueden exceder ese budget si no se ajusta" }
```

### 3.2 Eje Μ (materia)

```yaml
mu:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "scratchpad intra-invocacion via session activa" }
  "2": { projected: 2, fidelity: partial, loss: "OpenCode preserva contexto entre subagent y agent padre via session_child_*, pero no hay memory: user transparente cross-session como Claude Code" }
  "3": { projected: null, fidelity: none, loss: "OpenCode es CLI/TUI sincrono; no es daemon always-on" }
```

### 3.3 Eje Ξ (interaccion)

```yaml
xi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full }
  "2": { projected: 2, fidelity: full }
  "3": { projected: 3, fidelity: partial, loss: "protocolos multi-fase via subagent @mention + Task tool, pero coreografias largas dependen del wrapper aplicativo" }
  "4": { projected: 3, fidelity: partial, loss: "operad dinamica no soportada; topologia dinamica via Task tool queda con perdida estructural en handoff cross-subagent" }
```

### 3.4 Eje Λ (nivel sociotecnico)

```yaml
lambda:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "organizacional via per-project `.opencode/` + global `~/.config/opencode/`" }
  "2": { projected: 1, fidelity: partial, loss: "ecosistema colapsa a organizacional; OpenCode no tiene primitiva de cross-organization sharing" }
  "3": { projected: null, fidelity: none, loss: "society-in-the-loop no soportado" }
```

### 3.5 Eje Φ (acoplamiento humano-AI)

```yaml
phi:
  "0": { projected: 0, fidelity: full }
  "1": { projected: 1, fidelity: full, comment: "tool metaphor — default" }
  "2": { projected: 2, fidelity: full, comment: "permission system con `ask` materializa human-in-the-loop colaborativo de forma fina" }
  "3": { projected: 2, fidelity: partial, loss: "hybrid cognition completa requiere wrapper aplicativo; el permission system aproxima HOTL pero no cogniton compartida" }
  "4": { projected: null, fidelity: none, loss: "co-evolutivo no soportado nativamente" }
```

### 3.6 Eje Σ (vector etico)

```yaml
sigma:
  safety_norm:
    max_supported: 3
    enforcement: "permission system con allow/deny/ask granular por key (bash, edit, external_directory, etc.) + glob patterns"
  fairness:
    max_supported: 2
    enforcement: "declarativo via prompt + permission por agente"
  transparency:
    max_supported: 2
    enforcement: "logs de session + child session navigation; explicabilidad limitada al output de la session"
  accountability:
    max_supported: 2
    enforcement: "session id por agente + jerarquia parent/child; no audit trail cross-session transparente"
  sustainability:
    max_supported: 1
    enforcement: "declarativo"
```

## 4. Permission system como dimension runtime ortogonal

OpenCode introduce **permission system** que afecta la ejecucion pero
NO es parte del vector IR. Es metadata runtime. Vive en `opencode.json`
global o en frontmatter del agente.

### 4.1 Keys canonicas

| Key | Domain | Semantica |
|-----|--------|-----------|
| `read`, `edit`, `glob`, `grep`, `list` | filesystem read/write | acceso a codigo |
| `bash` | shell | ejecucion |
| `task` | subagentes | invocacion via Task tool |
| `external_directory` | filesystem cross-workspace | salir del workspace |
| `todowrite` | task tracking | escribir en TODO list |
| `webfetch`, `websearch`, `codesearch` | web | acceso externo |
| `lsp` | language server | navegacion semantica |
| `skill` | skills | invocacion de skills (con glob patterns por skill) |
| `question`, `doom_loop` | meta | preguntar al usuario; loops |

### 4.2 Valores

- `allow`: ejecucion automatica.
- `deny`: bloqueado, oculto al agente.
- `ask`: requiere aprobacion del usuario por turno.
- Objeto con patrones glob para granularidad fina:

```json
{
  "permission": {
    "bash": { "*": "ask", "git status": "allow", "rm *": "deny" },
    "skill": { "*": "allow", "internal-*": "deny" }
  }
}
```

### 4.3 Correspondencia con Φ (Shneiderman H)

| Permission profile | H aproximado |
|-------------------|---------------|
| Todo `ask` | H-3 (HITL — aprobacion en cada paso) |
| `bash: ask` + `edit: allow` | H-2 (HOTL — supervision continua de bash) |
| Todo `allow` | H-1 (override-on-demand) |
| Defecto sin permission overrides | depende del agente built-in (`build` → liberal; `plan` → restrictivo) |

## 5. Metadata de encaje runtime

```yaml
extensions:
  opencode:
    # Modo
    mode: primary | subagent | all
    # Modelo
    model: "anthropic/claude-opus-4-7" | "openai/gpt-5.5" | ...
    temperature: 0.0..1.0
    top_p: 0.0..1.0
    # Iteraciones
    steps: 20            # max agentic iterations
    # UI
    color: "#FF8800"     # hex o theme value
    # Visibility
    hidden: false        # subagentes ocultos en autocompletado
    disable: false       # desactivar agente sin borrarlo
    # Permission system
    permission:
      read: allow
      edit: ask
      bash:
        "*": ask
        "git status": allow
      skill:
        "*": allow
        "internal-*": deny
      task: allow
      webfetch: deny
    # Prompt
    prompt: "{file:./prompts/this-agent.md}"  # o string inline
```

## 6. Skill discovery y locations

OpenCode busca skills hacia arriba desde cwd hasta git worktree root,
en este orden:

1. Project: `.opencode/skills/{name}/SKILL.md`
2. Global: `~/.config/opencode/skills/{name}/SKILL.md`
3. Compat Claude: `.claude/skills/{name}/SKILL.md`
4. Compat agents: `.agents/skills/{name}/SKILL.md`

Esto significa que un skill KORA transmutado a agentskills.io
**funciona directamente** en OpenCode sin transmutacion adicional, si
se ubica en `.claude/skills/` o `.agents/skills/` del workspace.

Reglas de naming:

- `name`: 1-64 chars, lowercase alfanumerico con hyphens unicos
  separadores (regex `^[a-z0-9]+(-[a-z0-9]+)*$`).
- `name` debe coincidir con el nombre del directorio.
- `description`: 1-1024 chars, suficientemente especifica para que el
  agente decida cuando activar.
- Filename **DEBE** ser `SKILL.md` (mayusculas).

## 7. Modos de invocacion

| Modo | Trigger | Vector tipico |
|------|---------|----------------|
| Skill auto-activado | description match + `skill` tool | Π≤2, Μ=0 |
| Primary agent (Tab) | sesion CLI/TUI con tab cycling | Π=2, Μ=2, Ξ=2 |
| Subagent (`@mention`) | invocacion explicita por usuario o por primary agent via Task tool | Π=2, Μ=1-2, Ξ=2 |
| Hidden agent | invocado programaticamente, no aparece en autocompletado | Π=1-2, Μ=0-1 |
| CLI: `opencode agent create` | scaffolding interactivo | n/a (admin) |

## 8. Built-in agents (no transmutables)

Estos agentes son **runtime nativos**, NO se proyectan desde KORA IR:

| Agent | Mode | Tools |
|-------|------|-------|
| `build` | primary | full |
| `plan` | primary | restringido (edit/bash require ask) |
| `general` | subagent | multi-step research, full access |
| `explore` | subagent | read-only |
| `compaction` | hidden | system summarization |
| `title` | hidden | session naming |
| `summary` | hidden | session summarization |

KORA **NO genera** estos agentes. Si un artefacto KORA cumple la misma
funcion, se transmuta como agente custom adicional, no reemplazando los
built-in.

## 9. Reglas de transmutacion

Obligatorias:

1. `_transmutation.yml` emitido conforme `transmutation-spec §6`.
2. Output vive en `{workspace}/_BUILD/opencode/` (gitignored).
3. Si el IR declara `forma_material: habilidad`, la transmutacion
   produce paquete agentskills.io-compatible (`SKILL.md` + `scripts/`,
   `referencias/→references/`, `recursos/→assets/`) ubicable
   directamente en `.opencode/skills/`.
4. Si el IR declara `forma_material: subagente`, la transmutacion
   produce `.opencode/agents/{name}.md` con `mode: subagent`. Hidden
   `true` por defecto si el subagente no expone API humana.
5. Si el IR declara `forma_material: agente-propiamente-tal`, la
   transmutacion produce `.opencode/agents/{name}.md` con
   `mode: primary` o `mode: all` segun el caso.
6. Si el IR declara `forma_material: agente-plataforma`, la
   transmutacion **no esta soportada**: declarar perdida estructural
   total y pedir runtime con Μ=3 (openclaw).
7. El permission system se deriva del vector y de
   `extensions.opencode.permission` declarado. Defaults seguros:
   `bash: ask`, `external_directory: deny`, `webfetch: deny` salvo
   override explicito.
8. `model` declarado en `extensions.opencode.model` se propaga; si
   ausente, se hereda del primary agent invocador (subagentes) o del
   global config (primary).

## 10. Ingesta inversa (`Lift_{opencode}`)

OpenCode skills y agents pueden elevarse:

```bash
kora ingest --from opencode --file .opencode/skills/my-skill/SKILL.md
kora ingest --from opencode --file .opencode/agents/reviewer.md
```

### 10.1 Mapeo skill

| Campo OpenCode | Destino KORA IR |
|----------------|------------------|
| `name` | `_manifest.urn` slug + `nombre` |
| `description` | `descripcion` + `_manifest.provenance.source` |
| `metadata.*` | `extensions.opencode.metadata.*` |
| `compatibility` | `extensions.opencode.compatibility` |
| body content | `artefacto.plan` (heuristico) + body |
| `scripts/`, `references/`, `assets/` | preservados tal cual (cross-runtime con agentskills.io) |

Default `vector_ontologico` para skills ingestados: `(Π=2, Μ=0, Ξ=1, Λ=0,
Φ=1, Σ=[1,1,2,1,0])`. El autor ajusta segun caracteristicas reales.

### 10.2 Mapeo agente

| Campo OpenCode | Destino KORA IR |
|----------------|------------------|
| `description` | `descripcion` |
| `mode` | discriminante de `atlas.forma_material` (subagent → subagente; primary/all → agente-propiamente-tal) |
| `model`, `temperature`, `top_p`, `steps`, `color`, `hidden`, `disable` | `extensions.opencode.{model, temperature, ...}` |
| `permission` | `extensions.opencode.permission` (preservado tal cual) |
| `prompt` | body Markdown (si es file ref) o `extensions.opencode.prompt` |

Default `vector_ontologico`:

- `mode: subagent` → `(Π=2, Μ=1, Ξ=2, Λ=0, Φ=1, Σ=[2,1,2,2,1])`.
- `mode: primary | all` → `(Π=2, Μ=2, Ξ=2, Λ=0, Φ=2, Σ=[2,1,2,2,1])`.

### 10.3 Trace fidelity

```yaml
trace_fidelity:
  level: pendiente
  capture_mechanism: "por documentar en opencode-runtime-extension"
  notes: "OpenCode mantiene session id y child sessions; mecanismo estable de exportacion para audit pendiente"
```

## 11. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| Vector dentro del dominio | Vector IR ∈ `D_{opencode}` | lint |
| `_transmutation.yml` presente | Output target incluye artifact | lint |
| Naming valido | `name` cumple regex y coincide con directorio | lint |
| `description` en rango | 1-1024 chars | lint |
| Mode valido | `mode ∈ {primary, subagent, all}` para agentes | lint |
| Permission shape valido | keys del enum cerrado, valores `allow|deny|ask` o glob object | lint |
| Steps razonable | si declarado, `steps > 0` | lint |
| Defaults seguros | `bash: ask`, `external_directory: deny` salvo override | manual |
| Skill compat agentskills | habilidad transmute a `.opencode/skills/` byte-identical | runtime |

## 12. Dominio de invocacion

| Modo | Trigger | Vector tipico |
|------|---------|----------------|
| Skill auto-activado | description match + `skill` tool nativo | Π≤2, Μ=0, Ξ=1-2 |
| Primary `build` (default) | sesion TUI/CLI con tab cycling | Π=2, Μ=2, Ξ=2 |
| Primary custom | tab cycle hacia agente custom mode primary | Π=2, Μ=2, Ξ=2 |
| Subagent via `@mention` | usuario invoca explicitamente | Π=2, Μ=1, Ξ=2 |
| Subagent via Task tool | primary delega a subagente segun description | Π=2, Μ=1, Ξ=2-3 |
| Hidden agent | invocacion programatica, no aparece en autocompletado | Π=1-2, Μ=0-1 |

## 13. Contrato vigente v1.0.0

- OpenCode soporta {Utilidad, Disciplina, Delegado, Persona} con vector
  Π ≤ 3, Μ ≤ 2 (Μ=2 partial), Ξ ≤ 3, Λ ≤ 1, Φ ≤ 2 (Φ=3 partial).
- {Orquestador} parcial: subagentes accesibles via Task tool con
  permission gates, pero operad dinamica completa requiere wrapper
  aplicativo.
- {Servicio} y {Arquetipo} no soportados nativamente.
- Permission system es runtime-ortogonal y mas granular que
  Codex/Claude Code.
- Skills compatibles agentskills.io: una habilidad KORA transmuta sin
  cambios a `.opencode/skills/` o `.claude/skills/` (multi-runtime
  byte-identical).
- Built-in agents (`build`, `plan`, `general`, `explore`, system
  hidden) no se transmutan desde KORA IR.
- Ingesta inversa disponible para skills y agents custom.
- `mode: all` es OpenCode-especifico; en KORA IR proyecta
  ambivalente (`subagente` o `agente-propiamente-tal` segun uso real).

## 14. Relacion con otras specs

- `harness-spec`: vector ontologico fuente.
- `autoria-spec`: shape unificado del IR; este runtime soporta sus
  cuatro formas materiales excepto `agente-plataforma`.
- `transmutation-spec`: leyes functoriales de proyeccion.
- `runtime-spec-md`: contrato generico extendido aqui.
- `agentskills-runtime-extension`: skills KORA → OpenCode pasa
  transitivamente por agentskills.io en `.opencode/skills/` o
  `.claude/skills/` (compat declarada por OpenCode).
- `claude-code-runtime-extension`: comparte locations
  (`.claude/skills/`, `.claude/agents/` parcialmente). Skills son
  cross-runtime; agents requieren proyeccion separada por shape.

---
_manifest:
  urn: "urn:kora:kb:transmutation-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "KORA runtime-spec-md v3.6.0; polymath analysis; categorical-foundations 02, 14"
version: "1.0.0"
status: published
tags: [spec, transmutacion, funtor, runtime, plataforma]
lang: es
extensions: {}
---

# KORA/Transmutation-Spec v1.0.0

## 1. Definicion

La transmutacion es el funtor T: AGENT.md -> Artifact_target que mapea las 6 dimensiones del AGENT.md (Intermediate Representation) a artefactos nativos de una plataforma concreta, preservando composicion e identidad.

El AGENT.md es la representacion intermedia (IR) canonica de un agente KORA. Consolida las 6 dimensiones semanticas del workspace en un unico artefacto estructurado. La transmutacion materializa esa IR en el formato nativo de cada target.

### 1.1 Propiedades del funtor

Sea T el funtor de transmutacion. T **DEBE** satisfacer:

- **Composicion:** T(g . f) = T(g) . T(f) — transmutaciones consecutivas componen.
- **Identidad:** T(id_A) = id_{T(A)} — la transmutacion identidad produce el artefacto sin cambio.

Traces to: formal/02 §2 (Adjunction Free ⊣ Forget) ; formal/07 §2 (Preservation by Interface)

### 1.2 Fidelidad

El funtor T se evalua segun tres propiedades de fidelidad:

- **Faithful:** distinciones en la IR sobreviven en el target. Si dos agentes difieren en una dimension, sus transmutaciones difieren en la materializacion correspondiente.
- **Full:** toda interaccion observable en el target corresponde a una dimension de la IR. No hay comportamiento en el target que no tenga origen en la IR.
- **Essentially surjective:** todo agente-target razonable es transmutacion de algun IR. La plataforma no impone agentes que no puedan expresarse en KORA.

### 1.3 Alcance

Esta especificacion gobierna:

1. Transmutacion de agentes completos (AGENT.md a target)
2. Targets soportados y su clasificacion
3. Mapeo por dimension para cada target
4. Evaluacion de fidelidad por target
5. Output format y estructura de BUILD/
6. Registro de transmutacion (_transmutation.yml)
7. Invocacion via toolchain

Esta especificacion **NO** gobierna transmutacion de Skills. Los Skills son universales por isomorfismo fluido (formal/02 §4.1): un Skill degenerado CM-*.md es identico en todo target, y un Skill extendido se monta via lazy-load independiente del target. El funtor Forget preserva el CM Core sin perdida.

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Transmutacion | Funtor T que materializa un AGENT.md en artefactos nativos de una plataforma target |
| AGENT.md (IR) | Intermediate Representation: artefacto unico que estructura las 6 dimensiones semanticas de un agente KORA |
| Dimension | Eje semantico del IR: coalgebra, plan, interface, fibers, composition, safety |
| Target | Plataforma concreta donde el agente se materializa (claude-code, openclaw, codex, gemini) |
| Adapter | Skill KORA (SKILL.md en SKILLS/) que un modelo ejecuta para producir la transmutacion a un target |
| Fidelidad | Grado en que la transmutacion preserva la semantica de cada dimension del IR |
| BUILD/ | Directorio de salida donde se depositan los artefactos transmutados |
| _transmutation.yml | Manifiesto emitido por cada transmutacion que registra fuente, target, fidelidad y perdidas |

## 3. Las 6 dimensiones del IR

El AGENT.md estructura al agente en 6 dimensiones semanticas. Cada dimension mapea a uno o mas componentes del workspace KORA:

| Dim | Nombre | Contenido | Origen workspace |
| --- | --- | --- | --- |
| 1 | Coalgebra | FSM: estados, transiciones, acciones, prioridades, Skills invocados | AGENTS.md §1 (FSM) |
| 2 | Plan | Reglas duras, co-induccion terminal, contexto multi-turno, comportamiento operativo | AGENTS.md §2-§4 (§6 si existe) |
| 3 | Interface | Tools semanticas: firma, cuando usar, cuando NO, routing maps, KBs | TOOLS.md completo |
| 4 | Fibers | 5 fibras ortogonales del estado: identity (SOUL.md), operator (USER.md), memory (MEMORY.md), runtime (config.json parcial), knowledge (allowed_kb + routing) | SOUL.md, USER.md, MEMORY.md, config.json |
| 5 | Composition | Wiring inter-agente: tipo, sub-agentes, dependencias, rejection routing | AGENTS.md §5 (Wiring) + config.json sub_agents |
| 6 | Safety | Sandbox mode, tools allow/deny, runtime capabilities, limits, policy flags, model routing | config.json completo |

Traces to: formal/01 §2.1 (Fiber Structure) ; formal/01 §1.1 (F-coalgebra Definition) ; formal/01 §1.3 (Effect Monad M)

### 3.1 Invariante de completitud

Todo AGENT.md **DEBE** cubrir las 6 dimensiones. Una dimension puede estar vacia (e.g., composition vacia si el agente no tiene wiring), pero **DEBE** estar declarada explicitamente.

### 3.2 Invariante de segregacion

Cada dimension **DEBE** contener exclusivamente su materia. La contaminacion inter-dimensional en la IR es invalida. Enforcement: lint pre-transmutacion.

## 4. Targets soportados

| Target | Clase | Output | Adapter skill |
| --- | --- | --- | --- |
| claude-code | ephemeral | .md con YAML frontmatter | CM-TRANSMUTE-CLAUDE-CODE |
| openclaw | service | workspace + config | CM-TRANSMUTE-OPENCLAW |
| codex | ephemeral | instructions + config | CM-TRANSMUTE-CODEX |
| gemini | ephemeral | .md + settings | CM-TRANSMUTE-GEMINI |

### 4.1 Clase ephemeral vs service

- **Ephemeral:** el agente se instancia como contexto de una sesion. No persiste estado entre sesiones por mecanismo propio del target. Lifecycle = sesion.
- **Service:** el agente corre como servicio persistente. Mantiene estado, memory, heartbeat, canales. Lifecycle = deployment.

### 4.2 Extensibilidad

Nuevos targets se agregan declarando: clase, output format, adapter skill, y mapeo dimension x target. Cada nuevo target **DEBE** documentar fidelidad y perdidas antes de ser registrado.

## 5. Adapters como Skills

Los adapters son Skills KORA (SKILL.md en SKILLS/) que un modelo ejecuta. **NO** son scripts Python ni transformaciones programaticas.

### 5.1 Responsabilidad del adapter

El adapter recibe el AGENT.md parseado (las 6 dimensiones como estructura) y produce los artefactos nativos del target. El adapter aplica las reglas de mapeo de §6, respeta las perdidas documentadas de §7, y emite el registro de §9.

### 5.2 Responsabilidad del toolchain

El toolchain Python (scripts/kora transmute) orquesta:

1. Parsea el AGENT.md y extrae las 6 dimensiones
2. Valida pre-transmutacion (§11)
3. Invoca al modelo con el adapter skill y la IR parseada
4. Valida post-transmutacion contra schema del target
5. Emite _transmutation.yml
6. Deposita artefactos en BUILD/

### 5.3 Segregacion adapter/toolchain

El toolchain **NO DEBE** tomar decisiones semanticas de mapeo — esas viven en el adapter. El adapter **NO DEBE** ejecutar I/O de filesystem — eso lo hace el toolchain. La frontera es: el adapter decide **que** producir; el toolchain decide **donde** depositarlo.

## 6. Mapeo dimension x target

Tabla exhaustiva de como cada dimension del IR se materializa en cada target.

### 6.1 Dim 1 — Coalgebra (FSM)

| Campo IR | claude-code | openclaw | codex | gemini |
| --- | --- | --- | --- | --- |
| Estados S-* | Secciones markdown con heading por estado | AGENTS.md stripped (FSM preservada) | Seccion "## Workflow" en instructions.md con estados como pasos | Seccion "## Workflow" en GEMINI.md con estados como pasos |
| Transiciones | Prosa estructurada: "Si X, entonces ir a [seccion Y]" | Preservadas verbatim en sintaxis canonica | Lista condicional: "If X, proceed to step Y" | Lista condicional: "If X, proceed to step Y" |
| Prioridades | Orden de secciones + condicionales explicitos | Preservadas verbatim con [prioridad N] | Orden de condicionales (se pierde sintaxis de prioridad) | Orden de condicionales (se pierde sintaxis de prioridad) |
| Skills invocados (CM-*) | Inline como instruccion: "Ejecuta el procedimiento de [Skill]" | Referencia directa en skills/ (lazy-load nativo) | Inline como instruccion en prosa | Inline como instruccion en prosa |
| S-DISPATCHER | Primera seccion del .md: clasificacion de input | Preservado como estado FSM | Primer bloque de instructions.md | Primer bloque de GEMINI.md |
| S-END | Seccion final: "## Output" con formato de cierre | Preservado como estado terminal | Seccion final "## Output format" | Seccion final "## Output format" |

**Ejemplo — curator transmutado a claude-code:**

```markdown
# Curator

## Clasificacion
Ante cada solicitud, clasifica el tipo de trabajo:
- Si es nuevo artefacto en modo guiado -> ir a Ciclo Guiado
- Si es koraficiar documento fuente -> ir a Koraficacion
- Si es cristalizar decisiones -> ir a Cristalizacion
[... cada estado como seccion ...]

## Koraficacion
Transforma el documento fuente a formato KORA/MD.
1. Analizar fuente [...]
2. Si artefacto generado -> ir a Auditoria
3. Si necesita iteracion -> volver a Koraficacion

## Auditoria
Verificar conformidad del artefacto contra specs.
[...]
```

### 6.2 Dim 2 — Plan (reglas, co-induccion, contexto)

| Campo IR | claude-code | openclaw | codex | gemini |
| --- | --- | --- | --- | --- |
| Reglas duras (scope, allowed, forbidden) | Seccion "## Reglas" con MUST/MUST NOT explicitos | AGENTS.md stripped §2 preservado verbatim | Seccion "## Constraints" en instructions.md | Seccion "## Constraints" en GEMINI.md |
| Rejection message | Inline en reglas: "Si fuera de scope, responde: [mensaje]" | Preservado verbatim | Inline en constraints | Inline en constraints |
| Co-induccion checklist | Seccion "## Verificacion pre-output" con checks como lista | Preservada verbatim en §3 | Seccion "## Before responding, verify:" | Seccion "## Before responding, verify:" |
| Protocolo de correccion | Subseccion con acciones: "Si X falla, [accion]" | Preservado verbatim | Degradado a nota: "If a check fails, re-examine" | Degradado a nota: "If a check fails, re-examine" |
| Contexto multi-turno | Seccion "## Contexto de sesion" con reglas de retencion | Preservado verbatim en §4 | Omitido (Codex no tiene multi-turno nativo) | Degradado a nota generica de coherencia |
| Fidelidad/metricas (FS, CR) | Inline en reglas: "Todo artefacto DEBE cumplir FS=100%" | Preservado en reglas duras | Inline como constraint | Inline como constraint |

**Ejemplo — curator, seccion Plan en claude-code:**

```markdown
## Reglas
- SOLO operar sobre artefactos de conocimiento KORA/MD y KORA/Spec-MD
- NUNCA modificar specs fundacionales — redirigir al operador
- NUNCA construir agentes — redirigir a kora/forgemaster
- NUNCA modificar catalogo — redirigir a kora/custodio
- Si fuera de scope: "Eso esta fuera de mi curaduria. Para specs->operador. Para agentes->forgemaster."
- Fidelidad: todo artefacto generado DEBE cumplir FS=100%. CR>1.5 objetivo.
- Pipeline: todo artefacto transita inbox -> source -> drafts -> knowledge

## Verificacion pre-output
Antes de emitir cualquier resultado, verificar:
1. SCOPE_COMPLIANCE — la salida esta dentro del dominio de curaduria
2. STATE_AWARENESS — coherente con la fase actual del trabajo
3. INTERFACE_DISCIPLINE — solo usa tools y KBs declaradas
[...]
Si alguno falla, corregir antes de emitir.
```

### 6.3 Dim 3 — Interface (tools)

| Campo IR | claude-code | openclaw | codex | gemini |
| --- | --- | --- | --- | --- |
| Tools con firma | Omitido — Claude Code no acepta tool declarations custom en .md; se degradan a instrucciones de uso | TOOLS.md stripped preservado verbatim | Omitido — Codex usa tools internas; se degradan a instrucciones | Degradado a function declarations en settings.json si soportado |
| Cuando usar / Cuando NO | Prosa en seccion "## Herramientas disponibles" | Preservado verbatim en TOOLS.md | Prosa en seccion "## Available tools" | Prosa en GEMINI.md |
| Routing map (kb_route) | Inline como instruccion: "Para tema X, consultar [recurso Y]" | Preservado verbatim con URNs | Inline como instruccion | Inline como instruccion |
| allowed_kb | Lista en seccion de contexto: "Bases de conocimiento: [lista]" | Enforcement via config.json (excluido del bootstrap) | Lista informativa | Lista informativa |

**Ejemplo — curator, Interface en claude-code:**

```markdown
## Herramientas disponibles
- **catalog_resolve**: dado un URN, resolver a path fisico via catalogo
- **kb_route**: clasificar tema y resolver URN de KB prioritaria
  - Formato descriptivo -> urn:kora:kb:md-spec
  - Formato prescriptivo -> urn:kora:kb:spec-md
  - Gobernanza -> urn:kora:kb:gobernanza
- **artifact_read**: leer artefacto existente, separar frontmatter de cuerpo
- **artifact_write**: escribir artefacto (siempre con frontmatter + cuerpo completo)
- **artifact_validate**: validar artefacto contra md-spec o spec-md
- **spec_consult**: consultar specs fundacionales para conformidad
- **artifact_list**: listar artefactos por namespace, status o tipo
```

### 6.4 Dim 4 — Fibers (identity, operator, memory, runtime, knowledge)

| Fibra | Campo IR | claude-code | openclaw | codex | gemini |
| --- | --- | --- | --- | --- | --- |
| **Identity** | identidad dialectica | Seccion "## Identidad" al inicio del .md | SOUL.md stripped completo | Seccion "## Identity" en instructions.md | Seccion "## Identity" en GEMINI.md |
| **Identity** | paradigma cognitivo | Inline en identidad o en reglas | Preservado verbatim en SOUL.md | Inline en identity | Inline en identity |
| **Identity** | tono | Inline: "Tono: [descripcion]" | Preservado verbatim en SOUL.md | Inline en identity | Inline en identity |
| **Operator** | perfil usuario | Seccion "## Contexto del operador" | USER.md stripped completo | Omitido (Codex no tiene user context nativo) | Omitido |
| **Operator** | rutinas | Inline en contexto del operador | Preservado verbatim en USER.md | Omitido | Omitido |
| **Operator** | preferencias output | Inline en contexto del operador o en output format | Preservado verbatim en USER.md | Seccion "## Output format" | Seccion "## Output format" |
| **Memory** | MEMORY.md | No inyectado — Claude Code gestiona su propia memoria | Preservado en workspace (MEMORY.md + memory/) | No disponible | No disponible |
| **Memory** | episodic (memory/*.md) | No inyectado | Preservado en workspace | No disponible | No disponible |
| **Runtime** | model_routing | No aplicable — Claude Code tiene modelo fijo | Informado a openclaw.json (no al bootstrap) | No aplicable | No aplicable |
| **Runtime** | runtime_capabilities | Implicito en permisos de Claude Code | Enforcement server-side via config | No aplicable | No aplicable |
| **Knowledge** | allowed_kb | Lista informativa en el .md | Enforcement server-side via config.json | Lista informativa | Lista informativa |
| **Knowledge** | KBs referenciadas | Inline como contexto o instrucciones de consulta | Mount RO como volumenes (no en bootstrap) | Inline como contexto | Inline como contexto |

**Ejemplo — curator, Fibers.Identity en claude-code:**

```markdown
# Curator

kora/curator. Curador del corpus de conocimiento KORA. Domina ciclo de vida
completo de artefactos: disenar, koraficiar, cristalizar, auditar, editar,
reparar, mejorar y deprecar, preservando fidelidad, trazabilidad y consistencia.

Paradigma: Funtor K (koraficacion) y Funtor C (cristalizacion). Fidelidad
radical: no perder hechos. SSOT: un hecho en un lugar. Compresion semantica
maxima con hechos preservados.

Tono: Preciso, meticuloso, telegrafico. Directo e implacable con la grasa.
```

### 6.5 Dim 5 — Composition (wiring)

| Campo IR | claude-code | openclaw | codex | gemini |
| --- | --- | --- | --- | --- |
| Tipo (raiz/sub-agente) | Implicito — Claude Code no tiene jerarquia de agentes | Preservado en AGENTS.md stripped §5 | No disponible | No disponible |
| Sub-agentes directos | Si existen, declarados como sub-agents de Claude Code (.claude/agents/) | Preservado verbatim; resueltos como workspaces en gateway | No disponible — Codex no soporta composicion | No disponible |
| Dependencias inter-agente | Seccion "## Derivaciones" con instrucciones de redireccion | Preservadas verbatim; resueltas via hooks cross-gateway | Degradado a nota: "For [tema], suggest user contact [agente]" | Degradado a nota |
| Rejection routing | Inline en reglas: "Para X, redirigir a [agente]" | Preservado verbatim en reglas duras | Degradado a prosa de rechazo | Degradado a prosa de rechazo |
| max_depth / max_concurrent | No configurable en Claude Code .md | Enforcement server-side via config.json | No disponible | No disponible |

**Ejemplo — curator, Composition en claude-code:**

```markdown
## Derivaciones
- Specs fundacionales -> redirigir al operador directo
- Agentes (crear, modificar) -> redirigir a kora/forgemaster
- Catalogo (modificar directamente) -> redirigir a kora/custodio
```

### 6.6 Dim 6 — Safety (constraints, sandbox, limits)

| Campo IR | claude-code | openclaw | codex | gemini |
| --- | --- | --- | --- | --- |
| sandbox.mode | Implicito en permisos de Claude Code (no configurable via .md) | Enforcement server-side via config.json (excluido del bootstrap) | sandbox_mode en config.json de Codex | Implicito en settings |
| tools.allow | Implicito — Claude Code decide sus tools; la lista del .md es informativa | Enforcement server-side via config.json | tools en config.json de Codex | Implicito |
| tools.deny | No materializable en Claude Code .md | Enforcement server-side | No materializable | No materializable |
| runtime_capabilities | Implicito en permisos del entorno | Enforcement server-side | Implicito | Implicito |
| limits.quotas | No configurable | Enforcement server-side | No configurable | No configurable |
| limits.policy_flags | Degradado a prosa: "Antes de publicar, obtener aprobacion" | Enforcement server-side | Degradado a prosa | Degradado a prosa |
| model_routing | No aplicable | Informado a openclaw.json | No aplicable | No aplicable |

**Ejemplo — curator, Safety en claude-code:**

```markdown
## Restricciones operativas
- Antes de publicar un artefacto, ejecutar auditoria de conformidad
- Antes de deprecar un artefacto, obtener aprobacion explicita del operador
- Artefactos no deben exceder 50,000 tokens ni 20 segmentos
```

## 7. Fidelidad por target

| Target | Fidelidad global | Perdidas |
| --- | --- | --- |
| **OpenClaw** | Maxima | lifecycle (heartbeat, cron) y dissipation requieren config manual en openclaw.json; no son automatizables desde la IR |
| **Claude Code** | Alta | coalgebra.triggers/outputs implicitos en prosa (no hay FSM engine); limits no configurable via .md; safety enforcement implicito en el entorno (no declarativo); alignment implicito |
| **Codex** | Moderada | sin composition (no soporta sub-agentes ni wiring); sin memory (no hay persistencia entre sesiones); plan y safety degradan a prosa sin enforcement; contexto multi-turno perdido |
| **Gemini** | Moderada | similar a Codex; function declarations parcialmente soportadas; sin composition ni memory; plan y safety degradan a prosa |

### 7.1 Detalle de fidelidad por dimension

| Dimension | OpenClaw | Claude Code | Codex | Gemini |
| --- | --- | --- | --- | --- |
| 1. Coalgebra | **preserved** — FSM verbatim con engine nativo | **degraded** — FSM expresada como prosa con secciones; sin engine | **degraded** — workflow como pasos secuenciales | **degraded** — workflow como pasos secuenciales |
| 2. Plan | **preserved** — reglas, co-induccion y contexto verbatim | **preserved** — reglas y checks expresables con fidelidad | **degraded** — reglas a prosa; co-induccion parcial; sin multi-turno | **degraded** — reglas a prosa; co-induccion parcial; sin multi-turno |
| 3. Interface | **preserved** — TOOLS.md preservado; enforcement server-side | **degraded** — tools como instrucciones informativas; sin enforcement | **degraded** — tools como instrucciones; sin enforcement | **degraded** — function declarations parciales |
| 4. Fibers | **preserved** — 5 fibras materializadas en archivos separados | **degraded** — identity y operator inline; memory/runtime/knowledge implicitos | **lost** (operator, memory) / **degraded** (identity, knowledge) | **lost** (operator, memory) / **degraded** (identity, knowledge) |
| 5. Composition | **preserved** — wiring resoluble via hooks cross-gateway | **degraded** — sub-agents parciales; hooks no disponibles | **lost** — sin composicion | **lost** — sin composicion |
| 6. Safety | **preserved** — enforcement server-side completo | **degraded** — limits y sandbox implicitos; policy flags a prosa | **degraded** — sandbox parcial; sin policy flags | **degraded** — sandbox parcial; sin policy flags |

## 8. Output format

Cada transmutacion produce artefactos en `BUILD/{target}/{namespace}/{agent}/`:

| Target | Archivos producidos | Notas |
| --- | --- | --- |
| claude-code | `{name}.md` | Archivo unico con todas las dimensiones serializadas como markdown |
| openclaw | `workspace/AGENTS.md`, `workspace/SOUL.md`, `workspace/USER.md`, `workspace/TOOLS.md`, `workspace/skills/`, `config/openclaw.json5`, `DEPLOY.md` | Workspace completo stripped + config de plataforma + guia de deploy |
| codex | `instructions.md`, `config.json` | Instructions para Codex + config JSON nativa |
| gemini | `GEMINI.md`, `settings.json` | System instruction + settings JSON nativos |

### 8.1 Estructura de BUILD/

```text
BUILD/
  claude-code/
    kora/
      curator.md
      forgemaster.md
    fxsl/
      neriomath.md
  openclaw/
    kora/
      curator/
        workspace/
          AGENTS.md
          SOUL.md
          USER.md
          TOOLS.md
          skills/
            CM-INTENT-CLASSIFIER.md
            CM-ARTIFACT-DESIGNER/
              SKILL.md
              [...]
        config/
          openclaw.json5
        DEPLOY.md
  codex/
    kora/
      curator/
        instructions.md
        config.json
  gemini/
    kora/
      curator/
        GEMINI.md
        settings.json
  _transmutation.yml  (por cada agente transmutado)
```

### 8.2 Reglas de output

1. `BUILD/` es efimero y regenerable. **NO DEBE** versionarse en git.
2. Los artefactos en BUILD/ son derivados — la fuente de verdad es el AGENT.md.
3. Cada transmutacion **DEBE** producir artefactos completos, no deltas.
4. El frontmatter YAML del AGENT.md **DEBE** strippearse antes de materializar el output.
5. `config.json` del workspace KORA **DEBE** excluirse del output — su informacion informa la config de plataforma pero **NO** se copia.

## 9. Registro de transmutacion (_transmutation.yml)

Toda transmutacion **DEBE** emitir un manifiesto que registra fuente, target, fidelidad y perdidas.

### 9.1 Schema

```yaml
source: AGENT.md               # path al IR fuente
source_hash: "sha256:abc123..."  # hash del IR al momento de transmutacion
target: claude-code             # target name
target_path: BUILD/claude-code/kora/curator.md
adapter: CM-TRANSMUTE-CLAUDE-CODE
timestamp: "2026-04-14T15:30:00-04:00"  # ISO-8601 con timezone
version: "1.0.0"               # version de la spec usada
fidelity:
  dim_1_coalgebra: preserved | degraded | lost
  dim_2_plan: preserved | degraded | lost
  dim_3_interface: preserved | degraded | lost
  dim_4_fibers:
    identity: preserved | degraded | lost
    operator: preserved | degraded | lost
    memory: preserved | degraded | lost
    runtime: preserved | degraded | lost
    knowledge: preserved | degraded | lost
  dim_5_composition: preserved | degraded | lost
  dim_6_safety: preserved | degraded | lost
losses:
  - "coalgebra: FSM expresada como prosa; sin engine de estados"
  - "safety: limits no configurables via .md; enforcement implicito"
  - "fibers.memory: Claude Code gestiona su propia memoria; no inyectable"
```

### 9.2 Semantica de fidelidad

| Valor | Semantica |
| --- | --- |
| **preserved** | La dimension se materializa con fidelidad completa en el target. La informacion sobrevive sin perdida semantica. |
| **degraded** | La dimension se materializa parcialmente. Hay perdida de estructura, enforcement o expresividad, pero el contenido semantico principal sobrevive como prosa o config parcial. |
| **lost** | La dimension no tiene superficie en el target. La informacion se omite o solo se puede expresar como nota informativa sin efecto. |

### 9.3 Ejemplo completo — curator a claude-code

```yaml
source: AGENTS/kora/curator/AGENT.md
source_hash: "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
target: claude-code
target_path: BUILD/claude-code/kora/curator.md
adapter: CM-TRANSMUTE-CLAUDE-CODE
timestamp: "2026-04-14T15:30:00-04:00"
version: "1.0.0"
fidelity:
  dim_1_coalgebra: degraded
  dim_2_plan: preserved
  dim_3_interface: degraded
  dim_4_fibers:
    identity: preserved
    operator: preserved
    memory: lost
    runtime: degraded
    knowledge: degraded
  dim_5_composition: degraded
  dim_6_safety: degraded
losses:
  - "dim_1: FSM serializada como secciones markdown con transiciones en prosa; sin engine de estados; prioridades expresadas como orden de condicionales"
  - "dim_3: tools expresadas como instrucciones informativas; sin enforcement nativo de tool_use; routing maps inline"
  - "dim_4.memory: Claude Code gestiona memoria propia; MEMORY.md y episodic no inyectados"
  - "dim_4.runtime: model_routing no aplicable; runtime_capabilities implicitas"
  - "dim_4.knowledge: allowed_kb como lista informativa; sin enforcement server-side"
  - "dim_5: sub-agentes parciales via .claude/agents/; hooks cross-gateway no disponibles; rejection routing degradado a prosa"
  - "dim_6: sandbox, tools.deny, limits y policy_flags no configurables via .md; degradados a prosa informativa"
```

## 10. Invocacion

```bash
# Transmutar un agente a un target especifico
python3 scripts/kora transmute --target claude-code kora/curator

# Transmutar todos los agentes a un target
python3 scripts/kora transmute --target openclaw

# Transmutar un agente a todos sus targets declarados
python3 scripts/kora transmute kora/curator

# Dry-run: mostrar que se produciria sin escribir
python3 scripts/kora transmute --dry-run --target claude-code kora/curator

# Forzar re-transmutacion (ignora cache de hash)
python3 scripts/kora transmute --force --target claude-code kora/curator
```

### 10.1 Argumentos

| Argumento | Tipo | Default | Descripcion |
| --- | --- | --- | --- |
| `agent` | positional (opcional) | todos | Namespace/nombre del agente (e.g., `kora/curator`) |
| `--target` | string (opcional) | todos los targets del agente | Target especifico |
| `--dry-run` | flag | false | Mostrar plan sin ejecutar |
| `--force` | flag | false | Re-transmutar aunque el hash no haya cambiado |
| `--output` | path | BUILD/ | Directorio de salida alternativo |

### 10.2 Proceso

1. Resolver agente: `{namespace}/{nombre}` a `AGENTS/{namespace}/{nombre}/AGENT.md`
2. Parsear IR: extraer las 6 dimensiones del AGENT.md
3. Validar pre-transmutacion: `validate --profile strict` sobre el workspace
4. Para cada target:
   a. Cargar adapter skill (CM-TRANSMUTE-{TARGET})
   b. Invocar modelo con adapter + IR parseada
   c. Validar output contra schema del target
   d. Depositar artefactos en BUILD/{target}/{namespace}/{agent}/
   e. Emitir _transmutation.yml
5. Reportar resultado

## 11. Validacion

### 11.1 Pre-transmutacion

El AGENT.md **DEBE** pasar validacion antes de ser transmutado:

1. `python3 scripts/kora validate --profile strict` — el workspace del agente es conformante
2. Las 6 dimensiones estan presentes y segregadas en el IR
3. No hay contaminacion inter-dimensional
4. Todo CM-* referenciado en coalgebra resuelve en skills/

### 11.2 Post-transmutacion

El output **DEBE** pasar validacion del schema del target:

| Target | Validacion |
| --- | --- |
| claude-code | Markdown bien formado; no contiene frontmatter YAML; no contiene config.json |
| openclaw | `openclaw doctor` sobre workspace target; config valido |
| codex | instructions.md bien formado; config.json valido contra schema Codex |
| gemini | GEMINI.md bien formado; settings.json valido contra schema Gemini |

### 11.3 Registro

Toda transmutacion **DEBE** emitir `_transmutation.yml`. Una transmutacion sin registro es invalida.

### 11.4 Tabla de checks

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| IR completo | Las 6 dimensiones presentes | lint | Completar AGENT.md |
| IR segregado | Sin contaminacion inter-dimensional | lint | Corregir IR |
| Workspace valido | `validate --profile strict` pasa | lint | Corregir workspace |
| Skills resolubles | Todo CM-* referenciado existe | lint | Crear o corregir skill |
| Frontmatter stripped | Output no contiene frontmatter YAML | lint | Corregir adapter |
| Config excluido | config.json no copiado al output | lint | Corregir adapter |
| Schema target | Output valido contra schema del target | lint | Corregir adapter |
| Registro emitido | _transmutation.yml presente y completo | lint | Emitir registro |
| Hash coherente | source_hash coincide con AGENT.md actual | lint | Re-transmutar |
| Fidelidad documentada | Toda dimension tiene fidelidad declarada en registro | lint | Completar registro |
| Perdidas documentadas | Toda dimension `degraded` o `lost` tiene entrada en losses | lint | Completar registro |

## 12. Relacion con runtime-spec-md

Esta spec reemplaza las secciones §4-§9 de `runtime-spec-md.md` para agentes en formato AGENT.md. Especificamente:

| runtime-spec-md | transmutation-spec | Relacion |
| --- | --- | --- |
| §4 Adapters por plataforma | §4 Targets, §5 Adapters | Reemplazado: adapters son Skills, no tablas estaticas |
| §5 Wrapper generation | §8 Output format | Reemplazado: output es BUILD/ con estructura por target |
| §6 Platform equivalence | §7 Fidelidad por target | Reemplazado: fidelidad con granularidad por dimension |
| §7 Model routing | §6.6 Dim 6 Safety | Absorbido: routing es parte de la dimension Safety |
| §8 Fallback y budget | §6.6 Dim 6 Safety | Absorbido: fallback es parte de la dimension Safety |
| §9 Transmutacion | §1-§11 completa | Reemplazado: spec dedicada con mapeo exhaustivo |

`runtime-spec-md` sigue vigente para:

- Workspaces en formato legacy (5 archivos sin AGENT.md)
- §3 Core agnostico de plataforma (preservacion, reglas base)
- §9.7 Runtime drift (reconciliacion, source of truth)
- §10 Invariantes
- §11 Validacion legacy

La migracion de formato legacy a AGENT.md es ortogonal a esta spec y se gobernara por su propio proceso.

## 13. Precedencia

```
gobernanza > agent-spec-md > transmutation-spec > runtime-spec-md
```

En caso de conflicto entre esta spec y `runtime-spec-md`, esta spec prevalece para agentes en formato AGENT.md. Para agentes en formato legacy, `runtime-spec-md` prevalece.

## 14. Migracion

Esta seccion se establece con v1.0.0.

### Contrato vigente v1

- AGENT.md como IR de 6 dimensiones: coalgebra, plan, interface, fibers, composition, safety.
- 4 targets: claude-code, openclaw, codex, gemini.
- Adapters como Skills KORA, no scripts programaticos.
- Mapeo exhaustivo dimension x target con fidelidad documentada.
- Output en BUILD/{target}/{namespace}/{agent}/.
- _transmutation.yml obligatorio con fidelidad por dimension y perdidas.
- Validacion pre y post transmutacion.
- Precedencia: gobernanza > agent-spec-md > transmutation-spec > runtime-spec-md.

Toda futura transicion major **DEBE** documentar aqui: (1) que cambio, (2) que migrar, y (3) que se depreca.

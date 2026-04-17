---
_manifest:
  urn: "urn:kora:kb:agentfile-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-14"
    source: "v1.x: IR canonico del agente KORA; v2.0 redefine agentfile como serializacion-de-ontologia, derivada de harness-spec PMI × LFS"
version: "2.0.0"
status: published
tags: [spec, agente, agentfile, serializacion, proyeccion, compat]
lang: es
extensions: {}
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:skill-overlay-spec"
  cites:
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
---

# KORA/Agentfile-Spec v2.0.0

## 1. Definicion

`AGENT.md` es **una serializacion de authoring** del vector ontologico
PMI × LFS (definido en `harness-spec`). No es la ontologia del agente; es un
*shape* de authoring conveniente para agentes con plan ramificado, materia
persistente e interaccion bidireccional.

### 1.1 Cambio respecto a v1

v1.x trataba `AGENT.md` como **definicion primaria** del agente, con 6
dimensiones (coalgebra, plan, interface, fibers, composition, safety)
tratadas como ontologicas. Eso colapsaba tres capas distintas (ontologia,
authoring, runtime) en un solo plano, y usaba el nombre "coalgebra" para una
estructura que no era coalgebra formal.

v2.0 redefine `AGENT.md` como **serializacion**: un shape concreto que
proyecta sobre el vector ontologico de `harness-spec`. El vector es la
definicion primaria; el shape es authoring convencional.

## 2. Dominio de proyeccion

`AGENT.md` es la serializacion canonica para vectores con:

- **Π ≥ 2** (plan ramificado o con fixed-points).
- **Μ ≥ 2** (materia persistente individual o ambiental).
- **Ξ ∈ {2, 3, 4}** (interaccion bidireccional, coreografiada o composicional).
- **Λ ∈ {0, 1, 2}** (individual, organizacional, ecosistema).
- **Φ ∈ {1, 2, 3}** (instrumental, colaborativo, hibrido).

Vectores fuera de este dominio usan otras serializaciones (`skill-overlay-spec`
para Π≤2 y Μ≤1; `platform-agent-spec` para Μ=3 con ambiente externo).

Un mismo vector admite **multiples serializaciones**. El vector ontologico es
el source of truth; las serializaciones son proyecciones.

## 3. Fuente de verdad

1. El **vector ontologico** (`extensions.kora.harness_vector`) es la fuente
   autoritativa del agente.
2. El **shape de authoring** (las 6 dimensiones de §4) es una proyeccion
   conveniente del vector. Puede regenerarse desde el vector.
3. Todo mirror legacy es subordinado.
4. Todo artefacto runtime es derivado.

Si el shape contradice el vector, **el vector prevalece**. En practica, checks
garantizan consistencia entre ambos.

## 4. Envelope y shape de authoring

### 4.1 Frontmatter minimo

```yaml
---
_manifest:
  urn: "urn:{namespace}:agent:{id}"
  provenance:
    created_by: "..."
    created_at: "YYYY-MM-DD"
    source: "..."
version: "semver"
status: active  # lifecycle ejecutable (gobernanza §5)
name: "AgentName"
tags: [...]
lang: es
extensions:
  kora:
    # Vector ontologico — autoritativo
    harness_vector:
      pi: 2
      mu: 2
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2,2,2,2,1]
    presentation: state-primary
    # Metadata de atlas (descriptiva, opcional)
    atlas:
      harness_name: persona      # atlas A
      form: agent-proper         # atlas B
      hcai_metaphor: control-center  # atlas C
# Metadata de encaje runtime-especifica (opcional, por target)
  claude_code:
    model: opus
    color: purple
    max_turns: 15
    memory: user
  openclaw:
    bot_handler: telegram
    acp_compliant: true
# Agente: shape de 6 dimensiones (proyeccion del vector)
agent:
  profile: { ... }       # antes 'coalgebra' (descriptivo, no formal)
  plan: { ... }          # proyeccion de Π
  interface: { ... }     # proyeccion de Ξ
  context: { ... }       # antes 'fibers' (disuelto en subcampos)
  composition: { ... }   # proyeccion de Ξ-4 cuando aplica
  invariants: { ... }    # proyeccion de Σ + safety estructural
---
```

Cambios v2 respecto al schema anterior:

- `coalgebra` **renombrado a `profile`** — captura perfil descriptivo (description, domain, triggers, outputs). No es coalgebra formal; el nombre v1 era desfase semantico.
- `fibers` **disuelto** — sus 5 subcampos migran (ver §5).
- `safety` **bifurcado** — `invariants` declara Σ (etico) + derivacion de safety estructural (no declaracion directa).
- `harness_vector` **obligatorio** en `extensions.kora`.

### 4.2 Las 6 dimensiones como proyeccion del vector

Las dimensiones del shape son **convenciones de authoring**, no ontologia.
Mapeo con el vector ontologico:

| Dimension shape | Que contiene | Proyecta sobre |
|------------------|--------------|-----------------|
| `agent.profile` | description, domain, triggers, outputs, narrative | descriptivo; no proyecta a vector (es atlas) |
| `agent.plan` | initial_state, terminal_state, states (FSM) | Π (free monad expresado como FSM) |
| `agent.interface` | tools, permissions, protocolos | Ξ (lente polinomial o higher) |
| `agent.context` | identity, operator_profile, memory_config, runtime_hints, kb_refs | Μ (memory), Φ (operator), extensions (runtime), Knowledge refs |
| `agent.composition` | sub_agents, golden_paths, circuit_breakers, event_routing | Ξ-4 si aplica (operad dinamica); Λ si delega |
| `agent.invariants` | hard_rules, co_induction, guardrails, ethical_commitments | Σ (etico) + safety estructural derivable |

La dimension `profile` es **descriptiva** — no tiene peso ontologico. Sirve
para documentacion humana y metadata de descubrimiento.

## 5. Disolucion del objeto `fibers` (migracion v1 → v2)

En v1, `fibers` agrupaba 5 subcampos heterogeneos. v2 disuelve el contenedor
y redistribuye:

| Subcampo v1 | Destino v2 | Razon |
|--------------|------------|--------|
| `fibers.memory` | `agent.context.memory_config` + proyecta a **Μ** del vector | Materia temporal — estructural |
| `fibers.operator` | `agent.context.operator_profile` + proyecta a **Φ** | Contexto humano — HAJCS |
| `fibers.runtime` | `extensions.{runtime}.*` | Contexto de ejecucion — runtime-specifico, fuera del IR |
| `fibers.knowledge` | `extensions.kora.allowed_kb[]` (ya existente) | Acceso epistemico — morfismos a KnowCat, no propiedad del agente |
| `fibers.identity` | `extensions.distribution.identity` o metadata atlas | Authoring shape — metadata de presentacion |

Migracion automatica: `kora migrate --profile v2-agentfile` auto-redistribuye.

## 6. Safety: bifurcacion estructural vs normativa

v1 tenia `agent.safety` como campo monolitico con hard_rules, co_induction,
guardrails, alignment. Eso mezclaba dos cosas categoricamente distintas.

v2 las separa:

### 6.1 Safety estructural (derivada, no declarada)

- Sub-coalgebra `S ⊆ U` cerrada bajo la dinamica `α` (harness-spec §4.2).
- **No se declara en `AGENT.md`** — se deriva del vector (Μ, Ξ) + `invariants`.
- Check `safety-closure` verifica: si existe `hard_rules` que restringen
  estados, la sub-coalgebra correspondiente cierra bajo las transiciones del
  plan.

### 6.2 Σ normativa (declarada)

Vector etico de 5 componentes {safety_norm, fairness, transparency,
accountability, sustainability}. Se declara en:

- `extensions.kora.harness_vector.sigma` (vector compacto).
- `agent.invariants.ethical_commitments` (forma expandida con justificacion).

Ambas formas deben ser consistentes. Check `sigma-consistency` lo valida.

### 6.3 Hard rules y co-induction

Siguen declarandose en `agent.invariants`:

- `hard_rules`: predicados estaticos sobre input/output (heredado).
- `co_induction`: checks de consistencia conductual en multi-turno (heredado).
- `guardrails`: restricciones de rutina (heredado).
- `alignment`: transformacion natural hacia principal (proyecta a Φ).
- `ethical_commitments`: desarrollo de Σ (proyecta a `harness_vector.sigma`).

## 7. Topologia y ubicacion

Un agente productivo vive en `AGENTS/{ns}/{name}/`.

Los subdirs estandar:

- `AGENT.md` — serializacion principal (obligatorio).
- `AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md` — serializacion legacy (opcional, compat §13).
- `memory/` — materia persistente del agente (Μ≥2).
- `_BUILD/{target}/` — outputs de transmutacion (gitignored, regenerable).

Staging: `AGENTS/_FRAGUA/{INBOX,REVIEW}/` para pre-promocion.

## 8. Lifecycle

Agentes son artefactos ejecutables. Lifecycle (gobernanza §5):

```
draft → active → deprecated → retired
```

Las transiciones inversas son invalidas. Un agente retirado no reactivable —
se emite uno nuevo con `supersedes`.

## 9. Validacion

Checks sobre `AGENT.md`:

| Check | Condicion | Severity | Enforcement |
|-------|-----------|----------|-------------|
| Envelope valido | Frontmatter cumple §4.1 | high | schema |
| Vector ontologico presente | `extensions.kora.harness_vector` declarado | high | schema |
| Dominio de proyeccion | Vector cumple §2 (Π≥2, Μ≥2, Ξ≥2) | high | lint |
| Leyes PMI × LFS | Vector cumple harness-spec §4.1 | high | lint (delega) |
| Shape 6 dimensiones | `agent` tiene las 6 dimensiones canonicas | medium | lint |
| Consistencia shape ↔ vector | Los campos del shape reflejan el vector (ej. composition poblada ⟹ Ξ≥4) | medium | lint |
| Safety closure | Si hard_rules existen, sub-coalgebra cierra | medium | manual |
| Σ consistency | Vector Σ compacto coincide con expandido en invariants | medium | lint |
| Body subordinado al frontmatter | El body no contradice el vector | medium | manual |

## 10. Relacion con harness-spec

`harness-spec` es fuente de verdad ontologica. `agentfile-spec` es
serializacion. Cambios en `harness-spec` requieren revisar si
`agentfile-spec` necesita actualizar mapeo de campos.

El vector `harness_vector` **debe existir** en todo `AGENT.md` v2. Los campos
shape (`agent.*`) pueden derivarse del vector o declararse explicitamente;
deben ser consistentes.

## 11. Relacion con otras specs

- `harness-spec`: ontologia fuente.
- `skill-overlay-spec v2.0`: serializacion alternativa para otros dominios del vector.
- `transmutation-spec`: functor de proyeccion a runtimes concretos.
- `runtime-spec-md` + extensions: metadata de encaje runtime-especifica.
- `md-spec`: formato base KORA/MD usado por el frontmatter + body.

## 12. Complejidad y niveles

Los niveles `L0-L4` que v1 mencionaba eran escala de densidad de authoring,
no ontologia. Con harness-spec, la densidad se lee del vector:

- Un agente con vector completo `(2,2,2,0,1,[2,2,2,2,1])` es denso.
- Un agente minimo con `(2,2,2,0,1,[1,1,1,1,0])` es ligero.

No hay clases discretas de complejidad; hay vectores.

## 13. Compatibilidad con workspace legacy (5-componentes)

### 13.1 Coexistencia

Un workspace legacy tiene `AGENTS.md`, `config.json`, `IDENTITY.md`,
`SOUL.md`, `USER.md`, `TOOLS.md`. Si ademas tiene `AGENT.md`, la autoridad
es del **vector ontologico** declarado en `AGENT.md` (harness-spec).

Reglas:

1. Vector ontologico **prevalece** sobre shape legacy.
2. Archivos legacy son **mirrors subordinados** mientras dure la absorcion.
3. Conflicto entre `AGENT.md` y legacy se resuelve a favor del vector
   declarado en `AGENT.md`.
4. Coexistencia prolongada es deuda declarada
   (`extensions.kora.legacy_coexistence: <motivo>`).

### 13.2 Regimen URN de archivos legacy

Legacy usa regimen ejecutable (`gobernanza §4.3`):

| Archivo | URN |
|---------|-----|
| `AGENTS.md`   | `urn:{ns}:agent-bootstrap:{id}-agents:{version}`     |
| `config.json` | `urn:{ns}:agent-bootstrap:{id}-config:{version}`     |
| `IDENTITY.md` | `urn:{ns}:agent-bootstrap:{id}-identity:{version}`   |
| `SOUL.md`     | `urn:{ns}:agent-bootstrap:{id}-soul:{version}`       |
| `USER.md`     | `urn:{ns}:agent-bootstrap:{id}-user:{version}`       |
| `TOOLS.md`    | `urn:{ns}:agent-bootstrap:{id}-tools:{version}`      |

`AGENT.md` v2 mantiene regimen Agentfile (`urn:{ns}:agent:{id}` con `version`
fuera del URN) y puede declarar `supersedes` hacia los URNs legacy.

### 13.3 Disipacion

Progresion: **absorcion** → **mirror** → **eliminacion**. La absorcion a v2
requiere derivar el vector ontologico desde los campos legacy; esto es
automatizable parcialmente (`kora migrate --profile v2-agentfile`).

### 13.4 Prohibiciones

1. Nuevos agentes **NO DEBEN** nacer en scaffold legacy.
2. Nuevas capacidades **NO DEBEN** agregarse al legacy en lugar del vector.
3. Archivos legacy **NO** pueden contradecir safety o alignment del vector.

## 14. Migracion (v1 → v2)

### 14.1 Contrato vigente v2

- `AGENT.md` es serializacion, no ontologia.
- `extensions.kora.harness_vector` es fuente de verdad.
- El campo `coalgebra` (v1) se renombra a `profile` (descriptivo).
- El objeto `fibers` (v1) se disuelve en 5 destinos (§5).
- `safety` se bifurca en estructural derivable + Σ declarable (§6).

### 14.2 Cambios v1 → v2

- §1 redefinicion: `AGENT.md` = serializacion de ontologia.
- §2 dominio de proyeccion explicito.
- §3 fuente de verdad: vector ontologico prevalece.
- §4.1 frontmatter requiere `harness_vector`.
- §4.2 mapeo shape → vector documentado.
- §5 disolucion de `fibers`.
- §6 bifurcacion de safety.
- §9 checks revisados.
- §10-11 relaciones con `harness-spec` y otras specs.

### 14.3 Que migrar

- Agentes productivos actuales: agregar `harness_vector` al frontmatter
  (auto-derivable via `kora migrate --profile v2-agentfile`).
- Renombrar `coalgebra` → `profile` en agent shape.
- Disolver `fibers` en subcampos distribuidos.
- Bifurcar `safety` en `invariants.ethical_commitments` + derivacion.
- Declarar `extensions.kora.atlas.*` opcional para descubrimiento.

### 14.4 Compatibilidad transitoria

Durante la transicion v1 → v2, tooling acepta ambos shapes y deriva el
vector automaticamente si falta. Al completarse migracion de los 35
workspaces en `_FRAGUA/INBOX/`, el v1 se depreca.

### 14.5 Que se depreca en v2

- Uso del nombre "coalgebra" para perfil descriptivo.
- Objeto `fibers` como contenedor heterogeneo.
- Dimension `safety` monolitica.
- Declaracion ontologica implicita en el shape (sin vector explicito).

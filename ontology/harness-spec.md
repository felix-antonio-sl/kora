---
_manifest:
  urn: "urn:kora:kb:harness-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "ICAS-BoK corpus-categorico-arquitecto-sistemas-categorial-agentico; HCAI Foundations (Xu 2025); Shneiderman 2D framework; Libkind-Spivak Poly; revisión de docs oficiales Claude Code, Codex, Gemini, OpenClaw y Mastra"
version: "1.1.1"
status: publicado
tags: [spec, ontologia, arnés, pmi-lfs, agentico, hcai, constitucion]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
  cites:
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:procesos-spec"
    - "urn:kora:kb:risk-register-spec"
    - "urn:kora:kb:multiagente-spec"
    - "urn:fxsl:kb:icas-agencia"
    - "urn:fxsl:kb:icas-efectos"
    - "urn:fxsl:kb:icas-interaccion"
    - "urn:fxsl:kb:icas-escala"
---

# KORA/Harness-Spec v1.1.1

## 1. Definicion y propósito

`harness-spec` es la **constitucion ontologica** de los artefactos agenticos de
KORA. Define **que es** un artefacto agentico en el IR canonico, con rigor
categorico y alineamiento HCAI.

No es una spec de serializacion. No describe cómo se escribe un agente en
Markdown, ni como se ejecuta en un runtime. Esos son concerns de otras specs
(`autoria-spec`, `runtime-spec-md`).

Esta spec define **el espacio ontologico**. Las serializaciones son *shapes* de
authoring que proyectan sobre este espacio. Los runtimes son *fibras* que
consumen proyecciones.

### 1.1 Principio constitucional

> **KORA IR canoniza ontologia, no serializacion.**

Un artefacto agentico **es** un vector en el espacio ontologico definido aqui.
Cualquier serializacion (`AGENT.md`, `SKILL.md`, workspace OpenClaw) es una
**proyeccion de ese vector** a un *shape* concreto de authoring.

Consecuencia: dos artefactos con el mismo vector ontologico son
**categoricamente equivalentes**, aunque sus serializaciones difieran. Dos
artefactos con vectores distintos son **categoricamente distintos**, aunque
sus serializaciones se vean iguales.

## 2. Axioma fundamental

El axioma viene directo de `14-agencia` (Libkind-Spivak):

> **Un sistema agentico es la interaccion entre un plan finito (free monad `m_p`) y una materia infinita (cofree comonad `c_q`), modulada por una ley de interaccion `Ξ: m_p ⊗ c_q → m_{p⊗q}`.**

Esta tripleta es la estructura irreducible. Todo lo demas es **variacion,
contexto o presentacion** de la tripleta.

Formalmente, un **artefacto agentico** es:

```
Artefacto = (m_p × c_q × Ξ) ⋉ (Contexto)
```

donde `⋉` denota producto semidirecto: el contexto modula la tripleta, no la
sustituye.

## 3. El espacio ontologico PMI × LFS

El artefacto se caracteriza por un **vector de 6 componentes** sobre dos
tripletas semanticamente distintas.

### 3.1 Tripleta estructural PMI

Describe el artefacto **en si**. Deriva de la tripleta del corpus.

#### Π — Plan

Que sabe hacer el artefacto. Corresponde al free monad `m_p`.

- **Π-0**: sin plan — funcion pura `T: C → C`.
- **Π-1**: plan lineal — procedimiento secuencial sin ramificacion semantica.
- **Π-2**: plan ramificado — free monad `m_p` bien fundado (arbol de decision finito).
- **Π-3**: plan con fixed-points — free monad con recursion (interpretadores, meta-razonamiento).

#### Μ — Materia

Como se sostiene el artefacto en el tiempo. Corresponde al cofree comonad `c_q`.

- **Μ-0**: sin materia propia — ejecutor externo provee todo el soporte.
- **Μ-1**: materia efimera — scratchpad intra-invocacion (coalgebra con `U` acotada).
- **Μ-2**: materia persistente individual — estado cross-session por operador.
- **Μ-3**: materia ambiental — cofree comonad bisimular con eventos externos (always-on).

#### Ξ — Interaccion

Como el artefacto acopla plan con materia y con el mundo. Corresponde a la
ley de interaccion y a la composicion externa.

- **Ξ-0**: sin interaccion formal — ejecutor implicito del runtime.
- **Ξ-1**: interaccion atomica — invocacion simple con contrato I/O (lente trivial).
- **Ξ-2**: interaccion bidireccional — lente polinomial `φ: S·y^S → p`.
- **Ξ-3**: interaccion coreografiada — protocolo multi-fase (session types, Poly triangleleft).
- **Ξ-4**: interaccion composicional — operad dinamica `Org^#_m` (delegacion jerarquica con feedback).

### 3.2 Tripleta contextual LFS

Describe el artefacto **en relacion** con el contexto humano, organizacional
y etico. Deriva de HCAI (Xu 2025).

#### Λ — Nivel sociotecnico (hHCAI)

A que escala opera el artefacto.

- **Λ-0**: individual (scope de un operador).
- **Λ-1**: organizacional (equipo, workspace compartido).
- **Λ-2**: ecosistema (multiples organizaciones).
- **Λ-3**: sociedad (institucion, norma publica).

#### Φ — Acoplamiento humano-AI (HAJCS)

Como se relaciona con la cognicion humana.

- **Φ-0**: disjunto — no coordina con humano.
- **Φ-1**: instrumental — tool metaphor, supertool.
- **Φ-2**: colaborativo — teammate con liderazgo humano.
- **Φ-3**: hibrido — cognicion distribuida (HAJCS real).
- **Φ-4**: co-evolutivo — adaptacion mutua (futuro HCAI).

#### Σ — Vector etico (HCAI Grand Challenges)

Vector de 5 componentes con valores {0..3}:

```
Σ = [safety_norm, fairness, transparency, accountability, sustainability]
```

- `safety_norm` — compromiso de no-dano (distinto de safety estructural §4.2).
- `fairness` — no-discriminacion, equidad.
- `transparency` — explicabilidad de decisiones.
- `accountability` — atribucion de responsabilidad.
- `sustainability` — impacto ecologico y social.

La vista canonica del IR mantiene `Σ` en la grilla discreta `{0..3}^5` por
ergonomia de authoring. La interpretacion continua de ese vector como objeto
enriched en `[0,1]^5`, junto al puente hacia `qa_budget`, se gobierna por
`qa-spec`.

### 3.3 Vector ontologico

Un artefacto agentico se define por:

```yaml
vector_ontologico:
  pi: 2              # 0..3
  mu: 2              # 0..3
  xi: 2              # 0..4
  lambda: 1          # 0..3
  phi: 2             # 0..4
  sigma: [2,2,2,2,1] # [safety, fairness, transp, accntbl, sustain]
```

Seis componentes (nueve valores cuando se expande Σ). Representacion minima y
completa del artefacto en el IR canonico.

## 4. Leyes categoricas

Cada eje es un **retículo** (poset con join y meet). El espacio total es
producto reticular con estructura de producto semidirecto.

Traces to: `urn:kora:kb:cat-harness-lattice` §2-§3 (PMI×LFS formalizado como lattice producto acotado; las 5 leyes inter-eje §4.1 recortan el sublattice acotado de vectores bien-formados). La relación con la F-coálgebra de agente queda como problema abierto, no morfismo demostrado (ibíd. §5).

### 4.1 Leyes de consistencia inter-eje

Los ejes **no son todos independientes**. Hay restricciones obligatorias:

1. **Π requiere Μ acorde**: Π≥3 (fixed-points) requiere Μ≥1 (necesita estado para soportar recursion).
2. **Ξ-4 requiere composicion**: Ξ-4 (operad dinamica) requiere que el artefacto opere sobre multiples sub-artefactos — Λ≥1.
3. **Φ≥2 requiere memoria**: Φ-2+ (colaborativo/hibrido) requiere Μ≥1 — sin estado no hay acoplamiento observable.
4. **Σ accountability requiere transparency**: `Σ.accountability ≥ 2 ⟹ Σ.transparency ≥ 2` (no se puede atribuir responsabilidad sin explicabilidad).
5. **Λ-3 (sociedad) requiere Σ alto**: artefactos societales requieren compromisos eticos completos — `Λ=3 ⟹ Σ.i ≥ 2 ∀i`.

Un vector que viola estas leyes es **mal-formado**. Checks obligatorios.

### 4.2 Safety estructural vs Σ.safety_norm

Son **dos cosas distintas**:

- **Safety estructural** (`S_struct`): sub-coalgebra `S ⊆ U` cerrada bajo la dinamica `α` del cofree comonad. Propiedad **derivada de Μ y Ξ**, no eje independiente.
- **Σ.safety_norm**: compromiso etico de no-dano, vector HCAI. Propiedad **contextual**, modula comportamiento.

El marco separa ambas. El check `safety-closure` opera sobre `(Μ, Ξ)` verificando que `α(S) ⊆ F(S)`. El check `ethical-sigma-valid` opera sobre Σ.

### 4.3 Morfismos del espacio

- **Elevacion**: `v → v'` cuando `v ≤ v'` componente a componente (join entrega `v ∨ v'`).
- **Proyeccion**: `v → v''` donde `v'' ≤ v` (meet entrega `v ∧ v'`).
- **Transmutacion a runtime**: functor `T_R: Espacio → Ideal_R` — ver `transmutation-spec`.

## 5. Tres atlas complementarios

El mismo vector admite tres descripciones. Los atlas son **proyecciones
semanticas**, no clasificaciones disjuntas.

### 5.1 Atlas A — Arneses categoricos

Regiones nombradas del espacio con fundamento categorico.

| Arnés | Π | Μ | Ξ | Λ | Φ | Σ dominante | Ejemplo |
|-------|---|---|---|---|---|-------------|---------|
| **Utilidad** | 1 | 0 | 1 | 0 | 1 | bajo | skill trivial |
| **Disciplina** | 2 | 0 | 1-2 | 0 | 1 | medio | `cat-thinking` |
| **Delegado** | 2 | 1 | 2 | 0 | 1 | medio | subagente Task |
| **Persona** | 2 | 2 | 2-3 | 0-1 | 1-2 | alto | `polymath` |
| **Orquestador** | 2-3 | 2 | 4 | 1-2 | 2 | alto | `kora/forgemaster` |
| **Servicio** | 2 | 3 | 3 | 1-2 | 1-2 | alto | agente OpenClaw bot |
| **Arquetipo** | meta | meta | meta | meta | meta | meta | perfil scaffold |

Un vector puede caer entre arneses — los arneses son **clusters**, no
particiones.

### 5.2 Atlas B — Formas materiales

Cada runtime concreto soporta ciertas regiones. Los atlas de forma material
mapean vectores a implementaciones runtime actuales.

| Forma material | Runtime(s) | Region tipica |
|----------------|------------|----------------|
| Skill estandar (agentskills.io) | Claude Code, Codex, Gemini | Π=1-2, Μ=0, Ξ=1-2, Λ=0, Φ=1 |
| Subagente | Claude Code Task, Codex agent mode | Π=2, Μ=1, Ξ=2, Λ=0, Φ=1 |
| Agente propiamente tal | Claude Code persona, Codex session | Π=2, Μ=2, Ξ=2-3, Λ=0-1, Φ=1-2 |
| Agente de plataforma | OpenClaw fleet | Π=2, Μ=3, Ξ=3-4, Λ=1-2, Φ=1-2 |

La declaracion de forma material preferida es **metadata de encaje**, no parte
del IR canonico.

### 5.3 Atlas C — Metaforas HCAI (Shneiderman)

Proyeccion en el plano (V, H) de Shneiderman 2D framework. Aunque V (autonomy)
y H (human control) no son ejes propios del IR, derivan de (Μ, Φ):

- **V (autonomia AI)** deriva principalmente de Μ y parte de Π.
- **H (human control)** deriva de Φ.

Cuadrantes canonicos:

| Metafora | V | H | Region |
|----------|---|---|--------|
| **Supertool** | baja | alta | Μ=0, Φ=1, humano lidera |
| **Tele-bot** | media | alta | Μ=1, Φ=2, teleoperacion |
| **Active Appliance** | media | baja | Μ=1, Φ=1, autonomia acotada |
| **Control Center** | alta | media | Μ=2-3, Φ=2, supervision humana |

La zona objetivo HCAI (`high V + high H`) corresponde a `Μ≥2, Φ=2, Λ≥1, Σ
alto` — Orquestador con Control Center.

## 6. Mapeo con el corpus categorico

Cada eje tiene raiz directa en documentos del corpus referencial:

| Eje | Documento primario | Estructura formal |
|-----|---------------------|---------------------|
| Π | `14-agencia`, `09-efectos` | free monad `m_p`, monad `(T, η, μ)` |
| Μ | `14-agencia`, `09-efectos`, `15-tiempo` | cofree comonad `c_q`, sheaf temporal |
| Ξ | `14-agencia`, `11-interaccion` | NT `Ξ: m_p ⊗ c_q → m_{p⊗q}`, lente polinomial |
| Λ | `13-escala`, `hHCAI Xu-Gao 2025` | fibracion de Grothendieck sobre niveles |
| Φ | `14-agencia`, HAJCS Xu-Gao 2024 | pullback humano×AI sobre tarea compartida |
| Σ | `12b-safety-alignment`, `18-calidad-riesgo`, HCAI Grand Challenges | vector en categoria enriched sobre [0,1]^5 |

Esta alineacion garantiza que el marco no es invencion: es **consolidacion**
de estructura categorica ya presente en el corpus + HCAI.

`qa-spec` materializa esta fila como contrato operativo: `harness-spec`
declara el vector discreto y sus leyes; `qa-spec` fija la moneda enriched y los
cambios de base autorizados.

## 7. Invariantes del IR canonico

1. **Canonicidad ontologica**: el vector `vector_ontologico` es la
   representacion autoritativa del artefacto. Toda serializacion es derivada.
2. **Inmutabilidad del nucleo bajo cambio de runtime**: cambiar el target no
   altera el vector; altera solo la metadata de encaje.
3. **Consistencia de leyes inter-eje**: un vector valido respeta §4.1.
4. **Separacion estructural vs normativa**: `S_struct` es derivable; `Σ` es
   declarable.
5. **Preservacion bajo transmutacion**: `T_R` preserva estructura functorial
   o declara perdida (ver `transmutation-spec`).

## 8. Presentacion: estado-primario vs accion-primaria

Meta-dimension ortogonal a los 6 ejes. Eleccion de presentacion del artefacto:

- **estado-primario**: indexado por estado `U`, coalgebra `α: U → F(U)`.
- **accion-primaria**: indexado por morfismo/evento, funtor `Idx: Episodio → Accion`.

Ambas presentaciones son equivalentes modulo anamorfismo/catamorfismo
(dualidad `09-efectos`, Fukada en `14-agencia`). El artefacto declara una
como canonica; la dual es recuperable.

```yaml
extensions:
  kora:
    presentacion: estado-primario  # o accion-primaria
```

## 9. Validacion

Checks obligatorios sobre el vector ontologico:

| Check | Condicion | Severity | Enforcement |
|-------|-----------|----------|-------------|
| `vector-ontologico-presente` | `extensions.kora.vector_ontologico` existe y tiene 6 componentes | high | schema |
| `vector-ontologico-rango` | Valores en rango: Π∈{0..3}, Μ∈{0..3}, Ξ∈{0..4}, Λ∈{0..3}, Φ∈{0..4}, Σ={[v1..v5], vᵢ∈{0..3}} | high | schema |
| `pi-mu-consistency` | Π≥3 ⟹ Μ≥1 | high | lint |
| `xi-composition-consistency` | Ξ=4 ⟹ Λ≥1 | high | lint |
| `phi-memory-consistency` | Φ≥2 ⟹ Μ≥1 | high | lint |
| `sigma-accountability-transparency` | `Σ.accountability≥2 ⟹ Σ.transparency≥2` | medium | lint |
| `lambda-societal-sigma` | `Λ=3 ⟹ Σ.i≥2 ∀i` | medium | lint |
| `safety-closure` | Si `Μ≥1` y `Ξ≥2`, la sub-coalgebra de safety estructural cierra | medium | manual |
| `presentacion-declarada` | `extensions.kora.presentacion` ∈ {estado-primario, accion-primaria} | low | lint |

## 10. Relacion con otras specs

### 10.1 Spec de serializacion (consumidora)

`autoria-spec` es la unica serializacion de authoring para todo
artefacto agentico productivo. Cubre las cuatro formas materiales
(habilidad, subagente, agente-propiamente-tal, agente-plataforma) con
el mismo envelope; el subset del shape que aplica es condicional por
`atlas.forma_material`.

Cada forma material declara su **dominio de proyeccion** (que region
del espacio ontologico cubre) y su **mapeo de campos** (como sus
campos derivan del vector ontologico). Ver `autoria-spec §4, §5, §6`.

### 10.2 Specs de runtime (proyectoras)

Estas specs definen functores `T_R: Espacio → Ideal_R`:

- `runtime-spec-md`: contrato generico.
- `procesos-spec`: functorialidad declarada del toolchain.
- `risk-register-spec`: riesgo como efecto acumulativo sobre el artefacto.
- `multiagente-spec`: coherencia local-global de protocolos distribuidos.
- `claude-code-runtime-extension`, `codex-runtime-extension`, `gemini-runtime-extension`, `openclaw-runtime-extension`, `mastra-runtime-extension`: proyecciones a runtimes concretos.

Cada runtime-extension declara:
- Subconjunto del espacio ontologico que soporta.
- Fidelidad de proyeccion por eje.
- Metadata de encaje runtime-especifica.

### 10.3 Spec de transmutacion

`transmutation-spec` define las leyes del functor `T_R` — que preservar
obligatoriamente, que puede proyectarse con perdida, como declarar la perdida
en `_transmutation.yml`.

### 10.4 Specs de gobernanza y base

- `gobernanza`: precedencia, regimenes URN, identidad.
- `qa-spec`: semantica enriched de `Σ` y budgets de calidad.
- `md-spec`: formato KORA/MD usado por todas las serializaciones.
- `knowledge-spec`: tejido relacional de conocimiento consumible.

## 11. Versionado

- correccion editorial: patch.
- adicion de valores en ejes existentes, nuevos atlas: minor.
- cambio de definicion de ejes, reestructuracion de leyes: major.

## 12. Migracion

### 12.1 Contrato vigente v1.1.0

- KORA IR canoniza ontologia PMI × LFS.
- Seis ejes cardinales + meta-dimension de presentacion.
- Tres atlas complementarios sobre el mismo vector.
- Leyes de consistencia inter-eje obligatorias.
- Separacion estricta entre safety estructural (derivada) y Σ normativa (declarada).

### 12.2 Que migrar desde pre-v1

Los artefactos pre-existentes se migran en una sola pasada con
`kora migrate --perfil a-autoria`. La migracion:

1. Deriva heuristicamente el `vector_ontologico` desde campos anteriores (`harness_vector` legacy incluido).
2. Reemite el frontmatter conforme a `autoria-spec`.
3. Reescribe el URN al regimen unico `urn:{ns}:artefacto:{id}`.
4. El autor revisa y corrige el vector derivado; el toolchain emite
   `TODO` en campos no derivables.

No hay compatibilidad residual: el toolchain rechaza shapes anteriores
tras la migracion (ver `gobernanza §3.3`).

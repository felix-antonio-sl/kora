---
_manifest:
  urn: "urn:kora:kb:transmutation-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "harness-spec v1.1 + runtime-spec-md v3.8 + ICAS corpus 02-preservacion, 06-adjunciones, 09-efectos"
version: "1.1.0"
status: publicado
tags: [spec, transmutacion, functor, proyeccion, preservacion, bisimulacion, runtime]
lang: es
extensions: {}
relations:
  depends:
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:runtime-spec-md"
  cites:
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:multiagente-spec"
    - "urn:fxsl:kb:icas-preservacion"
    - "urn:fxsl:kb:icas-efectos"
---

# KORA/Transmutation-Spec v1.1.0

## 1. Definicion

`transmutation-spec` define las **leyes functoriales de la transmutacion**
desde el IR canonico de KORA (espacio PMI × LFS de `harness-spec`) hacia
runtimes concretos (Claude Code, Codex, OpenClaw, Gemini, Mastra, agentskills.io).

### 1.1 Objetivo

Cuando Felix transmuta un agente KORA a un runtime concreto, necesita:

1. **Correccion estructural** — el artefacto producido respeta las leyes
   categoricas del IR.
2. **Fidelidad declarada** — si hay perdida, se documenta explicitamente.
3. **Reversibilidad parcial** — cuando existe, el artefacto runtime puede
   elevarse de vuelta al IR.
4. **Evidencia verificable** — cada transmutacion emite
   `_transmutation.yml` como proof-carrying artifact.

### 1.2 Principio

> **La transmutacion es functor. Preserva composicion e identidad; la perdida se declara, nunca se oculta.**

## 2. Marco categorico

### 2.1 Functor de proyeccion

Para cada runtime `R`, existe un functor:

```
T_R: KORA_IR → Runtime_R
```

donde:

- Los **objetos** de KORA_IR son vectores en el espacio PMI × LFS.
- Los **morfismos** de KORA_IR son elevaciones/proyecciones entre vectores.
- `Runtime_R` es la categoria de artefactos soportados por el runtime R
  (skills, subagents, agents, bots) con sus morfismos naturales.

El functor `T_R` transporta vectores del IR al subconjunto soportado por R.

### 2.2 Dominio e imagen

Cada runtime `R` tiene:

- **Dominio de definicion** `D_R ⊆ KORA_IR` — vectores que `T_R` puede
  proyectar (con o sin perdida).
- **Imagen** `Im(T_R) ⊆ Runtime_R` — artefactos runtime reales producidos.
- **Kernel declarado** — vectores NO soportados, para los cuales `T_R` no
  esta definido.

Los runtime-extensions (`openclaw-runtime-extension`,
`claude-code-runtime-extension`, `mastra-runtime-extension`, etc.) declaran `D_R` e
`Im(T_R)` por eje.

### 2.3 Adjuncion inversa (cuando existe)

Para runtimes con artefactos foraneos que KORA puede absorber, existe un
functor de elevacion:

```
Lift_R: Runtime_R ⇢ KORA_IR
```

La adjuncion `Lift_R ⊣ T_R` (cuando es construible) garantiza que:

```
T_R ∘ Lift_R = id (modulo perdida declarada)
Lift_R ∘ T_R ≤ id (modulo atlas de encaje)
```

Es decir, ingerir un artefacto runtime, proyectarlo de vuelta, y compararlos
debe producir equivalencia observacional modulo la metadata de encaje.

No todos los runtimes tienen `Lift_R`. Cuando no existe, la transmutacion es
una **proyeccion unidireccional**.

## 3. Preservacion obligatoria

Un functor `T_R` es **correcto** si preserva las leyes functoriales
basicas. Violar cualquiera de estas rompe la transmutacion, no es "perdida
declarada".

### 3.1 Leyes functoriales basicas

| Ley | Enunciado | Consecuencia de violacion |
|------|-----------|-----------------------------|
| **Composicion** | `T_R(f ∘ g) = T_R(f) ∘ T_R(g)` | Orden de pasos se rompe |
| **Identidad** | `T_R(id) = id` | Invocacion trivial se rompe |

### 3.2 Preservacion estructural

| Estructura | Obligacion | Check |
|------------|-----------|--------|
| Naturalidad de Ξ | `T_R(Ξ_IR) = Ξ_R` (el diagrama plan-ejecutor conmuta en el target) | `xi-naturality-preserved` |
| Inclusion de sub-coalgebra safety | Si `S ⊆ U` cierra bajo `α` en IR, `T_R(S) ⊆ T_R(U)` cierra en R | `safety-closure-preserved` |
| Composicion Kleisli | Si el IR declara composicion via `composable_with`, la composicion se refleja en R | `kleisli-composition-preserved` |
| Monotonia en Π | Si `v1.pi ≤ v2.pi` en IR, tras proyeccion `T_R(v1).pi ≤ T_R(v2).pi` | `pi-monotonicity` |
| Monotonia en Μ | Analogo para Μ | `mu-monotonicity` |
| Monotonia en Ξ | Analogo para Ξ | `xi-monotonicity` |

### 3.3 Violacion estructural → transmutacion invalida

Si cualquiera de estas leyes se viola, el functor no es correcto. Es error
categorial, no perdida. La transmutacion **debe fallar**, no emitirse con
warning.

## 4. Proyeccion con perdida declarada

La perdida de capacidad por eje es **permitida** — el target puede no
soportar todos los valores del IR. Pero debe **declararse explicitamente**.

### 4.1 Tipos de fidelidad por eje

Para cada eje `E ∈ {Π, Μ, Ξ, Λ, Φ, Σ}`:

- **Fiel y plena**: `T_R` preserva todos los valores soportados y realiza la
  capacidad completa.
- **Fiel pero no plena**: preserva distinciones pero no realiza toda la
  capacidad del target (el runtime podria hacer mas).
- **Parcial**: algunos valores se proyectan, otros caen fuera del dominio.
- **Colapso permitido**: distintos valores se proyectan al mismo valor
  target (con declaracion explicita de que se pierde la distincion).

### 4.2 Niveles de perdida por eje

| Eje | Perdida minima | Perdida maxima tolerada | Prohibido |
|-----|-----------------|--------------------------|-----------|
| **Π** (plan) | recortar ramas no alcanzables | colapsar Π-3 → Π-2 (pierde recursion) | Π-2 → Π-0 (destruye ramas semanticas) |
| **Μ** (materia) | Μ-2 → Μ-1 (pierde cross-session) | Μ-3 → Μ-1 (pierde ambiente) | Declarar Μ-2 y proyectar a Μ-0 sin aviso |
| **Ξ** (interaccion) | Ξ-3 → Ξ-2 (colapsar multi-fase) | Ξ-4 → Ξ-2 (perder operad) | Romper la bidireccionalidad si IR la declara |
| **Λ** (nivel) | Λ-2 → Λ-1 (ecosystem → org) | Λ-3 → Λ-0 (society → individual, con declaracion) | Silencioso |
| **Φ** (acoplamiento humano) | Φ-2 → Φ-1 (colaborativo → instrumental) | Φ-3 → Φ-1 (hibrido → instrumental) | Degradar Φ sin declaracion cuando IR exige colaboracion |
| **Σ** (etico) | Bajar componentes no-criticos | Perder componentes sin enforcement mecanico pero mantener como compromiso declarado | Colapsar accountability si IR lo exige |

### 4.3 Criterio de aceptabilidad

La perdida es aceptable si y solo si:

1. **Declarada explicitamente** en `_transmutation.yml` (§6).
2. **Justificada** con la capacidad del runtime target.
3. **No violatoria** de §3 (leyes estructurales).
4. **Conocida al operador** — documentada en el runtime-extension spec.

## 5. Bisimulacion modulo proyeccion

Dos artefactos `A_1, A_2` en KORA_IR que son **bisimilares** (equivalencia
observacional segun `09-efectos`) deben seguir siendo bisimilares tras
proyeccion:

```
A_1 ∼_IR A_2  ⟹  T_R(A_1) ∼_R T_R(A_2) (modulo perdida declarada)
```

La bisimulacion runtime es respecto a las observaciones que el runtime
soporta. Si el runtime no soporta cierto tipo de observacion, la
bisimulacion es "modulo esa proyeccion".

Este principio garantiza que **refactorings del IR que preservan
comportamiento observable siguen preservandolo en todos los runtimes**.

## 6. `_transmutation.yml` como proof-carrying artifact

Cada transmutacion emite un artefacto de evidencia en la salida:

```
{workspace}/_BUILD/{target}/_transmutation.yml
```

### 6.1 Contenido obligatorio

```yaml
transmutation:
  # Identificacion
  source_urn: "urn:kora:agent:polymath"
  source_version: "2.0.0"
  target: claude-code
  functor: T_claude_code_v1.2
  timestamp: "2026-04-17T14:23:45Z"
  
  # Vector IR fuente
  source_vector:
    pi: 2
    mu: 2
    xi: 2
    lambda: 1
    phi: 2
    sigma: [2, 2, 2, 2, 1]
    presentation: state-primary
  
  # Preservacion estructural (obligatoria)
  structural_preservation:
    composition: preserved
    identity: preserved
    xi_naturality: preserved
    safety_closure: preserved
    kleisli_composition: preserved
    pi_monotonicity: preserved
    mu_monotonicity: preserved
    xi_monotonicity: preserved
  
  # Proyeccion por eje
  projections:
    pi:
      projected_to: 2
      fidelity: full
    mu:
      projected_to: 2
      fidelity: full
    xi:
      projected_to: 2
      fidelity: full
    lambda:
      projected_to: 1
      fidelity: full
    phi:
      projected_to: 2
      fidelity: full
    sigma:
      projected_to: [2, 2, 2, 1, 1]
      fidelity: partial
      losses:
        accountability:
          declared: 2
          projected: 1
          reason: "claude-code runtime no tiene mecanismo de audit trail persistente"
        sustainability:
          declared: 1
          projected: 1
          reason: "compromiso declarado pero no medible en runtime"
  
  # Claim de bisimulacion
  bisimulation_claim: "equivalent-modulo-projections"
  bisimulation_scope: "observaciones soportadas por claude-code"
  
  # Referencias
  references:
    source_artifact: "AGENTS/kora/polymath/AGENT.md"
    target_artifact: "AGENTS/kora/polymath/_BUILD/claude-code/polymath.md"
    runtime_extension_spec: "urn:kora:kb:claude-code-runtime-extension"
```

### 6.2 Contenido opcional

- `metadata.warnings[]` — advertencias operativas.
- `metadata.environment` — info del entorno (toolchain version, deps).
- `ingest_hint` — si el target admite `Lift_R`, puntero a como elevar de vuelta.

### 6.3 Validacion del artifact

El archivo `_transmutation.yml` debe validarse contra un schema JSON
(`schemas/kora-transmutation-schema.json`). Checks:

- Estructura correcta.
- `source_urn` resuelve.
- Cada componente de `projections` tiene `projected_to` y `fidelity`.
- Si `fidelity: partial`, `losses` estan declaradas.
- `structural_preservation` tiene las 8 filas obligatorias y todas estan en
  `preserved` (si alguna fallara, la transmutacion no debio emitirse).

## 7. Matriz de preservacion por runtime

Cada runtime tiene una matriz `P_R[eje × valor_IR → valor_R | nulo]` que
declara su fidelidad por eje.

### 7.1 Estructura de la matriz

```yaml
# Ejemplo: claude-code
runtime: claude-code
preservation_matrix:
  pi:
    "0": { projected: 0, fidelity: full }
    "1": { projected: 1, fidelity: full }
    "2": { projected: 2, fidelity: full }
    "3": { projected: 2, fidelity: partial, loss: "fixed-points se aplanan" }
  mu:
    "0": { projected: 0, fidelity: full }
    "1": { projected: 1, fidelity: full }
    "2": { projected: 2, fidelity: full }
    "3": { projected: null, fidelity: none, loss: "Claude Code no soporta ambiente externo always-on" }
  xi:
    "0": { projected: 0, fidelity: full }
    "1": { projected: 1, fidelity: full }
    "2": { projected: 2, fidelity: full }
    "3": { projected: 2, fidelity: partial, loss: "Claude Code no modela multi-fase explicita" }
    "4": { projected: 2, fidelity: partial, loss: "Claude Code no modela operad dinamica" }
  lambda:
    "0": { projected: 0, fidelity: full }
    "1": { projected: 1, fidelity: full }
    "2": { projected: 1, fidelity: partial, loss: "ecosistema se proyecta como org" }
    "3": { projected: null, fidelity: none, loss: "society-in-the-loop no soportado" }
  phi:
    "0": { projected: 0, fidelity: full }
    "1": { projected: 1, fidelity: full }
    "2": { projected: 2, fidelity: full }
    "3": { projected: 2, fidelity: partial, loss: "hybrid cognition no soportado nativamente" }
    "4": { projected: null, fidelity: none, loss: "co-evolutive no soportado" }
  sigma:
    safety_norm: { max_supported: 3, enforcement: "policy-based" }
    fairness: { max_supported: 2, enforcement: "declarative" }
    transparency: { max_supported: 3, enforcement: "explainable-output" }
    accountability: { max_supported: 1, enforcement: "none-beyond-logs" }
    sustainability: { max_supported: 1, enforcement: "declarative" }
```

### 7.2 Uso operativo

Cuando `kora transmute --target claude-code --agent X`:

1. Lee vector IR de `artifacts/agents/{ns}/X/AGENT.md`.
2. Consulta matriz `P_claude-code`.
3. Proyecta cada eje.
4. Emite artefacto target + `_transmutation.yml`.
5. Documenta cada perdida.

Si algun eje no tiene entrada en la matriz o el vector excede el dominio,
**falla con mensaje claro** indicando que el IR excede capacidad del target.

## 8. Reglas operativas

### 8.1 Obligatorias

1. Toda transmutacion **DEBE** emitir `_transmutation.yml`.
2. El target **NUNCA** es fuente primaria.
3. Toda perdida **DEBE** declararse.
4. Las leyes estructurales (§3) **DEBEN** preservarse.
5. La matriz de preservacion del runtime **DEBE** estar en el
   runtime-extension spec correspondiente.

### 8.2 Recomendadas

1. La transmutacion **DEBERIA** ser idempotente: `T_R(T_R(x)) = T_R(x)` si
   aplica.
2. Cuando exista `Lift_R`, **DEBERIA** ser invocable: `kora ingest --from
   claude-code --file X.md`.
3. La matriz de preservacion **DEBERIA** versionarse con el runtime
   target.

### 8.3 Prohibidas

1. Emitir artefacto runtime sin `_transmutation.yml`.
2. Transmutar vectores fuera del dominio del runtime sin fallo.
3. Declarar fidelidad `full` cuando hay perdida real.
4. Ocultar violacion de leyes estructurales como "perdida declarada".

## 9. Ingesta inversa (`Lift_R`)

Cuando un runtime tiene un artefacto foraneo que KORA quiere absorber, el
proceso inverso es ingesta:

```
kora ingest --from {runtime} --file {path} [--namespace {ns}]
```

Ejemplos:

- `kora ingest --from claude-code --file ~/.claude/agents/polymath.md
  --namespace kora` — eleva un subagente Claude Code a workspace KORA.
- `kora ingest --from codex --file ~/.codex/skills/my-skill/SKILL.md` —
  eleva un skill Codex.
- `kora ingest --from openclaw --workspace
  ~/openclaw-fleet/workspaces/mente-omega` — eleva un workspace OpenClaw.

### 9.1 Proceso

1. Parse del artefacto foraneo.
2. Aplicar `Lift_R` — construir vector PMI × LFS desde campos foraneos.
3. Generar `AGENT.md` (o `SKILL.md`) con vector + shape derivado.
4. Declarar ganancias: el artefacto elevado puede expresar mas estructura
   que la declarada originalmente (el IR es mas rico).
5. Emitir `_ingestion.yml` simetrico a `_transmutation.yml`.

### 9.2 Adjuncion

Si `Lift_R ⊣ T_R`, entonces:

```
ingest → transmute → ingest ≡ ingest (modulo atlas de encaje)
transmute → ingest → transmute ≡ transmute (modulo perdida declarada)
```

Esto es el round-trip test. Los checks `ingest-idempotency` y
`transmute-idempotency` lo validan.

### 9.3 Runtimes sin `Lift_R`

Algunos runtimes no admiten ingesta inversa (el artefacto foraneo carece de
suficiente metadata para reconstruir el vector IR con confianza). En ese
caso:

- El runtime-extension declara `lift_supported: false`.
- La ingesta manual requiere que Felix complete el vector a mano.
- El `_ingestion.yml` marca `source_fidelity: unknown`.

## 10. Composicion de functores

Si hay cadena `KORA_IR → R1 → R2`, la composicion `T_{R2} ∘ T_{R1}` es un
functor, y:

- Las perdidas se acumulan: `loss_{R2 ∘ R1} ⊇ loss_{R1} ∪ loss_{R2}`.
- `_transmutation.yml` del segundo paso debe referenciar el primero.
- Orden importa — no siempre `T_{R2} ∘ T_{R1} ≡ T_{R1} ∘ T_{R2}`.

Ejemplo: KORA → Claude Code → Codex (via manual copy) — dos transmutaciones
encadenadas con perdidas acumuladas.

En la practica, KORA transmuta directamente a cada runtime destino; la
composicion encadenada es excepcional.

## 11. Validacion

Checks obligatorios:

| Check | Condicion | Severity | Enforcement |
|-------|-----------|----------|-------------|
| `transmutation-yml-emitted` | Todo output target tiene `_transmutation.yml` | high | lint |
| `source-urn-resolves` | `source_urn` del yaml resuelve en catalogo KORA | high | lint |
| `structural-preservation-complete` | Las 8 leyes de §3 estan en `structural_preservation` y todas preservadas | high | schema |
| `projection-declaration-complete` | Cada uno de los 6 ejes tiene entrada en `projections` | high | schema |
| `losses-declared-when-partial` | Si `fidelity: partial`, `losses` declarado con razon | high | schema |
| `matrix-present-per-runtime` | El runtime-extension tiene matriz de preservacion | high | lint |
| `vector-within-domain` | Vector IR esta dentro del dominio del runtime target | high | lint |
| `bisimulation-claim-coherent` | `bisimulation_claim` consistente con fidelidades declaradas | medium | manual |
| `ingest-idempotency` | Si el runtime soporta Lift, `T ∘ L ∘ T ≡ T` modulo atlas | low | manual |

## 12. Relacion con otras specs

- `harness-spec`: ontologia fuente, define espacio IR.
- `autoria-spec`: serializacion de entrada unificada (lo que se transmuta, para las cuatro formas materiales).
- `runtime-spec-md`: contrato generico de runtime.
- Runtime-extensions (`openclaw-`, `claude-code-`, `codex-`, `gemini-`):
  cada una declara matriz de preservacion + encaje.
- `gobernanza`: precedencia; la transmutacion produce outputs derivados
  (§3 gobernanza).

## 13. Versionado

- Cambios editoriales sin cambio de semantica: patch.
- Agregar nuevos checks, campos opcionales en `_transmutation.yml`: minor.
- Cambio de leyes de preservacion, forma de matriz: major.

## 14. Migracion

### 14.1 Contrato vigente v1.0

- Transmutacion es functor, `_transmutation.yml` es evidencia obligatoria.
- Leyes estructurales (§3) obligatorias para todos los runtimes.
- Perdida declarada por eje con matriz de preservacion explicita.
- Ingesta inversa disponible cuando runtime soporta `Lift_R`.

### 14.2 Estado pre-v1.0

Antes de esta spec, las transmutaciones emitian outputs sin evidencia
estructurada. El contenido de `_transmutation.yml` estaba disperso en
ubicaciones no normadas.

### 14.3 Que migrar

- Implementacion de `kora transmute` debe emitir `_transmutation.yml`
  conforme al schema §6.
- Runtime-extensions existentes (`openclaw-runtime-extension`) deben
  completar su matriz de preservacion (§7).
- Nuevos runtime-extensions (`claude-code-`, `codex-`, `gemini-`) deben
  incluir matriz desde su primera version.

### 14.4 Que se depreca

- Outputs runtime sin `_transmutation.yml` adjunto.
- Declaraciones implicitas de fidelidad.
- Transmutaciones que violan leyes estructurales "silenciosamente".

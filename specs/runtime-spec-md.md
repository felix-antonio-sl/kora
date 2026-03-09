---
_manifest:
  urn: "urn:kora:kb:runtime-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 04, 07, repair of cross-platform adapter contract"
version: "3.2.0"
status: published
tags: [spec, runtime, deployment, adapters, wrappers, fallback]
lang: es
---

# KORA/Runtime-Spec v3.2.0

## 1. Definicion

Esta especificacion gobierna la adaptacion de un workspace KORA a un runtime concreto sin alterar la semantica del agente.

`runtime-spec` no redefine al agente. Gobierna transporte, inyeccion, enforcement y equivalencia comportamental razonable entre plataformas.

### 1.1 Alcance

Esta especificacion gobierna:

1. adapters por plataforma
2. wrappers derivados
3. preservacion de componentes e interfaz
4. model routing, fallback y budget
5. criterios de equivalencia cross-platform

## 2. Definiciones

| Termino                | Definicion                                                           |
| ---------------------- | -------------------------------------------------------------------- |
| Runtime                | Entorno de ejecucion que consume un workspace KORA                   |
| Platform Adapter       | Modulo que mapea componentes KORA al formato nativo del runtime      |
| Wrapper                | Artefacto derivado que adapta un workspace sin modificar sus fuentes |
| Behavioral Equivalence | Equivalencia funcional razonable del mismo agente entre plataformas  |
| Fallback Chain         | Cadena ordenada de modelos alternativos                              |
| Budget Enforcement     | Politica server-side de costo o tokens                               |

## 3. Core agnostico de plataforma

Todo runtime KORA **DEBE** preservar:

1. estructura del workspace
2. interfaz semantica declarada
3. security aplicada server-side
4. lazy-load de Skills

Traces to: formal/07 §2 (Preservation by Interface) ; formal/01 §1.3 (Effect Monad M)

### 3.1 Preservacion de componentes

| Componente            | Regla de preservacion                                                      |
| --------------------- | -------------------------------------------------------------------------- |
| `AGENTS.md`           | La FSM y reglas duras se preservan como behavior                           |
| `TOOLS.md`            | Se mapea a la primitiva de tool-use nativa                                 |
| `SOUL.md` / `USER.md` | Se inyectan solo donde corresponde; no se convierten en wiring ni security |
| `config.json`         | Se aplica fuera del LLM                                                    |
| `skills/`             | Se activa via lazy-load, no en bootstrap total                             |

### 3.2 Reglas base

1. `config.json` **NO DEBE** inyectarse como texto rector al LLM.
2. El runtime **DEBE** aplicar `config.json` server-side.
3. Los Skills **NO DEBEN** inyectarse todos en bootstrap.
4. Un cambio de modelo **NO DEBE** alterar FSM, tools declaradas ni constraints.

## 4. Adapters por plataforma

| Plataforma | Forma de behavior                              | Forma de tools          | Nota                                                  |
| ---------- | ---------------------------------------------- | ----------------------- | ----------------------------------------------------- |
| Claude     | system prompt estructurado / XML o equivalente | tool_use                | delimita bien secciones                               |
| GPT        | instructions Markdown estructuradas            | function calling        | nativo para tools                                     |
| Gemini     | system instruction estructurada                | function declarations   | compatible con grounding                              |
| OpenClaw   | wrapper tipo `SKILL.md` o equivalente          | gateway/platform config | plataforma emergente; nativo para skill-like wrappers |

Reglas:

1. El adapter **DEBE** strippear frontmatter antes de inyectar markdown al LLM.
2. El adapter **DEBE** mapear cada tool declarada o documentar la limitacion.
3. El adapter **NO DEBE** mezclar `config.json` con behavior.
4. La ausencia de equivalencia perfecta **NO DEBE** usarse para justificar drift estructural.

## 5. Wrapper generation

Los wrappers son artefactos derivados. Las fuentes del workspace **NO DEBEN** modificarse durante la generacion.

### 5.1 Reglas de generacion

1. El wrapper **DEBE** generarse fuera del workspace fuente.
2. El wrapper **DEBE** eliminar frontmatter antes de la inyeccion.
3. El wrapper **DEBE** respetar la segregacion original de componentes.
4. El wrapper **DEBERIA** declarar claramente la plataforma target.

## 6. Platform equivalence

La equivalencia cross-platform no exige bisimulacion textual estricta. Exige preservacion funcional de comportamiento e interfaz.

Traces to: formal/01 §5.2 (Bisimulation as Substitutability) ; formal/07 §4.2 (Compositional Preservation)

### 6.1 Invariantes de equivalencia

1. Mismo input -> output funcionalmente equivalente.
2. Mismas tools declaradas -> misma interfaz efectiva.
3. Mismas constraints -> misma fuerza de enforcement.
4. Mismo wiring y misma disponibilidad de Skills.

### 6.2 Evaluacion de equivalencia

Todo runtime **DEBERIA** verificar equivalencia con un conjunto pequeno de inputs representativos por agente y comparar:

- clasificacion o routing
- citas o evidencia requerida
- limites de scope
- respuesta ante fallos o gates

## 7. Model routing

`model_routing` pertenece a `config.json`, no a `AGENTS.md`.

Campos relevantes:

- `tier_default`
- `tier_overrides`
- `fallback_chain`
- `budget`
- `diversity`

Reglas:

1. El LLM **NO DEBE** auto-seleccionar su modelo.
2. El runtime **DEBE** aplicar el routing fuera del agente.
3. `AGENTS.md` **NO DEBE** contener nombres de modelos ni logica de tier.
4. El catalogo concreto de modelos **DEBERIA** vivir en un artefacto operativo separado, no en esta spec.

## 8. Fallback chains y budget

### 8.1 Fallback chains

1. Toda fallback chain **DEBE** declararse en `config.json`.
2. Fallback **PUEDE** degradar calidad, pero **NO DEBE** cambiar la estructura del agente.
3. Toda degradacion **DEBERIA** dejar observabilidad suficiente.

### 8.2 Budget enforcement

1. Budget **DEBE** aplicarse server-side.
2. Si hay fallback disponible, el runtime **DEBERIA** degradar graceful antes de abortar.
3. Si la politica explicita `degrade_on_limit = false`, el runtime **DEBE** abortar al agotar budget.

Traces to: formal/01 §1.3 (Effect Monad M)

## 10. Invariantes

1. Un cambio de plataforma o modelo **NO DEBE** alterar FSM, tools declaradas ni constraints.
2. Las fuentes del workspace **NO DEBEN** modificarse durante la generacion de wrappers.
3. `config.json` **NO DEBE** inyectarse como texto al LLM; su enforcement es server-side.
4. Los Skills **NO DEBEN** bootstrappearse completos; lazy-load **DEBE** preservarse.

## 11. Validacion

| Check                    | Criterio                                                   | Enforcement | Accion si falla          |
| ------------------------ | ---------------------------------------------------------- | ----------- | ------------------------ |
| Preservacion estructural | Los 5 componentes siguen materializados                    | runtime     | Corregir adapter         |
| Security server-side     | `config.json` no se delega al LLM                          | runtime     | Mover enforcement        |
| Frontmatter stripped     | El wrapper no inyecta YAML al LLM                          | lint        | Corregir pipeline        |
| Lazy-load preservado     | Skills no se bootstrappean completos                       | runtime     | Corregir adapter         |
| Tool mapping completo    | Toda tool declarada tiene mapping o limitacion documentada | runtime     | Completar mapping        |
| Routing segregado        | Tier, fallback y budget viven en `config.json`             | lint        | Reubicar config          |
| Equivalencia minima      | Inputs representativos no divergen funcionalmente          | eval        | Ajustar adapter o gating |
| Wrapper inmutable        | La fuente del workspace no se modifica                     | lint        | Regenerar wrapper        |

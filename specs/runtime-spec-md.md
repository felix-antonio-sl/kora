---
_manifest:
  urn: "urn:kora:kb:runtime-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 01, 02, 04, 07, repair of cross-platform adapter contract"
version: "3.6.0"
status: published
tags: [spec, runtime, deployment, adapters, wrappers, fallback]
lang: es
extensions: {}
---

# KORA/Runtime-Spec v3.6.0

## 1. Definicion

Esta especificacion gobierna la adaptacion de un workspace KORA a un runtime concreto sin alterar la semantica del agente.

`runtime-spec` no redefine al agente. Gobierna transporte, inyeccion, enforcement y equivalencia comportamental entre plataformas. La equivalencia es funcional, no textual: mismo input **DEBE** producir misma decision de routing, mismas tools invocadas y mismas constraints aplicadas; el texto de salida **PUEDE** diferir.

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
| Source Skill Bundle    | Skill extendido fuente materializado como `skills/CM-*/SKILL.md` y fibras adjuntas |
| Activation Projection  | Proyeccion `Forget(SKILL)` que expone solo el `CM Core` en tiempo de activacion |
| Behavioral Equivalence | Equivalencia funcional del mismo agente entre plataformas: mismo routing, mismas tools, mismas constraints |
| Fallback Chain         | Cadena ordenada de modelos alternativos                              |
| Budget Enforcement     | Politica server-side de costo o tokens                               |
| Platform Config Projection | Proyeccion estructurada de `config.json` hacia la config nativa del runtime |
| Managed Install Plan   | Declaracion estructurada de Skills, plugins o bundles que el runtime debe instalar por vias nativas |
| Runtime State          | Credenciales, sesiones, pairing stores, caches, volumes y otros artefactos operativos mutables del runtime |
| Transmutation Contract | Contrato estructurado emitido junto al wrapper para que configure y despliegue sin reinterpretacion textual del workspace |

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
| `skills/`             | Se activa via lazy-load, preservando tanto `CM-*.md` como `SKILL.md` extendidos |

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
4. Si la plataforma ofrece una superficie nativa y estructurada para config, policy, instalaciones gestionadas o bindings, el adapter **DEBE** preferir esa superficie a emulaciones textuales dentro del workspace.
5. La semantica critica de deploy, config o enforcement **NO DEBE** quedar delegada a bootstrap textual si el runtime permite expresarla estructuradamente.
6. La ausencia de equivalencia perfecta **NO DEBE** usarse para justificar drift estructural.

## 5. Wrapper generation

Los wrappers son artefactos derivados. Las fuentes del workspace **NO DEBEN** modificarse durante la generacion.

### 5.1 Reglas de generacion

1. El wrapper **DEBE** generarse fuera del workspace fuente.
2. El wrapper **DEBE** eliminar frontmatter antes de la inyeccion.
3. El wrapper **DEBE** respetar la segregacion original de componentes.
4. El wrapper **DEBERIA** declarar claramente la plataforma target.

### 5.2 Source Skill vs Wrapper

Reglas:

1. `skills/CM-*/SKILL.md` es un artefacto fuente del workspace; **NO** es un wrapper.
2. Un wrapper `SKILL.md` generado para una plataforma **DEBE** vivir fuera del workspace fuente.
3. La coincidencia de nombre `SKILL.md` entre fuente y wrapper **NO DEBE** usarse para colapsar ambas superficies.

### 5.3 Discover, Activate, Execute

El ciclo Discover/Activate/Execute para Skills extendidos se gobierna por `skill-spec-md §5`. El runtime **DEBE** preservar las tres fases y sus reglas.

Reglas adicionales de runtime:

1. Todo adapter **DEBE** documentar si opera en modo `Activate` (solo `CM Core`) o en modo `Execute` (bundle completo).
2. La ausencia de bundle completo **NO DEBE** alterar el comportamiento del `CM Core` ya activado.

## 6. Platform equivalence

La equivalencia cross-platform no exige bisimulacion textual estricta. Exige preservacion funcional de comportamiento e interfaz.

Traces to: formal/01 §5.2 (Bisimulation as Substitutability) ; formal/07 §4.2 (Compositional Preservation)

### 6.1 Invariantes de equivalencia

1. Mismo input -> output funcionalmente equivalente.
2. Mismas tools declaradas -> misma interfaz efectiva.
3. Mismas constraints -> misma fuerza de enforcement.
4. Mismo wiring y misma disponibilidad de Skills.
5. Misma proyeccion de activacion para todo Skill extendido activado.

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
3. Toda degradacion **DEBERIA** dejar observabilidad suficiente: como minimo, registro del tier usado, razon de la degradacion y budget restante.

### 8.2 Budget enforcement

1. Budget **DEBE** aplicarse server-side.
2. Si hay fallback disponible, el runtime **DEBERIA** degradar graceful antes de abortar.
3. Si la politica explicita `degrade_on_limit = false`, el runtime **DEBE** abortar al agotar budget.

Traces to: formal/01 §1.3 (Effect Monad M)

## 9. Transmutacion

La transmutacion es la materializacion de un workspace KORA en un runtime concreto preservando la semantica del agente.

### 9.1 Pipeline canonico

Todo proceso de transmutacion **DEBE** ejecutar esta secuencia:

1. Strip frontmatter YAML de todos los `.md` del workspace.
2. Excluir `config.json` del workspace target.
3. Generar artefactos requeridos por la plataforma (e.g., `IDENTITY.md`) derivandolos de componentes KORA existentes.
4. Copiar componentes de bootstrap al workspace target.
5. Verificar con toolchain de plataforma antes de deploy.

### 9.2 Reglas de exclusion

1. `config.json` **DEBE** excluirse del workspace target. Su informacion informa la config de plataforma pero **NO** se copia.
2. Frontmatter YAML **DEBE** strippearse de todos los archivos copiados.
3. Bloques `_manifest` **DEBEN** removerse antes de inyeccion al runtime.

### 9.3 Reglas de generacion

1. Para plataformas que requieren identidad publica (e.g., `IDENTITY.md` en OpenClaw), el proceso **DEBE** generar el artefacto derivando nombre y descripcion de `SOUL.md`. Este artefacto vive en el workspace target, **NO** en el workspace fuente KORA.
2. La config de plataforma (e.g., `openclaw.json`) **DEBE** configurarse informada por `config.json` pero **NO DEBE** ser copia mecanica.

### 9.4 Contrato estructurado de transmutacion

1. Toda transmutacion destinada a configuracion o deploy posterior **DEBE** emitir un `Transmutation Contract` autosuficiente junto al wrapper.
2. El contrato **DEBE** separar al menos:
   - workspace target
   - `Platform Config Projection`
   - `Managed Install Plan`
   - hints y restricciones de topologia/deploy
3. El paso de configuracion o deploy posterior **NO DEBE** depender de reinterpretar `TOOLS.md`, `SOUL.md` u otro bootstrap textual para datos criticos que ya sean expresables estructuradamente.
4. El adapter **NO DEBE** colapsar dentro del workspace target informacion que pertenece a config nativa, instalaciones gestionadas o estado operativo.

### 9.5 Estado operativo excluido

1. `Runtime State` **NO DEBE** formar parte del wrapper ni del `Transmutation Contract` salvo como referencia abstracta a prerequisitos.
2. Credenciales, `auth-profiles.json`, sesiones, pairing stores, caches, volumes y otros artefactos mutables **DEBEN** resolverse en runtime por vias nativas de plataforma.
3. Un pipeline de transmutacion **NO DEBE** promover estado operativo mutable a fuente normativa.

### 9.6 Limites de bootstrap

Todo runtime **PUEDE** imponer limites de tamaño al bootstrap inyectado. Cuando la plataforma declare limites, el proceso de transmutacion **DEBERIA** verificar que los componentes no excedan esos limites. Si exceden, los componentes **DEBERIAN** compactarse o particionarse en skills lazy-load.

### 9.7 Runtime drift

El workspace runtime opera como extension gobernada del workspace canonico (repo KORA). Se aplica el principio de extensiones (`gobernanza §6`):

1. **PUEDE** agregar: reglas, checks, skills, memory, conocimiento.
2. **NO PUEDE** relajar: eliminar reglas, debilitar restricciones, saltarse checks existentes.
3. **NO PUEDE** mutar identidad: `AGENTS.md` (FSM, reglas duras, co-induccion, contexto multi-turno y wiring), `SOUL.md` y `TOOLS.md` son contrato identitario del agente — modificarlos requiere backport al repo y re-auditoria.

Tipos de drift y su gestion:

| Tipo                    | Ejemplo                                 | Clasificacion       | Accion                  |
| ----------------------- | --------------------------------------- | ------------------- | ----------------------- |
| State legitimo          | `memory/`, `MEMORY.md`, `HEARTBEAT.md`  | Normal              | Sin accion              |
| Extension aditiva       | Regla dura nueva, check co-induccion    | Extension §6        | Evaluar backport        |
| Skill emergente         | Nuevo `CM-*.md` en `skills/`            | Extension §6        | Backport si pasa purity |
| Violacion sustractiva   | Regla eliminada, check removido         | Prohibido           | Corregir en runtime     |
| Mutacion identitaria    | FSM modificada, `SOUL.md` reescrito     | Prohibido           | Revertir o backportear via repo |

### 9.7.1 Reconciliacion

Periodicamente, el operador **DEBE** ejecutar reconciliacion:

1. Detectar drift: `diff` entre workspace repo (stripped) y workspace runtime.
2. Clasificar cada diferencia segun la tabla anterior.
3. Backportear extensiones valiosas al repo KORA.
4. Auditar backport (`gobernanza §10`).
5. Corregir violaciones en runtime.

Un re-deploy **NO DEBE** copiar el workspace del repo sobre el workspace desplegado sin ejecutar `diff` previo. El drift detectado **DEBE** evaluarse antes de descartarse.

### 9.7.2 Source of truth

El repo KORA es fuente de verdad normativa. El workspace runtime es fuente de verdad operativa. Cuando divergen, la normativa prevalece — pero la operativa puede alimentar la normativa a traves de la reconciliacion.

### 9.8 Verificacion

1. Pre-deploy: `kora validate --profile strict` + toolchain de plataforma (e.g., `openclaw doctor`).
2. Post-deploy: verificar cadena e2e.
3. El toolchain de plataforma **DEBE** ejecutarse antes de declarar deploy exitoso.

### 9.7 Tabla de mapping (referencia)

| KORA          | Workspace target                       | Notas                          |
| ------------- | -------------------------------------- | ------------------------------ |
| `AGENTS.md`   | `AGENTS.md` (stripped)                 | Sin frontmatter                |
| `SOUL.md`     | `SOUL.md` (stripped)                   | Sin frontmatter                |
| `USER.md`     | `USER.md` (stripped)                   | Sin frontmatter                |
| `TOOLS.md`    | `TOOLS.md` (stripped)                  | Sin frontmatter                |
| `skills/`     | `skills/` (stripped)                   | Sin frontmatter en cada CM     |
| `config.json` | **EXCLUIDO**                           | Informa config plataforma      |
| —             | `IDENTITY.md` (si plataforma requiere) | Derivado de `SOUL.md`          |

## 10. Invariantes

1. Un cambio de plataforma o modelo **NO DEBE** alterar FSM, tools declaradas ni constraints.
2. Las fuentes del workspace **NO DEBEN** modificarse durante la generacion de wrappers.
3. `config.json` **NO DEBE** inyectarse como texto al LLM; su enforcement es server-side.
4. Los Skills **NO DEBEN** bootstrappearse completos; lazy-load **DEBE** preservarse.
5. La activacion de un Skill extendido **DEBE** factorizar por `Forget(SKILL)` antes de cualquier montaje de bundle.

## 11. Validacion

| Check                    | Criterio                                                   | Enforcement | Accion si falla          |
| ------------------------ | ---------------------------------------------------------- | ----------- | ------------------------ |
| Preservacion estructural | Los 5 componentes siguen materializados                    | runtime     | Corregir adapter         |
| Security server-side     | `config.json` no se delega al LLM                          | runtime     | Mover enforcement        |
| Frontmatter stripped     | El wrapper no inyecta YAML al LLM                          | lint        | Corregir pipeline        |
| Lazy-load preservado     | Skills no se bootstrappean completos                       | runtime     | Corregir adapter         |
| Tool mapping completo    | Toda tool declarada tiene mapping o limitacion documentada | runtime     | Completar mapping        |
| Source/wrapper segregado | `skills/CM-*/SKILL.md` fuente no se confunde con wrapper   | lint        | Corregir pipeline        |
| Activacion por Forget    | Un Skill extendido se activa via `CM Core` antes del bundle| runtime     | Corregir adapter         |
| Routing segregado        | Tier, fallback y budget viven en `config.json`             | lint        | Reubicar config          |
| Native-first             | Config y enforcement usan superficies nativas cuando existen | runtime   | Corregir adapter         |
| Contrato estructurado    | El wrapper incluye contrato autosuficiente para config/deploy | manual   | Completar contract       |
| Estado operativo excluido | Credenciales, sesiones y caches quedan fuera del wrapper  | lint        | Excluir estado mutable   |
| Equivalencia minima      | Inputs representativos no divergen funcionalmente          | eval        | Ajustar adapter o gating |
| Wrapper inmutable        | La fuente del workspace no se modifica                     | lint        | Regenerar wrapper        |
| config.json excluido     | `config.json` no esta presente en workspace target         | lint        | Excluir del pipeline     |
| Drift pre-redeploy       | Re-deploy ejecuta diff antes de sobreescribir              | manual      | Ejecutar diff y evaluar  |
| Transmutacion verificada | Pipeline §9 completado antes de deploy                     | manual      | Completar pipeline       |

## 12. Migracion

Esta seccion se establece a partir de v3.5.0. Los breaking changes de major bumps anteriores no fueron documentados en seccion dedicada.

### Contrato vigente v3

- Core agnostico: 5 componentes preservados, security server-side, lazy-load (§3).
- Adapters por plataforma: Claude, GPT, Gemini, OpenClaw (§4).
- Wrappers derivados fuera del workspace fuente (§5).
- D/A/E gobernado por `skill-spec-md §5` con reglas adicionales de runtime (§5.3).
- Equivalencia funcional cross-platform, no bisimulacion textual (§6).
- Model routing y fallback en `config.json`, no en `AGENTS.md` (§7, §8).
- Transmutacion con pipeline canonico: strip, excluir config, generar, copiar, verificar (§9).
- Contrato estructurado obligatorio para config/deploy y estado operativo excluido (§9.4, §9.5).
- Runtime drift gobernado: agregar si, relajar no, mutar identidad no (§9.7).
- Contrato identitario: `AGENTS.md`, `SOUL.md`, `TOOLS.md` completos (§9.7).

Toda futura transicion major **DEBE** documentar aqui: (1) que cambio, (2) que migrar, y (3) que se depreca.

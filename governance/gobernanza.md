---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "refactor modern-first: AGENT.md canonico, capacidades portables, legacy como compatibilidad; v4.1 formaliza regimenes URN en §4.3; v4.2 canoniza ontologia PMI × LFS en harness-spec y redefine agentfile/skill-overlay como serializaciones; v4.3 unifica autoria en autoria-spec, retira agentfile-spec y skill-overlay-spec, reduce regimenes URN a dos, limpia residuos pre-unificacion; v4.4 incorpora procesos-spec, risk-register-spec, multiagente-spec y mastra-runtime-extension en la topologia v5"
version: "4.4.0"
status: publicado
tags: [gobernanza, constitucion, precedencia, identidad, enforcement]
lang: es
extensions:
  kora:
    family: spec
relations:
  cites:
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:autoria-spec"
---

# KORA/Gobernanza v4.4.0

## 1. Definicion

Esta es la constitucion operativa de KORA. Su objetivo es mantener un sistema
pequeño, moderno y composable. La gobernanza no intenta describir todos los
artefactos: fija el canon, define precedencia, decide identidad y disciplina el
uso de extensiones.

Principio rector:

> KORA es **vector ontologico PMI × LFS** (`harness-spec`) + **shape unificado de autoria** (`autoria-spec`) + **transmutacion funtorial** (`transmutation-spec`).

Desde v4.3, el ecosistema no acepta shapes anteriores: agentes y habilidades se escriben con la misma serializacion, discriminada por `atlas.forma_material`.

### 1.1 Canon de diseno

KORA **DEBE** operar con estas prioridades:

1. una sola fuente de verdad por objeto,
2. semantica concentrada en el IR canonico (vector PMI × LFS),
3. shape unificado de autoria para todo artefacto agentico productivo,
4. runtime y outputs siempre derivados.

Corolarios:

1. El vector ontologico `harness_vector` es el centro del sistema.
2. `autoria-spec` es la unica serializacion de autoria productiva (cuatro formas materiales: habilidad, subagente, agente-propiamente-tal, agente-plataforma).
3. Los outputs de transmutacion (`_BUILD/` por workspace) y los archivos runtime son derivados regenerables.
4. Specs anteriores (`agentfile-spec`, `skill-overlay-spec`, bundles `CM-*`, workspace legacy de 5-6 archivos) estan **retiradas**; se migran en una sola pasada (§10).

## 2. Definiciones

| Termino | Definicion |
|---------|------------|
| Canon | Conjunto de reglas normativas que KORA impone sin excepcion. |
| Capa | Nivel categorico de la arquitectura KORA: ontologia, serializacion, runtime, distribucion (§3.1). |
| Regimen URN | Gramatica de identidad para un tipo de artefacto (§4.3). |
| Fuente primaria | Archivo autoritativo que define un objeto KORA (§4). |
| Derivado | Artefacto regenerable desde su fuente primaria via funtor declarado (ej. transmutacion). |
| Mirror | Copia de una fuente primaria bajo una serializacion alternativa; subordinada y regenerable. |
| Extension de namespace | Spec que estrecha el canon para un ecosistema concreto sin relajarlo (§6). |
| Lifecycle | Maquina de estados de un artefacto (§5). |
| Kind estructural | Valor de `_manifest.type`; enum cerrado (§4.2). |
| Enforcement | Nivel de verificacion mecanica de una regla (§7). |

## 3. Taxonomia de specs y precedencia

Cuando dos reglas parezcan contradecirse, prevalece esta jerarquia:

1. `gobernanza.md` — constitucion.
2. specs ontologicas (`harness-spec.md`, `qa-spec.md`).
3. `md-spec.md` — formato base KORA/MD y perfil prescriptivo de specs.
4. specs canonicas de serializacion (`autoria-spec`, `knowledge-spec`) y de runtime (`runtime-spec-md`, `transmutation-spec`, runtime-extensions).
5. extensiones de namespace.
6. README, plantillas, artefactos generados.

Esta jerarquia se desarrolla en cuatro **capas categoricas** (§3.1) y una **regla de especializacion** (§3.4).

### 3.1 Separacion ontologia / serializacion / runtime / distribucion

v4.2 formaliza que KORA opera en **cuatro capas** categoricamente distintas:

| Capa | Qué gobierna | Specs |
|------|--------------|-------|
| **Ontologia** | Que *es* un artefacto agentico, como se interpreta su calidad y como componen sus procesos | `harness-spec`, `qa-spec`, `procesos-spec`, `risk-register-spec` |
| **Serializacion** | Como se *escribe* el artefacto (shape unificado de authoring) | `autoria-spec`, `md-spec`, `knowledge-spec` |
| **Runtime** | Como se *ejecuta* en un target concreto y como compone multiagente | `runtime-spec-md`, `multiagente-spec`, `transmutation-spec`, runtime-extensions |
| **Distribucion** | Como se *empaqueta y comparte* | `plugin.json`, `marketplace.json` (externas) |

**Principio**: KORA IR canoniza **ontologia** (PMI × LFS). Las
serializaciones son *proyecciones* de authoring. Los runtimes son *fibras
proyectadas*. La distribucion es *meta-encaje*.

### 3.2 Specs canonicas por capa

**Capa ontologica**:

- `harness-spec.md` — **constitucion ontologica** (espacio PMI × LFS).
- `qa-spec.md` — semantica enriquecida de quality attributes y `qa_budget`.
- `procesos-spec.md` — procesos del toolchain como funtores declarados.
- `risk-register-spec.md` — registro de riesgo como composicion Kleisli.

**Capa de serializacion**:

- `autoria-spec.md` — shape unificado de authoring para todo artefacto agentico productivo (cuatro formas materiales: habilidad, subagente, agente-propiamente-tal, agente-plataforma).
- `md-spec.md` — formato KORA/MD base usado por el frontmatter + body.
- `knowledge-spec.md` — tejido relacional y pipeline de conocimiento.

**Capa de runtime**:

- `runtime-spec-md.md` — contrato generico.
- `multiagente-spec.md` — ley de coreografia multiagente y handoffs.
- `transmutation-spec.md` — leyes functoriales de proyeccion IR → runtime.
- `claude-code-runtime-extension.md`, `codex-runtime-extension.md`, `gemini-runtime-extension.md`, `openclaw-runtime-extension.md`, `mastra-runtime-extension.md` — proyecciones a runtimes concretos.

### 3.3 Ruptura con formatos anteriores

Las specs `agentfile-spec` y `skill-overlay-spec` (v2.0.0) fueron
**retiradas** y absorbidas por `autoria-spec`. No hay coexistencia
transitoria: artefactos pre-existentes se migran en una sola pasada
(`kora migrate --perfil a-autoria`) y el toolchain rechaza shapes
anteriores.

### 3.4 Regla de especializacion

Entre specs del mismo nivel prevalece la más especifica para el objeto que
gobierna:

- `harness-spec` para vector ontologico PMI × LFS.
- `qa-spec` para quality attributes, floors derivados de `Σ` y `qa_budget`.
- `md-spec` para envelope KORA/MD y perfil prescriptivo de specs.
- `autoria-spec` para shape de todo artefacto agentico productivo.
- `knowledge-spec` para tejido relacional y pipeline de conocimiento.
- `transmutation-spec` para leyes de proyeccion IR → runtime.
- `multiagente-spec` para coherencia de protocolos distribuidos y handoffs.
- `runtime-spec-md` + extensions para encaje en runtime concreto.

## 4. Identidad y fuente de verdad

Todo objeto KORA **DEBE** tener una fuente primaria:

- artefacto agentico productivo: `AGENT.md` (cuando `forma_material ∈ {subagente, agente-propiamente-tal, agente-plataforma}`) o `SKILL.md` (cuando `forma_material = habilidad`), conforme a `autoria-spec`.
- artefacto de conocimiento: archivo KORA/MD conforme a `md-spec` + `knowledge-spec`.
- spec: archivo bajo `governance/`, `ontology/`, `serialization/` o `runtime/`
  conforme a `md-spec` perfil `spec`.
- output target: artefacto derivado en `{workspace}/_BUILD/{target}/`, regenerable desde la fuente primaria.

### 4.1 Regla de mirrors y outputs derivados

Un artefacto derivado (output de transmutacion, cache, vista materializada) **PUEDE** existir solo si:

1. la fuente primaria está clara,
2. el derivado no contradice la primaria,
3. el derivado puede regenerarse desde la primaria sin perdida declarada mas alla de la prevista por `transmutation-spec`.

Los outputs derivados **NO DEBEN** tratarse como autoridad: si divergen, prevalece la fuente primaria y el derivado se regenera.

### 4.2 Manifest kind

`_manifest.type` expresa el kind estructural del componente. Los kinds
reservados son:

- `artefacto` — artefacto agentico productivo (conforme a `autoria-spec`).
- `runtime_extension` — extension de runtime.
- `transmutation_record` — registro de transmutacion.

### 4.3 Regimenes de URN

KORA distingue **dos regimenes** de identidad URN:

| Regimen | Patron | Version | Uso |
| ------- | ------ | ------- | --- |
| Conceptual | `urn:{ns}:kb:{id}` | campo `version` fuera del URN | artefactos KORA/MD (knowledge, specs, meta) |
| Artefacto agentico | `urn:{ns}:artefacto:{id}` | campo `version` fuera del URN | todo artefacto conforme a `autoria-spec` (habilidad, subagente, agente-propiamente-tal, agente-plataforma) |

Reglas:

1. Ambos regimenes llevan la version **fuera** del URN, en el campo `version` del frontmatter.
2. Referencias en `relations`, `depends`, `cites` o body **DEBEN** usar la forma sin version; la resolucion de version es responsabilidad del catalogo y del runtime.
3. Un mismo componente **NO DEBE** declarar URN en dos regimenes simultaneamente; la migracion entre regimenes obliga a emitir un `supersedes` explicito.
4. Los regimenes anteriores (`urn:{ns}:agent:{id}`, `urn:{ns}:skill:{id}:{version}`, y ejecutable legacy con version embebida) estan **retirados**. Artefactos que los usaban se migran en una sola pasada.

## 5. Lifecycle y deprecacion

KORA distingue:

- artefactos conceptuales: `borrador -> publicado -> deprecado`
- artefactos agenticos productivos: `borrador -> activo -> deprecado -> retirado`

Reglas:

1. Toda nueva capacidad nace conforme a `autoria-spec`.
2. Todo nuevo artefacto agentico declara `forma_material` y `arnes_categorico`.
3. No se acepta nuevo shape anterior a `autoria-spec`.
4. Transiciones inversas del lifecycle son invalidas; retirados no son reactivables (emitir uno nuevo con `supersedes`).

### 5.1 Lifecycle a escala: olas

Una **ola** es una sub-categoria del pipeline de promocion que agrupa
artefactos que se canonizan juntos. Formalmente, una ola es un objeto del
functor de lifecycle:

```
Ola_k : Staging -> Productivo
```

Cada ola declara:

- **perimetro**: conjunto de URNs candidatos a promover.
- **invariante de cierre**: que condiciones debe satisfacer un artefacto
  para cerrar la ola (ej. `kora check --strict` verde, tests verdes,
  shape de autoria-spec vigente).
- **deuda residual**: lo que queda fuera del perimetro y debe absorber
  la ola siguiente.

El functor de transicion `Ola_k -> Ola_{k+1}` tiene como dominio la
deuda residual declarada de la ola anterior: cada ola comienza con el
objeto que la anterior no pudo comprimir.

#### Registro de olas

| Ola | Estado | Perimetro | Deuda residual |
|-----|--------|-----------|-----------------|
| ola-1 | cerrada (2026-04-18) | 7 workspaces meta-kora/dev + toolchain a-autoria + atomize acceptance gate | fidelidad-agentskills; coalgebra-conformance; multiagente; 21 agentes INBOX; 7 skills INBOX |
| ola-2 | cerrada (2026-04-19) | fidelidad-agentskills + coalgebra-conformance + batch-promote + dedup staging + H6/H5/H2/H13/H23/H7 | H9, H17, H20, H22 |

Esta tabla es la vista materializada del morfismo `Ola_k -> Ola_{k+1}`;
actualizarla es parte de cerrar una ola.

## 6. Extensiones

Una extension de namespace agrega restricciones a un target o ecosistema
concreto.

Reglas:

1. Una extension **DEBE** depender de una spec base o canonica.
2. Una extension **PUEDE** estrechar reglas.
3. Una extension **NO DEBE** relajar el canon por omision.
4. La extension vive en nivel 5 de precedencia (§3 lista jerarquica) aunque resida dentro de `runtime/`, `ontology/`, `serialization/` o `governance/`.

## 7. Enforcement

Toda regla normativa cae en uno de estos niveles:

- `schema`
- `lint`
- `runtime`
- `eval`
- `manual`

Reglas:

1. Una regla sin enforcement explicito se interpreta como `manual`.
2. El repo **NO DEBE** prometer enforcement mecanico inexistente.
3. El canon **NO DEBE** degradarse para acomodar tooling atrasado.

## 8. Invariantes

Los invariantes constitucionales son:

1. El vector ontologico PMI × LFS (`harness-spec`) es la fuente de verdad de todo artefacto agentico.
2. `autoria-spec` es la unica serializacion productiva: habilidades, subagentes, agentes y agentes de plataforma comparten envelope y se discriminan por `atlas.forma_material`.
3. `md-spec` es el formato base de todo artefacto KORA/MD y define el perfil prescriptivo de las specs.
4. Runtime y output siempre son derivados; se regeneran desde la fuente primaria.
5. Ninguna capa inferior recentraliza el sistema sobre la ontologia.
6. No hay regimen URN con version embebida. Solo dos regimenes: conceptual (`urn:{ns}:kb:{id}`) y artefacto agentico (`urn:{ns}:artefacto:{id}`).

## 9. Validacion

Checks minimos:

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Canon claro | Cada objeto tiene fuente primaria | lint/manual |
| Legacy acotado | No se expande lo legacy como camino por defecto | manual |
| Mirror limpio | Los mirrors no contradicen la fuente primaria | lint/manual |
| Extension monotona | Las extensiones no relajan el canon | manual |
| Kind valido | `_manifest.type` usa taxonomia reservada | lint |

## 10. Migracion

Contrato vigente v4.4:

- KORA unifica authoring en `autoria-spec`.
- `agentfile-spec` y `skill-overlay-spec` fueron retiradas — absorbidas por `autoria-spec`.
- Migracion forzada en una sola pasada: `kora migrate --perfil a-autoria`.
- El toolchain rechaza shapes anteriores tras la migracion.

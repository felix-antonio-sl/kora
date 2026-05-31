---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "refactor modern-first: AGENT.md canonico y capacidades portables; v4.1 formaliza regimenes URN en §4.3; v4.2 canoniza ontologia PMI × LFS en harness-spec; v4.3 unifica autoria en autoria-spec y retira specs anteriores; v4.4 incorpora procesos-spec, risk-register-spec, multiagente-spec y mastra-runtime-extension en la topologia v5; v4.6 registra agent-skill-construction-spec como metodologia KORA-native de construccion pre-transmutacion; v4.7 incorpora host-roles como extension operacional; v5.0 simplificacion KORA v6 Fase 1: absorbe host-roles v1.1 como §12 expandido, reconoce canario-spec y procesos-spec como deprecadas; v6.0 KORA esencial v7 (HITL 2026-05-20): activa hermes como runtime canonico, baja freeze parcial (autoria-spec y transmutation-spec quedan editables; harness-spec sigue en freeze), runtimes canonicos reducidos a {claude-code, codex, openclaw, hermes}; v6.1 (HITL 2026-05-31) explicita en §1 el proposito de KORA (repositorio, catalogo, produccion y mantenimiento de artefactos) y los tres tipos de artefacto (conocimiento, agentes, skills), subordinando la ecuacion categorial a garantia formal: conocimiento es tipo especifico de artefacto (no paraguas) y las specs no son artefactos"
version: "6.1.0"
status: publicado
tags: [gobernanza, constitucion, precedencia, identidad, enforcement, host-roles, hermes, runtimes]
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
  supersedes:
    - "urn:kora:kb:host-roles"
---

# KORA/Gobernanza v6.1.0

## 1. Definicion

Esta es la constitucion operativa de KORA. Su objetivo es mantener un sistema
pequeño, moderno y composable. La gobernanza no intenta describir todos los
artefactos: fija el canon, define precedencia, decide identidad y disciplina el
uso de extensiones.

**Que es KORA y para que sirve.** KORA es el repositorio, catalogo y sistema de
produccion y mantenimiento de los artefactos que consumen o ejecutan sistemas
LLM. No es una aplicacion tradicional: produce esos artefactos por un pipeline
gobernado, los cataloga y resuelve por URN, los mantiene coherentes en el
tiempo (checks, lifecycle, deprecacion) y proyecta los ejecutables a runtimes.
La fuente de verdad es el filesystem con manifests validos; `docs/generated/`
es derivado.

KORA gestiona **tres tipos de artefacto, y solo tres**:

1. **conocimiento** — archivos `.md` en estandar KORA/MD (`md-spec` +
   `knowledge-spec`), hechos para **consumo** de sistemas LLM como contexto: se
   leen, no se ejecutan.
2. **agentes** — `AGENT.md` conforme a `autoria-spec`: definen actores.
3. **skills** — `SKILL.md` conforme a `autoria-spec`: definen capacidades.

Agentes y skills se **proyectan a runtimes** (`claude-code`, `codex`,
`openclaw`, `hermes`) via transmutacion; el conocimiento no se proyecta, se
consume. Las **specs** (`governance/`, `ontology/`, `serialization/`,
`runtime/`) **no son artefactos**: son la ley que define que cuenta como
artefacto valido. La **toolchain** los produce, valida, resuelve y mantiene. El
termino "conocimiento" designa solo el tipo 1; nunca es paraguas de los otros
dos.

Principio rector (garantia formal de lo anterior):

> KORA es **vector ontologico PMI × LFS** (`harness-spec`) + **shape unificado de autoria** (`autoria-spec`) + **transmutacion funtorial** (`transmutation-spec`).

Desde v4.3, el ecosistema no acepta shapes anteriores: agentes y habilidades se escriben con la misma serializacion, discriminada por `atlas.forma_material`.

### 1.1 Canon de diseno

KORA **DEBE** operar con estas prioridades:

1. una sola fuente de verdad por objeto,
2. semantica concentrada en el IR canonico (vector PMI × LFS),
3. shape unificado de autoria para todo artefacto agentico productivo,
4. runtime y outputs siempre derivados.

Corolarios:

1. El vector ontologico `vector_ontologico` es el centro del sistema.
2. `autoria-spec` es la unica serializacion de autoria productiva (cuatro formas materiales: habilidad, subagente, agente-propiamente-tal, agente-plataforma).
3. Los outputs de transmutacion (`_BUILD/` por workspace) y los archivos runtime son derivados regenerables.
4. Specs y shapes anteriores estan **retirados**; se migran en una sola pasada (§11).

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
3. `md-spec.md` — formato base KORA/MD regimen descriptivo.
   `spec-md.md` — perfil prescriptivo (RFC 2119, Traces to, invariantes
   prescriptivos) que extiende md-spec para documentos de familia `spec`.
4. specs canonicas de serializacion (`autoria-spec`, `knowledge-spec`) y de runtime (`runtime-spec-md`, `transmutation-spec`, runtime-extensions).
5. extensiones de namespace.
6. README, plantillas, artefactos generados.

Esta jerarquia se desarrolla en cuatro **capas categoricas** (§3.1) y una **regla de especializacion** (§3.4).

### 3.1 Separacion ontologia / serializacion / runtime / distribucion

v4.2 formaliza que KORA opera en **cuatro capas** categoricamente distintas:

| Capa | Qué gobierna | Specs |
|------|--------------|-------|
| **Ontologia** | Que *es* un artefacto agentico, como se interpreta su calidad y como componen sus procesos | `harness-spec`, `qa-spec`, `procesos-spec`, `risk-register-spec` |
| **Serializacion** | Como se *escribe* el artefacto y como se construye su fuente primaria | `autoria-spec`, `md-spec`, `spec-md`, `knowledge-spec` |
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
- `md-spec.md` — formato KORA/MD base (regimen descriptivo).
- `spec-md.md` — perfil prescriptivo: RFC 2119, Traces to, cristalizacion,
  invariantes prescriptivos. Extiende `md-spec` para familia `spec`.
- `knowledge-spec.md` — tejido relacional y pipeline de conocimiento.

**Capa de runtime**:

- `runtime-spec-md.md` — contrato generico.
- `multiagente-spec.md` — ley de coreografia multiagente y handoffs.
- `transmutation-spec.md` — leyes functoriales de proyeccion IR → runtime.
- `claude-code-runtime-extension.md`, `codex-runtime-extension.md`, `gemini-runtime-extension.md`, `openclaw-runtime-extension.md`, `mastra-runtime-extension.md`, `opencode-runtime-extension.md` — proyecciones a runtimes concretos.

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
- `md-spec` para envelope KORA/MD descriptivo.
- `spec-md` para perfil prescriptivo (extiende md-spec para familia `spec`).
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
4. Los regimenes anteriores (`urn:{ns}:agent:{id}`, `urn:{ns}:skill:{id}:{version}`, y ejecutable con version embebida) estan **retirados**. Artefactos que los usaban se migran en una sola pasada.

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

## 8. Decisiones HITL vigentes

### 8.1 `_perfiles` no es regimen formal

`_perfiles` **NO** constituye una categoria ontologica canonica ni una forma
material valida de `autoria-spec`.

Reglas:

1. Todo material de perfiles vive como draft de referencia bajo
   `artifacts/agents/_FRAGUA/INBOX/perfiles/`.
2. Ese material queda fuera de productivo, fuera de transmutacion y fuera de
   cualquier promesa de shape canonico.
3. Si un perfil debe volverse agente o skill real, se absorbe a una forma
   material valida conforme a `autoria-spec`; no se eleva `_perfiles` como
   regimen propio.

### 8.2 Hermes es runtime canonico (desde 2026-05-20)

`Hermes` **ES** runtime target canonico de KORA desde la decision HITL
del 2026-05-20 (`urn:kora:kb:adr-kora-v7-esencial`).

Reglas:

1. `hermes` se admite en `transmute`, matrices de preservacion y
   `entornos_objetivo`.
2. El contenido normativo completo de
   `urn:kora:kb:hermes-runtime-extension` se desarrolla en Fase 2b; el
   stub vigente declara dominio de realizabilidad inicial y deuda
   explicita.
3. Critical path de runtimes canonicos: `claude-code`, `codex`,
   `openclaw`, `hermes` (cuatro).

### 8.3 Freeze formal parcial (post 2026-05-20)

La decision HITL del 2026-05-20 (`urn:kora:kb:adr-kora-v7-esencial`)
baja parcialmente el freeze formal que vivia desde v4.7:

| Spec | Estado |
|------|--------|
| `ontology/harness-spec.md` | **en freeze** (core ontologico PMI × LFS) |
| `serialization/autoria-spec.md` | **editable** (autoriza compactacion Fase 2b) |
| `runtime/transmutation-spec.md` | **editable** (autoriza compactacion Fase 2b) |

Reglas para `harness-spec` (sigue en freeze):

1. Solo se permiten correcciones de verdad necesarias para sostener
   artefactos productivos, checks o transmutaciones en curso.
2. No se permiten expansiones doctrinales, nuevos regimenes ni nuevos
   ejes del vector durante el freeze.
3. Todo cambio se justifica como fix puntual, no como rediseño
   conceptual.

Reglas para `autoria-spec` y `transmutation-spec` (editables):

1. Compactacion autorizada en Fase 2b con criterio: reducir lineas sin
   perder invariantes vivos (verificables por checks).
2. Cambios doctrinales menores admitidos; los mayores requieren ADR
   dedicado (familia `adr`) con `refines` o `supersedes` al ADR v7.
3. Toda compactacion **DEBE** preservar URN integrity y los tests
   existentes deben seguir verdes.

### 8.4 Runtimes archivados (decisiones-archivadas/specs-en-pausa)

Los siguientes runtimes quedan **archivados** y no son target canonico
salvo nuevo HITL:

| Runtime | Archivo | URN |
|---------|---------|-----|
| `gemini` | `governance/decisiones-archivadas/specs-en-pausa/gemini-runtime-extension.md` | `urn:kora:kb:gemini-runtime-extension` |
| `mastra` | `governance/decisiones-archivadas/specs-en-pausa/mastra-runtime-extension.md` | `urn:kora:kb:mastra-runtime-extension` |
| `opencode` | `governance/decisiones-archivadas/specs-en-pausa/opencode-runtime-extension.md` | `urn:kora:kb:opencode-runtime-extension` |
| `agentskills` | `governance/decisiones-archivadas/specs-en-pausa/agentskills-runtime-extension.md` | `urn:kora:kb:agentskills-runtime-extension` |

Reglas:

1. Los URNs archivados **siguen resolviendo** en el catalogo (URN
   integrity preservada through lifecycle).
2. `entornos_objetivo` en artefactos productivos **NO DEBE** incluir
   slugs archivados; el toolchain los rechaza desde KORA v7.
3. La reactivacion de cualquier runtime archivado requiere HITL
   explicito + ADR dedicado.

## 9. Invariantes

Los invariantes constitucionales son:

1. El vector ontologico PMI × LFS (`harness-spec`) es la fuente de verdad de todo artefacto agentico.
2. `autoria-spec` es la unica serializacion productiva: habilidades, subagentes, agentes y agentes de plataforma comparten envelope y se discriminan por `atlas.forma_material`.
3. `md-spec` es el formato base de todo artefacto KORA/MD y define el perfil prescriptivo de las specs.
4. Runtime y output siempre son derivados; se regeneran desde la fuente primaria.
5. Ninguna capa inferior recentraliza el sistema sobre la ontologia.
6. No hay regimen URN con version embebida. Solo dos regimenes: conceptual (`urn:{ns}:kb:{id}`) y artefacto agentico (`urn:{ns}:artefacto:{id}`).

## 10. Validacion

Checks minimos:

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Canon claro | Cada objeto tiene fuente primaria | lint/manual |
| Formatos retirados acotados | No se expanden formatos retirados como camino por defecto | manual |
| Mirror limpio | Los mirrors no contradicen la fuente primaria | lint/manual |
| Extension monotona | Las extensiones no relajan el canon | manual |
| Kind valido | `_manifest.type` usa taxonomia reservada | lint |

## 11. Migracion

Contrato establecido en v4.6.0 y vigente bajo v4.7.x:

- KORA unifica authoring en `autoria-spec`.
- `agentfile-spec` y `skill-overlay-spec` fueron retiradas — absorbidas por `autoria-spec`.
- Migracion forzada en una sola pasada: `kora migrate --perfil a-autoria`.
- El toolchain rechaza shapes anteriores tras la migracion.

## 12. Identidad operacional por host

Esta seccion absorbe `host-roles v1.1` (deprecada en v5.0). Fija la
**identidad operacional por maquina** del corpus KORA. Distingue dos
roles: `primary` y `secondary`. Solo existe **un** host `primary`
activo por instalacion; cualquier otra maquina con un clon del
repositorio es `secondary` por defecto.

Esta doctrina NO modifica el canon ontologico ni de serializacion:
regula la operacion del filesystem como SSOT, la disciplina de push a
`origin/master`, y la forma en que el toolchain identifica al host.

### 12.1 Definiciones

| Termino | Definicion |
|---------|------------|
| Host | Maquina concreta con un clon del repositorio KORA. |
| Primary | Host autoritativo para `master`. Puede pushear directamente. Es la SSOT operacional. |
| Secondary | Host replica. Trabaja en ramas feature, no pushea a `master` directo, propone cambios via PR. |
| Marker de host | Archivo local fuera del repo (`~/.kora/host.yml`) que declara el rol del host actual. |
| Default | Si el marker no existe, el host se interpreta como `secondary`. |

### 12.2 Host primary canonico

| Campo | Valor |
|-------|-------|
| Hostname | `hetzner2897261` |
| Machine ID | `9976abf4e8f6428b9f28f26221dbcdce` |
| Sistema | Ubuntu 24.04 (Hetzner) |
| Operador | Felix (FS) |
| Declarado | 2026-05-03 |

Solo este host es `primary`. La transferencia de rol a otra maquina es
decision HITL explicita que **DEBE** registrarse como nueva version de
esta spec (§12.7).

### 12.3 Reglas de push y derivados

1. Solo el host `primary` **DEBE** pushear directamente a `origin/master`.
2. Hosts `secondary` **NO DEBEN** ejecutar `git push origin master` ni
   equivalentes; crean ramas feature y abren Pull Requests.
3. `_BUILD/`, `docs/generated/`, sesiones, secretos y runtime en
   `~/.openclaw/` son autoritativos solo en `primary`.
4. Hosts `secondary` **PUEDEN** regenerar derivados localmente
   (`kora index`, `kora sync-docs`, `kora transmute`) pero esos
   derivados no son SSOT.

### 12.4 Toolchain y verificacion

1. `python3 toolchain/kora` **DEBE** leer el marker sin fallar si esta
   ausente; ausencia = `secondary`.
2. Comandos de mutacion (`migrate`, `promote`, `deprecate`) **PUEDEN**
   verificar el rol y advertir si se ejecutan en `secondary`.
3. El hook versionado `toolchain/git-hooks/pre-push` **DEBE** bloquear
   push directo a `origin/master` si el host no es `primary` o si el
   marker es inconsistente.
4. La instalacion local del hook se realiza con
   `python3 toolchain/kora install-hooks`, que configura
   `core.hooksPath=toolchain/git-hooks`.

### 12.5 Marker de host

El rol del host se declara en un archivo local fuera del repositorio:

- Path: `~/.kora/host.yml`
- Formato: YAML
- Versionado: NO (es estado de maquina, no de corpus)
- Default si ausente: `secondary`

Shape minimo:

```yaml
role: primary | secondary
hostname: "{hostname real}"
machine_id: "{contenido de /etc/machine-id}"
declared_at: "YYYY-MM-DD"
declared_by: "{operador}"
notes: "{texto libre}"
```

Reglas:

1. El campo `role` es obligatorio.
2. `hostname` y `machine_id` deben corresponder a la maquina real al
   momento de la lectura; divergencia indica que el marker fue copiado
   entre maquinas y **DEBE** corregirse antes de operar.
3. El marker no se sincroniza entre hosts.

### 12.6 Enforcement

| Regla | Nivel |
|-------|-------|
| Default secondary si marker ausente | manual |
| Solo primary pushea a master | hook local + branch protection GitHub |
| Marker consistente con maquina real | manual |
| Derivados no autoritativos en secondary | manual |

### 12.7 Cambio de host primary

Transferir el rol `primary` a otra maquina **DEBE**:

1. Emitir nueva version de esta spec con la nueva identidad
   (`hostname`, `machine_id`, fecha, operador).
2. Actualizar `~/.kora/host.yml` en ambas maquinas.
3. Registrar la transicion como handoff bajo `docs/handoffs/`.
4. Ejecutar `python3 toolchain/kora host -v` en ambas maquinas y
   archivar la salida.
5. Reinstalar hooks con `python3 toolchain/kora install-hooks` en el
   nuevo `primary` y en los `secondary` que pushean ramas feature.

No se admite cohabitacion de dos hosts `primary` simultaneos.

### 12.8 Runbook de recuperacion si el primary no esta disponible

Si `hetzner2897261` queda inaccesible:

1. Pausar pushes directos a `master` hasta completar la promocion HITL
   de un reemplazo.
2. Elegir una maquina candidata con clon actualizado y ejecutar
   `git fetch --all --prune` seguido de `git pull --rebase origin master`.
3. Verificar estado local con `python3 toolchain/kora host -v`,
   `python3 toolchain/kora check --strict` y
   `python3 -m unittest discover -s tests`.
4. Crear o actualizar `~/.kora/host.yml` en la candidata con
   `role: primary`, `hostname` y `machine_id` reales.
5. Bajar el host anterior a `secondary` cuando vuelva.
6. Actualizar esta spec con version nueva, registrar el cambio en
   `docs/handoffs/`, regenerar indice si corresponde y pushear desde el
   nuevo primary.

### 12.9 Invariantes de §12

1. Existe **a lo mas un** host `primary` por instalacion.
2. Los hosts `secondary` no son SSOT y sus derivados no obligan al
   `primary`.
3. La identidad operacional del host es **local**: no vive dentro del
   repo versionado, vive en el filesystem de la maquina.
4. Esta seccion opera como extension de gobernanza; no altera
   precedencia constitucional.

## 13. Migracion v4.7 → v5.0 (KORA v6 Fase 1)

Cambios doctrinales en v5.0:

1. **`host-roles.md` absorbida** en esta spec como §12 (subsecciones
   12.1-12.9). El URN `urn:kora:kb:host-roles` queda como nodo
   historico con `status: deprecado` y `supersedes` desde gobernanza.
   Refs `cites` a `urn:kora:kb:host-roles` siguen resolviendo y son
   validas; quien edite por mantenimiento **DEBERIA** reapuntar a
   `urn:kora:kb:gobernanza`.
2. **`canario-spec.md` y `procesos-spec.md`** reconocidas como
   deprecadas: contenido valido pero no canon vigente; sin clientes
   mecanicos en el toolchain. Quedan como referencia historica
   accesible por URN.
3. **Fase 2 declarada (cerrada parcialmente en v6.0)**: compactacion de
   `autoria-spec`, `md-spec` y consolidacion `runtime-spec-md` +
   `transmutation-spec`. La autorizacion HITL llego en v6.0 (Fase 2b);
   la ejecucion vive en sesion dedicada.

Decision arquitectural completa en
`urn:kora:kb:adr-kora-v6-simplificacion`.

## 14. Migracion v5.0 → v6.0 (KORA esencial v7)

Cambios doctrinales en v6.0 (HITL 2026-05-20):

1. **Hermes activado**: §8.2 reescrita. `hermes` es runtime canonico
   desde 2026-05-20. Stub `runtime/hermes-runtime-extension.md` v0.1
   declarado; contenido completo en Fase 2b.
2. **Freeze parcial**: §8.3 reescrita. `autoria-spec` y
   `transmutation-spec` quedan editables (autoriza compactacion);
   `harness-spec` sigue en freeze como core ontologico.
3. **Runtimes canonicos reducidos a 4**: `claude-code`, `codex`,
   `openclaw`, `hermes`. §8.4 nueva registra los 4 archivados
   (`gemini`, `mastra`, `opencode`, `agentskills`) con URNs que siguen
   resolviendo.
4. **Toolchain ajustado**: `transmute.py` reduce
   `SUPPORTED_TARGETS`/`TARGET_ADAPTERS`/`PRESERVATION_MATRIX` a 4 +
   hermes; rechaza slugs archivados en `--target`.
5. **Drift `entornos_objetivo` limpiado**: 5 skills productivos
   reciben actualizacion para listar solo runtimes canonicos.

Decision arquitectural completa en
`urn:kora:kb:adr-kora-v7-esencial`.

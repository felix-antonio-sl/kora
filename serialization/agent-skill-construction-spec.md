---
_manifest:
  urn: "urn:kora:kb:agent-skill-construction-spec"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-28"
    source: "Cristalizacion KORA-native del metodo de construccion de agentes y skills desde autoria-spec, harness-spec y cat-thinking; v1.1 declara que NO gobierna shape (eso vive en autoria-spec), reemplaza tablas duplicadas por punteros normativos, alinea spec_ref de checks con autoria-spec v1.2 y registra que el toolchain ya enforza status/version en root y status-por-directorio para artefactos productivos."
version: "1.1.0"
status: publicado
tags: [spec, construccion-agentica, autoria, pre-transmutacion, categorial]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:md-spec"
  cites:
    - "urn:kora:kb:knowledge-spec"
    - "urn:kora:kb:procesos-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:risk-register-spec"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:multiagente-spec"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:cat-agent-coalgebra"
    - "urn:kora:kb:cat-skill-algebra"
    - "urn:kora:kb:cat-behavioral-preservation"
    - "urn:fxsl:kb:icas-composicion"
    - "urn:fxsl:kb:icas-preservacion"
    - "urn:fxsl:kb:icas-efectos"
    - "urn:fxsl:kb:icas-agencia"
    - "urn:fxsl:kb:icas-escala"
    - "urn:fxsl:kb:icas-procesos"
    - "urn:fxsl:kb:icas-safety-alignment"
    - "urn:fxsl:kb:icas-infraestructura"
---

# KORA/Agent-Skill-Construction-Spec v1.1.0

## 1. Definicion

`agent-skill-construction-spec` gobierna la construccion de agentes y skills
KORA **antes** de cualquier transmutacion runtime. Su salida autoritativa es un
artefacto fuente conforme a `autoria-spec`: `SKILL.md` para
`forma_material: habilidad` y `AGENT.md` para las demas formas materiales.

La decision canonica es:

> La construccion agentica en KORA produce IR canonico primero; los runtimes son
> proyecciones posteriores.

Esta spec no eleva ningun formato externo o historico como fuente productiva.
Los insumos previos a KORA pueden informar el diseno, pero la salida
autoritativa siempre es IR canonico conforme a `autoria-spec`.

### 1.1 Alcance

Gobierna:

1. diseno de un agente o skill nuevo desde requerimientos,
2. reconstruccion de material pre-categorial en `_FRAGUA/` o `_TALLER/`,
3. promocion editorial de una idea a `AGENT.md` o `SKILL.md`,
4. handoff desde construccion hacia `transmutation-spec`.

No gobierna:

1. proyeccion a Claude Code, Codex, OpenClaw, Gemini, Mastra o agentskills,
2. despliegue, hosting o operacion runtime,
3. formatos externos o historicos como fuente productiva,
4. docs generadas o `_BUILD/` como autoridad.

### 1.2 Lo que NO gobierna esta spec

Esta spec dice **como** llegar al artefacto, no **cual** es su shape final.
Por tanto:

- **Shape de frontmatter y body**: gobernado por `autoria-spec §3-§7`.
  Esta spec no duplica el envelope, las matrices condicionales por forma
  material, ni los identificadores YAML.
- **Lifecycle agentico** (`borrador -> activo -> deprecado -> retirado`)
  y su enforcement de status-por-directorio: gobernado por
  `autoria-spec §11` y el check `autoria-conformance`.
- **Regimen URN `urn:{ns}:artefacto:{id}`** y coherencia namespace-directorio:
  gobernado por `autoria-spec §10` y el check `autoria-conformance`.
- **Validacion estructural completa** (vector, atlas, dominio, shape
  coalgebraico, fidelidad runtime): tabla completa en `autoria-spec §14`.
  Esta spec aporta solo los checks especificos del **proceso de
  construccion** (§5.2), no del shape resultante.

Si una regla aparece tanto aqui como en `autoria-spec`, **prevalece
`autoria-spec`** (§1.2 regla de precedencia).

### 1.2 Precedencia

Esta spec vive en la capa de **serializacion** y especializa el proceso de
crear el artefacto fuente. Si tensiona con otra spec:

1. `gobernanza` decide precedencia constitucional.
2. `harness-spec` decide que es ontologicamente valido.
3. `autoria-spec` decide el shape final de `AGENT.md`/`SKILL.md`.
4. Esta spec decide el proceso pre-transmutacion para llegar a ese shape.
5. `transmutation-spec` decide la proyeccion posterior a runtimes.

Regla: un constructor **NO DEBE** usar esta spec para relajar `autoria-spec`.
Rationale: la construccion es un funtor hacia IR; no redefine el codominio.

## 2. Modelo categorico

### 2.1 Categorias de trabajo

| Simbolo | Categoria | Objetos | Morfismos |
| --- | --- | --- | --- |
| `Req` | requerimientos agenticos | rol, objetivo, conocimiento, restricciones, entorno | refinamientos de requerimientos |
| `Blueprint` | disenos KORA tipados | vector PMI x LFS, atlas, contratos, FSM, knowledge map | refinamientos que preservan contrato observable |
| `IR` | artefactos canonicos | `AGENT.md`, `SKILL.md` conformes a `autoria-spec` | cambios versionados o promocion de forma material |
| `Diag` | diagnosticos | findings de validacion, riesgos, perdidas declaradas | agregacion y cierre de findings |
| `Runtime_R` | artefactos runtime | outputs derivados por target | proyecciones runtime |

La construccion canonica es:

```text
Build = Materialize o Design : Req -> IR
```

`Design: Req -> Blueprint` elige vector, forma material, interfaz y
conocimiento. `Materialize: Blueprint -> IR` escribe el archivo fuente y sus
fibras auxiliares.

Rationale: `urn:fxsl:kb:icas-procesos` modela procesos de ingenieria como
funtores entre categorias de artefactos. `urn:fxsl:kb:icas-preservacion`
exige declarar que se preserva y que se pierde en cada traduccion.

### 2.2 Leyes de construccion

1. `Build` **DEBE** preservar identidad semantica: el objetivo declarado en
   `Req` debe seguir observable en `IR`.
2. `Build` **DEBE** preservar composicion: si dos requerimientos se componen
   por interfaz, el artefacto resultante debe exponer una composicion tipada o
   rechazar la fusion.
3. `Build` **DEBE** preservar identidad: un requerimiento nulo o puramente
   editorial no debe inventar capacidades nuevas.
4. `Build` **DEBE** declarar perdida: cualquier elemento de `Req` que no entre
   en `IR` debe quedar como descarte justificado, riesgo o deuda.
5. `Build` **NO DEBE** saltar directo a `Runtime_R`. La flecha correcta es
   `Req -> IR -> Runtime_R`.

Correcto: requerimiento -> blueprint con vector -> `SKILL.md` valido ->
`kora transmute`.

Incorrecto: requerimiento -> prompt runtime o workspace externo sin fuente
KORA primaria.

Rationale: `urn:fxsl:kb:icas-composicion` fija composicion e identidad como
leyes basicas; `urn:fxsl:kb:icas-preservacion` fija la functorialidad como test
de traduccion.

### 2.3 Lectura minima con cat-thinking

Cuando el artefacto nuevo involucra arquitectura, interaccion, delegacion,
conocimiento gobernado, safety o runtime, el constructor **DEBE** ejecutar una
lectura categorial minima antes de fijar el vector:

1. identificar categoria base,
2. tipificar objetos y morfismos,
3. elegir la lectura mas debil que resuelve el problema,
4. citar URNs ICAS especificas que sostienen la decision,
5. declarar si la lectura es formal o heuristica.

La skill operativa es `urn:kora:artefacto:cat-thinking`. En este repo, su corpus
ICAS-BoK local vive en:

```text
artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/
```

## 3. Metodo de construccion

### 3.1 Fase A: Intake

El intake **DEBE** capturar:

| Campo | Pregunta | Salida |
| --- | --- | --- |
| identidad | que rol cumple y para quien | `perfil.dominio`, `descripcion`, `tags` |
| objetivo | que resultado observable entrega | `perfil.salidas`, `plan.estado_terminal` |
| forma | skill, subagente, agente o plataforma | `atlas.forma_material` |
| conocimiento | que URNs puede consultar | `conocimiento_permitido` |
| interaccion | que entradas, herramientas y permisos usa | `interfaz` |
| estado | que memoria o materia necesita | `vector_ontologico.mu`, `contexto.memoria_config` |
| riesgo | que puede salir mal y como se mitiga | `invariantes`, `qa_budget`, `risk_register` |

Si un campo no aplica, el constructor **DEBE** omitirlo o declararlo vacio segun
`autoria-spec`; **NO DEBE** rellenarlo con placeholder decorativo.

### 3.2 Fase B: Enmarque categorial

El constructor **DEBE** traducir el intake a PMI x LFS:

| Pregunta de diseno | Eje o estructura | Soporte |
| --- | --- | --- |
| que plan ejecuta | `pi` / free monad | `urn:fxsl:kb:icas-agencia` |
| sobre que materia corre | `mu` / cofree comonad | `urn:fxsl:kb:icas-agencia` |
| como interactua | `xi` / lente, protocolo u operad | `urn:fxsl:kb:icas-agencia`, `urn:fxsl:kb:icas-escala` |
| a que escala opera | `lambda` | `urn:fxsl:kb:icas-escala` |
| como se acopla al humano | `phi` | `harness-spec`, `qa-spec` |
| que compromisos eticos exige | `sigma`, `qa_budget`, `risk_register` | `urn:fxsl:kb:icas-safety-alignment` |

Regla: la forma material **NO DEBE** elegirse por gusto de packaging. Debe
derivarse del vector y del dominio de realizabilidad de `autoria-spec`.

Correcto: `mu=0`, `xi=1`, `lambda=0` -> candidata a `habilidad`.

Incorrecto: declarar `agente-plataforma` para una rutina sin materia ambiental.

### 3.3 Fase C: Decision de forma material

Resumen operativo para el constructor (la matriz autoritativa de dominio
por forma material vive en `autoria-spec §5`):

| Forma | Usar cuando | Evitar cuando |
| --- | --- | --- |
| `habilidad` | capacidad portable, sin workspace, `mu<=1`, `lambda=0` | requiere memoria persistente, orquestacion o servicio always-on |
| `subagente` | invocado por otro artefacto, contrato I/O claro | necesita identidad operativa propia frente a humano |
| `agente-propiamente-tal` | workspace productivo, memoria y ciclo propio | solo envuelve una tecnica reusable |
| `agente-plataforma` | materia ambiental, servicio o fleet always-on | no hay runtime capaz de sostener `mu=3` |

El constructor **DEBE** preferir la forma mas baja que satisface el objetivo.

Reglas:

1. La eleccion **DEBE** respetar el dominio de proyeccion valido declarado
   por `autoria-spec §5` para cada forma material; si el vector cae fuera,
   el constructor **DEBE** ajustar el vector o cambiar la forma elegida.
2. La promocion entre formas (`habilidad -> subagente -> agente-propiamente-tal -> agente-plataforma`)
   sigue las reglas de `autoria-spec §8`; **NO** se redefine aqui.

Rationale: `cat-thinking` exige la lectura categorial mas debil que cumple el
trabajo; esto reduce deuda y sobre-formalizacion.

### 3.4 Fase D: Contrato de conocimiento

Todo artefacto con conocimiento gobernado **DEBE** declarar conocimiento por
URN, no por path duro, en `extensions.kora.conocimiento_permitido`.

Reglas:

1. `conocimiento_permitido` **DEBE** contener solo URNs resolubles.
2. Si el artefacto no usa KB, **DEBE** declarar lista vacia o omitir el campo
   solo cuando `autoria-spec` lo permita.
3. La seleccion de conocimiento **DEBE** ser explicita: no hay retrieval
   implicito por similitud cuando el contrato exige fuente gobernada.
4. Paths locales **PUEDEN** aparecer en `referencias/` o body solo como ayuda de
   navegacion; no sustituyen URNs.

Correcto: `conocimiento_permitido: ["urn:kora:kb:autoria-spec"]`.

Incorrecto: `conocimiento_permitido: ["serialization/autoria-spec.md"]`.

Rationale: en KORA la cartografia de conocimiento se materializa como URNs
resolubles por catalogo derivado.

### 3.5 Fase E: Nucleo conductual

El plan **DEBE** modelarse como FSM cuando el artefacto tenga ramificacion real.
Para artefactos con `extensions.kora.verificacion_coalgebraica: true`, el
constructor **DEBE** declarar `artefacto.plan.fsm` conforme a `autoria-spec`.

Checks minimos:

1. estado inicial existe,
2. terminales existen,
3. transiciones apuntan a estados existentes,
4. todo estado no terminal alcanza algun terminal,
5. los ciclos tienen salida finita,
6. la sub-coalgebra segura, si se declara, cierra bajo transiciones.

Rationale: `urn:kora:kb:cat-agent-coalgebra` modela agentes como coalgebras y
FSM como categoria finita de estados/transiciones; `urn:fxsl:kb:icas-efectos`
soporta bisimulacion como equivalencia observacional.

### 3.6 Fase F: Interfaz y capacidades

La interfaz **DEBE** declarar lo observable:

1. entradas esperadas,
2. salidas emitidas,
3. herramientas o permisos necesarios,
4. limites de autoridad,
5. handoffs si `xi>=3`,
6. contrato de API observable cuando el artefacto se compone con otros.

Un artefacto **NO DEBE** asumir herramientas por ambiente. Las capacidades
deben aparecer en `interfaz`, `extensions.{runtime}` o en la runtime-extension
correspondiente.

Rationale: `urn:fxsl:kb:icas-infraestructura` modela tool use como profunctor:
la composicion con herramientas ocurre por interfaz, no por conocimiento de
implementacion interna.

### 3.7 Fase G: Invariantes, seguridad y riesgo

Todo artefacto productivo **DEBE** declarar reglas duras suficientes para
impedir drift de objetivo. Los agentes propiamente tales y de plataforma
**DEBEN** declarar `compromisos_eticos`.

Cuando el riesgo es no trivial, el constructor **DEBERIA** agregar:

1. `artefacto.contexto.qa_budget` para pisos operativos,
2. `artefacto.contexto.risk_register` para amenazas y mitigaciones,
3. criterio de verificacion runtime si habra transmutacion.

Correcto: una skill de curaduria declara que no publica conocimiento sin URN
resoluble.

Incorrecto: "ser cuidadoso" como unica regla dura.

Rationale: `urn:fxsl:kb:icas-safety-alignment` trata guardrails como sketches e
invariantes como sub-coalgebras; `qa-spec` y `risk-register-spec` materializan
el contrato operacional en KORA.

### 3.8 Fase H: Materializacion

La materializacion **DEBE** seguir la topologia normada por
`autoria-spec §5` para cada forma material. Resumen rapido:

| Forma | Fuente primaria | Fibras canonicas |
| --- | --- | --- |
| `habilidad` | `artifacts/skills/{ns}/{id}/SKILL.md` | `scripts/`, `referencias/`, `recursos/` (autoria-spec §5.1) |
| `subagente` | `artifacts/agents/{ns}/{id}/AGENT.md` | `memoria/` si `mu>=2`, `_BUILD/{target}/` derivado (autoria-spec §5.2) |
| `agente-propiamente-tal` | `artifacts/agents/{ns}/{id}/AGENT.md` | memoria, recursos, `_BUILD/`, `_transmutation.yml` (autoria-spec §5.3) |
| `agente-plataforma` | runtime-extension aplicable | materia ambiental segun runtime (autoria-spec §5.4) |

Reglas:

1. Cualquier subdir fuera de los canonicos declarados por `autoria-spec §5`
   o por su runtime-extension es invalido en `status: activo`.
2. El namespace del URN **DEBE** coincidir con el primer subdirectorio bajo
   `artifacts/agents/` o `artifacts/skills/`. Enforcement: lint
   (`autoria-conformance`).
3. El body **DEBE** explicar solo lo que ayude a operar el artefacto;
   detalle voluminoso pasa a `referencias/` o `recursos/`.

## 4. Absorcion de insumos

Los materiales en `_FRAGUA/INBOX` o `_TALLER/INBOX` son insumos de diseno, no
autoridad normativa. La absorcion valida conserva intencion, conocimiento,
estado, interfaz y riesgo, pero materializa esos elementos solo en el shape de
`autoria-spec`.

Reglas:

1. Un insumo externo **PUEDE** conservarse como referencia historica o evidencia
   de requerimientos.
2. Un insumo externo **NO DEBE** promocionarse copiando su envelope,
   namespaces, preambulos runtime ni catalogos como shape KORA productivo.
3. Toda perdida de semantica durante la absorcion **DEBE** declararse como
   descarte justificado, riesgo o deuda residual.

## 5. Validacion

### 5.1 Gate minimo

Antes de considerar construido un artefacto, el constructor **DEBE** correr:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

Si toco toolchain, specs, relaciones de conocimiento o comportamiento
compartido, **DEBE** correr ademas:

```bash
python3 -m unittest discover -s tests
```

Si toco knowledge o relaciones, **DEBE** revisar:

```bash
python3 toolchain/kora kb-graph --json --orphans
```

Si el cierre incluye runtime, la transmutacion aplicable **DEBE** ejecutarse
despues de que el IR fuente pase los gates anteriores.

### 5.2 Tabla de checks

Esta tabla cubre los **checks especificos de construccion** que esta spec
gobierna. Los checks de **shape final** (envelope, vector, atlas,
condicionales por forma material, lifecycle, namespace-directorio) viven
en `autoria-spec §14` y se ejecutan via `autoria-conformance`.

| Check | Condicion | Enforcement | Spec ref |
| --- | --- | --- | --- |
| `construction-source-primary` | existe `AGENT.md` o `SKILL.md` como fuente primaria | lint | §2 |
| `construction-vector-fit` | vector cumple `harness-spec §4.1` y dominio de forma material `autoria-spec §5` | lint | §3.2, §3.3 |
| `construction-knowledge-explicit` | conocimiento por URN resoluble, no path duro | lint/manual | §3.4 |
| `construction-fsm-valid` | estados, terminales y transiciones son coherentes | lint | §3.5 |
| `construction-interface-typed` | entradas, salidas, tools y permisos observables | manual | §3.6 |
| `construction-risk-declared` | riesgos no triviales tienen mitigacion o deuda | manual | §3.7 |
| `construction-runtime-separation` | no hay `_BUILD/` ni runtime output como fuente | manual | §3.8 |
| `construction-categorical-minimality` | usa la lectura categorial mas debil suficiente | manual | §2.3 |
| `construction-authoring-shape` | el artefacto usa `artefacto` y no un envelope externo | lint | §3.8 |

Checks complementarios (gobernados por `autoria-spec §14`, no por esta spec):

- `autoria-conformance` — envelope universal + fibra por forma material;
  incluye desde v1.1 el enforcement de `status`/`version` en root del
  frontmatter, `status` valido en zona productiva (no `borrador`) y
  coherencia namespace-directorio.
- `vector-laws` — leyes inter-eje `harness-spec §4.1`.
- `coalgebra-conformance` — termination del FSM cuando `plan.fsm` esta
  declarado y sub-coalgebra de safety cerrada.
- `fidelidad-agentskills`, `fidelidad-mastra` — proyeccion runtime sin
  perdida no declarada.
- `skill-structure` — subdirs canonicos para `habilidad`.

### 5.3 Criterio de cierre

Un artefacto queda listo para transmutacion si:

1. `autoria-spec` lo acepta,
2. `harness-spec` acepta su vector,
3. `knowledge-spec` acepta sus URNs,
4. los riesgos relevantes estan declarados,
5. `check --strict` pasa,
6. cualquier deuda no bloqueante queda escrita como deuda residual, no como
   silencio.

## 6. Antipatrones

| Antipatron | Falla | Correccion |
| --- | --- | --- |
| runtime-first | el output target suplanta IR | crear fuente `AGENT.md`/`SKILL.md` y transmutar despues |
| fuente transplantada | se copia un envelope externo como shape KORA | traducir a `autoria-spec` |
| KB por path | knowledge queda no resoluble por URN | usar `conocimiento_permitido` |
| vector decorativo | PMI x LFS no deriva del comportamiento | rehacer enmarque categorial |
| skill inflada | una habilidad contiene corpus entero | mover detalle a `referencias/` |
| agente sin materia | se declara agente donde basta skill | bajar forma material |
| guardrail retorico | seguridad no tiene regla verificable | escribir regla dura, qa o riesgo |
| over-formalizacion | se introduce 2-cat/operad sin necesidad | volver a categoria mas simple |

## 7. Migracion

Esta spec es aditiva.

### 7.1 Contrato vigente v1.1

Cambios v1.0 -> v1.1 (todos compatibles):

- **§1.2 (nueva)** — declara explicitamente que esta spec NO gobierna shape
  ni lifecycle ni regimen URN (todo en `autoria-spec`). Punto de
  precedencia explicito: si una regla aparece en ambas, prevalece
  `autoria-spec`.
- **§3.3** — la matriz de "usar cuando / evitar cuando" queda como resumen
  operativo; el dominio de proyeccion autoritativo y la promocion entre
  formas viven en `autoria-spec §5` y `§8`.
- **§3.8** — topologia con punteros a las subsecciones especificas de
  `autoria-spec §5.1-§5.4` por forma material; agrega regla de
  namespace-directorio enforced por `autoria-conformance`.
- **§5.2** — tabla de checks ahora declara `Spec ref` por check y separa
  explicitamente los checks de **construccion** (esta spec) de los checks
  de **shape final** (`autoria-spec §14`). Registra que `autoria-conformance`
  v1.1 enforza status/version-en-root, status-por-directorio y
  namespace-directorio para artefactos agenticos productivos.

### 7.2 Reglas residuales

1. Artefactos productivos existentes **NO REQUIEREN** migracion inmediata por
   la sola aparicion de esta spec.
2. La proxima reconstruccion o promocion de material en `_FRAGUA/` o
   `_TALLER/` **DEBERIA** usar esta spec como gate de diseño.
3. Material en staging **PUEDE** conservarse como fuente historica, pero no debe
   promocionarse sin absorcion a `autoria-spec`.
4. Specs, skills o agentes que todavia remitan a shapes retirados **DEBERIAN**
   reescribir esas referencias hacia `autoria-spec` cuando se toquen por
   mantenimiento.

## 8. Relacion con otras specs

- `harness-spec` define el espacio ontologico que el constructor debe habitar.
- `autoria-spec` define el shape final que esta spec materializa.
- `knowledge-spec` gobierna URNs y morfismos de conocimiento consumidos.
- `qa-spec` y `risk-register-spec` gobiernan calidad y riesgo cuando se
  declaran.
- `multiagente-spec` gobierna handoffs y coreografia cuando `xi>=3`.
- `transmutation-spec` empieza cuando el IR fuente ya es valido.

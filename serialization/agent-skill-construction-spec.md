---
_manifest:
  urn: "urn:kora:kb:agent-skill-construction-spec"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-28"
    source: "Cristalizacion KORA-native del metodo de construccion de agentes y skills, inspirada por artifacts/agents/_FRAGUA/INBOX/guide_core_005_koda-agent-spec_koda.yml y guide_core_006_koda-agent-construct_koda.yml, reinterpretada desde autoria-spec, harness-spec y cat-thinking."
version: "1.0.0"
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
    - "urn:kora:kb:canario-spec"
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

# KORA/Agent-Skill-Construction-Spec v1.0.0

## 1. Definicion

`agent-skill-construction-spec` gobierna la construccion de agentes y skills
KORA **antes** de cualquier transmutacion runtime. Su salida autoritativa es un
artefacto fuente conforme a `autoria-spec`: `SKILL.md` para
`forma_material: habilidad` y `AGENT.md` para las demas formas materiales.

La decision canonica es:

> La construccion agentica en KORA produce IR canonico primero; los runtimes son
> proyecciones posteriores.

Esta spec no importa el formato KODA `agent.yaml`. Toma de KODA solo las
decisiones estructurales que siguen siendo validas en KORA: fuente declarativa,
maquina de estados, cartografia explicita de conocimiento, limites de
seguridad y validacion antes de despliegue.

### 1.1 Alcance

Gobierna:

1. diseno de un agente o skill nuevo desde requerimientos,
2. reconstruccion de material pre-categorial en `_FRAGUA/` o `_TALLER/`,
3. promocion editorial de una idea a `AGENT.md` o `SKILL.md`,
4. handoff desde construccion hacia `transmutation-spec`.

No gobierna:

1. proyeccion a Claude Code, Codex, OpenClaw, Gemini, Mastra o agentskills,
2. despliegue, hosting o operacion runtime,
3. formato externo KODA como fuente productiva,
4. docs generadas o `_BUILD/` como autoridad.

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

Rutas legacy como `KNOWLEDGE/fxsl/cat/...` **NO DEBEN** usarse como path vivo.

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

| Forma | Usar cuando | Evitar cuando |
| --- | --- | --- |
| `habilidad` | capacidad portable, sin workspace, `mu<=1`, `lambda=0` | requiere memoria persistente, orquestacion o servicio always-on |
| `subagente` | invocado por otro artefacto, contrato I/O claro | necesita identidad operativa propia frente a humano |
| `agente-propiamente-tal` | workspace productivo, memoria y ciclo propio | solo envuelve una tecnica reusable |
| `agente-plataforma` | materia ambiental, servicio o fleet always-on | no hay runtime capaz de sostener `mu=3` |

El constructor **DEBE** preferir la forma mas baja que satisface el objetivo.
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

Rationale: KODA acierta al exigir cartografia explicita de conocimiento; en
KORA esa cartografia se materializa como URNs resolubles por catalogo derivado.

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
3. canario o criterio de verificacion runtime si habra transmutacion.

Correcto: una skill de curaduria declara que no publica conocimiento sin URN
resoluble.

Incorrecto: "ser cuidadoso" como unica regla dura.

Rationale: `urn:fxsl:kb:icas-safety-alignment` trata guardrails como sketches e
invariantes como sub-coalgebras; `qa-spec` y `risk-register-spec` materializan
el contrato operacional en KORA.

### 3.8 Fase H: Materializacion

La materializacion **DEBE** seguir la topologia de `autoria-spec`:

| Forma | Fuente primaria | Fibras permitidas |
| --- | --- | --- |
| `habilidad` | `artifacts/skills/{ns}/{id}/SKILL.md` | `scripts/`, `referencias/`, `recursos/` |
| `subagente` | `artifacts/agents/{ns}/{id}/AGENT.md` | `memoria/` si aplica, `_BUILD/` derivado |
| `agente-propiamente-tal` | `artifacts/agents/{ns}/{id}/AGENT.md` | memoria, skills, recursos, `_BUILD/` derivado |
| `agente-plataforma` | runtime-extension aplicable | materia ambiental y extension de plataforma |

El body **DEBE** explicar solo lo que ayude a operar el artefacto. Detalle
voluminoso debe moverse a `referencias/` o `recursos/` cuando la forma material
lo permita.

## 4. Traduccion de KODA a KORA

Los archivos KODA en `_FRAGUA/INBOX` son fuentes historicas o insumos de
diseño, no autoridad normativa. La traduccion permitida es:

| Decision KODA | Traduccion KORA |
| --- | --- |
| `agent.yaml` como source code | `AGENT.md`/`SKILL.md` conforme a `autoria-spec` |
| required namespaces | `artefacto.{perfil,plan,interfaz,contexto,composicion,invariantes}` |
| KODA runtime instructions | runtime-extension o transmutacion, no body fuente |
| explicit knowledge cartography | `conocimiento_permitido` + URNs resolubles |
| state machine | `artefacto.plan` y `plan.fsm` si aplica |
| private cognitive models | skills internas, `referencias/` o procedimientos no expuestos |
| minimum guard set | `invariantes`, `qa_budget`, `risk_register`, permisos de `interfaz` |
| validation checklist | `kora check --strict`, tests y canarios segun alcance |

Regla: un constructor **PUEDE** inspirarse en KODA, pero **NO DEBE** copiar sus
namespaces, runtime preamble ni catalogo legacy como shape productivo KORA.

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

Si el cierre incluye runtime, la transmutacion y canario aplicables **DEBEN**
ejecutarse despues de que el IR fuente pase los gates anteriores.

### 5.2 Tabla de checks

| Check | Condicion | Enforcement |
| --- | --- | --- |
| `construction-source-primary` | existe `AGENT.md` o `SKILL.md` como fuente primaria | lint |
| `construction-vector-fit` | vector cumple `harness-spec` y dominio de forma material | lint |
| `construction-knowledge-explicit` | conocimiento por URN resoluble, no path duro | lint/manual |
| `construction-fsm-valid` | estados, terminales y transiciones son coherentes | lint |
| `construction-interface-typed` | entradas, salidas, tools y permisos observables | manual |
| `construction-risk-declared` | riesgos no triviales tienen mitigacion o deuda | manual |
| `construction-runtime-separation` | no hay `_BUILD/` ni runtime output como fuente | manual |
| `construction-categorical-minimality` | usa la lectura categorial mas debil suficiente | manual |
| `construction-koda-no-copy` | no copia namespaces KODA como shape KORA | manual |

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
| YAML transplantado | KODA se copia como shape KORA | traducir a `autoria-spec` |
| KB por path | knowledge queda no resoluble por URN | usar `conocimiento_permitido` |
| vector decorativo | PMI x LFS no deriva del comportamiento | rehacer enmarque categorial |
| skill inflada | una habilidad contiene corpus entero | mover detalle a `referencias/` |
| agente sin materia | se declara agente donde basta skill | bajar forma material |
| guardrail retorico | seguridad no tiene regla verificable | escribir regla dura, qa o riesgo |
| over-formalizacion | se introduce 2-cat/operad sin necesidad | volver a categoria mas simple |

## 7. Migracion

Esta spec es aditiva.

Reglas:

1. Artefactos productivos existentes **NO REQUIEREN** migracion inmediata por
   la sola aparicion de esta spec.
2. La proxima reconstruccion o promocion de material en `_FRAGUA/` o
   `_TALLER/` **DEBERIA** usar esta spec como gate de diseño.
3. Material KODA en `_FRAGUA/INBOX` **PUEDE** conservarse como fuente historica,
   pero no debe promocionarse sin traduccion a `autoria-spec`.
4. Specs, skills o agentes que todavia remitan a shape legacy **DEBERIAN**
   reescribir esas referencias hacia esta spec y `autoria-spec` cuando se
   toquen por mantenimiento.

## 8. Relacion con otras specs

- `harness-spec` define el espacio ontologico que el constructor debe habitar.
- `autoria-spec` define el shape final que esta spec materializa.
- `knowledge-spec` gobierna URNs y morfismos de conocimiento consumidos.
- `qa-spec` y `risk-register-spec` gobiernan calidad y riesgo cuando se
  declaran.
- `multiagente-spec` gobierna handoffs y coreografia cuando `xi>=3`.
- `transmutation-spec` empieza cuando el IR fuente ya es valido.
- `canario-spec` verifica que la proyeccion runtime conserva contrato
  observable.

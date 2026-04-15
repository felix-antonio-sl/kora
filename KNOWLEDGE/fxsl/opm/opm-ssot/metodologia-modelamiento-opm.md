---
_manifest:
  urn: urn:fxsl:kb:metodologia-modelamiento-opm
  provenance:
    created_by: kora/curator
    created_at: '2026-03-25'
    source: synthesis:opm-iso-19450,opm-opl-es,opcloud-tutorial-videos,opm-applied-system-modeling,opm-canonical-example
version: 3.5.1
status: published
tags:
- opm
- methodology
- system-modeling
- sd-construction
- refinement
- complexity-management
- modeling-protocol
- patterns
- antipatterns
- control-flow
- error-handling
- quantitative
- simulation
- executable-modeling
- opcloud
lang: es
extensions:
  kora:
    family: specification
    depends_on:
    - urn:fxsl:kb:opm-iso-19450
    - urn:fxsl:kb:opl-es
    shard_index: 1
    shard_count: 4
    shard_root_urn: urn:fxsl:kb:metodologia-modelamiento-opm
relations:
  cites:
  - urn:fxsl:kb:opl-es
  - urn:fxsl:kb:opm-iso-19450
---


# Metodologia de Modelamiento OPM — Protocolo de Modelamiento Conceptual de Sistemas


## 1 Definicion

Esta especificacion define la metodologia para construir modelos conceptuales de sistemas usando Object-Process Methodology (OPM). Consolida reglas normativas desde [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450) y [OPL-ES](urn:fxsl:kb:opl-es), e incorpora directamente la guia operativa de tool usage previamente dispersa en artefactos hoy deprecados. Para la especificacion formal del lenguaje OPM, ver [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450). Para la realizacion textual en espanol, ver [OPL-ES](urn:fxsl:kb:opl-es).

### 1.1 Alcance y Precedencia del Corpus

Este artefacto es una **guia derivada**. No reemplaza la base normativa del corpus.

Orden de precedencia:

1. **ISO 19450** gobierna semantica OPM, notacion, relaciones y procedimiento base de construccion del SD.
2. **OPL-ES** gobierna la realizacion textual en espanol sin alterar la semantica OPM.
3. **Esta metodologia** integra las capas normativas anteriores y explicita reglas operativas para lifecycle, simulacion, gobernanza del modelo y uso de herramienta.

Regla de resolucion:

- Si una regla de **semantica OPM** entra en conflicto con una regla de herramienta, prevalece ISO 19450.
- Si un artefacto en `lang: es` define **realizacion OPL en espanol** como parte de su contrato, prevalece OPL-ES. Un artefacto expositivo en `lang: es` PUEDE mantener sentencias OPL canonicas en ingles para preservar roundtrip con ISO/OPCloud, siempre que lo declare explicitamente y no presente esas sentencias como OPL-ES.
- Las capacidades de OPCloud NO redefinen por si solas la semantica de OPM; solo operacionalizan su uso en la herramienta.
- Los artefactos deprecados del directorio NO participan en precedencia; solo sirven como routing historico.

## 2 Definiciones

| Termino | Definicion |
|---------|-----------|
| SD (System Diagram) | OPD de nivel 0 que define proposito, alcance y funcion principal del sistema |
| SD1 | OPD descendiente de SD donde el proceso principal se refina exponiendo subprocesos |
| OPD (Object-Process Diagram) | Diagrama unico de OPM que expresa estructura y comportamiento |
| OPL (Object-Process Language) | Modalidad textual de OPM, equivalente semantica del OPD |
| Beneficiario | Stakeholder que extrae valor y beneficio del sistema |
| Transformee | Objeto transformado por un proceso |
| Agente | Enabler humano exclusivamente; el termino esta reservado para personas o grupos de personas |
| Instrumento | Enabler no humano (fisico o informatical) |
| Funcion | Proceso de nivel superior que provee valor, percibido por el beneficiario |
| Arquitectura | Combinacion de estructura + comportamiento que habilita la funcion y produce emergencia |
| Emergencia | Capacidad del sistema completo que ninguna parte individual exhibe |
| Proceso state-preserving | Proceso que mantiene el status quo de un objeto sin transformarlo |
| Objeto transiente | Objeto de vida corta creado y consumido inmediatamente entre dos procesos |
| Semantic strength | Fuerza semantica de un link procedural que determina precedencia en conflictos |
| Singular Name Principle | Los nombres de things en OPM DEBEN ser singulares. En ingles, colecciones humanas usan "Group" y las inanimadas "Set". En espanol, los equivalentes son "Grupo" y "Conjunto" |

## 3 Fundamentos Ontologicos

### 3.1 Principio de Ontologia Minima

> Si un sistema puede especificarse al mismo nivel de precision y detalle con dos lenguajes de diferentes tamanos ontologicos, el lenguaje con ontologia menor es preferible, siempre que la comprensibilidad sea comparable.

OPM usa exactamente tres tipos de elementos: objetos, procesos, y relaciones.

### 3.2 Teorema Objeto-Proceso

> Objetos, procesos y relaciones entre ellos constituyen una ontologia universal minima.

Demostrado por necesidad (especificar estructura requiere objetos; especificar comportamiento requiere procesos) y suficiencia (las cosas existen o suceden; solo se asocian mediante relaciones). Los objetos pueden ser stateful (con estados explicitos, transformables via effect) o stateless (sin estados, solo creables/consumibles). La distincion stateful/stateless es posterior a la base ontologica.

### 3.3 Asercion Objeto-Proceso

> Usando objetos, procesos, relaciones, y mecanismos de refinamiento (in-zooming y unfolding), se puede modelar conceptualmente cualquier sistema en cualquier dominio y nivel de complejidad.

## 4 Principios de Modelamiento

Todo modelamiento OPM DEBE respetar estos principios. Constituyen restricciones invariantes que gobiernan cada decision.

### 4.1 Function-as-a-Seed

> El modelamiento de un sistema DEBE comenzar definiendo, nombrando y representando la funcion del sistema, que es su proceso de nivel superior.

La funcion es la semilla de la que evoluciona el modelo. Comenzar por la forma (objetos) en vez de la funcion (proceso) es un error comun.

### 4.2 Importancia de Thing

> La importancia de un thing T en un modelo OPM es directamente proporcional al OPD mas alto en la jerarquia donde T aparece.

Objetos y procesos tienen igual estatus; ninguno tiene supremacia sobre el otro.

### 4.3 Transformacion de Objeto por Proceso

> En un modelo OPM completo, cada proceso DEBE estar conectado a al menos un objeto que el proceso transforma o a un estado de ese objeto.

Un proceso sin transforming link no tiene significado. Un proceso PUEDE tener multiples transformees.

### 4.4 Unicidad de Link Procedural

> A cualquier nivel de detalle, un objeto y un proceso PUEDEN estar conectados con a lo sumo un link procedural, que determina univocamente el rol del objeto respecto al proceso.

**Resolucion de colision de roles:** Cuando un objeto es simultaneamente enabler (agent o instrument) y transformee (affectee) del mismo proceso, el transforming link DEBE prevalecer por mayor semantic strength. El modelador PUEDE agregar un stick-figure para preservar la identidad humana del agent desplazado. Alternativa: hacer in-zoom al proceso y asignar agent link a un subproceso y effect link a otro.

### 4.5 Representacion de Hechos del Modelo

> Todo hecho del modelo DEBE aparecer en al menos un OPD del set de OPDs del modelo.

No todo hecho necesita repetirse en cada OPD. Suficiente con que aparezca al menos una vez.

### 4.6 Jerarquia de Detalle

> Cuando un OPD se vuelve dificil de comprender por exceso de detalle, se DEBE crear un nuevo OPD descendiente.

Heuristica: un OPD NO DEBERIA exceder 20-25 entidades ni una pantalla/pagina.

### 4.7 Equivalencia Grafico-Texto

> Todo modelo OPM DEBE expresarse en modalidades graficas (OPD) y textuales (OPL) semanticamente equivalentes.

Cada OPD tiene un paragrafo OPL correspondiente. La redundancia aprovecha canales cognitivos duales (visual + verbal).

### 4.8 Trade-off Completitud-Claridad

> El detalle abrumador de sistemas reales DEBE balancearse distribuyendo la especificacion completa a traves del set de OPDs, manteniendo cada OPD individual claro y comprensible.

## 5 Clasificacion del Sistema

Antes de construir el SD, el modelador DEBE clasificar el sistema. La clasificacion determina que componentes del SD aplican.

Reglas prescriptivas por categoria:

- **Artificial**: DEBE modelarse con los 5 componentes completos
- **Natural**: NO DEBE modelarse purpose (usar "outcome"). NO DEBE modelarse problem occurrence. NO hay agentes humanos — solo instrumentos. Componentes aplicables del SD: main function (si), process enablers (si, solo instrumentos), environment (si), purpose (no → outcome), problem occurrence (no)
- **Social**: DEBE modelarse con los 5 componentes completos. Se PUEDE usar state-specified enabling links para condiciones ambientales
- **Socio-tecnico**: DEBE modelarse con los 5 componentes completos. Se PUEDE usar tagged structural links para relaciones no fundamentales

### 5.1 Patrones de Referencia por Categoria

Los siguientes patrones sintetizan ejemplos pedagogicos recurrentes que conviene tener a mano al clasificar el sistema antes de construir el SD:

| Categoria | Patron de referencia | Leccion operativa |
|-----------|----------------------|-------------------|
| Artificial | `Airplane Flying`, `Battery Charging` | Hay purpose explicito, problem occurrence, agentes humanos y un benefit-providing object claramente identificable |
| Natural | `Fetus Developing`, `Rain Storm Forming` | Se modela outcome en vez de purpose; el outcome puede ser beneficial o detrimental; no hay agentes humanos |
| Social | `Conference Occurring` | Las condiciones ambientales PUEDE expresarse con state-specified enabling links, por ejemplo `good Weather` |
| Socio-tecnico | `Online Professional Identity Managing` | Tagged structural links suelen ser necesarios para relaciones no fundamentales, por ejemplo `Profile represents User` |
| Physical con partes informaticales | `Baggage Transporting` | Un sistema con tracking o software auxiliar SIGUE clasificandose como physical si la transformacion dominante es fisica |

## 6 Construccion del SD — Nivel 0

El SD DEBE ser simple y claro, con minimos detalles tecnicos. Todos los stakeholders DEBEN poder comprender el SD sin expertise tecnico.

## 6.0 Wizard Agnostico de Construccion del SD

El `wizard` del SD es un **protocolo de interaccion** agnostico de herramienta. No presupone OPCloud, formularios, UI grafica ni asistente LLM. Cualquier implementacion valida DEBE guiar al modelador por una secuencia ordenada de checkpoints y producir, al final, un SD semanticamente completo.

**Implementaciones validas:** entrevista guiada, formulario estructurado, checklist operativa, asistente conversacional, plugin de modelado o workflow humano moderado.

**Regla central:** cada etapa del wizard DEBE cerrar con un hecho del modelo explicitado y listo para representarse en OPD/OPL. El wizard NO termina cuando el usuario "entiende" el sistema; termina cuando los facts minimos del SD quedaron decididos.

**Pre-etapa obligatoria:** antes de iniciar el wizard, el modelador DEBE clasificar el sistema segun §5. La clasificacion determina si se habla de purpose u outcome y si `Problem Occurrence` aplica.

| Etapa | Objetivo | Output minimo obligatorio | Mapeo metodologico |
|-------|----------|---------------------------|--------------------|
| 0 | Clasificar sistema | Tipo: artificial / natural / social / socio-tecnico | §5 |
| 1 | Fijar proceso principal | Nombre canonico del main process | §6.1 |
| 2 | Identificar stakeholder primario | Beneficiary group o affectee equivalente | §6.2 |
| 3 | Fijar valor a transformar | Beneficiary/outcome attribute + input/output states | §6.3 |
| 4 | Fijar funcion principal | Benefit-providing object + atributo funcional, si aplica | §6.4 |
| 5 | Resolver agencia humana | Agent set valido o declaracion explicita de ausencia | §6.5 |
| 6 | Delimitar el sistema | Nombre del sistema + exhibition del proceso principal | §6.6 |
| 7 | Identificar enablers no humanos | Instrument set | §6.7 |
| 8 | Fijar transformees y resultados | Inputs, affectees y outputs | §6.8 |
| 9 | Delimitar contexto externo | Environment objects/processes | §6.9 |
| 10 | Modelar problema inicial, si aplica | Problem occurrence o decision explicita de no-aplicacion | §6.10 |
| 11 | Cerrar con gate de consistencia | Checklist SD `PASS/FAIL` | §6.11 |

**Semantica de cierre por etapa:**

- Si una etapa no puede cerrarse, el wizard DEBE retroceder a la etapa anterior que bloquea la decision.
- Si el sistema es **natural**, la etapa 10 DEBE cerrarse como `NO APLICA`, no como omision silenciosa.
- Si el sistema transforma multiples objetos, la etapa 4 DEBE dejar explicitado cual es el `Benefit-Providing Object`.
- Si no existen agentes humanos, la etapa 5 DEBE registrar `sin agentes humanos` en vez de forzar un placeholder.

**Contrato de salida del wizard:** un wizard agnostico correcto entrega, como minimo, un paquete de decisiones equivalente a:

1. tipo de sistema
2. proceso principal
3. beneficiary/affectee
4. atributo de valor + transicion de estados
5. funcion principal
6. agentes
7. sistema + exhibition
8. instrumentos
9. input/output set
10. environment
11. problem occurrence o no-aplicacion
12. verificacion SD

Una herramienta PUEDE dividir o fusionar etapas por conveniencia UX, pero NO DEBE perder ninguno de estos outputs semanticamente necesarios.

## 6.1 Paso 1: Identificacion del Proceso Principal

La forma del nombre depende del idioma de realizacion:

- En artefactos y modelos en **ingles**, el nombre del proceso DEBE terminar con verbo en forma gerundio (sufijo "-ing"), conforme a [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).
- En artefactos y modelos en **espanol**, el nombre del proceso DEBE encabezarse con infinitivo (-ar, -er, -ir) o con una nominalizacion verbal cuya primera palabra termine en `-ción`, conforme a [OPL-ES](urn:fxsl:kb:opl-es) §1.1. La forma en `-miento` TAMBIEN PUEDE aceptarse cuando el dominio la exija.

**Correcto:** `Battery Charging`, `Airplane Flying`

**Incorrecto:** `Charge Battery`, `Fly Airplane`

En ingles, el nombre DEBERIA combinar el transformee seguido del verbo gerundio. En espanol, DEBERIA mantener la misma funcion nominal usando infinitivo o, cuando mejore la naturalidad terminologica del dominio, una forma encabezada por `-ción`.

## 6.2 Paso 2: Grupo Beneficiario

El nombre DEBE ser singular segun el Singular Name OPM Principle:

- En ingles: sufijo "Group" para humanos y "Set" para inanimados
- En espanol: sufijo "Grupo" para humanos y "Conjunto" para inanimados

El grupo beneficiario DEBE representarse como objeto fisico.

## 6.3 Paso 3: Atributo del Beneficiario y Estados

El modelador DEBE definir un atributo informatical del beneficiario con exactamente dos estados:
- **Estado input** (actual/problematico)
- **Estado output** (deseado/mejorado)

OPL: "[Main Process] changes [Beneficiary Attribute] of [Beneficiary Group] from [input] to [output]."

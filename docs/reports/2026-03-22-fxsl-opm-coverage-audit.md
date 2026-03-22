# FXSL OPM Coverage Audit

## Resumen

- Fecha: `2026-03-22`
- Metodo: matriz de cobertura por familia tematica (`source -> fact set -> artifact`)
- Alcance:
  - `OPERATIONS/source/fxsl/opm-methodology/opcloud-tutorial-videos.md`
  - `OPERATIONS/source/fxsl/opm-methodology/opm-iso.md`
  - `OPERATIONS/source/fxsl/opm-methodology/opm_youtube.md`
  - `OPERATIONS/source/fxsl/opm-methodology/OPM version felix.md`
- Artefactos auditados:
  - `KNOWLEDGE/fxsl/opm/opcloud-tutorial-videos.md`
  - `KNOWLEDGE/fxsl/opm/opm-iso-19450.md`
- Granularidad: exhaustiva a nivel de familias y secciones recuperables; no es un diff lexical linea-a-linea.

## Veredicto

| Artefacto | Conformidad mecanica | Cobertura por familias | CR | Juicio |
| --- | --- | --- | --- | --- |
| `KNOWLEDGE/fxsl/opm/opcloud-tutorial-videos.md` | `PASS` | Sin gaps factuales concretos detectados | `1.299` | `PASS con excepcion de compresion justificada` |
| `KNOWLEDGE/fxsl/opm/opm-iso-19450.md` | `PASS` | Sin gaps concretos detectados en esta matriz | `4.687` vs `opm-iso.md` | `PASS` |

Convenciones de estado:

- `COVERED`: el hecho o familia esta recuperado de forma suficiente.
- `COVERED+COMPRESSED`: el contenido esta recuperado con compresion fuerte, sin gap factual concreto detectado.
- `COVERED+SUPPLEMENTED`: la familia se cubre en el artefacto y absorbe material auxiliar desde fuentes complementarias.
- `COVERED+JUSTIFIED`: cobertura correcta con una excepcion explicitada, no un gap factual.

## Matriz A — OPCloud Tutorial

| Source section | Source ref | Fact set | Artifact ref | Estado | Nota |
| --- | --- | --- | --- | --- | --- |
| `Getting Started` | `opcloud source:25` | Creacion de objetos/procesos, guardado, navegacion, wizard | `opcloud artifact:26` | `COVERED` | Los headings primarios coinciden y los pasos operativos clave sobreviven. |
| `Core Features` | `opcloud source:102` | OPD3, search, objects/processes, states, links, OPL panel | `opcloud artifact:88` | `COVERED` | Reincorporados `Link Properties`, `Agent Links`, `Instance Links`, `Specialization`. |
| `Inner and Outer Objects` | `opcloud source:202` | inner/outer scope, conversion, drag warning, visual indicator | `opcloud artifact:149` | `COVERED` | El warning y el indicador visual quedaron preservados semantica y operativamente. |
| `Advanced Features` | `opcloud source:222` | halo, semi-folding, style, resize, grid, images | `opcloud artifact:160` | `COVERED` | No se detecto perdida material de comandos o restricciones. |
| `Model Management` | `opcloud source:308` | export, templates, ontology, permissions, moving, sub-models | `opcloud artifact:195` | `COVERED` | Se mantienen permisos, version history, owner/edit token y restricciones de organizacion. |
| `Settings and Preferences` | `opcloud source:404` | user/model settings, OPL language, arrangement | `opcloud artifact:230` | `COVERED` | Preserva settings funcionales. |
| `Integration Features` | `opcloud source:432` | MQTT, ROS | `opcloud artifact:251` | `COVERED` | Conserva arquitectura y casos de uso. |
| `Simulation and Execution` | `opcloud source:464` | conceptual simulation, computational objects, calculations, loops, input | `opcloud artifact:263` | `COVERED` | Preserva tipos, aliases, loops, user input y condiciones. |
| `Requirements Modeling` | `opcloud source:542` | attach/remove/view requirements y ejemplo Door-Peephole | `opcloud artifact:316` | `COVERED` | El ejemplo Door-Peephole ya esta recuperado explicitamente. |
| `Model Analysis` | `opcloud source:569` | system map, informativeness, missing knowledge, AI requirements | `opcloud artifact:326` | `COVERED` | Conserva `Pistol`, `RGCN`, verification type, acceptance criteria y triplets. |
| `Data Import` | `opcloud source:636` | CSV import para atributos | `opcloud artifact:350` | `COVERED` | Reglas, restricciones y opciones recuperadas. |
| `Stereotypes` | `opcloud source:654` | stereotypes, global/org, removal options | `opcloud artifact:366` | `COVERED` | Sin gaps concretos. |
| `OPD3 Management` | `opcloud source:669` | search, hide/show, open, cut, remove, paste, drag | `opcloud artifact:378` | `COVERED` | Cobertura directa. |
| `Workflow Tips` | `opcloud source:685` | bring connected, multiple selection, alignment | `opcloud artifact:384` | `COVERED` | Cobertura directa. |
| `Summary` | `opcloud source:721` | cierre global del tutorial | `opcloud artifact:400` | `COVERED+JUSTIFIED` | El cierre fue recomprimido y ahora incluye una justificacion explicita de compresion. |

## Matriz B — ISO Primario

| Source family | Source ref | Fact set | Artifact ref | Estado | Nota |
| --- | --- | --- | --- | --- | --- |
| `Scope + Normative references + Conformance` | `opm-iso source:489`, `495`, `899` | alcance, ausencia de referencias normativas, niveles de conformidad | `opm-iso artifact:33` | `COVERED+COMPRESSED` | Todo el nucleo esta en `Scope and Conformance`. |
| `Terms and definitions` | `opm-iso source:499` | glosario ISO 3.x | `opm-iso artifact:49` | `COVERED+COMPRESSED` | El glosario completo queda absorbido como tabla recuperable. |
| `Symbols` | `opm-iso source:849` | shapes, contours, shadings, procedural/structural symbols | `opm-iso artifact:179` | `COVERED+COMPRESSED` | Visual notation consolidada sin gap detectado. |
| `OPM modelling principles` | `opm-iso source:923` | principios 6.1 | `opm-iso artifact:146` | `COVERED` | Cobertura directa. |
| `Fundamental concepts` | `opm-iso source:961` | bimodality, elements, context, realization | `opm-iso artifact:159` | `COVERED` | Cobertura directa. |
| `Thing syntax and semantics` | `opm-iso source:1042`, `1044`, `1062`, `1084` | objetos, procesos, generic properties | `opm-iso artifact:277` | `COVERED+COMPRESSED` | Familia repartida entre `Things` y `Object States`. |
| `Object states` | `opm-iso source:1084` | stateful/stateless, representation, initial/default/final, attribute values | `opm-iso artifact:314` | `COVERED` | Cobertura directa. |
| `Link overview + operational semantics` | `opm-iso source:1160`, `1182` | procedural overview, preprocess/postprocess semantics | `opm-iso artifact:338` | `COVERED+COMPRESSED` | Condensado en `Links Overview`. |
| `Transforming links` | `opm-iso source:1212`, `1214`, `1315` | consumption, result, effect, state-specified variants | `opm-iso artifact:367` | `COVERED+COMPRESSED` | Cobertura fuerte, resumida por familias. |
| `Enabling links` | `opm-iso source:1256`, `1456` | agent, instrument, state-specified enabling | `opm-iso artifact:397` | `COVERED+COMPRESSED` | Cobertura fuerte, resumida por familias. |
| `Control links: events` | `opm-iso source:1514`, `1662`, `1701` | event links y resúmenes tabulares | `opm-iso artifact:419` | `COVERED+COMPRESSED` | Cobertura por tipo, no por replica tabular literal. |
| `Control links: conditions + exceptions` | `opm-iso source:1787`, `1834`, `1899`, `1953` | condition links, state-specified condition links, overtime/undertime | `opm-iso artifact:455` | `COVERED+COMPRESSED` | Cobertura por familias y reglas. |
| `Invocation links` | `opm-iso source:1744` | invocation y self-invocation | `opm-iso artifact:503` | `COVERED` | Cobertura directa. |
| `Structural links` | `opm-iso source:2005`, `2013`, `2085`, `2404` | tagged, fundamental, state-specified structural relations | `opm-iso artifact:518` | `COVERED+COMPRESSED` | Cobertura adecuada. |
| `Relationship cardinalities` | `opm-iso source:2578`, `2625`, `2636`, `2700` | multiplicidad, optionality, value constraints | `opm-iso artifact:580` | `COVERED+COMPRESSED` | Cobertura adecuada. |
| `Logical operators` | `opm-iso source:2724` | AND, XOR, OR, probabilistic fans, path labels | `opm-iso artifact:615` | `COVERED+COMPRESSED` | Cobertura adecuada. |
| `Context management basics` | `opm-iso source:2865` | SD completion, refinement-abstraction mechanisms | `opm-iso artifact:703` | `COVERED` | Cobertura directa. |
| `Implicit invocation links summary` | `opm-iso source:3251` | Table 24 | `opm-iso artifact:725` | `COVERED` | Reincorporado con fila explicita de semantica estructural. |
| `Link distribution across context` | `opm-iso source:3262` | distributive semantics, invalid distributed consumption/result, Figure 50-51 | `opm-iso artifact:744` | `COVERED` | Ya incluye la distincion valida/invalida y las anclas a Figure 50-51. |
| `Split state-specified transforming links` | `opm-iso source:3329` | underspecification, Figure 52, Table 25 | `opm-iso artifact:756` | `COVERED` | Reincorporado con tabla resumen y ancla a Figure 52. |
| `Precedence during out-zooming` | `opm-iso source:3578` | semantic strength and precedence | `opm-iso artifact:777` | `COVERED` | Cobertura directa. |
| `OPD labels + Whole-system OPL` | `opm-iso source:3472`, `3516` | labels, refinement OPL, Table 26 whole-system OPL | `opm-iso artifact:793` | `COVERED` | Reincorporado el nucleo recuperable de Table 26. |
| `System Diagram procedure` | `opm-iso source:2819`, `2865` | five components, guided SD procedure | `opm-iso artifact:838` | `COVERED` | Cobertura directa. |
| `System type variants` | `opm-iso source:2819`, suplementado por `opm_youtube` | artificial, natural, social, socio-technical variants | `opm-iso artifact:889` | `COVERED+SUPPLEMENTED` | La tipologia queda enriquecida con corpus complementario. |
| `Decision nodes + conditional behaviour` | `opm-iso source:2724`, suplementado por `opm_youtube` | boolean nodes, skip vs wait, iteration | `opm-iso artifact:909` | `COVERED+SUPPLEMENTED` | Cobertura adecuada. |
| `MBSE` | `opm-iso source:3934` | MBSE, alternative concepts, PDR, virtual integration | `opm-iso artifact:933` | `COVERED` | Cobertura directa. |
| `OPL EBNF` | `opm-iso source:4264` | document structure, identifiers, sentence families | `opm-iso artifact:972`, `1016` | `COVERED` | Repartido en dos secciones para mantener chunking valido. |
| `OPM Metamodel + Annex C models` | `opm-iso source:5010`, `5693`, `5733`, `5782` | model hierarchy, basic constructs, C.19-C.21 | `opm-iso artifact:1096` | `COVERED` | Ya contiene `New-Diagram In-Zooming/Out-Zooming` y simplificacion OPD. |
| `Dynamics and simulation + Annex D examples` | `opm-iso source:6159` | D.5-D.8, concrete duration values, overtime/undertime cases | `opm-iso artifact:1157` | `COVERED` | Reincorporados valores `63.3`, `23.4`, `lambda=5.6` y referencias D.5-D.8. |
| `Guidance and naming conventions` | `opm-iso source:4891`, `5004` | best practices, naming, capitalization, thing importance | `opm-iso artifact:1210` | `COVERED` | Cobertura directa. |
| `Applied examples` | `opm-iso source:1334`, `3516`, suplementado por `opm_youtube` | steel rod, check-based paying, dish washing, safe opening, vehicle specialization, home safety, coffee, electric car | `opm-iso artifact:1252` | `COVERED+SUPPLEMENTED` | Los ejemplos oficiales y auxiliares quedan absorbidos. |

## Matriz C — Fuentes Complementarias Declaradas

| Source file | Source ref | Fact set | Artifact ref | Estado | Nota |
| --- | --- | --- | --- | --- | --- |
| `OPM version felix.md` | `felix:19`, `27`, `113`, `147`, `435` | overview operacional de OPM, glosario compacto, basics, syntax/semantics, modelling principles | `opm-iso artifact:33`, `49`, `159`, `277`, `338`, `1210` | `COVERED+SUPPLEMENTED` | Funciona como refuerzo y simplificacion del ISO; no quedaron gaps concretos detectados. |
| `opm_youtube.md` | `youtube:176`, `184`, `188`, `252`, `284`, `315`, `320`, `473`, `483`, `496`, `507` | air traffic, MOOC, conference, identity management, baggage, natural/social system framing | `opm-iso artifact:889`, `1252`, `1285` | `COVERED+SUPPLEMENTED` | Ejemplos auxiliares absorbidos explicitamente. |
| `opcloud-tutorial-videos.md` como fuente complementaria de `opm-iso` | `opcloud source:25` | referencia cruzada a procedimientos UI de OPCloud | `opm-iso artifact:1295` | `COVERED` | Queda como cross-reference a artefacto dedicado, evitando duplicacion. |

## Residuo

No se detectaron gaps factuales concretos remanentes en esta matriz por familias tematicas.

Lo unico que queda como tension abierta no es fidelidad sino densidad:

- `opcloud` queda bajo el umbral ideal de `CR > 1.5`, pero la excepcion esta explicitada y no se observaron perdidas factuales materiales.
- `opm-iso` queda significativamente mas denso que la fuente primaria y ya no muestra omisiones concretas detectables en esta auditoria.

## Limites del metodo

Esta auditoria:

- si verifica cobertura por familias tematicas recuperables;
- si verifica que residuos detectados anteriormente fueron cerrados;
- no demuestra equivalencia lexical o mapeo factico atomico automatizado para cada linea de `opm-iso.md`.

Para barra maxima, el siguiente nivel es una matriz atomica `fact_id -> source quote -> artifact location -> status`, probablemente generada con tooling dedicado.

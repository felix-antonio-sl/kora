---
_manifest:
  urn: "urn:fxsl:kb:xanpan-agents-metodologia"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-11"
    source: "xanpan-agents-v21-metodologia.md (source/fxsl/xanpan)"
version: "2.1.0"
status: draft
tags: [xanpan, agentes, metodologia, hcai, agile]
lang: es
extensions:
  fxsl:
    family: methodology
---

# XANPAN::AGENTS v2.1

Metodologia agil post-humana para desarrollo de software con enjambres de agentes IA gobernados por humanos. Base conceptual: Allan Kelly (`Xanpan`, `Continuous Digital`, `OKRs in Agile`, `User Stories`) + Human-Centered AI (Shneiderman, Xu y colaboradores). Fecha de referencia: febrero 2026.

## Tesis operativa e invariantes

**Unidad ejecutora** - el equipo deja de ser un conjunto de desarrolladores humanos; pasa a ser un enjambre de agentes IA especializados.

**Unidad de gobierno** - el Product Owner conserva casi intacto el dominio del `que` y `por que`; el Operador gobierna el `como` tecnico y la topologia del enjambre.

**Discontinuidad** - estimacion, sprint fijo, pair programming, retrospectiva emocional y staging como red de seguridad pierden fundamento mecanico cuando el ejecutor opera a velocidad de maquina.

**Invariantes heredados de Kelly**

- Cada historia debe entregar valor de negocio.
- Los OKRs siguen siendo la capa estrategica primaria.
- La calidad compensa su costo cuando se integra desde el inicio.
- El software sigue siendo un activo vivo, no un proyecto estatico.
- La visualizacion del trabajo sigue siendo condicion de aprendizaje.

**Conceptos que colapsan**

| Concepto clasico | Motivo de colapso | Reemplazo |
| --- | --- | --- |
| Story points / planning poker | medían esfuerzo humano, no costo de inferencia | costo por token, cycle time, tasa de aceptacion |
| Sprint fijo 1-2 semanas | la ejecucion se comprime a horas o minutos | Pulso adaptativo + Ciclo 4-6 semanas |
| Pair programming humano | los agentes no transfieren conocimiento socialmente | cross-eval entre agentes |
| Retrospectiva emocional | no hay moral ni friccion interpersonal en agentes | retrospectiva analitica |
| Staging como barrera principal | despliegue y rollback pueden comprimirse | evals + feature flags + canary + rollback |

**Conceptos emergentes**

- `Evals` como TDD organizacional anti-alucinacion.
- `Costo por token` como metrica economica primaria.
- `Context engineering` como disciplina de alto apalancamiento.
- `Enjambre auto-evolutivo` con agentes que optimizan prompts, evals y topologia.
- `Backlog predictivo` con propuestas proactivas del enjambre.
- `Gobernanza multi-nivel HCAI` como acelerador, no freno.
- `Modos de fallo + circuit breakers` como parte del contrato metodologico.

## Fundamento HCAI

### Cuadrante objetivo

Shneiderman: la meta no es elegir entre automatizacion y control humano. La meta es `alta automatizacion + alto control humano` en simultaneo. En Xanpan::Agents, mas autonomia del enjambre exige mas puntos de control estrategico humano.

### Metaforas HCAI y traduccion metodologica

| Metafora | Funcion | Traduccion en Xanpan::Agents |
| --- | --- | --- |
| `Supertools` | amplificar intencion humana | PO asistido por agentes-planificadores |
| `Tele-bots` | ejecucion remota con autoridad humana | agentes-coder bajo direccion del Operador |
| `Active Appliances` | autonomia en limites definidos | CI, evals, linting, deploy y observabilidad automatizada |
| `Control Centers` | orquestacion humana visible | tablero del Operador y dashboard del enjambre |

### Triangulo THE

| Vertice | Implementacion |
| --- | --- |
| Tecnologia | Model Router, context engineering, evals, CI/CD |
| Factores humanos | PO, Operador, intervenciones human-in-the-loop |
| Etica | clasificacion de riesgo, minimo privilegio, gobernanza multi-nivel, auditoria |

### Cuatro loops HCAI

| Loop | Alcance | Implementacion |
| --- | --- | --- |
| `Human-in-the-loop` | individuo-agente | PO acepta/rechaza historias; Operador aprueba acciones destructivas; override humano absoluto |
| `Organization-in-the-loop` | estrategia organizacional | OKRs, presupuesto de tokens, cultura de calidad, leadership escalation |
| `Ecosystem-in-the-loop` | sistemas IA interconectados | MCP, interoperabilidad, coordinacion con otros sistemas |
| `Society-in-the-loop` | impacto regulatorio y social | EU AI Act, NIST AI RMF, transparencia, impacto laboral |

### Modelo de madurez HCAI

| Nivel | Estado | Rasgos |
| --- | --- | --- |
| 1 | Ad Hoc | uso esporadico de agentes, sin evals formales, PO=Operador |
| 2 | Repetible | evals basicos en CI, tablero operativo, roles PO/Operador diferenciados |
| 3 | Definido | metodologia completa, context engineering formal, Model Router, metricas de costo/calidad |
| 4 | Gestionado | enjambre auto-evolutivo, backlog predictivo, despliegue continuo con evals robustos |
| 5 | Optimizante | meta-agentes optimizan metodologia y proponen OKRs |

## Roles humanos y ampliacion de capacidades

### Product Owner

**Capacidades amplificadas**

- captura de necesidades acelerada mediante agentes-analistas
- priorizacion asistida por metricas de producto y OKRs
- backlog predictivo como fuente de borradores de historias
- validacion instantanea de historias por testabilidad, claridad y dependencias

**Responsabilidades irreductibles**

- juicio de valor
- empatia con usuarios
- decision etica
- aceptacion final de historias

### Operador

**Capacidades amplificadas**

- mantenimiento de `CONVENTIONS.md`, `ARCHITECTURE.md`, `STACK.md` y archivos equivalentes
- definicion de topologia del enjambre: agentes, modelos, herramientas, permisos
- configuracion del `Model Router`
- monitoreo de alucinacion, costo, tool-calling y acceptance rate

**Responsabilidades irreductibles**

- aprobar acciones destructivas, deploy a produccion y comunicaciones externas
- aprobar cambios arquitectonicos
- aprobar cambios de modelo base o recalibraciones mayores
- conducir retrospectiva analitica con el PO

### Context hygiene y Sentinel

`Sentinel` surge como mantenedor de contexto:

1. detecta drift entre codebase y context files
2. propone diffs como PR
3. mantiene versionado estricto y trazable
4. verifica coherencia entre archivos de contexto al inicio de cada sesion

### Roles satelite

| Rol | Activacion | Aporte |
| --- | --- | --- |
| `Domain Expert` | historias con conocimiento especializado | valida supuestos y restricciones del dominio |
| `Compliance Officer` | historias regulatorias o legales | valida cumplimiento pre-analizado por agente |
| `UX Researcher` | cambios relevantes de experiencia usuaria | valida flujos y prototipos |
| `Security Analyst` | cambios criticos o con nueva superficie de ataque | revisa hallazgos del agente-security |
| `Stakeholder Rep` | revisiones de Ciclo o decisiones estrategicas | observa, pregunta y alinea con negocio |

Principio: consulta a demanda, no gate burocratico permanente.

## Historias de usuario, temporalidad y tablero

### Historia de usuario como contrato humano-agente

Una historia conserva la estructura de Kelly y agrega componentes necesarios para agentes:

| Elemento | Responsable | Funcion |
| --- | --- | --- |
| `Who/What/Why` | PO | valor y alcance |
| `Criterios de aceptacion` | PO + agente | definicion de hecho |
| `Clasificacion de riesgo` | Operador + agente | decide evals y nivel de autonomia |
| `Context bundle` | Operador | contexto operativo y tecnico cargado al enjambre |
| `Traza a OKR` | PO | anclaje estrategico |

Jerarquia operacional:

- `Epica` - agrupa capacidad de negocio
- `Historia` - unidad minima de valor verificable
- `Tarea` - subtrabajo que un agente o humano ejecuta

### Modelo temporal

| Escala | Reemplaza | Duracion | Funcion |
| --- | --- | --- | --- |
| `Pulso` | sprint mecanico | 3 dias a 2 semanas, adaptativo | revisar metricas, aceptar historias, recalibrar enjambre |
| `Ciclo` | trimestre agil comprimido | 4-6 semanas | ejecutar y evaluar OKRs |
| `Horizonte` | plan anual | continuo | direccion de largo plazo |

Notas:

- el Pulso se adapta a velocidad real del enjambre
- `deadline` deja de ser herramienta de presion; pasa a ser compromiso de valor y riesgo
- key results deben preferir señal analogica antes que binarios que inviten a Goodhart

### Tablero neural

Columnas funcionales:

- `propuesta`
- `lista`
- `en ejecucion`
- `verificacion`
- `lista para PO`
- `done`
- `rechazada`

Tarjetas:

| Color / tipo | Semantica |
| --- | --- |
| azul | historias de negocio con valor, escritas por PO |
| roja | bugs detectados por evals o reportados por usuarios |
| amarilla | trabajo no planificado pero necesario |
| verde | mejoras de proceso: refactoring, optimizacion de prompts, mejoras de evals |
| naranja | calibracion del enjambre: cambios de modelo, reindexacion, ajustes de context engineering |
| purpura | propuesta proactiva del enjambre / backlog predictivo |

Reglas:

- limites WIP aplican tambien a agentes
- el tablero es fuente operacional, no decoracion
- PO y Operador lo usan como superficie comun de negociacion

## Economia de tokens, calidad y OKRs

### Metricas que reemplazan velocidad

| Metrica | Semantica |
| --- | --- |
| `CpH` | costo por historia |
| `TA` | tasa de aceptacion |
| `Cycle Time` | tiempo desde inicio a aceptacion |

### Priorizacion por valor, no por esfuerzo

Formula operativa:

`Prioridad = Valor de Negocio / (Coste Estimado en Tokens x Multiplicador de Riesgo)`

El multiplicador de riesgo sube para historias destructivas o con alta probabilidad de alucinacion. La priorizacion deja de estimar esfuerzo humano y pasa a optimizar ROI por token invertido.

### Presupuesto de tokens por Ciclo

Cada Ciclo tiene presupuesto aprobado. Distribucion base:

- historias de negocio: `60-70%`
- BAU y bugs: `20-25%`
- calibracion del enjambre: `10-15%`

Regla: mirar numeros sin convertirlos en target ciego. Medir controla Goodhart; perseguir la metrica lo alimenta.

### Curva de coste decreciente

Supuesto operativo: la inferencia se abarata y la capacidad util aumenta con rapidez relativa. La metodologia explota esa tendencia, pero no la trata como ley fisica. Si la curva se aplana, entra el modo degradado de este documento.

### Calidad y escudo contra la alucinacion

| Practica | Traduccion post-humana |
| --- | --- |
| TDD | TDD + evals |
| code review | reviewer-agent + diversidad de modelos + aprobacion humana cuando corresponde |
| CI | necesario pero insuficiente |
| DoD | incluye evaluacion funcional, seguridad, costo y aceptacion humana |

`Evals` obligatorios:

- regresion
- alucinacion
- tool-calling
- costo
- seguridad
- adversarial periodico

### Definition of Done para agentes

Toda historia debe pasar este pipeline de completitud:

1. codigo generado con unit tests y cobertura sobre el umbral configurado
2. tests de aceptacion derivados de ACs pasan
3. lint y type checking pasan sin errores
4. eval de regresion pasa
5. eval de seguridad pasa
6. PR creado con descripcion clara y contexto suficiente
7. CI verde en la rama candidata
8. aceptacion humana final del PO u otro aprobador requerido por clasificacion de riesgo

### OKR-first

Regla de gobierno: backlog derivado de OKRs, no al reves.

Estructura de ciclo:

- `Objetivo` - cambio estrategico buscado
- `KR` - resultado medible
- `Historias` - unidades de ejecucion ligadas a KRs
- `BAU` - mantener luces encendidas sin fingir que es feature

BAU no se absorbe como residuo del backlog. Kelly lo trata como problema de gobierno; Xanpan::Agents adopta volverlo un Objetivo cero explicito del Ciclo. Reserva tipica: `20-30%` del presupuesto para bugs, soporte, deuda tecnica y mantenimiento.

Agentes pueden asistir en redaccion y propuesta de OKRs, pero la aprobacion sigue siendo humana.

## Arquitectura del enjambre y gobernanza operacional

### Roles de agentes

Familias recurrentes:

- planner / analyst
- coder
- reviewer
- tester / eval
- deployer
- observer
- security
- sentinel

### Conway invertido

La organizacion ya no diseña primero la estructura humana y luego la tecnica. Puede diseñar una topologia de agentes y dejar que la estructura humana de gobierno se acople a esa topologia.

### Model Router

Funcion:

- enrutar por complejidad, costo y riesgo
- degradar a modelos mas baratos cuando corresponde
- mantener diversidad entre autor y verificador
- impedir loops de costo descontrolado

### Enjambre auto-evolutivo

Capacidades esperadas:

- proponer mejoras a prompts
- ampliar o endurecer evals
- sugerir cambios de topologia
- detectar deuda en context engineering

Guardarrail central: `Sentinel` auditado. Pregunta obligatoria: `quis custodiet ipsos custodes?` Respuesta operacional: meta-eval del Sentinel, diversidad de modelos y aprobacion humana.

### Equipos ameba con agentes

La estructura puede dividirse y recomponerse dinamicamente segun dominio o producto. Los agentes permiten reorganizacion de alta frecuencia sin el costo de re-forming humano.

## Gobernanza HCAI y software longevo

### Human-in-the-loop: intervenciones humanas obligatorias

| Actor | Intervenciones no delegables |
| --- | --- |
| PO | aceptar/rechazar historias, priorizar, decidir tradeoffs de valor y etica |
| Operador | aprobar acciones destructivas, deploys de alto riesgo, cambios de arquitectura, cambios de modelo |
| Roles satelite | validar dominio, compliance, seguridad o UX cuando aplique |

### Human-in-the-loop: autonomia explicita del enjambre

Todo lo no listado arriba no queda abierto en abstracto. El perimetro autonomo definido es:

- descomposicion de historias en tareas
- generacion de codigo y tests
- ejecucion de CI/CD hasta staging
- refactoring continuo y tareas verdes
- generacion de PRs y documentacion
- eval automatico entre agentes con reviewer distinto al coder
- deploy a produccion con feature flags solo si hay evals robustos y rollback automatico configurado

### Organization-in-the-loop

La autonomia del enjambre no existe fuera de contexto organizacional:

- OKRs derivan de estrategia organizacional; no son autonomos
- presupuesto de tokens requiere aprobacion de liderazgo
- cultura de calidad se fija a nivel organizacional y se implementa via evals y context engineering
- adopcion de agentes exige rediseño de roles, procesos y escalacion; no basta con "agregar agentes" al proceso heredado

### Ecosystem-in-the-loop

El enjambre opera dentro de un ecosistema cognitivo mas amplio:

- MCP conecta agentes con herramientas y sistemas externos
- multiples enjambres o sistemas IA requieren coordinacion explicita
- interoperabilidad evita islas de automatizacion incompatibles

### Society-in-the-loop

El marco HCAI obliga a externalizar impacto mas alla del equipo:

- cumplimiento regulatorio: EU AI Act, NIST AI RMF, ISO/IEC 42001
- impacto laboral: transicion de desarrolladores humanos a roles de mayor valor o reskilling asistido
- transparencia y auditabilidad: cada decision del enjambre debe dejar traza demostrable

### Principio de minima intervencion maximal

El humano interviene solo donde hay juicio de valor, riesgo irreversible, degradacion del enjambre o implicancias organizacionales, ecosistemicas o sociales. Todo lo demas se automatiza de forma explicita, no ambigua.

### Digital continuo

Principios:

- el software se mantiene indefinidamente mientras siga generando valor
- agentes reducen el costo marginal de mantenimiento y modernizacion
- `producto`, no `proyecto`, es la unidad economica durable
- longevidad no implica inmortalidad: regulacion, ecosistema y obsolescencia siguen existiendo

## Observabilidad, retrospectiva y seguridad

### Observabilidad del enjambre

Dashboard operativo en cinco dimensiones:

| Dimension | Metricas | Frecuencia |
| --- | --- | --- |
| costo | tokens por Pulso, costo por historia, costo por KR, % presupuesto consumido | continua |
| calidad | tasa de aceptacion, tasa de alucinacion, cobertura de tests, scores de eval | por Pulso |
| velocidad | historias `done` por Pulso, cycle time promedio, throughput | por Pulso |
| modelo | tasa de exito por modelo, latencia promedio, frecuencia de fallback | continua |
| enjambre | utilizacion de agentes, WIP por zona, profundidad de cola, tarjetas purpura pendientes | continua |

### Retrospectiva analitica

Sustituye la retro emocional por una secuencia analitica:

1. revision de OKRs: que KRs se lograron y cuales no
2. analisis de costo: si se respeto el presupuesto de tokens y donde se concentro el gasto
3. analisis de calidad: patrones de rechazo, alucinaciones recurrentes, fallos de eval
4. decisiones de ajuste: modelos, context engineering, topologia
5. actualizacion de evals: nuevos casos nacidos de fallos observados
6. revision de tarjetas purpura pendientes del Sentinel
7. eval del Sentinel: si las propuestas aplicadas mejoraron metricas o no

### Seguridad y gobernanza multi-nivel

Controles base:

- minimo privilegio por agente
- aislamiento de ejecucion
- validacion estricta de output de agentes
- agent-to-agent prompt injection tratado como amenaza de primera clase
- governance HCAI multinivel como marco de decision

## Velocidad exponencial y modo degradado

### Hipotesis de trabajo

Supuesto operativo: entre 2024 y 2026 la capacidad de modelos, el contexto util y el tool use avanzan con apariencia exponencial. Esta observacion no se trata como ley fisica sino como hipotesis de diseño.

### Principios para absorber mejora rapida

1. Diseñar para el modelo de mañana, no solo el de hoy.
2. Automatizar la automatizacion.
3. Ship fast, eval faster, rollback instantaneo.
4. Tratar el backlog como flujo continuo.
5. Exigir que cada Ciclo sea mas eficiente que el anterior.

### Modo degradado si la exponencialidad se aplana

- Pulso vuelve a frecuencia fija
- presupuesto de tokens vuelve a gestion de escasez
- humanos recuperan mas tareas cognitivas complejas
- la mejora se desplaza a prompts, contexto y evals

## Modos de fallo y circuit breakers

### Alucinacion sistemica

| Riesgo | Circuit breakers |
| --- | --- |
| codigo y tests comparten el mismo error semantico | diversidad obligatoria de modelos, golden dataset humano, auditoria de muestra por PO |

### Bias en los evals

| Riesgo | Circuit breakers |
| --- | --- |
| evals no cubren omisiones o clases nuevas de error | meta-eval por Ciclo, evals adversariales, convertir incidentes en nuevos evals |

### Divergencia PO-Operador

| Riesgo | Circuit breakers |
| --- | --- |
| velocidad deseada por PO entra en conflicto con estabilidad perseguida por Operador | OKRs firmados por ambos, dashboard como SSOT, escalacion a liderazgo |

### Vulnerabilidad novel fuera de cobertura

| Riesgo | Circuit breakers |
| --- | --- |
| un patron de ataque no cubierto llega a produccion | minimo privilegio, observabilidad separada del enjambre, revision periodica por Security Analyst |

### Meseta de capacidad

| Riesgo | Circuit breakers |
| --- | --- |
| las mejoras de modelo dejan de sostener la metodologia | Pulso fijo, austeridad de tokens, expansion del rol humano, inversion extra en context/evals |

### Corrupcion de context engineering

| Riesgo | Circuit breakers |
| --- | --- |
| context files se contradicen o envejecen sin fallo discreto | Sentinel, git blame, correlacion de metricas con cambios de contexto |

## Modelo de transicion

### Regla

La transicion del equipo humano al enjambre no es `big bang`; es `pick'n'mix` gradual.

### Fases

| Fase | Ventana | Estado |
| --- | --- | --- |
| `Augmented Development` | semanas 1-4 | devs humanos usan agentes como copilotos; se observa que tareas delegan naturalmente |
| `Parallel Track` | semanas 5-12 | mini-enjambre atiende 3-5 historias de bajo riesgo mientras el equipo humano sigue operando |
| `Accelerated Adoption` | semanas 13-24 | evals y context engineering se formalizan; Operador se consolida; humanos migran a roles de mayor valor |
| `Swarm-First` | semana 25+ | el enjambre es mecanismo primario de ejecucion; humanos gobiernan valor, arquitectura y dominio |

### Destinos probables de desarrolladores humanos

- Operador de enjambre
- PO o domain expert
- arquitecto
- ingeniero de evals
- reubicacion con apoyo de reskilling cuando aplique

### Anti-patrones de transicion

- reemplazo total el lunes
- agentes hacen todo y humanos solo miran
- esperar evals perfectos antes de activar el enjambre
- conservar Scrum intacto y agregar agentes como "devs mas rapidos"

## Sintesis y axiomas

### Xanpan::Agents en una oracion

PO humano define `que` y `por que`; Operador humano configura y supervisa un enjambre IA que resuelve el `como`; roles satelite validan dominio y riesgo; la calidad se sostiene con evals, aprobacion humana y gobernanza HCAI multi-nivel.

### Correspondencia Kelly -> Xanpan::Agents v2.1

| Kelly / agile clasico | Xanpan::Agents |
| --- | --- |
| Sprint | Pulso adaptativo |
| OKR trimestral | Ciclo 4-6 semanas |
| Planning Poker | eliminado |
| velocidad | CpH + TA + Cycle Time |
| Pair programming | cross-eval entre agentes |
| Retrospectiva | retrospectiva analitica |
| Scrum Master | Operador |
| equipo desarrollador | enjambre auto-evolutivo + Sentinel |
| board estatico | tablero neural + tarjetas purpura |
| TDD | TDD + evals + seguridad + adversarial |
| backlog estatico | backlog predictivo y flujo continuo |
| staging | deploy con evals, canary y rollback |

### Doce axiomas

1. Humano define `que` y `por que`; agente resuelve `como`.
2. Toda historia debe entregar valor de negocio.
3. OKRs gobiernan; backlog deriva.
4. La calidad compensa su costo si se materializa en evals.
5. El costo de token es recurso escaso.
6. Human-in-the-loop para valor y riesgo; autonomia para lo demas.
7. El software es activo vivo y longevo.
8. Visualizar todo es obligatorio.
9. Medir evita Goodhart; perseguir metricas lo alimenta.
10. Alta automatizacion y alto control humano no son opuestos.
11. El enjambre puede auto-evolucionar solo bajo gobernanza humana.
12. Diseñar para la curva exponencial exige modo degradado.

## Apendice: Korvo-Korax como proof of concept

### El sistema personal como laboratorio

Korvo-Korax precede al documento. Fue laboratorio de friccion real para probar context engineering, heartbeats, supervision de meta-agente y backlog predictivo en escala `N=1`.

### Mapeo

| Concepto | Implementacion Korvo-Korax |
| --- | --- |
| Product Owner | Korvo |
| Operador | Korvo en modo dual-hat |
| Enjambre | Korax + subagentes |
| OKRs | GTD + revisiones semanales |
| Evals | invariantes PCA |
| Sentinel | heartbeats + deteccion de colapso |
| Tarjetas purpura | propuestas proactivas generadas en heartbeats |
| Context engineering | `AGENTS.md`, `SOUL.md`, `MEMORY.md` |
| Model Router | `sonnet -> gpt-5.2 -> kimi -> glm5` |
| Tablero neural | estado del workspace + metricas de sesion |

### Lecciones

1. Mantener contexto es trabajo cognitivo sustantivo.
2. Los heartbeats anticipan el patron del Sentinel.
3. La diversidad de modelos reduce blind spots.
4. El backlog predictivo emerge cuando el contexto es suficiente.
5. La curva de capacidad se siente en saltos, no en linea recta.

### La violacion consciente: dual-hat PO/Operador

La implementacion personal viola deliberadamente la separacion de concerns que el §2 propone: Korvo es simultaneamente PO y Operador. Esa violacion tiene consecuencias predecibles:

- sesgo de confirmacion amplificado: quien define valor tambien configura al ejecutor
- fatiga atencional compuesta: context engineering, evaluacion de entregas y definicion de valor consumen la misma atencion humana
- PCA como compensador: el Protocol de Coherencia Atencional compensa la falta de separacion, detecta drift y fuerza coherencia

### Limitaciones del proof of concept

- N=1: un sistema personal no demuestra escalabilidad a equipos con multiples humanos
- sin separacion real PO/Operador: el dual-hat impide validar independencia de roles
- sin metricas formales instrumentadas: `CpH`, `TA` y `Cycle Time` observados de forma cualitativa, no instrumentada
- posible survivor bias: lo que funciona se recuerda mejor que lo descartado o fallido

Funcion del apendice: documentar que varias ideas de la metodologia emergieron de practica real antes de formalizarse. La teoria siguio a la experiencia, no al reves.

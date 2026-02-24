---
_manifest:
  urn: "urn:fxsl:kb:xanpan-agents-metodologia"
  provenance:
    created_by: "FS"
    created_at: "2026-02-24"
    source: "source/fxsl/xanpan/xanpan-agents-v21-metodologia.md"
version: "2.1.0"
status: published
tags: [xanpan, agentes, metodologia, hcai, okrs, enjambre, gobernanza, sentinel, evals]
lang: es
---

# Xanpan::Agents --- Metodologia de Desarrollo Agil Post-Humano v2.1.0

## 1. Manifiesto y Premisa

Xanpan::Agents v2.1 reconstruye el desarrollo agil desde la base semantica de que significa desarrollar software cuando los ejecutores cambian de especie cognitiva. Donde el agile clasico tenia 5-8 desarrolladores humanos, ahora hay un **enjambre de agentes IA**. Donde habia un Scrum Master, ahora hay un **Operador** orquestando topologias de modelos. El unico rol que sobrevive casi intacto es el **Product Owner**: la conciencia humana que define QUE construir y POR QUE.

Basado en los marcos de Allan Kelly (Xanpan, Continuous Digital, OKRs in Agile, User Stories) y fundamentado en Human-Centered AI (HCAI) de Shneiderman, Xu, et al.

### 1.1 Lo que permanece invariante

Los principios de Kelly que son verdades sobre la naturaleza del software y del valor --- no sobre la naturaleza del desarrollador --- sobreviven intactos:

- **Cada historia DEBE entregar valor de negocio.** Kelly: una user story sin beneficio de negocio no tiene razon de existir. Los agentes ejecutan mas rapido, pero ejecutar rapido algo sin valor es destruir recursos mas rapido.
- **OKRs como gobernanza estrategica.** Kelly: escribir OKRs trimestrales es fundamentalmente una pregunta de estrategia. Los agentes necesitan direccion mas que nunca; sin OKRs, un enjambre es una fuerza sin vector.
- **La calidad es gratis si inviertes en ella.** Crosby/Kelly: Quality is free. Con agentes, se amplifica: TDD, linting, evals no tienen coste cognitivo. El escudo contra la alucinacion es barato si se integra desde el dia cero.
- **Software como activo vivo.** Kelly/Continuous Digital: el software no puede ser un activo estatico; se degrada porque el mundo cambia. Con agentes, la inversion continua se vuelve economicamente trivial.
- **Visualizar todo.** Kelly: si no podemos ver, no podemos aprender. El tablero es el sistema nervioso. Con agentes, se convierte en dashboard en tiempo real.

### 1.2 Lo que colapsa

Conceptos que fueron respuestas a limitaciones humanas y que pierden su razon de ser mecanica:

| Concepto colapsado | Razon |
|---|---|
| Estimacion basada en esfuerzo humano (planning poker, story points, velocidad en puntos/sprint) | Media capacidad cognitiva humana. Los agentes no tienen dias buenos ni malos. El coste es predecible en tokens. |
| Iteraciones de 1-2 semanas como unidad temporal | Cuando un agente implementa una historia en minutos, la iteracion de dos semanas pierde su razon mecanica. El ritmo es continuo. |
| Pair programming como practica social | Era herramienta de calidad + transferencia de conocimiento entre humanos. Los agentes comparten conocimiento via context engineering. |
| Retrospectivas como reflexion emocional | Los agentes no experimentan frustracion ni conflicto interpersonal. La retro se transforma en analisis operacional puro. |

### 1.3 Lo que emerge

Conceptos nuevos que no tenian equivalente en equipos humanos:

- **Evaluacion continua (Evals) como TDD organizacional.** Verificar que los agentes no alucinan, no regresan, mantienen calidad. Es la practica tecnica obligatoria de esta era.
- **Coste por token como metrica de eficiencia.** Reemplaza la velocidad en puntos. Cuantificable, comparable, directamente vinculado a valor economico.
- **Context engineering como disciplina.** La ventana de contexto del LLM es el recurso mas escaso y valioso. Gestionarlo es la nueva competencia.
- **Enjambre auto-evolutivo.** Los agentes optimizan sus propios prompts, proponen mejoras a sus evals y sugieren reconfiguraciones de topologia. El enjambre aprende.
- **Backlog predictivo.** Los agentes analizan patrones de uso, metricas de producto y OKRs para proponer historias antes de que el PO las escriba. El PO pasa de escribir historias a curar y aprobar propuestas.
- **Despliegue continuo sin staging.** Con evals suficientemente robustos y feature flags, el concepto de ambiente de staging se comprime. Ship fast, eval faster, rollback instantaneo.
- **Gobernanza multi-nivel HCAI.** Humano-en-el-loop, Organizacion-en-el-loop, Ecosistema-en-el-loop, Sociedad-en-el-loop. Marcos de Shneiderman y Xu integrados como estructura de seguridad que habilita velocidad.
- **Modos de fallo y circuit breakers.** El happy path no es suficiente. La metodologia incluye patrones explicitos de degradacion, contencion y recuperacion ante fallos sistemicos del enjambre.

> **PRINCIPIO DE DISCONTINUIDAD:** No estamos optimizando el proceso existente. Cuando cambias la especie del ejecutor, cada concepto agil debe ser reconstruido desde sus axiomas. Estimacion, velocidad, iteracion, pair programming, retrospectiva, planning poker: todos nacieron como respuestas a limitaciones humanas. Cuando esas limitaciones desaparecen, las respuestas deben transformarse o morir.

---

## 2. Definiciones

La tabla **DEBE** incluir todo termino clave con significado preciso dentro de este documento:

| Termino | Definicion |
|---|---|
| **Product Owner (PO)** | Rol humano que define QUE construir y POR QUE. Decide valor de negocio, prioriza backlog, acepta/rechaza entregas. |
| **Operador** | Rol humano que configura, calibra y optimiza el enjambre de agentes. Ingeniero de sistemas inteligentes. |
| **Enjambre** | Conjunto de agentes IA especializados que ejecutan el desarrollo de software bajo gobernanza humana. |
| **Sentinel** | Meta-agente que monitorea al enjambre, propone optimizaciones de prompts, evals y topologia, y mantiene context hygiene. No puede ejecutar cambios sin aprobacion humana. |
| **Pulso** | Iteracion de gobernanza humana (adaptativa, 3 dias a 2 semanas). Reemplaza al sprint. |
| **Ciclo** | Periodo operacional de OKRs (4-6 semanas). Reemplaza al trimestre clasico. |
| **Horizonte** | Roadmap estrategico anual. Alineacion con Continuous Digital de Kelly. |
| **Tablero Neural** | Dashboard en tiempo real que visualiza historias, agentes y metricas del enjambre. Reemplaza al tablero de post-its. |
| **Coste por Historia (CpH)** | Tokens consumidos por historia completada y aceptada. Reemplaza velocidad en puntos/sprint. |
| **Tasa de Aceptacion (TA)** | Porcentaje de historias aceptadas por PO al primer intento. Metrica de calidad. |
| **Cycle Time** | Tiempo desde Backlog hasta Done para una historia. |
| **Eval** | Evaluacion automatizada que verifica calidad, seguridad, regresion, alucinacion o coste de un output de agente. |
| **LLM-as-a-Judge** | Patron donde un modelo de un provider distinto al generador evalua la calidad del output. |
| **Model Router** | Sistema de enrutamiento que asigna cada tarea al tier de modelo optimo por coste/capacidad. |
| **Tier de modelo** | Clasificacion de modelos por coste/capacidad: T1 (Economico), T2 (Balance), T3 (Frontier), T4 (Reasoning). |
| **Context engineering** | Disciplina de disenar, crear y mantener los artefactos que alimentan la ventana de contexto del LLM. |
| **Backlog predictivo** | Mecanismo donde los agentes proponen historias basadas en patrones detectados en metricas, uso y OKRs. El PO cura y aprueba. |
| **Tarjeta purpura** | Propuesta auto-generada por el enjambre (Sentinel) para mejora del sistema. Requiere aprobacion humana. |
| **Feature flag** | Mecanismo de activacion/desactivacion de funcionalidad en produccion sin redespliegue. Habilita deploy continuo sin staging. |
| **Golden dataset** | Subset de evals con respuestas correctas escritas por humanos, no generadas por agentes. Ancla contra drift sistemico. |
| **Circuit breaker** | Mecanismo de contencion automatica que detiene o degrada una operacion cuando se detecta un modo de fallo. |
| **Dual-hat** | Modo donde una persona ocupa simultaneamente los roles de PO y Operador. Requiere disciplina de alternancia explicita. |
| **Rol satelite** | Interfaz humana especializada (domain expert, compliance officer, UX researcher, security analyst) que el enjambre consulta a demanda. |
| **HCAI** | Human-Centered Artificial Intelligence. Marco de Shneiderman y Xu que demuestra que automatizacion y control humano son dimensiones independientes, no extremos de un espectro. |
| **Trianguolo THE** | Marco de Xu: Tecnologia-Factores Humanos-Etica. Toda solucion IA viable reside en la zona de integracion optima de las tres perspectivas. |
| **Korvo-Korax** | Sistema personal que implementa los patrones del corpus a escala minima. Proof of concept de la metodologia. |
| **OKR** | Objectives and Key Results. Mecanismo de alineacion estrategia-ejecucion. Adoptado en modalidad OKR-first. |
| **BAU** | Business As Usual. Trabajo operativo continuo (bugs, soporte, deuda tecnica, mantenimiento). |
| **PCA** | Pensamiento Ciclico Asincrono. Estructura temporal con ciclos y flujo continuo. |
| **Conway Invertido** | Principio donde la estructura del software dicta la topologia del enjambre (inversion de la Ley de Conway clasica). |
| **DoD** | Definition of Done. Pipeline de verificacion que toda historia **DEBE** completar. |
| **Senal de complejidad** | Clasificacion de una historia: simple, estandar, complejo, critico. Determina tier de modelo via Model Router. |
| **Clasificacion de riesgo** | Clasificacion de una historia: lectura, escritura, destructiva. Determina si requiere aprobacion humana pre-ejecucion. |

---

## 3. Fundamento Filosofico: HCAI como Acelerador

La mayoria de las metodologias ven la gobernanza como un freno. Xanpan::Agents la ve como un acelerador. Esta paradoja se resuelve con el marco de Human-Centered Artificial Intelligence (HCAI).

### 3.1 El insight de Shneiderman: no hay trade-off

El marco bidimensional de Shneiderman (2020) demuestra que automatizacion y control humano no son extremos de un espectro. Son dimensiones independientes. El cuadrante objetivo de HCAI es el superior derecho: ALTA automatizacion Y ALTO control humano simultaneamente.

> **PRINCIPIO HCAI:** La autonomia total del enjambre en la ejecucion tecnica es posible PORQUE existe gobernanza humana total en los nodos estrategicos. No es a pesar de la gobernanza. Es gracias a ella. Cuanto mas robusto el marco de control, mas agresiva puede ser la autonomia.

**Correcto:** `Mas autonomia de agentes + mas puntos de control estrategico = mejor resultado que cualquiera por separado.`
**Incorrecto:** `Mas autonomia de agentes = menos control humano. (Falso dilema refutado por Shneiderman.)`

### 3.2 Las cuatro metaforas de diseno

Shneiderman propone cuatro metaforas para sistemas IA. Cada una **DEBE** tener una manifestacion concreta en el enjambre:

| Metafora HCAI | Manifestacion en Xanpan::Agents |
|---|---|
| **Supertools** | El PO usa agentes-planificadores como superherramientas que amplifican su capacidad de definir y refinar historias |
| **Tele-bots** | Agentes-coder como efectores remotos: ejecutan codigo bajo la direccion estrategica del Operador, con feedback continuo |
| **Active Appliances** | Agentes de CI/CD, linting, eval: operan autonomamente dentro de limites estrictos configurados |
| **Control Centers** | El dashboard del Operador: centro de control que orquesta el enjambre con visibilidad total y capacidad de intervencion |

### 3.3 El Triangulo THE de Xu

Wei Xu (2019) propone el Triangulo Tecnologia-Factores Humanos-Etica (THE): toda solucion IA viable reside en la zona de integracion optima donde las tres perspectivas se solapan.

En Xanpan::Agents, el Triangulo THE se operacionaliza asi:

- **Tecnologia:** Model Router, context engineering, evals, CI/CD. El stack tecnico que habilita la ejecucion.
- **Factores Humanos:** El PO como conciencia de valor, el Operador como ingeniero de enjambre, los puntos de intervencion human-in-the-loop.
- **Etica:** Clasificacion de riesgo por historia, principio de minimo privilegio por agente, gobernanza multi-nivel, auditoria continua.

### 3.4 HCAI Jerarquico: los cuatro loops

Xu y Gao (2025) extienden HCAI a un modelo multi-nivel: hHCAI (Hierarchical Human-Centered AI). Cuatro niveles de gobernanza, cada uno con su loop de control:

| Loop HCAI | Alcance | Implementacion en Xanpan::Agents |
|---|---|---|
| **Human-in-the-loop** | Interaccion individuo-agente | PO acepta/rechaza historias. Operador aprueba acciones destructivas. Override absoluto. |
| **Organization-in-the-loop** | Contexto organizacional | OKRs alinean enjambre con estrategia organizacional. Presupuesto de tokens aprobado por liderazgo. |
| **Ecosystem-in-the-loop** | Multiples sistemas IA interconectados | Interoperabilidad via MCP. Coordinacion con otros sistemas IA. |
| **Society-in-the-loop** | Impacto macrosocial | Cumplimiento regulatorio (EU AI Act, NIST AI RMF). Consideracion de impacto laboral. Transparencia y auditabilidad. |

La implementacion detallada de cada loop se prescribe en [-> 12. Human-in-the-Loop: Loops de Gobernanza HCAI].

### 3.5 Modelo de Madurez HCAI

Winby y Xu (2025) proponen cinco niveles de madurez organizacional HCAI. Adaptados a Xanpan::Agents:

| Nivel | Estado | Caracteristicas |
|---|---|---|
| **1 - Ad Hoc** | Exploracion | Uso esporadico de agentes. Sin evals formales. Sin OKRs de enjambre. PO y Operador son la misma persona. |
| **2 - Repetible** | Adopcion inicial | Evals basicos en CI. Board implementado. PO y Operador diferenciados. Historias con criterios de aceptacion. |
| **3 - Definido** | Estandarizado | Metodologia completa adoptada. Context engineering formalizado. Model Router activo. Metricas de coste y calidad rastreadas. |
| **4 - Gestionado** | Optimizado | Enjambre auto-evolutivo activo. Backlog predictivo operando. Despliegue continuo con evals robustos. Analisis retrospectivo data-driven. |
| **5 - Optimizante** | Trascendente | El enjambre propone OKRs. Meta-agentes optimizan la metodologia misma. Sistema inteligente humano-IA integrado. |

> **POR QUE HCAI ACELERA EN VEZ DE FRENAR:** Sin gobernanza, cada decision requiere deliberacion ad hoc. Con gobernanza estructurada, las decisiones estan pre-tomadas: el agente SABE que puede hacer autonomamente y que requiere aprobacion. No hay ambiguedad. No hay paralizacion. La gobernanza es el pre-calculo que elimina friccion en runtime. Mas estructura = mas velocidad.

---

## 4. Roles Humanos

HCAI insiste: la IA **DEBE** aumentar y empoderar las capacidades humanas, no sustituirlas. En Xanpan::Agents, los humanos del sistema son superhumanos operando con capacidades amplificadas por el enjambre.

### 4.1 Product Owner: El Super-PO

#### Capacidades amplificadas por el enjambre

- **Captura de necesidades acelerada:** El PO habla con clientes y stakeholders. Un agente-analista transcribe, sintetiza y propone borradores de historias en formato Who/What/Why con criterios de aceptacion sugeridos. El PO refina en minutos.
- **Priorizacion asistida por datos:** Agentes-analistas cruzan metricas de producto, patrones de uso y OKRs para sugerir prioridades. El PO decide informado.
- **Backlog predictivo:** Agentes proponen historias basadas en patrones detectados. El PO pasa de ESCRIBIR historias a CURAR y APROBAR propuestas.
- **Validacion instantanea:** Cuando el PO escribe una historia, un agente la analiza inmediatamente: testabilidad, criterios de aceptacion, dependencias, cuantificacion de valor. Feedback en segundos.

#### Responsabilidades irreductiblemente humanas

El PO **DEBE** retener estas funciones sin delegacion a agentes:

- **Juicio de valor:** Esta feature sirve a nuestros usuarios reales? Alinea con nuestra vision? Los agentes optimizan; los humanos deciden QUE optimizar.
- **Empatia con el usuario:** Entender dolor, frustracion, deseo. Los agentes procesan datos de uso; el PO entiende personas.
- **Decision etica:** Deberiamos construir esto aunque podamos? El PO es el gatekeeper etico del producto.
- **Aceptacion final:** Cada historia completada **DEBE** pasar por aprobacion humana del PO. Sin excepciones. Nucleo del human-in-the-loop de HCAI.

### 4.2 Operador: El Ingeniero de Enjambre

#### Capacidades amplificadas

- **Context engineering:** Mantiene los archivos CONVENTIONS.md, ARCHITECTURE.md, STACK.md que alimentan a los agentes. Equivalente al modelo mental compartido de Kelly, pero externalizado y versionado.
- **Topologia de enjambre:** Define que agentes participan, con que modelos, que herramientas disponibles, que permisos. Puede reconfigurar en minutos sin forming-storming.
- **Model Router:** Configura routing de tareas al modelo optimo por coste/capacidad. Optimiza la economia de tokens del enjambre.
- **Monitor de calidad:** Observa metricas del enjambre: tasa de alucinacion, tasa de exito de tool-calling, coste por historia, acceptance rate. Interviene cuando detecta degradacion.

#### Responsabilidades irreductiblemente humanas

El Operador **DEBE** retener estas funciones sin delegacion a agentes:

- **Aprobacion de acciones destructivas:** Delete de datos, deploy a produccion, comunicaciones externas: **DEBEN** requerir aprobacion explicita del Operador.
- **Cambios arquitectonicos:** Decisiones que afectan la estructura fundamental del sistema.
- **Actualizaciones de modelo:** Cambiar el modelo base de un agente **DEBE** requerir evals de regresion y aprobacion del Operador.
- **Retrospectiva analitica:** Conduce el analisis periodico de rendimiento del enjambre con el PO.

#### Context hygiene: el Sentinel como mantenedor

El context engineering es trabajo cognitivo significativo. La solucion: el Sentinel mantiene context files y el Operador solo aprueba diffs.

Modelo de context hygiene:

1. **Deteccion automatica de drift:** El Sentinel **DEBE** comparar el estado real del codebase con lo declarado en ARCHITECTURE.md y CONVENTIONS.md. Cuando detecta divergencia, genera un diff propuesto.
2. **Actualizacion propuesta como PR:** El diff al context file se presenta como PR con justificacion. El Operador revisa y aprueba/ajusta.
3. **Versionado estricto:** Los context files **DEBEN** estar en git. Cada cambio tiene autor (Sentinel o Operador), timestamp y justificacion.
4. **Validacion cruzada:** Al inicio de cada sesion de agente, un check **DEBE** verificar que los context files son coherentes entre si y con el codebase real. Incoherencia = alerta al Operador.

### 4.3 Roles Satelite

Los roles satelite **NO** son miembros permanentes del equipo. Son interfaces humanas que el enjambre consulta a demanda, amplificadas por agentes especializados:

| Rol satelite | Cuando se activa | Como interactua con el enjambre |
|---|---|---|
| **Domain Expert** | Historias que requieren conocimiento especializado | Un agente-analista prepara briefing del contexto tecnico; el expert valida supuestos y restricciones de dominio |
| **Compliance Officer** | Historias clasificadas como regulatorias o con impacto legal | Agente-compliance pre-analiza contra marco regulatorio conocido; el officer valida y firma |
| **UX Researcher** | Historias que afectan experiencia de usuario | Agente genera prototipos o flujos; el researcher valida contra investigacion de usuarios reales |
| **Security Analyst** | Historias clasificadas como criticas o con superficie de ataque | Agente-security ejecuta analisis estatico/dinamico; el analyst revisa hallazgos y autoriza |
| **Stakeholder Rep** | Revisiones de Ciclo o decisiones estrategicas | Asiste a Retrospectiva Analitica como observador con voz; recibe reportes generados por agente-analyst |

Los roles satelite **DEBEN** seguir el patron HCAI de Supertools: el agente prepara, analiza y sintetiza; el humano especialista juzga, valida y decide.

**Correcto:** `Consulta a demanda: si una historia no tiene clasificacion regulatoria, el Compliance Officer nunca la ve.`
**Incorrecto:** `Gate burocratico: toda historia pasa por aprobacion del Compliance Officer aunque no tenga impacto legal.`

### 4.4 Modo dual-hat (equipos pequenos)

En equipos pequenos o individuales, una persona **PUEDE** ocupar multiples roles. El caso extremo es el operador-PO individual (ver [-> 20. Apendice: Korvo-Korax]).

El Operador Solitario **DEBE** alternar sombreros explicitamente:

- **Sombrero PO:** Al inicio de cada ciclo de trabajo, al definir que historias abordar, al decidir si un feature ship o necesita mas iteracion, al hablar con usuarios o stakeholders.
- **Sombrero Operador:** Al configurar herramientas, al interactuar con agentes LLM, al resolver problemas tecnicos, al optimizar prompts, al gestionar infraestructura.

El Operador Solitario **NO DEBE** mezclar sombreros en la misma sesion de trabajo.

**Correcto:** `Iniciar el ciclo con sombrero PO seleccionando historias por valor de negocio, luego cambiar a sombrero Operador para implementarlas.`
**Incorrecto:** `Decidir que construir y como construirlo en la misma conversacion mental, sin separacion explicita de roles.`

---

## 5. User Stories: Contrato Humano-Agente

La historia de usuario sobrevive como mecanismo central de captura de requisitos (Kelly: una user story es un placeholder para una conversacion, y cada historia tiene beneficio de negocio). Lo que cambia: la naturaleza de la conversacion y la velocidad de resolucion.

### 5.1 Anatomia de una historia

Toda historia **DEBE** contener cinco elementos:

| Elemento | Origen | Responsable | Descripcion |
|---|---|---|---|
| **Who/What/Why** | Kelly | PO | Formato clasico: "Como [usuario], quiero [funcionalidad], para [beneficio]" |
| **Criterios de aceptacion** | Kelly | PO + Agente | Condiciones testables que definen "hecho." El agente sugiere; el PO aprueba. |
| **Valor de negocio (puntos)** | Kelly | PO | Estimacion abstracta de valor asignada por PO. |
| **Senal de complejidad** | Nuevo | Operador/Auto | simple, estandar, complejo, critico. Determina tier de modelo via Model Router. |
| **Clasificacion de riesgo** | Nuevo | Operador/Auto | lectura, escritura, destructiva. Determina si requiere aprobacion humana pre-ejecucion. |

### 5.2 La conversacion humano-agente

En Xanpan::Agents, la conversacion es instantanea y continua:

1. PO escribe historia + criterios de aceptacion. **PUEDE** ser borrador imperfecto.
2. Agente analiza y hace preguntas clarificadoras inmediatamente.
3. PO refina en ciclos cortos. La conversacion de clarificacion que en Scrum toma dias, aqui toma minutos.
4. Agente genera plan de implementacion antes de escribir codigo. PO u Operador **DEBEN** aprobar el plan.
5. Ejecucion con feedback continuo. El agente **PUEDE** pedir clarificacion mid-flight si encuentra ambiguedad.

### 5.3 Jerarquia: Epicas, Historias, Tareas

La jerarquia de Kelly se preserva pero las fronteras se comprimen:

- **Epicas:** Objetivos de negocio que mapean directamente a Key Results de OKR. Demasiado grandes para un ciclo de ejecucion de agente. Escritas por PO.
- **Historias:** Unidades de valor entregable. Cada una con beneficio de negocio independiente y criterios de aceptacion testables. Un agente **PUEDE** consumir una historia en minutos a horas, no dias.
- **Tareas:** Auto-generadas por el agente al descomponer la historia. El humano **NO DEBE** escribir tareas. El agente planifica su propia descomposicion.

> **CUELLO DE BOTELLA INVERTIDO:** Los agentes pueden consumir el backlog mas rapido de lo que el PO puede nutrirlo. El cuello de botella se invierte: ya no es la velocidad de desarrollo sino la velocidad de definicion de valor por el humano. El backlog predictivo es la solucion a esta inversion.

---

## 6. Modelo Temporal: Del Sprint al Flujo Continuo

Kelly tiene razon: los humanos necesitan ritmo. Los agentes no, pero los humanos que gobiernan el proceso SI. La cadencia no desaparece; se transforma y se comprime.

### 6.1 Tres escalas temporales simultaneas

El modelo temporal de Xanpan::Agents **DEBE** operar en tres frecuencias:

#### Pulso (reemplaza al Sprint): adaptativo

El Pulso **NO** es una iteracion de desarrollo. Es una iteracion de gobernanza humana. Durante el periodo entre Pulsos, los agentes ejecutan historias continuamente. El Pulso es el momento donde los humanos:

- Revisan entregas y aceptan/rechazan contra criterios de aceptacion.
- Re-priorizan backlog basado en aprendizaje.
- Refinan historias pendientes en conversaciones humano-agente.
- Revisan metricas del enjambre (coste, calidad, rendimiento).
- Deciden si rotar, escalar o reducir agentes.

**Duracion adaptativa:** El Pulso por defecto es 1 semana. Si las metricas del enjambre son estables y el acceptance rate es >90%, **PUEDE** extenderse a 2 semanas. Si hay degradacion o lanzamiento critico, **PUEDE** comprimirse a 2-3 dias. El ritmo se adapta a la realidad.

**Correcto:** `Pulso de 3 dias ante degradacion de metricas del enjambre para intervenir rapidamente.`
**Incorrecto:** `Sprint fijo de 2 semanas aunque el acceptance rate haya caido al 50% y se necesite intervencion inmediata.`

#### Ciclo (reemplaza al Trimestre): 4-6 semanas

Periodo operacional de OKRs. Kelly recomienda OKRs trimestrales; Xanpan::Agents comprime a 4-6 semanas porque la velocidad de ejecucion permite iterar sobre objetivos mas rapidamente. Cada Ciclo **DEBE** comenzar con sesion de planificacion estrategica donde PO y Operador:

1. Revisan OKRs del Ciclo anterior (% KRs logrados, lecciones aprendidas).
2. Definen 1-3 Objetivos para el proximo Ciclo con Key Results medibles y preferiblemente analogos.
3. Derivan epicas necesarias para lograr cada KR.
4. Descomponen epicas en historias con soporte de agente-planificador.

#### Horizonte (ano): Continuo

Roadmap estrategico y OKRs anuales. Alineacion con el modelo Continuous Digital de Kelly. El enjambre opera siempre; no hay fin de proyecto.

### 6.2 Analogo mayor que Binario en Key Results

Siguiendo a Kelly, los Key Results **DEBERIAN** plantearse como declaraciones analogas, no binarias. Esto permite a los agentes entregar progreso parcial valioso en vez de perseguir objetivos todo-o-nada.

**Correcto:** `KR: Reducir tiempo de respuesta de 2s a menos de 500ms. (Permite celebrar llegar a 800ms en camino a 500ms.)`
**Incorrecto:** `KR: Implementar nuevo sistema de cache. (Binario: se hizo o no se hizo. Sin gradiente.)`

### 6.3 La muerte del deadline como fuente de estres

Con agentes, los deadlines cambian de naturaleza: ya no son fechas de entrega que generan estres en humanos. Son **horizontes de evaluacion**: momentos predefinidos donde los humanos evaluan progreso contra KRs y deciden si pivotar.

---

## 7. El Tablero Neural

Kelly insiste: si no podemos ver, no podemos aprender. Cada equipo **DEBE** disenar su propio tablero. En Xanpan::Agents, el tablero estatico de post-its evoluciona a un dashboard neural en tiempo real.

### 7.1 Columnas del flujo

Todo Tablero Neural **DEBE** contener al menos estas columnas:

| Columna | Descripcion | Velocidad tipica |
|---|---|---|
| **Backlog** | Historias priorizadas por valor de negocio, alimentadas por PO y backlog predictivo | Continua |
| **Refinamiento** | Conversacion humano-agente activa para clarificar criterios | Minutos |
| **Agent:Working** | Historia en ejecucion activa por agentes. WIP controlado. | Minutos a horas |
| **Agent:Review** | Entregable completado, pasando eval automatico (tests, lint, evals) | Segundos a minutos |
| **Human:Approval** | Paso eval automatico, espera aceptacion del PO | Horas (Pulso) |
| **Done** | Aceptada y desplegada o lista para despliegue | Terminal |
| **Rejected** | Rechazada por PO o fallo eval. Retorna a Refinamiento con feedback. | Retroceso |
| **Unplanned** | Trabajo emergente: bugs, urgencias. Kelly acepta que es inevitable y valioso. | Variable |

### 7.2 Tarjetas por color

| Color | Tipo | Responsable |
|---|---|---|
| **Azul** | Historias de negocio con valor | PO |
| **Rojo** | Bugs. Los agentes auto-detectan algunos via evals; otros reportados por usuarios | Automatico/PO |
| **Amarillo** | Trabajo no planificado. Kelly acepta que es inevitable e incluso valioso | Variable |
| **Verde** | Mejoras de proceso: refactoring, optimizacion de prompts, mejoras de evals | Operador |
| **Naranja** | Calibracion del enjambre: actualizaciones de modelo, re-indexacion de embeddings, ajustes de context engineering | Operador |
| **Purpura** | Tareas auto-propuestas por el enjambre. El Sentinel genera tarjetas purpura cuando detecta oportunidades de mejora. **DEBEN** requerir aprobacion del Operador. | Sentinel |

### 7.3 Limites WIP para agentes

Los agentes **PUEDEN** ejecutar en paralelo, pero el WIP sigue importando por dos razones:

- **Coste:** Cada agente ejecutando consume tokens; mas paralelismo = mas coste instantaneo.
- **Coherencia:** Demasiados agentes modificando el mismo codebase simultaneamente generan conflictos de merge.

El limite WIP es una restriccion de coherencia, no de capacidad cognitiva. El Operador **DEBE** configurar limites WIP por zona del codebase, no por agente individual.

---

## 8. Economia de Tokens: De Story Points a Metricas Reales

Kelly dedica capitulos enteros a demoler la ilusion de la estimacion precisa en equipos humanos. Con agentes, el problema de la estimacion se transforma: los agentes no sufren planning fallacy, pero introducen una nueva variable --- el coste de inferencia.

### 8.1 Tres metricas que reemplazan la velocidad

| Metrica | Definicion | Analogo clasico |
|---|---|---|
| **Coste por Historia (CpH)** | Tokens consumidos por historia completada y aceptada | Velocidad (puntos/sprint) |
| **Tasa de Aceptacion (TA)** | % de historias aceptadas por PO al primer intento | Calidad (defectos) |
| **Cycle Time** | Tiempo desde Backlog hasta Done para una historia | Lead time |

### 8.2 Priorizacion por valor, no por esfuerzo

Dado que el esfuerzo ya no es recurso humano escaso sino gasto economico predecible (tokens), la priorizacion se simplifica:

> **FORMULA DE PRIORIDAD:** `Prioridad = Valor de Negocio / (Coste Estimado en Tokens x Multiplicador de Riesgo)`. Donde el Multiplicador de Riesgo aumenta para historias clasificadas como destructivas o con alta probabilidad de alucinacion. Priorizacion pura por ROI: cuanto valor por token invertido.

### 8.3 Presupuesto de tokens por Ciclo

Cada Ciclo **DEBE** tener un presupuesto de tokens aprobado. El Operador **DEBE** distribuir el presupuesto entre:

| Partida | Porcentaje |
|---|---|
| Historias de negocio | 60-70% |
| BAU y bugs | 20-25% |
| Calibracion del enjambre | 10-15% |

Principio de Kelly: watching the numbers sin perseguirlos como targets (evitando la Ley de Goodhart).

### 8.4 La curva de coste decreciente

Los datos observados 2023-2026: los modelos se abaratan ~40% cada 6 meses. Esto significa que la capacidad del enjambre crece exponencialmente a presupuesto constante.

**Nota de prudencia (v2.1):** Esta curva es una hipotesis de trabajo basada en datos observados 2023-2026, no un axioma garantizado. Las scaling laws muestran indicios de rendimientos decrecientes en ciertos benchmarks. La metodologia incluye un modo degradado explicito (ver [-> 17. Modos de Fallo y Circuit Breakers]) para el escenario donde la curva se aplana.

---

## 9. Calidad: Escudo contra la Alucinacion

Kelly es intransigente: la calidad no es opcional. TDD, ATDD, refactoring, CI, code reviews son obligatorios. En Xanpan::Agents, las practicas tecnicas se transforman y se amplifican.

### 9.1 Mapeo de practicas tecnicas

| Practica Kelly | Transformacion en Xanpan::Agents |
|---|---|
| **TDD** | Nativa: el agente genera tests y codigo simultaneamente. Eval pipeline verifica cobertura minima. |
| **ATDD** | PO escribe ACs, agente genera tests de aceptacion. Tests ejecutados pre-aprobacion humana. |
| **Refactoring** | Agentes refactorizan continuamente como tareas verdes. Metricas de complejidad ciclomatica monitoreadas. |
| **CI** | Cada historia genera PR con CI automatico: lint + tests + evals. |
| **Code Review** | Eval automatico + cross-review entre agentes. Reviewer-agent **DEBE** ser distinto de author-agent. |
| **Pair Programming** | COLAPSA. Reemplazado por cross-eval. Los agentes no necesitan socializar conocimiento. |
| **Coding Standards** | Context engineering: CONVENTIONS.md como ley. Linting automatico pre-merge. |
| **Static Analysis** | Nativo en pipeline CI. Ruff, ESLint, type checking. |

### 9.2 Evals: la practica tecnica obligatoria

Los Evals son a Xanpan::Agents lo que TDD es al Xanpan clasico: la practica tecnica obligatoria sin la cual todo fracasa.

Todo enjambre **DEBE** implementar al menos estos tipos de eval:

- **Eval de regresion:** Dataset curado de queries + respuestas esperadas por agente. **DEBE** ejecutarse en cada cambio de modelo o config.
- **Eval de alucinacion:** Verificacion de que el output del agente no contiene informacion fabricada.
- **Eval de tool-calling:** Verificacion de que el agente selecciona herramientas correctas para cada tarea.
- **Eval de coste:** Verificacion de que el consumo de tokens esta dentro de limites presupuestarios.
- **Eval de seguridad:** Verificacion de que el agente no expone datos sensibles, no escala privilegios, no realiza acciones fuera de su allowlist. Alineado con el pilar de seguridad de HCAI.

### 9.3 Definition of Done para agentes

El DoD se formaliza como pipeline que toda historia **DEBE** pasar:

1. Codigo generado con unit tests (cobertura > umbral configurado).
2. Tests de aceptacion derivados de ACs pasan.
3. Lint y type checking pasan sin errores.
4. Eval de regresion pasa (no rompe funcionalidad existente).
5. Eval de seguridad pasa (no expone datos, no escala privilegios).
6. Eval de diversidad: verificador **DEBE** usar provider distinto al generador ([-> 11. Arquitectura del Enjambre]).
7. PR creado con descripcion clara y contexto.
8. CI verde.
9. Aprobacion humana del PO contra criterios de aceptacion.

El paso 6 alinea el DoD con el principio de diversidad de modelos obligatoria ([-> 11. Arquitectura del Enjambre]) y el circuito de alucinacion sistemica ([-> 17. Modos de Fallo y Circuit Breakers]).

**Correcto:** `Coder con Claude Opus genera codigo; Reviewer con GPT-4.1 ejecuta eval de diversidad. Providers distintos.`
**Incorrecto:** `Coder con Claude Opus genera codigo; Reviewer con Claude Sonnet ejecuta eval. Mismo provider, blind spots compartidos.`

> **GOBERNANZA HCAI: FIABILIDAD + SEGURIDAD + CONFIANZA.** Shneiderman define tres pilares de gobernanza: fiabilidad (practicas de ingenieria rigurosas), cultura de seguridad (gestion organizacional), certificacion de confianza (auditoria externa). En Xanpan::Agents: Fiabilidad = evals + CI/CD. Cultura de seguridad = context engineering + principio de minimo privilegio. Confianza = transparencia total via dashboard + audit trail de cada accion del agente.

---

## 10. OKRs: Gobernanza Estrategica

Los OKRs son el mecanismo que conecta la estrategia de negocio con la ejecucion del enjambre. Kelly: escribir OKRs trimestrales es fundamentalmente una pregunta de estrategia.

### 10.1 OKR-first, no Backlog-first

Xanpan::Agents adopta categoricamente **OKR-first:**

1. **OKRs de Ciclo** definen Objetivos y Key Results.
2. De cada KR se derivan **Epicas** necesarias.
3. De cada Epica se derivan **Historias**.
4. Historias pueblan **Backlog**.
5. Agentes consumen backlog en orden de prioridad por valor.

El flujo es unidireccional y trazable: Estrategia -> OKR -> KR -> Epica -> Historia -> Criterios de Aceptacion -> Ejecucion -> Eval -> Aprobacion Humana.

**Correcto:** `OKR-first: los OKRs del Ciclo generan epicas que generan historias.`
**Incorrecto:** `Backlog-first: las historias acumuladas generan OKRs post-hoc para justificar lo que ya se hizo.`

### 10.2 Estructura OKR

| Componente | Descripcion | Responsable |
|---|---|---|
| **Objetivo** | Cualitativo, inspiracional, alineado al Higher Purpose de Kelly | PO |
| **Key Results (2-4)** | Cuantitativos, analogos (no binarios), medibles | PO |
| **Epicas derivadas** | Trabajo necesario para lograr KRs. Descompuesto con soporte de agente-planificador | PO + Agente |
| **Presupuesto de tokens** | Presupuesto de inferencia estimado para el Ciclo | Operador |
| **Criterios de eval** | Como se medira el exito del KR al final del Ciclo | PO + Operador |

### 10.3 BAU: Mantener las luces encendidas

Xanpan::Agents adopta la Opcion 4 de Kelly: hacer BAU un Objetivo cero explicito. **DEBE** reservarse un porcentaje fijo del presupuesto de tokens del Ciclo (tipicamente 20-30%) para trabajo BAU: bugs, soporte, deuda tecnica, mantenimiento.

### 10.4 OKRs asistidos por agentes

En niveles de madurez 4-5 del HCAI-MM, los agentes no solo ejecutan hacia OKRs sino que proponen OKRs. Un agente-analista con acceso a metricas de producto, datos de uso y OKRs historicos **PUEDE** generar borradores de Objetivos y Key Results para el proximo Ciclo. El PO **DEBE** revisar, ajustar y aprobar. La inteligencia estrategica es hibrida: datos de maquina + juicio humano.

---

## 11. Arquitectura del Enjambre

Esta seccion no tiene equivalente en Kelly porque los equipos humanos no necesitan ser configurados. Los agentes SI. El Operador **DEBE** disenar la topologia del enjambre.

### 11.1 Roles de agentes

| Rol | Funcion | Tier de modelo |
|---|---|---|
| **Planner** | Descompone epicas en historias y historias en tareas | Tier 3 (Frontier) |
| **Coder** | Implementa codigo desde historias con TDD | Tier 2-3 |
| **Reviewer** | Revisa PRs generados por Coders; cross-eval | Tier 2 |
| **Tester** | Genera y ejecuta tests de aceptacion e integracion | Tier 2 |
| **Refactorer** | Mejora continua de codigo existente (tareas verdes) | Tier 2 |
| **Analyst** | Genera metricas, resumenes, reportes para PO | Tier 1-2 |
| **Orchestrator** | Coordina flujo entre agentes; Model Router | Tier 1 |
| **Sentinel** | Meta-agente que monitorea al enjambre (ver [-> 11.4 El enjambre auto-evolutivo]) | Tier 2-3 |

### 11.2 Conway Invertido

Kelly cita la Ley de Conway: la estructura del equipo determina la estructura del software. En Xanpan::Agents, la relacion se invierte: la estructura del software **DEBE** dictar la topologia del enjambre. Cada area del codebase (frontend, backend, infra) **PUEDE** tener agentes especializados con context engineering dedicado. Los limites WIP aplican por zona, no por agente.

El Operador **PUEDE** reconfigurar topologia entre Ciclos sin coste de forming-storming (los agentes no tienen curva de Tuckman).

### 11.3 Model Router

Cada tarea **DEBE** enrutarse al modelo optimo por coste/capacidad:

| Tier | Modelos (febrero 2026) | Casos de uso | Coste relativo |
|---|---|---|---|
| **Tier 1 (Economico)** | Flash, Haiku, Mini | Clasificacion, formateo, analisis simple, orquestacion | $ |
| **Tier 2 (Balance)** | Sonnet, GPT-4.1, Gemini Pro | Tool-calling, generacion de codigo estandar, reviews | $$ |
| **Tier 3 (Frontier)** | Opus, GPT-4.5, Gemini Ultra | Razonamiento complejo, planificacion, decisiones arquitectonicas | $$$ |
| **Tier 4 (Reasoning)** | o3, modelos thinking | Problemas matematicos, logicos, evaluacion critica | $$$$ |

Principio de diversidad de modelos obligatoria: si un agente genera algo, el agente que lo verifica **DEBE** usar un modelo de provider diferente. Si el Coder usa Claude, el Reviewer **DEBE** usar GPT. Si el analizador usa Gemini, el sintetizador **DEBE** usar Claude.

Un modelo no puede detectar sus propios blind spots. Dos modelos de providers diferentes tienen blind spots diferentes; la interseccion es mas pequena.

**Correcto:** `Agente-coder con Claude Opus, agente-reviewer con GPT-4.1.`
**Incorrecto:** `Agente-coder con Claude Opus, agente-reviewer con Claude Sonnet. (Mismo provider, blind spots compartidos.)`

### 11.4 El enjambre auto-evolutivo

El enjambre no solo ejecuta: aprende y se optimiza:

- **Auto-optimizacion de prompts:** El Sentinel analiza patrones de rechazo y propone ajustes a system prompts de otros agentes. El Operador **DEBE** aprobar los cambios.
- **Auto-generacion de evals:** Cuando una historia es rechazada, el Sentinel **DEBE** generar automaticamente un nuevo caso de eval para prevenir la recurrencia. El nuevo eval se agrega al pipeline tras aprobacion del Operador.
- **Auto-reconfiguracion de topologia:** Si el Sentinel detecta que un area del codebase tiene cycle time consistentemente alto, propone agregar un agente especializado o cambiar de tier de modelo. El Operador decide.
- **Tarjetas purpura:** El Sentinel genera tarjetas purpura en el tablero con propuestas de mejora. Son visibles para PO y Operador pero **NO DEBEN** ejecutarse sin aprobacion humana. HCAI en accion: automatizacion alta + control humano alto.

#### Quis custodiet ipsos custodes? El eval del Sentinel

El Sentinel es un agente. Puede alucinar. Si propone una reconfiguracion basada en una evaluacion erronea, el error se propaga sistemicamente. Solucion: separacion de concerns estilo auditor externo.

1. **Sentinel distinto a Reviewer:** El Sentinel **NO DEBE** revisar las mismas historias que evalua. Su input son metricas agregadas (tasas, tendencias, anomalias), no PRs individuales.
2. **Eval del evaluador:** Un subset de las propuestas del Sentinel **DEBE** evaluarse retroactivamente: las propuestas aplicadas mejoraron realmente las metricas? Si la tasa de mejora efectiva del Sentinel cae por debajo de un umbral, alerta al Operador.
3. **Modelo diferente:** El Sentinel **DEBE** usar un modelo y provider diferente al enjambre que evalua. Diversidad de modelos como defensa contra bias compartido.
4. **Veto asimetrico:** El Sentinel **PUEDE** proponer cualquier cosa pero **NO DEBE** ejecutar nada. El humano tiene veto absoluto y sin justificacion requerida. La asimetria es intencional: proponer es barato, ejecutar errores es caro.

> **PRINCIPIO DE AUTO-EVOLUCION GOBERNADA:** El enjambre puede proponer cualquier cambio sobre si mismo: prompts, evals, topologia, modelos. Pero no puede ejecutar ningun cambio sin aprobacion humana. Es el patron HCAI de alta automatizacion + alto control llevado al meta-nivel: el sistema se auto-mejora pero los humanos gobiernan la direccion de la mejora.

### 11.5 Equipos Ameba con agentes

Kelly adopta el modelo de Equipos Ameba de Inamori: equipos pequenos que crecen, se dividen y contraen organicamente. Con agentes, la elasticidad es instantanea:

- Necesitas mas capacidad para un deadline? Escala el numero de agentes-coder en minutos.
- El trabajo se reduce? Desescala sin coste emocional. No hay despidos, no hay perdida de moral.
- Area nueva de producto? Spawn sub-enjambre con context engineering especifico.
- Merge de dos lineas de producto? Fusiona context engineering. Los agentes no tienen territorios politicos.

---

## 12. Human-in-the-Loop: Loops de Gobernanza HCAI

Xu describe un paradigma donde el loop humano abarca el ciclo de vida completo del sistema: requisitos, diseno, desarrollo, despliegue, uso, operaciones y gobernanza.

### 12.1 Loop 1: Human-in-the-Loop (Individuo-Agente)

#### Intervenciones obligatorias

El humano **DEBE** intervenir en:

- **Aceptacion de historias:** PO acepta o rechaza cada historia completada contra criterios de aceptacion. Sin auto-aprobacion. Nunca.
- **Acciones destructivas:** Cualquier operacion clasificada como destructiva **DEBE** requerir aprobacion explicita del Operador.
- **Cambios arquitectonicos:** Decisiones que afectan estructura fundamental del sistema.
- **Actualizaciones de modelo:** Cambiar modelo base **DEBE** requerir regresion + aprobacion.
- **Cambios auto-evolutivos:** Toda propuesta del Sentinel **DEBE** requerir aprobacion del Operador.

#### Autonomia del enjambre (todo lo NO listado arriba)

- Descomposicion de historias en tareas.
- Generacion de codigo y tests.
- Ejecucion de CI/CD hasta deploy con feature flags (si evals robustos y rollback automatico configurado).
- Refactoring continuo (tareas verdes).
- Generacion de PRs y documentacion.
- Eval automatico entre agentes (reviewer distinto a coder).

**Correcto:** `CI/CD ejecuta hasta deploy con feature flags. Los evals robustos y rollback automatico configurado habilitan deploy autonomo sin staging.`
**Incorrecto:** `CI/CD ejecuta hasta staging. (Contradice el principio de despliegue continuo sin staging establecido en [-> 1.3 Lo que emerge] y [-> 16. Velocidad Exponencial].)`

### 12.2 Loop 2: Organization-in-the-Loop

Herrmann y Pfeiffer (2023) enfatizan que HCAI no puede ignorar el contexto organizacional:

- **OKRs como alineacion organizacional:** Los OKRs del enjambre **DEBEN** derivar de la estrategia de la organizacion. No son autonomos.
- **Presupuesto de tokens aprobado por liderazgo:** El coste del enjambre es gasto operativo aprobado a nivel organizacional.
- **Cultura de calidad como norma:** La organizacion define estandares de calidad que se implementan via context engineering y evals.
- **Rediseno de trabajo:** La adopcion de Xanpan::Agents requiere redisenar roles, procesos y flujos de decision. No es agregar agentes al proceso existente. Ver [-> 18. Modelo de Transicion].

### 12.3 Loop 3: Ecosystem-in-the-Loop

El enjambre no opera en aislamiento:

- **MCP para interoperabilidad:** Los agentes **DEBERIAN** conectarse con herramientas externas via MCP estandar.
- **Coordinacion con otros sistemas IA:** Si la organizacion tiene multiples enjambres o sistemas IA, **DEBEN** coordinarse.
- **Ecosistema cognitivo distribuido:** Xu describe ecosistemas como sistemas cognitivos distribuidos donde humanos e IA colectivamente perciben, razonan, aprenden y deciden.

### 12.4 Loop 4: Society-in-the-Loop

El nivel macrosocial de HCAI:

- **Cumplimiento regulatorio:** EU AI Act, NIST AI RMF, ISO/IEC 42001. El enjambre **DEBE** operar dentro de marcos regulatorios.
- **Impacto laboral:** Xanpan::Agents no evita la pregunta dificil: que pasa con los desarrolladores humanos? La respuesta HCAI: los humanos se elevan a roles de mayor valor (PO, Operador, arquitectos, estrategas) mientras los agentes absorben trabajo mecanico. Ver [-> 18. Modelo de Transicion].
- **Transparencia y auditabilidad:** Cada decision del agente **DEBE** tener audit trail. Cada historia **DEBE** tener trazabilidad completa.

> **PRINCIPIO DE MINIMA INTERVENCION MAXIMAL:** El humano interviene SOLO donde: (a) hay valor de negocio que juzgar (PO), (b) hay riesgo de dano irreversible (Operador), (c) la calidad del enjambre se degrada mas alla de umbrales configurados (alertas automaticas), o (d) hay implicaciones organizacionales, ecosistemicas o sociales que requieren juicio humano. Todo lo demas es autonomo. Esto no es negligencia; es diseno. Es HCAI.

---

## 13. Digital Continuo: Software Longevo

Kelly argumenta contra el pensamiento de proyecto: el software no esta terminado, evoluciona continuamente. Con agentes IA, este argumento se fortalece exponencialmente.

### 13.1 Software como activo vivo acelerado

- **Inversion continua posible y barata:** Los agentes **PUEDEN** mejorar, refactorizar y actualizar software continuamente a coste marginal. La excusa de no hay presupuesto para mantenimiento muere.
- **Eliminacion de gaps entre proyectos:** Kelly advierte que los gaps entre proyectos causan perdida de conocimiento tacito. Con agentes, el context engineering preserva conocimiento explicitamente.
- **Deuda tecnica como tarea continua:** En vez de acumular deuda hasta que un proyecto de refactoring la aborde, agentes-refactorer **DEBERIAN** trabajar continuamente como tareas verdes.

### 13.2 El software longevo

Si los agentes pueden mantener, actualizar y evolucionar software continuamente a coste marginal, el concepto de end of life del software cambia fundamentalmente. Los agentes **PUEDEN** migrar frameworks, actualizar dependencias, refactorizar arquitecturas completas --- todo como flujo continuo de tareas verdes.

**Matiz necesario:** El software no es literalmente inmortal. Muere no solo por perdida de valor de negocio --- muere por muerte de ecosistema:

- APIs que se deprecan sin reemplazo equivalente.
- Estandares que cambian de forma incompatible.
- Regulaciones que invalidan arquitecturas enteras.
- Plataformas que desaparecen.

Los agentes **PUEDEN** detectar temprano el drift ecosistemico (via Sentinel monitoreando changelogs de dependencias, anuncios de deprecacion, cambios regulatorios) y proponer migracion proactiva antes de que sea crisis.

### 13.3 Productos, no proyectos: amplificado

- No hay fin de proyecto: el enjambre opera siempre.
- No hay equipo de mantenimiento separado: el mismo enjambre que construye, mantiene.
- No hay hand-off: no hay transferencia de conocimiento porque el conocimiento esta en el context engineering, no en cerebros humanos que se van.
- El presupuesto es continuo: tokens/mes, no presupuesto de proyecto.

---

## 14. Observabilidad y Retrospectiva Analitica

### 14.1 Dashboard del enjambre

El Operador **DEBE** monitorear un dashboard en tiempo real con cinco dimensiones:

| Dimension | Metricas | Frecuencia |
|---|---|---|
| **Coste** | Tokens/Pulso, Coste/Historia, Coste/KR, % presupuesto consumido | Continua |
| **Calidad** | Tasa de Aceptacion, Tasa de Alucinacion, Cobertura de Tests, Scores de Eval | Por Pulso |
| **Velocidad** | Historias Done/Pulso, Cycle Time promedio, Throughput | Por Pulso |
| **Modelo** | Tasa de exito por modelo, latencia promedio, frecuencia de fallback | Continua |
| **Enjambre** | Utilizacion de agentes, WIP por zona, profundidad de cola, tarjetas purpura pendientes | Continua |

### 14.2 Retrospectiva Analitica

Al final de cada Ciclo (no cada Pulso), PO y Operador **DEBEN** conducir la Retrospectiva Analitica:

1. **Revision de OKRs:** Que KRs se lograron? Cuales no y por que?
2. **Analisis de coste:** Se respeto el presupuesto de tokens? Donde se concentro el gasto?
3. **Analisis de calidad:** Que patrones de rechazo se observaron? Hay alucinaciones recurrentes?
4. **Decisiones de ajuste:** Cambiar modelos? Ajustar context engineering? Reconfigurar topologia?
5. **Actualizacion de evals:** Agregar nuevos casos de test basados en fallos observados.
6. **Revision de tarjetas purpura:** Evaluar propuestas auto-evolutivas del Sentinel pendientes.
7. **Eval del Sentinel:** Las propuestas del Sentinel aplicadas en el Ciclo anterior mejoraron metricas? La tasa de mejora efectiva es aceptable?

La retrospectiva analitica elimina la dimension emocional de la retro clasica. No hay "que salio mal?" con carga emocional. Hay datos, patrones y decisiones operacionales.

---

## 15. Seguridad y Gobernanza Multi-Nivel

### 15.1 Principio de minimo privilegio por agente

- **Allowlist explicito:** Cada agente **DEBE** tener allowlist explicito de herramientas (AgentSkills) que puede invocar.
- **Sin acceso directo a secretos de produccion:** Secretos **DEBEN** ser inyectados en runtime por pipeline CI/CD.
- **Separacion de privilegios:** Agentes-coder **NO DEBEN** desplegar a produccion. Solo el pipeline CI/CD **PUEDE** activar features en produccion; deploy con feature flags es autonomo, activacion/release depende de clasificacion de riesgo.

**Correcto:** `Pipeline CI/CD activa feature en produccion con feature flag. Deploy autonomo si riesgo es lectura o escritura; aprobacion humana si riesgo es destructivo.`
**Incorrecto:** `Solo el pipeline CI/CD puede desplegar, tras aprobacion humana para TODOS los deploys. (Contradice el principio de despliegue continuo sin staging.)`

### 15.2 Aislamiento de ejecucion

| Nivel | Tipo | Descripcion |
|---|---|---|
| **Nivel 1 (Read)** | Container read-only | Para queries y analisis. Sin escritura. |
| **Nivel 2 (Write)** | Container efimero | Destruido post-ejecucion. Para generacion de codigo. |
| **Nivel 3 (OS Shell)** | MicroVM (Firecracker) | Timeout estricto, sin red externa. Para ejecucion de tests. |

Todo agente **DEBE** ejecutarse en el nivel de aislamiento correspondiente a sus permisos. Un agente con permiso Write **NO DEBE** ejecutarse en el host sin aislamiento.

**Correcto:** `Agente con permiso Write ejecuta en container efimero que se destruye post-ejecucion.`
**Incorrecto:** `Agente con permiso Shell ejecuta en el host sin aislamiento ni timeout.`

### 15.3 Agent-to-agent prompt injection

Una amenaza especifica de los enjambres multi-agente. Cuando los agentes pasan datos entre si, un agente comprometido por prompt injection via input de usuario **PUEDE** inyectar instrucciones maliciosas en su output, que otro agente consumira como input legitimo.

Controles obligatorios:

- **Sanitizacion en cada interfaz interna.** El output de cada agente **DEBE** validarse contra un schema tipado antes de alimentar al siguiente agente. **NO DEBE** pasarse texto libre entre agentes si se puede evitar; **DEBEN** pasarse estructuras tipadas.
- **Context isolation.** Cada agente **DEBE** tener su propio contexto. El agente-reviewer **NO DEBE** heredar el prompt del agente-coder; recibe solo el artefacto (codigo) y su propio prompt de revision.
- **Deteccion de anomalias inter-agente.** El agente-observer ([Swarm::Ops &sect;7.2](urn:fxsl:kb:swarm-ops-metodologia)) **DEBE** monitorear patrones de comunicacion entre agentes. Un agente que produce outputs con estructura inusual o contenido instruccional (meta-prompts) es senalizado.
- **Diversidad de modelos como mitigacion.** Si el agente-coder es comprometido via un blind spot del modelo que usa, el agente-reviewer (con modelo diferente) tiene mayor probabilidad de detectar la anomalia.

### 15.4 Gobernanza multinivel HCAI

Shneiderman propone cuatro niveles de gobernanza:

| Nivel Shneiderman | Mecanismo en Xanpan::Agents |
|---|---|
| **Equipo: practicas de ingenieria** | Evals, CI/CD, context engineering, DoD como pipeline automatico |
| **Organizacion: cultura de seguridad** | OKRs, presupuesto aprobado, roles definidos (PO/Operador), retrospectiva analitica |
| **Industria: certificacion de confianza** | Audit trail completo, trazabilidad historia-codigo-deploy, cumplimiento de estandares |
| **Gobierno: regulacion** | Compliance con EU AI Act, NIST AI RMF, ISO/IEC 42001, reportes de incidentes |

---

## 16. Velocidad Exponencial

Esta seccion no existe en ninguna metodologia agil previa porque ninguna fue disenada para un mundo donde la capacidad del ejecutor se duplica cada seis meses.

### 16.1 La curva exponencial: hipotesis de trabajo

Los datos observados 2023-2026:

- **Coste de inferencia:** Cae ~40% cada 6 meses.
- **Capacidad de los modelos:** Cada generacion maneja mas contexto, comete menos errores, usa herramientas mejor.
- **Herramientas de agentes:** MCP, Claude Code, Codex CLI, agentes de navegacion, agentes de investigacion: cada trimestre aparecen capacidades nuevas.

**Nota critica (v2.1):** Estos datos son observaciones empiricas, no leyes de la fisica. Las scaling laws muestran indicios de rendimientos decrecientes en ciertos benchmarks desde mid-2025. La exponencialidad es la hipotesis de trabajo, no un axioma. La metodologia esta disenada para surfear la exponencialidad si continua, y para degradar gracefully si se aplana (ver [-> 17. Modos de Fallo y Circuit Breakers]).

Una metodologia que no esta disenada para absorber mejoras exponenciales es una metodologia que se vuelve obsoleta en meses. Pero una metodologia que asume la exponencialidad como garantia es una metodologia que colapsa ante la primera meseta.

### 16.2 Principios para velocidad exponencial

Todo enjambre que opere bajo Xanpan::Agents **DEBE** adoptar estos principios:

#### Principio 1: Disenar para el modelo de manana, no el de hoy

La arquitectura del enjambre **DEBE** asumir que en 6 meses los modelos seran mas capaces y mas baratos. **NO DEBE** sobre-optimizarse para las limitaciones actuales. Si hoy se necesita un workaround porque el modelo falla en X, **DEBE** ponerse un eval pero **DEBE** asumirse que el workaround sera temporal.

#### Principio 2: Automatizar la automatizacion

No es suficiente automatizar el desarrollo. **DEBE** automatizarse la automatizacion misma. El Sentinel es la primera capa. En niveles de madurez 5, meta-agentes optimizan la metodologia misma: ajustan duracion de Pulsos, recalibran presupuestos de tokens, proponen reorganizaciones de topologia --- todo basado en datos.

#### Principio 3: Ship fast, eval faster, rollback instantaneo

El staging clasico era necesario porque el despliegue era costoso y el rollback dificil. Con feature flags, canary deploys y evals robustos, el flujo se comprime: generar, evaluar, desplegar, monitorear, rollback si falla. Todo automatico. Todo en minutos. La red de seguridad no es un ambiente de staging; es un pipeline de evals + rollback automatico.

**Correcto:** `Deploy continuo con feature flags + evals robustos + rollback automatico. Sin staging.`
**Incorrecto:** `Pipeline con ambiente de staging separado como paso obligatorio. (Introduce latencia innecesaria cuando los evals son robustos.)`

#### Principio 4: El backlog es un flujo, no un repositorio

El backlog **NO DEBE** pensarse como una lista estatica que se prioriza y se consume. Es un flujo continuo: entran historias del PO, entran propuestas del backlog predictivo, salen historias ejecutadas, salen historias descartadas. Optimizar el flujo, no el inventario.

#### Principio 5: Cada Ciclo debe ser mas eficiente que el anterior

Si el Ciclo 3 no es mas eficiente que el Ciclo 2, algo esta mal. El enjambre auto-evolutivo, la mejora continua de evals, la optimizacion de context engineering y la caida de costes de inferencia **DEBEN** producir una curva de mejora compuesta. Si la curva se aplana, diagnosticar y corregir. La estasis es sintoma de enfermedad --- o senal de que la hipotesis exponencial necesita revision (ver [-> 17. Modos de Fallo y Circuit Breakers]).

---

## 17. Modos de Fallo y Circuit Breakers

El happy path no es suficiente. Las metodologias serias no se miden por como funcionan cuando todo va bien, sino por como fallan cuando algo sale mal.

### 17.1 Alucinacion sistemica

**Modo de fallo:** El enjambre genera codigo que pasa todos los evals pero contiene errores semanticos sutiles. Los tests pasan porque los tests mismos fueron generados por un agente que compartio el mismo error de comprension que el agente que genero el codigo.

**Circuit breakers:**

- **Diversidad de modelos obligatoria:** Coder y Reviewer **DEBEN** usar modelos de providers diferentes. Los modelos de un mismo provider comparten biases de entrenamiento; la diversidad reduce la probabilidad de bias compartido.
- **Golden dataset humano:** Un subset de evals **DEBE** tener respuestas correctas escritas por humanos, no generadas por agentes. Estas anclas humanas detectan drift sistemico.
- **Auditoria de muestra por PO:** Ademas de aceptar/rechazar historias, el PO **DEBERIA** periodicamente (cada Pulso) inspeccionar en profundidad 1-2 historias completadas, incluyendo el codigo generado, no solo el comportamiento funcional.

### 17.2 Bias en los evals

**Modo de fallo:** Los evals mismos tienen bias. Un eval de alucinacion que solo chequea afirmaciones factuales pero no detecta omisiones criticas. Un eval de seguridad que cubre OWASP Top 10 pero no detecta vulnerabilidades novedosas.

**Circuit breakers:**

- **Meta-eval periodico:** Cada Ciclo, el Operador (asistido por Sentinel) **DEBE** revisar el conjunto de evals: cubren los modos de fallo observados? Hay areas sin cobertura? El meta-eval es humano-liderado porque la definicion de que deberia evaluar requiere juicio que los agentes no tienen.
- **Evals adversariales:** Periodicamente, un agente **DEBE** recibir la instruccion explicita de intentar romper el sistema: generar codigo que pase evals pero sea incorrecto, encontrar formas de escalar privilegios, producir output que engane al Reviewer. Los resultados alimentan nuevos evals.
- **Incidentes como evals:** Cada bug en produccion, cada historia rechazada, cada anomalia detectada **DEBE** convertirse en un nuevo caso de eval. El corpus de evals es un organismo vivo que crece con cada fallo. Kelly: Quality is free --- pero solo si aprendes de cada error.

### 17.3 Divergencia PO-Operador

**Modo de fallo:** El PO quiere velocidad de features. El Operador quiere estabilidad del enjambre. Sus incentivos divergen. Sin mecanismo de resolucion, se genera deadlock.

**Circuit breakers:**

- **OKRs como contrato compartido:** Los OKRs del Ciclo **DEBEN** ser definidos conjuntamente. Si el PO quiere velocidad, **DEBE** explicitarlo como KR medible. Si el Operador quiere estabilidad, **DEBE** explicitarlo como KR medible. Ambos firman los mismos OKRs.
- **Dashboard como fuente de verdad:** Las metricas no mienten. Si el acceptance rate cae al 60%, el PO no puede argumentar que todo va bien. Si el coste por historia es 3x el presupuesto, el Operador no puede argumentar que el enjambre funciona. Los datos resuelven disputas.
- **Escalacion a liderazgo:** Si PO y Operador no resuelven, el conflicto escala al nivel Organization-in-the-Loop. Si ocurre frecuentemente, la separacion de roles **PUEDE** necesitar rediseno.

### 17.4 Vulnerabilidad novel no cubierta por evals

**Modo de fallo:** Un agente-coder genera codigo que introduce una vulnerabilidad de seguridad completamente nueva --- algo que ningun eval cubre porque es un patron de ataque que no existia cuando los evals fueron disenados. Pasa CI, pasa evals, pasa review, llega a produccion.

**Circuit breakers:**

- **Principio de minimo privilegio como backstop:** Incluso si el codigo tiene una vulnerabilidad, el agente que lo genero no tiene acceso a produccion. El deploy pasa por pipeline CI/CD con permisos restringidos. La superficie de ataque se contiene por diseno.
- **Monitoreo de produccion separado del enjambre:** La observabilidad de produccion (APM, WAF, anomaly detection) **DEBE** ser sistema independiente, no controlado por los mismos agentes que generaron el codigo.
- **Rotacion de Security Analyst como rol satelite:** Periodicamente (cada Ciclo o ante cambios significativos de superficie de ataque), un humano especialista en seguridad **DEBERIA** revisar la arquitectura y los patrones de codigo desplegados.

### 17.5 Meseta de capacidad (la exponencialidad se detiene)

**Modo de fallo:** Las scaling laws se aplanan. Los modelos dejan de mejorar significativamente entre generaciones. El coste de inferencia se estabiliza. La hipotesis exponencial del [-> 16. Velocidad Exponencial] deja de ser valida.

**Circuit breakers:**

- **Pulso vuelve a ritmo fijo:** Si la mejora entre Ciclos se aplana (<5% mejora en CpH durante 3 Ciclos consecutivos), el Pulso adaptativo **DEBE** volver a frecuencia fija semanal. La incertidumbre requiere mas gobernanza, no menos.
- **Presupuesto de tokens como recurso escaso:** Se abandona la mentalidad de presupuesto creciente a coste constante y se adopta gestion de escasez: priorizacion mas estricta, eliminacion de tareas verdes no esenciales, reduccion del presupuesto de calibracion al minimo necesario.
- **Roles humanos se expanden:** Si los agentes no mejoran, los humanos retoman tareas de mayor complejidad cognitiva. El modelo no es binario (humano vs. agente); es un espectro donde la frontera se ajusta segun las capacidades reales.
- **Inversion en evals y context engineering se intensifica:** Si los modelos no mejoran, la forma de sacar mas rendimiento es optimizar como los usamos: mejores prompts, mejor contexto, mejores evals.

### 17.6 Corrupcion de context engineering

**Modo de fallo:** Los context files acumulan contradicciones, informacion obsoleta o instrucciones ambiguas. Los agentes reciben senales conflictivas y su rendimiento se degrada gradualmente sin un fallo discreto que dispare alertas.

**Circuit breakers:**

- **Sentinel como auditor de context:** Verificacion automatica de coherencia entre context files y codebase real ([-> 4.2 Operador: El Ingeniero de Enjambre]).
- **Context files en git con blame:** Cada linea tiene autor y fecha. El Operador **PUEDE** trazar cuando se introdujo una contradiccion.
- **Metric correlation:** Si el acceptance rate cae sin cambio de modelo ni de tipo de historias, la primera hipotesis **DEBE** ser degradacion de context. El dashboard **DEBE** correlacionar cambios en context files con cambios en metricas.

---

## 18. Modelo de Transicion: Del Equipo Humano al Enjambre

La transicion **NO DEBE** ser un big bang. Se migra gradualmente, exactamente como Kelly recomienda adoptar Xanpan: pick'n'mix --- toma lo que funcione, descarta lo que no.

### 18.1 Fase 0: Augmented Development (semanas 1-4)

Los desarrolladores humanos continuan haciendo su trabajo normal pero empiezan a usar agentes como herramientas:

- Cada dev usa un agente-coder como copiloto (Claude Code, Cursor, Copilot).
- Se instrumentan metricas basicas: cuanto codigo genera el agente vs. el humano? Que tipo de tareas delegan naturalmente?
- Se identifica al futuro Operador: el dev mas interesado en configurar y optimizar agentes.
- Se identifica al futuro PO (o se confirma al PO existente si ya hay uno).

**Objetivo:** Construir intuicion sobre que pueden y no pueden hacer los agentes en el codebase especifico.

### 18.2 Fase 1: Parallel Track (semanas 5-12)

Se crea un track paralelo donde un mini-enjambre trabaja en historias seleccionadas mientras el equipo humano continua:

- El Operador (emergente) configura un enjambre minimo: 1 Coder + 1 Reviewer + CI con evals basicos.
- Se seleccionan 3-5 historias de bajo riesgo y complejidad media para el enjambre.
- El equipo humano trabaja en el resto del backlog normalmente.
- Se comparan resultados: velocidad, calidad, coste. Sin presion por resultados; es un experimento.

**Objetivo:** Validar que el enjambre **PUEDE** producir codigo de produccion en el stack del equipo.

### 18.3 Fase 2: Accelerated Adoption (semanas 13-24)

El enjambre absorbe progresivamente mas tipos de historias:

- Evals se formalizan. Context engineering se establece (CONVENTIONS.md, ARCHITECTURE.md).
- El Operador se dedica full-time (o near full-time) al enjambre.
- Desarrolladores humanos se redistribuyen: algunos se convierten en Operadores de sub-enjambres, otros migran a roles de PO, arquitectos o domain experts.
- El tablero se implementa. Metricas de coste y calidad se rastrean por Pulso.

**Objetivo:** Alcanzar Nivel 2-3 de madurez HCAI.

### 18.4 Fase 3: Swarm-First (semanas 25+)

El enjambre es el mecanismo primario de ejecucion:

- Todas las historias pasan por el enjambre. Humanos intervienen en aceptacion, arquitectura, dominio.
- Sentinel activado. Backlog predictivo en prueba. Tarjetas purpura aparecen.
- Roles humanos estabilizados: PO, Operador, roles satelite segun necesidad.
- Retrospectiva Analitica como practica establecida.

**Objetivo:** Operacion normal segun Xanpan::Agents completo.

### 18.5 Que pasa con los desarrolladores humanos

- **Algunos se convierten en Operadores:** Los devs con interes en infraestructura, DevOps y optimizacion son candidatos naturales.
- **Algunos se convierten en POs o domain experts:** Los devs con mas conocimiento de negocio y usuarios migran hacia roles de definicion de valor.
- **Algunos se convierten en arquitectos:** Los devs senior definen ARCHITECTURE.md, revisan cambios arquitectonicos y mantienen la vision tecnica de largo plazo.
- **Algunos se convierten en ingenieros de evals:** Disenar, mantener y mejorar el corpus de evals es trabajo especializado que requiere conocimiento profundo del dominio y del stack.
- **Algunos necesitaran reubicarse:** Ser honesto sobre esto es parte del principio HCAI de Society-in-the-Loop. La organizacion **DEBE** facilitar la transicion: reskilling, reubicacion interna, tiempo y soporte.

### 18.6 Anti-patrones de transicion

| Anti-patron | Descripcion |
|---|---|
| **Reemplazamos al equipo el lunes** | Big bang. Garantia de desastre. Sin context engineering, sin evals, sin comprension de las limitaciones. |
| **Los agentes hacen todo, los devs supervisan** | Subestima la atencion requerida. Los devs no estan entrenados para supervisar agentes; es una habilidad diferente. |
| **Primero perfeccionamos los evals, despues activamos el enjambre** | Paralisis por analisis. Los evals se perfeccionan con uso real, no en laboratorio. Ship, eval, iterate. |
| **Mantenemos el Scrum existente y le agregamos agentes** | Los agentes no son devs mas rapidos. Son una especie diferente. Intentar meterlos en ceremonias Scrum no funciona. |

---

## 19. Sintesis: La Metodologia Completa

### 19.1 Xanpan::Agents en una oracion

Un Product Owner humano define QUE construir via user stories y OKRs. Un Operador humano configura y supervisa un enjambre de agentes IA auto-evolutivo que construye el COMO. Roles satelite aportan expertise de dominio cuando se necesita. La calidad se garantiza via evals automaticos y aprobacion humana. La gobernanza HCAI multi-nivel asegura que la velocidad exponencial sirva a valores humanos. El software evoluciona continuamente como activo longevo. La metodologia incluye modos de fallo explicitos y circuit breakers para cuando las cosas van mal.

### 19.2 Tabla de correspondencia Kelly a Xanpan::Agents v2.1

| Concepto clasico | Transformacion v2.1 | Fundamento |
|---|---|---|
| Sprint (2 semanas) | Pulso adaptativo (3d-2sem) | Velocidad de agentes comprime revision |
| OKR trimestral | Ciclo (4-6 semanas) | Ejecucion rapida permite iterar mas |
| Planning Poker | ELIMINADO | Agentes no tienen sesgo de estimacion |
| Velocidad (pts/sprint) | CpH + Tasa Aceptacion + Cycle Time | Metricas economicas reales |
| Pair Programming | Cross-eval entre agentes | No necesitan socializar conocimiento |
| Retrospectiva | Retrospectiva Analitica | Datos operacionales, no emocion |
| Scrum Master | Operador | De facilitador social a ingeniero de enjambre |
| Equipo desarrollador | Enjambre auto-evolutivo + Sentinel | Agentes especializados + meta-agente auditor |
| Board estatico | Tablero Neural + tarjetas purpura | Dashboard tiempo real + auto-propuestas |
| TDD | TDD + Evals (incl. seguridad + adversarial) | Evals como TDD organizacional anti-alucinacion |
| Trabajo no planificado | Preservado (amarillo + BAU OKR) | Kelly tiene razon: lo no planificado es valioso |
| Productos no proyectos | Reforzado: software longevo | Agentes mantienen software indefinidamente* |
| Gobernanza de proyecto | Gobernanza multi-nivel HCAI | 4 loops: humano, org, ecosistema, sociedad |
| Backlog estatico | Backlog predictivo + flujo | Agentes proponen historias + PO cura |
| Deploy con staging | Ship fast, eval faster, rollback | Evals + feature flags reemplazan staging |
| (sin equivalente) | Roles satelite | Domain experts, compliance, security, UX |
| (sin equivalente) | Modos de fallo + circuit breakers | Resiliencia disenada, no improvisada |
| (sin equivalente) | Modelo de transicion | Migracion gradual, no big bang |

*Longevo, no inmortal. Ver [-> 13. Digital Continuo: Software Longevo] para matices sobre obsolescencia ecosistemica y regulatoria.

### 19.3 Los 12 Axiomas de Xanpan::Agents v2.1

> **AXIOMA 1:** Humano define QUE y POR QUE. Agente resuelve COMO. (Invariante fundamental.)

> **AXIOMA 2:** Cada historia debe entregar valor de negocio. (Invariante Kelly.)

> **AXIOMA 3:** OKRs gobiernan la direccion. El backlog es derivado, no primario.

> **AXIOMA 4:** La calidad es gratis si inviertes en evals. (Evolucion del axioma Crosby/Kelly.)

> **AXIOMA 5:** El coste de token es el nuevo recurso escaso. Gestionalo como presupuesto.

> **AXIOMA 6:** Human-in-the-loop para valor y riesgo. Autonomia para todo lo demas.

> **AXIOMA 7:** El software es un activo vivo y longevo. (Invariante Kelly/Continuous Digital, amplificado.)

> **AXIOMA 8:** Visualiza todo. El tablero neural es el sistema nervioso.

> **AXIOMA 9:** Mide, no persigas. (Principio Kelly contra Goodhart.)

> **AXIOMA 10:** Alta automatizacion Y alto control humano. No hay trade-off. (Principio HCAI de Shneiderman.)

> **AXIOMA 11:** El enjambre se auto-evoluciona bajo gobernanza humana. (Con Sentinel auditado y circuit breakers.)

> **AXIOMA 12:** Disena para la curva exponencial --- pero incluye modo degradado. (Hipotesis de trabajo, no axioma.)

---

## 20. Apendice: Korvo-Korax

### 20.1 El sistema personal como laboratorio

Antes de que Xanpan::Agents fuera un documento, fue una practica. El sistema Korvo-Korax es un prototipo de esta metodologia a escala personal --- un equipo de un humano con un enjambre de uno. No es una implementacion perfecta; es un laboratorio donde las ideas se testean con friccion real.

### 20.2 Mapeo de conceptos

| Concepto Xanpan::Agents | Implementacion Korvo-Korax |
|---|---|
| Product Owner | Korvo (definicion de valor y direccion) |
| Operador | Korvo (dual-hat: configura y opera el sistema) |
| Enjambre | Korax + sub-agentes segun tarea |
| OKRs | GTD + sistema de proyectos con revisiones semanales |
| Evals | Invariantes PCA (Protocol de Coherencia Atencional) |
| Sentinel | Heartbeats + mecanismo de deteccion de colapso |
| Tarjetas purpura | Propuestas proactivas generadas en heartbeats |
| Context engineering | AGENTS.md + SOUL.md + MEMORY.md |
| Model Router | Fallback chain: sonnet, gpt-5.2, kimi, glm5 |
| Tablero Neural | Estado del workspace + metricas de sesion |

### 20.3 La violacion consciente: dual-hat PO/Operador

La implementacion personal viola deliberadamente la separacion de concerns que [-> 4. Roles Humanos] propone: Korvo es simultaneamente PO y Operador. Consecuencias predecibles:

- **Sesgo de confirmacion amplificado:** Quien define el valor es quien configura al ejecutor. No hay segundo par de ojos humano.
- **Fatiga atencional compuesta:** Mantener context engineering + evaluar entregas + definir valor consume el mismo recurso escaso (atencion humana) sin posibilidad de delegacion.
- **El PCA como compensador:** El Protocol de Coherencia Atencional es el mecanismo que compensa esta falta de separacion.

### 20.4 Lecciones observadas

1. **El context engineering es MAS dificil de lo que parece.** Mantener AGENTS.md actualizado es trabajo cognitivo significativo. Llevo a la propuesta de Sentinel como mantenedor de context ([-> 4.2 Operador: El Ingeniero de Enjambre]).
2. **Los heartbeats como proto-Sentinel funcionan.** La deteccion proactiva de problemas con propuestas de accion subordinadas a aprobacion humana es el patron mas robusto encontrado. Llevo al diseno del Sentinel y las tarjetas purpura.
3. **La diversidad de modelos importa.** Usar un solo provider crea blind spots. El fallback chain no es solo redundancia; es diversidad cognitiva. Llevo al principio de diversidad de modelos en [-> 17.1 Alucinacion sistemica].
4. **El backlog predictivo emerge naturalmente.** Cuando el agente tiene suficiente contexto, empieza a sugerir tareas antes de que el humano las piense.
5. **La curva exponencial se siente.** Lo que era imposible hace 6 meses ahora es rutina. Pero la sensacion no es lineal: hay mesetas seguidas de saltos. Llevo a tratar la exponencialidad como hipotesis con modo degradado ([-> 16. Velocidad Exponencial], [-> 17.5 Meseta de capacidad]).

### 20.5 Limitaciones como proof of concept

Korvo-Korax es un N=1. Las limitaciones son severas:

- No escala a equipos. Un sistema personal no demuestra que la metodologia funcione con multiples humanos.
- No tiene separacion de roles real. El dual-hat hace imposible validar que PO/Operador/Sentinel funcionen como roles independientes.
- No tiene metricas formales. No hay CpH, TA, ni Cycle Time instrumentados.
- Survivor bias. Se reporta lo que funciona; los fracasos se olvidan o se racionalizan.

La funcion de este apendice no es probar que Xanpan::Agents funciona. Es documentar que las ideas centrales --- context engineering, meta-agente supervisor, backlog predictivo, gobernanza humana de enjambre --- emergieron de la practica real antes de ser formalizadas. La teoria siguio a la experiencia, no al reves.

---

## 21. Validacion

| Check | Criterio | Accion si falla |
|---|---|---|
| Frontmatter valido | Parsea sin error, campos autorizados, version 2.1.0 | Corregir YAML |
| Numeracion secuencial | Secciones `##` numeradas 1 a 21 sin saltos | Renumerar |
| Keywords RFC 2119 en negrita | Toda keyword normativa (**DEBE**, **NO DEBE**, **DEBERIA**, **PUEDE**) en negrita | Formatear |
| Headings descriptivos | Ningun heading generico | Renombrar |
| Sin ambiguedad | Cada regla tiene exactamente una lectura | Reescribir o agregar ejemplo |
| Ejemplos presentes | Toda regla con complejidad semantica o riesgo de ambiguedad tiene par Correcto/Incorrecto | Agregar ejemplos |
| Sin prosa innecesaria | Toda prosa cumple funcion normativa (racionalizar, desambiguar, contextualizar) | Eliminar |
| Consistencia interna | Sin contradicciones no resueltas entre reglas. En particular: staging eliminado en favor de evals + feature flags (consistente en secciones 1.3, 12.1, 15.1 y 16.2) | Resolver conflicto |
| No-circularidad | Ningun termino definido circularmente | Reescribir definiciones |
| Definiciones completas | Todo termino clave del documento tiene entrada en seccion 2 | Agregar a seccion 2 |
| Referencias validas | Todo `(urn:...)` y `[-> N. Seccion]` resuelve | Corregir |
| 12 axiomas preservados | Seccion 19.3 contiene exactamente 12 axiomas | Verificar |
| P0 fix aplicado | No hay contradiccion sobre staging. Secciones 1.3, 12.1, 15.1 y 16.2 son consistentes | Verificar alineacion |
| P1a fix aplicado | Eval de diversidad presente en DoD (seccion 9.3 paso 6) | Verificar paso 6 |
| P2 fixes aplicados | LLM-as-a-Judge unificado, Korvo-Korax con guion, sin emoji | Buscar y corregir |
| Tablas con datos preservados | Todas las tablas del source con datos significativos estan presentes | Verificar completitud |
| Auto-suficiencia | Conceptos externos definidos inline o referenciados via URN | Agregar definicion |

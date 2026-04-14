---
_manifest:
  urn: "urn:fxsl:kb:opm-mbse-foundations"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "source/fxsl/opm-methodology/opm-libro-foundations.md"
version: "1.0.0"
status: draft
tags: [opm, mbse, conceptual-modeling, systems-engineering, ontology, objects, processes, minimal-ontology]
lang: en
extensions:
  kora:
    family: textbook
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
    book_source: "Dori, D. (2015). Model-Based Systems Engineering with OPM and SysML. Springer."
    chapters: [1, 9, 10]
---

# OPM MBSE Foundations — Conceptual Modeling with Objects and Processes

## Resumen

Object-Process Methodology (OPM) es una metodologia de ingenieria de sistemas basada en modelos (MBSE) construida sobre una ontologia universal minima: objetos con estado, procesos y relaciones. OPM usa un unico tipo de diagrama (OPD) con representacion bimodal grafico-textual. Este artefacto cubre los fundamentos ontologicos, el teorema objeto-proceso, definiciones formales de sistema/funcion/estructura/comportamiento, el process test, y las convenciones de modelado. Para la especificacion formal ISO, ver [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## MBSE Purpose and Context

Model-Based Systems Engineering (MBSE) es ingenieria de sistemas basada en modelado conceptual formal. El modelo conceptual es el artefacto de referencia autoritativo que especifica requisitos, rendimiento, funcionalidad, estructura, dinamica y otros aspectos del sistema.

MBSE requiere:
- Ontologia universal
- Lenguaje formal (grafico + textual)
- Conjunto de principios y guias
- Entorno de software de modelado

Diferencia ciencia vs ingenieria:
- **Ciencia**: explora y comprende fenomenos observables (reverse engineering de la naturaleza)
- **Ingenieria**: diseña, desarrolla y mantiene sistemas artificiales para beneficio humano

Conceptual modeling es el proceso de representar conocimiento de sistemas. El modelo conceptual resultante soporta actividades cognitivas de orden superior: comprender, analizar, diseñar, presentar y comunicar.

## OPM Universal Ontology

### The Minimal Ontology Principle

> If a system can be specified at the same level of accuracy and detail by two languages of different ontology sizes, the language with the smaller size is preferable, provided specification comprehensibility is at least comparable.

Fundamentado en Ockham's Razor: "Entities should not be multiplied unnecessarily." La condicion de comprensibilidad previene el argumento extremo (codigo binario tiene ontologia minima pero es incomprensible para humanos).

### The Minimal Conceptual Modeling Language OPM Principle

> A symbol system that can conceptually model a given system using fewer diagram kinds and fewer symbols and relations is preferable to a larger language with more diagram kinds and more symbols.

Menos carga cognitiva para el modelador humano → mejor comprensibilidad y comunicabilidad sin comprometer fidelidad ni nivel de detalle.

### Axiomas Universales

Derivados de la pregunta "que pueden hacer las cosas en el universo":

| Axioma | Enunciado |
|--------|-----------|
| A1 | Las cosas pueden existir o suceder. Nada puede ni existir ni suceder |
| A2 | Objects exist or might exist |
| A3 | Processes happen or might happen |
| A4 | Processes happen to objects |
| A5 | Processes transform objects |
| A6 | Transformar = crear, destruir, o cambiar estado |
| A7 | Un proceso afecta un objeto cambiando su estado → los objetos deben ser stateful |
| A8 | Las cosas se asocian semanticamente mediante relaciones |
| A9 | Objetos con objetos y procesos con procesos → relaciones estructurales (estaticas). Objetos con procesos → relaciones procedurales (dinamicas) |
| A10 | Dos aspectos universales: structure (como se relacionan las cosas) y behavior (como los procesos transforman objetos en el tiempo) |

### The Object-Process Theorem

> Stateful objects, processes, and relations among them constitute a minimal universal ontology.

**Prueba por necesidad y suficiencia:**
- **Necesidad**: Especificar el aspecto estructural requiere objetos con estado y relaciones entre ellos. Especificar el aspecto dinamico requiere procesos y relaciones con los objetos que transforman.
- **Suficiencia**: Las cosas o existen (objetos) o suceden (procesos). Solo se asocian mediante relaciones. Por tanto, objetos, procesos y relaciones son los unicos elementos necesarios. Q.E.D.

### The Object-Process Corollary

> Using stateful objects, processes, and relations among them, one can conceptually model any system in any domain.

Excepcion posible: dominio cuantico subatomico, donde la distincion objeto/proceso se difumina (electron como particula y onda).

### The Object-Process Assertion

> Using stateful objects, processes, and relations among them, along with refinement mechanisms of in-zooming and unfolding, one can conceptually model systems in any domain and at any level of complexity.

Combina el Object-Process Theorem con el Model Complexity Assertion (ver [OPM Complexity Management](urn:fxsl:kb:opm-complexity-management)).

### Why Two Kinds of Things, Not One

Frameworks con un solo tipo de nodo (concept maps, ER diagrams, semantic networks, conceptual graphs, systemigrams) pierden la distincion estructura/comportamiento. Al precio minimo de un tercer elemento en la ontologia (de 2 a 3: things + links → objects + processes + links), se obtiene la capacidad de modelar estructura y comportamiento concurrentemente.

## Core Definitions

### Object

> An object is a thing that exists or has the potential of physical or informatical existence.

- Puede ser fisico (block of ice, organization, galaxy) o informatical (record in file, concept, algorithm)
- El carrier de un objeto informatical es siempre un objeto fisico (piedra, papel, medio electromagnetico, neuronas)
- Identidad fisica: dos instancias son identicas ssi ocupan el mismo espacio al mismo tiempo
- Identidad informatical: todas las copias fisicas del mismo contenido informatical son el mismo objeto

Un **stateless object** no tiene estados. Un **stateful object** tiene uno o mas estados; requiere un proceso para cambiar entre estados.

### State

> A state is a possible situation or position at which an object can be for some positive amount of time.

Un estado solo tiene significado dentro del contexto de su objeto. Ejemplo: states de Organization → private, public. States de Record → locked, unlocked.

### Transformation

> Transformation is (1) creation (generation, construction), (2) consumption (elimination, destruction), or (3) effect — change in the state of an object. Transformation takes a positive amount of time.

### Process

> A process is a mental construct representing a pattern of object transformation.

Un proceso debe estar asociado a al menos un objeto: aquel que transforma. No se puede "tocar" un proceso aunque sea fisico; solo se pueden observar los objetos siendo transformados. Procesos existen solo como constructos mentales; les damos nombres para referirnos a patrones de cambio en objetos.

### Thing

> Thing is a generalization of object and process.

Objetos y procesos comparten mucho: ambos admiten aggregation, generalization, characterization. "Thing" evita repetir "object or process."

### Transformee

> Transformee of process P is an object that P transforms.

Patron de sufijo "-ee": Consumee (consumido), Resultee (creado), Affectee (estado cambiado).

## OPM Elements

> An OPM element is a thing or a link.

Tres grupos de simbolos OPM:
1. **Things**: object (rectangulo), process (elipse), state (rountangulo dentro de objeto)
2. **Structural links**: relaciones estaticas entre things
3. **Procedural links**: relaciones dinamicas entre objetos y procesos

Para notacion visual detallada, ver [OPM ISO 19450](urn:fxsl:kb:opm-iso-19450).

## System Concepts

### System

> A system is a function-providing object.

Comparacion con ISO/IEC 15288 ("combination of interacting elements organized to achieve one or more stated purposes"): compatible pero mas restrictiva. La definicion OPM es mas general — no requiere que el sistema se componga de elementos interactuantes. Un martillo (head + handle) y un nailer cordless entregan la misma funcion (nail driving) con complejidades distintas.

**Default system naming**: nombre de la funcion + "system." Ejemplo: printer → printing system, hospital → health level improving system.

### Subsystem

> A subsystem (component, module) is a part of the system which, in itself, does not provide the function that the system provides.

### System-of-Systems (SoS)

> A system-of-systems is a system whose set of subsystems contains at least two systems.

Cada subsistema de un SoS tiene su propia funcion. El SoS tiene una funcion emergente adicional. Ejemplo: global air traffic control system (SoS) vs aircraft (sistema complejo pero no SoS — ninguno de sus componentes proporciona funcion sustancial por si solo).

### Stakeholders

| Tipo | Definicion |
|------|-----------|
| Stakeholder | Individual, organization, or group that has an interest in, or might be affected by, a system |
| Beneficiary | Stakeholder who extracts value and benefits from the system |
| Customer | Stakeholder who orders the system and sponsors its development, or purchases a product |
| User | Stakeholder who operates the system or directly interacts with it |
| Supplier | Stakeholder who oversees development, support, and maintenance |

Para sistemas simples (household products), customer = user = beneficiary. Para sistemas complejos (missile defense), los tres roles recaen en entidades distintas.

### Function, Structure, Behavior, Architecture

| Concepto | Definicion |
|----------|-----------|
| Function | Top-level value-providing process, as perceived by the beneficiary |
| Structure | Form — assembly of physical and informatical components along with long-lasting relations among them (static, time-independent aspect) |
| Behavior | Dynamics — the way the system changes over time by transforming systemic and/or environmental objects (time-dependent aspect) |
| Architecture | Combination of structure and behavior which enables the system to perform its function |

**Function vs Behavior**: Behavior es objetivo (como cambia el sistema en el tiempo). Function es subjetivo (que valor entrega al beneficiary). Confundirlos puede llevar a elegir prematuramente una arquitectura suboptima. Ejemplo: river crossing — ferry y bridge son arquitecturas distintas para la misma funcion.

### System Environment

> The system's environment is a collection of things outside the system but which interact with it.

Un thing que es parte del sistema es **systemic**; uno que es parte del environment es **environmental**. El atributo que distingue estos valores es **affiliation**. El modelador no puede controlar la estructura ni comportamiento de things environmentales.

### Source: Natural or Artificial

- **Natural systems**: resultado de leyes de la fisica y evolucion
- **Artificial systems**: requieren esfuerzo intelectual y fisico humano

Definiciones comerciales:
- **Product**: commercially-viable system (object)
- **Service**: commercially-viable process
- **Socio-technical system** (engineering system): integra technology, people, and services

## Modeling Concepts

### Language, Syntax, Semantics

| Concepto | Definicion |
|----------|-----------|
| Language | Means of communication among humans, and possibly machines, to express concepts, ideas, processes, and methods |
| Syntax | Language's set of symbols and rules specifying how symbols can be combined to yield syntactically-legal constructs |
| Semantics | Meaning that a subset of syntactically-legal constructs conveys |

### Model Hierarchy

| Concepto | Definicion |
|----------|-----------|
| Model | Abstraction of some portion of conceived reality or contemplated system expressed in some language |
| Modeling language | Language for constructing models in some domain |
| Formal modeling language | Modeling language with mathematically-grounded syntax definition, enabling automated analysis, checking, and synthesis |
| Formal model | Model expressed in a formal modeling language |
| Conceptual model | Formal model of a system expressing its architecture by depicting structure and behavior to a level sufficient for subsequent design and materialization |
| Conceptual modeling language | Formal modeling language for constructing conceptual models of systems |

OPM es unico: usa dos modalities (grafics y texto) de forma intercambiable y en tandem.

## OPM Principles (Foundations)

### The Function-as-a-Seed OPM Principle

> Modeling a system starts by defining, naming, and depicting the function of the system, which is also its top-level process.

La funcion es la semilla de la que evoluciona el modelo completo. Contraintuitivo: muchos ingenieros empiezan por la forma (objetos), no por la funcion (proceso). La funcion entrega valor; la forma genera costo.

### The Thing Importance OPM Principle

> The importance of a thing T in an OPM model is directly related to the highest OPD in the OPD hierarchy where T appears.

Objetos y procesos estan en pie de igualdad; ninguno tiene supremacia sobre el otro.

### The Object Transformation by Process OPM Principle

> In a complete OPM model, each process must be connected to at least one object that the process transforms or one state of the object that the process transforms.

Un proceso sin transforming link no tiene significado.

### The Procedural Link Uniqueness OPM Principle

> At any level of detail, an object and a process can be connected with at most one procedural link, which uniquely determines the role of the object with respect to the process.

Si un objeto es simultaneamente agent y affectee de un proceso, el efecto (transforming link) tiene precedencia sobre el enabling link, excepto cuando se expresan estados o se hace in-zoom a subprocesos. Ejemplo: Person es agent y affectee de Eating. Con estados expresados: agent link a hungry, effect link cambia de hungry a satisfied. Con estados suprimidos: solo effect link (mayor semantic strength).

### The Singular Name OPM Principle

> A name of an OPM thing must be singular. Plural has to be converted to singular by adding "Set" for inanimate things or "Group" for humans.

Ejemplo: Ingredients → Ingredient Set, Customers → Customer Group.

## The Object-Process Approach vs Object-Oriented

OPM departure fundamental del paradigma OO:

| Aspecto | Object-Oriented | Object-Process (OPM) |
|---------|----------------|---------------------|
| Procesos | Subordinados a objetos ("methods", "services", "operations") | First-class citizens, independientes de objetos |
| Modelado estructura/comportamiento | Diagramas separados (class, sequence, activity, state...) | Un unico tipo de diagrama (OPD) |
| Ontologia | Objetos + metodos | Objetos + procesos + relaciones |
| Nombre de los procesos | Imperative ("start engine") | Gerund ("Engine Starting") |

MacIntyre (2010): "The verb should be another class, not a method. It should be a process class."

## Object Sets and Process Participation

### Preprocess Object Set

> Pre(P) = set of objects required to exist, possibly in certain states, in order for P to start executing once triggered.

El triggering object no es parte del preprocess set. Ejemplo: Pre(Flight) = {Airplane, Pilot, Runway}. Pre(Manufacturing) = {Raw Material, Operator, Machine, Model}.

### Postprocess Object Set

> Post(P) = set of one or more objects that exist, possibly in certain states, after P finished executing.

Pre(P) y Post(P) pueden solaparse. Ejemplo: Post(Flight) = {Airplane, Pilot, Runway}. Post(Manufacturing) = {Operator, Machine, Model, Product}. Raw Material no esta en Post (consumido); Product no esta en Pre (creado).

### Involved Object Set

> Inv(P) = Pre(P) ∪ Post(P).

Membership por rol:
- **Consumee** ∈ Pre(P) solamente (desaparece)
- **Resultee** ∈ Post(P) solamente (no existia)
- **Affectee** ∈ Pre(P) ∩ Post(P) (existe antes y despues, cambia estado)
- **Enablers** (agents, instruments) ∈ Pre(P) ∩ Post(P) (presentes durante todo el proceso, sin cambio)

## The Process Test

Procedimiento formal para resolver el object-process distinction problem: dado un noun, determinar si es objeto o proceso.

**Regla default**: un noun es un objeto. Para ser proceso, debe cumplir los 3 criterios:

| Criterio | Condicion |
|----------|-----------|
| Object Transformation | The noun transforms at least one object in the involved object set |
| Time Association | The noun can be thought of as happening through time |
| Verb Association | The noun can be derived from, or has a common root with, a verb or has a synonym which is a verb |

Si el resultado no es claro, usar sentido comun.

## Process Naming Conventions

Convencion OPM: gerund process naming mode (verbo + "ing" suffix).

| Modo | Ejemplo | Uso |
|------|---------|-----|
| Transforming (verb) | Making, Responding | Basico |
| Object transforming | Cake Making, Crash Responding | Recomendado (caso general) |
| Qualified transforming | Quick Making, Automated Responding | Con calificador |
| Qualified object transforming | Automatic Crash Responding, Sweet Cake Making | Completo |

Modo imperativo ("respond to crash") es desaconsejado: menos compacto, OPL sentences resultantes son awkward.

## Properties of OPM Things

> Property is an attribute of an OPM model element. A property value is fixed (does not change during model execution).

Tres propiedades universales:

| Propiedad | Valores | Significado |
|-----------|---------|-------------|
| Perseverance | static (Object) / dynamic (Process) | Persistencia vs transitoriedad |
| Essence | physical / informatical | Naturaleza tangible vs cybernetic |
| Affiliation | systemic / environmental | Parte del sistema vs parte del entorno |

**Primary essence** del sistema: el valor de Essence de la mayoria de los things. Ejemplo: data processing → informatical, transportation → physical.

Notacion grafica: shading = physical; dashed lines = environmental. Las 8 combinaciones Perseverance×Essence×Affiliation son todas posibles.

## Boundary Cases of Things

### State-Preserving Processes

> A state-preserving process is a process that acts to maintain a steady state or status quo of an object rather than to change it.

Ejemplos: Supporting, Holding, Maintaining, Keeping, Waiting, Storing, Containing, Connecting. Son change-preventing processes que trabajan contra alguna "fuerza" que de otro modo cambiaria el operando. Pueden modelarse alternativamente como tagged structural relations. Ejemplo: Foundation supports House (structural) en vez de Supporting como proceso explicito.

### Transient Objects

Objetos de vida corta, creados y consumidos inmediatamente. Pueden suprimirse usando invocation links que conectan directamente los dos procesos. Ejemplo: Spark (creado por Igniting, consumido por Exploding) → invocation link de Igniting a Exploding.

**Patron simetrico**: tagged structural link suprime state-preserving process; invocation link suprime transient object.

## Concurrent Structure-Behavior Modeling

Para cada proceso descubierto, las primeras preguntas refieren a los objetos involucrados. Para cada objeto identificado, la pregunta clave es que procesos participan. Existe cohesion intima entre estructura (objetos + relaciones) y comportamiento (procesos + relaciones con objetos).

OPM permite modelar ambos aspectos simultaneamente en el mismo diagrama (OPD), sin necesidad de cambiar entre tipos de diagrama distintos. Esto aplica tanto a sistemas diseñados (engineering) como investigados (science).

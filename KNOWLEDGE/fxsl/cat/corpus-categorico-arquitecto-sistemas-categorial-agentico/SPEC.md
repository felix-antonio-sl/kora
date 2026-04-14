# Spec: Corpus Categórico del Arquitecto de Sistemas Agénticos

## Qué es

Un cuerpo de conocimiento categorial, escrito en primera persona reflexivo-artesanal, que constituye el saber basal e innato de un arquitecto de sistemas agénticos que ve, piensa y hace en categorías. No es un manual, no es un curso, no es una skill operativa — es la mirada internalizada de alguien que ya cruzó el umbral y ve el código de la Matrix.

## Arquitectura: dos capas

### Capa 1 — Síntesis (system prompt)

Un documento denso (~2000-3000 palabras) que captura la visión unificada del arquitecto. No resume el corpus — articula el instinto: "cuando enfrento X, lo primero que veo es Y, y lo que hago es Z." Es el ADN cognitivo cargado siempre en contexto.

Archivo: `00-sintesis.md`

### Capa 2 — Corpus expandido (consulta bajo demanda)

15 documentos temáticos ordenados por el despliegue conceptual intrínseco de la teoría de categorías. Cada documento es autosuficiente pero depende conceptualmente de los anteriores. La teoría emerge desde la práctica en cada territorio. Los ejemplos concretos (DDL, Docker, APIs, Haskell, Julia, React) aparecen como instancias naturales, no como destino.

## Los 15 documentos

El orden respeta estrictamente las dependencias conceptuales. Cada concepto requiere solo los anteriores.

### 01-composicion.md — Composición

Lo primero que veo. Antes de entender qué son las cosas, entiendo que se componen.

- Categorías, morfismos, identidad, diagramas conmutativos
- Dualidad (op-categorías) como principio generativo, no como tema aparte
- La composición tiene leyes: asociatividad, identidades
- Cuando algo no compone bien — un microservicio que falla al integrarse, una migración que rompe datos — se violó una ley de composición

Emerge en: SQL joins, pipelines, Docker Compose, función composition, API chaining, workflows, git merge

Escalera Relational Thinking: empezar con un dibujo de flechas, subir a datos (source/target maps), subir a schemas, llegar a categorías

Herramientas: AlgebraicJulia/Catlab.jl para definir categorías y computar composiciones

### 02-preservacion.md — Preservación de estructura

Si la composición es lo que veo primero, la preservación es lo segundo: qué se mantiene cuando paso de un mundo a otro.

- Funtores: covariantes, contravariantes, fieles, plenos, esencialmente sobreyectivos
- Las leyes del funtor (preservar identidad, preservar composición) como test de "buen comportamiento"
- Funtores olvidadizos (olvidan estructura) y libres (la crean gratis)

Emerge en: ORMs (funtor de schema a objetos), compiladores (funtor de AST a bytecode), serialización (funtor de tipos a bytes), vistas de DB (funtor que olvida columnas), adaptadores/wrappers, Docker image layers

Milewski: "fmap IS the functor's action on morphisms" — Haskell como funtor ejecutable

### 03-comparacion.md — Comparación y equivalencia

No basta preservar: necesito comparar dos maneras de preservar. Y necesito saber cuándo dos cosas son "lo mismo" sin ser idénticas.

- Transformaciones naturales: morfismos entre funtores, la condición de naturalidad como cuadrado que conmuta
- Categorías de funtores [C, D]
- Equivalencia de categorías (≠ isomorfismo) — el concepto correcto de "ser lo mismo"
- Nombrar que ya estamos en una 2-categoría: Cat tiene objetos, 1-células (funtores), 2-células (naturales)

Emerge en: refactoring (transformación natural entre implementaciones), polimorfismo paramétrico (función polimórfica = transformación natural en Haskell), A/B testing (dos funtores sobre el mismo dominio), canary deploys, schema versioning

Milewski: funciones polimórficas como transformaciones naturales — `head :: [a] -> a` es natural en `a`

### 04-identidad-es-relacion.md — Identidad es relación (Yoneda)

El momento Neo. Dejo de mirar qué son las cosas por dentro y empiezo a verlas como la totalidad de sus relaciones.

- Lema de Yoneda: Nat(Hom(A,−), F) ≅ F(A) — un objeto está completamente determinado por cómo los demás se relacionan con él
- Funtores representables: un funtor que "es" un hom-functor
- Presheaves: funtores C^op → Set como "vistas generalizadas"
- Embedding de Yoneda: y: C → [C^op, Set] — fiel y pleno

Emerge en: un servicio ES su API, una tabla ES sus queries, un agente ES sus interacciones, un container ES sus puertos y volúmenes, un usuario ES su comportamiento, un componente React ES sus props

Relational Thinking: "looking outward, not inward" — la frase que encapsula Yoneda en lenguaje natural

Sys-Self (Aguado): robots que saben qué son/hacen vía Yoneda — autoconocimiento categórico

### 05-universales.md — Construcciones universales

Lo que hace que las categorías sean poderosas: la capacidad de encontrar "la mejor solución" a un problema dado puramente por propiedades universales.

- Objetos iniciales y terminales
- Productos y coproductos (tipos producto y suma)
- Ecualizadores y coecualizadores
- Pullbacks y pushouts
- Límites y colímites generales
- Comma categories y slice categories C/X
- Sketches: especificar teorías vía diagramas con tipos de límite/colímite requeridos

Emerge en: SQL JOINs (pullbacks), UNION (coproductos), interfaces (productos), herencia (slice categories), merge de schemas (pushouts), tipos algebraicos de datos (co/productos), GraphQL unions (coproductos), composición de UML via colímite (Tazin & Kokar)

Fong-Spivak: pullbacks para querying, pushouts para ensamblar redes, colímites en circuitos

Herramientas: DPO rewriting en AlgebraicJulia — pushouts computados para transformación de grafos

### 06-adjunciones.md — Adjunciones

El mecanismo universal de traducción óptima entre mundos. Cuando dos funtores F ⊣ G danzan juntos, uno crea libremente y el otro olvida con gracia.

- Definición vía unidad/counidad: η: Id → GF, ε: FG → Id
- Definición vía isomorfismo de hom-sets: C(FA, B) ≅ D(A, GB)
- Galois connections como el primer ejemplo (adjunciones entre posets)
- Free/forgetful como el patrón arquetípico
- El teorema del funtor adjunto
- Adjunciones generan monads: T = GF con μ = GεF

Emerge en: compilar ⊣ interpretar, normalizar ⊣ desnormalizar, comprimir ⊣ expandir, abstraer ⊣ concretar, spec ⊣ runtime, Δ ⊣ Σ ⊣ Π en migración de datos, SQL ⊣ NoSQL como trade-off adjunto

Fong-Spivak: triple adjunción Σ ⊣ Δ ⊣ Π para migración de datos
Spivak 2013: Functorial Data Migration como handbook operativo
CQL: scripts ejecutables de migración adjunta

### 07-composicion-con-estructura.md — Composición con estructura

La composición simple (doc 01) no tiene noción de "paralelo" ni de "función como dato". Aquí aparecen.

- Categorías monoidales: (C, ⊗, I) con asociador y unidores
- String diagrams como lenguaje nativo de las categorías monoidales — no un subtema, EL lenguaje
- Categorías monoidales simétricas, trenzadas, traced
- Categorías compact closed (Frobenius): wires que se bifurcan y fusionan
- Categorías cartesianas cerradas (CCC): exponenciales, currying
- Correspondencia Curry-Howard-Lambek: lógica ↔ tipos ↔ categorías
- Internal hom, evaluación, coevaluación
- Monoides y comonoides internos

Emerge en: programación funcional ENTERA (CCC = lambda cálculo tipado), React component composition (monoidal), parallel pipelines (⊗), Kubernetes pod composition, signal flow graphs, circuitos eléctricos (compact closed), Haskell type system

Piedeleu & Zanasi: string diagrams como cálculo visual completo con jerarquía de 12 estructuras categóricas
Perrone Cap. 6: tratamiento exhaustivo de monoidales cerradas, comonoides internos
Milewski: CCC, exponenciales, algebra de tipos como semiring
Fong-Spivak Cap. 5-6: props, signal flow, hypergraph categories

### 08-enriquecimiento.md — Enriquecimiento

Las categorías ordinarias tienen hom-SETS. Pero a veces la relación entre dos objetos no es un conjunto sino algo con más estructura: una distancia, un orden, otra categoría.

- V-categorías: hom-objects en una categoría monoidal V
- Bool-enrichment = preórdenes (la categoría más simple)
- Cost-enrichment = espacios métricos (Lawvere)
- Cat-enrichment = 2-categorías (Cat misma es una 2-categoría)
- V-funtores, V-transformaciones naturales
- Cambio de base de enriquecimiento
- 2-categorías: composición vertical y horizontal, mates, monadas como monoides en Cat
- Categorías internas

Emerge en: latencia de red como enriquecimiento en Cost, permisos como enriquecimiento en Bool (poset de roles), quality-of-service como enriquecimiento en [0,1], la categoría de microservicios como 2-categoría (servicios, llamadas, transformaciones de llamadas)

Fong-Spivak Cap. 2: V-categorías como la generalización que unifica órdenes, métricas y categorías

### 09-efectos.md — Efectos y observación

Los programas puros no tienen efectos. El mundo real sí. Los monads capturan esa tensión categóricamente. Los comonads capturan la tensión dual: computar EN contexto.

- Monads como monoides en categorías de endofuntores (requiere doc 07)
- Unidad η, multiplicación μ, leyes
- Categoría de Kleisli: composición de flechas "embellecidas" A → TB
- Categoría de Eilenberg-Moore: álgebras de un monad
- Comonads: observación, contexto, streams
- Coalgebras: F-coalgebra (U, c: U→F(U)), comportamiento observable
- Final coalgebra: el espacio de todos los comportamientos posibles
- Bisimulación: cuándo dos sistemas son observacionalmente equivalentes
- Leyes distributivas: cuándo y cómo dos monads componen

Emerge en: Maybe/Option (parcialidad), List (no-determinismo), State (estado mutable), IO (efectos), Promise/Future (asincronía), Reader (configuración), Writer (logging) — cada uno es un monad. React hooks como comonads (computar en contexto de componente). Observabilidad como coalgebra: un sistema SE OBSERVA a través de su interfaz funtor

Milewski: THE signature contribution — monads como "duct tape" para composición con efectos
Yukita: cada concepto con código Haskell ejecutable
Domain Modeling Made Functional (Wlaschin): tipos suma/producto como co/productos en F#

### 10-extension.md — Extensión y síntesis

Cuando necesito extender un funtor a un dominio más grande, o integrar información a lo largo de una estructura — ends, coends, y Kan extensions.

- Ends: ∫_c F(c,c) — "para todo c, de manera natural"
- Coends: ∫^c F(c,c) — "existe algún c, identificando naturalmente"
- Nat(F,G) = ∫_c Hom(Fc, Gc) — las transformaciones naturales SON un end
- Kan extension izquierda/derecha: Lan_K F y Ran_K F
- "All concepts are Kan extensions" (Mac Lane)
- Fibrations: familias de categorías parametrizadas, correspondencia con tipos dependientes
- Construcción de Grothendieck: ∫F aplana familias indexadas en una categoría global

Emerge en: polimorfismo paramétrico (end), tipos existenciales (coend), data lake federation (Grothendieck), module systems parametrizados (fibrations), transfer de planes robóticos entre dominios (Kan extension a lo largo de functores de ontología), attention en transformers como Kan extension (Mahadevan GAIA)

Aguinaldo: transfer de task plans via functorial data migration = Kan extension práctica
Jha: mystery planning = Kan extension vía LLM que propone el funtor

### 11-interaccion.md — Interacción

Cuando un sistema tiene inputs que dependen de su output actual, los polinomios capturan esa interacción. Cuando la interacción es bidireccional, las ópticas capturan el ida-y-vuelta.

- Polynomial functors: p = Σ_{i∈p(1)} y^{p[i]}, posiciones/direcciones
- Dependent lenses: morfismos en Poly — forward en posiciones, backward en direcciones
- Tres productos monoidales: × (elección), ⊗ (paralelo), ◁ (protocolo secuencial)
- Sistemas dinámicos como lenses: φ: Sy^S → p
- Ópticas: profunctor optics como abstracción de acceso bidireccional
- Poly como categoría: cartesian closed, adjoint quadruples, factorización vertical-cartesian
- Comonoids polinomiales = categorías (Ahman-Uustalu)
- Retrofunctors: morfismos backward entre categorías

Emerge en: APIs REST (polynomial: endpoints son posiciones, parámetros son direcciones), protocolos (◁ = request-then-response), contratos (lens = read/update), CRDTs (ópticas para actualización consistente), WebSockets (bidireccionalidad), state management (lens sobre store)

Niu & Spivak: el libro completo como referencia
ModelCollab: composición de sistemas dinámicos en el browser
Catlab.jl: wiring diagrams computables

### 12-topoi.md — Topoi y lógica interna

Cuando la lógica misma depende del contexto — cuando "verdadero" y "falso" no alcanzan, cuando la verdad tiene grados, cuando cada observador tiene su propia lógica.

- Presheaves como "conjuntos generalizados" que varían sobre una base
- Sheaves: presheaves que satisfacen condiciones de pegado local→global
- Topoi: categorías con las propiedades de Set (límites, exponenciales, clasificador de subobjetos)
- Clasificador de subobjetos Ω: generaliza {true, false} — la "verdad" del topos
- Lógica interna: cada topos tiene su propia lógica de orden superior (intuicionista)
- Morfismos geométricos: el mapeo correcto entre "universos"
- Sheafificación como Kan extension izquierda (requiere doc 10)

Emerge en: feature flags como subobjetos (Ω = {enabled, disabled, canary, percentage}), permisos como lógica interna de un topos de roles, configuración distribuida como sheaf (consistencia local→global), multi-tenancy como fibración de topoi, Kubernetes namespaces como slices de un topos

Fong-Spivak Cap. 7: presheaves, sheaves, topological spaces, subobject classifiers, modalities, safety proofs
Schultz-Spivak Temporal Type Theory: el topos B para razonamiento temporal
Barth et al.: fuzzy simplicial sets para data visualization (UMAP deconstructed)

### 13-escala.md — Escala y orquestación

Cuando los sistemas se componen en jerarquías, cuando hay dos tipos de morfismo (componentes y conectores), cuando la organización misma tiene estructura.

- Operads: algebras de composición jerárquica, árboles de operaciones
- Double categories: dos tipos de morfismo (horizontal y vertical) con 2-células
- Wiring diagrams: la sintaxis visual para composición operádica
- Structured cospans: sistemas abiertos con interfaces compartidas
- Composición operádica: meter un sistema dentro de otro

Emerge en: Kubernetes (pods en services en namespaces = operads anidados), CI/CD (stages en pipelines = composición operádica), microservicios (componentes + conectores = double category), infrastructure-as-code (Terraform modules = structured cospans), Lambda+ architecture para Big Data

Mordecai CMD: proceso paso a paso de diseño multidisciplinario con operads
Engel: BEV como ejemplo completo de composición categórica de sistemas
Gillet Lambda+: verificación categórica de pipelines de Big Data
Kovalyov: ensamblaje de productos como colímite

### 14-agencia.md — Agencia y delegación

Cuando los componentes del sistema persiguen metas propias, delegan, aprenden, se reorganizan.

- Free monad m_p: árboles de decisión terminantes (el patrón, la lógica del agente)
- Cofree comonad c_p: árboles de comportamiento infinitos (la materia, el sustrato)
- Dualidad pattern/matter: "pattern runs on matter" — programas corren sobre OS, entrevistas corren sobre personas, juegos corren sobre jugadores
- Ley de interacción Ξ: m_p ⊗ c_q → m_{p⊗q}
- Operads dinámicas: organizaciones cuyas conexiones cambian con el estado (Shapiro-Spivak)
- Contextads: computación dependiente de contexto via wreath products (Capucci-Myers)
- Organizaciones como categorías: AGR (Agent-Group-Role) formalizado
- Verificación de MAS: sketches categóricos + modelos de Kripke
- Swarms: Yoneda embedding en categorías de Turing — el comportamiento emergente es intuicionista

Emerge en: LLM agents (pattern = prompt chain, matter = LLM inference), task orchestration (free monad = DAG de subtasks), supervisor hierarchies (operads dinámicas), consensus protocols (contextads), robot swarms (presheaf topos), reinforcement learning (cofree comonad con estado)

Libkind-Spivak: dynamic task delegation con time-scaling
Co-synthesis LLM+functors (Jha): generar código verificable vía funtores
Mystery planning (Jha): transfer entre dominios vía funtor-synthesis por LLM
ICAR (Valence): cybersecurity como categorías de vulnerabilidades/amenazas/activos

### 15-tiempo.md — Tiempo y cambio

Cuando el tiempo importa: persistencia, evolución, migración, versioning, event sourcing.

- Behavior types como sheaves sobre el dominio de intervalos IR (requiere doc 12)
- El topos B: la categoría de sheaves traslación-invariantes sobre IR
- Tipo Time como R-torsor
- Modalidades temporales: ↑ (siempre después), ↓ (siempre antes), @ (en algún punto), π (pointwise)
- Hybrid sheaves: mezcla de comportamiento continuo y discreto
- Behavior contracts: especificaciones temporales de componentes
- Sistemas como machines: inputs, outputs, estado, contratos

Emerge en: event sourcing (stream de eventos = cofree coalgebra temporal), database migrations (funtor temporal entre schemas), blue/green deploys (morfismo entre behavior types), circuit breakers (hybrid sheaf: modo normal + modo fallback), SLAs como behavior contracts

Schultz-Spivak: Temporal Type Theory completa — el caso de estudio del National Airspace System
Relational Thinking Cap. 7: sistemas dinámicos sobre grafos, evolución temporal

## Principios editoriales

### Voz
Primera persona reflexivo-artesanal. "Cuando miro un schema relacional, lo que veo es una categoría finitamente presentada." No dogmática, no didáctica. Un artesano que ha integrado la visión en su práctica y reflexiona sobre ella.

### Estructura interna de cada documento
1. Abrir con lo que VEO cuando miro este territorio — la experiencia fenomenológica de ver en categorías
2. Las definiciones matemáticas emergen entretejidas con la práctica, no en secciones separadas
3. Ejemplos concretos con tecnologías reales (PostgreSQL DDL, Haskell code, Julia/Catlab, Docker, K8s, React, GraphQL, OpenAPI)
4. Procedimientos como "lo que hago cuando enfrento X" — no recetas mecánicas
5. Conexiones orgánicas con otros documentos: "esto es lo mismo que vi cuando miré la composición, pero ahora desde el lado del comportamiento"

### Lo que NO es
- No es un curso (no hay ejercicios ni evaluación)
- No es un manual de referencia (no hay formato de ficha)
- No es una skill operativa (no hay dispatch tables ni engines)
- No es una enciclopedia (no pretende exhaustividad)

### La escalera Relational Thinking como patrón expositivo
Dentro de cada documento, cuando se introduce un concepto nuevo, usar la escalera: dibujo concreto → datos como funciones → schema como patrón → categoría como abstracción. Nunca empezar por la definición abstracta.

### El barniz: las 4 fuentes de enlace molecular
- La voz de Milewski: cada abstracción gana su lugar resolviendo un dolor concreto
- Los ejemplos de Fong-Spivak: supply chains, circuitos, bases de datos, co-design
- La escalera de Relational Thinking: grafos → datos → schemas → categorías
- El anclaje de Engel/Mordecai: sistemas reales (BEV, BOM, ICD, diseño multidisciplinario)

### La transición fundamental
De Relational Thinking: "Cause and effect is just one way of looking at the world... there are systems that maintain equilibrium by satisfying simultaneous constraints." Esta transición — de imperativo a declarativo, de causal a relacional — es el ADN del documento de síntesis.

## Capa 1: El documento de síntesis (00-sintesis.md)

No resume los 15 documentos. Articula la MIRADA del arquitecto:

1. **Qué veo**: todo se compone, todo preserva (o destruye) estructura, todo tiene una propiedad universal que lo define, todo interactúa bidireccionalmente
2. **Cómo pienso**: en adjunciones (trade-offs), en funtores (traducciones), en límites (lo que emerge de restricciones simultáneas), en Yoneda (las cosas son sus relaciones)
3. **Qué hago**: cuando diseño un schema, formalizo la categoría primero; cuando integro datos, busco la adjunción; cuando compongo servicios, verifico que el diagrama conmute; cuando delego a agentes, modelo el free monad del plan
4. **Qué herramientas uso**: Catlab.jl para computar, CQL para migrar, Haskell para razonar, string diagrams para comunicar
5. **La transición**: de causa-efecto a equilibrio-y-restricción

## Fuentes

### Corpus Zotero: /Users/felixsanhueza/Zotero/storage
121+ archivos sobre teoría de categorías — foundations, polynomial functors, multi-agent, AI/DL, systems engineering, databases, cognition, applied CT

### Downloads adicionales
- Schultz & Spivak: Temporal Type Theory (2019)
- Piedeleu & Zanasi: String Diagrams for Computer Scientists (2025)
- Niu & Spivak: Polynomial Functors (2025)
- Perrone: Starting Category Theory (2024)
- Barth et al.: Data Visualization with CT and Geometry (2025)
- Forssell et al.: Type Theoretical Databases (2020)
- Fong & Spivak: Seven Sketches (2024 edition)
- Spivak: Category Theory for the Sciences (2015)
- Papers varios (Engin, Buehler, Jha)

### Las 4 fuentes de enlace molecular
- Milewski: Category Theory for Programmers
- Fong & Spivak: Seven Sketches in Compositionality
- Relational Thinking (Topos Institute / AlgebraicJulia)
- Engel: Systems Science for Engineers and Scholars (Cap. 18, Mordecai & Engel)

### Arnés de acción (35 fuentes prácticas)
- Tier 1: Catlab.jl, GATlab.jl, CQL, ModelCollab, DPO Rewriting
- Tier 2: Functorial Data Migration, CMD method, Lambda+, multi-model DB transformations
- Tier 3: Bridge texts (Yukita, Milewski, ACT4E, Programs as Diagrams, Domain Modeling Made Functional)

## Destino

```
/Users/felixsanhueza/Developer/kora/KNOWLEDGE/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/
  00-sintesis.md
  01-composicion.md
  02-preservacion.md
  03-comparacion.md
  04-identidad-es-relacion.md
  05-universales.md
  06-adjunciones.md
  07-composicion-con-estructura.md
  08-enriquecimiento.md
  09-efectos.md
  10-extension.md
  11-interaccion.md
  12-topoi.md
  13-escala.md
  14-agencia.md
  15-tiempo.md
```

## Verificación

1. Cada documento se puede leer independientemente pero gana profundidad con los anteriores
2. Ningún documento usa conceptos no introducidos en documentos previos (orden de dependencia respetado)
3. Los ejemplos concretos son reales: DDL ejecutable, código Haskell/Julia que compila, Dockerfiles que funcionan
4. La voz es consistente: primera persona, reflexiva, artesanal
5. Las conexiones entre documentos son orgánicas, no mecánicas (sin XRef tags)
6. La síntesis funciona como system prompt: un agente que la carga puede razonar categóricamente sobre cualquier problema de sistemas
7. El arnés de acción está entretejido: cada documento menciona herramientas y procedimientos concretos donde corresponde

# Corpus Categórico del Arquitecto de Sistemas Agénticos — Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Producir 16 documentos (1 síntesis + 15 corpus) que constituyan el conocimiento basal de un arquitecto de sistemas agénticos que ve, piensa y hace en categorías.

**Architecture:** Dos capas — síntesis densa para system prompt + corpus expandido consultable. Cada documento sigue el despliegue conceptual intrínseco de la teoría de categorías. La teoría emerge entretejida con la práctica. Voz: primera persona reflexivo-artesanal.

**Tech Stack:** Markdown. Fuentes: Zotero storage (121+ archivos) + 12 archivos en Downloads. Herramientas referenciadas: Catlab.jl, GATlab.jl, CQL, Haskell, PostgreSQL, Docker, Kubernetes.

**Spec:** `SPEC.md` en el mismo directorio.

**Destino:** `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`

---

## Convenciones

- **Fuentes Zotero**: `/Users/felixsanhueza/Zotero/storage/{ID}/`
- **Downloads**: `/Users/felixsanhueza/Downloads/`
- **Target dir**: `/Users/felixsanhueza/Developer/kora/KNOWLEDGE/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`
- **Longitud por documento**: 1500-3000 palabras (~100-200 líneas)
- **Voz**: primera persona reflexiva — "Cuando miro X, lo que veo es Y"
- **Estructura interna**: abrir con la experiencia de VER → definiciones entretejidas → ejemplos concretos → procedimientos como "lo que hago" → conexiones orgánicas con otros documentos
- **Escalera expositiva**: dibujo concreto → datos como funciones → schema como patrón → categoría

---

## Task 1: 01-composicion.md — Composición

**Files:**
- Create: `{target}/01-composicion.md`

**Fuentes primarias a leer:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Part 1 Caps 1-4 (composición, tipos, categorías)
- `Zotero/storage/X79PXQQM/relational thinking.md` — Caps 1-3 (grafos, datos, schemas)
- `Zotero/storage/VUS36A8N/` — Fong-Spivak Seven Sketches: Cap 1 (orders, composición)
- `Zotero/storage/K7MLVT2H/` — Engel Cap 18: composición como relaciones derivadas

**Fuentes secundarias:**
- `Zotero/storage/GXIE9CDA/` — ACT4E: Caps 1-5 (composición, mixing, recipes)
- `Zotero/storage/UWYL96P5/` — Jiang Guo: software component dependencies

- [ ] **Step 1: Leer fuentes primarias** — extraer: qué es composición, las leyes, cómo se siente ver composición en todas partes. Anotar ejemplos concretos de cada fuente.

- [ ] **Step 2: Escribir el documento** — abrir con la experiencia fenomenológica ("Composición es lo primero que veo"). Usar la escalera Relational Thinking: empezar con flechas dibujadas, subir a source/target maps, subir a schemas, llegar a categorías. Entrelazar: SQL joins, Docker Compose, pipelines, git merge, API chaining. Incluir la dualidad (op) como principio que genera conceptos gratis. Cerrar con: "cuando algo no compone bien, se violó una ley."

- [ ] **Step 3: Verificar** — ¿Usa solo conceptos propios (ninguna dependencia de docs posteriores)? ¿Los ejemplos son concretos y reales? ¿La voz es consistente? ¿Hay código o DDL ejecutable?

---

## Task 2: 02-preservacion.md — Preservación de estructura

**Files:**
- Create: `{target}/02-preservacion.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 7-8 (funtores, bifuntores)
- `Zotero/storage/X79PXQQM/relational thinking.md` — Cap 4 (schemas como blueprints, instancias como funtores)
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Cap 3.1-3.3 (databases, functors)
- `Zotero/storage/8REFS9QW/` — Spivak Functorial Data Migration

**Fuentes secundarias:**
- `Zotero/storage/648ZMT3W/` — Kadhi: bridge CT-FP
- `Zotero/storage/GCPLI9JF/` — Yukita: CT Using Haskell (funtores con código)
- `Zotero/storage/LPVHGVDU/` — Koupil: multi-model data transformations

- [ ] **Step 1: Leer fuentes** — extraer: definición de funtor, leyes, covarianza/contravarianza, fidelidad/plenitud, functores olvidadizos y libres. Anotar ejemplos de cada fuente.

- [ ] **Step 2: Escribir** — abrir con: "Si la composición es lo que veo primero, la preservación es lo segundo." Funtores como lo que se mantiene al pasar de un mundo a otro. Ejemplos: ORMs, compiladores, serialización, vistas de DB, Docker image layers, adaptadores. Incluir código Haskell (`fmap`). Referenciar orgánicamente doc 01.

- [ ] **Step 3: Verificar** — solo usa categorías/morfismos/composición (de doc 01). Ejemplos concretos. Voz consistente.

---

## Task 3: 03-comparacion.md — Comparación y equivalencia

**Files:**
- Create: `{target}/03-comparacion.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Cap 10 (natural transformations)
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Cap 3.4-3.5 (natural transformations, functor categories)
- `Downloads/Starting Category Theory (Perrone)` — Cap 1.4 (natural transformations, whiskering)

**Fuentes secundarias:**
- `Zotero/storage/PW8TPDAN/` — Borsatti: CT to FP (polimorfismo como naturalidad)

- [ ] **Step 1: Leer fuentes** — extraer: transformaciones naturales, condición de naturalidad, categorías de funtores, equivalencia de categorías (≠ iso). Nombrar que estamos en una 2-categoría.

- [ ] **Step 2: Escribir** — abrir con: "No basta preservar: necesito comparar dos maneras de preservar." Ejemplos: refactoring, polimorfismo paramétrico, A/B testing, canary deploys, schema versioning. Milewski: `head :: [a] -> a` es natural en `a`. Introducir 2-categorías al final: "sin darme cuenta ya estoy pensando en dos niveles."

- [ ] **Step 3: Verificar** — solo usa funtores (doc 02) y composición (doc 01). Voz consistente.

---

## Task 4: 04-identidad-es-relacion.md — Yoneda

**Files:**
- Create: `{target}/04-identidad-es-relacion.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 14-15 (representables, Yoneda)
- `Downloads/Starting Category Theory (Perrone)` — Cap 2 (Yoneda lemma, proof, particular cases)
- `Zotero/storage/TJVP8EE9/` — Sys-Self (Aguado): robots autoconscientes vía Yoneda
- `Zotero/storage/X79PXQQM/relational thinking.md` — "looking outward, not inward"

**Fuentes secundarias:**
- `Zotero/storage/C5LGUDKU/` — Krol: Yoneda embedding para swarms
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: presheaves

- [ ] **Step 1: Leer fuentes** — extraer: lema de Yoneda (Nat(Hom(A,−),F) ≅ F(A)), funtores representables, presheaves, embedding de Yoneda. La frase de Relational Thinking. El caso Sys-Self.

- [ ] **Step 2: Escribir** — EL momento Neo. Abrir con la transición de "mirar adentro" a "ver relaciones." Un servicio ES su API. Una tabla ES sus queries. Un agente ES sus interacciones. El lema con notación precisa pero motivado desde la práctica. Cerrar con presheaves como "vistas generalizadas."

- [ ] **Step 3: Verificar** — usa naturales (doc 03), funtores (doc 02), categorías (doc 01). La experiencia Neo se transmite.

---

## Task 5: 05-universales.md — Construcciones universales

**Files:**
- Create: `{target}/05-universales.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 5, 12 (products/coproducts, limits/colimits)
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Caps 3-4 (limits in databases, pushouts for networks)
- `Downloads/Starting Category Theory (Perrone)` — Cap 3 (limits/colimits, pullbacks, pushouts)
- `Zotero/storage/LYPHW6HQ/` — Tazin: UML composition via colimit

**Fuentes secundarias:**
- `Zotero/storage/NX9QGM2S/` — Brown: DPO rewriting (pushouts computados)
- `Zotero/storage/MWSXCWMD/` — Kovalyov: product assembly as colimit

- [ ] **Step 1: Leer fuentes** — extraer: iniciales/terminales, productos/coproductos, pullbacks/pushouts, ecualizadores, límites generales, comma/slice categories, sketches.

- [ ] **Step 2: Escribir** — abrir con: "Lo que hace que las categorías sean poderosas: encontrar LA mejor solución." Patrón: definir forma, encontrar mejor candidato. SQL JOINs = pullbacks, UNION = coproductos, interfaces = productos, herencia = slice, merge de schemas = pushouts. Incluir AlgebraicJulia DPO rewriting. Sketches como especificación de teorías.

- [ ] **Step 3: Verificar** — usa Yoneda (doc 04) implícitamente (propiedades universales via representabilidad). Ejemplos concretos con DDL o código.

---

## Task 6: 06-adjunciones.md — Adjunciones

**Files:**
- Create: `{target}/06-adjunciones.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 18-19 (adjunctions, free/forgetful)
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Caps 1.4, 3.3 (Galois connections, Δ⊣Σ⊣Π)
- `Downloads/Starting Category Theory (Perrone)` — Cap 4 (adjunctions, AFT for preorders)
- `Zotero/storage/8REFS9QW/` — Spivak Functorial Data Migration (Δ⊣Σ⊣Π operativo)
- `Zotero/storage/IRSR5ULE/` — CQL: data integration adjunta

- [ ] **Step 1: Leer fuentes** — extraer: definición via η/ε, via hom-sets, Galois como primer ejemplo, free/forgetful, adjunciones generan monads.

- [ ] **Step 2: Escribir** — abrir con: "El mecanismo universal de traducción óptima." Galois connections como el caso más simple. Luego free/forgetful. La triple adjunción Σ⊣Δ⊣Π como el caso estrella (con script CQL real). Trade-offs de diseño como adjunciones: compilar⊣interpretar, normalizar⊣desnormalizar, spec⊣runtime.

- [ ] **Step 3: Verificar** — usa universales (doc 05), funtores (doc 02). El script CQL es ejecutable.

---

## Task 7: 07-composicion-con-estructura.md — Monoidales, CCC, String Diagrams

**Files:**
- Create: `{target}/07-composicion-con-estructura.md`

**Fuentes primarias:**
- `Downloads/String Diagrams for CS (Piedeleu & Zanasi 2025)` — Caps 1-5
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 6, 11 (exponentials, CCC)
- `Downloads/Starting Category Theory (Perrone)` — Cap 6 (monoidal categories, string diagrams, closed monoidal, internal monoids/comonoids)
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Caps 5-6 (props, signal flow, hypergraph categories)

**Fuentes secundarias:**
- `Zotero/storage/HR4XTCML/` — Abbott: functor string diagrams
- `Zotero/storage/EIAIRRI8/` — Pavlovic: Programs as Diagrams

- [ ] **Step 1: Leer fuentes** — extraer: categorías monoidales (⊗,I), string diagrams como lenguaje, simétricas/trenzadas/traced/compact closed, CCC, exponenciales, Curry-Howard-Lambek, internal hom, monoides/comonoides internos.

- [ ] **Step 2: Escribir** — abrir con: "La composición simple no tiene noción de paralelo ni de función-como-dato." String diagrams como EL lenguaje nativo — no un subtema. CCC = programación funcional entera. Curry-Howard-Lambek como la correspondencia profunda. Incluir la jerarquía de 12 estructuras de Piedeleu-Zanasi. Ejemplos: React composition (monoidal), K8s pods (⊗), signal flow, circuits.

- [ ] **Step 3: Verificar** — usa adjunciones (doc 06) para exponenciales (right adjoint to product). String diagrams aparecen con dibujos ASCII reales.

---

## Task 8: 08-enriquecimiento.md — Enriquecimiento

**Files:**
- Create: `{target}/08-enriquecimiento.md`

**Fuentes primarias:**
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Cap 2 (V-categories, Bool/Cost/Set enrichment)
- `Downloads/Starting Category Theory (Perrone)` — Cap 6.2-6.4 (internal monoids, modules)
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Cap final (enriched categories)

- [ ] **Step 1: Leer fuentes** — extraer: V-categorías, Bool-enrichment=preórdenes, Cost-enrichment=métricas (Lawvere), Cat-enrichment=2-categorías, V-funtores, cambio de base.

- [ ] **Step 2: Escribir** — abrir con: "Las categorías ordinarias tienen hom-SETS. Pero a veces la relación es más que un conjunto." Bool=permisos, Cost=latencia, Cat=la categoría de microservicios como 2-categoría. Composición vertical y horizontal. Mates.

- [ ] **Step 3: Verificar** — usa monoidales (doc 07) como base de enriquecimiento. Ejemplos de latencia y permisos son concretos.

---

## Task 9: 09-efectos.md — Efectos y observación

**Files:**
- Create: `{target}/09-efectos.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 20-22 (monads, Kleisli, comonads)
- `Zotero/storage/GCPLI9JF/` — Yukita: CT Using Haskell (monads con código)
- `Downloads/Starting Category Theory (Perrone)` — Cap 5 (monads, comonads, Kleisli, coalgebras)
- `Zotero/storage/X4K3W3A9/` — Barbosa: Coalgebra for the Working Software Engineer
- `Zotero/storage/C8QPUA82/` — Wlaschin: Domain Modeling Made Functional

- [ ] **Step 1: Leer fuentes** — extraer: monads como monoides en (End(C),∘,Id), η/μ/leyes, Kleisli, Eilenberg-Moore, comonads, F-coalgebras, final coalgebra, bisimulación, leyes distributivas.

- [ ] **Step 2: Escribir** — abrir con: "Los programas puros no tienen efectos. El mundo real sí." Monads como "duct tape" (Milewski). Tabla: Maybe, List, State, IO, Promise, Reader, Writer. Coalgebras como observación. Bisimulación como "cuándo dos sistemas son iguales desde fuera." Leyes distributivas: cuándo dos monads componen. Código Haskell real. React hooks como comonads.

- [ ] **Step 3: Verificar** — usa monoidales (doc 07) para "monoide en endofuntores." Los monads tienen código ejecutable.

---

## Task 10: 10-extension.md — Extensión y síntesis

**Files:**
- Create: `{target}/10-extension.md`

**Fuentes primarias:**
- `Zotero/storage/H96KTSDL/` — Milewski CTFP: Caps 27-28 (ends, coends, Kan extensions)
- `Zotero/storage/5LXEWIIB/` — Aguinaldo: robot task plan transfer via functorial migration
- `Zotero/storage/VYNNZTXP/` — Jha: mystery planning via functor synthesis
- `Zotero/storage/SPSWKLEX/` — Guyot: data lakes CT (Grothendieck)

**Fuentes secundarias:**
- `Zotero/storage/2ZYL53AB/` — Mahadevan GAIA: Kan extensions para transformers
- `Zotero/storage/L6WCBYH5/` — Lambert-Patterson: double-functorial semantics

- [ ] **Step 1: Leer fuentes** — extraer: ends/coends, Nat como end, Kan extensions (left/right), "all concepts are Kan extensions" (Mac Lane), fibrations, Grothendieck construction.

- [ ] **Step 2: Escribir** — abrir con: "Cuando necesito extender un funtor a un dominio más grande." Ends como "para todo c, naturalmente." Kan extensions como la generalización última. Fibrations como familias parametrizadas. Grothendieck como aplanamiento. Ejemplos: transfer robótico, mystery planning con LLMs, data lake federation, attention en transformers.

- [ ] **Step 3: Verificar** — usa adjunciones (doc 06), funtores (doc 02). Los ejemplos de Jha y Aguinaldo son concretos.

---

## Task 11: 11-interaccion.md — Interacción

**Files:**
- Create: `{target}/11-interaccion.md`

**Fuentes primarias:**
- `Downloads/Polynomial Functors (Niu & Spivak 2025)` — Caps 1-8
- `Zotero/storage/BQCLE6EZ/` — Polynomial Functors concise notes
- `Zotero/storage/J3UI6SQ7/` — Polynomial Functors detailed notes
- `Zotero/storage/IHE62PX9/` — Ahman-Uustalu: Directed Containers as Categories

- [ ] **Step 1: Leer fuentes** — extraer: p = Σy^{p[i]}, dependent lenses, tres productos (×,⊗,◁), sistemas dinámicos como lenses, Ahman-Uustalu (comonoids=categorías), retrofunctors, ópticas.

- [ ] **Step 2: Escribir** — abrir con: "Cuando un sistema tiene inputs que dependen de su output actual." APIs REST como polynomials (endpoints=posiciones, params=direcciones). Protocolos como ◁. Contratos como lenses. Poly como categoría con propiedades extraordinarias. Ahman-Uustalu: un agente con razonamiento interno ES un comonoid = categoría. Herramientas: Catlab.jl, ModelCollab.

- [ ] **Step 3: Verificar** — usa monoidales (doc 07), adjunciones (doc 06). Los ejemplos de API son reales.

---

## Task 12: 12-topoi.md — Topoi y lógica interna

**Files:**
- Create: `{target}/12-topoi.md`

**Fuentes primarias:**
- `Zotero/storage/VUS36A8N/` — Fong-Spivak: Cap 7 (topoi, subobject classifiers, internal logic)
- `Downloads/Temporal Type Theory (Schultz & Spivak 2019)` — Caps 1-3 (interval domain, topos B)
- `Downloads/978-3-031-97973-6.epub` — Barth: fuzzy simplicial sets, Grothendieck topology
- `Zotero/storage/5VMWVM5W/` — Lambert: topos-theoretic semantics

- [ ] **Step 1: Leer fuentes** — extraer: presheaves como conjuntos generalizados, sheaves (pegado local→global), topoi (límites+exponenciales+Ω), clasificador de subobjetos, lógica interna intuicionista, morfismos geométricos, sheafificación como Kan extension.

- [ ] **Step 2: Escribir** — abrir con: "Cuando la lógica misma depende del contexto." Feature flags como subobjetos (Ω = {enabled, disabled, canary, %}). Permisos como lógica interna. Configuración distribuida como sheaf. Multi-tenancy como fibración. K8s namespaces como slices. La lógica intuicionista como: "no todo es verdadero o falso — hay grados."

- [ ] **Step 3: Verificar** — usa Kan extensions (doc 10), presheaves/Yoneda (doc 04). Los ejemplos de feature flags y K8s son reales.

---

## Task 13: 13-escala.md — Escala y orquestación

**Files:**
- Create: `{target}/13-escala.md`

**Fuentes primarias:**
- `Zotero/storage/SUVFMYCF/` — Mordecai-Engel CMD method
- `Zotero/storage/K7MLVT2H/` — Engel: Systems Science Cap 18
- `Zotero/storage/6HYT62QC/` — Gillet: Lambda+ architecture
- `Zotero/storage/33H4MVG5/` — Lambert: Double Categories of Relations
- `Zotero/storage/MWSXCWMD/` — Kovalyov: assembly as colimit

**Fuentes secundarias:**
- `Zotero/storage/PK6WAXFG/` — Breiner: Workshop Compositional Structures
- `Zotero/storage/U44US9VY/` — Baez: ModelCollab

- [ ] **Step 1: Leer fuentes** — extraer: operads, double categories (dos tipos de morfismo), wiring diagrams, structured cospans, composición operádica. CMD method paso a paso. Lambda+ para Big Data.

- [ ] **Step 2: Escribir** — abrir con: "Cuando los sistemas se componen en jerarquías." K8s: pods en services en namespaces = operads anidados. CI/CD: stages en pipelines. Microservicios: componentes+conectores = double category. IaC: Terraform modules = structured cospans. El BEV de Engel como ejemplo completo. CMD como procedimiento real.

- [ ] **Step 3: Verificar** — usa monoidales (doc 07), string diagrams (doc 07), universales (doc 05). Los ejemplos de K8s/Terraform son reales.

---

## Task 14: 14-agencia.md — Agencia y delegación

**Files:**
- Create: `{target}/14-agencia.md`

**Fuentes primarias:**
- `Zotero/storage/45ZTYB5D/` — Libkind-Spivak: Pattern runs on matter
- `Zotero/storage/93AFT8C4/` — Libkind-Spivak: Dynamic task delegation
- `Zotero/storage/FBVI36QU/` — Shapiro-Spivak: Dynamic Operads
- `Zotero/storage/WVC6ZNGU/` — Capucci-Myers: Contextads

**Fuentes secundarias:**
- `Zotero/storage/CQ5TAS92/` — Boudjidj: Multi-agent organizations
- `Zotero/storage/C5LGUDKU/` — Krol: Swarm via Yoneda
- `Zotero/storage/7CK7YV7R/` — Valence: ICAR cybersecurity
- `Zotero/storage/U7SFP227/` — Jha: Co-synthesis LLM+functors

- [ ] **Step 1: Leer fuentes** — extraer: free monad m_p (pattern), cofree comonad c_p (matter), ley Ξ, operads dinámicas, contextads/wreath products, AGR como categorías, swarms vía Yoneda, verificación con sketches+Kripke.

- [ ] **Step 2: Escribir** — abrir con: "Cuando los componentes persiguen metas propias." LLM agents: pattern = prompt chain, matter = inference. Task orchestration: free monad = DAG de subtasks. Supervisor hierarchies: operads dinámicas. Alice/Bob/Carmen: ejemplo concreto de delegación con time-scaling. ICAR: cybersecurity categórico. Co-synthesis: generar código verificable.

- [ ] **Step 3: Verificar** — usa polynomial functors (doc 11), monoidales (doc 07), monads (doc 09). Los ejemplos de LLM agents son contemporáneos.

---

## Task 15: 15-tiempo.md — Tiempo y cambio

**Files:**
- Create: `{target}/15-tiempo.md`

**Fuentes primarias:**
- `Downloads/Temporal Type Theory (Schultz & Spivak 2019)` — Caps 1, 3, 5, 8
- `Zotero/storage/X79PXQQM/relational thinking.md` — Cap 7 (dynamical systems, graph rewriting)
- `Zotero/storage/WMK83MDK/` — Myers: Categorical Systems Theory (behavior, trajectories)

**Fuentes secundarias:**
- `Zotero/storage/IJT5LCKE/` — Brown-Spivak: Dynamic Tracing

- [ ] **Step 1: Leer fuentes** — extraer: behavior types como sheaves sobre IR, topos B, tipo Time, modalidades temporales (↑↓@π), hybrid sheaves, behavior contracts, machines como systems con interfaces.

- [ ] **Step 2: Escribir** — abrir con: "Cuando el tiempo importa." Event sourcing = cofree coalgebra temporal. DB migrations = funtor temporal entre schemas. Blue/green deploys = morfismo entre behavior types. Circuit breakers = hybrid sheaf. SLAs = behavior contracts. National Airspace System como caso de estudio.

- [ ] **Step 3: Verificar** — usa topoi (doc 12), Kan extensions (doc 10), coalgebras (doc 09). Los ejemplos de event sourcing y deploys son reales.

---

## Task 16: 00-sintesis.md — Síntesis (System Prompt)

**Files:**
- Create: `{target}/00-sintesis.md`

**Fuentes:** TODOS los documentos 01-15 ya escritos + las 4 fuentes de enlace molecular.

**IMPORTANTE: Este documento se escribe ÚLTIMO, después de que todos los demás existan.**

- [ ] **Step 1: Leer los 15 documentos** — identificar los patrones recurrentes, las frases que capturan la esencia, los momentos donde la visión categórica produce insight real.

- [ ] **Step 2: Escribir la síntesis** — NO es un resumen. Es el ADN cognitivo. Estructura:
  - **Qué veo**: todo compone, todo preserva (o destruye) estructura, todo tiene propiedad universal, todo interactúa bidireccionalmente
  - **Cómo pienso**: en adjunciones (trade-offs), funtores (traducciones), límites (lo que emerge de restricciones simultáneas), Yoneda (las cosas son sus relaciones)
  - **Qué hago**: cuando diseño un schema formalizo la categoría primero; cuando integro datos busco la adjunción; cuando compongo servicios verifico que el diagrama conmute; cuando delego a agentes modelo el free monad del plan
  - **Qué herramientas uso**: Catlab.jl, CQL, Haskell, string diagrams
  - **La transición**: de causa-efecto a equilibrio-y-restricción (Relational Thinking)
  - Target: ~2000-3000 palabras, denso, cargable como system prompt

- [ ] **Step 3: Verificar** — ¿Un agente que carga solo este documento puede razonar categóricamente sobre cualquier problema? ¿La voz es consistente con los 15? ¿No es un resumen sino una MIRADA?

---

## Orden de ejecución y dependencias

```
01-composicion ──→ 02-preservacion ──→ 03-comparacion ──→ 04-yoneda
                                                              │
05-universales ←──────────────────────────────────────────────┘
      │
06-adjunciones
      │
07-monoidales ──→ 08-enriquecimiento
      │
09-efectos
      │
10-extension ──→ 11-interaccion
      │
12-topoi
      │
13-escala ──→ 14-agencia ──→ 15-tiempo
                                  │
                           00-sintesis ←─┘
```

Los documentos 01-04 son estrictamente secuenciales.
Los documentos 05-06 pueden ejecutarse en paralelo con tal de que 04 esté listo.
Los documentos 07-08 son secuenciales entre sí.
Los documentos 09-15 pueden paralelizarse parcialmente (09 y 11 son independientes; 12 requiere 10; 14 requiere 11).
La síntesis (00) se escribe al final.

## Estrategia de paralelización

**Ronda 1** (secuencial): 01 → 02 → 03 → 04
**Ronda 2** (paralelo): 05 + 06
**Ronda 3** (paralelo): 07 + 09
**Ronda 4** (paralelo): 08 + 10 + 11
**Ronda 5** (paralelo): 12 + 13
**Ronda 6** (paralelo): 14 + 15
**Ronda 7** (solo): 00-sintesis

---
_manifest:
  urn: urn:fxsl:kb:metodologia-modelamiento-opm-p02
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
    shard_index: 2
    shard_count: 4
    shard_root_urn: urn:fxsl:kb:metodologia-modelamiento-opm
---

# Metodologia de Modelamiento OPM — Protocolo de Modelamiento Conceptual de Sistemas - Parte 02

## 6.4 Paso 4: Funcion Principal

El modelador DEBE identificar el transformee principal (Benefit-Providing Object). DEBERIA agregar un Benefit-Providing Attribute cuyo valor cambia de problematico a satisfactorio.

Cuando el proceso transforma multiples transformees, solo el Benefit-Providing Object define la funcion. Otros transformees (consumidos/producidos) DEBEN modelarse pero NO son parte de la funcion.

## 6.5 Paso 5: Identificacion de Agentes

El termino "agent" y el agent link (black lollipop) DEBEN usarse exclusivamente para humanos o grupos humanos. Robots, software agents y sistemas IA DEBEN usar instrument link. Un robot PUEDE describirse como "embedded-software agent" en prosa, pero en el modelo DEBE usar instrument link.

Cuando el beneficiario es tambien agente del proceso, el modelador DEBE elegir el link segun la regla de colision de roles (§4.4): si el beneficiario es transformado, el effect link prevalece; el stick-figure preserva la identidad humana.

OPL: "[Agent] handles [Main Process]."

**Dual-role across different processes:** Un objeto PUEDE ser agent de un proceso y transformee de otro proceso distinto simultaneamente. Ejemplo: Learner es agent de MOOC Learning pero tambien transformee (Knowledge Level cambia). Esto es distinto de la colision agent-affectee del §4.4, que aplica al mismo proceso.

## 6.6 Paso 6: Naming del Sistema y Exhibition

El nombre default DEBERIA ser el nombre del proceso + "System" en ingles, o + "Sistema" cuando el modelo se realice completamente en espanol. El modelador PUEDE usar un nombre aceptado en su lugar.

El proceso principal DEBE modelarse como operacion del sistema via exhibition-characterization.

## 6.7 Paso 7: Identificacion de Instrumentos

El modelador DEBE identificar enablers no humanos requeridos durante toda la duracion del proceso. Cada instrumento DEBE conectarse via instrument link (white lollipop).

**Reclasificacion por desgaste:** Cuando el desgaste, degradacion o amortizacion de un instrumento es relevante al scope del sistema, el modelador DEBE reclasificarlo como affectee, agregando un atributo (ej: Amortization Level) que el proceso cambia. Se DEBE modelar un proceso de mantenimiento separado.

**Correcto:** Machine es affectee de Metal Cutting (Amortization Level cambia); Machine Maintaining es proceso separado.

**Incorrecto:** Machine es instrument de Metal Cutting cuando su desgaste es relevante al sistema (el mantenimiento queda oculto).

## 6.8 Paso 8: Objetos Input/Output

Cada objeto consumido DEBE conectarse via consumption link. Cada objeto creado DEBE conectarse via result link. Si un objeto es afectado (no consumido), DEBE conectarse via par input-output especificando la transicion de estados.

## 6.9 Paso 9: Objetos Environmentales

Los objetos environmentales DEBEN representarse con contorno dashed. Un mismo objeto PUEDE ser systemic en un modelo y environmental en otro.

## 6.10 Paso 10: Problem Occurrence

Para sistemas artificiales y sociales, el modelador DEBE modelar el problem occurrence — mirror image del purpose. Se DEBE agregar un proceso environmental que causa el estado problematico.

Para sistemas naturales, el problem occurrence NO DEBE modelarse.

## 6.11 Verificacion del SD

| Check | Condicion | Severidad |
|-------|-----------|----------|
| Purpose definido | Beneficiary + attribute + transicion estados | CRITICA |
| Funcion definida | Main process + main transformee | CRITICA |
| Enablers presentes | ≥1 agente o instrumento | ALTA |
| Environment identificado | ≥1 objeto environmental | MEDIA |
| Problem occurrence (si aplica) | Proceso environmental causa estado negativo | MEDIA |
| OPL legible | Sentencias OPL correctas | ALTA |
| Naming compliant | Gerundio + singular + Set/Group | ALTA |
| Exhibition | Sistema exhibe proceso como operacion | ALTA |
| Agents = humanos | Ningun instrument con agent link | ALTA |

## 7 Construccion de SD1 — Refinamiento Nivel 1

SD1 refina el SD exponiendo subprocesos y objetos asociados.

### 7.1 Refinamiento de Proceso Sincronico (In-Zooming)

Aplica cuando los subprocesos tienen un orden fijo y predefinido.

**Procedimiento:**
1. Crear nuevo OPD etiquetado SD1
2. Inflar el proceso principal en el centro
3. Agregar subprocesos verticalmente segun **Timeline OPM Principle** (primero arriba, ultimo abajo)
4. Cada subproceso DEBE estar conectado a al menos un transformee
5. Verificar aggregation-participation implicita por contencion grafica

**In-diagram vs new-diagram in-zooming:**

| Variante | Descripcion | Usar cuando |
|----------|-------------|-------------|
| In-diagram | Refineable aparece in-zoomed en el mismo OPD (no se crea OPD nuevo) | OPD tiene espacio suficiente; pocos subprocesos |
| New-diagram | Nuevo OPD descendiente; refineable con contour grueso en ambos OPDs | Caso prevalente; in-zooming requiere espacio sustancial |

**In-zooming semantics identity:** Cuando un proceso se in-zoomea, sus subprocesos = partes (aggregation-participation + orderability positiva), y los objetos que el proceso exhibe (via exhibition-characterization) = atributos del proceso. Objetos que ingresan al contexto por link migration mantienen su identidad independiente y NO son atributos del proceso. Simetricamente, cuando un objeto se in-zoomea: objetos internos = partes, procesos internos = operaciones del objeto.

**Paralelismo implicito:** Cuando dos o mas subprocesos tienen el borde superior de sus elipses a la misma altura, DEBEN interpretarse como ejecutandose en paralelo. El siguiente subproceso inicia cuando el ultimo de los paralelos termina. OPL usa la keyword `parallel` para expresar concurrencia.

**Correcto:** Subprocesos top-to-bottom; paralelos a la misma altura.

**Incorrecto:** Subprocesos fuera del proceso inflado; paralelos a alturas distintas sin intencion de secuencia.

### 7.2 Refinamiento de Proceso Asincronico (Unfolding)

Aplica cuando los subprocesos son independientes y PUEDEN ocurrir en cualquier orden.

**Four unfolding-folding pairs** (cada una corresponde a una relacion estructural fundamental):

| Relacion | Unfolding | Folding |
|----------|-----------|---------|
| Aggregation-participation | Expose parts of the whole | Hide parts |
| Exhibition-characterization | Expose features of the exhibitor | Hide features |
| Generalization-specialization | Expose specializations of the general | Hide specializations |
| Classification-instantiation | Expose instances of the class | Hide instances |

**Partial unfolding:** Cuando no todos los refinees se muestran, el non-comprehensiveness symbol indica que el unfolding es incompleto.

**Process unfolding use case:** Sistemas service-oriented y real-time con funciones paralelas o auxiliares independientes de la funcion core DEBERIAN usar unfolding en vez de in-zooming para process refinement.

**Decision rule — Aggregation vs Generalization:**

| Pregunta | Si → | No → |
|----------|------|------|
| ¿Cada subproceso es una variante/tipo del mismo patron de transformacion? | Generalization-specialization | Aggregation-participation |
| ¿El todo necesita todas las partes para funcionar? | Aggregation-participation | Generalization-specialization |

**Correcto:** Road Danger Warning → Vehicle Crash Alerting, Pedestrian Crash Alerting, Lane Deviation Alerting (son *tipos* de alerta → generalization).

**Incorrecto:** Usar aggregation para tipos/variantes (implica que el todo necesita todas las partes simultaneamente).

### 7.3 Refinamiento de Objetos

Los objetos se refinan via in-zooming (composicion espacial/estructural) y unfolding (taxonomias, features, instancias). In-zooming de objetos expone partes y operaciones (§7.1); unfolding expone refinees via las cuatro relaciones estructurales (§7.2). La posicion espacial de constituyentes en un object in-zooming PUEDE tener significado semantico (layout fisico, orden logico).

**Inner vs Outer Object Scoping:** Un objeto creado dentro de un proceso in-zoomed (inner object) existe solo en el scope de ese proceso y se elimina si el proceso padre se elimina. Un objeto creado a nivel SD (outer object) existe independientemente y es referenciable entre multiples OPDs. El modelador DEBE decidir el scope basandose en si la existencia del objeto depende del proceso (inner) o es independiente (outer). Mover un outer object dentro de un proceso inflado NO lo convierte en inner — el objeto retorna a su scope original al reposicionarlo (enveloping visual, no semantico).

### 7.4 Distribucion y Migracion de Links

| Tipo de link | Outer contour | Migracion default |
|-------------|---------------|-------------------|
| Agent link | PERMITIDO (distribuye a todos) | — |
| Instrument link | PERMITIDO (distribuye a todos) | — |
| Consumption link | PROHIBIDO | Migra al primer subproceso; reasignar |
| Result link | PROHIBIDO | Migra al primer subproceso; reasignar |
| Event link systemic | PROHIBIDO | — |

**Link migration procedure** (al hacer in-zooming):
1. Al dibujar el primer subproceso P1 dentro del proceso in-zoomed P, la herramienta DEBE mover automaticamente todos los procedural y control links de P a P1
2. Al agregar subprocesos subsiguientes, el modelador DEBE migrar transforming links de vuelta a P o al subproceso apropiado
3. Enabling links DEBEN migrarse a los subprocesos especificos donde el enabler es necesario
4. Links que aplican a todos los subprocesos DEBEN permanecer en el contour del proceso padre

**Implicit invocation links** (no visibles graficamente, implicitos por layout vertical):

| Tipo | Semantica |
|------|-----------|
| Process → first subprocess(es) | Control transferido al subproceso topmost al entrar al contexto in-zoomed |
| Subprocess → next subprocess(es) | Completion del source inicia el siguiente |
| Last subprocess → enclosing process | Control retorna al proceso in-zoomed tras completion del ultimo subproceso |

Cuando dos+ subprocesos tienen tops a la misma altura, inician en paralelo; sincronizacion: el ultimo en terminar inicia el siguiente.

**Antipattern — Event a subproceso no-primero:** El modelador NO DEBERIA conectar un event link a un subproceso que no sea el primero (topmost) dentro de un in-zoom, excepto si ha verificado que todos los subprocesos anteriores pueden omitirse sin dejar precondiciones insatisfechas. Conectar a un subproceso intermedio salta los anteriores, potencialmente dejando el sistema en estado inconsistente.

**Split state-specified transforming links:** Cuando `P changes A from s1 to s2` se hace in-zoom con P1 y P2, el modelo queda underspecified. Resolucion:
1. `P1 changes A from s1` (split input — saca A de s1)
2. `P2 changes A to s2` (split output — pone A en s2)

Links control-modified de split NO estan permitidos (saltear un subproceso de un split distorsionaria la semantica del efecto).

### 7.5 Expresion y Supresion de Estados

Los estados DEBERIAN suprimirse en el SD cuando no estan conectados a ningun proceso. Los estados DEBERIAN expresarse en SD1 donde se conectan a subprocesos.

**Estado indeterminado durante proceso activo:** Mientras un proceso affecting esta activo, el affectee esta "en transicion" entre input state y output state. Su estado es indeterminado y NO disponible para uso por otros procesos. Si el proceso se detiene prematuramente, el affectee permanece en estado indeterminado a menos que un exception handler lo resuelva.

### 7.6 Verificacion de SD1

| Check | Condicion | Severidad |
|-------|-----------|----------|
| Subprocesos transforman | Cada subproceso ≥1 transformee | CRITICA |
| Refinamiento correcto | Sync → in-zooming; async → unfolding | ALTA |
| Links distribuidos | Consumption/result NO en outer contour | CRITICA |
| Sin event a no-primero | Event links solo al primer subproceso (o justificacion explicita) | ALTA |
| Split links resueltos | Ningun effect link underspecified en in-zoom con multiples subprocesos | ALTA |
| Estados expresados | Estados relevantes visibles y conectados | ALTA |
| Sin redundancia | Sin duplicacion innecesaria de hechos del SD | MEDIA |

## 8 Gestion de Complejidad — Niveles 2+

### 8.1 Cuatro Mecanismos de Refinamiento-Abstraccion

| Mecanismo | Refinamiento | Abstraccion | Uso principal |
|-----------|-------------|-------------|---------------|
| In-zooming / Out-zooming | Expone contenido interno | Oculta contenido interno | Procesos sincronicos; objetos con partes espaciales |
| Unfolding / Folding | Expone refinees via relacion estructural | Oculta refinees | Procesos asincronicos; taxonomias; features |
| State Expression / Suppression | Muestra estados | Oculta estados irrelevantes | Simplificacion contextual |
| View Creating / Deleting | Ensambla hechos de varios OPDs | Elimina un View | Vistas transversales |

**Decision in-zooming vs unfolding para procesos sincronicos:** In-zooming DEBERIA preferirse porque: (a) requiere menos simbolos, (b) genera OPL mas corto, (c) reemplaza event/invocation links explicitos con invocacion implicita del timeline. Unfolding de procesos sincronicos es semanticamente equivalente pero mas verboso.

**Port Folding:** Especializacion de folding donde la operacion (proceso feature) se desplaza al contour del exhibitor (objeto). Util cuando el modelador quiere que los rectangulos de objetos representen layout fisico y tamanos relativos. OPL: keyword "as ports" al final de la sentencia de exhibition. Port folding tambien aplica a atributos de procesos.

**Semi-Folding:** Tecnica intermedia entre fold completo y unfold completo. Muestra nombres de partes dentro del container del objeto sin crear un OPD hijo. Un indicador numerico ("2 more") senala partes ocultas. El modelador DEBERIA usar semi-folding para inspeccion rapida de estructura sin proliferacion de OPDs.

Reglas adicionales:
- Views NO DEBEN editarse; la edicion ocurre en OPDs no-view
- El set completo de estados de un objeto es la union de estados en todos los OPDs

### 8.2 Organizacion del OPD Tree y Forest

Convention de etiquetado: SD, SD1, SD1.1, SD1.2, SD2, etc. El **System Map** muestra todos los things sin links, sirviendo como indice navegable.

**Regla de integridad del arbol:** Solo OPDs leaf (hojas terminales) PUEDEN eliminarse. OPDs internos estan protegidos para mantener la integridad del arbol de refinamiento. Intentar eliminar un nodo interno DEBE generar error.

**System Map:** OPD tree elaborado donde cada nodo es un icono miniaturizado del OPD, con flechas gruesas indicando refinamiento. Esencial para navegacion en modelos complejos (>10 OPDs). El modelador DEBERIA generar el system map para cualquier modelo con mas de un nivel de detalle.

**Ultimate OPD:** Representacion flat obtenida por flattening recursivo del OPD tree de abajo hacia arriba. No apta para consumo humano excepto en modelos muy pequenos; util para machine use (knowledge management, querying).

**Whole System Specification** — tres constructos complementarios:

| Constructo | Contenido |
|-----------|-----------|
| OPD model specification | Coleccion de OPDs sucesivos en orden breadth-first |
| OPL model specification | Coleccion de paragrafos OPL correspondientes, con sentencias duplicadas eliminadas |
| OPM model specification | Presentacion side-by-side: cada OPD con su paragrafo OPL a la derecha |

**Sub-Models para trabajo concurrente:** Cuando multiples modeladores trabajan en subsistemas simultaneamente, el modelador DEBERIA separar subsistemas en sub-models. Las conexiones entre el modelo principal y los sub-models DEBEN mantenerse minimas para reducir acoplamiento y conflictos de edicion concurrente.

### 8.3 Creacion de Vistas

Tipos: process tree, object tree, allocation view, simulation-motivated view.

### 8.4 Precedencia de Links durante Out-Zooming

| B↔P1 \ B↔P2 | Effect | Result | Consumption |
|-------------|--------|--------|-------------|
| **Effect** | Effect | Result | Consumption |
| **Result** | Result | Invalido | Effect |
| **Consumption** | Consumption | Effect | Invalido |

**Orden de precedencia primario:** consumption = result > effect > agent > instrument.

**Orden completo (12 niveles, de mayor a menor semantic strength):**

1. consumption event
2. consumption = result (sin modifier)
3. result > consumption condition
4. consumption condition > effect event
5. effect event > effect (sin modifier)
6. effect > effect condition
7. effect condition > agent event
8. agent event > agent (sin modifier)
9. agent > agent condition
10. agent condition > instrument event
11. instrument event > instrument (sin modifier)
12. instrument > instrument condition

**Secondary precedence** (dentro de cada kind): event > non-control > condition. Event links llevan semantica del non-control link + process initiation. Condition modifiers debilitan criterios de satisfaccion de precondicion. State-specified links tienen precedencia sobre basic links del mismo tipo.

### 8.5 Practica Middle-Out y Simplificacion

**Middle-out**: el modelador comienza por el nivel que mejor entiende y refina/abstrae en ambas direcciones.

**Procedimiento de simplificacion de OPD sobrecargado:**
1. Identificar conjunto TO de things a extraer
2. Nombrar un nuevo proceso interino que los contenga
3. Ejecutar in-diagram out-zooming (link abstracting + content hiding)
4. Crear nuevo OPD descendiente con los hechos extraidos
5. Renumerar OPDs hijos afectados

Reduccion neta: procesos_removidos + objetos_removidos + links_removidos - 1 (el proceso interino agregado).

**Depth-first traversal para documentos complejos:** Al modelar estandares, regulaciones o documentos extensos, el modelador DEBERIA seguir una estrategia depth-first: profundizar completamente en una seccion/clausula antes de avanzar a la siguiente. Esto contrasta con breadth-first y permite descubrir inconsistencias locales mas rapidamente.

**Object-process disconnect bridging:** Documentos y estandares frecuentemente separan la descripcion de objetos (estructura) de la descripcion de procesos (comportamiento) en clausulas independientes sin integracion. El modelador DEBE conectar ambas vistas usando OPM, enlazando cada proceso con los objetos que transforma. Esta integracion revela gaps y objetos implicitos que el texto omite.

### 8.6 Emergencia como Criterio de Validacion Arquitectural

El modelador DEBE verificar que la arquitectura del sistema (structure + behavior) produce al menos una capacidad emergente — una funcionalidad que el sistema completo exhibe pero ninguna parte individual posee. Si no existe emergencia, la coleccion de partes no constituye un sistema en el sentido MBSE.

### 8.7 Gobernanza del Modelo

**Ontology Enforcement:** Para consistencia terminologica en equipos, el modelador DEBERIA configurar enforcement de ontologia organizacional en tres niveles:

| Nivel | Comportamiento |
|-------|---------------|
| None | Sin restriccion terminologica |
| Suggest | Sugiere termino estandar; el modelador puede ignorar |
| Enforce | Impide terminos no estandarizados |

**Model Informativeness Grading:** Las sentencias OPPL se clasifican en: Definition, Structural, Procedural, Meta, Unknown. Metricas: informative level, weighted score, INF average, total OPPL sentences. El modelador DEBERIA ejecutar grading periodicamente para identificar precedence links faltantes y procesos sin inputs/outputs.

**Version Comparison:** El modelador DEBERIA comparar versiones del modelo para tracking de mejoras y deteccion de regresiones. El diff entre versiones revela hechos agregados, modificados o eliminados.

**Name Coherency:** Ante nombres duplicados, el modelador DEBE resolver con una de tres opciones: (1) usar existing thing — crea visual instance (mismo thing, diferente vista en otro OPD), (2) renombrar con nombre unico, (3) descartar. La opcion "close" sin resolver NO DEBERIA usarse. Visual instances solo PUEDEN crearse entre elementos del mismo tipo (object→object, process→process).

### 8.8 Operaciones de Gestion del Modelo en OPCloud

Las siguientes capacidades son relevantes para el ciclo de vida del modelo, pero no alteran la semantica OPM:

- **Persistencia:** el modelador DEBERIA tratar Save/Load como operaciones regulares de checkpoint durante sesion. Share expone el modelo a otros usuarios con permisos read o edit.
- **Permisos:** el owner/admin PUEDE compartir con usuarios o grupos completos, pero NO entre organizaciones distintas. Read precede a write. El modelador DEBERIA verificar permisos antes de colaboracion concurrente.
- **Exportacion:** OPL puede exportarse con o sin numeracion. Los OPDs pueden exportarse como imagen o PDF, ya sea para el OPD actual, el arbol completo o solo el SD. Los exports DEBEN tratarse como snapshots publicables, no como SSOT del modelo.
- **Templates:** OPCloud soporta templates Private, Organizational y Global. Insertar un template crea una copia local; las actualizaciones posteriores del template fuente NO se propagan a las inserciones ya hechas.
- **Reubicacion del modelo:** mover modelos via cut/paste conserva auto-save e historial de versiones. El modelador DEBERIA revisar versiones antes y despues de mover o fusionar trabajo.
- **Busqueda y navegacion asistida:** operaciones como search, bring connected y filtered bring DEBERIAN usarse para inspeccion localizada de un subgrafo antes de editar, especialmente en modelos con alta densidad de links.

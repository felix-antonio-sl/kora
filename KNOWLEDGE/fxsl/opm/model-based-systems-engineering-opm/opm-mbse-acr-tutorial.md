---
_manifest:
  urn: "urn:fxsl:kb:opm-mbse-acr-tutorial"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-25"
    source: "OPERATIONS/source/fxsl/opm-methodology/opm-libro-acr-tutorial.md"
version: "1.0.0"
status: published
tags: [opm, tutorial, acr, automatic-crash-response, mbse-history, worked-example, modeling-walkthrough]
lang: en
extensions:
  kora:
    family: textbook
    bilingual: true
    depends_on:
      - "urn:fxsl:kb:opm-iso-19450"
      - "urn:fxsl:kb:opm-mbse-foundations"
      - "urn:fxsl:kb:opm-dynamic-behavior"
      - "urn:fxsl:kb:opm-structural-relations"
      - "urn:fxsl:kb:opm-complexity-management"
      - "urn:fxsl:kb:sysml-foundations-diagrams"
    book_source: "Dori, D. (2015). Model-Based Systems Engineering with OPM and SysML. Springer."
    chapters: ["Preface", 1, 2, 3, 4, 5, 6, 7, 8]
---

# ACR Tutorial — OPM History and Modeling the Automatic Crash Response System

## Resumen

Este artefacto cubre dos dominios: (1) la historia de OPM, desde su genesis en 1993 hasta la adopcion como ISO 19450 en 2015, y (2) un tutorial paso a paso modelando el GM OnStar Automatic Crash Response (ACR) system usando OPM. El tutorial ilustra principios formales cubiertos en artefactos dedicados. Para definiciones formales ver [OPM Foundations](urn:fxsl:kb:opm-mbse-foundations), [Dynamic Behavior](urn:fxsl:kb:opm-dynamic-behavior), [Structural Relations](urn:fxsl:kb:opm-structural-relations), [Complexity Management](urn:fxsl:kb:opm-complexity-management).

## OPM Historical Context

### Genesis (1993)

Dov Dori, Technion/MIT. Eureka moment modelando un sistema de transformacion de dibujos de ingenieria a modelos CAD (University of Washington, 1993). Al dibujar nodos en una pizarra, descubrio que no todos eran objetos: algunos representaban cosas que suceden a objetos → los llamo procesos. Emergio un bipartite graph (objetos + procesos). Primer OPD jamas dibujado.

**Insight fundacional**: el pendulo del paradigma procedural al OO fue demasiado drastico. El OO suprimio el aspecto procedural de los sistemas, esencial para describir como cambian en el tiempo. Procesos como cake baking o check cashing no pueden ser "metodos" propiedad de un objeto — son patrones de transformacion independientes.

### Methods Wars and UML (1990s)

| Año | Evento |
|-----|--------|
| Early 1990s | ~36 metodos OO compiten ("Methods War") |
| 1993 | Primer paper OPM rechazado: "mixing water with oil". Journal of Logic and Computation lo acepto |
| 1997 | OMG adopta UML 1.0 como de-facto standard para software design (9 tipos de diagramas) |
| 2000 | Dori propone en OMG extender UML a systems at large → rechazado |
| 2001 | INCOSE inicia extension de UML para SE |
| 2002 | Primer libro OPM: "Object-Process Methodology — a Holistic Systems Paradigm" (Dori) |
| 2003 | OMG emite UML for SE Request for Proposals |
| 2006 | OMG adopta SysML 1.0 (basado en UML 2) |
| 2015 | ISO adopta OPM como ISO 19450 (6 años de trabajo) |

### OPM Foundation Summary

Cuatro pilares:
1. **Ontologia universal minima**: objetos con estado + procesos que los transforman
2. **Representacion bimodal**: grafico (OPD) + textual (OPL) semanticamente equivalentes
3. **Single diagram type**: unico tipo de diagrama (OPD) vs 9+ en UML/SysML
4. **Complexity management**: in-zooming + unfolding de un solo tipo de diagrama

### Book-ISO Relationship

El libro es un superset de ISO 19450. ISO es normativo y conciso; el libro agrega motivacion, rationale, fundamentos filosoficos, y puntos informativos que no caben en un estandar.

## ACR System Specification

GM OnStar Automatic Crash Response (ACR) system. Especificacion original del sitio web de OnStar:

**Componentes clave**:
- GPS satellite + cellular technology conectan vehiculo con OnStar Center
- Sensing and Diagnostic Module (SDM) con acelerometro mide severidad del crash
- OnStar module transmite informacion al OnStar Call Center (OCC)

**Flujo operacional**:
1. Crash frontal, lateral o trasero de severidad moderada-a-severa detectado por SDM
2. SDM transmite crash information al OnStar module (independiente de airbag deployment)
3. OnStar module envia mensaje al OCC via cellular
4. Advisor establece voice connection con vehicle occupants
5. Advisor puede conferencing 911 dispatch / PSAP
6. Si no hay respuesta de occupants → advisor provee crash info al dispatcher
7. GPS localiza el vehiculo para emergency workers

## Modeling Walkthrough

### Step 1: Function as Seed

Funcion del sistema: **Automatic Crash Responding** (top-level process). Beneficiary: **Vehicle Occupants Group** (object). Effect link bidireccional entre el proceso y el objeto (el proceso cambia el estado del grupo de ocupantes). System Diagram (SD) construido con 3 elementos: proceso, objeto, link.

### Step 2: Text and Simulation

OPL sentences generadas automaticamente del OPD. Estados del Vehicle Occupants Group: possibly injured → being helped. Animated simulation ejecuta el modelo mostrando transiciones de estado.

### Step 3: Links

Tipos de links aplicados al ACR:
- **Agent link** (filled lollipop): OnStar Advisor handles Message Handling
- **Instrument link** (open lollipop): Cellular Connection enables communication
- **Effect link**: Automatic Crash Responding affects Vehicle Occupants Group
- **Result link**: process creates Message
- **Consumption link**: process consumes Signal

Physical vs informatical things distinguidos: Signal (informatical), SDM (physical). Systemic vs environmental: ACR System (systemic), Hospital (environmental).

### Step 4: SysML Comparison

Mismo sistema modelado en SysML usando Use Case Diagram, Block Definition Diagram, State Machine Diagram. Para comparacion sistematica OPM-SysML, ver [SysML Foundations](urn:fxsl:kb:sysml-foundations-diagrams).

### Step 5: In-Zooming

Automatic Crash Responding se refina mediante in-zoom a un nuevo OPD (SD1) exponiendo subprocesos: Crash Severity Measuring, Message Creating, Message Sending. OPD Tree: SD → SD1. Crash Severity medida como atributo con valores: light, moderate, severe.

### Step 6: Dynamic Aspect

Timeline principle aplicado: subprocesos ejecutan top-to-bottom en SD1. Exiting ocurre si severity = light. Message Creating y Sending solo si severity ≥ moderate. Scenarios = threads of execution alternativos.

### Step 7: Control and Branching

Branching con Boolean objects: si severity = light → exit; si moderate/severe → continuar. Condition link vs instrument link. XOR entre paths. Zoom into Crash Severity Measuring expone subprocesos de diagnostico.

### Step 8: Abstraction and Views

Message Handling in-zoomed en nuevo OPD. Structural view del ACR System: parts y sus relaciones estaticas. Combinacion de vistas estructurales y dinamicas demuestra la capacidad de OPM para modelar ambos aspectos en un framework unificado.

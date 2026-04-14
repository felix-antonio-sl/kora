# Automation systems and integration — Object-Process Methodology

## ISO/PAS 19450

## Contents

- [Automation systems and integration — Object-Process Methodology](#automation-systems-and-integration--object-process-methodology)
  - [ISO/PAS 19450](#isopas-19450)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Automation systems and integration — Object-Process Methodology](#automation-systems-and-integration--object-process-methodology-1)
  - [1 Scope](#1-scope)
  - [2 Normative references](#2-normative-references)
  - [3 Terms and definitions](#3-terms-and-definitions)
  - [3.1 abstraction](#31-abstraction)
  - [3.2 affectee](#32-affectee)
  - [3.3 agent](#33-agent)
  - [3.4 attribute](#34-attribute)
  - [3.5 behaviour](#35-behaviour)
  - [3.6 beneficiary](#36-beneficiary)
  - [3.7 class](#37-class)
  - [3.8 completeness](#38-completeness)
  - [3.9 condition link](#39-condition-link)
  - [3.10 consumee](#310-consumee)
  - [3.11 context](#311-context)
  - [3.12 control link](#312-control-link)
  - [3.13 control modifier](#313-control-modifier)
  - [3.14 discriminating attribute](#314-discriminating-attribute)
  - [3.15 effect](#315-effect)
  - [3.16 element](#316-element)
  - [3.17 enabler](#317-enabler)
  - [3.18 event](#318-event)
  - [3.19 event link](#319-event-link)
  - [3.20 exhibitor](#320-exhibitor)
  - [3.21 feature](#321-feature)
  - [3.22 folding](#322-folding)
  - [3.23 function](#323-function)
  - [3.24 general](#324-general)
  - [3.25 informatical](#325-informatical)
  - [3.26 inheritance](#326-inheritance)
  - [3.27 input link](#327-input-link)
  - [3.28 instance](#328-instance)
  - [3.29 instance](#329-instance)
  - [3.30 instrument](#330-instrument)
  - [3.31 invocation](#331-invocation)
  - [3.32 involved object set](#332-involved-object-set)
  - [3.33 in-zoom context](#333-in-zoom-context)
  - [3.34 in-zooming](#334-in-zooming)
  - [3.35 in-zooming](#335-in-zooming)
  - [3.36 link](#336-link)
  - [3.37 metamodel](#337-metamodel)
  - [3.38 model fact](#338-model-fact)
  - [3.39 object](#339-object)
  - [3.40 object class](#340-object-class)
  - [3.41 Object-Process Diagram (OPD)](#341-object-process-diagram-opd)
  - [3.42 Object-Process Language (OPL)](#342-object-process-language-opl)
  - [3.43 Object-Process Methodology (OPM)](#343-object-process-methodology-opm)
  - [3.44 OPD object tree](#344-opd-object-tree)
  - [3.45 OPD process tree](#345-opd-process-tree)
  - [3.46 operation](#346-operation)
  - [3.47 output link](#347-output-link)
  - [3.48 out-zooming](#348-out-zooming)
  - [3.49 out-zooming](#349-out-zooming)
  - [3.50 perseverance](#350-perseverance)
  - [3.51 postcondition](#351-postcondition)
  - [3.52 postprocess object set](#352-postprocess-object-set)
  - [3.53 precondition](#353-precondition)
  - [3.54 preprocess object set](#354-preprocess-object-set)
  - [3.55 primary essence](#355-primary-essence)
  - [3.56 procedural link](#356-procedural-link)
  - [3.57 procedural relation](#357-procedural-relation)
  - [3.58 process](#358-process)
  - [3.59 process class](#359-process-class)
  - [3.60 property](#360-property)
  - [3.61 refineable](#361-refineable)
  - [3.62 refinee](#362-refinee)
  - [3.63 refinement](#363-refinement)
  - [3.64 resultee](#364-resultee)
  - [3.65 stakeholder](#365-stakeholder)
  - [3.66 stateful object](#366-stateful-object)
  - [3.67 stateless object](#367-stateless-object)
  - [3.68 state](#368-state)
  - [3.69 state](#369-state)
  - [3.70 state expression](#370-state-expression)
  - [3.71 state suppression](#371-state-suppression)
  - [3.72 structural link](#372-structural-link)
  - [3.73 structural relation](#373-structural-relation)
  - [3.74 structure](#374-structure)
  - [3.75 System Diagram (SD)](#375-system-diagram-sd)
  - [3.76 thing](#376-thing)
  - [4 Symbols](#4-symbols)
  - [5 Conformance](#5-conformance)
  - [6 OPM principles and concepts](#6-opm-principles-and-concepts)
  - [6.1 OPM modelling principles](#61-opm-modelling-principles)
    - [6.1.1 Modelling as a purpose-serving activity](#611-modelling-as-a-purpose-serving-activity)
    - [6.1.2 Unification of function, structure, and behaviour](#612-unification-of-function-structure-and-behaviour)
    - [6.1.3 Identifying functional value](#613-identifying-functional-value)
    - [6.1.4 Function versus behaviour](#614-function-versus-behaviour)
    - [6.1.5 System boundary setting](#615-system-boundary-setting)
    - [6.1.6 Clarity and completeness trade-off](#616-clarity-and-completeness-trade-off)
  - [6.2 OPM Fundamental concepts](#62-opm-fundamental-concepts)
    - [6.2.1 Bimodal representation](#621-bimodal-representation)
    - [6.2.2 OPM modelling elements](#622-opm-modelling-elements)
    - [6.2.3 OPM things: objects and processes](#623-opm-things-objects-and-processes)
    - [6.2.4 OPM links: procedural and structural](#624-opm-links-procedural-and-structural)
    - [6.2.5 OPM context management](#625-opm-context-management)
    - [6.2.6 OPM model implementation](#626-opm-model-implementation)
      - [6.2.6.1 Conceptual models versus runtime models](#6261-conceptual-models-versus-runtime-models)
      - [6.2.6.2 OPM model realization](#6262-opm-model-realization)
      - [6.2.6.3 OPD Navigation and OPL composition](#6263-opd-navigation-and-opl-composition)
  - [7 OPM thing syntax and semantics](#7-opm-thing-syntax-and-semantics)
  - [7.1 Objects](#71-objects)
    - [7.1.1 Description](#711-description)
    - [7.1.2 Representation](#712-representation)
  - [7.2 Processes](#72-processes)
    - [7.2.1 Description](#721-description)
    - [7.2.2 Representation](#722-representation)
  - [7.3 OPM things](#73-opm-things)
    - [7.3.1 OPM thing defined](#731-opm-thing-defined)
    - [7.3.2 Object-process test](#732-object-process-test)
    - [7.3.3 OPM thing generic properties](#733-opm-thing-generic-properties)
    - [7.3.4 Default values of thing generic properties](#734-default-values-of-thing-generic-properties)
    - [7.3.5 Object states](#735-object-states)
      - [7.3.5.1 Stateful and stateless objects](#7351-stateful-and-stateless-objects)
      - [7.3.5.2 Object state representation](#7352-object-state-representation)
      - [7.3.5.3 Initial, default, and final states](#7353-initial-default-and-final-states)
      - [7.3.5.4 Representation](#7354-representation)
      - [7.3.5.5 Attribute values](#7355-attribute-values)
  - [8 OPM link syntax and semantics overview](#8-opm-link-syntax-and-semantics-overview)
  - [8.1 Procedural link overview](#81-procedural-link-overview)
    - [8.1.1 Kinds of procedural links](#811-kinds-of-procedural-links)
    - [8.1.2 Procedural link uniqueness OPM principle](#812-procedural-link-uniqueness-opm-principle)
    - [8.1.3 State-specified procedural links](#813-state-specified-procedural-links)
  - [8.2 Operational semantics and flow of execution control](#82-operational-semantics-and-flow-of-execution-control)
    - [8.2.1 Event-Condition-Action control mechanism](#821-event-condition-action-control-mechanism)
    - [8.2.2 Preprocess object set and postprocess object set](#822-preprocess-object-set-and-postprocess-object-set)
  - [9 Procedural links](#9-procedural-links)
  - [9.1 Transforming links](#91-transforming-links)
    - [9.1.1 Kinds of transforming links](#911-kinds-of-transforming-links)
    - [9.1.2 Consumption link](#912-consumption-link)
    - [9.1.3 Result link](#913-result-link)
    - [9.1.4 Effect link](#914-effect-link)
    - [9.1.5 Basic transforming links summary](#915-basic-transforming-links-summary)
  - [9.2 Enabling links](#92-enabling-links)
    - [9.2.1 Kinds of enabling links](#921-kinds-of-enabling-links)
    - [9.2.2 Agent and Agent Link](#922-agent-and-agent-link)
    - [9.2.3 Instrument and Instrument Link](#923-instrument-and-instrument-link)
    - [9.2.4 Basic enabling links summary](#924-basic-enabling-links-summary)
    - [Table 2 — Basic enabling links summary](#table-2--basic-enabling-links-summary)
  - [9.3 State-specified transforming links](#93-state-specified-transforming-links)
    - [9.3.1 State-specified consumption link](#931-state-specified-consumption-link)
    - [9.3.2 State-specified result link](#932-state-specified-result-link)
    - [9.3.3 State-specified effect links](#933-state-specified-effect-links)
      - [9.3.3.1 Input and output effect links](#9331-input-and-output-effect-links)
      - [9.3.3.2 Input-output-specified effect link](#9332-input-output-specified-effect-link)
      - [9.3.3.3 Input-specified effect link](#9333-input-specified-effect-link)
      - [9.3.3.4 Output-specified effect link](#9334-output-specified-effect-link)
    - [9.3.4 State-specified transforming links summary](#934-state-specified-transforming-links-summary)
    - [Table 3 — State-specified transforming links summary](#table-3--state-specified-transforming-links-summary)
  - [9.4 State-specified enabling links](#94-state-specified-enabling-links)
    - [9.4.1 State-specified agent link](#941-state-specified-agent-link)
    - [9.4.2 State-specified instrument link](#942-state-specified-instrument-link)
    - [9.4.3 State-specified enabling links summary](#943-state-specified-enabling-links-summary)
    - [Table 4 — State-specified enabling links summary](#table-4--state-specified-enabling-links-summary)
  - [9.5 Control links](#95-control-links)
    - [9.5.1 Kinds of control links](#951-kinds-of-control-links)
    - [9.5.2 Event links](#952-event-links)
      - [9.5.2.1 Transforming event links](#9521-transforming-event-links)
        - [9.5.2.1.1 Consumption event link](#95211-consumption-event-link)
        - [9.5.2.1.2 Effect event link](#95212-effect-event-link)
        - [9.5.2.1.3 Transforming event links summary](#95213-transforming-event-links-summary)
    - [Table 5 — Transforming event links summary](#table-5--transforming-event-links-summary)
      - [9.5.2.2 Enabling event links](#9522-enabling-event-links)
        - [9.5.2.2.1 Agent event link](#95221-agent-event-link)
        - [9.5.2.2.2 Instrument event link](#95222-instrument-event-link)
        - [9.5.2.2.3 Enabling event links summary](#95223-enabling-event-links-summary)
    - [Table 6 — Enabling event links summary](#table-6--enabling-event-links-summary)
      - [9.5.2.3 State-specified transforming event links](#9523-state-specified-transforming-event-links)
        - [9.5.2.3.1 State-specified consumption event link](#95231-state-specified-consumption-event-link)
        - [9.5.2.3.2 Input-output-specified effect event link](#95232-input-output-specified-effect-event-link)
        - [9.5.2.3.3 Input-specified effect event link](#95233-input-specified-effect-event-link)
        - [9.5.2.3.4 Output-specified effect event link](#95234-output-specified-effect-event-link)
        - [9.5.2.3.5 State-specified transforming event links summary](#95235-state-specified-transforming-event-links-summary)
  - [Table 7 — State-specified transforming event links summary](#table-7--state-specified-transforming-event-links-summary)
      - [9.5.2.4 State-specified enabling event links](#9524-state-specified-enabling-event-links)
        - [9.5.2.4.1 State-specified agent event link](#95241-state-specified-agent-event-link)
        - [9.5.2.4.2 State-specified instrument event link](#95242-state-specified-instrument-event-link)
        - [9.5.2.4.3 State-specified enabling event links summary](#95243-state-specified-enabling-event-links-summary)
  - [Table 8 — State-specified enabling event links summary](#table-8--state-specified-enabling-event-links-summary)
      - [9.5.2.5 Invocation links](#9525-invocation-links)
        - [9.5.2.5.1 Process invocation and invocation link](#95251-process-invocation-and-invocation-link)
        - [9.5.2.5.2 Self-invocation link](#95252-self-invocation-link)
        - [9.5.2.5.3 Invocation links summary](#95253-invocation-links-summary)
  - [Table 9 — Invocation links summary](#table-9--invocation-links-summary)
    - [9.5.3 Condition links](#953-condition-links)
      - [9.5.3.1 Basic Condition transforming links](#9531-basic-condition-transforming-links)
        - [9.5.3.1.1 Condition consumption link](#95311-condition-consumption-link)
        - [9.5.3.1.2 Condition effect link](#95312-condition-effect-link)
        - [9.5.3.1.3 Condition transforming links summary](#95313-condition-transforming-links-summary)
  - [Table 10 — Condition transforming links summary](#table-10--condition-transforming-links-summary)
      - [9.5.3.2 Basic condition enabling links](#9532-basic-condition-enabling-links)
        - [9.5.3.2.1 Condition agent link](#95321-condition-agent-link)
        - [9.5.3.2.2 Condition instrument link](#95322-condition-instrument-link)
        - [9.5.3.2.3 Basic condition enabling links summary](#95323-basic-condition-enabling-links-summary)
  - [Table 11 — Basic condition enabling links summary](#table-11--basic-condition-enabling-links-summary)
      - [9.5.3.3 Condition state-specified transforming links](#9533-condition-state-specified-transforming-links)
        - [9.5.3.3.1 Condition state-specified consumption link](#95331-condition-state-specified-consumption-link)
        - [9.5.3.3.2 Condition input-output-specified effect link](#95332-condition-input-output-specified-effect-link)
        - [9.5.3.3.3 Condition input-specified effect link](#95333-condition-input-specified-effect-link)
        - [9.5.3.3.4 Condition output-specified effect link](#95334-condition-output-specified-effect-link)
        - [9.5.3.3.5 Condition state-specified transforming links summary](#95335-condition-state-specified-transforming-links-summary)
  - [Table 12 — Condition state-specified transforming links summary](#table-12--condition-state-specified-transforming-links-summary)
  - [Table 12 (continued)](#table-12-continued)
      - [9.5.3.4 Condition state-specified enabling links](#9534-condition-state-specified-enabling-links)
        - [9.5.3.4.1 Condition state-specified agent link](#95341-condition-state-specified-agent-link)
        - [9.5.3.4.2 Condition state-specified instrument link](#95342-condition-state-specified-instrument-link)
      - [9.5.3.3 Condition state-specified enabling links summary](#9533-condition-state-specified-enabling-links-summary)
  - [Table 13 — Condition state-specified enabling links summary](#table-13--condition-state-specified-enabling-links-summary)
    - [9.5.4 Exception links](#954-exception-links)
      - [9.5.4.1 Minimal, Expected, and Maximal Process Duration and Duration Distribution](#9541-minimal-expected-and-maximal-process-duration-and-duration-distribution)
      - [9.5.4.2 Overtime exception link](#9542-overtime-exception-link)
      - [9.5.4.3 Undertime exception link](#9543-undertime-exception-link)
  - [10 Structural links](#10-structural-links)
  - [10.1 Kinds of structural links](#101-kinds-of-structural-links)
  - [10.2 Tagged structural link](#102-tagged-structural-link)
    - [10.2.1 Unidirectional tagged structural link](#1021-unidirectional-tagged-structural-link)
    - [10.2.2 Unidirectional null-tagged structural link](#1022-unidirectional-null-tagged-structural-link)
    - [10.2.3 Bidirectional tagged structural link](#1023-bidirectional-tagged-structural-link)
    - [10.2.4 Reciprocal tagged structural link](#1024-reciprocal-tagged-structural-link)
  - [10.3 Fundamental structural relations](#103-fundamental-structural-relations)
    - [10.3.1 Kinds of fundamental structural relations](#1031-kinds-of-fundamental-structural-relations)
    - [10.3.2 Aggregation-participation relation link](#1032-aggregation-participation-relation-link)
    - [10.3.3 Exhibition-characterization link](#1033-exhibition-characterization-link)
      - [10.3.3.1 Exhibition-characterization relation link expression](#10331-exhibition-characterization-relation-link-expression)
      - [10.3.3.2 Attribute state and exhibitor features](#10332-attribute-state-and-exhibitor-features)
        - [10.3.3.2.1 Attribute state as value](#103321-attribute-state-as-value)
        - [10.3.3.2.2 Expressing exhibitor-feature relation](#103322-expressing-exhibitor-feature-relation)
    - [10.3.4 Generalization-specialization and inheritance](#1034-generalization-specialization-and-inheritance)
      - [10.3.4.1 Generalization-specialization relation link](#10341-generalization-specialization-relation-link)
      - [10.3.4.2 Inheritance through specialization](#10342-inheritance-through-specialization)
      - [10.3.4.3 Specialization restriction through discriminating attribute](#10343-specialization-restriction-through-discriminating-attribute)
    - [10.3.5 Classification-instantiation link](#1035-classification-instantiation-link)
      - [10.3.5.1 Classification-instantiation relation link](#10351-classification-instantiation-relation-link)
      - [10.3.5.2 Instances of object class and process class](#10352-instances-of-object-class-and-process-class)
    - [10.3.6 Structural relation link and tagged structural link summary](#1036-structural-relation-link-and-tagged-structural-link-summary)
    - [Table 14 — Structural relations and link summary](#table-14--structural-relations-and-link-summary)
  - [10.4 State-specified structural relations and links](#104-state-specified-structural-relations-and-links)
    - [10.4.1 State-specified characterization relation link](#1041-state-specified-characterization-relation-link)
    - [10.4.2 State-specified tagged structural relations](#1042-state-specified-tagged-structural-relations)
      - [10.4.2.1 State-specified tagged structural links](#10421-state-specified-tagged-structural-links)
      - [10.4.2.2 Unidirectional source state-specified tagged structural link](#10422-unidirectional-source-state-specified-tagged-structural-link)
      - [10.4.2.3 Unidirectional destination state-specified tagged structural link](#10423-unidirectional-destination-state-specified-tagged-structural-link)
      - [10.4.2.4 Unidirectional source-and-destination state-specified tagged structural link](#10424-unidirectional-source-and-destination-state-specified-tagged-structural-link)
      - [10.4.2.5 Bidirectional source-or-destination state-specified tagged structural link](#10425-bidirectional-source-or-destination-state-specified-tagged-structural-link)
      - [10.4.2.6 Bidirectional source-and-destination state-specified tagged structural link](#10426-bidirectional-source-and-destination-state-specified-tagged-structural-link)
      - [10.4.2.7 Reciprocal source-or-destination state-specified tagged structural link](#10427-reciprocal-source-or-destination-state-specified-tagged-structural-link)
      - [10.4.2.8 Reciprocal source-and-destination state-specified tagged structural link](#10428-reciprocal-source-and-destination-state-specified-tagged-structural-link)
      - [10.4.2.9 State-specified tagged structural link summary](#10429-state-specified-tagged-structural-link-summary)
    - [Table 15 — State-specified structural relations and links summary](#table-15--state-specified-structural-relations-and-links-summary)
  - [11 Relationship cardinalities](#11-relationship-cardinalities)
  - [11.1 Object multiplicity in structural and procedural links](#111-object-multiplicity-in-structural-and-procedural-links)
  - [Table 16 — Link optionality summary](#table-16--link-optionality-summary)
  - [11.2 Object multiplicity expressions and constraints](#112-object-multiplicity-expressions-and-constraints)
  - [11.3 Attribute value and multiplicity constraints](#113-attribute-value-and-multiplicity-constraints)
  - [12 Logical operators: AND, XOR, and OR](#12-logical-operators-and-xor-and-or)
  - [12.1 Logical AND procedural links](#121-logical-and-procedural-links)
  - [12.2 Logical XOR and OR procedural links](#122-logical-xor-and-or-procedural-links)
  - [12.3 Diverging and converging XOR and OR links](#123-diverging-and-converging-xor-and-or-links)
  - [Table 17 — Summary of XOR and OR converging consumption and result links](#table-17--summary-of-xor-and-or-converging-consumption-and-result-links)
  - [Table 18 — Summary of XOR and OR diverging consumption and result link fans](#table-18--summary-of-xor-and-or-diverging-consumption-and-result-link-fans)
  - [Table 19 — Summary of XOR and OR effect link fans](#table-19--summary-of-xor-and-or-effect-link-fans)
  - [Table 20 — Summary of agent and instrument link fans](#table-20--summary-of-agent-and-instrument-link-fans)
  - [Table 21 — Summary of invocation link fans](#table-21--summary-of-invocation-link-fans)
  - [12.4 State-specified XOR and OR link fans](#124-state-specified-xor-and-or-link-fans)
  - [12.5 Control-modified link fans](#125-control-modified-link-fans)
  - [Table 22 — Event and condition effect link fans](#table-22--event-and-condition-effect-link-fans)
  - [12.6 State-specified control-modified link fans](#126-state-specified-control-modified-link-fans)
  - [Table 23 — State-specified and stateless control-modified link fans](#table-23--state-specified-and-stateless-control-modified-link-fans)
  - [12.7 Link probabilities and probabilistic link fans](#127-link-probabilities-and-probabilistic-link-fans)
  - [13 Execution path and path labels](#13-execution-path-and-path-labels)
  - [14 Context management with OPM](#14-context-management-with-opm)
  - [14.1 Completing the SD](#141-completing-the-sd)
  - [14.2 Achieving model comprehension](#142-achieving-model-comprehension)
    - [14.2.1 OPM refinement-abstraction mechanisms](#1421-opm-refinement-abstraction-mechanisms)
      - [14.2.1.1 State expression and state suppression](#14211-state-expression-and-state-suppression)
      - [14.2.1.2 Unfolding and folding](#14212-unfolding-and-folding)
      - [14.2.1.3 In-zooming and out-zooming](#14213-in-zooming-and-out-zooming)
    - [14.2.2 Control (operational) semantics within an in-zoomed process context](#1422-control-operational-semantics-within-an-in-zoomed-process-context)
      - [14.2.2.1 Implicit invocation link](#14221-implicit-invocation-link)
      - [14.2.2.2 Implicit parallel invocation link set](#14222-implicit-parallel-invocation-link-set)
      - [14.2.2.3 Implicit invocation links summary](#14223-implicit-invocation-links-summary)
      - [Table 24 — Implicit invocation links summary](#table-24--implicit-invocation-links-summary)
      - [14.2.2.4 Link distribution across context](#14224-link-distribution-across-context)
        - [14.2.2.4.1 Semantics of link distribution](#142241-semantics-of-link-distribution)
        - [14.2.2.4.2 Event and condition link constraint](#142242-event-and-condition-link-constraint)
        - [14.2.2.4.3 Split state-specified transforming links](#142243-split-state-specified-transforming-links)
      - [Table 25 — Split input-output specified effect link pair summary](#table-25--split-input-output-specified-effect-link-pair-summary)
      - [14.2.2.4 Operational instances of involved object set](#14224-operational-instances-of-involved-object-set)
      - [14.2.2.5 Synchronous vs. asynchronous process refinement](#14225-synchronous-vs-asynchronous-process-refinement)
      - [14.2.2.6 Expressing the context of a system](#14226-expressing-the-context-of-a-system)
        - [14.2.2.6.1 Navigating the contexts of a system](#142261-navigating-the-contexts-of-a-system)
          - [14.2.2.6.1.1 The OPD process tree](#1422611-the-opd-process-tree)
          - [14.2.2.6.1.2 The OPD object tree](#1422612-the-opd-object-tree)
          - [14.2.2.6.1.3 OPM diagram labels](#1422613-opm-diagram-labels)
          - [14.2.2.6.1.4 OPD process tree edge label](#1422614-opd-process-tree-edge-label)
          - [14.2.2.6.1.5 System map and model views](#1422615-system-map-and-model-views)
        - [14.2.2.6.2 Whole System OPL specification](#142262-whole-system-opl-specification)
    - [Table 26 — Whole system OPL for Dish Washing System](#table-26--whole-system-opl-for-dish-washing-system)
    - [14.2.3 OPM fact consistency principle](#1423-opm-fact-consistency-principle)
    - [14.2.4 Abstraction ambiguity resolution for procedural links](#1424-abstraction-ambiguity-resolution-for-procedural-links)
      - [14.2.4.1 Abstraction and procedural link precedence](#14241-abstraction-and-procedural-link-precedence)
      - [14.2.4.2 Precedence among transforming links](#14242-precedence-among-transforming-links)
      - [14.2.4.3 Precedence among transforming and enabling links](#14243-precedence-among-transforming-and-enabling-links)
      - [14.2.4.4 Secondary precedence among same-kind non-control links and control links](#14244-secondary-precedence-among-same-kind-non-control-links-and-control-links)
      - [14.2.4.5 Summary of the procedural links semantic strength](#14245-summary-of-the-procedural-links-semantic-strength)
  - [Annex A (normative)](#annex-a-normative)
  - [OPL formal syntax in EBNF](#opl-formal-syntax-in-ebnf)
  - [A.1 General](#a1-general)
  - [A.2 OPL in the context of OPD](#a2-opl-in-the-context-of-opd)
  - [A.3 Preliminaries](#a3-preliminaries)
    - [A.3.1 EBNF syntax](#a31-ebnf-syntax)
    - [A.3.2 Base declarations](#a32-base-declarations)
    - [A.3.3 OPL special sequences](#a33-opl-special-sequences)
  - [A.4 OPL Syntax](#a4-opl-syntax)
    - [A.4.1 OPL document structure](#a41-opl-document-structure)
    - [A.4.2 OPL Identifiers](#a42-opl-identifiers)
    - [A.4.3 OPL lists](#a43-opl-lists)
    - [A.4.4 OPL Thing description](#a44-opl-thing-description)
      - [A.4.4.1 Thing description sentence](#a441-thing-description-sentence)
      - [A.4.4.2 Generic property sentence](#a442-generic-property-sentence)
      - [A.4.4.3 Type description sentence](#a443-type-description-sentence)
      - [A.4.4.4 State description sentence](#a444-state-description-sentence)
    - [A.4.5 OPL Procedural sentences](#a45-opl-procedural-sentences)
      - [A.4.5.1 Procedural sentence](#a451-procedural-sentence)
      - [A.4.5.2 OPL Transformations](#a452-opl-transformations)
        - [A.4.5.2.1 Transforming sentence](#a4521-transforming-sentence)
        - [A.4.5.2.2 Consumption sentence](#a4522-consumption-sentence)
        - [A.4.5.2.3 Result sentence](#a4523-result-sentence)
        - [A.4.5.2.4 Effect sentence](#a4524-effect-sentence)
        - [A.4.5.2.5 Change sentence](#a4525-change-sentence)
      - [A.4.5.3 OPL Enablers](#a453-opl-enablers)
        - [A.4.5.3.1 Enabling sentences](#a4531-enabling-sentences)
        - [A.4.5.3.2 Agent sentence](#a4532-agent-sentence)
        - [A.4.5.3.3 Instrument sentence](#a4533-instrument-sentence)
      - [A.4.5.4 OPL Flow of control](#a454-opl-flow-of-control)
        - [A.4.5.4.1 Control sentence](#a4541-control-sentence)
        - [A.4.5.4.2 Event sentence](#a4542-event-sentence)
        - [A.4.5.4.3 Condition sentence](#a4543-condition-sentence)
        - [A.4.5.4.4 Invocation sentence](#a4544-invocation-sentence)
        - [A.4.5.4.5 Exception sentence](#a4545-exception-sentence)
    - [A.4.6 OPL Structural sentences](#a46-opl-structural-sentences)
      - [A.4.6.1 Structural sentence](#a461-structural-sentence)
      - [A.4.6.2 OPL tagged structures](#a462-opl-tagged-structures)
        - [A.4.6.2.1 Tagged structural sentence](#a4621-tagged-structural-sentence)
        - [A.4.6.2.2 Unidirectional tagged structural sentence](#a4622-unidirectional-tagged-structural-sentence)
        - [A.4.6.2.3 Bidirectional tagged structural sentences](#a4623-bidirectional-tagged-structural-sentences)
      - [A.4.6.3 OPL fundamental structures](#a463-opl-fundamental-structures)
        - [A.4.6.3.1 Aggregation sentences](#a4631-aggregation-sentences)
        - [A.4.6.3.2 Characterization sentences](#a4632-characterization-sentences)
      - [A.4.6.4 Exhibition sentences](#a464-exhibition-sentences)
      - [A.4.6.5 Specialization sentences](#a465-specialization-sentences)
      - [A.4.6.6 Instantiation sentences](#a466-instantiation-sentences)
    - [A.4.7 OPL Context management](#a47-opl-context-management)
      - [A.4.7.1 Context management sentence](#a471-context-management-sentence)
      - [A.4.7.2 Unfolding sentences](#a472-unfolding-sentences)
      - [A.4.7.3 Folding sentences](#a473-folding-sentences)
      - [A.4.7.4 In zoom sentence](#a474-in-zoom-sentence)
      - [A.4.7.5 Out zooming sentence](#a475-out-zooming-sentence)
  - [Annex B (informative)](#annex-b-informative)
  - [Guidance for OPM](#guidance-for-opm)
  - [B.1 General](#b1-general)
  - [B.2 Thing importance OPM principle](#b2-thing-importance-opm-principle)
  - [B.3 What a new OPD should contain](#b3-what-a-new-opd-should-contain)
  - [B.4 The element representation OPM principle](#b4-the-element-representation-opm-principle)
  - [B.5 The multiple thing copies convention](#b5-the-multiple-thing-copies-convention)
  - [B.6 Naming guidelines](#b6-naming-guidelines)
    - [B.6.1 Importance of name selection](#b61-importance-of-name-selection)
    - [B.6.2 Object naming](#b62-object-naming)
    - [B.6.3 Process naming](#b63-process-naming)
    - [B.6.4 State naming](#b64-state-naming)
    - [B.6.5 Capitalization convention](#b65-capitalization-convention)
  - [Annex C (informative)](#annex-c-informative)
  - [Modelling OPM using OPM](#modelling-opm-using-opm)
  - [C.1 OPM models of OPM](#c1-opm-models-of-opm)
  - [C.2 OPM model structure](#c2-opm-model-structure)
    - [Figure C.1 — OPM model structure](#figure-c1--opm-model-structure)
  - [C.3 OPD Construct model](#c3-opd-construct-model)
    - [Figure C.2 — Model of OPD Construct and Basic Construct](#figure-c2--model-of-opd-construct-and-basic-construct)
  - [Figure C.3 — OPD Construct and Basic Construct construction](#figure-c3--opd-construct-and-basic-construct-construction)
  - [C.4 OPM Element models](#c4-opm-element-models)
  - [Figure C.4 — OPM model of OPM Element](#figure-c4--opm-model-of-opm-element)
  - [Figure C.5 — OPM model of Thing](#figure-c5--opm-model-of-thing)
  - [Figure C.6 — Example of state-specific object](#figure-c6--example-of-state-specific-object)
  - [Figure C.7 — OPM model of stateful object and state](#figure-c7--opm-model-of-stateful-object-and-state)
  - [Figure C.8 — OPM model of links](#figure-c8--opm-model-of-links)
  - [Figure C.9 — OPM model of Thing generic properties](#figure-c9--opm-model-of-thing-generic-properties)
  - [Figure C.10 — OPM model of Thing symbolic representation](#figure-c10--opm-model-of-thing-symbolic-representation)
  - [Figure C.11 — OPM model of the eight Thing symbol representations](#figure-c11--opm-model-of-the-eight-thing-symbol-representations)
  - [Figure C.12 — Basic Construct elaboration](#figure-c12--basic-construct-elaboration)
  - [Figure C.13 — OPM model of Basic Structural Construct](#figure-c13--opm-model-of-basic-structural-construct)
  - [Figure C.14 — OPM model of Basic Procedural Construct](#figure-c14--opm-model-of-basic-procedural-construct)
  - [Figure C.15 — OPM model of Transformation Construct](#figure-c15--opm-model-of-transformation-construct)
  - [Figure C.16 — OPM model of Transformation Construct link directionality](#figure-c16--opm-model-of-transformation-construct-link-directionality)
  - [Figure C.17 — OPM model of Basic Enablement Construct](#figure-c17--opm-model-of-basic-enablement-construct)
  - [Figure C.18 — OPM model of state-specified agent construct with mapped example](#figure-c18--opm-model-of-state-specified-agent-construct-with-mapped-example)
  - [C.5 In-zooming and out-zooming models](#c5-in-zooming-and-out-zooming-models)
    - [C.5.1 The in-zooming and out-zooming mechanisms](#c51-the-in-zooming-and-out-zooming-mechanisms)
  - [Figure C.19 — New-Diagram In-Zooming and New-Diagram Out-Zooming models](#figure-c19--new-diagram-in-zooming-and-new-diagram-out-zooming-models)
  - [Figure C.20 — New-Diagram In-Zooming and New-Diagram Out-Zooming elaboration](#figure-c20--new-diagram-in-zooming-and-new-diagram-out-zooming-elaboration)
    - [C.5.2 Simplifying an OPD](#c52-simplifying-an-opd)
  - [Figure C.21 — Simplifying an OPD](#figure-c21--simplifying-an-opd)
  - [C.6 OPM Process Performance Controlling model](#c6-opm-process-performance-controlling-model)
    - [C.6.1 OPM Process Performance Controlling System – SD](#c61-opm-process-performance-controlling-system--sd)
    - [C.6.2 Process Performance Controlling in-zoomed as SD1](#c62-process-performance-controlling-in-zoomed-as-sd1)
    - [C.6.3 Process Initiating in-zoomed as SD1.1](#c63-process-initiating-in-zoomed-as-sd11)
    - [C.6.4 Precondition Evaluating in-zoomed as SD1.1.1](#c64-precondition-evaluating-in-zoomed-as-sd111)
    - [C.6.5 Transformee Set Checking in-zoomed as SD1.1.1.1](#c65-transformee-set-checking-in-zoomed-as-sd1111)
    - [C.6.6 Process Performing in-zoomed as SD1.2](#c66-process-performing-in-zoomed-as-sd12)
    - [C.6.7 Initial Process Performing in-zoomed as SD1.2.1](#c67-initial-process-performing-in-zoomed-as-sd121)
    - [C.6.8 Main Process Performing in-zoomed as SD1.2.2](#c68-main-process-performing-in-zoomed-as-sd122)
    - [C.6.9 Final Process Performing in-zoomed as SD1.2.3](#c69-final-process-performing-in-zoomed-as-sd123)
  - [Annex D (informative)](#annex-d-informative)
  - [OPM dynamics and simulation](#opm-dynamics-and-simulation)
  - [D.1 OPM executability](#d1-opm-executability)
  - [D.2 Change and effect](#d2-change-and-effect)
  - [D.3 Existence and transformation](#d3-existence-and-transformation)
  - [D.4 Timeline OPM principle](#d4-timeline-opm-principle)
  - [D.5 Timed events](#d5-timed-events)
  - [D.6 Object history and the lifespan diagram](#d6-object-history-and-the-lifespan-diagram)
  - [D.7 Process duration](#d7-process-duration)
    - [Example 1](#example-1)
    - [Example 2](#example-2)
    - [Example 3](#example-3)
    - [Example 4](#example-4)


---

## Introduction

Object-Process Methodology (OPM) is a compact conceptual approach, language, and methodology for modelling and knowledge representation of automation systems. The application of OPM ranges from simple assemblies of elemental components to complex, multidisciplinary, dynamic systems. OPM is suitable for implementation and support by tools using information and computer technology. This Publicly Available Specification specifies both the language and methodology aspects of OPM in order to establish a common basis for system architects, designers, and OPM-compliant tool developers to model all kinds of systems.

OPM provides two semantically equivalent modalities of representation for the same model: graphical and textual. A set of hierarchically structured, interrelated Object-Process Diagrams (OPDs) constitutes the graphical model, and a set of automatically generated sentences in a subset of the English language constitutes the textual model expressed in the Object-Process Language (OPL). In a graphical-visual model, each OPD consists of OPM elements, depicted as graphic symbols, sometimes with label annotation. The OPD syntax specifies the consistent and correct ways to manage the arrangement of those graphically elements. Using OPL, OPM generates the corresponding textual model for each OPD in a manner that retains the constraints of the graphical model. Since the syntax and semantics of OPL are a subset of English natural language, domain experts easily understand the textual model.

OPM notation supports the conceptual modelling of systems with formal syntax and semantics. This formality serves as the basis for model-based systems engineering in general, including systems architecting, engineering, development, life cycle support, communication, and evolution. Furthermore, the domain-independent nature of OPM opens system modelling to the entire scientific, commercial and industrial community for developing, investigating and analysing manufacturing and other industrial and business systems inside their specific application domains; thereby enabling companies to merge and provide for interoperability of different skills and competencies into a common intuitive yet formal framework.

OPM facilitates a common view of the system under construction, test, integration, and daily maintenance, providing for working in a multidisciplinary environment. Moreover, using OPM, companies can improve their overall, big-picture view of the system’s functionality, flexibility in assignment of personnel to tasks, and managing exceptions and error recovery. System specification is extensible for any necessary detail, encompassing the functional, structural and behavioural aspects of a system.

One particular application of OPM is in the drafting and authoring of technical standards. OPM helps sketch the implementation of a standard and identify weaknesses in the standard to reduce, thereby significantly improving the quality of successive drafts. With OPM, even as the model-based text of a system expands to include more details, the underlying model keeps maintaining its high degree of formality and consistency.

This Publicly Available Specification provides a baseline for system architects and designers, who can use it to model systems concisely and effectively. OPM tool vendors can utilise the PAS as a formal standard specification for creating software tools to enhance conceptual modelling.

This Publicly Available Specification provides a presentation of the normative text that follows the Extended Backus-Naur Form (EBNF) specification of the language syntax. All elements are presented in Clauses 6 to 13 with only minimal reference to methodological aspects, Clause 14 presents the context management mechanisms related to in-zooming and unfolding.

This specification utilizes several conventions for the presentation of OPM. Specifically, Arial bold font in text and Arial bold italic font in figure captions, table captions and headings distinguish label names for OPM objects, processes, states, and link tags. OPL reserved words are in Arial regular font with commas and periods in Arial bold font. Most figures contain both a graphic image, the OPD portion, and a textual equivalent, the OPL portion. Because this is a language specification, the precise use of term definitions is essential and several terms in common use have particular meaning when using OPM. Clause B.6 explains other conventions for the use of OPM.

Annex A presents the formal syntax for OPL, in EBNF form.

Annex B presents conventions and patterns commonly used in OPM applications.

Annex C presents aspects of OPM as OPM models.

Annex D summarizes the dynamic and simulation capabilities of OPM.

The International Organization for Standardization (ISO) draws attention to the fact that it is claimed that compliance with this document may involve the use of a patent concerning OPM as a modelling system given in Clauses 6 to 14.

ISO takes no position concerning the evidence, validity and scope of this patent right.

The holder of this patent right has assured the ISO that he/she is willing to negotiate licences either free of charge or under reasonable and non-discriminatory terms and conditions with applicants throughout the world. In this respect, the statement of the holder of this patent right is registered with ISO. Information may be obtained from:

Prof. Dov Dori

Technion Israel Institute of Technology

Technion City

Haifa 32000, Israel

<dori@ie.technion.ac.il>

Attention is drawn to the possibility that some of the elements of this document may be the subject of patent rights other than those identified above. ISO shall not be held responsible for identifying any or all such patent rights.

ISO (<www.iso.org/patents>) and IEC (<http://patents.iec.ch>) maintain on-line databases of patents relevant to their standards. Users are encouraged to consult the databases for the most up to date information concerning patents.

---

## Automation systems and integration — Object-Process Methodology

## 1 Scope

This Publicly Available Specification specifies Object-Process Methodology (OPM) with detail sufficient for enabling practitioners to utilise the concepts, semantics, and syntax of Object-Process Methodology as a modelling paradigm and language for producing conceptual models at various extents of detail, and for enabling tool vendors to provide application modelling products to aid those practitioners.

While this Publicly Available Specification presents some examples for the use of Object-Process Methodology to improve clarity, it does not attempt to provide a complete reference for all the possible applications of Object-Process Methodology.

## 2 Normative references

There are no normative references.

## 3 Terms and definitions

For the purposes of this document, the following terms and definitions apply.

## 3.1 abstraction

decreasing the extent of detail and system model completeness (3.8) in order to achieve better comprehension

## 3.2 affectee

transformee (3.78) that is affected by a process (3.58) occurrence, i.e. its state (3.69) changes

Note 1 to entry: An affectee can only be a stateful object (3.66). A stateless object (3.67) can only be created or consumed, but not affected.

## 3.3 agent

enabler (3.17) that is a human or a group of humans

## 3.4 attribute

object (3.39) that characterizes a thing (3.76) other than itself

## 3.5 behaviour

transformation (3.77) of objects (3.39) resulting from the execution of an Object-Process Methodology (3.43) model comprising a collection of things (3.76) and links (3.36) to objects in the model

## 3.6 beneficiary

&lt;system&gt; stakeholder (3.65) who gains functional value (3.82) from the system’s operation (3.46)

## 3.7 class

collection of things (3.76) with the same perseverance (3.50), essence, and affiliation values, and the same feature (3.21) and state (3.69) set

## 3.8 completeness

&lt;system model&gt; extent to which all the details of a system are specified in a model

## 3.9 condition link

procedural link (3.56) from an object (3.39) or object state (3.69) to a process (3.58), denoting a procedural constraint

## 3.10 consumee

transformee (3.78) that a process (3.58) occurrence consumes or eliminates

## 3.11 context

&lt;model&gt; portion of an Object-Process Methodology (3.43) model represented by an Object-Process Diagram (3.41) and corresponding Object-Process Language (3.42) text

## 3.12 control link

procedural link (3.56) with additional control semantics

## 3.13 control modifier

symbol embellishing a link (3.36) to add control semantics to it, making it a control link (3.12)

Note 1 to entry: The control modifiers are the symbols ‘e’ for event (3.18) and ‘c’ for condition.

## 3.14 discriminating attribute

attribute (3.4) whose different values (3.81) identify corresponding specialization relations

## 3.15 effect

change in the state (3.69) of an object (3.39) or an attribute (3.4) value (3.81)

Note 1 to entry: An effect only applies to a stateful object (3.66).

## 3.16 element

thing (3.76) or link (3.36)

## 3.17 enabler

&lt;process&gt; object (3.39) that enables a process (3.58) but which the process does not transform

## 3.18 event

&lt;OPM&gt; point in time of creation (or appearance) of an object, or entrance of an object (3.39) to a particular state (3.69), either of which may initiate an evaluation of the process (3.58) precondition (3.53)

## 3.19 event link

control link (3.12) denoting an event (3.18) originating from an object (3.39) or object state (3.69) to a process (3.58)

## 3.20 exhibitor

thing (3.76) that exhibits (is characterized by) a feature (3.21) by means of the exhibition-characterization relation

## 3.21 feature

attribute (3.4) or operation (3.46)

## 3.22 folding

mechanism of abstraction (3.1) achieved by hiding the refineables (3.61) of an unfolded refinee (3.62)

Note 1 to entry: The four kinds of folded refineables are parts (part folding), features (3.21) (feature folding), specializations (specialization folding), and instances (3.28) (instance folding).

Note 2 to entry: Folding is primarily applied to objects (3.39). When applied to a process, its subprocesses are unordered, which is adequate for modelling asynchronous systems, in which processes’ temporal order is undefined.

Note 3 to entry: The opposite of folding is unfolding (3.80).

## 3.23 function

process (3.58) that provides functional value (3.82) to a beneficiary (3.6)

## 3.24 general

&lt;OPM&gt; refineable (3.61) with specializations

## 3.25 informatical

of, or pertaining to informatics, e.g. data, information, knowledge

## 3.26 inheritance

assignment of Object-Process Methodology (3.43) elements (3.16) of a general (3.24) to its specializations

## 3.27 input link

link (3.36) from object (3.39) source (input) state (3.69) to the transforming process (3.58)

## 3.28 instance

&lt;model&gt; object (3.39) instance or process (3.58) instance that is a refinee (3.62) in a classification-instantiation relation

## 3.29 instance

&lt;operational&gt; object (3.39) instance or process (3.58) instance that is an actual, uniquely identifiable thing (3.76) that exists during model operation (3.46), e.g. during simulation or runtime implementation

Note 1 to entry: A process instance is identifiable by the operational instances of the involved object set (3.32) during process occurrence and the process start and end time stamps of the occurrence.

## 3.30 instrument

non-human enabler (3.17)

## 3.31 invocation

&lt;process&gt; initiating of a process (3.58) by a process

## 3.32 involved object set

union of preprocess object set (3.54) and postprocess object set (3.52)

## 3.33 in-zoom context

things (3.76) and links (3.36) within the boundary of the thing being in-zoomed

## 3.34 in-zooming

&lt;object&gt; object (3.39) part unfolding (3.80) that indicates spatial ordering of the constituent objects

## 3.35 in-zooming

&lt;process&gt; process (3.58) part unfolding (3.80) that indicates temporal partial ordering of the constituent processes

## 3.36 link

graphical expression of a structural relation (3.73) or a procedural relation (3.57) between two Object-Process Methodology (3.43) things (3.76)

## 3.37 metamodel

model of a modelling language or part of a modelling language

## 3.38 model fact

relation between two Object-Process Methodology (3.43) things (3.76) or states (3.69) in the Object-Process Methodology model

## 3.39 object

&lt;OPM&gt; model element (3.16) representing a thing (3.76) that does or might exist physically or informatically (3.25)

## 3.40 object class

pattern for objects (3.39) that have the same structure (3.74) and pattern of transformation (3.77)

## 3.41 Object-Process Diagram (OPD)

Object-Process Methodology (3.43) graphic representation of an Object-Process Methodology model or part of a model, in which objects (3.39) and processes (3.58) in the universe of interest appear together with the structural links (3.72) and procedural links (3.56) among them

## 3.42 Object-Process Language (OPL)

subset of English natural language that represents textually the Object-Process Methodology (3.43) model that the Object-Process Diagram (3.42) represents graphically

## 3.43 Object-Process Methodology (OPM)

formal language and method for specifying complex, multidisciplinary systems in a single function-structure-behaviour unifying model that uses a bimodal graphic-text representation of objects (3.39) in the system and their transformation (3.77) or use by processes (3.58)

## 3.44 OPD object tree

tree graph, whose root is an object (3.39), depicting elaboration of the object through refinement (3.63)

## 3.45 OPD process tree

tree graph whose root is the System Diagram (3.75) and each node is an Object-Process Diagram (3.42) obtained by in-zooming (3.35) of a process (3.58) in its ancestor Object-Process Diagram (or the System Diagram) and each directed edge points from the refined process at the parent Object-Process Diagram to the same process in the child Object-Process Diagram

Note 1 to entry: Object-Process Methodology (3.43) model elaboration usually occurs by process decomposition through in-zooming, therefore the OPD process tree is the primary way to navigate an Object-Process Methodology model.

## 3.46 operation

process (3.58) that a thing (3.76) performs, which characterizes the thing other than itself

## 3.47 output link

link (3.36) from the transforming process (3.58) to the output (destination) state (3.69) of an object (3.39)

## 3.48 out-zooming

&lt;object&gt; inverse of object (3.39) in-zooming (3.34)

## 3.49 out-zooming

&lt;process&gt; inverse of process (3.58) in-zooming (3.35)

## 3.50 perseverance

property (3.60) of thing (3.76) which can be static, defining an object (3.39), or dynamic, defining a process (3.58)

## 3.51 postcondition

&lt;process&gt; condition that is the outcome of successful process (3.58) completion

## 3.52 postprocess object set

collection of objects (3.39) remaining or resulting from process (3.58) completion

Note 1 to entry: The postprocess object set may include stateful objects (3.66), for which specific states (3.69) result from process performance.

## 3.53 precondition

&lt;process&gt; condition for starting a process (3.58)

## 3.54 preprocess object set

collection of objects (3.39) to evaluate prior to starting a process (3.58)

Note 1 to entry: The collection of the objects may include stateful objects (3.66) for which specific states (3.69) are necessary for process performance.

## 3.55 primary essence

&lt;system&gt; essence of the majority of things (3.76) in a system, which can be either informatical (3.25) or physical

## 3.56 procedural link

graphical notation of *procedural relation* (3.57) in Object-Process Methodology (3.43)

## 3.57 procedural relation

connection or association between an *object* (3.39) or *object state* (3.69) and a *process* (3.58)

Note 1 to entry: Procedural relations specify how the system operates to attain its *function* (3.23), designating time-dependent or conditional initiating of processes that transform objects.

Note 2 to entry: An *invocation* (3.31) or exception link (3.36) signifies a transient object in the flow of execution control between two processes.

## 3.58 process

*transformation* (3.77) of one or more *objects* (3.39) in the system

## 3.59 process class

pattern for *processes* (3.58) that perform the same *object* (3.39) *transformation* (3.77) pattern

## 3.60 property

modelling annotation common to all *elements* (3.16) of a specific kind that serve to distinguish that element

Note 1 to entry: Cardinality constraints, path labels, and *structural link* (3.72) tags are frequent property annotations.

Note 2 to entry: Unlike an *attribute* (3.4), the value of a property may not change during model simulation or operational implementation. Each kind of element has its own set of properties.

Note 3 to entry: Property is an attribute of an element in the Object-Process Methodology (3.43) metamodel (3.37).

## 3.61 refineable

<OPM> *thing* (3.76) amenable to *refinement* (3.63), which can be a *whole* (3.83), an *exhibitor* (3.20), a *general* (3.24), or a *class* (3.7)

## 3.62 refinee

thing (3.76) that refines a *refineable* (3.61), which can be a part, a *feature* (3.21), a specialization, or an *instance* (3.29)

Note 1 to entry: Each of the four kinds of refinees has a corresponding refineable (part-whole, feature-exhibitor, specialization-generalization, instance-class).

## 3.63 refinement

<model> elaboration that increases the extent of detail and the consequent model *completeness* (3.8)

## 3.64 resultee

*transformee* (3.78) that a *process* (3.58) occurrence creates

## 3.65 stakeholder

<OPM> individual, organization, or group of people that has an interest in, or might be affected by the system being contemplated, developed, or deployed

---

## 3.66 stateful object

*object* (3.39) with specified *states* (3.69)

## 3.67 stateless object

*object* (3.39) lacking specified *states* (3.69)

## 3.68 state

<object> possible situation or position of an *object* (3.39)

Note 1 to entry: In Object-Process Methodology (3.43) there is no concept of process state, such as “started”, “in process”, or “finished” within a model. Instead, Object-Process Methodology represents and models subprocesses, such as starting, processing, or finishing.

## 3.69 state

<system> snapshot of the system model taken at a certain point in time, which shows all the existing *object* (3.39) instances, current states of each *stateful object* (3.66) instance, and the *process* (3.58) instances, with their elapsed times, executing at the time the snapshot occurs

## 3.70 state expression

*refinement* (3.63) involving the revealing of any proper subset of an *object’s* (3.39) set of states (3.69)

## 3.71 state suppression

*abstraction* (3.1) involving the hiding of any proper subset of an *object’s* (3.39) set of states (3.69)

## 3.72 structural link

graphic notation of *structural relation* (3.73) in Object-Process Methodology (3.43)

## 3.73 structural relation

operationally invariant connection or association between things

Note 1 to entry: Structural relations persist in the system for at least some interval of time. They provide the structural aspect of the system, and are not contingent upon conditions that are time-dependent.

## 3.74 structure

<OPM> collection of *objects* (3.39) in an Object-Process Methodology (3.43) model and the non-transient relations or associations among them

## 3.75 System Diagram (SD)

Object-Process Diagram (3.41) with one systemic *process* (3.58) indicating the system *function* (3.23) and the *objects* (3.39) connecting with that function to depict the overall *context* (3.11) for and top-level view of the system

Note 1 to entry: System Diagram is the root of the OPD process tree (3.45) and has no extent of detail beyond the overall context depicted.

## 3.76 thing

<OPM> *object* (3.39) or *process* (3.58)

---

## 4 Symbols

[Figure: Set of graphical symbols used in OPM. Rectangular boxes represent objects, elliptical shapes represent processes. Variations in border style or shading indicate whether the object or process is physical, informatic, or environmental.]

Symbols include:

* object
* physical object
* environmental object
* process
* physical process
* environmental process

[Figure: Additional graphical symbols showing relations and links between objects and processes.]

Relations represented:

* state
* aggregation-participation
* exhibition-characterization
* generalization-specialization
* classification-instantiation

Structural links:

* unidirectional tagged structural link
* bidirectional tagged structural link

Procedural links:

* agent link
* instrument link
* effect link
* consumption link
* result link
* input-output link pair
* instrument event link
* consumption event link
* instrumental condition link
* consumption condition link
* invocation link

[Figure: Additional link types]

* self-invocation link
* over-time exception link
* under-time exception link

---

## 5 Conformance

Anticipating that the implementation of this Publicly Available Specification by toolmakers and utilization by end-users is likely to occur in increments over time, several kinds of conformance criteria are appropriate.

* **a) Partial (symbolic) conformance with OPM** shall use the language part of OPM, namely OPM Semantics and Syntax, by:

1. using only OPM symbols defined in Clause 4 with the meaning assigned to them in this Publicly Available Specification; and
2. using only OPM elements defined in Clauses 7 to 12 with the meaning assigned to them in this Publicly Available Specification.

* **b) Full conformance with OPM** shall require:

1. conformance with a); and
2. conformance with the approach and scheme of modelling systems with OPM, as defined in Clauses 6 and 14.

* **c) Conformance by toolmakers** shall require:

1. conformance with a);
2. provision for b) – users are guided and helped to adhere to b) on the basis of the formalism of a); and
3. support for OPL according to the EBNF definition specified in Annex A.

---

## 6 OPM principles and concepts

## 6.1 OPM modelling principles

### 6.1.1 Modelling as a purpose-serving activity

System function and modelling purpose shall guide the scope and extent of detail of an OPM model. A complex or complicated system may involve many stakeholders, including the beneficiary, owner, users, and regulators, as well as many hardware and software components, exposing different aspects relevant to each stakeholder.

Example: A manufacturing plant that produces widgets may be modelled differently from the viewpoints of the marketing manager and the maintenance manager.

### 6.1.2 Unification of function, structure, and behaviour

The OPM structure model of a system shall be an assembly of the physical and informatical objects connected by structural relations.

The OPM behaviour model reflects mechanisms that act on the system over time to transform objects.

The combination of structure and behaviour enables the system to perform a function that delivers functional value to stakeholders.

### 6.1.3 Identifying functional value

The functional value providing process of a modelled system shall express the function of the system as perceived by the system’s main beneficiary.

Identifying and labelling this primary process is a critical first step in constructing an OPM model.

### 6.1.4 Function versus behaviour

The value of the function to the beneficiary is often expressed in process terms emphasizing behaviour. The modeller should distinguish between function and behaviour to create a clear and unambiguous system model.

Example: River crossing may be achieved by bridge or ferry. Both achieve the same function but differ structurally and behaviourally.

### 6.1.5 System boundary setting

The system’s environment shall be a collection of things outside the system that may interact with it.

### 6.1.6 Clarity and completeness trade-off

Real systems contain overwhelming detail. Understanding requires balancing clarity and completeness. Excessive detail reduces comprehension.

---

## 6.2 OPM Fundamental concepts

### 6.2.1 Bimodal representation

An OPM model shall be bimodal with expression in semantically equivalent graphics and text representations.

Each graphical diagram (OPD) shall have an equivalent textual paragraph using OPL.

### 6.2.2 OPM modelling elements

Elements are of two kinds:

* **things**
* **links**

Things are:

* objects
* processes

Links designate associations between things.

Links are either:

* procedural
* structural

[Figure: OPM metamodel overview showing relationships between OPM Element, OPM Link, Structural Link, Procedural Link, Process, and Object.]

---

### 6.2.3 OPM things: objects and processes

An object is a thing that exists or can exist physically or informatically.

A process expresses the transformation of objects in the system.

Processes transform objects by:

* creating them
* consuming them
* changing their state

---

### 6.2.4 OPM links: procedural and structural

Procedural links denote procedural relations. A procedural relation specifies how the system operates to attain its function.

Structural links denote structural relations that persist for some time interval.

---

### 6.2.5 OPM context management

OPM provides mechanisms for managing contextual scope of model detail.

The fundamental unit is the **OPD (Object-Process Diagram)** depicting modelling elements of that context.

---

### 6.2.6 OPM model implementation

#### 6.2.6.1 Conceptual models versus runtime models

Conceptual models describe structure and behaviour patterns.

Runtime models represent operational instance occurrences.

Simulation can be performed by creating object and process operational instances.

#### 6.2.6.2 OPM model realization

A model expressing consistent detail is implementable as a simulation capable of realizing resources and producing functional value.

#### 6.2.6.3 OPD Navigation and OPL composition

Mechanisms for in-zooming and unfolding provide ways to link diagrams and corresponding OPL descriptions.

---

## 7 OPM thing syntax and semantics

## 7.1 Objects

### 7.1.1 Description

An object is a thing that exists or has the potential of physical or informatical existence.

From a temporal viewpoint, existence of an object is persistent unless a process acts on it.

An OPM object category identifier identifies a pattern of structure, properties, and features.

### 7.1.2 Representation

A rectangular box containing the object name represents an object.

[Figure: Object graphic notation showing a rectangular box labelled “Vehicle Occupant Group”.]

---

## 7.2 Processes

### 7.2.1 Description

A process is a thing that transforms one or more objects.

Transformation may be:

* generation
* effect
* consumption

A process has positive performance time duration.

### 7.2.2 Representation

An ellipse containing the process name represents a process.

[Figure: Process graphic notation showing ellipse labelled “Automatic Crash Responding”.]

---

## 7.3 OPM things

### 7.3.1 OPM thing defined

An OPM thing shall be either an object or a process.

Objects and processes are symmetric in many respects and depend on each other.

### 7.3.2 Object-process test

To distinguish whether a noun represents an object or a process:

A process must satisfy three criteria:

* time association
* verb association
* object transformation

Example: *Flight* is a process because it transforms the location of an airplane.

### 7.3.3 OPM thing generic properties

All OPM things have three generic properties:

* **Perseverance** — static (object) or dynamic (process)
* **Essence** — physical or informatical
* **Affiliation** — systemic or environmental

[Figure: Generic attribute combinations showing physical/informational and systemic/environmental variations for objects and processes.]

### 7.3.4 Default values of thing generic properties

The default value of affiliation is systemic.

System primary essence is determined by the majority essence of contained things.

### 7.3.5 Object states

#### 7.3.5.1 Stateful and stateless objects

A stateful object has a set of permissible states.

A stateless object has no specified states.

#### 7.3.5.2 Object state representation

A rounded rectangle inside an object represents a state.

Example states: *inside the museum*, *out of the museum*.

[Figure: Museum Visitor object with two states.]

#### 7.3.5.3 Initial, default, and final states

* initial state: state at object creation
* final state: state when object is consumed
* default state: most likely state during random inspection

#### 7.3.5.4 Representation

Initial states: thick border
Final states: double border
Default states: diagonal arrow indicator

[Figure: Specification object showing states preliminary (initial), approved (default), cancelled (final).]

#### 7.3.5.5 Attribute values

Attributes are objects whose states represent attribute values.

Example: Temperature = 75 °C.

Attributes may specify measurement units.

---

## 8 OPM link syntax and semantics overview

## 8.1 Procedural link overview

### 8.1.1 Kinds of procedural links

Procedural links include:

* **Transforming link** — connects a process with a transformee object
* **Enabling link** — connects an enabler object with a process
* **Control link** — execution control mechanism

### 8.1.2 Procedural link uniqueness OPM principle

An object or state shall have exactly one role with respect to a process it links to.

### 8.1.3 State-specified procedural links

A procedural link may connect a process to a specified state of an object.

---

## 8.2 Operational semantics and flow of execution control

### 8.2.1 Event-Condition-Action control mechanism

Execution control is based on the Event-Condition-Action paradigm.

Process performance begins when:

1. an initiating event occurs
2. a precondition is satisfied

Events and conditions jointly specify flow of execution.

### 8.2.2 Preprocess object set and postprocess object set

Preprocess object set defines preconditions for process activation.

Typical elements:

* consumed objects
* affected objects
* enablers

Postprocess object set defines postconditions:

* resultees
* affected objects

---

## 9 Procedural links

## 9.1 Transforming links

### 9.1.1 Kinds of transforming links

Transforming links connect a process with the object it transforms.

Three types:

* consumption link
* result link
* effect link

[Figure: Three diagrams illustrating deleting (consumes file), creating (yields file), editing (affects file).]

### 9.1.2 Consumption link

A consumption link specifies that the process destroys or eliminates the linked object.

Syntax: **Processing consumes Consumee.**

### 9.1.3 Result link

A result link specifies that the process creates the linked object.

Syntax: **Processing yields Resultee.**

### 9.1.4 Effect link

An effect link specifies that the process changes the state of the object.

Syntax: **Processing affects Affectee.**

### 9.1.5 Basic transforming links summary

| Name             | Semantics                        | Sample OPD & OPL         | Source                              | Destination       |
| ---------------- | -------------------------------- | ------------------------ | ----------------------------------- | ----------------- |
| Consumption link | The process consumes the object  | Eating consumes Food     | consumed object                     | consuming process |
| Result link      | The process generates the object | Mining yields Copper     | creating process                    | created object    |
| Effect link      | The process affects the object   | Purifying affects Copper | affected object & affecting process | both              |

---

## 9.2 Enabling links

### 9.2.1 Kinds of enabling links

An enabling link specifies an enabler for a process.

Two kinds:

* agent link
* instrument link

### 9.2.2 Agent and Agent Link

An **agent** is a human or group capable of intelligent decision-making.

Agent link syntax:

**Agent handles Processing.**

[Figure: Agent link example showing Welder enabling Welding which consumes Steel Part A and Steel Part B and yields Steel Part AB.]

### 9.2.3 Instrument and Instrument Link

An **instrument** is an inanimate enabler necessary for a process.

Instrument link syntax:

**Processing requires Instrument.**

Example: Machine enabling transformation of Bar Stock to Machined Part.

---

[Figure: Instrument link example. A process named **Sintering** is shown as an oval. A rectangular object **Insert Set** contains two states: *pre-sintered* and *sintered*. Arrows connect the states to the process, indicating transformation from *pre-sintered* to *sintered*. Another rectangle labeled **Sintering Oven** connects to the process, representing an instrument required for the process.]

Insert Set can be **pre-sintered** or **sintered**.
**Sintering** requires **Sintering Oven**.
**Sintering** changes **Insert Set** from **pre-sintered** to **sintered**.

**Figure 9 — Instrument link example**

**EXAMPLE 3**
In the Figure 9 OPD, if during the **Sintering** process **Sintering Oven** ceases to exist, e.g. due to severe cracking, **Sintering** will stop and **Insert Set** will not be in its **sintered** state, although it already left its **pre-sintered** state.

---

### 9.2.4 Basic enabling links summary

Table 2 summarizes the basic enabling links.

### Table 2 — Basic enabling links summary

| Name                | Semantics                                                                                                                                     | Sample OPD & OPL                                                                                          | Source                           | Destination     |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------- |
| **Agent Link**      | Agent is a human or a group of humans who enables the occurrence of the process to which it is linked but is not transformed by that process. | [Diagram: Object **Welder** connected to process **Welding**.] **Welder handles Welding.**                | agent – the enabling object      | enabled process |
| **Instrument Link** | Instrument is an inanimate object that enables the occurrence of the process to which it is linked but is not transformed by that process.    | [Diagram: Object **Machine** connected to process **Manufacturing**.] **Manufacturing requires Machine.** | instrument – the enabling object | enabled process |

---

## 9.3 State-specified transforming links

### 9.3.1 State-specified consumption link

A state-specified consumption link shall be a consumption link from a specified state of the consumee to the linked process that consumes (destroys, eliminates) the object. Existence of the consumee in the specified state shall be a precondition, or part of the precondition, for process activation. If the consumee is not in that specified state, then process activation shall wait for the consumee to exist at that specified state.

Graphically, an arrow with a closed arrowhead pointing from the specified state of the object to the process, which consumes the object, shall denote the state-specified consumption link.

The syntax of a state-specified consumption link OPL sentence shall be: **Process consumes specified-state Object.**

The consumption shall be immediate upon process activation, unless the modeller needs to model consumption of the object over time. In this case, the consumption link shall have a property that indicates the rate of consumption of the consumee and the consumee shall have an attribute that indicates the available quantity.

**NOTE 1** The modeller can create an exception if the object quantity is less than the rate times the expected process duration.
**NOTE 2** See 11.1 for the denotation of link properties.

**EXAMPLE 1**
Steel Rod at state **pre-heat-treated** is a consumee for the process **Machining**, which generates the resultee **Shaft**. When **Machining** activates, it consumes **pre-heat-treated Steel Rod**, because this **pre-heat-treated Steel Rod** is not available for any purpose other than becoming a **Shaft** resultee of this process. If Steel Rod previously went through a **Heat Treating** process, it is at state **heat-treated**, and therefore not available to undergo **Machining**.

**EXAMPLE 2**
Continuing with Example 1, **Steel Rod** is at state **pre-heat-treated** and has an attribute **Quantity [units]** with value 600. The state-specified consumption link has a property **Rate [units/hour]** with value 60. When **Machining** performs, it consumes the 600 **Steel Rods** after 10 working hours.

---

### 9.3.2 State-specified result link

A state-specified result link shall be a result link from a process to a specified state of the resultee that the process creates (generates, yields). Existence of the resultee at the specified state shall be a postcondition, or part of the postcondition, upon completion of the generating process.

Graphically, an arrow with a closed arrowhead pointing from the process to the specified state of the object shall denote the state-specified result link.

The syntax of a state-specified result link OPL sentence shall be: **Process yields specified-state Object.**

The generation of the resultee at the particular state shall be immediate upon process completion, unless the modeller needs to model the generation of the object over time. In this case, the result link shall have a property that indicates its rate of resultee generation and the resultee shall have an attribute that indicates the available quantity at that specified state.

**NOTE 1** See 11.1 for the denotation of link properties.
**NOTE 2** At runtime, an operating model can consist of multiple operational instances of an object with each operational instance at a different state.

**EXAMPLE 1**
Steel Rod at state **pre-heat-treated** is a consumee for the process **Machining**, which generates the resultee **Shaft** at state **pre-heat-treated**. A state-specified result link from **Machining** to the **pre-heat-treated** state of **Shaft** denotes this model specification.

A result link yielding a stateful object with an initial state should attach at that object rectangle or one of its states other than the initial state.

**NOTE 3** The modeller might want the OPL on the right in Figure 10, but the OPL on the left reduces ambiguity.

---

[Figure: Two diagrams labeled P and object A with states s1, s2, s3. The left diagram connects process P to the object A as a whole. The right diagram connects process P to state s2 of object A. The caption explains that the left representation is correct and the right one incorrect when modeling a result link to an object with an initial state.]

**Figure 10 — Correct (left) and incorrect (right) result link to an object with an initial state**

---

### 9.3.3 State-specified effect links

#### 9.3.3.1 Input and output effect links

An input source link shall be the link from a specified state of an object, an input source, to the transforming process, while the output destination link shall be the link from the transforming process to a specified state of an object, an output destination. These links provide three possible modelling situations in the context of a single object linking to a single process:

a) input-output-specified effect link specifying both input source and output destination states;
b) input-specified effect link specifying only the input source state; and
c) output-specified effect link specifying only the output destination state.

---

#### 9.3.3.2 Input-output-specified effect link

An input-output-specified effect link shall be a pair of effect links, where the input source link connects to an affecting process from a specified state of an affectee, and the output destination link connects from that same process to a different output destination state of the same affectee. Existence of the affectee at the input source state shall be a precondition, or part of the precondition, for affecting process activation. Existence of the affectee at the output destination state shall be a postcondition, or part of the postcondition, upon affecting process completion.

Graphically, a pair of arrows consisting of an arrow with a closed arrowhead from the input source state of the affectee to the affecting process, the input source link, and a similar arrow from that process to the output destination state of the affectee at process completion, the output destination link, shall denote the input-output-specified effect link.

The syntax of an input-output-specified effect link OPL sentence shall be: **Process changes Object from input-state to output-state.**

**EXAMPLE 1**
The OPD in Figure 11 depicts state-specified consumption and result links. **Machining** can only consume **Raw Metal Bar** in state **cut** and generate **Part** in state **pre-tested**. **Cutting** and **Testing** are environmental processes. Cutting needs to precede Machining in order to change **Raw Metal Bar** from its **pre-cut** to its **cut** state, while Testing changes **Part** from **pre-tested** to **tested**.

**NOTE 1** In the case of an input-output-specified effect link, once an affecting process starts, it causes the object to exit out of its input source state. However, the object reaches its output destination state only when the process completes. Between process start and process completion, the affectee object is in transition between the two states.

---

[Figure: Process diagram involving objects Raw Metal Bar (states: pre-cut, cut), Part (states: pre-tested, tested), and processes Cutting, Machining, and Testing. Machine Operator and Coolant enable Machining. Cutting changes Raw Metal Bar from pre-cut to cut; Machining consumes cut Raw Metal Bar and yields pre-tested Part; Testing changes Part from pre-tested to tested.]

Raw Metal Bar is physical.
Raw Metal Bar can be **pre-cut** or **cut**.
Machine Operator is physical.
Coolant is physical.
Machining is physical.
Machining requires Coolant.
Machine Operator handles Machining.
Part is physical.
Part can be **pre-tested** or **tested**.
Testing is environmental and physical.
Cutting is environmental and physical.
Cutting changes Raw Metal Bar from **pre-cut** to **cut**.
Machining consumes **cut Raw Metal Bar**.
Machining yields **pre-tested Part**.
Testing changes Part from **pre-tested** to **tested**.

**Figure 11 — State-specified consumption and results links**

**NOTE 2**
If an active affecting process stops prematurely, i.e. it does not complete, the state of any affectee remains indeterminate unless exception handling resolves the object to one of its permissible states.

---

#### 9.3.3.3 Input-specified effect link

An input-specified effect link shall be a pair of effect links, where the input source link connects to an affecting process from an input source state of the affectee, and the output destination link connects from the same process to the same affectee without specifying a particular state. The output destination state of the object shall be its default state or, if the object does not have a default state, then the state probability distribution of the object shall determine the output destination state of that object.

Existence of the affectee at the input source state is a precondition for affecting process activation. Existence of the affectee at any of its states shall be a postcondition upon affecting process completion.

Graphically, a pair of arrows consisting of an arrow with a closed arrowhead from the input source state of the affectee to the affecting process, and a similar arrow from that process to the affectee but not to any one of its states shall denote the input-specified effect link.

The syntax of an input-specified effect link OPL sentence shall be: **Process changes Object from input-state.**

---

#### 9.3.3.4 Output-specified effect link

An output-specified effect link shall be a pair of effect links, where the input source link connects to an affecting process from an affectee without specifying a particular state, and the output destination link connects from the same process to an output destination state of the same affectee. Existence of the affectee shall be a precondition for affecting process activation. Existence of the affectee at the output destination state shall be a postcondition upon affecting process completion.

Graphically, a pair of arrows consisting of an arrow with a closed arrowhead from the affectee without specifying a particular state to the input link, and a similar arrow from that process to an output destination state of that affectee, the output link, shall denote the output-specified effect link.

The syntax of an input-specified effect link OPL sentence shall be: **Process changes Object to output-state.**

---

### 9.3.4 State-specified transforming links summary

Table 3 summarizes the state-specified transforming links.

### Table 3 — State-specified transforming links summary

| Name                                        | Semantics                                                                                                                       | Sample OPD & OPL                                    | Source                | Destination       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | --------------------- | ----------------- |
| **State-specified consumption link**        | The process consumes the object if and only if the object is in the specified state.                                            | Eating consumes edible Food.                        | consumee state        | process           |
| **State-specified result link**             | The process generates the object in the specified state.                                                                        | Mining yields raw Copper.                           | process               | resultee state    |
| **Input-output-specified effect link pair** | The process changes the object from a specified input state via the input link to a specified output state via the output link. | Purifying changes Copper from raw to pure.          | affectee source state | affecting process |
| **Input-specified effect link pair**        | The process changes the object from a specified input state to any output state.                                                | Testing changes Sample from awaiting test.          | affectee source state | affecting process |
| **Output-specified effect link pair**       | The process changes the object from any input state to a specified output state.                                                | Cleaning & Painting changes Engine Hood to painted. | affectee              | affecting process |

---

## 9.4 State-specified enabling links

### 9.4.1 State-specified agent link

A state-specified agent link shall be an agent link from a specified state of the agent to a process. The agent in the specified state shall be necessary for process activation and performance.

Graphically, a line with a filled circle resembling a black lollipop at the terminal end extending from the specified state of the agent object to the process it enables shall denote a state-specified agent link.

The syntax of a state-specified agent link OPL sentence shall be: **Specified-state Agent handles Processing.**

**NOTE** State name labels do not appear with beginning capital letters except when they appear at the beginning of an OPL sentence.

**EXAMPLE**
A **Pilot** needs to be **sober** in order to qualify as an agent for the **Flying** process of an **Airplane**.
In OPL: **Sober Pilot handles Flying.**

---

### 9.4.2 State-specified instrument link

A state-specified instrument link shall be an instrument link from a specified state of the instrument to a process. The instrument in the specified state shall be necessary for process activation and performance.

Graphically, a line with an empty circle resembling a white lollipop at the terminal end extending from the specified state of the instrument object to the process it enables shall denote a state-specified instrument link.

The syntax of a state-specified instrument link OPL sentence shall be: **Processing requires specified-state Instrument.**

**EXAMPLE**
The OPD in Figure 12 depicts the difference between basic and state-specified instrument links. On the left, the object **Moving Truck** is the instrument for **Moving**, meaning that the state of this object does not matter, while on the right, the qualifying state **serviced** of **Moving Truck** is an instrument of **Moving**, meaning that if and only if **Moving Truck** is serviced can **Moving** take place.

[Figure: Two diagrams comparing instrument link types. Left diagram: Moving Truck object with states worn out and serviced connects to process Moving regardless of state. Right diagram: Moving Truck connects only through the state serviced, indicating that the process requires that specific state.]

Moving Truck is physical.
Moving Truck can be **worn out** or **serviced**.
Servicing is environmental and physical.
Servicing changes Moving Truck from **worn out** to **serviced**.
Apartment Content Location is physical.
Apartment Content Location can be **old apartment** or **new apartment**.
Moving is physical.
Moving requires **serviced Moving Truck**.
Moving changes Apartment Content Location from **old apartment** to **new apartment**.

**Figure 12 — Instrument link on left vs. state-specified instrument link on right**

---

### 9.4.3 State-specified enabling links summary

Table 4 summarizes the state-specified enabling links.

### Table 4 — State-specified enabling links summary

| Name                                | Semantics                                                                   | Sample OPD & OPL                          | Source           | Destination     |
| ----------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------- | ---------------- | --------------- |
| **State-specified agent link**      | The human agent enables the process provided she is at the specified state. | Healthy Miner handles Copper Mining.      | agent state      | enabled process |
| **State-specified instrument link** | The process requires the instrument at the specified state.                 | Copper Mining requires operational Drill. | instrument state | enabled process |

---

## 9.5 Control links

### 9.5.1 Kinds of control links

As part of the Event-Condition-Action paradigm underlying the operational semantics of OPM, an event link, a condition link, and an exception link shall express an event, a condition, and a time exception respectively. These three link kinds shall be control links. Control links shall occur either between an object and a process or between two processes.

An event link shall specify a source event and a destination process to activate upon event occurrence. The event occurrence causes an evaluation of the process precondition for satisfaction.

Satisfying the precondition allows process performance to proceed and the process becomes active. If the process precondition is not satisfied, then process performance shall not occur. Regardless of whether the evaluation is successful or not, the event shall be lost.

If the process precondition is not satisfied, process activation shall not occur until another event activates the process. Control links determine if the process waits for another activating event or if the flow of execution control bypasses the process.

**NOTE 1** Subsequent events can come from other sources to initiate precondition evaluation.

A condition link shall be a procedural link between a source object or object state and a destination process. A condition link shall provide a bypass mechanism, which enables system execution control to skip, or bypass, the destination process if its precondition satisfaction evaluation fails.

**NOTE 2** Without the condition link bypass mechanism, the failure to satisfy the precondition constrains the process to wait for satisfaction of the precondition.

For both event links and condition links, each kind of incoming transforming link and enabling link, i.e. a link from an object or object state to a process, shall have a corresponding kind of event link and condition link.

An exception link shall be a procedural link between a process that for some reason is unable to complete successfully or takes more or less time to complete than expected, and a process that is to manage the exception situation.

**NOTE 3** Since failure to complete successfully often results in undertime or overtime performance, exception links can serve other situations. In addition, all non-time related exceptions can be modelled using value ranges.

Graphically, a control modifier appearing as an annotation next to an incoming transforming link or enabling link, i.e. a link from an object or an object state to a process, shall denote the corresponding control link. The symbol “e” annotation, signifying event, shall denote an event link and the symbol “c” annotation, signifying condition, shall denote a condition link.

---

### 9.5.2 Event links

#### 9.5.2.1 Transforming event links

##### 9.5.2.1.1 Consumption event link

A consumption event link shall be an annotated consumption link between an object and a process, which an operational instance of the object initiates. Satisfaction of the process precondition and the subsequent process performance shall consume the instance of the initiating object.

Graphically, an arrow with a closed arrowhead pointing from the object to the process with the small letter “e” annotation near the arrowhead, signifying event, shall denote the consumption event link.

The syntax of a consumption event link OPL sentence shall be: **Object initiates Process, which consumes Object.**

---

##### 9.5.2.1.2 Effect event link

An effect event link shall be an annotated portion of an effect link from an object to a process, which an operational instance of the object initiates. Satisfaction of the process precondition and the subsequent process performance shall affect the initiating object in some manner.

Graphically, a bidirectional arrow with closed arrowheads at each end between the object and the process with a small letter “e” annotation near the process end of the arrow, signifying event, shall denote the effect event link.

The syntax of an effect event link OPL sentence shall be: **Object initiates Process, which affects Object.**

---

##### 9.5.2.1.3 Transforming event links summary

Table 5 summarizes the transforming event links.

### Table 5 — Transforming event links summary

| Name                       | Semantics                                                                   | Sample OPD & OPL                                  | Source              | Destination       |
| -------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------- | ------------------- | ----------------- |
| **Consumption event link** | The object initiates the process, which, if performed, consumes the object. | Food initiates Eating, which consumes Food.       | initiating consumee | initiated process |
| **Effect event link**      | The object initiates the process, which, if performed, affects the object.  | Copper initiates Purifying, which affects Copper. | initiating affectee | initiated process |

**NOTE** The event link is the link from the object to the process; the link from the process to the object is not an event link.

---

#### 9.5.2.2 Enabling event links

##### 9.5.2.2.1 Agent event link

An agent event link shall be an annotated enabling link from an agent object to the process that it initiates and enables.

Graphically, a line with a filled circle resembling a black lollipop at the terminal end extending from an agent object to the process it initiates and enables with a small letter “e” annotation near the process end, signifying event, shall denote an agent event link.

The syntax of an agent event link OPL sentence shall be: **Agent initiates and handles Process.**

---

##### 9.5.2.2.2 Instrument event link

An instrument event link shall be an annotated enabling link from an instrument object to the process that it initiates and enables.

Graphically, a line with an empty circle resembling a white lollipop at the terminal end extending from the instrument object to the process it initiates and enables with a small letter “e” annotation near the process end, signifying event, shall denote an instrument event link.

The syntax of an instrument event link OPL sentence shall be: **Instrument initiates Process, which requires Instrument.**

---

##### 9.5.2.2.3 Enabling event links summary

Table 6 summarizes the enabling event links.

### Table 6 — Enabling event links summary

| Name                      | Semantics                                                                                                                        | Sample OPD & OPL                                     | Source                | Destination       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------- | ----------------- |
| **Agent event link**      | The agent—a human—both initiates and enables the process. The agent needs to exist throughout the process duration.              | Miner initiates and handles Copper Mining.           | initiating agent      | initiated process |
| **Instrument event link** | The object initiates the process as an instrument, so it does not change, but it needs to exist throughout the process duration. | Drill initiates Copper Mining, which requires Drill. | initiating instrument | initiated process |

---

#### 9.5.2.3 State-specified transforming event links

##### 9.5.2.3.1 State-specified consumption event link

A state-specified consumption event link shall be an annotated consumption link from a specified state of an object to a process, which an operational instance of the object initiates. Satisfaction of the process precondition, including the initiating object at the specified state, and the subsequent process performance shall consume the initiating object.

Graphically, an arrow with a closed arrowhead pointing from the specified state of the object to the process with the small letter “e” annotation near the arrowhead, signifying event, shall denote the state-specified consumption event link.

The syntax of a state-specified consumption event link OPL sentence shall be: **Specified-state Object initiates Process, which consumes Object.**

##### 9.5.2.3.2 Input-output-specified effect event link

An input-output-specified effect event link shall be an annotated input-output-specified effect link that initiates the affecting process when an operational instance of the object enters the specified input source state.

Graphically, the input-output-specified effect link with a small letter “e” annotation near the arrowhead end of the input link, signifying event, shall denote the input-output-specified effect event link.

The syntax of an input-output-specified effect event link OPL sentence shall be: **Input-state Object initiates Process**, which changes **Object from input-state to output-state**.

---

##### 9.5.2.3.3 Input-specified effect event link

An input-specified effect event link shall be an annotated input-specified effect link that initiates the affecting process when an operational instance of the object enters the specified input source state.

Graphically, the input-specified effect link with a small letter “e” annotation at the arrowhead end of the input link, signifying event, shall denote the input-specified effect event link.

The syntax of an input-specified effect event link OPL sentence shall be: **Input-state Object initiates Process**, which changes **Object from input-state**.

---

##### 9.5.2.3.4 Output-specified effect event link

An output-specified effect event link shall be an annotated output-specified effect link that initiates the affecting process when an operational instance of the object comes into existence.

Graphically, the output-specified effect link with a small letter “e” annotation at the arrowhead end of the input link, signifying event, shall denote the output-specified effect event link.

The syntax of an output-specified effect event link OPL sentence shall be: **Object in any state initiates Process**, which changes **Object to destination-state**.

---

##### 9.5.2.3.5 State-specified transforming event links summary

Table 7 summarizes the state-specified transforming event links.

---

## Table 7 — State-specified transforming event links summary

| Name                                       | Semantics                                                                                                       | Sample OPD & OPL                                                                                                                                                                                                                    | Source                | Destination                                    |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------------- |
| **State-specified consumption event link** | The object in the specified state both initiates the process and is consumed by it.                             | [Diagram: Object **Food** with states *non-edible* and *edible*. The state **edible** connects to process **Eating** via an event link.] **Edible Food initiates Eating, which consumes Food.**                                     | consumee state        | initiated process                              |
| **Input-output specified event link pair** | The object in the specified state both initiates the process and is transformed by it to the output state.      | [Diagram: Object **Copper** with states *raw* and *pure*. State **raw** connects to process **Purifying**, which outputs state **pure**.] **Raw Copper initiates Purifying, which changes Copper from raw to pure.**                | affectee source state | initiates process / affectee destination state |
| **Input-specified effect link pair**       | The object in the specified state both initiates the process and is transformed by it to any one of its states. | [Diagram: Object **Sample** with states *awaiting test*, *passed test*, *failed test*. State **awaiting test** initiates process **Testing**.] **Awaiting test Sample initiates Testing, which changes Sample from awaiting test.** | affectee source state | initiated process / affectee                   |
| **Output-specified event link pair**       | The object (in any one of its states) both initiates the process and is transformed by it to the output state.  | [Diagram: Object **Engine Hood** with states *rusty*, *oily*, *painted*. Process **Cleaning & Painting** transforms the hood to **painted**.] **Engine Hood initiates Cleaning & Painting, which changes Engine Hood to painted.**  | affectee              | initiates process / affectee destination state |

---

#### 9.5.2.4 State-specified enabling event links

##### 9.5.2.4.1 State-specified agent event link

A state-specified agent event link shall be an annotated state-specified agent link that initiates the process when an operational instance of the agent enters the specified state.

Graphically, the state-specified agent link with a small letter “e” annotation near the process end of the link, signifying event, shall denote the state-specified agent event link.

The syntax of a state-specified agent event link OPL sentence shall be: **Specified-state Agent initiates and handles Processing.**

---

##### 9.5.2.4.2 State-specified instrument event link

A state-specified instrument event link shall be an annotated state-specified instrument link that initiates the process when an operational instance of the instrument enters the specified state.

Graphically, the state-specified instrument link with a small letter “e” annotation near the process end of the link, signifying event, shall denote the state-specified instrument event link.

The syntax of a state-specified instrument event link OPL sentence shall be: **Specified-state Instrument initiates Processing**, which requires **specified-state Instrument**.

---

##### 9.5.2.4.3 State-specified enabling event links summary

Table 8 summarizes the state-specified enabling event links.

---

## Table 8 — State-specified enabling event links summary

| Name                                      | Semantics                                                                                                                                                                              | Sample OPD & OPL                                                                                                                                                                                                      | Source           | Destination       |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| **State-specified agent event link**      | The human agent in the specified state both initiates the process and acts as its agent. The agent needs to be at the specified state throughout the process duration.                 | [Diagram: Agent **Miner** with states *sick* and *healthy*. State **healthy** connects to process **Copper Mining**.] **Healthy Miner initiates and handles Copper Mining.**                                          | agent state      | initiated process |
| **State-specified instrument event link** | The object at the specified state both initiates the process and is instrument for its performance. The instrument needs to be at the specified state throughout the process duration. | [Diagram: Instrument **Drill** with states *faulty* and *operational*. State **operational** connects to process **Copper Mining**.] **Operational Drill initiates Copper Mining, which requires operational Drill.** | instrument state | initiated process |

---

#### 9.5.2.5 Invocation links

##### 9.5.2.5.1 Process invocation and invocation link

Process invocation shall be an event by which a process initiates a process. An invocation link shall be a link from a source process to the destination process that it invokes (initiates), signifying that when the source process completes, it immediately initiates the destination process at the other end of the invocation link.

**NOTE 1**
A normal or expected flow of execution control does not invoke a new process if the prior process does not complete successfully. It is up to the modeler to take care of any process that aborts. Clause C.6 provides several ways to manage termination of a process because of a failure, especially C.6.8.

**NOTE 2**
Since an OPM process performs a transformation, the invocation link semantically implies the creation of an interim object by the invoking source process that the subsequent invoked destination process immediately consumes. In an OPM model, an invocation link can replace a transient, short-lived physical or informational object (such as **Record ID** in a query), that a source process creates to initiate the destination process, which immediately consumes the transient object.

Graphically, a lightning symbol jagged line from the invoking source process to the invoked destination process ending with a closed arrowhead at the invoked process shall denote an invocation link.

The syntax of an invocation link OPL sentence shall be: **Invoking-process invokes invoked-process.**

---

##### 9.5.2.5.2 Self-invocation link

Self-invocation shall be invocation of a process by itself such that upon process completion, the process immediately invokes itself. The self-invocation link shall specify self-invocation.

Graphically, a pair of invocation links, originating at the process and joining head to tail before ending back at the original process shall denote the self-invocation link.

The syntax of a self-invocation link OPL sentence shall be: **Invoking-process invokes itself.**

---

##### 9.5.2.5.3 Invocation links summary

Table 9 summarizes the invocation links.

---

## Table 9 — Invocation links summary

| Name                     | Semantics                                                                                       | Sample OPD & OPL                                                                                                                                              | Source             | Destination               |
| ------------------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------- |
| **Invocation link**      | As soon as the invoking process ends, it invokes the process pointed to by the invocation link. | [Diagram: Process **Product Finishing** connected by a lightning-style link to process **Product Shipping**.] **Product Finishing invokes Product Shipping.** | Initiating process | Another initiated process |
| **Self-invocation link** | Upon process completion, it immediately invokes itself.                                         | [Diagram: Process **Recurrent Processing** connected to itself by invocation arrows.] **Recurrent Processing invokes itself.**                                | Initiating process | The same process          |

---

### 9.5.3 Condition links

#### 9.5.3.1 Basic Condition transforming links

##### 9.5.3.1.1 Condition consumption link

A condition consumption link shall be an annotated consumption link from a consumee to a process. If a consumee operational instance exists when an event initiates the process, then the presence of that consumee operational instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and consumes that consumee instance. However, if a consumee operational instance does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, an arrow with a closed arrowhead pointing from the consumee to the process with the small letter “c” annotation near the arrowhead, signifying condition, shall denote a condition consumption link.

The syntax of the condition consumption link OPL sentence shall be: **Process occurs if Object exists**, in which case **Object is consumed**, otherwise **Process is skipped**.

An alternate syntax of the condition consumption link OPL sentence shall be: **If Object exists then Process occurs and consumes Object**, otherwise bypass **Process**.

---

##### 9.5.3.1.2 Condition effect link

A condition effect link shall be an annotated effect link from an affectee to a process. If an affectee object operational instance exists when an event initiates the process, then the presence of that affectee instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and affects that affectee instance. However, if an affectee operational instance does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, a bidirectional arrow with two closed arrowheads, one pointing in each direction between the affectee and the affecting process, with the small letter “c” annotation near the process end of the arrow, signifying condition, shall denote a condition effect link.

The syntax of the condition effect link OPL sentence shall be: **Process occurs if Object exists**, in which case **Process affects Object**, otherwise **Process is skipped**.

An alternate syntax of the condition effect link OPL sentence shall be: **If Object exists then Process occurs and affects Object**, otherwise bypass **Process**.

---

##### 9.5.3.1.3 Condition transforming links summary

Table 10 summarizes the condition transforming links.

---

## Table 10 — Condition transforming links summary

| Name                           | Semantics                                                                                                                                                                                                                      | Sample OPD & OPL                                                                                                                                                                     | Source              | Destination         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------------- |
| **Condition consumption link** | If an object operational instance exists and the rest of the process precondition is satisfied, then the process performs and consumes the object instance, otherwise execution control advances to initiate the next process. | [Diagram: Object **Object** connected to **Process** with condition link.] **Process occurs if Object exists, in which case Process consumes Object, otherwise Process is skipped.** | Conditioning object | Conditioned process |
| **Condition effect link**      | If an object operational instance exists and the rest of the process precondition is satisfied, then the process performs and affects the object instance, otherwise execution control advances to initiate the next process.  | [Diagram: Object **Object** bidirectionally connected to **Process**.] **Process occurs if Object exists, in which case Process affects Object, otherwise Process is skipped.**      | Conditioning object | Conditioned process |

---

#### 9.5.3.2 Basic condition enabling links

##### 9.5.3.2.1 Condition agent link

A condition agent link shall be an annotated agent link from an agent to a process. If an agent operational instance exists when an event initiates the process, then the presence of that agent instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and that agent handles its performance. However, if an agent operational instance does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, a line with a filled circle resembling a black lollipop at the terminal end extending from an agent object to the process it enables, with the small letter “c” annotation near the process end, signifying condition, shall denote a condition agent link.

The syntax of the condition agent link OPL sentence shall be: **Agent handles Process if Agent exists**, else **Process is skipped**.

An alternate syntax for the condition agent link OPL sentence shall be: **If Agent exists then Agent handles Process**, otherwise bypass **Process**.

---

##### 9.5.3.2.2 Condition instrument link

A condition instrument link shall be an annotated instrument link from an instrument to a process. If an instrument operational instance exists when an event initiates the process, then the presence of that instrument instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts. However, if an instrument operational instance does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, a line with an empty circle resembling a white lollipop at the terminal end, extending from an instrument object to the process it enables, with the small letter “c” annotation near the process end, signifying condition, shall denote a condition instrument link.

The syntax of the condition instrument link OPL sentence shall be: **Process occurs if Instrument exists**, else **Process is skipped**.

An alternate syntax for the condition instrument link OPL sentence shall be: **If Instrument exists then Process occurs**, otherwise bypass **Process**.

---

[Figure: Example OPD diagram illustrating a condition instrument link. The central process is **Cellular Network Signal Amplifying**. It receives enabling links from several objects including **Signal Booster**, **User**, **Calling Mobile Device**, and **Cellular Network Signal**. A condition instrument link labeled “c” connects **Nearby Mobile Device** to the process, indicating that amplification occurs only if a nearby mobile device exists.]

**Cellular Network Signal Amplifying occurs if Nearby Mobile Device exists, otherwise Cellular Network Signal Amplifying is skipped.**

---

##### 9.5.3.2.3 Basic condition enabling links summary

Table 11 summarizes the basic condition enabling links.

---

## Table 11 — Basic condition enabling links summary

| Name                          | Semantics                                                                                | Sample OPD & OPL                                                                                                                                                                                  | Source                  | Destination         |
| ----------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------- |
| **Agent condition link**      | The agent enables the process if the agent is present, otherwise the process is skipped. | [Diagram: Agent **Engineer** connected to process **Part Designing** with condition annotation.] **Engineer handles Part Designing if Engineer is present, otherwise Part Designing is skipped.** | Conditioning agent      | Conditioned process |
| **Instrument condition link** | The instrument enables the process if it exists, otherwise the process is skipped.       | [Diagram: Instrument **LASER Meter** connected to process **Precise Measuring**.] **Precise Measuring occurs if LASER Meter exists, otherwise Precise Measuring is skipped.**                     | Conditioning instrument | Conditioned process |

---

#### 9.5.3.3 Condition state-specified transforming links

##### 9.5.3.3.1 Condition state-specified consumption link

A condition state-specified consumption link shall be an annotated condition consumption link from a specified state of a consumee to a process. If an operational instance of the consumee at the specified state exists when an event initiates the process, then the presence of that consumee instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and consumes that consumee instance. However, if an operational instance of a consumee in the specified state does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, an arrow with a closed arrowhead pointing from the specified state of the consumee to the process with the small letter “c” annotation near the arrowhead, signifying condition, shall denote a condition state-specified consumption link.

The syntax of the condition state-specified consumption link OPL sentence shall be: **Process occurs if Object is specified-state**, in which case **Object is consumed**, otherwise **Process is skipped**.

An alternate syntax for the condition state-specified consumption link OPL sentence shall be: **If specified-state Object exists then Process occurs and consumes Object**, otherwise bypass **Process**.

---

##### 9.5.3.3.2 Condition input-output-specified effect link

A condition input-output-specified effect link shall be an annotated input-output-specified effect link from a source input state to a process. If an operational instance of the affectee at the specified state exists when an event initiates the process, then the presence of that affectee instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and affects that object operational instance by changing the state of the instance from the specified input state to the specified output state. However, if an operational instance of an affectee at the specified state does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, the condition input-output-specified effect link with the small letter “c” annotation near the arrowhead of the input link, signifying condition, shall denote a condition input-output-specified effect link.

The syntax of the condition input-output-specified effect link OPL sentence shall be: **Process occurs if Object is input-state**, in which case **Process changes Object from input-state to output-state**, otherwise **Process is skipped**.

An alternate syntax for the condition input-output-specified effect link OPL sentence shall be: **If input-state Object then Process changes Object from input-state to output-state**, otherwise bypass **Process**.

---

##### 9.5.3.3.3 Condition input-specified effect link

A condition input-specified effect link shall be an annotated input-specified effect link from a source input state to a process. If an operational instance of the affectee at the specified state exists when an event initiates the process, then the presence of that affectee instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and affects that object instance by changing the state of the instance from the specified input state to a destination state. The destination state shall be either its default state or, if the object does not have a default state, the state probability distribution of the object shall determine the output destination state of that object (see 12.7). However, if an operational instance of an affectee at the specified state does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, the condition input-specified effect link with the small letter “c” annotation near the arrowhead of the input link, signifying condition, shall denote the condition input-specified effect link.

The syntax of a condition input-specified effect link OPL sentence shall be: **Process occurs if Object is input-state**, in which case **Process changes Object from input-state**, otherwise **Process is skipped**.

An alternate syntax for a condition input-specified effect link OPL sentence shall be: **If input-state Object then Process changes Object from input-state**, otherwise bypass **Process**.

---

##### 9.5.3.3.4 Condition output-specified effect link

A condition output-specified effect link shall be an annotated output-specified effect link from a source object to a process. If an operational instance of the affectee exists when an event initiates the process, then the presence of that affectee instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and affects that object instance by changing the state of the instance to the specified output-state. However, if an operational instance of an affectee does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, the condition output-specified effect link with the small letter “c” annotation near the arrowhead of the input link, signifying condition, shall denote a condition output-specified effect link.

The syntax of the condition output-specified effect link OPL sentence shall be: **Process occurs if Object exists**, in which case **Process changes Object to output-state**, otherwise **Process is skipped**.

An alternate syntax for the condition output-specified effect link OPL sentence shall be: **If Object exists then Process changes Object to output-state**, otherwise bypass **Process**.

---

##### 9.5.3.3.5 Condition state-specified transforming links summary

Table 12 summarizes the condition state-specified transforming links.

---

## Table 12 — Condition state-specified transforming links summary

| Name                                             | Semantics                                                                                                                                                                                         | Sample OPD & OPL                                                                                                                                                                                                                                                                                         | Source                                           | Destination         |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------- |
| **Condition state-specified consumption link**   | The process performs if the object is in the state from which the link originates, otherwise the process is skipped.                                                                              | [Diagram: Object **Raw Material Sample** with states *pre-approved* and *approved*. State **pre-approved** connects to process **Testing**.] **Testing occurs if Raw Material Sample is pre-approved, in which case Raw Material Sample is consumed, otherwise Testing is skipped.**                     | conditioning specified state of the object       | conditioned process |
| **Condition input-output-specified effect link** | The process performs if the object is in the input state (from which the link originates) and changes the object from its input state to its output state, otherwise the process is skipped.      | [Diagram: Object **Raw Material** with states *pre-tested* and *tested*. State **pre-tested** triggers process **Testing** leading to **tested**.] **Testing occurs if Raw Material is pre-tested, in which case Testing changes Raw Material from pre-tested to tested, otherwise Testing is skipped.** | conditioning specified input state of the object | conditioned process |
| **Condition input-specified effect link**        | The process performs if the object is in the input state (from which the link originates) and changes the object from its input state to any one of its states, otherwise the process is skipped. | [Diagram: Object **Message** with states *created* and *delivered*. State **created** triggers process **Delivery Attempting**.] **Delivery Attempting occurs if Message is created, in which case Delivery Attempting changes Message from created, otherwise Delivery Attempting is skipped.**         | conditioning specified input state of the object | conditioned process |

## Table 12 (continued)

| Name                                   | Semantics                                                                                                                                    | Sample OPD & OPL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Source              | Destination         |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- |
| Condition output-specified effect link | The process performs if the object exists and changes the object from its input state to its output state, otherwise the process is skipped. | [Figure: A diagram showing an object **Suspicious Component** with possible states **pre-tested**, **tested**, and **stress-tested**. A process **Stress Testing** is connected to the object via a link annotated with the letter **c** indicating a condition. The diagram illustrates that the process occurs only if the object exists in a relevant state and changes the state to **stress-tested**.]<br><br>**Stress Testing occurs if Suspicious Component exists, in which case Stress Testing changes Suspicious Component to stress-tested, otherwise Stress Testing is skipped.** | conditioning object | conditioned process |

---

#### 9.5.3.4 Condition state-specified enabling links

##### 9.5.3.4.1 Condition state-specified agent link

A condition state-specified agent link shall be an annotated state-specified agent link from a specified state of an agent to a process. If an operational instance of the agent at the specified state exists when an event initiates the process, then the presence of that agent instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts and that agent handles operation. However, if an operational instance of an agent in the specified state does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, the state-specified agent link with a small letter **“c”** annotation near the process end, signifying condition, shall denote a condition state-specified agent link.

The syntax of the condition state-specified agent link OPL sentence shall be:

**Agent handles Process if Agent is specified-state, else Process is skipped.**

An alternate syntax for the condition state-specified agent link OPL sentence shall be:

**If specified-state Agent exists then Agent handles Process, otherwise bypass Process.**

---

##### 9.5.3.4.2 Condition state-specified instrument link

A condition state-specified instrument link shall be an annotated state-specified instrument link from a specified state of an instrument to a process. If an operational instance of the instrument at the specified state exists when an event initiates the process, then the presence of that instrument instance satisfies the process precondition with respect to that object. If evaluation of the entire preprocess object set satisfies the precondition, the process starts. However, if an operational instance of an instrument in the specified state does not exist when an event initiates the process, then the process precondition evaluation fails and the flow of execution control bypasses, or ‘skips’, the process without process performance.

Graphically, the state-specified instrument link with a small letter **“c”** annotation near the process end, signifying condition, shall denote a condition state-specified instrument link.

The syntax of the condition state-specified instrument link OPL sentence shall be:

**Process occurs if Instrument is specified-state, otherwise Process is skipped.**

An alternate syntax for the condition state-specified instrument link OPL sentence shall be:

**If specified-state Instrument then Process occurs, otherwise bypass Process.**

---

#### 9.5.3.3 Condition state-specified enabling links summary

**Table 13 summarizes the condition state-specified enabling links.**

## Table 13 — Condition state-specified enabling links summary

| Name                                      | Semantics                                                                                               | Sample OPD & OPL                                                                                                                                                                                                                                                                                                                                                                                                                  | Source                                     | Destination         |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------- |
| State-specified agent condition link      | The agent enables the process if the agent is in the specified state, otherwise the process is skipped. | [Figure: A diagram showing an **Engineer** object with states **safety design authorized** and **safety design unauthorized**. The process **Critical Part Designing** is connected with a conditional annotation **c** indicating that the engineer must be in the authorized state.]<br><br>**Engineer handles Critical Part Designing if Engineer is safety design authorized, otherwise Critical Part Designing is skipped.** | conditioning specified state of agent      | conditioned process |
| State-specified instrument condition link | The instrument enables the process if it is in the specified state, otherwise the process is skipped.   | [Figure: A diagram showing a **LASER Meter** object with states **periodically calibrated** and **manufacturer calibrated**. A process **Ultra-Precision Measuring** occurs only if the meter is in a specific state.]<br><br>**Ultra-Precision Measuring occurs if LASER Meter is periodically calibrated, otherwise Precise Measuring is skipped.**                                                                             | conditioning specified state of instrument | conditioned process |

---

### 9.5.4 Exception links

#### 9.5.4.1 Minimal, Expected, and Maximal Process Duration and Duration Distribution

A process may have a **Duration** attribute with a value that expresses units of time. **Duration** may specialize into **Minimal Duration**, **Expected Duration**, and **Maximal Duration**.

**Minimal Duration** and **Maximal Duration** should designate the minimum and maximum allowable time units for process completion. **Expected Duration** of a process should be the statistical mean of the duration of that process.

Duration may have an optional **Duration Distribution** property with a value identifying the name and parameters for a probability distribution function associated with the process duration. At run-time, the value of **Duration** is determined separately for each process instance (i.e. for each individual process occurrence) by sampling from the process **Duration Distribution**.

**NOTE**
See Annex D for process duration and system time run-time discussion and examples.

---

#### 9.5.4.2 Overtime exception link

The overtime exception link shall connect the source process with an overtime handling destination process to specify that if at runtime, performance of the source process instance exceeds its **Maximal Duration** value, then an event initiates the destination process.

Graphically, a single short bar, oblique to the line connecting the source and destination processes and next to the destination process, shall denote the overtime exception link.

Given that **max-duration** is the value of **Maximal Duration**, and **time-unit** is an allowable time measurement unit, the syntax of the overtime exception link shall be:

**Overtime Handling Destination Process occurs if duration of Source Process exceeds max-duration time-units.**

---

#### 9.5.4.3 Undertime exception link

The undertime exception link shall connect the source process with an undertime handling destination process to specify that if at runtime, performance of the source process instance takes less than its **Minimal Duration** value, then an event initiates the destination process.

Graphically, two parallel short bars, oblique to the line connecting the source and destination processes and next to the destination process, shall denote the undertime exception link.

Given that **min-duration** is the value of **Minimal Duration**, and **time-unit** is an allowable time measurement unit, the syntax of the undertime exception link shall be:

**Undertime Handling Destination Process occurs if duration of Source Process falls short of min-duration time-units.**

**NOTE**

Similar to the invocation link, the two time exception links are procedural links that connect two processes directly, unlike most procedural links, which connect an object and a process. There is, in fact, an interim object **Overtime Exception Message** or an **Undertime Exception Message** created by the OPM’s process execution mechanism realizing the process failed to end by the maximal allotted time or ended prematurely, falling short of the minimal allotted time, respectively. Since the OPM operational mechanism creates and immediately consumes these objects, their depiction is not necessary in the model.

---

## 10 Structural links

## 10.1 Kinds of structural links

Structural links specify static, time-independent, long-lasting relations in the system. A structural link shall connect two or more objects or two or more processes, but not an object and a process, except in the case of an exhibition-characterization link (see **10.3.3**). The two kinds of structural links shall be tagged structural links and fundamental structural links of aggregation-participation, exhibition-characterization, generalization-specialization, and classification-instantiation.

---

## 10.2 Tagged structural link

### 10.2.1 Unidirectional tagged structural link

A unidirectional tagged structural link shall have a user-defined semantics regarding the nature of the relation from one thing to the other thing. A meaningful tag, in the form of a textual phrase, shall express the nature of the structural relation between the connecting objects or connecting processes. The tag should convey that meaning when placed in the OPL sentence.

Graphically, an arrow with an open arrowhead and a tag annotation near the shaft shall denote a unidirectional tagged structural link.

The syntax of the unidirectional tagged structural link OPL sentence shall be:

**Source-thing tag Destination-thing.**

**NOTE**

Since the tag is a label added to the model by the modeller, in the OPL sentence the tag phrase appears in bold to distinguish it from other words implicit in the syntactic construction.

---

### 10.2.2 Unidirectional null-tagged structural link

A unidirectional null-tagged structural link shall be a unidirectional tagged structural link with no tag annotation, signifying the use of the default unidirectional tag. The default tag shall be **“relates to”**.

The syntax of the unidirectional null-tagged structural link OPL sentence shall be:

**Source-thing relates to Destination-thing.**

**NOTE**

The modeller can have the option of setting the default unidirectional tag, which does not appear in bold letters, for a specific system or a set of systems.

---

### 10.2.3 Bidirectional tagged structural link

Because relations between things are bidirectional, every tagged structural link has a corresponding tagged structural link in the opposite direction. When the tags in both directions are meaningful and not just the inverse of each other, they may be annotated by two tags on either side of a single bidirectional tagged structural link.

Graphically, a line with harpoon shaped arrowheads on opposite sides at both ends of the link shall denote a bidirectional tagged structural link. Each tag shall align on the side of the arrow with the harpoon edge sticking out of the arrowhead, unambiguously determining the direction in which each relation applies.

The syntax of the resulting tagged structural link shall be two separate unidirectional tagged structural link OPL sentences, one for each direction.

[Figure: Diagram with objects **Airport**, **Highway**, **City**, and **Underwater Tunnel** connected with tagged relations such as *serves*, *surrounds*, *passes through*, and *enables traffic flow*.]

Airport serves City.
Highway surrounds City.
Highway passes through Underwater Tunnel.
Underwater Tunnel enables traffic flow in Highway.

---

### 10.2.4 Reciprocal tagged structural link

A reciprocal tagged structural link shall be a bidirectional tagged structural link with only one tag or no tag. In either case, reciprocity shall indicate that the tag of a bidirectional structural link has the same semantics for each direction of the relation. When no tag appears, the default tag shall be **“are related”.**

The syntax of the reciprocal tagged structural link with only one tag shall be:

**Source-thing and Destination-thing are reciprocity-tag.**

The syntax of the reciprocal tagged structural link with no tag shall be:

**Source-thing and Destination-thing are related.**

[Figure: Diagram showing **Engine** and **Gearbox** connected with reciprocal relation “attached”.]

Engine is attached to Gearbox.
Gearbox is attached to Engine.

Equivalent reciprocal expression:

Engine and Gearbox are attached.

---

## 10.3 Fundamental structural relations

### 10.3.1 Kinds of fundamental structural relations

The fundamental structural relations are the most prevalent structural relations among OPM things and are of particular significance for specifying and understanding systems. Each of the fundamental relations shall elaborate or refine one source thing, the refineable, into a collection of one or more destination things, the refinees.

The fundamental structural relations shall be:

* Aggregation-participation, which designates the relation between a whole and its parts;
* Exhibition-characterization, which designates the relation between an exhibitor, a thing exhibiting one or more features (attributes and/or operations), and the things that characterize the exhibitor;
* Generalization-specialization, which designates the relation between a general thing and its specializations; and
* Classification-instantiation, which designates the relation between a class of things and a refinee instance of that class.

Aggregation, exhibition, generalization, and classification shall be the refinement relation identifiers, i.e., the identifiers associated with the relation as seen from the perspective of the refineable. Participation, characterization, specialization, and instantiation shall be the corresponding complementary relation identifiers, i.e., the relation identifiers as seen from the perspective of their refinees.

With the exception of exhibition-characterization, the refinee destination things shall all have the same **Perseverance** value as the refineable source thing, i.e. either all are objects with static Perseverance or all are processes with dynamic Perseverance.

---

### 10.3.2 Aggregation-participation relation link

The fundamental structural relation aggregation-participation shall mean that a refineable, the whole, aggregates one or more refinees, the parts.

[Figure: Diagram where **Resource Description Framework Statement** is composed of three parts: **Subject**, **Predicate**, and **Object**.]

**Resource Description Framework Statement consists of Subject, Predicate and Object.**

Graphically, a black solid (filled in) triangle with its apex connecting by a line to the whole and the parts connecting by lines to the opposite horizontal base shall denote the aggregation-participation relation link.

The syntax of the aggregation-participation relation link shall be:

**Whole-thing consists of Part-thing₁, Part-thing₂, …, and Part-thingₙ.**

When the representation of the collection of parts at the particular extent of detail is incomplete, the aggregation-participation relation link shall signify the incomplete representation with an annotation.

Graphically, a short horizontal bar crossing the vertical line below the black triangle shall denote the incomplete aggregation-participation relation link.

The syntax of the aggregation-participation relation link indicating a partial collection of parts where at least one part is missing shall be:

**Whole-thing consists of Part-thing₁, Part-thing₂, …, Part-thingₖ, and at least one other part.**

[Figure: Diagram showing **Whole** composed of **Part A**, **Part B**, **Part C**, **Part D**, with a process **Consuming** that consumes selected parts. Another variant shows partial aggregation where only **Part B** and **Part D** are explicitly connected.]

---

### 10.3.3 Exhibition-characterization link

#### 10.3.3.1 Exhibition-characterization relation link expression

The fundamental structural relation exhibition-characterization shall mean that a refineable, the exhibitor, exhibits one or more features that characterize the exhibitor, the refinees. The features shall characterize the exhibitor.

A feature shall be a thing. An attribute shall be a feature that is an object. An operation shall be a feature that is a process. A process exhibitor and an object exhibitor shall each have at least one feature and may have both attributes, their object features, and operations, their process features.

The exhibition-characterization relation can combine the four exhibitor-feature combinations of object and process.

[Figure: Four diagrams illustrating combinations of exhibitor types and feature types — object exhibitor with attribute, object exhibitor with operation, process exhibitor with attribute, and process exhibitor with operation.]

**Object Exhibitor exhibits Attribute.**
**Process Exhibitor exhibits Attribute.**
**Object Exhibitor exhibits Operation.**
**Process Exhibitor exhibits Operation.**

Graphically, a smaller black triangle inside a larger empty triangle with that larger triangle’s apex connecting by a line to the exhibitor and the features connecting to the opposite (horizontal) base shall denote the exhibition-characterization relation link.

The syntax of the exhibition-characterization relation link for an object exhibitor with a complete collection of attributes and operations shall be:

**Object-exhibitor exhibits Attribute₁, Attribute₂, …, and Attributeₙ, as well as Operation₁, Operation₂, … and Operationₘ.**

The syntax of the exhibition-characterization relation link for a process exhibitor with a complete collection of n operation features and m attribute features shall be:

**Process-exhibitor exhibits Operation₁, Operation₂, … and Operationₙ, as well as Attribute₁, Attribute₂, … and Attributeₘ.**

**NOTE**

In the OPL for exhibition-characterization, for an object exhibitor the list of attributes precedes the list of operations, while for a process exhibitor the list of operations precedes the list of attributes.

When the representation of the collection of features at the particular extent of detail is incomplete, the exhibition-characterization relation link shall signify the incomplete representation with an annotation.

Graphically, a short horizontal bar crossing the vertical line below the larger empty triangle denotes the incomplete exhibition-characterization relation link.

The syntax of the exhibition-characterization relation link for an object exhibitor with a partial collection of attribute features and k operation features shall be:

**Object-exhibitor-thing exhibits Attribute₁, Attribute₂, …, Attributeⱼ, and at least one other attribute, as well as Operation₁, Operation₂, …, Operationₖ, and at least one other operation.**

The syntax of the exhibition-characterization relation link for a process exhibitor with a partial collection of j operation features and k attribute features shall be:

**Process-exhibitor exhibits Operation₁, Operation₂, … Operationⱼ, and at least one other operation, as well as Attribute₁, Attribute₂, … Attributeₖ, and at least one other attribute.**

---

#### 10.3.3.2 Attribute state and exhibitor features

##### 10.3.3.2.1 Attribute state as value

An attribute state, i.e. a state of the object that is the refinee attribute, shall be a value for that attribute. The static, conceptual model, shall identify all possible values for the attribute. Some may be ranges of values, while the dynamic, operational instance model shall indicate the actual attribute value at the time of the attribute’s inspection.

---

##### 10.3.3.2.2 Expressing exhibitor-feature relation

When expressing features or values for an attribute, the model shall identify the exhibitor of that feature or value. To specify the exhibitor of the feature, the relation **“of”** shall occur in OPL sentences between the feature and its exhibitor.

The syntax for an OPL sentence identifying the exhibitor-feature relation shall be:

**Feature of Exhibitor …**

**EXAMPLE 1**

Specific Weight in g/cm³ of Metal Powder Mixture ranges from 7.545 to 7.537.

**EXAMPLE 2**

Travelling Medium of Ship is water surface.

---

### 10.3.4 Generalization-specialization and inheritance

#### 10.3.4.1 Generalization-specialization relation link

The fundamental structural relation generalization-specialization shall mean that a refineable, the general, generalizes one or more refinees, which are specializations of the general. The generalization-specialization relation binds one or more specializations with the same Perseverance as the general, such that both the general and all its specializations are objects or the general and all its specializations are processes.

Graphically, an empty triangle with its apex connecting by a line to the general and the specializations connecting by lines to the opposite base shall denote the generalization-specialization relation link.

For a complete collection of n specializations of a general that is an object, the syntax of the generalization-specialization relation link OPL sentence shall be:

**Specialization-object₁, Specialization-object₂, …, and Specialization-objectₙ are General-object.**

For a complete collection of n specializations of a general that is a process, the syntax of the generalization-specialization relation link OPL sentence shall be:

**Specialization-process₁, Specialization-process₂, …, and Specialization-processₙ are General-process.**

When the representation of the collection of specializations at the particular extent of detail is incomplete, the generalization-specialization relation link shall signify the incomplete representation with an annotation.

Graphically, a short horizontal bar crossing the vertical line below the empty triangle shall denote the incomplete generalization-specialization relation link.

For an incomplete set of k specializations of a general that is an object, the syntax of the generalization-specialization relation link OPL sentence shall be:

**Specialization-object₁, Specialization-object₂, …, Specialization-objectₖ, and at least one other specialization are General-object.**

For an incomplete set of k specializations of a general that is a process, the syntax of the generalization-specialization relation link OPL sentence shall be: **Specialization-process₁, Specialization-process₂, …, Specialization-processₖ**, and at least one other specialization are **General-process**.

**EXAMPLE**
Figure 24 shows single and plural specializations of objects and processes.

[Figure: Four diagrams illustrating specialization relationships.
Top left: A box labeled “Camera” connected via a generalization triangle to “Digital Camera”, representing the statement “Digital Camera is a Camera.”
Top right: An oval labeled “Food Gathering” connected via a generalization triangle to “Hunting”, representing “Hunting is Food Gathering.”
Bottom left: A box labeled “Camera” connected via a generalization triangle branching to two boxes “Analog Camera” and “Digital Camera”, illustrating that both are types of Camera.
Bottom right: An oval labeled “Food Gathering” connected via a triangle branching to “Hunting” and “Fishing”, showing both as specializations of Food Gathering.]

**Digital Camera is a Camera**

**Hunting is Food Gathering**

**Analog Camera and Digital Camera are Cameras**

**Hunting and Fishing are Food Gathering**

**Figure 24 — Single and plural specializations of objects and processes**

**NOTE**
A tool can keep track of the set of refinees for each refineable and adjust the symbol and corresponding OPL sentences for each fundamental structural relation link as the modeller changes the collection of refinees.

---

#### 10.3.4.2 Inheritance through specialization

Inheritance shall be assignment of OPM elements, things and links, of a general to its specializations.

A specialization thing shall inherit from the general thing through the generalization-specialization link each of the following four kinds of inheritable elements that exist:

* all the parts of a general from its aggregation-participation link;
* all the features of the general from its exhibition-characterization link;
* all the tagged structural links to which the general connects; and
* all the procedural links to which the general connects.

OPM shall provide the opportunity for multiple inheritances by allowing a thing to inherit from more than one general thing each of the refinees – the four inheritable elements (participants, features, tagged structural links, and procedural links) that exist for that general thing.

The modeller may override any of the participants of the general thing, which are by default inherited by the specialization, by specifying for any participant inherited from a general, a specialization of that participant with a different name and a different set of states (see **10.3.4.3**).

**NOTE**
When a generalization-specialization relation link exists, at runtime the specialized thing instance does not exist in the absence of the more general thing instance that it specializes and from which it inherits each of the four kinds of inheritable elements.

---

To create a general from one or more candidate specializations, the inheritable elements common to each of the candidates shall be migrated to a generalization thing. The manipulation of inheritable elements shall be as follows:

* Combine all of the common features and common participants of the specializations into one newly created general;
* Connect the new general using the generalization-specialization relation link to the specializations;
* Remove from the specializations all of the common features and common participants, which the specializations now inherit from the new general; and
* Migrate any common tagged structural links and any common procedural link edge that connects to all the specializations from the specializations to the general.

---

#### 10.3.4.3 Specialization restriction through discriminating attribute

The possible values of an attribute inherited from a general may restrict the permissible value of a specialization. An inherited attribute with different values that constrain distinct values for corresponding specialization characteristics shall be a **discriminating attribute**.

**NOTE**
A specialization inherits the features, and possible attribute values, of its generalization. Elaborating the general through refinement allows for a more precise valuation of inherited attributes, including specification of attribute value appropriate for the specialization’s characterization through the exhibition-characterization refinement that it inherits (see also **10.4.1**).

**EXAMPLE 1**
Figure 25 shows an OPD in which **Vehicle** exhibits the attribute **Travelling Medium** with values **ground**, **air**, and **water surface**. **Travelling Medium** is the discriminating attribute of **Vehicle**, because it constrains the specializations of **Vehicle** to values of its **Travelling Medium**. **Vehicle** has specializations **Car**, **Aircraft**, and **Ship**, with the corresponding **Travelling Medium** values **ground**, **air**, and **water surface**.

[Figure: Diagram showing a class “Vehicle” exhibiting an attribute “Travelling Medium” with three possible values: ground, air, and water surface. Below it, three specializations branch from Vehicle: Car, Aircraft, and Ship. Each specialization is associated with the specific value of the attribute Travelling Medium: Car → ground, Aircraft → air, Ship → water surface.]

Vehicle exhibits Travelling Medium.
Travelling Medium of Vehicle can be ground, air, and water surface.
Car, Aircraft, and Ship are Vehicles.
Travelling Medium of Car is ground.
Travelling Medium of Aircraft is air.
Travelling Medium of Ship is water surface.

**Figure 25 — The discriminating attribute Travelling Medium and its specializations**

---

A general may have more than one discriminating attribute. The maximum number of specializations with more than one discriminating attribute shall be the Cartesian product of the number of possible values for each discriminating attribute, where some combination of attribute values may be invalid.

**EXAMPLE 2**
Extending the content of Figure 25, another attribute of **Vehicle** might be **Purpose** with the two values **civilian** and **military**. Based on these two values, there are two Vehicle specializations: **civilian Vehicle** and **military Vehicle**. Due to multiple inheritance, the result is an inheritance lattice where the number of the most detailed specializations would be 3 × 2 = 6 as follows: **civilian Car**, **civilian Aircraft**, **civilian Ship**, **military Car**, **military Aircraft**, and **military Ship**.

---

### 10.3.5 Classification-instantiation link

#### 10.3.5.1 Classification-instantiation relation link

The fundamental structural relation classification-instantiation shall mean that a refineable, the class, classifies one or more refinees, the instances of the classification. The classification, which is an object class or a process class, is a source pattern for a thing connecting with one or more destination things, which are instances of the source thing’s pattern, i.e. the qualities the pattern specifies acquire explicit values to instantiate the instance thing. This relation provides the modeller with an explicit mechanism for expressing the relationship between a class and its instances, which the provisioning of values creates.

**NOTE 1**
The use of the term instance when considering members of the instance set of a conceptual class are referred to as “refinee instances” to distinguish them from “operational instances” of an operating model. For every refinee instance, there are one or more operational instances possible.

**NOTE 2**
All OPM things expressed in a conceptual model are a class pattern for instances of that thing intended to occur during model evaluation or operation. By creating a thing in the conceptual model, the modeller is implying that at least one operational instance of that thing or a specialization of that thing can exist at some time during the system’s operation.

If the class pattern includes an exhibition-characterization link specifying a refinee attribute with a permissible range of values, then the corresponding attribute value of each operational instance of a refinee instance of that class shall be within the value range specification of its class attribute feature.

Graphically, a small black circle inside an otherwise empty larger triangle with apex connecting by a line to the class thing and the instance things connecting by lines to the opposite base shall denote the classification-instantiation relation link.

The syntax of the classification-instantiation relation link between an object class and a single instance shall be:
**Instance-object is an instance of Class-object.**

The syntax of the classification-instantiation relation link between a process class and a single instance shall be:
**Instance-process is an instance of Class-process.**

The syntax of the classification-instantiation relation link between a process class and n instances shall be:
**Instance-object₁, Instance-object₂ and Instance-objectₙ are instances of Class-object.**

The syntax of the classification-instantiation relation link between a process class and n instances shall be:
**Instance-process₁, Instance-process₂ and Instance-processₙ are instances of Class-process.**

**NOTE 3**
Since the number of instances of any class might not be known a priori and can vary during operation of the system, there is no distinction between complete and incomplete collections of destination things for the classification-instantiation relation.

**EXAMPLE 1**
In Figure 26, **Adult** is a class with three attributes: **Gender**, with possible values **female** and **male**, **Height in cm**, with possible values **120..240**, and **Weight in kg**, with possible values **40..240**. **Jack Robinson** is an instance of **Adult**, with **Gender** value **male**, **Height in cm** value **185** and **Weight in kg** value **88**.

[Figure: Two diagrams comparing conceptual class and instance. Left side shows class “Adult” with attributes Gender (female, male), Height (120–240 cm), and Weight (40–240 kg). Right side shows instance “Jack Robinson : Adult” with concrete values: Gender = male, Height = 185 cm, Weight = 88 kg.]

Adult exhibits Gender, Height in cm, and Weight in kg.
Gender of Adult can be female or male.
Height in cm of Adult ranges from 120 to 240.
Weight in kg of Adult ranges from 40 to 240.

Jack Robinson is an instance of Adult.
Gender of Jack Robinson is male.
Height in cm of Jack Robinson is 185.
Weight in kg of Jack Robinson is 88.

**Figure 26 — Classification-instantiation with value range (class on left and instance on right)**

**EXAMPLE 2**
The OPD on the left hand side of Figure 27 is a conceptual model of **Metal Powder Mixture**, indicating that its **Specific Weight** attribute value can range from **7.545 g/cm³ to 7.537 g/cm³**. Figure 27 is an operational instance (runtime) model of **Metal Powder Mixture Instance**, indicating that its **Specific Weight** attribute value is **7.555 g/cm³**. This value is within the allowable range.

[Figure: Conceptual model showing object “Metal Powder Mixture” with attribute “Specific Weight [gr/cm3]” having range 7.545–7.573. On the right, an instance “Mixture Lot #7545 : Metal Powder Mixture” with attribute value Specific Weight = 7.555.]

Metal Powder Mixture exhibits Specific Weight in g/cm³.
Specific Weight in g/cm³ of Metal Powder Mixture ranges from 7.545 to 7.537.
Mixture Lot #7545 is an instance of Metal Powder Mixture.
Specific Weight in g/cm³ of Mixture Lot #7545 is 7.555.

**Figure 27 — Attribute state as value: conceptual versus operational models**

**NOTE 4**
The OPL sentence “Mixture Lot #7545 exhibits Specific Weight in g/cm³” is not present in the OPL of Figure 27 because that sentence is implicit from the expressed fact “Mixture Lot #7545 is an instance of Metal Powder Mixture”, and therefore Mixture Lot #7545 inherits this attribute from Metal Powder Mixture.

---

#### 10.3.5.2 Instances of object class and process class

An object class and a process class shall be two distinct kinds of classes. An instance of a class shall be an incarnation of a particular identifiable instance of that class with the same classification identifier.

A single refinee object shall be an object instance, while the pattern of object, to which all of the instances adhere, shall be an object class, the refineable.

A process class shall be a pattern of happening (the sequence of subprocesses), which involves object classes that are members of the preprocess and postprocess object sets. A process occurrence, which follows this pattern and involves particular object instances in its preprocess and postprocess object sets, shall be a process instance. Hence, a process instance shall be a particular occurrence of a process class to which that instance belongs. Any process instance shall have associated with it a distinct set of preprocess and postprocess object instance sets.

**NOTE**
The power of the process class concept is that it enables the modelling of a process as a template or a protocol for some transformation that a class of objects undergoes. That transformation includes neither the spatio-temporal framework nor the particular set of object instances with which the process instance associates.

---

### 10.3.6 Structural relation link and tagged structural link summary

### Table 14 — Structural relations and link summary

| Structural Relation Forward-Reverse (refineable-to-refinee; bold is the short name) | OPD Symbol                                                                          | OPL Sentence Forward (refineable-to-refinee)           | OPL Sentence Reverse (refinee-to-refineable)             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| Aggregation-Participation                                                           | [Diagram: Whole connected via triangle to Part A and Part B]                        | Whole consists of Part A and Part B.                   | –                                                        |
| Exhibition-Characterization                                                         | [Diagram: Exhibitor connected via triangle to Attribute A and Operation B]          | Exhibitor exhibits Attribute A as well as Operation B. | –                                                        |
| Generalization-Specialization                                                       | [Diagram: General Thing branching to Specialization A and Specialization B]         | –                                                      | Specialization A and Specialization B are General Thing. |
| Classification-Instantiation                                                        | [Diagram: Class branching to Instance A and Instance B via classification triangle] | –                                                      | Instance A and Instance B are instances of Class.        |
| Unidirectional tagged [Unidirectional null tagged]                                  | [Diagram: Source → Destination with tag-name]                                       | Source tag-name Destination.                           | [Source relates to Destination.]                         |
| Bidirectional tagged                                                                | [Diagram: A ↔ B with tags a-to-b and b-to-a]                                        | A a-to-b tag B.                                        | B b-to-a tag A.                                          |
| Reciprocal tagged [Reciprocal null tagged]                                          | [Diagram: A ↔ B reciprocal tag]                                                     | A and B are reciprocal tag.                            | [A and B are related.]                                   |

---

## 10.4 State-specified structural relations and links

### 10.4.1 State-specified characterization relation link

A state-specified characterization relation link shall be an exhibition-characterization relation link from a specialized object that exhibits an attribute value for a discriminating attribute of its generalization, meaning that the specialized object shall have only that value for the attribute it inherits.

Graphically, the exhibition-characterization relation link triangular symbol, with its apex connecting to the specialized object and its opposite base connecting to the value shown as a state, shall denote the state-specified characterization relation link.

**NOTE**
While not necessary, the OPD will be more understandable if the exhibition-characterization link of the general with the discriminating attribute appears in the same OPD as well (see Figure 28).

The syntax of the state-specified characterization relation link shall be:
**Specialized-object exhibits value-name Attribute-Name.**

**EXAMPLE**
Using the state-specified characterization relation link, the OPD in Figure 28 is significantly more compact than its equivalent OPD in Figure 25. Here, the discriminating attribute **Travelling Medium** of **Vehicle** with values **ground, air, and water surface** appears only once, as opposed to four times in Figure 25. The model for **Car, Aircraft, and Ship** are specializations of **Vehicle**, connecting each specialization with a state-specified characterization relation link to the corresponding **Travelling Medium** value of **ground, air, and water surface** respectively.

[Figure: Diagram showing Vehicle specialized into Car, Aircraft, and Ship. A shared attribute Travelling Medium (ground, air, water surface) is shown once, and each specialization connects to its specific value through a state-specified characterization relation.]

Vehicle exhibits Travelling Medium.
Travelling Medium of Vehicle can be ground, air, and water surface.
Car, Aircraft, and Ship are Vehicles.
Car exhibits ground Travelling Medium.
Aircraft exhibits air Travelling Medium.
Ship exhibits water surface Travelling Medium.

**Figure 28 — State-specified characterization link example**

---

### 10.4.2 State-specified tagged structural relations

#### 10.4.2.1 State-specified tagged structural links

A state-specified tagged structural link shall be a tagged structural link between an object state or attribute value and another object, object state or attribute value, signifying a relation between these two things with the tag expressing the semantics of the relation. In case of a null tag, i.e. no explicit tag specification, the corresponding OPL shall use the default null tag (see **10.2.2**).

Three kinds of state-specified tagged structural links shall exist: source state-specified tagged structural link; destination state-specified tagged structural link; and source-and-destination state-specified tagged structural link. Each kind shall include the unidirectional, bidirectional, and reciprocal tagged structural link, giving rise to seven kinds of state-specified tagged structural relation link and corresponding OPL sentences, which Table 15 summarizes.

---

#### 10.4.2.2 Unidirectional source state-specified tagged structural link

A unidirectional source state-specified tagged structural link shall be a unidirectional tagged structural link from a specific state of the source object to a destination object without a state specification.

Graphically, an arrow with an open arrowhead connecting from a state of the source object to the destination object and a tag-name annotation near the shaft shall denote a unidirectional source state-specified tagged structural link.

The syntax of the unidirectional source state-specified tagged structural link OPL sentence shall be:
**Specified-state source-object tag-name Destination-object.**

**NOTE**
A null tag uses the default tag-name “relates to”, not in bold, unless modified by the modeller.

---

#### 10.4.2.3 Unidirectional destination state-specified tagged structural link

A unidirectional destination state-specified tagged structural link shall be a unidirectional tagged structural link from a source object without a state specification to a specific state of the destination object.

Graphically, an arrow with an open arrowhead connecting from a source object to a specific state of the destination object and a tag-name annotation near the shaft shall denote a unidirectional destination state-specified tagged structural link.

The syntax of the unidirectional destination state-specified tagged structural link OPL sentence shall be:
**Source-object tag-name specified-state Destination-object.**

**NOTE**
A null tag uses the default tag-name “relates to”, not in bold, unless modified by the modeller.

---

#### 10.4.2.4 Unidirectional source-and-destination state-specified tagged structural link

A unidirectional source-and-destination state-specified tagged structural link shall be a unidirectional tagged structural link from a specific state of a source object to a specific state of the destination object.

Graphically, an arrow with an open arrowhead connecting from a specific state of a source object to a specific state of the destination object and a tag-name annotation near the shaft shall denote a unidirectional source-and-destination state-specified tagged structural link.

The syntax of the unidirectional source-and-destination state-specified tagged structural link OPL sentence shall be:
**Source-specified-state source-object tag-name destination-specified-state Destination-object.**

**NOTE**
A null tag uses the default tag-name “relates to”, not in bold, unless modified by the modeller.

---

#### 10.4.2.5 Bidirectional source-or-destination state-specified tagged structural link

A bidirectional source-or-destination state-specified tagged structural link shall be a bidirectional tagged structural link with a specific state for either the source or destination object but not both.

Graphically, a line with harpoon shaped arrowheads on opposite sides at both ends of the link, one connecting to an object or object state and the other connecting to an object state or object respectively, shall denote a bidirectional tagged structural link. Each tag-name shall align on the side of the arrow with the harpoon edge sticking out of the arrowhead, unambiguously determining the direction in which each relation applies.

The syntax of the resulting bidirectional source-or-destination state-specified tagged structural link shall be two separate unidirectional tagged structural link OPL sentences, one for each direction with the corresponding state specifications.

---

#### 10.4.2.6 Bidirectional source-and-destination state-specified tagged structural link

A bidirectional source-and-destination state-specified tagged structural link shall be a bidirectional tagged structural link with a specific state for both the source and destination object.

Graphically, a line with harpoon shaped arrowheads on opposite sides at both ends of the link, connecting a specific state of one object to a specific state of another object, shall denote a bidirectional tagged structural link. Each tag-name shall align on the side of the arrow with the harpoon edge sticking out of the arrowhead, unambiguously determining the direction to which each relation applies.

The syntax of the resulting bidirectional source-and-destination state-specified tagged structural link shall be two separate unidirectional source-and-destination tagged structural link OPL sentences, one for each direction with the corresponding state specifications.

---

#### 10.4.2.7 Reciprocal source-or-destination state-specified tagged structural link

A reciprocal source-or-destination tagged structural link shall be a bidirectional source-or-destination tagged structural link with a specific state for one of the involved objects but not both, and only one reciprocity-tag or no tag. In either case, reciprocity shall indicate that the tag of a reciprocal source-or-destination state-specified tagged structural link has the same semantics for each direction of the relation. When no tag appears, the default tag shall be **“are related”**.

Graphically, a line with harpoon shaped arrowheads on opposite sides at both ends of the link, connecting a specific state of one object to another object without state specification and depicting only one tag-name aligning with the arrow, shall denote a reciprocal source-or-destination state-specified tagged structural link.

The syntax of the reciprocal source-or-destination state-specified tagged structural link with only one tag shall be either:
**Source-specified-state Source-object and Destination-object are reciprocity-tag**;
or,
**Source-object and destination-specified-state Destination-object are reciprocity-tag.**

---

#### 10.4.2.8 Reciprocal source-and-destination state-specified tagged structural link

A reciprocal source-and-destination tagged structural link shall be a bidirectional source-and-destination tagged structural link with a specific state for both involved objects, and only one reciprocity-tag or no tag. In either case, reciprocity shall indicate that the tag of a reciprocal source-and-destination state-specified tagged structural link has the same semantics for each direction of the relation. When no tag appears, the default tag shall be **“are related”**.

Graphically, a line with harpoon shaped arrowheads on opposite sides at both ends of the link connecting a specific state of one object to a specific state of another object and depicting only one tag-name aligning with the arrow, shall denote a reciprocal source-and-destination state-specified tagged structural link.

The syntax of the reciprocal source-and-destination state-specified tagged structural link with only one tag-name shall be:
**Source-specified-state Source-object and destination-specified-state Destination-object are reciprocity-tag.**

The syntax of the reciprocal source-and-destination state-specified tagged structural link with no tag-name shall be:
**Source-specified-state Source-object and destination-specified-state Destination-object are related.**

---

#### 10.4.2.9 State-specified tagged structural link summary

### Table 15 — State-specified structural relations and links summary

| Directionality     | source state-specified                | destination state-specified | source-and-destination state-specified        |
| ------------------ | ------------------------------------- | --------------------------- | --------------------------------------------- |
| **unidirectional** | S A tag-name B.                       | B tag-name S A.             | Sa A tag-name Sb B.                           |
| **bidirectional**  | S A f-tag-name B. / B b-tag-name S A. | —                           | Sa A f-tag-name Sb B. / Sb B b-tag-name Sa A. |
| **reciprocal**     | B and S A are recip-tag-name.         | —                           | Sa A and Sb B are recip-tag-name.             |

**EXAMPLE 1**
In the OPD in Figure 29, **Keeper** is an attribute of **Check** with values **payer**, **payee**, and **bank**. Each of these values is also an object in its own right in the model. Three unidirectional, source-state-specified null-tagged structural links connect each value to its corresponding object. Note that there is no requirement that the name of the state or value be the same as the name of the related object, as demonstrated by **financial institution** and **Bank**.

[Figure: Diagram illustrating a **Check-Based Paying** process. In the center is a circular process labeled “Check-Based Paying.” On the left side is a grouping labeled **Keeper**, containing three roles represented as small rounded boxes: **payer**, **payee**, and **financial institution**. Each role connects to corresponding object boxes labeled **Payer**, **Payee**, and **Bank**, which are linked to the central process. On the right side is a grouping labeled **Check**, listing four possible states of a check: **blank**, **signed**, **endorsed**, and **cashed & cancelled**. Multiple arrows indicate structural links between the keeper roles and the central process.]

Check can be **blank**, **signed**, **endorsed**, or **cashed & cancelled**.
Check exhibits **Keeper**.
Keeper can be **payer**, **payee**, or **financial institution**.
Payer Keeper relates to **Payer**.
Payee Keeper relates to **Payee**.
Financial institution Keeper relates to **Bank**. (remaining OPL omitted)

**Figure 29 — Associating attribute values with objects via state-specified structural link**

**EXAMPLE 2**
In the OPD in **Figure 30**, each one of the three **Phase** values of **Water** is associated with its corresponding **Temperature** value range via three source-and-destination state-specified tagged structural links whose tag is “**exists for the range of**”.

---

[Figure: Diagram showing object **Water** connected to two attribute groups: **Phase** and **Temperature [Celsius]**.
The **Phase** group contains three states: **solid**, **liquid**, and **gas**.
The **Temperature [Celsius]** group contains three ranges: **below zero**, **between zero and 100**, and **above 100**.
Arrows labeled “exists for the range of” link each phase to its corresponding temperature range: solid → below zero; liquid → between zero and 100; gas → above 100.]

Water exhibits **Phase** and **Temperature in Celsius**.
Phase of Water can be **solid**, **liquid** or **gas**.
Temperature of Water in Celsius can be **below zero**, **between zero and 100**, or **above 100**.
Solid Phase exists for the range of **below zero Temperature in Celsius**.
Liquid Phase exists for the range of **between zero and 100 Temperature in Celsius**.
Gas Phase exists for the range of **above 100 Temperature in Celsius**.

**Figure 30 — Source-and-destination state-specified tagged structural link**

---

## 11 Relationship cardinalities

## 11.1 Object multiplicity in structural and procedural links

Object multiplicity shall refer to a requirement or constraint specification, sometimes called a participation constraint, on the quantity or count of object operational instances associated with a link. Unless a multiplicity specification is present, each end of a link shall specify only one object operational instance. Multiplicity specifications may appear in the following situations:

a) to specify multiple source or destination object operational instances for a tagged structural link of any kind;

b) to specify a participant object with multiple operational instances in an aggregation-participation link, where a different participation specification may be attached to each one of the parts of the whole; and

c) to specify an object with multiple operational instances in a procedural relation.

The specification of object multiplicity may occur as integers or as parameter symbols that resolve to integer values during model execution and may include arithmetic expressions. The specification may include a range of values or a set of value ranges.

Graphically, an integer, a range of integers, a parameter symbol, a range of parameter symbols, or set of integers or parameter symbols, any of which may appear as annotations near the link end to which it applies, shall denote object multiplicity.

The syntax of an OPL sentence that includes an object with multiplicity shall include the object multiplicity preceding the object name, with the object name appearing in its plural form if the cardinality specifies more than one operational instance is possible. The following EXAMPLES present some of the many uses of object multiplicity on OPL sentences.

---

[Figure: Two small diagrams showing object multiplicity examples.
Left diagram: **Factory** linked to **Shopfloor** with the number **3** above the link.
Right diagram: **Printer** linked to two parts **Colour Cartridge** and **Black Cartridge**, with multiplicity **3** shown for Colour Cartridge.]

Factory comprises **3 Shopfloors**.
Printer consists of **3 Colour Cartridges**, **Black Cartridge** and other parts.

**Figure 31 — Object multiplicity examples**

Object multiplicity may be a parameter or a range of parameters or a set of two or more ranges of numbers and/or parameters separated by a comma. A range shall be indicated as qmin .. qmax and shall be closed, i.e. include the boundaries qmin and qmax. In OPL, the expression of the range symbol “..” shall be “to” and the expression of the comma that separates two adjacent ranges shall be “or”.

The specification of object multiplicity may occur as an optionality parameter using the range symbol, the asterisk symbol and the question mark symbol in the following manner:

— “0..1” shall mean zero or one, using the question mark (?) annotation near the object to which it applies with an OPL syntax of “an optional” immediately preceding the object;

— “0..*” shall mean zero or more, using the asterisk symbol (*) annotation near the object to which it applies with the OPL syntax of “optional” immediately preceding the object; and

— “1..*” shall mean one or more, using the plus symbol (+) annotation near the object to which it applies with OPL syntax of “at least one” immediately preceding the object.

**NOTE 1**
The range symbol “..” has two uses in multiplicity specification, one as a separator between two boundary values, e.g. qmin .. qmax, with interpretation of “to” and one as separator between optional values, e.g. “0..*”, with interpretation of “or”.

**NOTE 2**
Care is necessary when specifying cardinality constraints so that the constraint applies to the object as specified and not a property of that object. If the object has a unit of measure, then multiplicity refers to the count of single units of that measure, e.g. 32 Water in millilitres.

---

## Table 16 — Link optionality summary

| Lower & Upper Bounds qmin .. qmax | Participation Constraint Symbol & OPL Phrase | OPD Example & Corresponding OPL Sentence                                                                               |
| --------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 0..1                              | ? — an optional                              | [Figure: Diagram showing Car linked to Sunroof with a question mark annotation.] **Car has an optional Sunroof.**      |
| 0..*                              | * — optional (none to many)                  | [Figure: Diagram showing Car linked to Airbag with an asterisk annotation.] **Car is equipped with optional Airbags.** |
| 1..1                              | (none)                                       | [Figure: Diagram showing Car linked to Steering Wheel.] **Car is steered by Steering Wheel.**                          |
| 1..*                              | + — at least one                             | [Figure: Diagram showing Car linked to Spare Tire with plus annotation.] **Car carries at least one Spare Tire.**      |

---

## 11.2 Object multiplicity expressions and constraints

Object multiplicity may include arithmetic expressions, which shall use the operator symbols “+”, “-”, “*”, “/”, “(“, and “)” with their usual semantics and shall use the usual textual correspondence in the corresponding OPL sentences.

An integer or an arithmetic expression may constrain object multiplicity. Graphically, expression constraints shall appear after a semicolon separating them from the expression that they constrain and shall use the equality/inequality symbols “=”, “≠”, “<”, “≤”, and “≥”, the curly braces “{” and “}” for enclosing set members, and the membership operator “in” (element of, ∈), all with their usual semantics.

The corresponding OPL sentence shall place the constraint phrase in bold letters after the object to which the constraint applies in the form “, where constraint”.

**EXAMPLE 1**
Figure 32 provides object multiplicity examples with ranges and parameters.

[Figure: Two diagrams showing **Machine Center** controlling **Machine** with multiplicity expressions.
First diagram: “3..5, 8..10”.
Second diagram: “2, 3*n; n ≤ 4”.]

Machine Center controls **3 to 5 or 8 to 10 Machines**.
Machine Center controls **2 or 3*n Machines, where n ≤ 4**.

**Figure 32 — Object multiplicity examples with ranges and parameters**

---

**EXAMPLE 2**
Figure 33 models a **Blade Replacing** system in which a **Jet Engine** has **b Installed Blades**. Two to four (a number set to k) **Aviation Engine Mechanics** handle the Blade Replacing process, for which they use **k Blade Fastening Tools**. Also, one or two **Aerospace Engineers** handle the Blade Replacing process. This process yields **b Dismantled Blades**, which undergo **Blade Inspecting**, an environmental process that yields **a (which is at most b) of Inspected Blades**. The process consumes a total of **b Blades**, with **i inspected and b−i new**. Any number of **new Blades** can be obtained by **Purchasing** them.

[Figure: Complex OPD diagram with objects Aviation Engine Mechanic, Blade Fastening Tool, Aerospace Engineer, Jet Engine, Installed Blade, Blade, Dismantled Blade and processes Blade Replacing, Blade Inspecting, and Purchasing, with multiplicity parameters b, i, k and constraints.]

k = 2 to 4 **Aviation Engine Mechanics** handle **Blade Replacing**.
Jet Engine can be **used** or **refurbished**.
Jet Engine consists of **b Installed Blades**.
1 to 2 **Aerospace Engineers** handle **Blade Replacing**.
An optional **Aerospace Engineer** handles **Blade Inspecting**.
Blade can be **inspected** or **new**.
Blade Replacing requires **k Blade Fastening Tools**.
Blade Replacing changes **Jet Engine** from **used** to **refurbished**.
Blade Replacing consumes **i inspected Blades** and **b − i new Blades**.
Blade Replacing yields **b Dismantled Blades**.
Blade Inspecting consumes **b Dismantled Blades**.
Blade Inspecting yields **a ≤ b inspected Blades**.
Purchasing yields **many new Blades**.

**Figure 33 — Object multiplicity: arithmetic expressions and constraints example**

If an object multiplicity parameter has more than one constraint, they shall appear as a semicolon-separated list of constraints following the parameter. Any constraint may include any object multiplicity parameter appearing in the model. Parameter names shall be unique for the entire system model.

**EXAMPLE 3**
Figure 34 depicts a way to specify parameterized participation constraints in an OPD and the corresponding OPL sentences.

[Figure: Diagram showing **Airplane** consisting of **Body**, **2 Wings**, and **e Engines**, with constraints linking engines to body and wings. Expressions show relationships among parameters e, b, and w.]

Airplane consists of **Body**, **2 Wings**, and **e Engines**, where **e ≥ 1, e = b + 2*w**.
**b Engines** are attached to **Body**, where **b in {0,1}**.
**w Engines** are attached to **Wing**, where **0 ≤ w ≤ 3**.

**Figure 34 — Multiple parameterized constraints example**

**NOTE 1**
Aggregation-participation is the only fundamental structural relation for which participation constraints apply.

**NOTE 2**
Expressing multiplicity of processes does not use participation constraints. Rather, expressing sequential repetition of the same process uses a recurrent process with a counter for the number of iterations. Parallel synchronous processes or asynchronous processes within an in-zoomed process provide other iteration mechanisms.

---

## 11.3 Attribute value and multiplicity constraints

The expression of object multiplicity for structural and procedural links specifies integer values or parameter symbols that resolve to integer values. In contrast, the values associated with attributes of objects or processes may be integer or real values, or parameter symbols that resolve to integer or real values, as well as character strings and enumerated values.

**NOTE 1**
Real values accommodate expression using the unit of measure associated with the object.

Graphically, a labelled, rounded-corner rectangle placed inside the attribute to which it belongs shall denote an attribute value with the value or value range (integers, real numbers, or string characters) corresponding to the label name. In OPL text, the attribute value shall appear in **bold face** without capitalization.

The syntax for an object with an attribute value OPL sentence shall be:
**Attribute of Object is value.**

The syntax for an object with an attribute value range OPL sentence shall be:
**Attribute of Object range is value-range.**

**NOTE 2**
Attribute value range has the same expressiveness applicable for object multiplicity, except optionality.

A structural or a procedural link connecting with an attribute that has a real number value may specify a relationship constraint, which is distinct from an object multiplicity.

Graphically, an attribute value constraint is an annotation by a number, integer or real, or a symbol parameter, near the attribute end of the link and aligning with the link.

---

## 12 Logical operators: AND, XOR, and OR

## 12.1 Logical AND procedural links

A group of two or more procedural links of the same kind that originate from, or arrive at, the same process shall have the semantics of logical AND.

Graphically, the links with AND semantics do not touch each other on the process contour.

The syntax of links with AND semantics shall be a phrase using “and” conjunction in a single OPL sentence rather than separate sentences for each link.

**EXAMPLE 1**
Figure 35 (right), the **Safe Opening** process requires both **Safe Owner A** and **Safe Owner B**. In Figure 35 (left), opening the **Safe** requires all three keys.

[Figure: Two diagrams of Safe Opening.
Left: Keys A, B, C connected to the Safe Opening process; Safe changes from closed to open.
Right: Safe Owner A and Safe Owner B connected to the Safe Opening process.]

Safe can be **closed** or **open**.
Safe Opening requires **Key A, Key B, and Key C**.
Safe Opening changes **Safe** from **closed** to **open**.

Safe can be **closed** or **open**.
Safe Owner A and Safe Owner B handle **Safe Opening**.
Safe Opening changes **Safe** from **closed** to **open**.

**Figure 35 — Logical AND for agent and instrument links**

---

**EXAMPLE 2**
In Figure 36 (left), **Meal Preparing** yields all three of the dishes. In Figure 36 (right), **Meal Eating** consumes all three dishes.

[Figure: Two diagrams showing processes with multiple results or consumptions.
Left: Chef performs Meal Preparing, producing Starter, Entree, Dessert.
Right: Meal Eating consumes Starter, Entree, Dessert and affects Diner.]

Chef handles **Meal Preparing**.
Meal Preparing yields **Starter, Entree and Dessert**.

Meal Eating affects **Diner**.
Meal Eating consumes **Dessert, Entree and Starter**.

**Figure 36 — Logical AND for result and consumption links**

---

**EXAMPLE 3**
In the OPD on the left of **Figure 37**, **Interest Rate Changing** affects the three objects **Exchange Rate**, **Price Index**, and **Interest Rate**. In the OPD on the right, all three effects of **Interest Rate Raising** on **Exchange Rate**, **Price Index**, and **Interest Rate** are explicit via three pairs of input-output-specified effect links.

[Figure: Two diagrams with Central Bank triggering interest rate change processes affecting exchange rate, price index, and interest rate.]

Central Bank handles **Interest Rate Changing**.
Interest Rate Changing affects **Exchange Rate, Price Index, and Interest Rate**.

Central Bank handles **Interest Rate Changing**.
Interest Rate can be **high** or **low**.
Price Index can be **low** or **high**.
Exchange Rate can be **high** or **low**.
Interest Rate Raising changes **Exchange Rate from low to high**, **Price Index from low to high**, and **Interest Rate from low to high**.

**Figure 37 — Logical AND for effect link and input-output link pairs**

---

## 12.2 Logical XOR and OR procedural links

A group of two or more procedural links of the same kind that originate from a common point, or arrive at a common point, on the same object or process shall be a link fan. A link fan shall follow the semantics of either a XOR or an OR operator. The link fan end that is common to the links shall be the convergent link end. The link end that is not common to the links shall be the divergent link end.

The **XOR** operator shall mean that exactly one of the things at the divergent link end of the link fan exists or occurs. If the divergent link end has objects, then only one exists. If the divergent link end has processes, then only one occurs.

**NOTE**
This use of the XOR operator in OPM is different to some binary XOR operator interpretations, where the output is 1 for an odd number of inputs and 0 for an even number of inputs.

Graphically, a dashed arc across the links of the link fan with the arc focal point at the convergent endpoint of contact shall denote the XOR operator.

The syntax of a link fan of n things with XOR semantics shall be a single OPL sentence containing a phrase of the form: **exactly one of Thing1, Thing2,…, and Thingn…**

The **OR** operator shall mean that at least one of the two or more things at the divergent end of the link fan exists or occurs. If the divergent link end has objects, then at least one object exists. If the divergent link end has processes, then at least one process occurs.

Graphically, two concentric dashed arcs across the links of the link fan with the focal point at the convergent endpoint of contact shall denote the OR operator.

The syntax of a link fan of n things with OR semantics shall be a single OPL sentence containing a phrase of the form: **at least one of Thing1, Thing2,…, and Thingn…**

**EXAMPLE**
In the OPD on the right of **Figure 38**, using XOR, exactly one of **Safe Owner A** and **Safe Owner B** needs to be present in order for **Safe Opening** to occur. In the OPD on the left, using OR, at least one of **Safe Owner A** and **Safe Owner B** needs to be present in order for **Safe Opening** to occur. The link fan in both OPDs is convergent and consists of two agent links.

[Figure: Two diagrams. Left shows OR semantics where Safe Opening can be handled by Safe Owner A or Safe Owner B. Right shows XOR semantics where exactly one of the two must handle Safe Opening.]

Exactly one of **Safe Owner A** and **Safe Owner B** handles **Safe Opening**.
At least one of **Safe Owner A** and **Safe Owner B** handles **Safe Opening**.

**Figure 38 — Logical OR (left) and logical XOR (right) examples of agent link**

---

## 12.3 Diverging and converging XOR and OR links

**Table 17** shows that when the source things are objects and the destination thing is a process, the consumption link fan is converging, while when the source things are processes and the destination thing is an object, the result link fan is converging.

---

## Table 17 — Summary of XOR and OR converging consumption and result links

|                                     | XOR                                                                                          | OR                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Converging consumption link fan** | [Figure: Objects A, B, C converging to process P.] **P consumes exactly one of A, B, or C.** | [Figure: Objects A, B, C converging to process P.] **P consumes at least one of A, B, or C.** |
| **Converging result link fan**      | [Figure: Processes P, Q, R converging to object B.] **Exactly one of P, Q, or R yields B.**  | [Figure: Processes P, Q, R converging to object B.] **At least one of P, Q, or R yields B.**  |

---

**Table 18** shows that when the source thing is an object and the destination things are processes, the consumption link fan shall be diverging, while when the source thing is a process and the destination things are objects, the result link fan shall be diverging.

---

## Table 18 — Summary of XOR and OR diverging consumption and result link fans

|                                    | XOR                                                                                          | OR                                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Diverging consumption link fan** | [Figure: Object B diverging to processes P, Q, R.] **Exactly one of P, Q, or R consumes B.** | [Figure: Object B diverging to processes P, Q, R.] **At least one of P, Q, or R consumes B.** |
| **Diverging result link fan**      | [Figure: Process P diverging to objects A, B, C.] **P yields exactly one of A, B, or C.**    | [Figure: Process P diverging to objects A, B, C.] **P yields at least one of A, B, or C.**    |

Since an effect link is bidirectional, the things linked by an effect link fan are both source and destination at the same time, voiding the definitions of convergent and divergent link fans. Instead, as **Table 19** shows, the distinction shall occur with respect to multiple objects or multiple processes that a link fan connects.

---

## Table 19 — Summary of XOR and OR effect link fans

|                                        | XOR                                                                                         | OR                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Multiple objects effect link fan**   | [Figure: Process P connected to objects A, B, C.] **P affects exactly one of A, B, or C.**  | [Figure: Process P connected to objects A, B, C.] **P affects at least one of A, B, or C.**  |
| **Multiple processes effect link fan** | [Figure: Processes P, Q, R connected to object B.] **Exactly one of P, Q, or R affects B.** | [Figure: Processes P, Q, R connected to object B.] **At least one of P, Q, or R affects B.** |

Since an enabler is an object, as shown in **Table 20**, both agent and instrument link fans shall be diverging with multiple processes as targets.

## Table 20 — Summary of agent and instrument link fans

|                         | **XOR**                                                                                                                                                                                                                                     | **OR**                                                                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agent link fan**      | [Figure: A process or entity **B** connected by a fan of links to three processes **P**, **Q**, and **R**. The fan indicates mutually exclusive branching. Only one of the three links is active.] **B handles exactly one of P, Q, or R.** | [Figure: A process or entity **B** connected by a fan of links to **P**, **Q**, and **R** with a non-exclusive fan indicator. Multiple links may be active simultaneously.] **B handles at least one of P, Q, or R.** |
| **Instrument link fan** | [Figure: Entity **B** connected via a fan to processes **P**, **Q**, and **R** where the instrument **B** is required by exactly one of them. The XOR fan marker indicates exclusivity.] **Exactly one of P, Q, or R requires B.**          | [Figure: Entity **B** connected via a fan to processes **P**, **Q**, and **R** where the instrument **B** may be required by one or more processes.] **At least one of P, Q, or R requires B.**                       |

Invocation link fans may be diverging or converging for both XOR and OR, as shown in Table 21.

---

## Table 21 — Summary of invocation link fans

|                                    | **XOR**                                                                                                                              | **OR**                                                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Diverging invocation link fan**  | [Figure: Process **P** branching to processes **Q** and **R** with an XOR fan marker.] **P invokes exactly one Q or R.**             | [Figure: Process **P** branching to **Q** and **R** with an OR fan marker.] **P invokes at least one of Q or R.**            |
| **Converging invocation link fan** | [Figure: Processes **P** and **Q** both connecting to process **R**, with an XOR merge marker.] **Exactly one of P or Q invokes R.** | [Figure: Processes **P** and **Q** both connecting to **R**, with an OR merge marker.] **At least one of P or Q invokes R.** |

---

## 12.4 State-specified XOR and OR link fans

Each one of the link fans in **12.3** shall have a corresponding state-specified version, where the source and destination may be specific object states or objects without a state specification. Combinations of state-specified and stateless links as sources and destinations of a link fan may occur.

**EXAMPLE**
Figure 39 shows on the left a XOR state-specified instrument link fan and on the right an OR mixed result link fan where the links are state-specified for objects **A** and **C** but not for **B**.

---

[Figure: Two diagrams demonstrating state-specified link fans.
Left: Object **B** with states **s1** and **s2** connected to processes **P**, **Q**, and **R**, indicating that exactly one of these requires state **s2** of **B**.
Right: Process **P** branching to objects **A**, **B**, and **C**, where **A** contains states **s3** and **s4**, **C** contains state **s5**, and **B** has no state specification. The result indicates that **P** yields at least one of **s3 A**, **B**, or **s5 C**.]

**Figure 39 — State-specified XOR and OR link examples**

---

## 12.5 Control-modified link fans

Each one of the XOR link fans for consumption, result, effect, and enabling links and their state-specified versions shall have a corresponding control-modified link fan: an **event link fan** and a **condition link fan**.

**Table 22** presents the event and condition effect link fans, as representatives of the basic (non-state-specified) links version of the modified link fans.

---

## Table 22 — Event and condition effect link fans

| **Event**                                                                                                                                                                                | **Condition**                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Figure: Object **B** linked to processes **P**, **Q**, and **R**, each with an event marker.] **B initiates exactly one of P, Q, or R, in which case the occurring process affects B.** | [Figure: Object **B** linked to processes **P**, **Q**, and **R**, each with a condition marker.] **Exactly one of P, Q, or R occurs if B exists, in which case the occurring process affects B. Otherwise these processes are skipped.** |

---

## 12.6 State-specified control-modified link fans

Each one of the control-modified link fans, except the control-modified effect link fan, shall have a corresponding state-specified control-modified link fan. Since the state-specified versions are more complicated than their non-state-specified version, **Table 23** presents the OPD and OPL of the state-specified versions and the corresponding stateless version below for each state-specified version.

---

## Table 23 — State-specified and stateless control-modified link fans

|                          | **Event Control modifier**                                                                                                                                                                                                                        | **Condition Control modifier**                                                                                                                                                                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Consumption link fan** | [Figure: Object **B** with states **s1** and **s2** linked to processes **P**, **Q**, **R**.] **S2 B initiates exactly one of P, Q, or R, which consumes B.**  *The stateless case:* **B initiates exactly one of P, Q, or R, which consumes B.** | **Exactly one of P, Q, or R occurs if B is s2, in which case the occurring process consumes B, otherwise these processes are skipped.**  *The stateless case:* **Exactly one of P, Q, or R occurs if B exists, in which case the occurring process consumes B, otherwise these processes are skipped.** |
| **Agent link fan**       | **S2 B initiates and handles exactly one of P, Q, or R.**  *The stateless case:* **B initiates and handles exactly one of P, Q, or R.**                                                                                                           | **B handles exactly one of P, Q, or R if B is s2, otherwise these processes are skipped.**  *The stateless case:* **B handles exactly one of P, Q, or R if B exists, otherwise these processes are skipped.**                                                                                           |
| **Instrument link fan**  | **S2 B initiates exactly one of P, Q, or R, which requires s2 B.**  *The stateless case:* **B initiates exactly one of P, Q, or R, which requires B.**                                                                                            | **Exactly one of P, Q, or R requires that B is s2, otherwise these processes are skipped.**  *The stateless case:* **Exactly one of P, Q, or R requires that B exists, otherwise these processes are skipped.**                                                                                         |

Each XOR link fan in **Table 22** and in **Table 23** shall have its **OR counterpart** (designated by a double-dotted arc) with a corresponding OPL sentence in which the reserved phrase **“at least”** replaces **“exactly.”**

---

## 12.7 Link probabilities and probabilistic link fans

A process **P** with a result link that yields a stateful object **B** with **n** states, **s1** to **sn**, without specifying a particular state shall mean that the probability of generating **B** at any one particular state shall be **1/n**. In this case, the single result link to the object shall replace the result link fan to each of its states.

**EXAMPLE 1**
In the left OPD of **Figure 40**, the result link from **P** to **B**, which has three states, means that **P** will create **B** with equal probability, **Pr = 1/3**, for creation at each state. The right OPD of **Figure 40** shows the more cumbersome way to express the same situation.

---

[Figure: Two diagrams illustrating equivalence between a single result link and XOR state-specific result links.
Left: Process **P** producing object **B** with states **s1**, **s2**, **s3** without specifying a particular state.
Right: Process **P** branching with XOR links to **s1 B**, **s2 B**, and **s3 B**, representing explicit state outcomes.]

**Figure 40 — Equivalence between result link and a set of XOR state-specified result links**

Generally, probabilities of following a specific link in a link fan are not equal. Link probability may be a property value assigned to a link in a XOR diverging link fan that specifies the probability of following that particular link among the possible links in the fan link. A probabilistic link fan shall be a link fan with annotations on each fan link for its probability property, where the sum of the probabilities shall be exactly **1**.

Graphically, along each fan link with a probability property an annotation shall appear in the form **Pr=p**, where **p** is the link probability numeric value or a parameter, which denotes the probability of the system execution control to select and follow that particular link of the fan.

The corresponding OPL sentence shall be the XOR diverging link fan sentence without link probabilities omitting the phrase **“exactly one of…”** and inserting the phrase **“…with probability p”** following each participating thing name with a probability annotation **“Pr=p.”**

**EXAMPLE 2**
**Figure 41** shows two probabilistic state-specified object creation examples and their deterministic analogues. In the OPD on the left, process **P** can create object **B** in three possible states, **s1**, **s2**, or **s3**, with corresponding probabilities **0.32**, **0.24**, and **0.44** indicated along each result link of the result link fan. In the OPD on the right, **P** can create one of the objects **A**, **B**, or **C** at state **sc1** with the probabilities indicated along each result link of the result link fan.

---

[Figure: Two diagrams of probabilistic object creation.
Left: Process **P** branching to **s1 B (0.32)**, **s2 B (0.24)**, and **s3 B (0.44)**.
Right: Process **P** branching to objects **A**, **B**, or **C (sc1)** with probabilities indicated.]

**Figure 41 — Probabilistic state-specified object creation examples**

For a process **P** with a result link that yields a stateful object **B** with states **s1** to **sn**, and with initial state **si**, **P** shall create **B** at state **si** with probability **1.0**. However, if **B** has **m**, with **m < n** initial states, **P** shall create **B** at one of the initial states with probability **1/m**.

For a probabilistic result link fan, any one of the resultees may be an object without or with a specified state. For all the link fans comprising other procedural link kinds (including those with the event and condition control modifiers), where the targets of the links in the link fan are processes, the source may be an object or a specified state of an object.

**EXAMPLE 3**
The OPD in the top of **Figure 42** shows a probabilistic result link fan in which **P** yields, with specified probabilities, one of the objects **A** or **B**, or **C** at state **sc1**, or **D** at state **sd1** or **sd2**. The OPD in the middle of **Figure 42** shows a probabilistic consumption link fan in which **A** is consumed, with specified probabilities, by one of the processes **P** or **Q** or **R**. The OPD in the bottom expresses the same, with the additional fact that **A** needs to be at state **s2**.

---

[Figure: Three diagrams illustrating probabilistic link fans involving objects with and without state specification.
Top: Process **P** branching probabilistically to objects **A**, **B**, **C(sc1)**, **D(sd1)**, **D(sd2)**.
Middle: Object **A** consumed probabilistically by processes **P**, **Q**, **R**.
Bottom: Same as middle but specifying state **s2** of object **A**.]

**Figure 42 — Objects with and without specified states as sources and destinations of a probabilistic link fan**

---

## 13 Execution path and path labels

A path label shall be a link property and corresponding annotation aligning a pair of procedural links. When the process precondition involves an object with path label link connections, and the postprocess object set has more than one possibility for destination object, the appropriate postprocess object set destination shall be the one obtained using a link with the same path label as that used by the preprocess object set.

**EXAMPLE 1**
In **Figure 43**, there are two output links: one from **Heating** to the state **liquid** of **Water** and the other to state **gas**. When entering **Heating** from state **ice**, it is not clear whether the result state is **liquid** or **gas**. The path labels along the procedural links resolve this dilemma by uniquely determining the appropriate link on process exit, as shown by the animated simulation on the left.

---

[Figure: Diagram showing object **Water** with states **ice**, **liquid**, and **gas**, and process **Heating**. Two labeled paths connect the states and the process, illustrating how labels such as **ice-to-liq** and **liq-to-gas** determine the output state.]

**Figure 43 — Execution path and path labels**

**NOTE**
A path label is a label on a procedural link that removes the ambiguity arising from multiple outgoing procedural links by specifying that the link to follow is the one with the same label as the one initiating the process.

**EXAMPLE 2**
**Figure 44** demonstrates the use of path labels on consumption and result links, followed by the OPL paragraph.

---

[Figure: Diagram with objects **Tomato**, **Cucumber**, and **Meat** connected to process **Food Preparing** with path labels **herbivore** and **carnivore**. Output objects **Salad**, **Stew**, and **Steak** are produced depending on the path label.]

Following path **carnivore**, Food Preparing consumes **Meat**.
Following path **herbivore**, Food Preparing consumes **Cucumber** and **Tomato**.
Following path **carnivore**, Food Preparing yields **Stew** and **Steak**.
Following path **herbivore**, Food Preparing yields **Salad**.

**Figure 44 — Path labels demonstrated on consumption and result links**

---

## 14 Context management with OPM

## 14.1 Completing the SD

The definition of system purpose, scope, and function in terms of boundary, stakeholders, preconditions and postconditions shall be the basis for determining whether other elements, including environmental things, should appear in the model.

The SD shall be an OPD that models:

* the stakeholders, in particular the beneficiaries;
* a process to convey the functional value the beneficiary expects to receive; and
* other environmental and systemic things necessary to create a succinct corresponding OPL paragraph.

The corresponding OPL paragraph should provide the situational context for the system’s operation.

Expression of the functional value may be:

* explicit, by identifying the source input and destination output states of the beneficiary or the initial and final values of one or more of its attributes, or
* implicit, by indicating that the beneficiary is affected by the system’s function.

The SD should contain only the central, important things – those things indispensable for understanding the function and context of the system. The modeller shall use the refinement mechanisms of OPM to expose gradually the detail concerning the things that are the content of the SD.

**EXAMPLE**
In a **Manufacturing Facility**, the **Beneficiary** has developed and deployed a **Preventive Maintenance System**. The function of the system, **Preventive Maintenance Executing**, changes the **Downtime** attribute of the **Manufacturing Facility** from “high” to “low”. This change adds functional value to the **Manufacturing Facility**, as it has more up-time to manufacture products and increase sales and revenues at the cost of investing in developing and operating the **Preventive Maintenance System**.

---

## 14.2 Achieving model comprehension

### 14.2.1 OPM refinement-abstraction mechanisms

OPM shall provide abstracting and refining mechanisms to manage the expression of model clarity and completeness. These mechanisms make possible the specification of contextualized model segments as separate, yet interconnected OPDs, which, taken together, comprise a model of the functional value providing system. These mechanisms shall enable presenting and viewing the modelled system, and the elements it contains, in various contexts that are interrelated with common objects, processes and relations. The set of clearly specified and compatible interconnected OPDs should completely specify the entire system to an appropriate extent of detail and provide a comprehensive representation of that system with a corresponding textual statement of the model in OPL.

The OPM refinement-abstraction mechanisms shall be the following three pairs: **State expression and suppression**, **unfolding and folding**, and **in-zooming and out-zooming**.

---

#### 14.2.1.1 State expression and state suppression

Explicitly depicting the states of an object in an OPD may result in a diagram that is too crowded or busy, making it hard to read or comprehend.

OPM shall provide an option for state suppression, which suppresses the appearance of some or all the states of an object as represented in a particular OPD when those states are not necessary in the context of that OPD.

The inverse of state suppression shall be state expression, which exposes information concerning possible object states. The OPL corresponding to an OPD shall express the states of the objects only as the OPD depicts.

In OPM the modeller may suppress any subset of states. However, the complete set of object states for an object shall be the union of the states of that same object appearing in all of the OPDs of the entire OPM model.

Graphically, the annotation indicating that an object presents a proper subset (i.e. at least one but not all) of its states, shall be a small state suppression symbol in the object’s right bottom corner. This symbol appears as a small state with an ellipsis label, which signifies the existence of one or more states that the view is suppressing. The textual equivalence of the state suppression symbol shall be the reserved phrase **“or other states”.**

**EXAMPLE**
**Figure 45** shows a stateful object with all states expressed, and a suppressed version.

---

[Figure: Two diagrams of object **A** with states **s1**, **s2**, **s3**, **s4**, **s5**.
Left diagram shows all states explicitly.
Right diagram shows only **s1** and **s3**, with an ellipsis symbol indicating additional suppressed states.]

**Figure 45 — A stateful object with all states expressed (left) and a partially suppressed version (right)**

---

#### 14.2.1.2 Unfolding and folding

Unfolding shall be a mechanism for refinement, elaboration, or decomposition. Unfolding shall reveal a set of things, the refinable, that relate to the unfolded thing, the refineable. The result of unfolding shall be a hierarchy tree, the root of which shall be the unfolded thing. Linked to the root shall be the things that constitute the elaboration of the unfolded thing.

Conversely, folding shall be a mechanism for abstraction or composition, which shall apply to an unfolded hierarchical tree. Folding shall hide the set of unfolded things, leaving just the root.

Each of the four fundamental structural relation links may apply unfolding and folding. The four kinds of unfolding-folding pairs shall be:

* aggregation unfolding—exposing the parts of a whole, and participation folding—hiding the parts of a whole;
* exhibition unfolding—exposing the exhibitor’s features, and characterization folding—hiding the exhibitor’s features;
* generalization unfolding—exposing the specializations of the general, and specialization folding—hiding the general’s specializations; and
* classification unfolding—exposing the class instances, and instantiation folding—hiding the class instances.

In-diagram unfolding shall occur when the refineable and its refinees appear unfolded in the same OPD. Because unfolding uses the fundamental structural links, in-diagram unfolding is graphically, syntactically and semantically equivalent to using fundamental structural links.

---

New-diagram unfolding shall occur when the refineable and its refinees appear unfolded in a new OPD.

Graphically, the refineable shall have a thick contour in both the more abstract OPD in which the refineable appears folded without refinees, and in the new more detailed OPD context, in which the refineable appears unfolded and connects to its refinees with one or more fundamental structural links.

The corresponding OPL sentence for the new-diagram OPD where the refineable has **n** refinees shall be:
**Refineable unfolds into Refinee1, Refinee2,..., and Refineen**

**NOTE 1**
Unfolding can be more precisely specified as part-unfolding, feature-unfolding, specialization-unfolding, and instance-unfolding (see **A.4.7.2**).

The modeller decision whether to use in-diagram or new-diagram unfolding should account for the trade-off between the clutter added to the current OPD and the need to create a new OPD for displaying the refinees and associated links amongst them.

**NOTE 2**
Unfolding often occurs as a combination of new-diagram and in-diagram unfolding to represent multiple elaboration or decomposition situations.

**NOTE 3**
Partial unfolding can be depicted in the same manner as a partial fundamental structural relation link.

To satisfy a particular contextual relevance for an OPD, a modeller may choose which refinees appear unfolded. Following the bimodal representation of OPM, the OPL corresponding to the OPD shall express only those refinees that appear in that OPD.

**NOTE 4**
Partial folding is equivalent to partial unfolding where the collections of displayed and hidden refinee sets are complementary.

**NOTE 5**
Unfolding reveals finer structural details rather than behaviour, i.e. no transfer of execution control occurs, see **14.2.2**. However, hierarchical dependencies involving procedural links can result in behavioural changes associated with use of the unfolded thing.

---

#### 14.2.1.3 In-zooming and out-zooming

In-zooming shall be a kind of unfolding that combines aggregation-participation and exhibition-characterization with additional semantics. For processes, in-zooming enables modelling the subprocesses, their temporal order, their interactions with objects, and passing of execution control to and from that context. For objects, in-zooming creates a distinct context that enables modelling of the constituent objects’ spatial or logical order.

Graphically, for both in-diagram and new-diagram process in-zooming, the ellipse of the refineable enlarges to accommodate the symbols for the refinees, and the links amongst them, which are within the in-zoom context. In the case of new-diagram in-zooming, the refineable shall have a thick contour in both the more abstract OPD in which the refineable appears without refinees, and in the new more detailed OPD context, in which the refineable appears surrounding the subprocess refinees and attendant objects.

The corresponding process in-zoom OPL sentence shall be:
**Process zooms into Subprocess A, Subprocess B, and Subprocess C, in that sequence.**

**NOTE 1**
In-zooming can be more precisely specified by indicating the abstract OPD name and the more detailed OPD name (see **A.4.7.4**).

The context of an in-zoomed process shall include the subprocesses, which are parts of the in-zoomed process, and possibly internal objects that are attributes of the in-zoomed process. The contextual scope of the in-zoomed process shall be the refineable, its subprocesses, attributes and links as depicted in the OPD.

The execution timeline within the context of an in-zoomed process shall flow from the top of its enlarged process ellipse symbol to the bottom of that ellipse. This timeline shall depict the sequence of subprocess invocations. The vertical arrangement of the top point of the subprocess ellipse symbols

Analogous to process in-zooming, object in-zooming shall expose constituent objects as parts of the in-zoomed object and possibly interim processes that are in-zoomed object operations within the scope of the in-zoomed object context. Unlike in-zooming a process, in-zooming an object does not result in a transfer of execution control. The consequence of new-diagram object in-zooming is a context shift from the object as part of a larger OPD context to the object as the entire OPD context in which the constituent parts of the object are exposed and spatially or logically ordered.

Graphically, the rectangle of the in-zoomed object enlarges to accommodate the symbols for the referees, and the links amongst them. The arrangement of the object rectangles within the context of the in-zoomed object enlarged rectangle shall indicate spatial arrangement or logical order of the objects. This enables ordered enumeration of data, such as in a vector or a matrix.

The corresponding object in-zoom OPL sentence shall be: **Object zooms into Subobject A, Subobject B, and Subobject C, in that sequence.**

**EXAMPLE 1**
**Figure 46** depicts abstract **Processing** in SD, the system diagram, and details of **Processing** in SD1 after zooming into **Processing**, showing its two subprocesses.

[Figure: Two OPD diagrams illustrating a generic example of process in-zooming.
Left diagram (SD): An oval labeled “Processing” connected to rectangles labeled Agent, Instrument, Consumee, Affectee, and Result.
Right diagram (SD1): A large enclosing oval labeled “Processing” containing two inner ovals “A Subprocessing” and “B Subprocessing.” External objects Agent, Instrument, Consumee, Affectee, and Result are linked to these subprocesses. Arrows indicate the relationships between objects and subprocesses and the sequence from A Subprocessing to B Subprocessing.]

**SD**

Agent handles **Processing**.
Processing requires **Instrument**.
Processing consumes **Consumee**.
Processing affects **Affectee**.
Processing yields **Result**.

**SD1**

Processing requires **Instrument**.
Processing affects **Affectee**.
Processing zooms into **A Subprocessing** and **B Subprocessing** in that sequence.
Agent handles **A Subprocessing**.
A Subprocessing consumes **Consumee**.
B Subprocessing yields **Result**.

**Figure 46 — New-diagram in-zooming generic example**

---

**EXAMPLE 2**
**Figure 47** depicts the **Check-Based Paying** process of **Figure 29** with in-zooming to expose the sequence of subprocesses and the allocation of links from the process to its subprocesses.

[Figure: OPD diagram of a “Check-Based Paying” process. Inside a large ellipse labeled “Check-Based Paying” appear four subprocesses: Writing & Signing, Delivering & Accepting, Endorsing & Submitting, and Cashing & Cancelling. External objects include Keeper, Payer, Payee, Bank, and Check. The Check object shows possible states: blank, signed, endorsed, cashed & cancelled. Arrows show relations between the actors and subprocesses and the transformation of the check’s state through the subprocess sequence.]

Check exhibits **Keeper**.
Check can be **blank**, **signed**, **endorsed**, or **cashed & cancelled**.
State **blank** of **Check** is initial.
State **cashed & cancelled** of **Check** is final.
Keeper can be **payer**, **payee**, or **financial institution**.
State **payer** of **Keeper** is initial and final.
Payer Keeper relates to **Payer**.
Payee Keeper relates to **Payee**.
Financial institution Keeper relates to **Bank**.
**Check-Based Paying** zooms into **Writing & Signing**, **Delivering & Accepting**, **Endorsing & Submitting**, and **Cashing & Cancelling**, in that sequence.
Payer handles **Writing & Signing** and **Delivering & Accepting**.
Payee handles **Delivering & Accepting** and **Endorsing & Submitting**.
Bank handles **Cashing & Cancelling**.
**Writing & Signing** changes **Check** from **blank** to **signed**.
**Delivering & Accepting** changes **Keeper** from **payer** to **payee**.
**Endorsing & Submitting** changes **Check** from **signed** to **endorsed** and **Keeper** from **payee** to **financial institution**.
**Cashing & Cancelling** changes **Check** from **endorsed** to **cashed & cancelled** and **Keeper** from **financial institution** to **payer**.

**Figure 47 — Check-Based Paying process with in-zooming to expose its four sequential subprocesses**

---

### 14.2.2 Control (operational) semantics within an in-zoomed process context

#### 14.2.2.1 Implicit invocation link

In-zooming a process shall specify a transfer of execution control to subprocesses at a different extent of detail. Executing a process with an in-zoomed context shall recursively transfer execution control to the top-most subprocess(es) within that process context, which is in a different OPD in case of new-diagram in-zooming. Execution control shall return to the in-zoomed process after its final enabled subprocess completes.

The implicit invocation link shall be an invocation link between a process and an in-zoom subprocess, between two subprocesses within the context of an in-zoomed process, or between an in-zoomed subprocess and its parent process. Similar to its explicit counterpart, the implicit invocation link shall signify the invocation of a subsequent process or concurrently beginning processes.

Upon arriving at an in-zoomed process context, execution control shall immediately transfer to the subprocess(es) with the highest ellipse (oval) top-most point within this process in-zoom context. The implicit invocation link from a process to its top-most in-zoom subprocess transfers execution control. Along the process timeline, the completion of a source subprocess immediately invokes the subsequent subprocess(es) using the implicit invocation link. Upon completion of the subprocess with an ellipse top-most point that is lowest within this in-zoom context, execution control shall return to the in-zoomed process along the implicit invocation link.

Since invocation is an event, satisfaction of the precondition for each subprocess is necessary to allow that subprocess to perform.

When two or more subprocesses have their top-most ellipse points at the same height, then an implicit invocation link shall initiate each process and they shall start in parallel upon individual precondition satisfaction. The process that completes last shall initiate the next process or set of parallel subprocesses.

Graphically, no symbol explicitly denotes the implicit invocation link. The top-to-bottom vertical arrangement of the top-most point of the subprocess ellipse symbols within the context of the in-zoomed process shall denote an implicit invocation link between successive subprocesses in that arrangement.

The syntax of an implicit invocation link OPL sentence shall be: **Process zooms into Subprocess A and Subprocess B, in that sequence.**

**EXAMPLE**
In the OPD on the left hand side of **Figure 48**, **Cleaning** invokes **Coating**, so **Cleaning** affects **Product** first and then **Coating** affects **Product**. The invocation link dictates this process sequence. In the equivalent OPD on the right hand side of **Figure 48**, **Finishing** zooms into **Cleaning** and **Coating**, with the former’s ellipse top point above the latter’s, so when **Finishing** starts, execution control immediately transfers to **Cleaning**, and when **Cleaning** ends, the implicit invocation link invokes **Coating**. The two OPDs are semantically equivalent, except that the one on the left does not have **Finishing** as an enclosing context, making it less expressive from a system viewpoint while using more graphical elements.

[Figure: Two diagrams comparing explicit invocation and implicit invocation.
Left: A Product object connected to two processes Cleaning and Coating; Cleaning invokes Coating.
Right: A larger process Finishing encloses subprocesses Cleaning and Coating arranged vertically, indicating the implicit invocation order.]

Cleaning affects **Product**.
Cleaning invokes **Coating**.
Coating affects **Product**.

Finishing affects **Product**.
Finishing zooms into **Cleaning** and **Coating**, in that sequence.

**Figure 48 — Invocation link (left) and implicit invocation link (right)**

---

#### 14.2.2.2 Implicit parallel invocation link set

Graphically, when the ellipse top points of two or more subprocesses within the scope of an in-zoomed process are at the same height (within possible allowable tolerance), these subprocesses shall begin in parallel, subject to precondition satisfaction for both. In this situation, there is a set of implicit invocation links from the source process of the implicit invocation link to each one of the parallel processes.

The heights of the enclosed subprocesses’ ellipse top points induce a partial order among these subprocesses. Subprocesses whose ellipse top points are at the same height start in parallel. When the last one of these subprocesses ends, i.e., process synchronization occurs, execution control shall attempt to invoke the next subprocess. If there are two or more subprocesses with a lower ellipse-top point at the same height, the execution control invokes them in parallel. If there are no more subprocesses to invoke, execution control returns to the in-zoomed refineable process.

The syntax of the implicit parallel invocation link OPL sentence shall be: **Process zooms into parallel Subprocess A and Subprocess B.**

**EXAMPLE**
**Figure 49** shows subprocesses with the following partial order: A, (B, C), D, (E, F, G). B and C start upon completion of A. D starts upon completion of the longer process from among B and C. E, F, and G start upon completion of D. Execution control returns to Processing upon completion of the longer process from among E, F, and G.

[Figure: Diagram showing process Processing containing seven subprocesses arranged vertically and in parallel groups: A at top, B and C parallel below, D next, and E, F, G parallel at the bottom.]

Processing zooms into **A**, parallel **B** and **C**, **D**, and parallel **E**, **F**, and **G**, in that sequence.

**Figure 49 — Partial subprocesses order and implicit parallel invocation link set**

---

#### 14.2.2.3 Implicit invocation links summary

**Table 24** summarizes the implicit invocation links.

#### Table 24 — Implicit invocation links summary

| Name                                  | Semantics                                                                                                                                                    | Sample OPD & OPL                                                                                                                                                                                                                              | Source                                                                                                                               | Destination                                                                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implicit invocation link              | Upon subprocess completion within the context of an in-zoomed process, the subprocess immediately invokes the one(s) below it.                               | [Figure: Diagram where Product Terminating contains subprocesses Product Finishing and Product Shipping.] Product Terminating zooms into Product Finishing and Product Shipping, in that sequence.                                            | Initiating process, whose ellipse top point is above the initiated process                                                           | Initiated process, whose ellipse top point is below the ellipse top point of the initiating process                                                 |
| Parallel implicit invocation link set | Top: Subprocesses A and B initiate in parallel as soon as Processing starts. Bottom: Subprocesses B and C initiate in parallel as soon as subprocess A ends. | [Figure: Diagram where Processing zooms into parallel A and B.] Processing zooms into parallel A and B. [Figure: Diagram where Processing zooms into A and parallel B and C.] Processing zooms into A and parallel B and C, in that sequence. | Initiating process, whose ellipse top point is above the set of initiated processes, whose ellipse top points are at the same height | A set of initiated processes, whose ellipse top points are at the same height (within tolerance) and below the initiating process ellipse top point |

---

#### 14.2.2.4 Link distribution across context

##### 14.2.2.4.1 Semantics of link distribution

Graphically, a procedural link attached to the contour of an in-zoomed process has distributive semantics. Leaving a link attached to the contour of the in-zoomed process shall mean that the link is distributed and attached to each one of the subprocesses. The contour of the in-zoomed process has semantics analogous to that of algebraic parentheses following a multiplication symbol, which distribute the multiplication operator to the expressions inside the parentheses.

**EXAMPLE 1**
In **Figure 50**, the OPDs on the left and right are equivalent, but the one on the left is clearer and less cluttered. An agent link from **A** to **P** means that **A** handles the subprocesses **P1**, **P2**, and **P3**. An instrument link from **B** to **P** means that the subprocesses **P1**, **P2**, and **P3** require **B**. Analogously in algebra, suppose the agent (or instrument) link was a multiplication operator, **A** was a multiplier and in-zoomed addition, such that **P = P1 + P2 + P3**, and **P** was a multiplicand, then **A * P = A * (P1 + P2 + P3) = A * P1 + A * P2 + A * P3**.

[Figure: Two diagrams illustrating link distribution. Left: object A and B linked to process P containing subprocesses P1, P2, P3. Right: equivalent representation where A and B connect individually to P1, P2, P3.]

A handles **P**.
P requires **B**.
P zooms into **P1**, **P2**, and **P3**, in that sequence.

P zooms into **P1**, **P2**, and **P3**, in that sequence.
A handles **P1**, **P2**, and **P3**.
P1, P2, and P3 require **B**.

**Figure 50 — In-zooming link distribution**

If an enabler connects to the outer contour of an in-zoomed contour it shall connect to at least one of its subprocesses. Consumption and result links shall not be attached to the outer contour of an in-zoomed process because this violates temporal logical conditions. With a distributed consumption link, an attempt would be made to consume an already-consumed object by a subprocess that is not the first to perform. Similarly, a distributed result link would attempt to create an already existing object instance.

**NOTE 1**
The modeller needs to be careful when more than one process creates the same object, i.e. more than one operational instance of the object exists, or more than one process affect or consume the same object. OPM modelling tools need to track the number and identities of operational instances of each object and each process in order to be able to perform simulations.

**EXAMPLE 2**
In **Figure 51** the OPD on the left contains invalid consumption and result links, as annotated in the OPL. The consumption link gives rise to the OPL sentence “P consumes C.” Applying link distribution, the consequence is the three OPL sentences “P1 consumes C.”, “P2 consumes C.”, and “P3 consumes C.” However, since **P1** consumes **C** first according to its temporal order, the same instance of **C** does not exist when **P2** or **P3** performs and therefore **P2** and **P3** cannot consume **C** again. Similarly, the same operational instance of **B** results only once. The OPD on the right depicts valid links by specifying which of the subprocesses of **P** consumes **C** (**P1**) and which one yields **B** (**P2**).

[Figure: Two diagrams illustrating restrictions on distributing consumption and result links. Left: invalid configuration with distributed links causing multiple consumptions or results. Right: corrected configuration specifying which subprocess consumes and which yields.]

A handles **P**.
P requires **D**.
P zooms into **P1**, **P2**, and **P3**, in that sequence.
P consumes **C**. — NOT VALID!
P yields **B**. — NOT VALID!
P3 affects **B**.

A handles **P**.
P requires **D**.
P zooms into **P1**, **P2**, and **P3**, in that sequence.
P1 consumes **C**.
P2 yields **B**.
P3 affects **B**.

**Figure 51 — Link distribution restriction for consumption and result links**

---

Since attaching a consumption or result link to an in-zoomed process is invalid, when a process is in-zoomed, all the consumption and result links that were attached to it shall be attached initially or by default to its first subprocess.

**NOTE 2**
A modelling tool can automatically establish default semantics, which the modeller can modify.

**EXAMPLE 3**
In **Figure 51** as soon as the modeller in-zooms **P** and inserts **P1** into its context, the destination end of the consumption link from **C** migrates from **P** to **P1**. Similarly, the source end of the result link to **B** also migrates from **P** to **P1**. When the modeller adds **P2**, the modeller can migrate the destination end of the consumption link and/or the source end of the result link from **P1** to **P2**, as **Figure 51** shows.

---

##### 14.2.2.4.2 Event and condition link constraint

An event link from a systemic object or state shall not cross the boundary of an in-zoomed process from the outside of that process to initiate any one of its subprocesses at any level, because this amounts to an attempt to interfere with the prescribed temporal order of the synchronous (see 14.2.3.5) in-zoomed process. If the crossing event link emanates from an environmental object or state, the modeller should model how such a contingency is handled.

If the skipped process is within an in-zoom context and there is a subsequent process in this context, execution control initiates that process, otherwise execution control transfers back to the in-zoomed process.

---

##### 14.2.2.4.3 Split state-specified transforming links

When a process that changes an object from an input state to an output state is in-zoomed and contains more than one subprocess, the OPD, either in-diagram or new-diagram, becomes underspecified. To restore specification, the modeller shall attach both the state-specified input link and the state-specified output link to one of the subprocesses in a temporally-feasible manner. Splitting the input-output specified link pair in two shall signify the split state-specified transforming link pair.

Graphically, two links to an object with two or more states connecting across a process contour to different subprocesses with one state-specified input link and one state-specified output link shall denote the split state-specified transforming link.

**EXAMPLE 1**
In **Figure 52** the OPD in the middle in-zooms process **P** from the OPD on the left but is underspecified because **P1** or **P2** could each change **A** from **s1** to **s2**, or **P1** could change **A** from **s1** and **P2** could change **A** to **s2**. The OPD on the right models this last case, giving rise to a new split input link from **s1** of **A** to **P1** and a new split output link from **P2** to **s2**.

[Figure: Three diagrams showing object A with states s1 and s2 interacting with process P and its subprocesses P1 and P2. The rightmost diagram explicitly splits the state-specified transforming links.]

A can be **s1** or **s2**.
P changes **A** from **s1** to **s2**.

A can be **s1** or **s2**.
P zooms into **P1** and **P2**, in that sequence.
P changes **A** from **s1** to **s2**.
— UNDERSPECIFIED!

A can be **s1** or **s2**.
P zooms into **P1** and **P2**, in that sequence.
P1 changes **A** from **s1**.
P2 changes **A** to **s2**.

**Figure 52 — Split state-specified transforming link to resolve under specification**

---

**Table 25** summarizes the split input-output specified effect link pair.

#### Table 25 — Split input-output specified effect link pair summary

| Name                                          | Semantics                                                                                                                                                                         | Sample OPD & OPL                                                                                                                         | Source                                                                                                           | Destination                                                                                                         |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Split input-output specified effect link pair | An early subprocess of an in-zoomed process takes an object out of its input state. A late subprocess of the same in-zoomed process changes the object to be in its output state. | [Figure: Object A with states s1 and s2 connected to subprocesses P1 and P2 within process P.] P1 changes A from s1. P2 changes A to s2. | *The top arrow:* Input state of an affected object. *The bottom arrow:* Late subprocess of an in-zoomed process. | *The top arrow:* Early subprocess of an in-zoomed process. *The bottom arrow:* Output state of the affected object. |

**NOTE 1**
There are no control-link versions of the split input-specified effect link.

**NOTE 2**
An object can have the role of an instrument in an abstract OPD and a transformee in another descendant, more detailed and concrete OPD. At the abstract OPD, the process does not appear to affect the object, because the object’s initial state is the same as its final state. Therefore, at the abstract OPD the object is an instrument, as indicated by an instrument link. However, at a descendant, more concrete OPD, that same process does appear to change the state of that object from the initial state and then back to the initial state.

**EXAMPLE 2**
In **Figure 53** the left SD (**SD: Dish Washing System**), a **Dishwasher** object is an instrument to the **Dish Washing** process, since no change in state of the **Dishwasher** is visible at that extent of abstraction. In the descendent OPD (**SD1: Dish Washing in-zoomed**), **Dish Washing** zooms into **Loading** (of a dirty Dish Set), **Cleaning** (which changes **Dish Set** from dirty to clean), and **Unloading** (of a clean Dish Set). **Loading** changes the state of **Dishwasher** from **empty** to **loaded**, while **Unloading** changes it back from **loaded** to **empty**, so **empty** is both the initial and final state (brown link emphasis). While the **Dishwasher** is an instrument in the SD, at the more detailed descendent OPD, the **Dishwasher** is an affectee—it becomes **loaded** and then **empty** again. The only effect visible in the SD is the effect on **Dish Set**.

[Figure: Two OPD diagrams illustrating dish washing. Left: system diagram showing Dish Washing with objects Dishwasher, Household User, Soap, and Dish Set. Right: in-zoomed diagram where Dish Washing includes subprocesses Dish Loading, Detergent Inserting, Dish Cleaning & Drying, and Dish Unloading, with state changes of Dishwasher, Soap Compartment, and Dish Set.]

**SD: Dish Washing System**

Household User handles **Dish Washing**.
Dish Washing requires **Dishwasher**.
Dish Washing consumes **Soap**.
Dish Washing affects **Dish Set**.

**SD1: Dish Washing in-zoomed**

Dish Washer consists of **Soap Compartment** and other parts.
Dishwasher can be **empty** or **loaded**.
State **empty** of **Dishwasher** is initial and final.
Soap Compartment can be **empty** or **loaded**.
State **empty** of **Soap Compartment** is initial.
Dish Set exhibits **Cleanliness**.
Cleanliness of Dish Set can be **dirty** or **clean**.
State **dirty** of Cleanliness of Dish Set is initial.
State **clean** of Cleanliness of Dish Set is final.
Household User handles **Dish Washing**.
Dish Washing zooms into **Dish Loading**, **Detergent Inserting**, **Dish Cleaning & Drying**, and **Dish Unloading**, in that sequence.

Dish Loading changes **Dishwasher** from **empty** to **loaded**.
Detergent Inserting requires **Soap**.
Detergent Inserting changes **Soap Compartment** from **empty** to **loaded**.
Dish Cleaning & Drying requires **Dishwasher**.
Dish Cleaning & Drying consumes **Soap**.
Dish Cleaning & Drying changes **Cleanliness** of **Dish Set** from **dirty** to **clean**.
Dish Unloading changes **Dishwasher** from **loaded** to **empty**.

**Figure 53 — Role of abstraction with split state transforming links**

---

#### 14.2.2.4 Operational instances of involved object set

As a consequence of link distribution, the following constraints shall apply to operational instances of transformees:

* each consumee operational instance in the preprocess object set of a process shall cease to exist at the beginning of the most detailed subprocess of that process, which consumes the operational instance, and the operational instance is not in the postprocess object set of that process;

* each affectee operational instance in the preprocess object set of a process that changes that operational instance as a consequence of the process performance shall exit from its input state, the state from which it changes, at the beginning of the most detailed subprocess that changes the affectee;

* each affectee operational instance in the postprocess object set of a process that changes that operational instance as a consequence of the process performance shall enter its output state at the completion of the most detailed subprocess that changes the affectee; and

* each result operational instance in the postprocess object set of a process shall begin existence at the completion of the most detailed subprocess that yields the result operational instance and the operational instance is not in the preprocess object set of that process.

---

#### 14.2.2.5 Synchronous vs. asynchronous process refinement

Since the aggregation-participation fundamental structural relation does not prescribe any “partial order” of process performance, the modelling of synchronous process refinement shall use in-zooming.

**EXAMPLE 1**
The system in **Figure 53** is synchronous: there is a fixed, well-defined order of each subprocess within the in-zoom context of **Dish Washing**.

The modelling of asynchronous process refinement shall use the aggregation-participation fundamental structural link either through in-diagram aggregation unfolding or as a new-diagram aggregation unfolding of the process.

**EXAMPLE 2**
**Figure 54** depicts a portion of a **Home Safety System** that carries out the function **Home Safety Maintaining**, which includes the subprocesses **Burglary Handling**, **Fire Protecting**, and **Earthquake Alarming**. Since the order of these three subprocesses is unknown, the OPD uses in-diagram aggregation unfolding with an aggregation-participation link from this function rather than an in-zoomed version of **Home Safety Maintaining**. **Home Safety Maintaining** in-zooms into a recurring systemic process (not shown), **Monitoring & Detecting**, for which **Detection Module** is an instrument and **Threat Appearing** is an environmental process.

[Figure: Diagram of Home Safety Maintaining connected to subprocesses Burglary Handling, Fire Protecting, and Earthquake Alarming, with objects Detection Module and Detected Threat (states burglary, fire, earthquake).]

Home Safety Maintaining consists of **Burglary Handling**, **Fire Protecting**, and **Earthquake Alarming**.
Detection Module exhibits **Detection Threat**.
Detection Threat can be **burglary**, **fire**, or **earthquake**.
Burglary Detected Threat initiates **Burglary Handling**, which requires **burglary Detected Threat**.
Fire Detected Threat initiates **Fire Protecting**, which requires **fire Detected Threat**.
Earthquake Detected Threat initiates **Earthquake Alarming**, which requires **earthquake Detected Threat**.

**Figure 54 — Home Safety Maintaining is an asynchronous system**

#### 14.2.2.6 Expressing the context of a system

##### 14.2.2.6.1 Navigating the contexts of a system

###### 14.2.2.6.1.1 The OPD process tree

An OPD process tree, also called OPD tree, shall be a directed tree graph with root node of SD, the system diagram, and the other OPDs as nodes with their OPD labels. The directed edges of an OPD tree shall have labels with each edge pointing from the parent OPD, which contains the refineable process, to a child OPD containing refines, which elaborates a refineable process in the parent OPD via new-diagram in-zooming for synchronous subprocesses or new-diagram aggregation unfolding for asynchronous subprocesses.

###### 14.2.2.6.1.2 The OPD object tree

Unlike the OPD process tree that has a single root, the OPD object tree is more like a forest of many trees, each stemming from a distinct refineable object that unfolds or in-zooms to reveal detail. Rather than identifying the possible flow of execution control found in the OPD process tree, the OPD object tree shall encapsulate the information about an object as a hierarchic structure. The system execution should maintain dependencies among OPD object tree elements and between OPD object trees.

**NOTE**
OPM tools provide rules for model construction that enforce the maintenance of dependencies during model creation.

###### 14.2.2.6.1.3 OPM diagram labels

The OPM system name shall be the name of the OPM model that specifies the system. An OPD name is the name that identifies each OPD in the OPD process tree.

SD shall be the label designation for the root OPD in the OPD tree hierarchy. This SD occupies tier 0 in the OPD hierarchy tree and shall have exactly one process; higher numbered tiers, i.e. those corresponding to successive refinements, may have one or more processes. SD shall contain one and only one systemic process, which represents the overarching system function that delivers functional value to stakeholders. SD may contain one or more environmental processes.

###### 14.2.2.6.1.4 OPD process tree edge label

Since each elaborated process in an OPD process tree has a unique name, each edge label shall refer to the refinement of that process in another OPD. Each edge in the OPD process tree shall have a label. That label shall express a refinement relation that corresponds to the implicit invocation link or unfolding relation. Considering each OPD to be an object and the entire OPD process tree to be a single OPD, each edge shall be a unidirectional tagged structural link with a tag of “is refined by in-zooming **Refineable Name** in”, or “is refined by unfolding **Refineable Name** in”.

An OPD refinement OPL sentence shall be an OPL sentence describing the refinement relation between a refineable present in a tierₙ OPD and the tierₙ₊₁ refinement OPD.

The syntax of an in-zoomed OPD refinement OPL sentence shall be:
**Tierₙ OPD label is refined by in-zooming Refineable Process Name in Tierₙ₊₁ OPD Label.**

The syntax of an unfolded OPD refinement OPL sentence shall be:
**Tierₙ OPD label is refined by unfolding Refineable Process Name in Tierₙ₊₁ OPD Label.**

**NOTE**
Several OPD of Clause C.6 show the use of edge label syntax.

###### 14.2.2.6.1.5 System map and model views

A system map shall be an OPD process tree that explicitly depicts the element (things and links) content of each OPD (node). Because the system map may become very large and unwieldy, mechanisms shall allow access to model content and the associations among elements. These mechanisms, collectively referred to as model views consisting of model facts, shall include a list of all things and the OPDs in which they appear, the OPD process tree, and the OPD object trees.

In addition, an OPM tool set should provide a mechanism for creating views, as OPDs with associated OPL sentences, of objects and processes that meet specific criteria. These views may include the critical path for minimal system execution duration, or a list of system agents and instruments, or an OPD of objects and processes involved in a specific kind of link or set of links.

**EXAMPLE**
An OPD can be created by

a) refining (unfolding or in-zooming) an object, or

b) collecting and presenting in a new OPD things that appear in various OPDs for expressing assignment of system sub-functions to system-module objects.

---

##### 14.2.2.6.2 Whole System OPL specification

An OPL paragraph shall be the collection of OPL sentences that together specify in text the semantic expression of the corresponding OPD.

**NOTE 1**
An OPL paragraph name, using the OPD name, can precede the first OPL sentence of each OPL paragraph.

An OPM system model shall be the collection of successive OPL paragraphs corresponding to the collection of OPDs present.

An entire OPL specification of a system should begin with an OPL specification starting title. The OPL paragraphs follow the title in successive blocks, each beginning on a new line with the corresponding OPD and the OPL paragraph sentences following.

**NOTE 2**
The sequence of OPL paragraphs generally begins with the SD and follows breadth-first order, unless the modeller identifies a different sequence.

**EXAMPLE**
Table 26 contains the entire OPL specification of the OPM model in Figure 53.

---

### Table 26 — Whole system OPL for Dish Washing System

**OPL specification of Dish Washing System**

**SD: Dish Washing System**

Household User handles Dish Washing.
Dish Washing requires Dishwasher.
Dish Washing consumes Soap.
Dish Washing affects Dish Set.

SD is refined by in-zooming Dish Washing in SD1.

**SD1: Dish Washing in-zoomed**

Dish Washer consists of Soap Compartment and other parts.
Dishwasher can be empty or loaded.

State empty of Dishwasher is initial and final.

Soap Compartment can be empty or loaded.

State empty of Soap Compartment is initial.

Dish Set exhibits Cleanliness.

Cleanliness of Dish Set can be dirty or clean.

State dirty of Cleanliness of Dish Set is initial.
State clean of Cleanliness of Dish Set is final.

Household User handles Dish Washing.

Dish Washing zooms into Dish Loading, Detergent Inserting, Dish Cleaning & Drying, and Dish Unloading, in that sequence.

Dish Loading changes Dishwasher from empty to loaded.

Detergent Inserting requires Soap.

Detergent Inserting changes Soap Compartment from empty to loaded.

Dish Cleaning & Drying requires Dishwasher.

Dish Cleaning & Drying consumes Soap.

Dish Cleaning & Drying changes Cleanliness of Dish Set from dirty to clean.

Dish Unloading changes Dishwasher from loaded to empty.

End of OPL specification of Dish Washing System

---

### 14.2.3 OPM fact consistency principle

The fact consistency OPM principle stipulates that:

a) a model fact appearing in one OPD shall be true for the entire collection of OPDs within the OPM system model, and

b) no OPD in the OPD process tree or an OPD object tree shall contain a model fact that contradicts a model fact in the same OPD or in another OPD.

A fact in one OPD may be a refinement or an abstraction of a fact in a different OPD within the same OPM system model.

**NOTE**
This principle does not preclude the possibility of representing any model element any number of times in as many OPDs as the modeller wishes. Since a link cannot exist without the things it links, if a link is present then the two things on its ends need to be present as well.

**EXAMPLE**
It is not possible for one OPD to express the fact that “P yields A.” and for the same or another OPD in the same OPD tree to express the fact that “P consumes A.” However, it is permissible for one OPD to express the fact that “P affects A.” and for another OPD in the same OPD tree to express the fact that “P changes A from s1 to s2.” because the latter fact is a refinement, not a contradiction of the former.

---

### 14.2.4 Abstraction ambiguity resolution for procedural links

#### 14.2.4.1 Abstraction and procedural link precedence

Out-zooming abstracts a collection of related things, the refinees and associated links, into a refineable. When the modeller performs the abstraction, the procedural links between refinees and things that are not refinees, shall migrate to the context of the OPD that depicts the refineable. This migration may cause a situation in which two or more procedural links of different kinds link an object and a process. According to the procedural link uniqueness OPM principle (see 8.1.2) an object or an object state shall link to a process by only one procedural link. To sustain this principle, the modeller shall resolve the conflict between candidate links to determine which link remains or which new link replaces the candidates in the abstract OPD. The loss of detail information is consistent with the notion of abstraction.

**EXAMPLE**
Figure 55 demonstrates the problem of procedural link abstraction. In SD1, the result link from P1 to B is more significant than the effect link from P2 to B, so when SD1 is out-zoomed to SD, the result link prevails.

[Figure: Diagram illustrating abstraction of procedural links. The left diagram labeled SD1 shows object B linked to processes P1 and P2 within a larger process P. During “Out-zooming,” these internal processes collapse into process P. The resulting diagram (SD) shows object B connected to process P by a single link, representing the prevailing procedural relation.]

**Figure 55 — Abstracting procedural links**

Semantic strength and link precedence are two concepts to guide the determination of which links to retain and which to hide when an OPD is out-zoomed or folded.

Semantic strength of a procedural link shall be the significance of the information that the link carries. Information concerning a change in existence, either creation or elimination, is more significant than information about change to an existing thing. The relative semantic strength of the two conflicting procedural links shall determine link precedence. When two or more procedural links compete to remain represented in an OPD abstraction of refinement, the link that prevails is the one with the highest semantic strength.

**NOTE**
The concept of link precedence allows the modeller to resolve conflicts in representation amongst OPD contexts and guides the modeller in establishing appropriate procedural links at the various extents of detail.

---

#### 14.2.4.2 Precedence among transforming links

Transforming links include result, effect, and consumption links. Since object creation and consumption are semantically stronger, i.e. they have higher semantic strength than affecting the object by changing its state, result and consumption links have precedence over effect links, as demonstrated in Figure 55. However, since result and consumption links are semantically equivalent, when they compete, the prevailing link shall be the effect link because the effect link can be thought of as implicitly changing an object from its existent state to its non-existent state, or vice-versa.

Table 27 shows transforming link precedence: P in the upper left corner is out-zoomed. The column headings show the three possible transforming links between P1 and B, while the row headings show the three possible links between P2 and B. The table cells show the prevailing link between B and P after P is out-zoomed.

| Zoomed-in process P | B-to-P1 Link                            | B-to-P1 Link                                     | B-to-P1 Link                                   |
| ------------------- | --------------------------------------- | ------------------------------------------------ | ---------------------------------------------- |
|                     | [Figure: object B linked to process P1] | [Figure: object B linked downward to process P1] | [Figure: object B linked upward to process P1] |
| B-to-P2 Link        | [Figure: link representation]           | Invalid                                          | [Figure: link representation]                  |
| B-to-P2 Link        | [Figure: link representation]           | Invalid                                          | [Figure: link representation]                  |
| B-to-P2 Link        | Invalid                                 | [Figure: link representation]                    | Invalid                                        |

**Table 27 — Transforming link precedence: Resolving conflicts between effect, result, and consumption links**

---

#### 14.2.4.3 Precedence among transforming and enabling links

Transforming links are semantically stronger than enabling links, because transforming links denote creation, consumption, or change of the linked object, while the enabling links only denote enablement. A transforming link shall have precedence over an enabling link as shown in Figure 56.

Within the enabling links, an agent link shall have precedence over an instrument link because in artificial systems the humans are central to the process, and they need to ensure the system’s proper operation. In addition, wherever there is human interaction, an interface should exist and this information should be available to the modeller of a refineable so that they can plan accordingly.

[Figure: Diagram showing SD1 with object B connected to internal processes P1 and P2 inside process P. During “Out-zooming,” the diagram simplifies to SD where object B connects directly to process P with a single prevailing link.]

**Figure 56 — Link precedence for transforming and enabling links**

Summarizing the semantic strength of the procedural non-control links, the primary order of precedence shall be:
consumption = result > effect > agent > instrument, where the = and > refer to the semantic strength of the links. State-specified links shall have higher precedence than basic links that do not specify states.

---

#### 14.2.4.4 Secondary precedence among same-kind non-control links and control links

Almost every non-control link kind has a corresponding event and condition link that is useful for determining finer, secondary precedence distinction within each kind of procedural link. The relative semantic strength for the secondary order of precedence within each member of the primary order of precedence shall have the event link of stronger semantic strength than its corresponding non-control link, while the condition link shall have a weaker semantic strength than its corresponding non-control link.

The semantic strength of an event link shall be stronger than the semantic strength of its corresponding non-control link because any event link has semantics of both its corresponding non-control link plus the event capable of initiating a process. The semantic strength of a condition link shall be weaker than the semantic strength of its corresponding non-control link because the condition modifier weakens the precondition satisfaction criteria for the connecting process.

---

#### 14.2.4.5 Summary of the procedural links semantic strength

Summarizing the semantic strength of the procedural links based on the distinction between primary and secondary precedence, the complete order of precedence shall be as follows:

1. consumption event > consumption
2. consumption = result
3. result > consumption condition
4. consumption condition > effect event
5. effect event > effect
6. effect > effect condition
7. effect condition > agent event
8. agent event > agent
9. agent > agent condition
10. agent condition > instrument event
11. instrument event > instrument
12. instrument > instrument condition

---

## Annex A (normative)

## OPL formal syntax in EBNF

## A.1 General

OPL is a subset of English that shall express textually the OPM specification that the OPD set expresses graphically.

OPL is a dual-purpose language. First, it serves domain experts and system architects engaged in analysing and designing a system, such as an electronic commerce system or a Web-based enterprise resource planning system. Second, it provides a firm basis for automatically generating the designed application.

OPL is the textual counterpart of the graphic OPM system specification, corresponding to the diagrammatic description in the OPD set. OPL shall be an automatically generated textual description of the system in a subset of natural English. Devoid of the idiosyncrasies and excessive cryptic details that characterize programming languages, OPL sentences shall be understandable to people without technical or programming experience.

Because of the extensive variety in model expression enabled by OPM, the OPL syntax expression in EBNF below is necessarily incomplete, e.g. the opportunities for statements regarding probability in 12.7 and execution path management in Clause 13 are lacking EBNF expressions. The enormous variety of participation constraints, especially those expressible as mathematical formulas, do not have formal specification in this annex.

## A.2 OPL in the context of OPD

This annex provides a formal specification of the OPL conforming to ISO/IEC 14977:1996, which results from the various OPD graphical constructions found in Clauses 7 to 14. To aid the reader, this annex references the corresponding OPD subclauses where appropriate and clause/subclause headings help to partition the EBNF according to syntactic forms for modelling elements.

## A.3 Preliminaries

### A.3.1 EBNF syntax

The following syntax uses the notation of EBNF as described in ISO/IEC 14977:1996. The normal character representing each operator of Extended BNF and its implied precedence shall be (highest precedence at the top):

* `*` repetition-symbol
* `-` except-symbol
* `,` concatenate-symbol
* `|` definition-separator-symbol
* `=` defining-symbol
* `;` terminator-symbol

The normal precedence shall be over-ridden by the following bracket pairs:

* `( start-group-symbol end-group-symbol )`
* `[ start-option-symbol end-option-symbol ]`
* `{ start-repeat-symbol end-repeat-symbol }`
* `? special-sequence-symbol ?`

**NOTE 1**
A space character enclosed in quotes as in `" "` denotes that a literal space character is required, otherwise space characters and line endings (so-called white space) have no significance.

**NOTE 2**
A meta identifier can occur on both the left and right sides of a rule, so enabling recursion.

**NOTE 3**
The first-quote-symbol identifies syntactic elements of OPL variable labels, which are the names and values appearing in OPD graphical models and OPL sentences. These particular syntactic elements are found only in A.3.2.

**NOTE 4**
The second-quote-symbol identifies syntactic elements of OPL constants, which are words and phrases appearing in OPL sentences as interpretations of the graphical element configurations and link tags in an OPD.

**NOTE 5**
Beginning with A.3.2 and through the remainder of Annex A, all text, except headings, conform to ISO/IEC 14977:1996.

---

### A.3.2 Base declarations

```
(* Region OPL EBNF *)
(* Region Base declarations: The following base declarations define certain strings: *)

non zero digit = '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' ;
decimal digit = '0' | non zero digit ;
positive integer = non zero digit, {decimal digit} ;
positive real number = {decimal digit}, ".", decimal digit, {decimal digit} ;

upper case letter = 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M'
| 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' ;

lower case letter = 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm'
| 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' ;

letter = upper case letter | lower case letter ;

string character = letter | decimal digit | '-' | '|' | '&' | '/' | ' ' ;

name = letter, {string character} ;
capitalized word = upper case letter {string character} ;
non capitalized word = lower case letter {string character} ;

non capitalized phrase =
    non capitalized word,
    { " ", (non capitalized word | capitalized word) } ;

type identifier =
      "boolean"
    | "string"
    | number type
    | "enumerated" ;

prefix = "unsigned" ;

number type =
      [prefix], "integer"
    | "float"
    | "double"
    | "short"
    | "long" ;

participation limit = positive integer | positive real number ;

participation constraint =
      lower single
    | upper single
    | lower plural
    | upper plural
    | ( "0" | participation limit, [ " to ", participation limit ] ) ;

expression constraint =
    " where ", name,
    ( ( logical operation, value name )
    | ( logical begin set,
        ( name | value name ),
        { ",", ( name | value name ) },
        logical end set ) ) ;

lower single = "a" | "an" | "an optional" | "at least one" ;
upper single = "A" | "An" | "An optional" | "At least one" ;
lower plural = "optional" | "many" ;
upper plural = "Optional" | "Many" ;

range clause =
      " is ", value name
    | " ranges from ", value name, " to ", value name ;

logical operation = "=" | "<" | ">" | "<=" | ">=" ;
logical begin set = " in {" ;
logical end set = "}" ;

(* EndRegion: Base declarations *)
```

---

### A.3.3 OPL special sequences

```
(* Region: special sequences – This region defines all special sequences like New Line, Plural objects and processes *)

new line = ? application specific character sequence resulting in a line feed followed by return to first character position on the line ? ;

measurement unit = ? any specified or commonly understood measurement of time, space, quantity, or quality ? ;

value name = ? a number or name appropriate for the associated measurement unit ? ;

singular object name = ? capitalized singular noun phrase ? ;
plural object name = ? capitalized plural noun phrase ? ;

singular process name =
      ? capitalized gerund phrase ?
    | ? capitalized singular noun phrase ? ;

plural process name =
      ? capitalized gerund phrase ?
    | ? capitalized plural noun phrase ? ;

parent OPD = ? OPD from which a new-diagram in-zooming or new diagram unfolding occurs ? ;
child OPD = ? OPD resulting from a new-diagram in-zooming or new diagram unfolding ? ;

max duration time units =
      ? value of maximum duration in time units for process execution ? ;

min duration time units =
      ? value of minimum duration in time units for process execution ? ;

(* EndRegion: Special Sequences *)
```

---

## A.4 OPL Syntax

### A.4.1 OPL document structure

```
(* Region OPL document *)

OPL paragraph = OPL sentence, { new line, OPL sentence } ;

OPL sentence = OPL formal sentence, "." ;

OPL formal sentence =
      thing description sentence
    | procedural sentence
    | structural sentence
    | context management sentence ;
```

### A.4.2 OPL Identifiers

```
(* Region: Identifiers – This region defines all identifiers used throughout the grammar *)

object identifier =
      singular object name, [ " in ", measurement unit ], [ range clause ]
    | singular object name, " object", [ " in ", measurement unit ], [ range clause ]
    | plural object name, " in ", measurement unit, [ range clause ]
    | plural object name, " objects", [ " in ", measurement unit ], [ range clause ] ;

process identifier =
      singular process name
    | singular process name, " process"
    | plural process name
    | plural process name, " processes" ;

thing identifier =
      object identifier
    | process identifier ;

state identifier = non capitalized word ;

tag expression = non capitalized phrase ;

(* EndRegion: Identifiers *)
```

---

### A.4.3 OPL lists

```
(* Region: Lists – This region defines various lists: object list, process list, object with optional state list *)

process list =
      process identifier
    | process identifier, { ",", process identifier }, " and ", process identifier ;

process Or list =
      process identifier
    | process identifier, { ",", process identifier }, " or ", process identifier ;

process Xor list at beginning = "One of ", process Or list ;
process Xor list at end = "one of", process Or list ;

object list =
      object identifier
    | object identifier, { ",", object identifier }, " and ", object identifier ;

object with optional state =
      [ state identifier, " " ], object identifier ;

object with optional state list =
      object with optional state
    | object with optional state, { ",", object with optional state }, " and ", object with optional state ;

object Or list =
      object with optional state
    | object with optional state, { ",", object with optional state }, " or ", object with optional state ;

object Or list nostates =
      object identifier
    | object identifier, { ",", object identifier }, " or ", object identifier ;

object Xor list at beginning = "One of ", object Or list ;
object Xor list at end = "one of", object Or list ;
object nostate Xor list at end = "one of", object list ;

state list =
      state identifier
    | state identifier, { ",", state identifier }, " and ", state identifier ;

state Or list =
      state identifier
    | state identifier, { ",", state identifier }, " or ", state identifier ;

state Xor list at end = "one of", state Or list ;

(* EndRegion: Lists *)
```

---

### A.4.4 OPL Thing description

#### A.4.4.1 Thing description sentence

```
(* Region: Thing Description – This region defines all thing description sentences *)

thing description sentence =
      generic property sentence
    | type description sentence
    | state description sentence ;
```

#### A.4.4.2 Generic property sentence

```
generic property sentence =
      thing identifier,
      " is ",
      [ essence ],
      [ affiliation ],
      [ perseverance ] ;

essence = "Informatical" | "Physical" ;
```

(*Physical is the non-default value of Essence, the default value of which is Informatical.*)

affiliation = "Systemic" | "Environmental" ;
(*Environmental is the non-default value of Affiliation, the default value of which is Systemic.*)

perseverance = "Persistent" | "Transient" ;
(*Transient is the non-default value of Perseverance, the default value of which is Persistent.*)

---

#### A.4.4.3 Type description sentence

type description sentence = object identifier, " is of type ", type identifier ;

---

#### A.4.4.4 State description sentence

state description sentence = state enum sentence
| initial states sentence
| final states sentence
| default state sentence
| combined state sentence ;

state enum sentence = object identifier, " is ", state identifier
| object identifier, " can be ", state identifier, [{", ", state identifier}], " and ", state identifier
| object identifier, " can be ", state identifier, [{", ", state identifier}], ", and other states" ;

initial states sentence = single initial states sentence
| multiple initial states sentence ;

single initial states sentence = "State ", state identifier, " of ", object identifier, " is initial" ;

multiple initial states sentence = "States ", state list " of ", object identifier, " are initial" ;

final states sentence = single final state sentence
| multiple final state sentence ;

single final state sentence = "State ", state identifier, " of ", object identifier, " is final" ;

multiple final state sentence = "States ", state list, " of ", object identifier, " are final" ;

default state sentence = "State ", state identifier, " of ", object identifier, " is default" ;

combined state sentence = object identifier, " is initially ", state identifier | state identifier,
[{ " and ", state identifier }], and finally ", state OR list ;

input state = state identifier ;
(*the state or states of the associated object in a process precondition set*)

output state = state identifier ;
(*the state or states of the associated object in a process postcondition set*)

active process identifier = process identifier ;

(*EndRegion: Thing Description*)

---

### A.4.5 OPL Procedural sentences

#### A.4.5.1 Procedural sentence

(*Region: Procedural sentences – This region defines all procedural sentences*)

procedural sentence = transforming sentence
| enabling sentence
| control sentence ;

---

#### A.4.5.2 OPL Transformations

##### A.4.5.2.1 Transforming sentence

(*Region: Transforming sentences – This region defines consumption, result, effect and change sentences, and their variations*)

transforming sentence = consumption sentence
| result sentence
| effect sentence
| change sentence ;

---

##### A.4.5.2.2 Consumption sentence

consumption sentence = ( process identifier, " consumes ", object with optional state list )
| consumption select sentence ;

consumption select sentence = consumption Or sentence
| consumption Xor sentence ;

consumption Or sentence = consumption source Or sentence
| consumption destination Or sentence ;

consumption source Or sentence = process identifier, " consumes at least one of ", object Or list ;

consumption destination Or sentence = "At least one of ", process Or list, " consumes ", object with optional state ;

consumption Xor sentence = consumption source Xor sentence
| consumption destination Xor sentence ;

consumption source Xor sentence = process identifier, " consumes exactly ", object Xor list at end ;

consumption destination Xor sentence = "Exactly ", process Xor list at end, " consumes ", object with optional state ;

---

##### A.4.5.2.3 Result sentence

result sentence = ( process identifier, " yields ", object with optional state list )
| result select sentence ;

result select sentence = result Or sentence
| result Xor sentence ;

result Or sentence = result source Or sentence
| result destination Or sentence ;

result source Or sentence = "At least one of ", process Or list, " yields ", object with optional state ;

result destination Or sentence = process identifier, " yields at least one of ", object Or list ;

result Xor sentence = result source Xor sentence
| result destination Xor sentence ;

result source Xor sentence = "Exactly ", process Xor list at end, " yields ", object with optional state ;

result destination Xor sentence = process identifier, " yields exactly ", object Xor list at end ;

---

##### A.4.5.2.4 Effect sentence

effect sentence = ( process identifier, " affects ", object list )
| effect select sentence ;

effect select sentence = effect Or sentence
| effect Xor sentence ;

effect Or sentence = effect object Or sentence
| effect process Or sentence ;

effect object Or sentence = process identifier, " affects at least one of ", object Or list nostates ;

effect process Or sentence = "At least one of ", process Or list, " affects ", object identifier ;

effect Xor sentence = effect object Xor sentence
| effect process Xor sentence ;

effect object Xor sentence = process identifier, " affects exactly ", object nostates Xor list at end ;

effect process Xor sentence = "Exactly ", process Xor list at end, " affects ", object identifier ;

---

##### A.4.5.2.5 Change sentence

change sentence = in out specified change sentence
| input specified change sentence
| output specified change sentence ;

---

in out specified change sentence = ( process identifier, " changes ", in out object change list )
| in out specified change select sentence ;

in out object change list = in out object change phrase
| in out object change phrase, [{", ", in out object change phrase}],
" and ", in out object change phrase ;

in out object change phrase = object identifier, " from ", input state, " to ", output state ;

in out specified change select sentence = in out specified change Or sentence
| in out specified change Xor sentence ;

in out specified change Or sentence = ( process identifier, " changes ", Or in out object change list )
| ( process Or list, " changes ", in out object change phrase )
| in out specified change state Or sentence ;

Or in out object change list = in out object change phrase, [{", ", in out object change phrase}],
" or ", in out object change phrase ;

in out specified change state Or sentence = ( process identifier, " changes ", object identifier,
" from ", state Or list, " to ", state identifier )
| ( process identifier, " changes ", object identifier,
" from ", state identifier, " to ", state Or list ) ;

in out specified change Xor sentence = in out specified change object Xor sentence
| in out specified change process Xor sentence ;

in out specified change object Xor sentence = process identifier, " changes one of ", Or in out object change list ;

in out specified change process Xor sentence = process Xor list at beginning, " changes ", in out object change phrase ;

in out specified change state Xor sentence = ( process identifier, " changes ", object identifier,
" from ", state Xor list at end, " to ", state identifier )
| ( process identifier, " changes ", object identifier, " from ", state identifier, " to ", state Xor list at end ) ;

---

input specified change sentence = ( process identifier, " changes ", input object change list )
| input specified change select sentence ;

input object change phrase = object identifier, " from ", input state ;

input object change list = input object change phrase
| input object change phrase, [{", ", input object change phrase}],
" and ", input object change phrase ;

input specified change select sentence = input specified change Or sentence
| input specified change Xor sentence ;

input specified change Or sentence = ( process identifier, " changes ", Or input object change list )
| ( process Or list, " changes ", input object change phrase )
| ( process identifier, " changes ", object identifier, " from ", state Or list ) ;

Or input object change list = input object change phrase, [{", ", input object change phrase}],
" or ", input object change phrase ;

input specified change Xor sentence = ( process identifier, " changes one of ", Or input object change list )
| ( process Xor list at beginning, " changes ", input object change phrase )
| ( process identifier, " changes ", object identifier, " from ", state Xor list at end ) ;

---

output specified change sentence = ( process identifier, " changes ", output object change list )
| output specified change select sentence ;

output object change list = output object change phrase
| output object change phrase, [{", ", output object change phrase}],
" and ", output object change phrase ;

output object change phrase = object identifier, " to ", output state ;

output specified change select sentence = output specified change Or sentence
| output specified change Xor sentence ;

output specified change Or sentence = ( process identifier, " changes ", Or output object change list )
| ( process Or list, " changes ", output object change phrase )
| ( process identifier, " changes ", object identifier, " to ", state Or list ) ;

output specified change Xor sentence = ( process identifier, " changes one of ", Or output object change list )
| ( process Xor list at beginning, " changes ", output object change phrase )
| ( process identifier, " changes ", object identifier, " to ", state Xor list at end ) ;

(*EndRegion: Transforming sentences*)

---

#### A.4.5.3 OPL Enablers

##### A.4.5.3.1 Enabling sentences

(*Region: Enabling sentences – This region defines Agent and Instrument sentences and their possible variations*)

enabling sentence = agent sentence
| instrument sentence ;

---

##### A.4.5.3.2 Agent sentence

agent sentence = ( object with optional state list, " handle ", process identifier )
| agent select sentence ;

agent select sentence = agent Or sentence
| agent Xor sentence ;

agent Or sentence = agent source Or sentence
| agent destination Or sentence ;

agent source Or sentence = "At least one of ", object Or list, "handles ", process identifier ;

agent destination Or sentence = object with optional state, " handles at least one of ", process Or list ;

agent Xor sentence = agent source Xor sentence
| agent destination Xor sentence ;

agent source Xor sentence = "Exactly ", object Xor list at end, " handles ", process identifier ;

agent destination Xor sentence = object with optional state, " handles exactly ", process Xor list at end ;

---

##### A.4.5.3.3 Instrument sentence

instrument sentence = ( process identifier, " requires ", object with optional state list )
| instrument select sentence ;

instrument select sentence = instrument Or sentence
| instrument Xor sentence ;

instrument Or sentence = instrument source Or sentence
| instrument destination Or sentence ;

instrument source Or sentence = process identifier, " requires at least one of ", object Or list ;

instrument destination Or sentence = "At least one of ", process Or list, " requires ", object with optional state ;

instrument Xor sentence = instrument source Xor sentence
| instrument destination Xor sentence ;

instrument source Xor sentence = process identifier, " requires exactly ", object Xor list at end ;

instrument destination Xor sentence = "Exactly ", process Xor list at end, " requires ", object with optional state ;

(*EndRegion: Enabling sentences*)

---

#### A.4.5.4 OPL Flow of control

##### A.4.5.4.1 Control sentence

(*Region: Control sentences – This region defines all sentences related to flow of control in the system*)

control sentence = event sentence
| condition sentence
| invocation sentence
| exception sentence ;

---

##### A.4.5.4.2 Event sentence

event sentence = consumption event sentence
| effect event sentence
| agent event sentence
| instrument event sentence ;

consumption event sentence = object with optional state, " initiates ", process identifier,
", which consumes ", object identifier ;

effect event sentence = simple effect event sentence
| in out specified effect event sentence
| input specified effect event sentence
| output specified effect event sentence ;

simple effect event sentence = object identifier, " initiates ", process identifier, ", which affects ", object identifier ;

in out specified effect event sentence = input state, object identifier, " initiates ", process identifier,
", which changes ", in out object change phrase ;

input specified effect event sentence = input state, object identifier, " initiates ", process identifier,
", which changes ", object identifier, " from ", input state ;

output specified effect event sentence = object identifier, " in any state initiates ", process identifier,
", which changes ", object identifier, " to ", output state ;

agent event sentence = object with optional state, " initiates and handles ", process identifier ;

instrument event sentence = object with optional state, " initiates ", process identifier,
", which requires ", object with optional state ;

---

##### A.4.5.4.3 Condition sentence

condition sentence = condition transforming sentence
| condition enabling sentence ;

condition transforming sentence = conditional consumption sentence
| conditional state specified consumption sentence
| conditional effect sentence ;

conditional consumption sentence = ( process identifier, " occurs if ", object identifier,
" exists, in which case ", object identifier, " is consumed, otherwise ", process identifier, " is skipped " )
| ( "If ", object identifier, " exists then ", process identifier, " occurs and consumes ", object identifier,
", otherwise bypass ", process identifier ) ;

conditional state specified consumption sentence = ( process identifier, " occurs if ", object identifier,
" is ", input state, ", in which case ", object identifier, " is consumed, otherwise ", process identifier, " is skipped " )
| ( "If ", input state, object identifier, " exists then ", process identifier,
" occurs and consumes ", object identifier, ", otherwise bypass ", process identifier ) ;

conditional effect sentence = simple conditional effect sentence
| in out specified conditional effect sentence
| input specified conditional effect sentence
| output specified conditional effect sentence ;

simple conditional effect sentence = ( process identifier, " occurs if ", object identifier,
" exists, in which case ", process identifier, " affects ", object identifier,
", otherwise ", process identifier, " is skipped " )
| ( "If ", object identifier, " exists then ", process identifier,
" occurs and affects ", object identifier, ", otherwise bypass ", process identifier ) ;

in out specified conditional effect sentence = ( process identifier, " occurs if there is ",
input state, object identifier, ", in which case ", process identifier,
" changes ", in out object change phrase, ", else ", process identifier, " is skipped " )
| ( process identifier, " occurs if there is ", input state, object identifier,
", in which case ", process identifier, " changes ", in out object change phrase,
", otherwise bypass ", process identifier ) ;

input specified conditional effect sentence = ( process identifier, " occurs if there is ",
input state, object identifier, ", in which case ", process identifier,
" changes ", object identifier, " from ", input state, ", else ", process identifier, " is skipped " )
| ( process identifier, " occurs if there is ", input state, object identifier,
", in which case ", process identifier, " changes ", object identifier, " from ", input state,
", otherwise bypass ", process identifier ) ;

output specified conditional effect sentence = ( process identifier, " occurs if ", object identifier,
" exists, in which case ", process identifier, " changes ", object identifier, " to ", output state,
", otherwise ", process identifier, " is skipped " )
| ( process identifier, " occurs if ", object identifier, " exists, in which case ", process identifier,
" changes ", object identifier, " to ", output state, ", otherwise bypass ", process identifier ) ;

condition enabling sentence = conditional agent sentence
| conditional instrument sentence ;

conditional agent sentence = ( process identifier, " occurs if ", object with optional state,
" exists, else ", process identifier, " is skipped " )
| ( process identifier, " occurs if ", object with optional state,
" exists, else bypass ", process identifier ) ;

conditional instrument sentence = ( process identifier, " occurs if ", object with optional state,
" exists, else ", process identifier, " is skipped " )
| ( process identifier, " occurs if ", object with optional state,
" exists, else bypass ", process identifier ) ;

---

##### A.4.5.4.4 Invocation sentence

invocation sentence = ( process identifier, " invokes ", process list )
| ( process identifier, " invokes itself " )
| invocation select sentence ;

invocation select sentence = invocation Or sentence
| invocation Xor sentence ;

invocation Or sentence = ( "At least one of ", process Or list, " invokes ", process identifier )
| ( process identifier, " invokes at least one of ", process Or list ) ;

invocation Xor sentence = ( "Exactly one of ", process Or list, " invokes ", process identifier )
| ( process identifier, " invokes exactly ", process Xor list at end ) ;

---

##### A.4.5.4.5 Exception sentence

exception sentence = overtime exception sentence
| undertime exception sentence ;

overtime exception sentence = active process identifier,
" occurs if duration of ", process identifier, " exceeds ", max duration time units ;

undertime exception sentence = active process identifier,
" occurs if duration of ", process identifier, " falls short of ", min duration time units ;

(*EndRegion: Control sentences*)

(*EndRegion: Procedural sentences*)

---

### A.4.6 OPL Structural sentences

#### A.4.6.1 Structural sentence

(*Region: Structural sentences – This region defines all sentences that connect things in static, time-independent, long-lasting relations*)

structural sentence = tagged structural sentence
| aggregation sentence
| characterization sentence
| exhibition sentence
| specialization sentence
| instantiation sentence ;

---

#### A.4.6.2 OPL tagged structures

##### A.4.6.2.1 Tagged structural sentence

tagged structural sentence = unidirectional tagged structural sentence
| bidirectional tagged structural sentence ;

---

##### A.4.6.2.2 Unidirectional tagged structural sentence

unidirectional tagged structural sentence = single link unidirectional tagged sentence
| forked tagged structural sentence ;

single link unidirectional tagged sentence = nullTag unidirectional object tagged structural sentence
| nullTag unidirectional process tagged structural sentence
| non nullTag unidirectional object tagged structural sentence
| non nullTag unidirectional process tagged structural sentence ;

nullTag unidirectional object tagged structural sentence =
[participation constraint, " "], source object, uniDirNullTag,
[participation constraint, " "], destination object ;

nullTag unidirectional process tagged structural sentence =
[participation constraint, " "], source process, uniDirNullTag,
[participation constraint, " "], destination process ;

non nullTag unidirectional object tagged structural sentence =
[participation constraint, " "], source object, " ", forward tag, " ",
[participation constraint, " "], destination object, [expression constraint] ;

non nullTag unidirectional process tagged structural sentence =
[participation constraint, " "], source process, " ", forward tag, " ",
[participation constraint, " "], destination process ;

forked tagged structural sentence = forked nullTag object tagged structural sentence
| forked nullTag process tagged structural sentence
| forked non nullTag object tagged structural sentence
| forked non nullTag process tagged structural sentence ;

forked nullTag object tagged structural sentence =
[participation constraint, " "], source object, uniDirNullTag, object tine set ;

forked nullTag process tagged structural sentence =
[participation constraint, " "], source process, uniDirNullTag, process tine set ;

forked non nullTag object tagged structural sentence =
[participation constraint, " "], source object, " ", forward tag, " ", object tine set ;

forked non nullTag process tagged structural sentence =
[participation constraint, " "], source process, " ", forward tag, " ", process tine set ;

object tine set = tine object
| ( tine object, [{", ", tine object}], " and ", (tine object | "more") ),
[( ", ordered by ", order criteria ) [( ", in that sequence" )]] ;

process tine set = tine process
| ( tine process, [{", ", tine process}], " and ", (tine process | "more") ),
[( ", ordered by ", order criteria ) [( ", in that sequence" )]] ;

order criteria = name ;

tine object = [ participation constraint, " " ], object with optional state ;

source object = object with optional state ;

destination object = object with optional state ;

tine process = [ participation constraint, " " ], process identifier ;

source process = process identifier ;

destination process = process identifier ;

uniDirNullTag = " relates to "
| " relate to "
| user defined uniDirNullTag ;

forward tag = tag expression ;

user defined uniDirNullTag = tag expression ;

---

##### A.4.6.2.3 Bidirectional tagged structural sentences

bidirectional tagged structural sentence = asymmetric bidirectional object tagged structural sentence
| asymmetric bidirectional process tagged structural sentence
| symmetric bidirectional object tagged structural sentence
| symmetric bidirectional process tagged structural sentence ;

asymmetric bidirectional object tagged structural sentence =
( [ participation constraint, " " ], source object, bidir forward tag,
[ participation constraint, " " ], destination object, [expression constraint] )
| ( [ participation constraint, " " ], destination object, bidir backward tag,
[ participation constraint, " " ], source object, [expression constraint] ) ;

asymmetric bidirectional process tagged structural sentence =
( [ participation constraint, " " ], source process, bidir forward tag,
[ participation constraint, " " ], destination process )
| ( [ participation constraint, " " ], destination process, bidir backward tag,
[ participation constraint, " " ], source process ) ;

symmetric bidirectional object tagged structural sentence =
( [ participation constraint, " " ], source object, " and ",
[ participation constraint, " " ], destination object, " are ", biDirNullTag ) ;

symmetric bidirectional process tagged structural sentence =
( [ participation constraint, " " ], source process, " and ",
[ participation constraint, " " ], destination process, " are ", biDirNullTag ) ;

symmetric tag = tag expression ;
bidir forward tag = tag expression ;
bidir backward tag = tag expression ;

biDirNullTag = " related "
| user defined biDirNullTag ;

user defined biDirNullTag = tag expression ;

---

#### A.4.6.3 OPL fundamental structures

##### A.4.6.3.1 Aggregation sentences

aggregation sentence = object forked aggregation sentence
| process forked aggregation sentence ;

object forked aggregation sentence = whole object, " consists of ", object parts list ;

process forked aggregation sentence = whole process, " consists of ", process parts list ;

object parts list = part object
| ( part object, [{", ", part object}], " and ", ( part object | " at least one other part" ) ) ;

process parts list = part process
| ( part process, [{", ", part process}], " and ", ( part process | " at least one other part" ) ) ;

whole object = object identifier ;
part object = [participation constraint, " "], object identifier ;

whole process = process identifier ;
part process = [participation constraint, " "], process identifier ;

---

##### A.4.6.3.2 Characterization sentences

characterization sentence = object forked characterization sentence
| process forked characterization sentence ;

object forked characterization sentence = basic object forked characterization sentence
| partial object forked characterization sentence
| AsWellAs object forked characterization sentence
| partial AsWellAs object forked characterization sentence ;

basic object forked characterization sentence = object identifier, " exhibits ", ( attribute list | operator list ) ;

partial object forked characterization sentence = object identifier, " exhibits ",
( ( attribute list, " and at least one other attribute" )
| ( operator list, " and at least one other operator" ) ) ;

AsWellAs object forked characterization sentence = object identifier, " exhibits ",
attribute list, ", as well as ", operator list ;

partial AsWellAs object forked characterization sentence = object identifier, " exhibits ",
attribute list, ", and at least one other attribute", ", as well as ", operator list,
", and at least one other operator" ;

attribute = object identifier ;
operator = process identifier ;

attribute list = object list ;
operator list = process list ;

process forked characterization sentence = basic process forked characterization sentence
| partial process forked characterization sentence
| AsWellAs process forked characterization sentence ;

basic process forked characterization sentence = process identifier, " exhibits ", ( operator list | attribute list ) ;

partial process forked characterization sentence = process identifier, " exhibits ",
( ( operator list, " and at least one other operator" )
| ( attribute list, " and at least one other attribute" ) ) ;

AsWellAs process forked characterization sentence = process identifier, " exhibits ",
operator list, ", as well as ", attribute list ;

partial AsWellAs process forked characterization sentence = process identifier, " exhibits ",
operator list, ", and at least one other operator", ", as well as ", attribute list,
", and at least one other attribute" ;

---

#### A.4.6.4 Exhibition sentences

exhibition sentence = object exhibition sentence
| process exhibition sentence ;

object exhibition sentence = feature, " of ", object identifier,
( range clause | " is ", ( ( attribute list | operator list )
| ( attribute list, " as well as ", operator list ) ) ) ;

process exhibition sentence = feature, " of ", process identifier, " is ",
( ( operator list | object list ) | ( operator list, " as well as ", attribute list ) ) ;

feature = attribute | operator ;

---

#### A.4.6.5 Specialization sentences

specialization sentence = object specialization sentence
| process specialization sentence
| state specialization sentence ;

object specialization sentence = basic object specialization sentence
| multiple object specialization sentence
| partial object specialization sentence
| Xor object specialization sentence
| multiple object inheritance specialization sentence ;

basic object specialization sentence = special object, " is a ", general object ;

multiple object specialization sentence = special object list, " are ", general object ;

partial object specialization sentence = special object list,
" and other specializations are ", general object ;

Xor object specialization sentence = basic Xor object specialization sentence
| comma separated Xor object specialization sentence ;

basic Xor object specialization sentence = special object,
" can be either ", general object, " or ", general object ;

comma separated Xor object specialization sentence = special object,
" can be one of ", general object, {", ", general object}, " or ", general object ;

multiple object inheritance specialization sentence = special object, " is ", general object list ;

general object = object identifier ;
special object = object identifier ;

general object list = "a ", object identifier, [{ " a ", object identifier }], " and a ", object identifier ;

special object list = object list ;

process specialization sentence = basic process specialization sentence
| multiple process specialization sentence
| partial process specialization sentence
| Xor process specialization sentence
| multiple process inheritance specialization sentence ;

basic process specialization sentence = special process, " is ", general process ;

multiple process specialization sentence = special process list, " are ", general process ;

partial process specialization sentence = special process list,
" and other specializations are ", general process ;

Xor process specialization sentence = basic Xor process specialization sentence
| comma separated Xor process specialization sentence ;

basic Xor process specialization sentence = special process,
" can be either ", general process, " or ", general process ;

comma separated Xor process specialization sentence = special process,
" can be one of ", general process, {", ", general process}, " or ", general process ;

multiple process inheritance specialization sentence = special process, " is ", general process list ;

general process = process identifier ;
special process = process identifier ;

general process list = "a ", process identifier, [{ " a ", process identifier }], " and a ", process identifier ;

special process list = process list ;

state specialization sentence = basic state specialization sentence
| multiple state specialization sentence
| partial state specialization sentence ;

basic state specialization sentence = state specified object, " is a ", state specified object ;

multiple state specialization sentence = state specified object list, " are ", state specified object ;

partial state specialization sentence = state specified object list,
" and other specializations are ", state specified object ;

state specified object = state identifier, " ", object identifier ;  
state specified object list = state specified object  
| state specified object, [{ ", ", state specified object }], ", and ", state specified object ;

---

#### A.4.6.6 Instantiation sentences

instantiation sentence = object instantiation sentence  
| process instantiation sentence ;  

(*see 10.3.5*)

object instantiation sentence = basic object instantiation sentence  
| multiple object instantiation sentence ;  

basic object instantiation sentence = instance object, " is an instance of ", object class ;  

multiple object instantiation sentence = instance object list, " are instances of ", object class ;  

process instantiation sentence = basic process instantiation sentence  
| multiple process instantiation sentence ;  

basic process instantiation sentence = instance process, " is an instance of ", process class ;  

multiple process instantiation sentence = instance process list, " are an instance of ", process class ;  

instance object = object identifier ;  
instance process = process identifier ;  
object class = object identifier ;  
process class = process identifier ;  
instance object list = object list ;  
instance process list = process list ;

(*EndRegion: Structural sentences*)

---

### A.4.7 OPL Context management

#### A.4.7.1 Context management sentence

(*Region: Context management sentences - This region defines all sentences that manage OPD context shifts*)

context management sentence = unfolding sentence  
| folding sentence  
| in Zooming sentence  
| out Zooming sentence ;

(*see 14.2.1*)

(*in diagram object and process unfolding are equivalent to corresponding structural sentences*)

---

#### A.4.7.2 Unfolding sentences

unfolding sentence = object unfolding sentence  
| process unfolding sentence ;

object unfolding sentence = underspecified object unfolding sentence  
| whole object unfolding sentence  
| general object unfolding sentence  
| class object unfolding sentence  
| exhibitor object unfolding sentence ;

underspecified object unfolding sentence = object identifier, " unfolds into ", attribute list, [", as well as ", operator list ] ;

whole object unfolding sentence = whole object, " from ", parent OPD, " part-unfolds in ", child OPD, " into ", object parts list ;

general object unfolding sentence = general object, " from ", parent OPD, " specialization-unfolds in ", child OPD, " into ", special object list ;

class object unfolding sentence = object class, " from ", parent OPD, " instance-unfolds in ", child OPD, " into ", instance object list ;

exhibitor object unfolding sentence = object identifier, " from ", parent OPD, " feature-unfolds in ", child OPD, " into ", attribute list, [", as well as ", operator list ] ;

process unfolding sentence = underspecified process unfolding sentence  
| whole process unfolding sentence  
| general process unfolding sentence  
| class process unfolding sentence  
| exhibitor process unfolding sentence ;

underspecified process unfolding sentence = process identifier, " unfolds into ", operator list, [", as well as ", attribute list ] ;

whole process unfolding sentence = whole process, " from ", parent OPD, " part-unfolds in ", child OPD, " into ", process parts list ;

general process unfolding sentence = general process, " from ", parent OPD, " specialization-unfolds in ", child OPD, " into ", special process list ;

class process unfolding sentence = process class, " from ", parent OPD, " instance-unfolds in ", child OPD, " into ", instance process list ;

exhibitor process unfolding sentence = process identifier, " from ", parent OPD, " feature-unfolds in ", child OPD, " into ", operator list, [", as well as ", attribute list ] ;

---

#### A.4.7.3 Folding sentences

folding sentence = object folding sentence  
| process folding sentence ;

(*a folding sentence is only relevant for an OPD object or process for which unfolding produces a child OPD and is the OPL equivalent to the graphical bold contour designation*)

object folding sentence = object identifier, " is folding of ", child OPD ;  

process folding sentence = process identifier, " is folding of ", child OPD ;

---

#### A.4.7.4 In zoom sentence

in zooming sentence = process in zoom sentence  
| object in zoom sentence ;

process in zoom sentence = in diagram process in zoom sentence  
| new diagram process in zoom sentence ;

in diagram process in zoom sentence =  
( process identifier, " zooms into ", process list, " in that sequence", [", as well as ", object in zoom list ] )  
| ( process identifier, " zooms into parallel ", process list, [", as well as ", object in zoom list ] )  
| ( process identifier, " zooms into ", process list, " and parallel ", process list, " in that sequence", [", as well as ", object in zoom list ] ) ;

new diagram process in zoom sentence =  
( process identifier, " from ", parent OPD, " zooms in ", child OPD, " into ", process list, " in that sequence", [", as well as ", object in zoom list ] )  
| ( process identifier, " from ", parent OPD, " zooms in ", child OPD, " into parallel ", process list, [", as well as ", object in zoom list ] )  
| ( process identifier, " from ", parent OPD, " zooms in ", child OPD, " into ", process list, " and parallel ", process list, " in that sequence", [", as well as ", object in zoom list ] ) ;

object in zoom sentence = in diagram object in zoom sentence  
| new diagram object in zoom sentence ;

in diagram object in zoom sentence = ( object identifier, " zooms into ", object list, " in that sequence", [", as well as ", process in zoom list ] ) ;

new diagram object in zoom sentence = ( object identifier, " from ", parent OPD, " zooms in ", child OPD, " into ", object list, " in that sequence", [", as well as ", process in zoom list ] ) ;

object in zoom list = object identifier, [{ ", ", object identifier }], ", and ", object identifier, " in that sequence" ;

process in zoom list = process identifier, [{ ", ", process identifier }], ", and ", process identifier, " in that sequence" ;

---

#### A.4.7.5 Out zooming sentence

out zooming sentence = process out zoom sentence  
| object out zoom sentence ;

(*an out zoom sentence is only relevant for an OPD process or object for which in zooming produces a child OPD and is the OPL equivalent to the graphical bold contour designation*)

process out Zoom sentence = process identifier, " is out zoom from ", child OPD ;  

object out Zoom sentence = object identifier, " is out zoom from ", child OPD ;

(*EndRegion: Context management sentences*)

(*EndRegion: OPL document*)

(*EndRegion: OPL EBNF*)

---

## Annex B (informative)

## Guidance for OPM

## B.1 General

In view of the rapid development of complex and complicated systems, the need for an intuitive yet formal way of documenting standards for and designs of new systems, or knowledge about existing systems becomes ever more apparent. This need, in turn, requires a solid infrastructure for recording, storing, arranging, and presenting the accumulated knowledge and the creative ideas that build on this knowledge.

Conceptual modelling refers to the practice of representing system-related knowledge. The outcome of this activity is a conceptual model. Conceptual modelling, which usually precedes mathematical and physical modelling, is the primary activity required not only for engineering systems to be understood, designed, and managed, but also for authoring standards that are as complete and as coherent as possible. Modelling is essential and gives rise to model-based systems engineering (MBSE).

Understanding physical, biological, artificial, and social systems and devising standards related to them requires a well-founded, formal, yet intuitive methodology and language that is capable of modelling these complexities in a coherent, straightforward manner. The same modelling paradigm, the heart of the methodology, should serve for both designing new systems and for studying and improving existing systems. The paradigm should apply to artificial as well as natural systems, and faithfully represent physical and informatical things of the modelled domain. OPM provides the means to address these aspirations.

---

## B.2 Thing importance OPM principle

Major system-level processes can be as important as, or even more important than objects in the system model. In particular, OPM specifies that the top-level process of an OPM model of a system is the system's function, the value-providing process that embodies the system's purpose and use. Hence, a process needs to be amenable for modelling independent of any particular set of objects involved in its occurrence.

The relative importance of a thing T in an OPM system model is generally proportional to the highest OPD in the OPD hierarchy where T appears.

---

## B.3 What a new OPD should contain

A good OPD set is readable and easy to follow and comprehend. The following rules of thumb are helpful in deciding when to create a new OPD and ways to keep OPDs as easy to read and grasp as possible:

— the OPD should not stretch over more than one page or one average-size monitor screen;  

— the OPD should not contain more than 20–25 things;  

— things should not occlude each other, i.e. they are either completely contained within higher-level things, e.g. in case of zooming, or have no overlapping area;  

— the diagram should not contain too many links – roughly the same as the number of things;  

— a link should not cross the area occupied by a thing; and  

— the number of links crossing each other should be minimized.

---

## B.4 The element representation OPM principle

An OPM model element appearing in one OPD may appear in any other OPD as the same element. This principle allows the possibility of representing any model element (thing or link) any number of times in as many OPDs as the modeller finds useful. Since a link cannot exist without the things it links, for a link to appear in an OPD, the two things that it links need to be present as well.

Although a modeller may include any number of things in any OPD, for reasons of clarity and clutter avoidance, it is often highly desirable to include in an OPD only those elements that are necessary to grasp a certain aspect or view of the system.

---

## B.5 The multiple thing copies convention

To avoid long and winding links that cross from one side of the OPD to another and clutter it, an OPD may contain multiple copies of the same thing. This multiple thing copies convention complements the element representation OPM principle. Just as an OPM model element appearing in one OPD may appear in any OPD, an OPM element may appear more than once in any OPD. Accordingly, for the sake of avoiding OPD clutter by long, crisscrossing links, a thing may appear at another place in the same OPD using a shorter link. To facilitate recognition of the repetition, the modeller may replace thing symbol by a corresponding duplicate thing symbol – a small object or process slightly showing behind the repeated thing as illustrated in Figure B.1. However, the modeller should use this alternative sparingly as it requires the model reader to notice and keep in mind the longer links that do not appear explicitly in the current OPD context.

[Figure: Diagram illustrating duplicate object and duplicate process symbols. On the left side, a rectangle labeled "Duplicate Object" connected via a triangular link to an oval process labeled "Copying." On the right side, two oval processes labeled "Copying" and "Photocopying" connected to a rectangle labeled "Duplicate Object." The diagram demonstrates how duplicate symbols represent repeated elements to avoid long crossing links.]

---

## B.6 Naming guidelines

### B.6.1 Importance of name selection

Selecting appropriate labelling names for OPM model elements, i.e. the objects, processes, and links, is important because the labels affect the ease of communication to and comprehension of the model by the intended audience and the logical flow and sense-making of the corresponding OPL sentences.

---

### B.6.2 Object naming

A name for an object should be singular. Convert plural names to a singular form. The recommended way to convert an object with several members is to add the word “Set” (usually for inanimate objects) or “Group” (usually for humans) after the singular form.

**EXAMPLE 1**

“Ingredients” (say, of a cake) becomes “Ingredient Set”, while “Customers” becomes “Customer Group”.

Because object names need to be unique within the system model, the modeller may use the name of a refineable as a prefix for its refine names or may use the name of the refineable as a suffix preceded by “of” after the refine name. Either of these naming schemes allows contextual distinctions when referring to refinees with similar semantics.

Object names may be phrases with more than one word, as in Apple Cake or Automobile Crash.

**EXAMPLE 2**

If a modeller wants **Size** as an attribute of both **Clock Set** and **Watch Set**, then to distinguish between the two Size attributes the former can be **Clock Set Size** and the latter **Watch Set Size** or the former can be **Size of Clock Set** and the latter **Size of Watch Set**.

NOTE 1  
An implementation of OPM can notify the modeller when an attempt to include an object as a refinee in more than one context occurs so that the modeller can determine the appropriateness of the inclusion.

NOTE 2  
An implementation can establish a default syntax to resolve refinee names.

---

### B.6.3 Process naming

A process name is a phrase whose last word should be the gerund form of a verb, i.e. a verb with the “ing” suffix. If there are several choices, such as in Construction vs. Constructing, the latter is preferable.

The following variations for process naming exist:

— the verb version, which is simply the gerund form of the verb, namely verb + ing, as in **Making** or **Responding**;

— the noun-verb version, which is a concatenation of a noun (an OPM object) with the gerund, namely noun + verb + ing, as in **Cake Making** or **Crash Responding**;

— the adjective-verb version, which is a concatenation of an adjective with the gerund form of the verb, namely adjective + verb + ing, as in **Quick Making** or **Automated Responding**; and

— the adjective-noun-verb version, which is a concatenation of an adjective with a noun with the gerund, namely adjective + noun + verb + ing, as in **Quick Cake Making** or **Automatic Crash Responding**.

In the latter cases, the adjective qualifies the process (the gerund, which is a noun). However, the adjective may also qualify the object (the noun), as in **Sweet Cake Making** or **Fatal Crash Responding**.

The name of the function, as well as the names of all OPM processes, should consist of no more than four capitalized words ending with a gerund verb form, e.g. **Large City Population Securing**.

Because process names need to be unique, the modeller may use the name of a refineable as a suffix preceded by “of” after the refine name. The naming scheme allows contextualized distinctions when referring to refinees with similar semantics.

---

### B.6.4 State naming

The names of states should reflect the various relevant situations in which their “owning” object can occur at any given point in time. Preferred state names are passive forms of the owning object rather than the gerund form.

**EXAMPLE**

If a **Product** is painted and then inspected, its states need to be **painted** and **inspected**, rather than **painting** and **inspecting**. **Painting** is the process that changes **Product** from its **unpainted** to its **painted** state, and **Inspecting** changes **Product** from its **painted** state to its **inspected** state. While **Painting** of the **Product** occurs, it has left its **unpainted** state for as long as **Painting** takes place and it is in transition between states and has not yet entered its **painted** state until **Painting** is complete.

---

### B.6.5 Capitalization convention

In OPM the first letter of each word in the name of a thing (object or process) is capitalized, while the name of an object state or a link is not capitalized. This convention helps to produce OPL sentences that are more readable.

---

## Annex C (informative)

## Modelling OPM using OPM

## C.1 OPM models of OPM

The OPD in **Figure C.1** represents aspects of OPM as OPM models. **Clause C.4** elaborates specific elements. **Clause C.5** presents a model relating to the treatment of links during unfolding and in-zooming. **Clause C.6** presents a model for evaluating process invocation, performance, and completion.

This set of clauses expresses OPM as a set of OPD together with the corresponding OPL. For this presentation, the modeller has chosen to limit the model contents to relatively simple OPM usage, i.e. compound links are minimal and there is no attempt to unify the individual OPD into a single OPM model. However, some advanced OPL expressions that limit the redundancy of text and aid in clarifying otherwise distinct but related model facts do occur.

---

## C.2 OPM model structure

[Figure: Diagram showing the hierarchical structure of an OPM model. At the top, "OPM Model" specifies "System." Beneath it are parallel graphical and textual hierarchies. The graphical side includes "OPD Set," "OPD," "OPD Construct," "Link Set," "Link," "Thing Set," and "Thing." The textual side includes "OPL Spec," "OPL Paragraph," "OPL Sentence," "Phrase," "Reserved Phrase," and "Word." Relationships indicate that graphical constructs specify textual ones and vice versa, establishing correspondence between diagrammatic and linguistic model representations.]

**OPM Model specifies System.**  
**OPM Model consists of OPD Set and OPL Spec.**  
**OPL Spec consists of at least one OPL Paragraph.**  
**OPD Set consists of at least one OPD.**  
**OPD Set graphically specifies OPL Spec.**  
**OPL Spec textually specifies OPD Set.**  
**OPD consists of at least one OPD Construct.**  
**OPL Paragraph consists of at least one OPL Sentence.**  
**OPD graphically specifies OPL Paragraph.**  
**OPL Paragraph textually specifies OPD.**  
**OPD Construct graphically specifies OPL Sentence.**  
**OPL Sentence textually specifies OPD Construct.**  
**OPD Construct consists of Thing Set and Link Set.**  
**Thing Set consists of two to many Things.**  
**Link Set consists of at least one Link.**  
**Thing exhibits Name.**  
**OPL Sentence consists of three to many Phrases and at least one Punctuation Mark.**  
**Phrase consists of at least one Word.**  
**OPL Reserved Phrase and Name of Thing are Phrases.**  
**Link graphically specifies Reserved Phrase.**  
**Reserved Phrase textually specifies Link.**  
**Thing can be in-zoomed to create OPD.**

---

### Figure C.1 — OPM model structure

Figure C.1 is a model of the structure of an OPM model that depicts the conceptual aspects of OPM as parallel hierarchies of the graphic and textual OPM modalities and their correspondence to produce equivalent model expressions. An OPD Construct is the graphical expression of the corresponding textual OPL Sentence, which expresses the same model fact. An OPD and its corresponding OPL Paragraph are collections of model facts that a modeller places into the same model context.

---

## C.3 OPD Construct model

Figure C.2 elaborates the OPD Construct concept. The purpose of this model is to distinguish Basic Construct from another possible OPD Construct. A Basic Construct is a specialization of OPD Construct, which consists of exactly two Things connected by exactly one Link. The non-basic constructs include, among others, those with link fans or more than two refinees.

**EXAMPLE 1**

In **Figure C.1**, the two objects **OPM Model** and **OPD Set** together with the aggregation-participation link from the former to the latter constitute a basic construct. The OPL sentence that is equivalent to this basic construct is: **OPM Model consists of OPD Set.**

**EXAMPLE 2**

In **Figure C.1**, the three objects **OPM Model**, **OPD Set**, and **OPL Spec** together with the aggregation-participation link from **OPM Model** to **OPD Set** and **OPL Spec** constitute a compound construct. The OPL sentence that is equivalent to this basic construct is: **OPM Model consists of OPD Set and OPL Spec.**

**NOTE**

An object-state link is implicit between an object and each one of its states. Graphically, this link expression occurs by placing the state inside the object rectangle, effectively linking the state with the object. Therefore, an object with two or more states is an **OPD Construct**, and an object with one state is a **Basic Construct**. A stateless object is not a construct at all, as it has not even an implicit link.

---

[Figure: Diagram illustrating the OPD Construct and Basic Construct relationship. The diagram shows OPD Construct consisting of Thing Set and Link Set. Thing Set contains two or more Things, and Link Set contains at least one Link. A Basic Construct is shown as a specific OPD Construct with exactly two Things and one Link, and constraints on the sizes of the Thing Set and Link Set.]

**OPD Construct consists of Thing Set and Link Set.**  
**Thing and Link are Elements.**  
**Thing Set consists of 2 to many Things.**  
**Link Set consists of at least one Link.**  
**Thing Set exhibits Size of Thing Set.**  
**Link Set exhibits Size of Link Set.**  
**Size of Thing Set can be 2 or >=3.**  
**Size of Link Set can be 1 or >=2.**  
**Basic Construct is an OPD Construct.**  
**Basic Construct exhibits 1 Size of Link Set.**  
**Basic Construct exhibits 2 Size of Thing Set.**

---

### Figure C.2 — Model of OPD Construct and Basic Construct

In some situations, the syntax of two constructs combine easily into a compound OPL sentence that reduces redundancy in the text as shown in the next model variation for OPD Construct.

A modeller could add a process to the model of **Figure C.2** to indicate that the OPD Construct exhibits **Connecting** as shown in **Figure C.3**. By adding states **disconnected** and **connected** of **Thing Set**, the purpose of the model thus includes the action of transforming a **disconnected Thing Set** to a **connected Thing Set** using the **Link Set** as an instrument of connection.

## Figure C.3 — OPD Construct and Basic Construct construction

[Figure: Diagram illustrating the **OPD Construct** structure and its relationship to **Basic Construct**, **Link Set**, **Thing Set**, **Cardinality**, and **Connecting**.
The central element is *Connecting*, represented as a process connecting two states (*disconnected* → *connected*) within a *Thing Set*.
An **OPD Construct** consists of a **Link Set** and a **Thing Set**.
The **Link Set** contains one or more **Link** elements.
The **Thing Set** contains multiple **Thing** elements.
Cardinality constraints appear below both sets (for Link Set: `1` or `>=2`; for Thing Set: `2` or `>=3`).
Both **Link** and **Thing** are specializations of **Element**.
Arrows and inheritance triangles show structural relationships between constructs and sets.]

**OPD Construct** consists of **Link Set** and **Thing Set**.
**OPD Construct** exhibits **Connecting**.
**Link Set** consists of at least one **Link**.
**Link Set** exhibits **Cardinality**.
**Cardinality** of **Link Set** can be 1 or >=2.
**Thing Set** exhibits **Cardinality**.
**Thing Set** consists of 2 to many **Things**.
**Cardinality** of **Thing Set** can be 2 or >=3.
**Link** and **Thing** are **Elements**.
**Connecting** requires **Link Set**.
**Connecting** changes **Thing Set** from **disconnected** to **connected**.
State **disconnected** of **Thing Set** is **initial**.
State **connected** of **Thing Set** is **final**.
**Basic Construct** is an **OPD Construct**.
**Basic Construct** exhibits **1 Cardinality of Link Set** and **2 Cardinality of Thing Set**.

---

## C.4 OPM Element models

The model in **Figure C.4** is only valid for basic constructs because **Link connects 2 Things and not more than two**.

---

## Figure C.4 — OPM model of OPM Element

[Figure: Structural diagram defining the **Element** hierarchy and the relationship between **Thing** and **Link**.
A **Link** connects exactly two **Things** and is composed of **Source**, **Destination**, and **Connector**.
The **Connector** is composed of **Line**, **Symbol**, optional **Tag**, and optional **Path Label**.
Multiplicity is represented with symbols (`?`, `*`, `+`, or none) corresponding to lower and upper bounds (`0..1`, `0..*`, `1..1`, `1..*`).
Inheritance triangles illustrate that Source and Destination are **Linked Things**, which are themselves **Things**.]

**Thing** and **Link** are **Elements**.
**Link** connects **2 Things**.
**Link** consists of **Source**, **Destination**, and **Connector**.
**Connector** consists of **Line**, **Symbol**, an optional **Tag**, and an optional **Path Label**.
**Tag** and **Path Label** are **Phrases**.
**Source** and **Destination** are **Linked Things**.
**Linked Thing** is a **Thing**.
**Linked Thing** exhibits **Symbol** and **Multiplicity**.
**Multiplicity** exhibits **Symbol** and **Lower&Upper Bound**.
**Lower&Upper Bound** can be **0..1**, **0..***, **1..1**, or **1..***.
**Lower&Upper Bound** is by default **1..1**.
**Symbol of Multiplicity** can be **?**, *****, **NONE**, or **+**.
**? Symbol of Multiplicity** denotes **0..1 Lower&Upper Bound**.
*** Symbol of Multiplicity** denotes **0..* Lower&Upper Bound**.
**NONE Symbol of Multiplicity** denotes **1..1 Lower&Upper Bound**.
**+ Symbol of Multiplicity** denotes **1..* Lower&Upper Bound**.

---

## Figure C.5 — OPM model of Thing

[Figure: Diagram showing the specialization of **Thing** into **Process** and **Object**.
Objects may have a **State Set** describing their possible states.
Objects may be **Stateless** (no states) or **Stateful** (with one or more states).
Stateful objects generate **State-Specific Objects**, each associated with a particular state.]

**Process** and **Object** are **Things**.
**Object** exhibits **State Set**.
**State Set** exhibits **Size**.
**Cardinality of State Set** can be **s=0** or **s>=1**.
**State Set** consists of optional **States**.
**Current State** is a **State**.
**Stateless Object** and **Stateful Object** are **Objects**.
**Stateless Object** exhibits **s=0 Size of State Set**.
**Stateful Object** exhibits **s>=1 Size of State Set**.
**Stateful Object** represents **s State-Specific Objects**.
**State-Specific Object Set** consists of **s State-Specific Objects**.
**State-Specific Object** refers to **State**.

---

## Figure C.6 — Example of state-specific object

[Figure: Example diagram centered on **Product** and its states.
Five state-specific specializations of Product are shown: **Designed Product**, **Manufactured Product**, **Tested Product**, **Purchased Product**, and **Used Product**.
Each refers to a corresponding state of Product (designed, manufactured, tested, purchased, used).
All are grouped in a **State-Specific Product Set** derived from Product.]

**Product** can be **designed**, **manufactured**, **tested**, **purchased**, or **used**.
**Product** derives **State-Specific Product Set**.
**State-Specific Product Set** consists of **5 State-Specific Products**.
**State-Specific Product** is a **Product**.
**State-Specific Product** refers to the **current state of Product**.
**Designed Product**, **Manufactured Product**, **Tested Product**, **Purchased Product**, and **Used Product** are **State-Specific Products**.
**Designed Product** refers to **Product’s state designed**.
**Manufactured Product** refers to **Product’s state manufactured**.
**Tested Product** refers to **Product’s state tested**.
**Purchased Product** refers to **Product’s state purchased**.
**Used Product** refers to **Product’s state used**.

---

## Figure C.7 — OPM model of stateful object and state

[Figure: Diagram showing a **Stateful Object** connected to a **State Set** composed of **States**.
States may be designated as **Initial**, **Final**, or **Default**.
Symbols indicate different visual representations of these states (e.g., bold-contour rountangle for initial state, double-contour rountangle for final state).]

**Stateful Object** exhibits **State Set**.
**State Set** consists of at least one **State**, optional **Initial States**, optional **Final States**, and an optional **Default State**.
**State** exhibits **Designation** and **Symbol**.
**Designation** can be **initial**, **final**, or **default**.
**Initial State**, **Final State**, and **Default State** are **States**.
**Initial State** exhibits **initial Designation** and **bold-contour rountangle Symbol of State**.
**Final State** exhibits **final Designation** and **double-contour rountangle Symbol of State**.
**Default State** exhibits **default Designation** and **rountangle pointed to by open arrow Symbol of State**.

---

## Figure C.8 — OPM model of links

[Figure: Hierarchical model of link types.
A **Link** connects two **Things** and contains a **Linked Pair** describing the relationship type.
Links are divided into **Structural Link** and **Procedural Link**.
Structural links include Object-Object Link, Object-State Link, and State-State Link.
Procedural links include Process-Object Link, Process-State Link, and Process-Process Link.]

**Thing** and **Link** are **Elements**.
**Link** connects **2 Things**.
**Link** exhibits **Linked Pair**.
**Linked Pair** consists of **2 Things**.
**Linked Pair** can be **object-object**, **object-state**, **state-state**, **process-object**, **process-state**, or **process-process**.
**Structural Link** and **Procedural Link** are **Links**.
**Object-Object Link** and **State-State Link** are **Structural Links**.
**Object-State Link** is an **Object-Object Link**.
**Object-Object Link** exhibits **object-object Linked Pair**.
**Object-State Link** exhibits **object-state Linked Pair**.
**State-State Link** exhibits **state-state Linked Pair**.
**Process-Object Link** and **Process-Process Link** are **Procedural Links**.
**Process-State Link** is a **Process-Object Link**.
**Process-Object Link** exhibits **process-object Linked Pair**.
**Process-State Link** exhibits **process-state Linked Pair**.
**Process-Process Link** exhibits **process-process Linked Pair**.

---

## Figure C.9 — OPM model of Thing generic properties

[Figure: Diagram describing generic properties of **Thing**: **Perseverance**, **Essence**, and **Affiliation**.
Perseverance differentiates **Object** (persistent) from **Process** (transient).
Essence differentiates **Physical** vs **Informatical** entities.
Affiliation differentiates **Systemic** vs **Environmental** entities.]

**Thing** exhibits **Perseverance**, **Essence**, and **Affiliation**.
**Perseverance** can be **transient** or **persistent**.
**Essence** can be **physical** or **informatical**.
**Affiliation** can be **systemic** or **environmental**.
**Object** and **Process** are **Things**.
**Process** exhibits **transient Perseverance**.
**Object** exhibits **persistent Perseverance**.
**Physical Process**, **Informatical Process**, **Systemic Process**, and **Environmental Process** are **Processes**.
**Physical Object**, **Informatical Object**, **Systemic Object**, and **Environmental Object** are **Objects**.
**Physical Process** and **Physical Object** exhibit **physical Essence**.
**Informatical Process** and **Informatical Object** exhibit **informatical Essence**.
**Systemic Process** and **Systemic Object** exhibit **systemic Affiliation**.
**Environmental Process** and **Environmental Object** exhibit **environmental Affiliation**.

---

## Figure C.10 — OPM model of Thing symbolic representation

[Figure: Diagram explaining the graphical symbol of **Thing**, composed of **Shape**, **Depth**, and **Contour**.
Processes use ellipse shapes while objects use rectangles.
Depth indicates shading (shaded vs flat).
Contour indicates line style (solid vs dashed).]

**Thing** exhibits **Symbol**.
**Symbol of Thing** consists of **Shape**, **Depth**, and **Contour**.
**Shape** can be **ellipse** or **rectangle**.
**Depth** can be **shaded** or **non-shaded**.
**Contour** can be **solid** or **dashed**.
**Process** and **Object** are **Things**.
**Process** exhibits **ellipse Shape**.
**Object** exhibits **rectangle Shape**.
**Physical Process**, **Informatical Process**, **Systemic Process**, and **Environmental Process** are **Processes**.
**Physical Object**, **Informatical Object**, **Systemic Object**, and **Environmental Object** are **Objects**.
**Physical Process** and **Physical Object** exhibit **shaded Depth**.
**Informatical Process** and **Informatical Object** exhibit **flat Depth**.
**Systemic Process** and **Systemic Object** exhibit **solid Contour**.
**Environmental Process** and **Environmental Object** exhibit **dashed Contour**.

---

## Figure C.11 — OPM model of the eight Thing symbol representations

[Figure: Diagram enumerating the eight possible graphical combinations of Thing symbols based on the Cartesian product of Shape (ellipse/rectangle), Depth (shaded/non-shaded), and Contour (solid/dashed).]

**Thing** exhibits **Symbol**.
**Symbol of Thing** consists of **Depth**, **Contour**, and **Shape**.
**Symbol of Thing** can be **shaded dashed rectangle**, **shaded solid ellipse**, **non-shaded dashed ellipse**, **non-shaded solid ellipse**, **non-shaded solid rectangle**, **non-shaded dashed rectangle**, **shaded solid rectangle**, or **shaded dashed rectangle**.
**Object** and **Process** are **Things**.
**Physical Process**, **Informatical Process**, **Systemic Process**, and **Environmental Process** are **Processes**.
**Physical Object**, **Informatical Object**, **Systemic Object**, and **Environmental Object** are **Objects**.
**Physical Systemic Process** is a **Physical Process** and a **Systemic Process**.
**Physical Systemic Process** exhibits **shaded solid ellipse Symbol of Thing**.
**Physical Environmental Process** is a **Physical Process** and an **Environmental Process**.
**Physical Environmental Process** exhibits **shaded dashed ellipse Symbol of Thing**.
**Informatical Environmental Process** is an **Informatical Process** and an **Environmental Process**.
**Informatical Environmental Process** exhibits **non-shaded dashed ellipse Symbol of Thing**.
**Informatical Systemic Process** is an **Informatical Process** and a **Systemic Process**.
**Informatical Systemic Process** exhibits **non-shaded solid ellipse Symbol of Thing**.
**Physical Environmental Object** is a **Physical Object** and an **Environmental Object**.
**Physical Environmental Object** exhibits **shaded dashed rectangle Symbol of Thing**.
**Physical Systemic Object** is a **Physical Object** and a **Systemic Object**.
**Physical Systemic Object** exhibits **shaded solid rectangle Symbol of Thing**.
**Informatical Environmental Object** is an **Informatical Object** and an **Environmental Object**.
**Informatical Environmental Object** exhibits **non-shaded dashed rectangle Symbol of Thing**.
**Informatical Systemic Object** is an **Informatical Object** and a **Systemic Object**.
**Informatical Systemic Object** exhibits **non-shaded solid rectangle Symbol of Thing**.

---

## Figure C.12 — Basic Construct elaboration

[Figure: Diagram showing the **Basic Construct** composed of a **Link** and two **Things**.
The model specializes Basic Construct into **Basic Structural Construct** and **Basic Procedural Construct**.
Structural links connect two **Objects**, while procedural links connect a **Process** and an **Object**.]

**Basic Construct** consists of **Link** and **2 Things**.
**Link** connects **2 Things**.
**Structural Link** and **Procedural Link** are **Links**.
**Basic Structural Construct** and **Basic Procedural Construct** are **Basic Constructs**.
**Basic Structural Construct** consists of **Structural Link** and **2 Objects**.
**Basic Procedural Construct** consists of **Procedural Link**, **Object**, and **Process**.
**Structural Link** connects **2 Objects**.
**Procedural Link** connects a **Process** and an **Object**.

**Figure C.13** is an OPM model of **Basic Structural Construct**.

## Figure C.13 — OPM model of Basic Structural Construct

[Figure: Diagram representing the **OPM model of Basic Structural Construct**.
At the top sits the element **Basic Structural Construct**, connected to several conceptual components.

Core components:

* **Refineable**
* **Refinee**
* **Structural Link**
* **Thing**

Structural links include several semantic variants:

* Aggregation-Participation Link
* Exhibition-Characterization Link
* Generalization-Specialization Link
* Classification-Instantiation Link
* Tagged Structural Link

Refineables include:

* Whole
* Exhibitor
* General
* Class

Refinees include:

* Part
* Feature
* Specialization
* Instance

Each link type corresponds to a semantic category shown in a “Semantics” box on the left:

* aggregation-participation
* exhibition-characterization
* generalization-specialization
* classification-instantiation
* user-defined

On the right side the diagram shows structural constructs corresponding to these semantics:

* Aggregation-Participation Construct
* Exhibition-Characterization Construct
* Generalization-Specialization Construct
* Classification-Instantiation Construct
* Tagged Structural Construct

Arrows show hierarchical refinement relationships among constructs and between refineable/refinee elements and their structural links.]

Basic Structural Construct consists of **Refineable, Refinee, and Structural Link**.
Refineable and Refinee are **Things**.
Whole, Exhibitor, General, and Class are **Refineables**.
Part, Feature, Specialization, and Instance are **Refinees**.
Structural Link exhibits **Semantics**.
Semantics of Structural Link can be **aggregation-participation, exhibition-characterization, generalization-specialization, classification-instantiation, or user-defined**.
Aggregation-Participation Link, Exhibition-Characterization Link, Generalization-Specialization Link, Classification-Instantiation Link, and Tagged Structural Link are **Structural Links**.
Aggregation-Participation Link exhibits **aggregation-participation Semantics**.
Exhibition-Characterization Link exhibits **exhibition-characterization Semantics**.
Generalization-Specialization Link exhibits **generalization-specialization Semantics**.
Classification-Instantiation exhibits **classification-instantiation Semantics**.
Tagged Structural Link exhibits **user-defined Semantics**.

Aggregation-Participation Construct, Exhibition-Characterization Construct, Generalization-Specialization Construct, Classification-Instantiation Construct and Tagged Structural Construct are **Basic Structural Constructs**.

Aggregation-Participation Construct consists of **Aggregation-Participation Link, Whole, and Part**.
Exhibition-Characterization Construct consists of **Exhibition-Characterization Link, Exhibitor, and Feature**.
Generalization-Specialization Construct consists of **Generalization-Specialization Link, General, and Specialization**.
Classification-Instantiation Construct consists of **Classification-Instantiation Link, Class, and Instance**.
Tagged Structural Construct consists of **Tagged Structural Link and 2 Things**.

---

## Figure C.14 — OPM model of Basic Procedural Construct

[Figure: Diagram representing the **OPM model of Basic Procedural Construct**.
At the top is **Basic Procedural Construct**, composed of **Object**, **Process**, and **Procedural Link**.

Procedural Link has semantics categories:

* transformation
* enablement
* enablement & control
* transformation & control

Specific link types shown:

* Transforming Link
* Enabling Link
* Enabling & Control Link
* Transforming & Control Link

Objects involved include:

* Transformee
* Enabler
* Controlling Enabler
* Controlling Transformee

The diagram shows constructs derived from these links:

* Transformation Construct
* Enablement Construct
* Enablement & Control Construct
* Transformation & Control Construct

Arrows illustrate relationships among processes, objects, and links.]

Basic Procedural Construct consists of **Object, Process, and Procedural Link**.
Procedural Link exhibits **Semantics**.
Semantics of Procedural Link can be **transformation, enablement, transformation & control, and enablement & control**.
Transformee and Enabler are **Objects**.
Controlling Transformee is a **Transformee**.
Controlling Enabler is an **Enabler**.
Transforming Link and Enabling Link are **Procedural Links**.
Transforming & Control Link is a **Transforming Link**.
Enabling & Control Link is an **Enabling Link**.

Transforming Link exhibits **transformation Semantics of Procedural Link**.
Enabling Link exhibits **enablement Semantics of Procedural Link**.
Transforming & Control Link exhibits **transformation & control Semantics of Procedural Link**.
Enabling & Control Link exhibits **enablement & control Semantics of Procedural Link**.

Transformation Construct and Enablement Construct are **Basic Procedural Constructs**.
Transformation Construct consists of **Transforming Link, Transformee, and Process**.
Enablement Construct consists of **Enablement Link, Enabler, and Process**.
Transformation & Control Construct is a **Transformation Construct**.
Enablement & Control Construct is an **Enablement Construct**.

Transformation & Control Construct consists of **Transforming & Control Link, Controlling Transformee, and Process**.
Enablement & Control Construct consists of **Enablement & Control Link, Controlling Enabler, and Process**.

---

## Figure C.15 — OPM model of Transformation Construct

[Figure: Diagram showing the **Transformation Construct**.
The construct contains three main elements:

* Transformee
* Process
* Transforming Link

Transforming Link has symbols:

* unidirectional closed arrowhead
* bidirectional closed arrowhead pair

Semantics associated with the link:

* consumption
* effect
* result

Additional elements:

* Consumee
* Affectee
* Resultee
* Consumption Link
* Effect Link
* Result Link

These participate in:

* Consumption Construct
* Effect Construct
* Result Construct
* State-Specified Consumption Construct
* State-Specified Result Construct

The diagram visually shows flows between process and objects according to the three semantics.]

Transformation Construct consists of **Transformee, Process, and Transforming Link**.
Transforming Link exhibits **Symbol and Semantics**.
Symbol of Transforming Link can be **unidirectional closed arrowhead or bidirectional closed arrowhead pair**.
Semantics of Transforming Link can be **consumption, effect, or result**.
Consumption Link, Effect Link, and Result Link are **Transforming Links**.
Consumee, Affectee, and Resultee are **Transformees**.

Consumption Construct, Result Construct, and Effect Construct are **Transformation Constructs**.

Consumption Construct consists of **Consumption Link, Process, and Consumee**.
Effect Construct consists of **Effect Link, Process, and Affectee**.
Result Construct consists of **Result Link, Process, and Resultee**.

Consumption Link exhibits **unidirectional closed arrowhead Symbol of Transforming Link and consumption Semantics of Transforming Link**.
Effect Link exhibits **bidirectional closed arrowhead consumption pair of Transforming Link and effect Semantics of Transforming Link**.
Result Link exhibits **unidirectional closed arrowhead Symbol of Transforming Link and result Semantics of Transforming Link**.

State-Specified Consumption Construct is a **Consumption Construct**.
State-Specified Result Construct is a **Result Construct**.

---

## Figure C.16 — OPM model of Transformation Construct link directionality

[Figure: Diagram illustrating directionality of links in the Transformation Construct.

Objects shown:

* Transformee
* Process
* Consumee
* Affectee
* Resultee

Links:

* Consumption Link
* Effect Link
* Result Link

Directional annotations indicate:

Consumption Link connects from Consumee.
Consumption Link connects to Process.

Effect Link connects Affectee and Process.

Result Link connects to Resultee.
Result Link connects from Process.

Construct groupings include:

* Consumption Construct
* Effect Construct
* Result Construct.]

Transformation Construct consists of **Transformee, Process, and Transforming Link**.
Consumption Link, Effect Link, and Result Link are **Transforming Links**.
Consumption Construct, Result Construct, and Effect Construct are **Transformation Constructs**.

Consumption Construct consists of **Consumption Link, Process, and Consumee**.
Effect Construct consists of **Effect Link, Process, and Affectee**.
Result Construct consists of **Result Link, Process, and Resultee**.

Consumption Link connects from **Consumee**.
Consumption Link connects to **Process**.
Effect Link connects **Affectee and Process**.
Result Link connects to **Resultee**.
Result Link connects from **Process**.

---

## Figure C.17 — OPM model of Basic Enablement Construct

[Figure: Diagram representing the **Basic Enablement Construct**.

Main elements:

* Enabler
* Process
* Enabling Link

Additional elements:

* Agent
* Instrument
* Agent Link
* Instrument Link

Semantics box lists:

* agent
* instrument

Symbol box lists:

* black lollipop
* white lollipop

Derived constructs:

* Agent Construct
* Instrument Construct
* State-Specified Agent Construct
* State-Specified Instrument Construct.]

Enablement Construct consists of **Enabler, Process, and Enabling Link**.
Enabling Link exhibits **Semantics and Symbol**.
Enabling Link connects from **Enabler**.
Enabling Link connects to **Process**.
Semantics of Enabling Link can be **Agent or Instrument**.
Symbol of Enabling Link can be **black lollipop or white lollipop**.

Agent and Instrument are **Enablers**.
Agent Link and Instrument Link are **Enabling Links**.

Agent Link exhibits **agent Semantics of Enabling Link and black lollipop Symbol of Enabling Link**.
Instrument Link exhibits **instrument Semantics of Enabling Link and white lollipop Symbol of Enabling Link**.

Agent Construct and Instrument Construct are **Enablement Constructs**.
Agent Construct consists of **Agent, Process, and Agent Link**.
Instrument Construct consists of **Instrument, Process, and Instrument Link**.

State-Specified Agent Construct is an **Agent Construct**.
State-Specified Instrument Construct is an **Instrument Construct**.

---

## Figure C.18 — OPM model of state-specified agent construct with mapped example

[Figure: Diagram showing a mapping example of a **State-Specified Agent Construct**.

Upper section shows the conceptual model:

* State-Specific Object
* State-Specific Enabler
* State-Specific Agent
* Agent Link
* Process
* State-Specified Agent Construct

Lower section presents an example:

Administrator object with states:

* unauthorized
* authorized

Authorized Administrator performs the process **Approving**.

Arrows map conceptual elements to their OPD symbols in the example model.]

State-Specified Agent Construct consists of **State-Specified Agent, Process, and Agent Link**.
State-Specified Agent is a **State-Specified Enabler**.
State-Specified Enabler is a **State-Specified Object**.
Agent Link connects **State-Specified Agent and Process**.

Figure C.18 depicts two OPM models with the top of the figure expressing essential associations for a State-Specified Agent Construct and the bottom of the figure expressing a corresponding model construct. The former provides a metamodel for the latter. The broad arrows map the conceptual parts of the construct to the OPD symbols of the example. Below the OPD in the example is the corresponding OPL.

For instructional purposes, similar mapping figures may express the correspondence between models of OPM construct conceptual models and corresponding OPM models in application.

---

## C.5 In-zooming and out-zooming models

### C.5.1 The in-zooming and out-zooming mechanisms

Both **new-diagram in-zooming** and **new-diagram out-zooming** create a new OPD context from an existing OPD context.

New-diagram in-zooming starts with an OPD of relatively less details and adds elaboration or refinement as a descendant OPD that applies to a specific thing in the less detailed OPD.

New-diagram out-zooming starts with an OPD of relatively more details and removes elaboration or refinement to produce a less detailed, more abstract thing in an ancestor context.

New-diagram in-zooming elaborates a refineable present in an existing OPD, say **SDn**, by creating a new OPD, **SDn+1**, which elaborates the refineable by adding subprocesses, associated objects, and relevant links.

The new-diagram in-zooming and in new-diagram out-zooming processes are inverse operations.

---

## Figure C.19 — New-Diagram In-Zooming and New-Diagram Out-Zooming models

[Figure: Diagram illustrating the two processes:

Left side — New-Diagram In-Zooming
Steps:

1. Content Showing
2. Semi-Zoomed OPD
3. Link Refining

Right side — New-Diagram Out-Zooming
Steps:

1. Link Abstracting
2. Semi-Zoomed OPD
3. Content Hiding

The diagrams show transitions between model levels **SDn** and **SDn+1**.]

New-Diagram In-Zooming requires **SDn**.
New-Diagram In-Zooming yields **SDn+1**.
New-Diagram Out-Zooming requires **SDn+1**.

New-Diagram In-Zooming zooms into **Content Showing and Link Refining**, in that sequence, as well as **Semi-Zoomed OPD**.
Content Showing requires **SDn**.
Content Showing yields **Semi-Zoomed OPD**.
Link Refining consumes **Semi-Zoomed OPD**.
Link Refining yields **SDn+1**.

New-Diagram Out-Zooming zooms into **Link Abstracting and Content Hiding**, in that sequence, as well as **Semi-Zoomed OPD**.
Link Abstracting requires **SDn+1**.
Link Abstracting yields **Semi-Zoomed OPD**.
Content Hiding consumes **Semi-Zoomed OPD**.
Content Hiding yields **SDn**.

Semi-Zoomed OPD is an interim object created and subsequently consumed during **New Diagram In-Zooming or New Diagram Out-Zooming**. Semi-Zoomed OPD appears only within the contexts of New-Diagram In-Zooming and New-Diagram Out-Zooming.

---

## Figure C.20 — New-Diagram In-Zooming and New-Diagram Out-Zooming elaboration

[Figure: Diagram illustrating detailed example of the in-zooming and out-zooming process.

Elements include:

* SDn model with process **P** and objects **C, A, D, B**
* Semi-Zoomed OPD containing subprocesses **P1, P2, P3** and internal object **BP**
* SDn+1 model where links migrate to subprocesses
* Corresponding out-zooming transformation reversing the process

The diagram shows how subprocesses replace a higher-level process and how links migrate to refined elements.]

Figure C.20 shows **New-Diagram In-Zooming and New-Diagram Out-Zooming** with unfolding of **SDn, SDn+1, and Semi-zoomed OPD from Figure C.19**.

New-Diagram In-Zooming and New-Diagram Out-Zooming operate on a particular instance of **SDn** shown at the middle top of Figure C.20, where the **SDn detail is one of many possibilities**.

In this case, SDn includes **P**, which is the refined process, as well as four objects connected to **P** with different kinds of links: the **consumee C**, the **agent A**, the **instrument D**, and the **resultee B**.

The in-diagram in-zooming of **Semi-Zoomed OPD** makes clear that it is an interim representation created and consumed during **New Diagram In-Zooming** as well as during **New Diagram Out-Zooming**.

Content Showing is the first of the two **New-Diagram In-Zooming** subprocesses.
During Content Showing, the boundary of **P** expands to make room for showing its content—the model subprocesses **P1, P2, and P3**, as well as the interim model object **BP**.

The result of Content Showing is the unfolding of object **Semi-Zoomed OPD**.

During **Link Refining**, the procedural links attached to the contour of **P** migrate to the appropriate subprocesses as determined by the modeller.

Thus, since **P1 consumes C**, the consumption link arrowhead migrates from **P to P1**.
The agent **A** handles both **P1 and P2**, so in **SDn+1** two agent links replace the single one in **SDn**, one to **P1** and the other to **P2**.

**P3 requires D**, so the instrument link moves from **P to P3**.

Finally, since **BP results from P1 and P3 consumes it**, the corresponding result and consumption links are added, making **BP an internal object of P**, an object that is only recognizable within the context of **P**, like **P1, P2, and P3**.

Notice that **BP is to P as Semi-Zoomed OPD is to New-Diagram In-Zooming**.

---

### C.5.2 Simplifying an OPD

In-diagram out-zooming can combine with new-diagram in-zooming to simplify an already-modelled OPD that the modeller deems overly complicated.

In-diagram out-zooming followed by new-diagram in-zooming is an option when the modeller realizes that the current OPD is overloaded with details.

In-diagram out-zooming reduces the cognitive load necessary to understand the complicated OPD at the expense of adding a new OPD to the OPD set, which is the result of the subsequent new-diagram in-zooming.

---

## Figure C.21 — Simplifying an OPD

[Figure: Multi-panel diagram illustrating simplification of an OPD.

Left side: original OPD set containing three diagrams (SD, SD1, SD1.1).
Middle: selection of processes **P1, P2, P3** and object **BP** as the set **TO** for abstraction into new process **P123**.
Right side: new OPD set containing four diagrams after simplification and renumbering.

The process **P123** replaces the original set and appears as an abstract process in a new diagram hierarchy.]

In the middle of Figure C.21 the processes **P1, P2, and P3**, along with the object **BP** are the four members of **TO**, which are surrounded by **P123**.

The consequence of creating **P123** is the disappearance of the four members of **TO** from the new **SD1**.

Each link that crosses the grey-white boundary of the middle graphic now connects to the boundary of **P123** in the new **SD1**.

The objects connecting to the boundary of **P123** in the new **SD1** then connect to the appropriate subprocesses in the new **SD1.1**.

The object **BK** cannot be a member of **TO** because if **BK occurs in P123 its links create two procedural links connecting two processes directly**, **P4 to P123 and P123 to P5**.

OPM does not define the semantics of these links and the model would violate the specification that **every procedural link (except the invocation and time exception links) connects an object to a process**.

---

## C.6 OPM Process Performance Controlling model

### C.6.1 OPM Process Performance Controlling System – SD

[Figure: System diagram showing **Process Performance Controlling**.

Central process:

* Process Performance Controlling

Input:

* Executable Process

Outputs:

* Success Message
* Failure Message

Failure message can include:

* Cancel Message
* Abort Message

Objects involved:

* Involved Object Set

  * Preprocess Object Set
  * Postprocess Object Set

Each object set has a size constraint:

* Preprocess Object Set: r ≥ 0
* Postprocess Object Set: s ≥ 0
* Involved Object Set: r + s ≥ 0

Arrows represent relations between the process and object sets.]

Involved Object Set consists of **Preprocess Object Set and Postprocess Object Set**.
Preprocess Object Set exhibits **Size**.
Size of Preprocess Object Set is **r≥0**.
Postprocess Object Set exhibits **Size**.
Size of Postprocess Object Set is **s≥0**.
Involved Object Set exhibits **Size**.
Size of Involved Object Set is **r+s≥0**.

Process Performance Controlling affects **Involved Object Set**.
Executable Process is **environmental**.
Executable Process invokes **Process Performance Controlling**.

Process Performance Controlling yields one of **Success Message or Failure Message**.
Abort Message and Cancel Message are **Failure Messages**.

### C.6.2 Process Performance Controlling in-zoomed as SD1

[Figure: Diagram showing the decomposition of **Process Performance Controlling** into two subprocesses: **Process Initiating** and **Process Performing**, enclosed within a large boundary representing the controlling context. Inputs include **Preprocess Object Set**, composed of **Enabler Set**, **Consumee Set**, and **Affectee Set**. Additional elements include **Cancel Message**, **Success Message**, and **Abort Message**. Outputs include **Postprocess Object Set**, consisting of **Resultsee Set** and **Affectee Set**. A **Postcondition** object can take values *false* or *true*. A **Process Status** object can take states *idle*, *started (t=0)*, *aborted*, or *completed (t=n)*. Arrows indicate control flow between initiating and performing processes.]

Process Performance Controlling zooms into **Process Initiating** and **Process Performing**, in that sequence, as well as **Postcondition**.
**Preprocess Object Set** consists of **Consumee Set**, **Affectee Set**, and **Enabler Set**.
**Postprocess Object Set** consists of **Resultsee Set** and **Affectee Set**.
**Executable Process** is environmental.
**Executable Process** invokes **Process Initiating**.
**Process Performance Controlling** exhibits **Process Status**.
**Process Status** can be **idle**, **started (t=0)**, **aborted**, or **completed (t=n)**.
**Process Status** is initially **idle** and finally **completed (t=n)** or **aborted**.
**Postcondition** can be **false** or **true**.
**Postcondition** is initially **false**.
**Process Initiating** requires **Preprocess Object Set**.
**Process Initiating** changes **Process Status** from **idle** to exactly one of **idle** or **started (t=0)**.
**Process Initiating** yields **false Postcondition** and **Cancel Message**.
**Process Performing** occurs if **Enabler Set** exists, otherwise **Process Performing** is skipped.
**Process Performing** affects **Postcondition** and **Affectee Set**.
**Process Performing** changes **Process Status** from **started (t=0)** to exactly one of **aborted** or **completed (t=n)**.
**Process Performing** yields **Resultsee Set** and either **Success Message** or **Abortion Message**.

---

### C.6.3 Process Initiating in-zoomed as SD1.1

[Figure: Diagram showing the internal structure of **Process Initiating**, including subprocess **Precondition Evaluating**, which branches into **Cancelling** and **Starting** based on the value of **Precondition**. Inputs include **Preprocess Object Set** and environmental **Executable Process**. Outputs include **Cancel Message**, **Failure Time (t=0)**, **Process Status** changes, and **Postcondition**.]

**Process Initiating** from SD1 zooms in **SD1.1** into **Precondition Evaluating** and parallel **Cancelling** and **Starting**, in that sequence, as well as **Precondition**.
**Process Status** can be **idle**, **started (t=0)**, or other states.
**Process Status** is initially **idle**.
**Postcondition** can be **false** or **true**.
**Postcondition** is initially **false**.
**Executable Process** is environmental.
**Executable Process** invokes **Precondition Evaluating**.
**Precondition Evaluating** yields **Precondition**.
**Precondition** can be **true** or **false**.
**Precondition Evaluating** requires **Preprocess Object Set**.
**Precondition Evaluating** changes **Process Status** from **idle**.
**Cancelling** occurs if **Precondition** is **false**, otherwise **Cancelling** is skipped.
**Cancelling** changes **Process Status** to **idle**.
**Cancelling** yields **Cancel Message**.
**Cancellation Message** exhibits **Failure time**.
**Cancelling** sets the value of **Failure time** to **t=0**.
**Failure time** of **Cancel Message** is **t=0**.
**Starting** occurs if **Precondition** is **true**, in which case **Precondition** is consumed, otherwise **Starting** is skipped.
**Starting** changes **Process Status** to **started (t=0)**.
**Starting** yields **false Postcondition**.

---

### C.6.4 Precondition Evaluating in-zoomed as SD1.1.1

[Figure: Diagram detailing the internal operations of **Precondition Evaluating**. Subprocesses include **Enabler Set Checking**, **Consumee & Affectee Set Checking**, **Precondition Refuting**, and **Precondition Confirming**. These processes evaluate the presence and validity of **Enabler Set**, **Consumee Set**, and **Affectee Set**, producing intermediate results such as **Enabler Set Check Result** and **Consumee & Affectee Set Check Result** (each with possible values *positive* or *negative*). The final outcome determines whether **Precondition** becomes *true* or remains *false*.]

**Precondition Evaluating** from SD1.1 zooms in **SD1.1.1** into **Enabler Set Checking**, **Consumee & Affectee Set Checking**, **Precondition Refuting**, and **Precondition Confirming**, in that sequence, as well as **Enabler Set Check Result** and **Consumee & Affectee Set Check Result**.
**Preprocess Object Set** consists of **Enabler Set** and **Consumee & Affectee Set**.
**Process Status** can be **idle**, **started (t=0)**, or other states.
**Process Status** is initially **idle**.
**Precondition** can be **false** or **true**.
**Precondition** is initially **false**.
**Executable Process** invokes **Enabler Set Checking**.
**Enabler Set Checking** requires that **Enabler Set** exists, otherwise **Enabler Set Checking** is skipped.
**Enabler Set Checking** changes **Process Status** from **idle**.
**Enabler Set Check Result** can be **positive** or **negative**.
**Enabler Set Check Result** is initially **positive**.
**Enabler Set Checking** affects **Enabler Set Check Result**.
**Consumee & Affectee Set Checking** occurs if **Enabler Set Check Result** is **positive** and **Consumee & Affectee Set** exists, otherwise **Consumee & Affectee Set Checking** is skipped.
**Consumee & Affectee Set Check Result** can be **positive** or **negative**.
**Consumee & Affectee Set Check Result** is initially **positive**.
**Consumee & Affectee Set Checking** affects **Consumee & Affectee Set Check Result**.
**Precondition Refuting** requires that either **Enabler Set Check Result** is **negative** or **Consumee & Affectee Set Check Result** is **negative**, otherwise **Precondition Refuting** is skipped.
**Precondition Refuting** changes **Process Status** to **idle**.
**Precondition Confirming** occurs if **Transformee Check Result** is **positive**, otherwise **Precondition Confirming** is skipped.
**Precondition Confirming** changes **Precondition** from **false** to **true** and **Process Status** to **started (t=0)**.

---

### C.6.5 Transformee Set Checking in-zoomed as SD1.1.1.1

[Figure: Diagram expanding **Consumee & Affectee Set Checking** into subprocesses **Consumee Set Checking**, **Affectee Set Checking**, and **Transformee Set Disqualifying**. Input sets include **Consumee Set** and **Affectee Set**, with results recorded as **Consumee Set Check Result** and **Affectee Set Check Result** (each with possible values *positive* or *negative*). A disqualification process changes the combined result when either set fails validation.]

**Consumee & Affectee Set Checking** from SD1.1.1 zooms in **SD1.1.1.1** into **Consumee Set Checking**, **Affectee Set Checking**, and **Transformee Set Disqualifying**, in that sequence, as well as **Affectee Set Check Results** and **Consumee Set Check Results**.
**Enabler Set Check Result** can be **negative** or **positive**.
**Enabler Set Check Result** is initially **positive**.
**Consumee & Affectee Set Check Result** can be **negative** or **positive**.
**Consumee & Affectee Set Check Result** is initially **positive**.
**Consumee & Affectee Set** consists of **Consumee Set** and **Affectee Set**.
**Consumee & Affectee Set Checking** occurs if **Enabler Set Check Result** is **positive**, otherwise **Consumee & Affectee Set Checking** is skipped.
**Consumee Set Check Results** can be **negative** or **positive**.
**Consumee Set Check Results** is initially **positive**.
**Consumee Set Checking** occurs if **Consumee Set** exists, otherwise **Consumee Set Checking** is skipped.
**Consumee Set Checking** affects **Consumee Set Check Results**.
**Affectee Set Checking** occurs if **Consumee Set Consumee Set Check Results** is **positive** and **Affectee Set** exists, otherwise **Affectee Set Checking** is skipped.
**Affectee Set Checking** yields **Affectee Set Check Results**.
**Affectee Set Check Results** can be **negative** or **positive**.
**Transformee Set Disqualifying** occurs if either **Affectee Set Check Results** is **negative** or **Consumee Set Check Results** is **negative**.
**Transformee Set Disqualifying** changes **Consumee & Affectee Set Check Result** from **positive** to **negative**.

---

### C.6.6 Process Performing in-zoomed as SD1.2

[Figure: Diagram showing **Process Performing** decomposed into **Initial Process Performing**, **Main Process Performing**, and **Final Process Performing**. Objects involved include **Consumee Set**, **Enabler Set**, **Affectee Set**, and **Postcondition**. **Process Status** transitions through states: *started (t=0)* → *operating (t<n)* → *completing (t=n)* → *completed (t=n)* or *aborted*. Outputs include **Success Message** and **Resultsee Set**.]

**Process Performing** from SD1 zooms in **SD1.2** into **Initial Process Performing**, **Main Process Performing**, and **Final Process Performing**, in that sequence.
**Process Status** can be **idle**, **started (t=0)**, **operating (t<n)**, **aborted**, **completing (t=n)**, **completed (t=n)**, or other states.
**Process Status** is finally **completed (t=n)**.
**Postcondition** can be **false** or **true**.
**Postcondition** is initially **false**.
**Affectee Set** consists of optional **Affectees**.
**Affectee** can be **input state** or **output state**.
**Affectee** is initially **input state** and finally **output state**.
**Initial Process Performing** changes **Process Status** from **started (t=0)** to **operating (t<n)**, **Postcondition** from **false**, and **Affectee** from **input state**.
**Initial Process Performing** consumes **Consumee Set**.
**Main Process Performing** requires **Enabler Set**.
**Main Process Performing** yields an optional **Abort Message**.
**Main Process Performing** changes **Process Status** from **operating (t<n)** to one of **completing (t=n)** or **aborted**.
**Final Process Performing** changes **Process Status** from **completing (t=n)** to **completed (t=n)**, **Postcondition** to **true**, and **Affectee** to **output state**.
**Final Process Performing** yields **Success Message** and **Resultsee Set**.

---

### C.6.7 Initial Process Performing in-zoomed as SD1.2.1

[Figure: Diagram expanding **Initial Process Performing** into parallel processes **Input State Exiting** and **Consumee Set Consuming**. These operations update the **Affectee** object from input state and consume items from the **Consumee Set**, leading to a transition of **Process Status** from *started (t=0)* to *operating (t<n)*.]

**Initial Process Performing** from SD1.2 zooms in **SD1.2.1** into parallel **Input State Exiting** and **Consumee Set Consuming**.
**Preprocess Object Set** consists of **Enabler Set**, **Affectee Set**, and **Consumee Set**.
**Affectee Set** consists of optional **Affectees**.
**Affectee** can be **input state** or **output state**.
**Affectee** is initially **input state** and finally **output state**.
**Process Status** can be **started (t=0)**, **operating (t<0)**, or other states.
**Postcondition** can be **false** or **true**.
**Postcondition** is initially **false**.
**Initial Process Performing** requires **Enabler Set**.
**Input State Exiting** changes **Affectee** from **input state**.
One of **Consumee Set Consuming** or **Input State Exiting** changes **Process Status** from **started (t=0)** to **operating (t<n)** and **Postcondition** from **false**.

---

### C.6.8 Main Process Performing in-zoomed as SD1.2.2

[Figure: Diagram showing the main execution stage of the process. Subprocesses include **Elapsed Time & Duration Comparing**, **Enabler & Affectee Set Checking**, **Process Executing & Time Incrementing**, **Aborting & Notifying**, and **Finalizing**. Objects include **Elapsed Time (e)** and **Duration (d)**, producing **Time Comparison Result** values *e<d*, *e=d*, or *e>d*. Depending on these outcomes and approval results, the process either continues execution, aborts, or proceeds to completion.]

Main Process Performing from SD1.2 zooms in **SD1.2.2** into **Elapsed Time & Duration Comparing**, **Enabler & Affectee Set Checking**, **Aborting & Notifying**, **Time Incrementing**, and **Finalizing**, in that sequence, as well as **Time Comparison Result** and **Set Approval**.
**Executable Process** exhibits **Executable Process Instruction Set** and **Overtime Exception Handling**.
**Executable Process**, **Executable Process Instruction Set**, and **Overtime Exception Handling** are environmental.
**Process Status** can be **aborted**, **completed (t=n)**, **operating (t<0)** or other states.
**Process Status** is finally **aborted** or **completed (t=n)**.
**Postcondition** can be **false** or **true**.
**Postcondition** is initially **false**.
**Main Process Performing** exhibits **Elapsed Time** in **Time Unit** and **Duration** in **Time Unit**.
**Abortion Message** exhibits **Elapsed Time** in **Time Unit**.
**Elapsed Time** in **Time Unit** is **e**.
**Duration** in **Time Unit** is **d**.
**Elapsed Time & Duration Comparing** requires **Elapsed Time** in **Time Unit** and **Duration** in **Time Unit**.
**Elapsed Time & Duration Comparing** changes **Postcondition** from **false**.
**Elapsed Time & Duration Comparing** yields **Time Comparison Result**.
**Time Comparison Result** can be **e<d**, **e=d**, or **e>d**.
**Time Comparison Result** is initially **e<d** or **e=d** and finally **e=d** or **e>d**.
**Enabler & Affectee Set Checking** requires **Enabler Set** and **Affectee Set**.
**Enabler & Affectee Set Checking** occurs if **Time Comparison Result** is **e<d**, in which case **Enabler & Affectee Set Checking** consumes **Time Comparison Result**, otherwise **Enabler & Affectee Set Checking** is skipped.
**Enabler & Affectee Set Checking** yields **Set Approval**.
**Set Approval** can be **granted** or **denied**.
**Aborting & Notifying** occurs if **Set Approval** is **denied**, in which case **Aborting & Notifying** consumes **Set Approval**, otherwise **Aborting & Notifying** is skipped.
**Aborting & Notifying** changes **Process Status** from **operating (t<n)** to **aborted** and **Postcondition** to **false**.
**Aborting & Notifying** yields **Abort Message**.
**Abort Message Finalizing** occurs if **Time Comparison Result** is **e=d**, in which case **Finalizing** consumes **Time Comparison Result**, otherwise **Finalizing** is skipped.
**Finalizing** changes **Process Status** from **operating (t<n)** to **completed (t=n)** and **Postcondition** to **true**.
**Process Executing & Time Incrementing** requires **Executable Process Instruction Set**.
**Process Executing & Time Incrementing** occurs if **Set Approval** is **granted**, in which case **Process Executing & Time Incrementing** consumes **Set Approval**, otherwise **Process Executing & Time Incrementing** is skipped.
**Time Incrementing** consumes **Sets are OK**.
**Time Incrementing** yields **elt=1..ext Elapsed Time** in **Time Unit**.
**Process Executing & Time Incrementing** changes the value **e** of **Elapsed Time** in **Time Unit**.
**Process Executing & Time Incrementing** invokes **Elapsed Time & Duration Comparing**.
**Overtime Exception Handling** consumes **e>d Time Comparison Result**.

---

### C.6.9 Final Process Performing in-zoomed as SD1.2.3

[Figure: Diagram illustrating the final stage of the process. Subprocesses include **Resultsee Set Generating**, **Output State Entering**, and **Success Notifying**. Inputs include **Postprocess Object Set** composed of **Resultsee Set** and **Affectee Set**. Outputs include **Success Message**, updated **Postcondition**, and final **Process Status** state **completed (t=n)**.]

**Final Process Performing** from SD1.2 zooms in **SD1.2.3** into parallel **Resultsee Set Generating**, **Output State Entering**, and **Success Notifying**, in that sequence.
**Postprocess Object Set** consists of **Resultsee Set** and **Affectee Set**.
**Affectee Set** consists of optional **Affectees**.
**Affectee** can be **input state** or **output state**.
**Affectee** is initially **input state** and finally **output state**.
**Process Status** can be **completed (t=n)**, **completing (t=n)**, or other states.
**Process Status** is finally **completed (t=n)**.
**Postcondition** can be **false** or **true**.
**Postcondition** is initially **false**.
**Resultsee Set Generating** yields **Resultsee Set**.
**Output State Entering** changes **Affectee** to **output state**.
**Success Notifying** changes **Postcondition** to **true**.
**Success Notifying** yields **Success Message**.

---

## Annex D (informative)

## OPM dynamics and simulation

## D.1 OPM executability

An OPM model provides for executability—the ability to simulate a system by executing its model via animation in a properly designed software environment.

## D.2 Change and effect

A change of an object is an alteration in the state of that object. More specifically, a change of an object is reflected by replacing its current state by another state. The only thing that can cause this change is a process. The process causes the change by taking as input an object at some state, and outputting it in another state. Hence, a change of an object means a change in the state at which the object is at.

Stateful objects can be affected, i.e. their states can change. This change mechanism underlines the intimate, inseparable link between objects and processes. This change in state is the effect of the process on the object.

Effect is therefore defined as the change in the state of an object that a process causes.

While the terms “change” and “effect” are almost synonymous, there is a subtle difference in their usage. Effect is used to refer to what the process does to the object, and change—to what happens to the object as a result of the process occurrence. The above definition of effect is refined later in this annex with the notions of input and output links.

## D.3 Existence and transformation

Change is only one possibility of what can happen to an object when a process acts on it. A process affects an object to change it, but it can also do things that are more drastic: it can generate an object or consume it. The term transformation covers these three additional modes by which a process can act on an object: construction, effect, and consumption.

Construction is synonymous with creation, generation, or yielding. Effect is synonymous with change or switch, and consumption is synonymous with elimination, termination, annihilation, or destruction. The effect of a process on an object is to change that object from one of its states to another, but the object still exists, and it keeps maintaining the identity it had before the process occurred. Construction and consumption change the very existence of the object and are therefore more profound transformations than effect.

When a process constructs (yields, generates, creates, or results in) an object, the meaning is that the object, which had not previously existed, has undergone a radical transformation. This transformation made it stand out and become identifiable and meaningful in the system. It now deserves treatment and reference as a new, separate entity.

When a process consumes (eliminates or destroys) an object, the meaning is that the object, which had previously existed, and was identifiable and meaningful in the system, has undergone a radical transformation. Consequently, the object no longer exists in the system and is no longer identifiable.

## D.4 Timeline OPM principle

By default, the execution timeline within an in-zoomed process begins at the graphical top and ends at the graphical bottom, unless there is indication to deviate from the timeline. Such indications include the special OPM internal events within the scope of the process that may cause loops, and the process whose name is or ends with the phrase **Exception Exiting**. Regardless of its graphical position, if this process is invoked, the context process, i.e. the in-zoomed process within which this process is embedded, exits promptly and unconditionally.

The top-most point of the process ellipse serves as a reference point, so a process whose reference point is higher than its peer(s) starts earlier. If the reference points of two or more processes are at the same height (within a few graphical units, e.g. pixels, of tolerance), these processes start simultaneously and in parallel.

---

## D.5 Timed events

The events presented so far were object or state events: they happened when a specific object became existent or entered a specific state. In contrast, timed events depend on the arrival of a specific time in the system, as shown below.

A state event can represent a time event, as **Figure D.1** demonstrates.

[Figure: Legal system model change from minor to adult at the age of 18 years.
The diagram shows several OPM elements. On the left, an ellipse labeled **Birth** connects to a dashed ellipse labeled **Growing**. Below is an object **Age [yr]** with three states: **0**, **< 18**, and **≥ 18**. The states are connected with arrows indicating progression from birth through growth. On the right is an object **Person** with two states: **minor** and **adult**. A process labeled **Legal Status Changing** is connected to the **Person** object and is triggered when the age reaches the threshold indicating adulthood. Arrows indicate that the change in the **Age** object state causes the **Legal Status Changing** process, which changes the state of **Person** from **minor** to **adult**.]

**Figure D.1 — Legal system model change from minor to adult at the Age of 18 Years**

**Figure D.2** demonstrates the System Clock event initiating Legal Status Changing.

[Figure: System clock event initiating legal status change.
The diagram shows an ellipse labeled **Birth** connected to the object **Person** with states **minor** and **adult**. A rectangular object labeled **System Clock [yr]** contains the value **18**. A connection marked with **e** leads from the clock to the process **Legal Status Changing**. The process then changes the state of the **Person** object from **minor** to **adult**.]

**Figure D.2 — The System Clock event initiating Legal Status Changing**

---

## D.6 Object history and the lifespan diagram

At any point in time, an object can be in one of its states, or exists in transition between two states.

A lifespan diagram is a diagram showing for any point in time during the life of the system what objects exists in the system, what state each object is at, and what processes are active.

[Figure: Car painting lifespan diagram example composed of four stacked diagrams representing successive time periods. Each diagram shows rows labeled **Name**, **Type**, and time columns (1, 2, 3, 4, 5). Objects include **Painting (Process)**, **Color (Object)**, and **Car (Object)**. The diagrams illustrate how the process **Painting** changes from **not active** to **active** and back to **not active**, while the **Color** object transitions from **white** to **red**, and the **Car** object continues to exist throughout the time periods.]

**Figure D.3 — Car Painting four lifespan diagrams example**

The four lifespan diagrams shown at **Figure D.3** record the history of the car painting system as time progresses. These four lifespan diagrams are displayed stacked vertically to facilitate their inspection. In the first diagram, only the first time period is displayed. Painting is not active, and the Car is white.

In the second diagram, the first three time periods are displayed. In the third period, Painting is active, and the Car is no longer white. The same happens in the fourth period, as shown in the third diagram. Finally, in the fifth period, shown in the bottom diagram, Painting is no longer active, and the Car is red.

---

## D.7 Process duration

System time unit is the default time unit used for specifying all duration kinds of all the processes in the system unless there is an explicit different time unit for a specific process, in which case that time unit overrides the system time unit.

A compact way to express the relevant process property values in an OPD uses exhibition-characterization and specialization links. Assuming that the following are relevant process properties, Example 1 expresses two ways to graphically configure the properties:

* the time measurement unit;

* time duration parameters, which can be one of the following:

  * three values, standing for the minimal, expected, and maximal duration, respectively,
  * two values, standing for the minimal and maximal duration, respectively, or
  * one value, standing for both the minimal and maximal durations; and,

* the duration distribution name and its one or more parameters.

The following are possible normative distributions and their parameter(s):

* **Normal**, mean=xx; sd=yy;
* **Uniform**, a=xx, b=yy; and,
* **Exponential**, lambda=xx.

**NOTE**
The time measurement unit of seconds is the customary default and often omitted.

---

### Example 1

**Figure D.5** illustrates a metamodel of Processing Duration with property values. On the left is the complete metamodel. The process on the right shows a compact way to record all the data on the left, except for the (actual) Duration, which is a run-time property. The Duration Distribution in this example is normal with mean 45,6 min and standard deviation 7,3 min.

[Figure: Processing duration metamodel.
A process **Processing** is connected to several property objects. One branch leads to **Duration [min]** showing a value of **63.3**. Another branch leads to **Duration Distribution**, which specifies **normal, mean=45.6, sd=7.3**. Beneath these are objects representing **Minimal Duration (30.0)**, **Expected Duration (45.6)**, and **Maximal Duration (60.0)**. Another element lists possible time units: **ms**, **sec**, **min**, **hour**, **day**, **week**, **month**, **year**. On the right side, a compact notation displays the process with duration parameters: minimal, expected, maximal durations and the normal distribution.]

**Figure D.5 — Processing Duration with property values**

---

### Example 2

**Figure D.6** provides process duration examples.

[Figure: Three example process duration representations.

1. **Processing [hour]** with durations (8.0, 10.0) and distribution **exponential, lambda=5.6**.
2. **Processing [ms]** with distribution **normal, mean=1.63, sd=0.16**.
3. **Processing [days]** with distribution **uniform, a=3, b=5**.]

**Figure D.6 — Process duration examples**

Processing exhibits **8.0 h** and **10.0 h** Minimal Duration and Maximal Duration, respectively, and exponential Duration Distribution with parameter lambda=5.6.

Processing exhibits normal Duration Distribution with parameters mean=1.63 and sd=0.16 ms.

Processing exhibits uniform Duration Distribution with parameters a=3 and b=5 days.

---

### Example 3

In **Figure D.7**, Processing {instance id=1} Duration is **63,3 min**, hence **Overtime Exception Handling** occurs.

[Figure: Overtime exception example.
A process **Processing [min] (30.0, 45.6, 60.0)** with distribution **uniform, a=5.0, b=70.0** and instance id=1 is shown connected to **Duration [min] = 63.3**. Since the duration exceeds the maximal expected value, a process **Overtime Exception Handling** is triggered. Both the main process and exception process affect an object labeled **Affectee**.]

Processing exhibits **30.0**, **45.6**, and **60.0 min** Minimal Duration, Expected Duration, and Maximal Duration, respectively, and **uniform Duration Distribution** with parameters **a=5.0** and **b=70.0**.

Either **Processing** or **Overtime Exception Handling** affects **Affectee**.

**Overtime Exception Handling** occurs if duration of **Processing** exceeds **60.0 min**.

**Overtime Exception Handling** affects **Affectee**.

**Figure D.7 — Overtime exception example**

---

### Example 4

In **Figure D.8**, Processing {instance id=2} Duration is **23,4 min**, hence **Undertime Exception Handling** occurs.

[Figure: Undertime exception example.
A process **Processing [min] (30.0, 45.6, 60.0)** with distribution **uniform, a=5.0, b=70.0** and instance id=2 is shown connected to **Duration [min] = 23.4**. Since the duration falls below the minimal threshold, a process **Under-time Exception Handling** is triggered. Both the main process and exception process affect an object labeled **Affectee**.]

Processing exhibits **30.0**, **45.6**, and **60.0 min** Minimal Duration, Expected Duration, and Maximal Duration, respectively, and **uniform Duration Distribution** with parameters **a=5.0** and **b=70.0**.

Either **Processing** or **Undertime Exception Handling** affects **Affectee**.

**Undertime Exception Handling** occurs if duration of **Processing** falls short of **60.0 min**.

**Undertime Exception Handling** affects **Affectee**.

**Figure D.8 — Undertime exception example**

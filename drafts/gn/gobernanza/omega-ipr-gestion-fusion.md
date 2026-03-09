---
_manifest:
  urn: urn:gn:kb:omega-ipr-gestion-fusion
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- finanzas-publicas
- gestion-ipr
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml: 3ab92b1ccdacc60070e0a8796dd54bb600e956cf0e3f6a4b50b606bc23610385
    source_type: ontology_yaml
    transformation_mode: derive_ttl_scope
    fs: 100
    cr: 1.53
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Fusion semantica IPR/Gestion; requiere validacion de alcance.
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 8
    meat_count: 637
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__omega-ipr-gestion-fusion.md.json
---

# Ontología Ω-IPR: Gestión y Fusión de Financiamiento

## Meta

### Urn
urn:gorenuble:omega:ontology:ipr-gestion-fusion:1.0.0

### Type
Ω-Ontology

### Schema
Omega schema 2.0.0

### Based on
- urn:fxsl:cat:omega-opm-ws:1.0.0
- [Gestión Operacional de Intervenciones Públicas Regionales (IPR)](urn:gn:kb:gestion-ipr)
- urn:knowledge:gorenuble:gn:selector-ipr:3.1.0

### Date
2025-12-25

### Description
Fusión categorial profunda de los dominios de Gestión Operacional IPR y 
Selector de Vías de Financiamiento. Utiliza construcciones universales:
- Fibración de Grothendieck para polimorfismo de mecanismos
- Mónadas separadas para cada sistema de evaluación (RATE, RF, ITF, CONCURSO)
- Coalgebra para ciclo de vida IPR
- Pullback para admisibilidad documental
- Profuntor Selector ↔ Gestión

## Omega objects

### Omega objects
| id | type | description |
| --- | --- | --- |
| Ω-IPR | Ω-Object | Intervención Pública Regional: unidad atómica de financiamiento del GORE |
| Ω-MECANISMO | Ω-Object (Fiber Index) | Vía de financiamiento que determina reglas, proceso y sistema de evaluación |
| Ω-DICTAMEN | Ω-Object (Effect Constructor) | Resultado de evaluación según sistema aplicable |
| Ω-ACTOR | Ω-Object (Agent) | Agentes que participan en el ciclo de vida IPR |
| Ω-DOCUMENTO | Ω-Object |  |

## Omega processes

### Omega processes
| id | type | name | source | target | actor |
| --- | --- | --- | --- | --- | --- |
| P-INGRESAR | Ω-Transform | Ingresar Postulación | POSTULACION_EXTERNA | POSTULACION_REGISTRADA | OFICINA-PARTES |
| P-FILTRAR-CDR | Ω-Transform | Filtrar Pertinencia CDR | POSTULACION_REGISTRADA | PRE_ADMISIBLE \| NO_PRE_ADMISIBLE | CDR |
| P-REVISAR-FORMAL | Ω-Transform | Revisar Admisibilidad Formal | PRE_ADMISIBLE | ADMISIBLE \| ADMISIBLE_OBS \| INADMISIBLE | ANALISTA-DIPIR |
| P-EVALUAR-SNI | Kleisli(Ω-RATE) | Evaluar Técnico-Económico SNI | Ω-IDI | T_RATE(Ω-IDI) | MDSF |
| P-EVALUAR-PPR | Kleisli(Ω-RF) | Evaluar Programa Glosa 06 | Ω-PPR | T_RF(Ω-PPR) | DIPRES/SES |
| P-EVALUAR-TRANSFER | Kleisli(Ω-ITF) | Evaluar Transferencia Pública | Ω-PPR-TRANSFER | T_ITF(Ω-PPR-TRANSFER) | GORE |
| P-EVALUAR-CONCURSO | Kleisli(Ω-CONCURSO) | Evaluar Concurso Competitivo | Ω-SUBVENCION \| Ω-FRPD | T_CONC(IPR) | COMITE-EVALUADOR |
| P-APROBAR-CORE | Ω-Align | Aprobar Financiamiento CORE | CARTERA_RS | APROBADO_CORE \| RECHAZADO_CORE | CORE |
| P-EMITIR-CDP | Ω-Transform | Emitir CDP | APROBADO_CORE \| APROBADO_TECNICO | CDP_EMITIDO | PRESUPUESTO |
| P-FORMALIZAR-CONVENIO | Ω-Transform | Formalizar Convenio | CDP_EMITIDO | CONVENIO_FIRMADO | ['GOBERNADOR', 'UT-RECEPTORA'] |
| P-TRAMITAR-RESOLUCION | Ω-Transform | Tramitar Resolución Aprobatoria | CONVENIO_FIRMADO | CONVENIO_TRAMITADO | ['PRESUPUESTO', 'CGR'] |
| P-EJECUTAR | Coalgebra | Ejecutar IPR | CONVENIO_TRAMITADO | EN_EJECUCION |  |
| P-MODIFICAR | Ω-Transform | Gestionar Modificación | EN_EJECUCION | MODIFICACION_APROBADA \| MODIFICACION_RECHAZADA | DIPIR |
| P-CERRAR-TECNICO | Ω-Transform | Cierre Técnico | EJECUCION_COMPLETA | CIERRE_TECNICO | SUPERVISOR-GORE |
| P-CERRAR-FINANCIERO | Ω-Transform | Cierre Financiero | CIERRE_TECNICO | CERRADO | DAF |

## Omega coalgebra

### Id
Ω-IPR-LIFECYCLE

### Type
Coalgebra

### Functor
F(S) = (Event × S) + Termination

### State space

#### Fase 1 ingreso
- FORMULACION
- POSTULADA
- PRE_ADMISIBLE_CDR
- NO_PRE_ADMISIBLE
- PARA_REVISION_TECNICA
- EN_CARTERA_PRE_ADMISIBLE
- ADMISIBLE
- ADMISIBLE_OBS
- INADMISIBLE

#### Fase 2 evaluacion
- ENVIADO_MDSF
- ENVIADO_DIPRES
- EN_EVALUACION_GORE
- RS
- RF
- AD
- FI
- OT
- ELEGIBLE
- NO_ELEGIBLE
- APROBADO_TECNICO

#### Fase 3 financiamiento
- CARTERA_CORE
- APROBADO_CORE
- RECHAZADO_CORE
- CDP_EMITIDO
- ENVIADO_FINANCIAMIENTO

#### Fase 4 formalizacion
- CONVENIO_FIRMADO
- CONVENIO_TRAMITADO
- TRANSFERENCIA_PROGRAMADA

#### Fase 5 ejecucion
- EN_EJECUCION
- LICITACION_EN_CURSO
- ADJUDICADO
- CONTRATO_FIRMADO
- OBRA_EN_TERRENO

#### Fase 6 modificaciones
- MODIFICACION_SOLICITADA
- MODIFICACION_EN_EVALUACION
- MODIFICACION_APROBADA
- MODIFICACION_RECHAZADA

#### Fase 7 cierre
- RECEPCION_PROVISORIA
- RECEPCION_DEFINITIVA
- CIERRE_TECNICO
- CIERRE_FINANCIERO
- CERRADO

#### Terminales
- CERRADO
- INADMISIBLE_INFORMADO
- OT
- RECHAZADO_CORE
- NO_PRE_ADMISIBLE

### Transitions
| from | to | event | morphism |
| --- | --- | --- | --- |
| FORMULACION | POSTULADA | Ingreso Oficio Oficina de Partes | P-INGRESAR |
| POSTULADA | PRE_ADMISIBLE_CDR | Sesión CDR | P-FILTRAR-CDR |
| PRE_ADMISIBLE_CDR | ADMISIBLE | Revisión Formal OK | P-REVISAR-FORMAL |
| ADMISIBLE | ENVIADO_MDSF | Oficio a MDSF |  |
| ENVIADO_MDSF | RS | RATE favorable | P-EVALUAR-SNI |
| RS | APROBADO_CORE | Votación CORE | P-APROBAR-CORE |
| APROBADO_CORE | CDP_EMITIDO | Emisión CDP | P-EMITIR-CDP |
| CDP_EMITIDO | CONVENIO_FIRMADO | Firma bilateral | P-FORMALIZAR-CONVENIO |
| CONVENIO_FIRMADO | CONVENIO_TRAMITADO | Toma de Razón CGR | P-TRAMITAR-RESOLUCION |
| CONVENIO_TRAMITADO | EN_EJECUCION | Transferencia de fondos | P-EJECUTAR |
| EN_EJECUCION | CIERRE_TECNICO | Recepción definitiva | P-CERRAR-TECNICO |
| CIERRE_TECNICO | CERRADO | Rendición aprobada | P-CERRAR-FINANCIERO |

## Omega constructions

### Omega constructions
| id | type | name |
| --- | --- | --- |
| Ω-MECANISMO-FIBRATION | GrothendieckFibration | Polimorfismo de Mecanismos de Financiamiento |
| Ω-ADMISIBILIDAD-PULLBACK | Pullback | Admisibilidad como Límite |
| Ω-SELECTOR-ADJUNCTION | Adjunction | Selector de Vías como Funtor Libre |

## Omega monads

### Omega monads
| id | type | name | applies_to | evaluator | structure |
| --- | --- | --- | --- | --- | --- |
| Ω-RATE-MONAD | Monad | Evaluación Técnico-Económica SNI | ['MEC-SNI-GENERAL', 'MEC-C33-CONSERVACION', 'MEC-5000UTM'] | MDSF | T_RATE(X) = X × {RS} + X × {AD} + {FI(gaps)} + {OT(reason)} |
| Ω-RF-MONAD | Monad | Evaluación Ex-Ante de Programas | ['MEC-G06-DIRECTA'] | DIPRES/SES | T_RF(X) = X × {RF} + {FI(obs)} + {OT(rechazo)} |
| Ω-ITF-MONAD | Monad | Evaluación Interna de Transferencias | ['MEC-TRANSFER-PUB'] | GORE | T_ITF(X) = X × {ITF_OK} + X × {ITF_OBS} + {NO_REC} |
| Ω-CONCURSO-MONAD | Monad | Evaluación Competitiva por Mérito | ['MEC-SUBV8', 'MEC-FRPD-CAPITAL', 'MEC-FRPD-PROGRAMA'] | Comité_Evaluador | T_CONC(X) = X × {ELEGIBLE, puntaje} + {NO_ELEGIBLE} + {LISTA_ESPERA} |
| Ω-TECNICA-MONAD | Monad | Evaluación Técnica GORE (Exenta) | ['MEC-FRIL', 'MEC-5000UTM'] | GORE (DIPRES/DIINF) | T_TEC(X) = X × {APROBADO} + {OBSERVADO} + {RECHAZADO} |

## Omega profunctor

### Id
Ω-GESTION-IPR-PROFUNCTOR

### Type
Profunctor

### Signature
Π: Selector^op × Gestión → Set

### Source category
kb_gn_011_selector_ipr_koda.yml

### Target category
kb_gn_019_gestion_ipr_koda.yml

### Mappings
| selector |
| --- |
| MEC-SNI-GENERAL |
| MEC-FRIL |
| MEC-G06-DIRECTA |
| MEC-TRANSFER-PUB |
| MEC-SUBV8 |
| MEC-FRPD-CAPITAL |

### Composition law
Selector(M) determina unívocamente Track(Fase2) y Dictamen

## Omega axioms

### Omega axioms
| id | statement |
| --- | --- |
| AX-MECANISMO-DETERMINA-TRACK | El mecanismo de financiamiento determina unívocamente el track de evaluación |
| AX-PULLBACK-ADMISIBILIDAD | La admisibilidad es el pullback de requisitos sobre documentos presentados |
| AX-MONAD-PROPAGATION | FI/OT se propagan monádicamente; RS/RF/AD/ITF habilitan bind a siguiente fase |
| AX-FIBRATION-TRANSPORT | Cambiar de mecanismo requiere funtor de transporte entre fibras |
| AX-COALGEBRA-TERMINATION | Todo estado tiene transición a estado sucesor o a terminal |
| AX-CORE-OBLIGATORIO | IDI > 7000 UTM requiere paso por CORE (invariante institucional) |
| AX-DICTAMEN-EXCLUSIVO | Cada mecanismo tiene exactamente un sistema de dictamen aplicable |
| AX-PROFUNCTOR-DETERMINISMO | El profuntor Selector→Gestión es funcional (determinista) |
| AX-EXENTO-NO-BYPASA | Exención de evaluación central NO implica ausencia de evaluación |

---
_manifest:
  urn: urn:gn:kb:omega-ipr-gestion-fusion
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml
version: 2.0.0
status: published
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
    cr: 1.25
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Fusion semantica IPR/Gestion; requiere validacion de alcance.
    dependencies: []
    expected_sections:
    - Contenido
    document_family: omega
    publication_class: knowledge
    skeleton_count: 7
    meat_count: 629
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__omega-ipr-gestion-fusion.md.json
---

# Ontología Ω-IPR: Gestión y Fusión de Financiamiento

## Resumen
Fusion semantica IPR/Gestion; requiere validacion de alcance.
Fusión categorial profunda de los dominios de Gestión Operacional IPR y 
Selector de Vías de Financiamiento. Utiliza construcciones universales:
- Fibración de Grothendieck para polimorfismo de mecanismos
- Mónadas separadas para cada sistema de evaluación (RATE, RF, ITF, CONCURSO)
- Coalgebra para ciclo de vida IPR
- Pullback para admisibilidad documental
- Profuntor Selector ↔ Gestión

### Estadísticas
- Tipo: Ω-Ontology
- Fecha: 2025-12-25
- Objetos Ω: 5
- Procesos Ω: 15
- Axiomas Ω: 9

### Referencias
- [Gestión Operacional de Intervenciones Públicas Regionales (IPR)](urn:gn:kb:gestion-ipr)
- [Selector de Vías de Financiamiento — IPR GORE Ñuble](urn:gn:kb:selector-ipr)

## Objetos Ω
| ID | Tipo | Descripción |
| --- | --- | --- |
| Ω-IPR | Ω-Object | Intervención Pública Regional: unidad atómica de financiamiento del GORE |
| Ω-MECANISMO | Ω-Object (Fiber Index) | Vía de financiamiento que determina reglas, proceso y sistema de evaluación |
| Ω-DICTAMEN | Ω-Object (Effect Constructor) | Resultado de evaluación según sistema aplicable |
| Ω-ACTOR | Ω-Object (Agent) | Agentes que participan en el ciclo de vida IPR |
| Ω-DOCUMENTO | Ω-Object |  |

## Procesos Ω
| ID | Nombre | Tipo | Actor |
| --- | --- | --- | --- |
| P-INGRESAR | Ingresar Postulación | Ω-Transform | OFICINA-PARTES |
| P-FILTRAR-CDR | Filtrar Pertinencia CDR | Ω-Transform | CDR |
| P-REVISAR-FORMAL | Revisar Admisibilidad Formal | Ω-Transform | ANALISTA-DIPIR |
| P-EVALUAR-SNI | Evaluar Técnico-Económico SNI | Kleisli(Ω-RATE) | MDSF |
| P-EVALUAR-PPR | Evaluar Programa Glosa 06 | Kleisli(Ω-RF) | DIPRES/SES |
| P-EVALUAR-TRANSFER | Evaluar Transferencia Pública | Kleisli(Ω-ITF) | GORE |
| P-EVALUAR-CONCURSO | Evaluar Concurso Competitivo | Kleisli(Ω-CONCURSO) | COMITE-EVALUADOR |
| P-APROBAR-CORE | Aprobar Financiamiento CORE | Ω-Align | CORE |
| P-EMITIR-CDP | Emitir CDP | Ω-Transform | PRESUPUESTO |
| P-FORMALIZAR-CONVENIO | Formalizar Convenio | Ω-Transform | ['GOBERNADOR', 'UT-RECEPTORA'] |
| P-TRAMITAR-RESOLUCION | Tramitar Resolución Aprobatoria | Ω-Transform | ['PRESUPUESTO', 'CGR'] |
| P-EJECUTAR | Ejecutar IPR | Coalgebra |  |
| P-MODIFICAR | Gestionar Modificación | Ω-Transform | DIPIR |
| P-CERRAR-TECNICO | Cierre Técnico | Ω-Transform | SUPERVISOR-GORE |
| P-CERRAR-FINANCIERO | Cierre Financiero | Ω-Transform | DAF |

## Ciclo de vida Ω
Funtor: F(S) = (Event × S) + Termination

### Espacio de estados
| Fase | Estados |
| --- | --- |
| Fase 1 ingreso | FORMULACION, POSTULADA, PRE_ADMISIBLE_CDR, NO_PRE_ADMISIBLE, PARA_REVISION_TECNICA, EN_CARTERA_PRE_ADMISIBLE, ADMISIBLE, ADMISIBLE_OBS, INADMISIBLE |
| Fase 2 evaluacion | ENVIADO_MDSF, ENVIADO_DIPRES, EN_EVALUACION_GORE, RS, RF, AD, FI, OT, ELEGIBLE, NO_ELEGIBLE, APROBADO_TECNICO |
| Fase 3 financiamiento | CARTERA_CORE, APROBADO_CORE, RECHAZADO_CORE, CDP_EMITIDO, ENVIADO_FINANCIAMIENTO |
| Fase 4 formalizacion | CONVENIO_FIRMADO, CONVENIO_TRAMITADO, TRANSFERENCIA_PROGRAMADA |
| Fase 5 ejecucion | EN_EJECUCION, LICITACION_EN_CURSO, ADJUDICADO, CONTRATO_FIRMADO, OBRA_EN_TERRENO |
| Fase 6 modificaciones | MODIFICACION_SOLICITADA, MODIFICACION_EN_EVALUACION, MODIFICACION_APROBADA, MODIFICACION_RECHAZADA |
| Fase 7 cierre | RECEPCION_PROVISORIA, RECEPCION_DEFINITIVA, CIERRE_TECNICO, CIERRE_FINANCIERO, CERRADO |
| Terminales | CERRADO, INADMISIBLE_INFORMADO, OT, RECHAZADO_CORE, NO_PRE_ADMISIBLE |

### Transiciones
| Desde | Hacia | Evento | Morfismo |
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

## Construcciones Ω
| ID | Tipo | Nombre |
| --- | --- | --- |
| Ω-MECANISMO-FIBRATION | GrothendieckFibration | Polimorfismo de Mecanismos de Financiamiento |
| Ω-ADMISIBILIDAD-PULLBACK | Pullback | Admisibilidad como Límite |
| Ω-SELECTOR-ADJUNCTION | Adjunction | Selector de Vías como Funtor Libre |

## Mónadas Ω
| ID | Nombre | Evaluador | Estructura |
| --- | --- | --- | --- |
| Ω-RATE-MONAD | Evaluación Técnico-Económica SNI | MDSF | T_RATE(X) = X × {RS} + X × {AD} + {FI(gaps)} + {OT(reason)} |
| Ω-RF-MONAD | Evaluación Ex-Ante de Programas | DIPRES/SES | T_RF(X) = X × {RF} + {FI(obs)} + {OT(rechazo)} |
| Ω-ITF-MONAD | Evaluación Interna de Transferencias | GORE | T_ITF(X) = X × {ITF_OK} + X × {ITF_OBS} + {NO_REC} |
| Ω-CONCURSO-MONAD | Evaluación Competitiva por Mérito | Comité_Evaluador | T_CONC(X) = X × {ELEGIBLE, puntaje} + {NO_ELEGIBLE} + {LISTA_ESPERA} |
| Ω-TECNICA-MONAD | Evaluación Técnica GORE (Exenta) | GORE (DIPRES/DIINF) | T_TEC(X) = X × {APROBADO} + {OBSERVADO} + {RECHAZADO} |

## Profuntor Ω
Signatura: Π: Selector^op × Gestión → Set
Ley de composición: Selector(M) determina unívocamente Track(Fase2) y Dictamen

### Mapeos
| Selector | Fase 2 | Fase 3 | Dictamen |
| --- | --- | --- | --- |
| MEC-SNI-GENERAL | GN-IPR-F2-TRACK-A-SNI | GN-IPR-F3-CON-CORE | RATE |
| MEC-FRIL | GN-IPR-F2-C-FRIL-8FNDR-FRPD-CIRC33 | GN-IPR-F3-SIN-CORE | APROBACION_TECNICA |
| MEC-G06-DIRECTA | GN-IPR-F2-TRACK-B-PPR | GN-IPR-F3-CON-CORE | RF |
| MEC-TRANSFER-PUB | Evaluación_Interna_GORE | GN-IPR-F3-CON-CORE | ITF |
| MEC-SUBV8 | Concurso_Competitivo | Asignación_Directa_o_Concurso | CONCURSO |
| MEC-FRPD-CAPITAL | FRPD-FASE3-GORE | Depende_Tipo | CONCURSO |

## Axiomas Ω
| ID | Enunciado |
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

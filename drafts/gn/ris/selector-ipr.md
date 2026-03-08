---
_manifest:
  urn: urn:gn:kb:selector-ipr
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- inversion-publica
- financiamiento
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml: 578cc776ec61c76afff987ab3acf43017fdd85346ae42deb18396e79a6321050
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.1
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 20
    meat_count: 604
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__selector-ipr.md.json
---

# Selector de Vías de Financiamiento — IPR GORE Ñuble
## ID
KB-GN-011-SELECTOR-IPR-KODA

## Version
3.1.0

## Status
Published

## Format
KODA/Spec

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
IA-CLAUDE

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-11-25

## Modification Date
2025-11-26

## Ctx
Selector de Vías de Financiamiento GORE

## Primary Source
kb_gn_011_selector_ipr.md

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English, content in original language. Never translate content.
END_LLM_INSTRUCTIONS


## Definiciones Centralizadas
### ID
DEF-CENTRAL
### Def
Conceptos clave transversales documentales
### GORE
#### ID
DEF-GORE
#### Def
Gobierno Regional. Órgano autónomo encargado de la administración superior de cada región de Chile.
### IPR
#### ID
DEF-IPR
#### Def
Iniciativa de Proyectos Regionales. Término genérico para cualquier iniciativa (proyecto o programa) que busca financiamiento del GORE.
### FNDR
#### ID
DEF-FNDR
#### Def
Fondo Nacional de Desarrollo Regional. Principal fuente de financiamiento para la inversión pública regional en Chile.
### FRPD
#### ID
DEF-FRPD
#### Def
Fondo Regional para la Productividad y el Desarrollo (FRPD). Fondo específico para iniciativas de productividad y desarrollo, innovación, competitividad, ciencia y tecnología.
### SNI
#### ID
DEF-SNI
#### Def
Sistema Nacional de Inversiones. Marco normativo y metodológico para la evaluación y priorización de la inversión pública en Chile.
### MDSyF
#### ID
DEF-MDSYF
#### Def
Ministerio de Desarrollo Social y Familia. Organismo central encargado de la evaluación técnico-económica de proyectos de inversión pública.
### DIPRES
#### ID
DEF-DIPRES
#### Def
Dirección de Presupuestos. Organismo técnico del Ministerio de Hacienda encargado de la formulación, ejecución y control del Presupuesto del Sector Público.
### SES
#### ID
DEF-SES
#### Def
Subsecretaría de Evaluación Social. Parte del MDSyF, responsable de la evaluación social de proyectos y programas.
### BIP
#### ID
DEF-BIP
#### Def
Banco Integrado de Proyectos. Plataforma informática del SNI donde se registran y gestionan las iniciativas de inversión pública.
### UTM
#### ID
DEF-UTM
#### Def
Unidad Tributaria Mensual. Unidad de cuenta reajustable utilizada en Chile para fines tributarios y multas.
### CLP
#### ID
DEF-CLP
#### Def
Peso Chileno. Moneda oficial de Chile.
### Subt24
#### ID
DEF-SUBT24
#### Def
Subtítulo 24. Transferencias Corrientes. Partida presupuestaria para gastos de operación y transferencias sin contrapartida de capital.
### Subt31
#### ID
DEF-SUBT31
#### Def
Subtítulo 31. Inversión Real. Partida presupuestaria para la adquisición de activos no financieros (inversión directa).
### Subt33
#### ID
DEF-SUBT33
#### Def
Subtítulo 33. Transferencias de Capital. Partida presupuestaria para transferencias destinadas a financiar inversión.
### ANF
#### ID
DEF-ANF
#### Def
Activos No Financieros. Bienes durables que no son financieros (ej. edificios, maquinaria, vehículos).
### IDI
#### ID
DEF-IDI
#### Def
Iniciativa de Inversión. Sinónimo de proyecto de inversión en el contexto del SNI.
### PPR
#### ID
DEF-PPR
#### Def
Programa Público Regional. Iniciativa de gasto corriente o mixto ejecutada por el GORE o transferida a terceros.
### MML
#### ID
DEF-MML
#### Def
Metodología Marco Lógico. Herramienta de planificación y gestión de proyectos y programas.
### CAE
#### ID
DEF-CAE
#### Def
Costo Anual Equivalente. Indicador utilizado en evaluación de proyectos para comparar alternativas con vidas útiles diferentes.
### NIP
#### ID
DEF-NIP
#### Def
Normas de Inversión Pública. Conjunto de regulaciones y directrices que rigen el proceso de inversión pública.
### STS
#### ID
DEF-STS
#### Def
Structured Text Specification. Formato de especificación de texto estructurado.
### KODA
#### ID
DEF-KODA
#### Def
Knowledge Object Document Architecture. Arquitectura de documento para objetos de conocimiento.
### Municipalidad
#### ID
ORG-MUNICIPALIDAD
#### Def
Municipalidad u otra entidad municipal que puede ejecutar proyectos o programas financiados con recursos del GORE.
### SUBDERE
#### ID
ORG-SUBDERE
#### Def
Subsecretaría de Desarrollo Regional y Administrativo. Órgano responsable de lineamientos operativos del FRIL, entre otros fondos.
### Plataforma BIP
#### ID
PLAT-BIP
#### Def
Plataforma informática del Banco Integrado de Proyectos.
#### Ref
DEF-BIP

## Contexto General
### ID
CTX-SELECTOR-IPR
### Purp
Orientar selección estratégica mecanismo financiamiento
### Ref GORE
DEF-GORE
### Ref IPR
DEF-IPR
### Dest
Formuladores, planificadores, decisores
### Obj
Proveer marco discernimiento PREVIO formulación detallada determinar vía financiamiento idónea
### Pregunta Guia
#### ID
CTX-PREGUNTA-CENTRAL
#### Def
¿Dada IPR, qué vía más adecuada?
#### Ref IPR
DEF-IPR
#### Ref SNI
DEF-SNI
### Principio Rector
#### ID
CTX-PRINCIPIO-RECTOR
#### Def
Correcta clasificación naturaleza IPR (proyecto vs programa) y ejecutor determina vía financiamiento y proceso evaluación aplicable
#### Ref IPR
DEF-IPR
#### Ref SNI
DEF-SNI
#### Ref MML
DEF-MML
#### Prohib
Este documento NO es guía formulación detallada
#### Res
Elección informada optimiza alineación, agiliza aprobación, maximiza impacto regional

## Catalogo Mecanismos
### ID
CAT-MECANISMOS-GORE
### Def
Portafolio mecanismos aplicación fondos inversión regional, cada uno con propósito, regulación, proceso evaluación específico
### Ref GORE
DEF-GORE
### Ref FNDR
DEF-FNDR
### Ref FRPD
DEF-FRPD
### IPR Proyecto
#### ID
CAT-IPR-PROYECTO
#### Def
Iniciativa gasto capital crear/ampliar/reponer/mejorar activos físicos/intangibles larga duración
#### Ref IDI
DEF-IDI
#### Caracteristicas
#### Naturaleza Gasto
- DEF-SUBT31
- DEF-SUBT33
#### Producto
Activo durable o intangible vida útil >1 año
#### Proceso Evaluacion Primario
DEF-SNI
#### Plataforma Primaria
DEF-BIP
#### Ctx
kb_gn_024_guia_idi_sni.md
#### Mecanismo SNI General
#### ID
MEC-SNI-GENERAL
#### Purp
Financiar proyectos inversión que por complejidad o monto no califican vías simplificadas
#### Ref
- MEC-FRIL
- MEC-C33
#### Warn Principio Proporcionalidad
#### ID
WARN-SNI-PROPORCIONALIDAD
#### Def
SNI NO es proceso único. Rigor se adapta según magnitud proyecto
#### Ctx
kb_gn_024_guia_idi_sni.md#KB-GN-024-SNI-PROPORCIONALIDAD-01
#### Proceso Maduracion Preinversional
#### ID
PROC-MADURACION-SNI
#### Def
Proyectos complejos deben madurar por etapas estudio para reducir incertidumbre
#### Proc
Idea → Perfil → Prefactibilidad → Factibilidad
#### Niveles Profundidad Evaluacion
#### ID
PROC-NIVELES-EVAL-SNI
#### Def
SNI aplica distintos niveles análisis. Proyectos simples tienen requisitos reducidos, complejos exigen mayor rigor
#### Ctx
kb_gn_024_guia_idi_sni.md#KB-GN-024-SNI-PROPORCIONALIDAD-01
#### Req Evaluacion
#### ID
REQ-EVAL-MDSF
#### Ref Evaluador
DEF-MDSYF
#### Res Nombre
RATE (Resultado Análisis Técnico-Económico)
#### RATE Posibles
#### RS
#### ID
RATE-RS
#### Def
Recomendado Satisfactoriamente - Aprobado financiamiento
#### FI
#### ID
RATE-FI
#### Def
Falta Información - Devuelto con observaciones subsanar
#### OT
#### ID
RATE-OT
#### Def
Objetado Técnicamente - Rechazado problemas fondo
#### AD
#### ID
RATE-AD
#### Def
Admisibilidad - Estado que acredita cumplimiento mínimo para control y registro sin evaluación socioeconómica completa.
#### Fnd
DL 1.263 Art.19bis
#### Ref NIP
DEF-NIP
#### Ctx
kb_gn_024_guia_idi_sni.md
#### Mecanismo FRIL
#### ID
MEC-FRIL
#### Purp
Agilizar financiamiento proyectos infraestructura menor escala
#### Dest
Exclusivo ejecución
#### Ref Ejecutor
ORG-MUNICIPALIDAD
#### Caracteristicas
#### Tope Costo
#### ID
FRIL-TOPE-COSTO
#### Def
Proyectos costo total <5.000 UTM
#### Tope Regional Nuble
4.545 UTM
#### Monto Minimo
$100.000.000 CLP
#### Ref
- DEF-UTM
- DEF-CLP
#### Exencion RS
#### ID
FRIL-EXENCION-RS
#### Def
Proyectos municipales <5.000 UTM no requieren informe favorable MDSyF. Debe ingresarse al SNI información necesaria para control/registro.
#### Ref
- DEF-MDSYF
- RATE-RS
#### Ventaja Estrategica Conservacion
#### ID
FRIL-VENTAJA-CONSERVACION
#### Def
Para Proyectos Conservación calificados, vía más ágil porque NO requiere AD
#### Ref
- DEF-MDSYF
- MEC-C33
#### Prohibiciones
#### ID
FRIL-PROHIB
#### Items
- NO financia adquisición activos aislados (vehículos, equipamiento no indispensable obra)
- Costo activos no financieros NO puede superar 10% costo total proyecto
- NO financia proyectos fraccionados por etapas para eludir umbrales
#### Req Postulacion
#### ID
FRIL-REQ-POSTULACION
#### Def
Proceso postulación vía concursos calendarizados (llamados) con cupos limitados comuna, evaluación mérito GORE
#### Warn
NO es asignación automática
#### Req Registro SNI
#### ID
FRIL-REQ-SNI
#### Def
Ingreso de información necesaria al SNI para fines de control/registro (no depende de contar con informe favorable MDSyF en el tramo <5.000 UTM).
#### Fnd
Ley de Presupuestos 2026 Partida 31 Glosa 12 (GN-LEY-PPTO-2026-P31-GLO-12): Resolución Exenta N°15.051/2023 SUBDERE; Oficio Ordinario N°2/26.01.2024 MH y MDSyF e instructivo asociado.
#### Ctx
kb_gn_026_guia-fril.md
#### Mecanismo Circular33
#### ID
MEC-C33
#### Purp
Simplificar y agilizar evaluación/financiamiento IPRs tipo proyecto características específicas menor complejidad
#### Warn Modificacion Normativa
#### ID
WARN-C33-MODIFICACION
#### Def
Grado simplificación y autonomía modificado por normativa vigente, especialmente Conservaciones y Emergencias
#### Aplicabilidad
#### Estudios Basicos
#### ID
C33-ESTUDIOS
#### Warn
Sujeto restricciones. Estudios propio GORE financian con presupuesto funcionamiento. Estudios terceros requieren autorización especial DIPRES
#### Adquisicion ANF
#### ID
C33-ANF
#### Def
Adquisición ANF que NO forman parte proyecto mayor
#### Ref ANF
DEF-ANF
#### Ref DIPRES
DEF-DIPRES
#### Warn
Modificaciones presupuestarias requieren visación
#### Req Cofinanciamiento
#### ID
C33-ANF-COFINANCIA
#### Def
Exige cofinanciamiento ≥20% costo total por institución solicitante
#### Req Certificados
#### ID
C33-ANF-REQ-CERT
#### Req
- Si corresponde a compra de nuevos activos no financieros: incorporar certificado de disponibilidad presupuestaria para gastos recurrentes emitido por el Ministerio o Subsecretaría respectiva.
- Compras para Fuerzas de Orden y Seguridad Pública: certificado de pertinencia emitido por el Ministerio de Seguridad Pública.
- Activos no financieros para Bomberos: certificado de pertinencia técnica emitido por la Junta Nacional de Bomberos de Chile.
- Compra de terrenos: efectuar coordinación con SERVIU regional cuando corresponda.
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-09
#### Proyectos Conservacion
#### ID
C33-CONSERVACION
#### Warn Perdida Autonomia
#### Def
Aunque vía simplificada sin evaluación técnico-económica completa, normativa vigente exige ingreso BIP para obtener estado AD como requisito registro control
#### Ref
- DEF-BIP
- RATE-AD
- DEF-MDSYF
#### Condiciones Viabilidad
#### Cond Costo
#### ID
C33-CONS-COND-COSTO
#### Def
Costo reparación ≤30% costo reponer activo completo
#### Cond Vida Util
#### ID
C33-CONS-COND-VIDAUTIL
#### Def
Si activo cumplió vida útil, requiere estudio CAE demuestre mantener más conveniente que reponer
#### Ref CAE
DEF-CAE
#### Ref SNI
DEF-SNI
#### Warn
Si supera 30% costo, debe ir evaluación SNI completa
#### Proyectos Reconstruccion
#### ID
C33-RECONSTRUCCION
#### Prohib
Vía NO financia fases Respuesta o Rehabilitación inmediata. Estas gestionan directamente con DIPRES
#### Ref DIPRES
DEF-DIPRES
#### Res
Permite vías evaluación más rápidas/simplificadas que proceso SNI completo, pero con nuevas dependencias organismos centrales
#### Fnd
Circular N°33/2009 MINHAC, Ley de Presupuestos 2026 (Ley N°21.796).
#### Ref NIP
DEF-NIP
#### Ctx
kb_gn_029_guia-circ33.md
### IPR Programa
#### ID
CAT-IPR-PROGRAMA
#### Def
IPR mediante conjunto acciones/prestaciones busca resolver problema población objetivo mediante entrega servicios/transferencias, NO creación activos físicos
#### Ref IPR
DEF-IPR
#### Ref Gasto
DEF-SUBT24
#### Caracteristicas
#### Naturaleza Gasto
DEF-SUBT24
#### Producto
Entrega continua prestaciones, cambio condición población
#### Proceso Evaluacion Primario
#### ID
PROC-EVAL-PROGRAMA-EJECUTOR
#### Def
Depende críticamente QUIÉN ejecuta iniciativa
#### Plataforma Primaria
Formularios Perfil/Diseño, Plataformas postulación
#### Ref GORE
DEF-GORE
#### Warn Division Vias
#### ID
WARN-PROGRAMA-DIVISION-VIAS
#### Def
PPR divide en dos vías mutuamente excluyentes según ejecutor
#### Ref PPR
DEF-PPR
#### Mecanismo Glosa06 Directa
#### ID
MEC-G06-DIRECTA
#### Purp
Financiar programas donde GORE es responsable principal implementación y entrega servicios
#### Dest
Programas ejecutados directamente GORE (con personal y recursos propios)
#### Denominaciones Comunes
#### ID
G06-DENOM
#### Items
- Programa Público Regional (PPR) Ejecución Directa
- Programa Vía Glosa 06
- Programa Evaluación Ex-Ante
#### Warn No Confundir
#### ID
WARN-G06-NO-CONFUNDIR-SNI
#### Def
NO confundir con 'Programa Inversión' SNI. Evaluación ex-ante PPR se rige por DIPRES/SES (RF), y la oferta programática ejecutada directamente por GORE está sujeta al Sistema de Evaluación y Monitoreo del MDSyF y DIPRES.
#### Ref
- DEF-SNI
- DEF-PPR
- DEF-DIPRES
- DEF-SES
- DEF-MDSYF
#### Req Evaluacion Bifasica
#### ID
REQ-G06-EVAL-BIFASICA
#### Def
Proceso bifásico evaluación ex-ante
#### Fase1 Perfil
#### ID
G06-FASE1-PERFIL
#### Proc
Presentar Formulario Perfil a DIPRES/SES para primer filtro pertinencia
#### Fase2 Diseno
#### ID
G06-FASE2-DISENO
#### Proc
Solo si perfil aprobado, elaborar/presentar Formulario Diseño detallado para evaluación fondo
#### Res Objetivo
Recomendación Favorable (RF)
#### Resultado Recomendacion Favorable
#### ID
RATE-RF
#### Def
Recomendación Favorable - Dictamen DIPRES/SES que habilita uso de recursos vía Glosa 06.
#### Req Metodologia
#### ID
REQ-G06-MML
#### Def
Formulación obligatoria bajo MML
#### Ref MML
DEF-MML
#### Req Excepciones Evaluacion Ex Ante
#### ID
G06-REQ-EXCEP-EXANTE
#### Cpt
- Se exceptuarán del proceso de evaluación ex-ante: programas que hayan iniciado su ejecución en años anteriores; subvenciones asociadas al Concurso de Vinculación con la Comunidad 8%; transferencias a universidades, municipalidades, otras entidades públicas y gobierno central e instituciones privadas beneficiarias sin fines de lucro; ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias y desastres naturales (en coordinación con el Ministerio del Interior).
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-06
#### Req Tope Administracion 5pct
#### ID
G06-REQ-TOPE-ADM-5PCT
#### Def
Podrá destinarse hasta un 5% del monto total de la transferencia a gastos que demande la administración de las iniciativas en el Gobierno Regional (personal, bienes y servicios de consumo y adquisición de activos no financieros, asociados con la ejecución del programa). El personal contratado a honorarios con cargo a este 5% tendrá la calidad de agente público.
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-06
#### Warn Convenios Transferencias
#### ID
WARN-G06-CONVENIOS-ART24
#### Warn
Cuando existan convenios de transferencia con instituciones privadas, aplicar obligaciones y prohibiciones de convenios/rendición establecidas en la Ley de Presupuestos vigente (incluye rendición vía Sistema de Rendición Electrónica de Cuentas).
#### Ctx
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25
#### Fnd
Ley de Presupuestos 2026 Partida 31 Glosa 06 (GN-LEY-PPTO-2026-P31-GLO-06), Oficio Circular N°22 (o vigente).
#### Ref DIPRES
DEF-DIPRES
#### Ctx
kb_gn_025_guia-programas.md
#### Mecanismo Transferencia Publico
#### ID
MEC-TRANSFER-PUB
#### Purp
Financiar programas donde entidad pública distinta GORE ejecuta iniciativa
#### Dest
Instituciones públicas (Servicios Públicos, Municipalidades, Universidades Estado)
#### Denominaciones Comunes
#### ID
TRANSFER-PUB-DENOM
#### Items
- Transferencia Programa Instituciones Públicas
- Programa Ejecución Indirecta
- Programa Exención Glosa 06 letra c
#### Warn Exencion No Simplifica
#### ID
WARN-TRANSFER-EXENCION
#### Def
Exención evaluación central (DIPRES/SES) NO implica proceso simple. Reemplazada por riguroso proceso evaluación interno GORE
#### Caracteristicas
#### Fnd Exencion
#### ID
TRANSFER-FND-EXENCION
#### Def
Exención evaluación ex-ante DIPRES/SES según Glosa 06 letra c
#### Req Evaluacion GORE
#### ID
REQ-TRANSFER-EVAL-GORE
#### Def
Proceso formal GORE multifásico
#### Proc
- 1) Admisibilidad Documental
- 2) Pertinencia Estratégica Comité Regional
- 3) Evaluación Técnica Diseño (MML)
#### Res Culmina
Informe Técnico Favorable (ITF) interno
#### Req Metodologia
#### ID
REQ-TRANSFER-MML
#### Def
Formulación obligatoria bajo Metodología Marco Lógico (MML)
#### Prohib SNI
#### ID
PROHIB-TRANSFER-SNI
#### Def
NO usa metodología SNI ni BIP
#### Restricciones Gasto
#### ID
TRANSFER-RESTRIC-GASTO
#### Def
Uso fondos estrictamente regulado
#### Tope Personal
#### ID
TRANSFER-TOPE-PERSONAL
#### Def
Tope máximo 5% contratación personal a honorarios por entidad pública receptora. Vínculo cesa de pleno derecho al finalizar el convenio de transferencia.
#### Ctx
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-06
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART07
#### Modalidad Transferencia Municipal
#### ID
TRANSFER-MODAL-MUNICIPAL
#### Def
Para municipalidades, transferencia directa fondos (no consolidable)
#### Warn
NO exime riguroso proceso evaluación interno GORE que reemplaza evaluación central
#### Ctx
kb_gn_001_guia-transferencia-programas.md
#### Mecanismo Subvencion 8pct
#### ID
MEC-SUBV8
#### Purp
Subvencionar actividades acotadas interés comunitario, NO programas públicos complejos
#### Dest
Principalmente instituciones privadas sin fines lucro, organizaciones comunitarias. Municipalidades acceso fondos específicos con reglas/montos diferenciados
#### Warn Error Conceptual
#### ID
WARN-SUBV8-ERROR-CONCEPTO
#### Def
Vía NO financia "Programas Públicos Regionales" (PPR) con lógica resolución problemas estructurales, sino "actividades" corta duración (ej. talleres, festivales, campañas)
#### Req Evaluacion Competitiva
#### ID
REQ-SUBV8-EVAL-COMPETITIVA
#### Def
Proceso altamente formalizado y competitivo basado en mérito según bases concursales GORE.
#### Proc Portafolio
#### ID
SUBV8-PROC-PORTAFOLIO
#### Def
Organizado como portafolio múltiples fondos temáticos (Cultura, Deporte, Social, Seguridad, etc.)
#### Def Caracteristicas
Cada fondo con presupuesto, reglas, montos máximos proyecto varían según área y tipo organización postulante
#### Proc Seleccion Puntaje
#### ID
SUBV8-PROC-PUNTAJE
#### Def
Selección basada sistema puntaje. Iniciativas deben superar umbral calidad para considerarse
#### Prohib Restricciones
#### ID
SUBV8-PROHIB-RESTRIC
#### Items
- Restricciones elegibilidad estrictas (ej. 2 años antigüedad organizaciones)
- Restricciones gasto (ej. NO financiar proyectos únicamente compra equipamiento)
#### Res Exencion
#### ID
SUBV8-RES-EXENCION
#### Def
Exento evaluación SNI y evaluación ex-ante programas DIPRES/SES
#### Cond Asignacion Directa
#### ID
SUBV8-COND-ASIG-DIR
#### Cond
Se podrá asignar hasta un 10% de los recursos del Concurso de Vinculación con la Comunidad 8% para financiar, previo acuerdo del Consejo Regional, mediante asignaciones directas actividades asociadas con casos emblemáticos, excepcionales y emergentes (sujeto a lo dispuesto en Resolución N°72/08.01.2025 DIPRES y sus modificaciones).
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-07
#### Req Convenios y Rendicion
#### ID
SUBV8-REQ-CONVENIOS-ART24
#### Req
- Convenios de transferencia deben cumplir obligaciones y prohibiciones del Art. 24 (incluye rendiciones a través del Sistema de Rendición Electrónica de Cuentas de la CGR).
- Para instituciones privadas ejecutoras de políticas públicas, considerar requisitos adicionales (incluye garantías cuando el monto transferido supere 1.000 UTM).
#### Ctx
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25
#### Fnd
Ley de Presupuestos 2026 Partida 31 Glosa 07 (GN-LEY-PPTO-2026-P31-GLO-07).
#### Ctx
kb_gn_028_instructivo-subvencion-8.md
### IPR Productivo
#### ID
CAT-IPR-PRODUCTIVO
#### Def
Iniciativas (proyectos o programas) orientadas inversión productiva y desarrollo económico regional
#### Fnd Recursos
#### ID
FND-FRPD
#### Def
Fondo Regional para la Productividad y el Desarrollo (FRPD)
#### Mecanismo FRPD
#### ID
MEC-FRPD
#### Purp
Financiar IPRs diversificación productiva, desarrollo económico, investigación/ciencia/tecnología/innovación (I+D+i)
#### Warn Acceso Restringido
#### ID
WARN-FRPD-ACCESO
#### Def
Acceso altamente restringido. Solo pueden postular instituciones explícitamente habilitadas normativa SUBCTCI (principalmente agencias fomento, institutos investigación, universidades acreditadas). NO vía acceso universal
#### Ambitos
#### ID
FRPD-AMBITOS
#### Items
- Fomento productivo
- Desarrollo capital humano
- Apoyo competitividad regional
- I+D+i
#### Req Evaluacion Multifasica
#### ID
REQ-FRPD-EVAL-MULTIFASICA
#### Def
Proceso selección multifásico y competitivo, previo cualquier evaluación fondo
#### Fase1 Admisibilidad Admin
#### ID
FRPD-FASE1-ADMIN
#### Proc
Filtro documental y requisitos básicos
#### Fase2 Admisibilidad Tecnica
#### ID
FRPD-FASE2-TECNICA
#### Proc
Concurso puntaje ante comité evaluador determinar "Elegibilidad"
#### Fase3 Evaluacion GORE
#### ID
FRPD-FASE3-GORE
#### Proc
Revisión fondo iniciativas "Elegibles"
#### Casos Evaluacion
#### Caso CTCI
#### ID
FRPD-CASO-CTCI
#### Def
Iniciativas Ciencia/Tecnología/Conocimiento/Innovación seleccionadas concurso
#### Res
Exentas evaluación ex-ante DIPRES/SES o SNI. Aprobación concurso es final
#### Caso Fomento General
#### ID
FRPD-CASO-FOMENTO
#### Def
Iniciativas NO califican CTCI
#### Req
Ganar concurso previo es solo PREREQUISITO obtener derecho iniciar proceso evaluación estándar completo (Vía Ref: MEC-SNI-GENERAL si proyecto capital, Vía Programas si servicios)
#### Req Provision Sin Distribuir
#### ID
FRPD-REQ-PROVISION-33-03
#### Def
Distribución inicial debe contemplar provisión sin distribuir en Ítem 33.03 para FRPD, desde donde se reasignan recursos.
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-13
#### Req Transferencia Directa Concursos
#### ID
FRPD-REQ-TRANSFER-DIRECTA
#### Def
Faculta transferencias directas para iniciativas seleccionadas en concursos (p.ej. CORFO/ANID), conforme a normativa vigente y ejecutores habilitados.
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-13
#### Fnd
Ley N°21.591 (Royalty Minero); Ley de Presupuestos 2026 Partida 31 Glosa 13 (GN-LEY-PPTO-2026-P31-GLO-13): Decreto N°1699/2025 MH; Resolución Exenta N°33/2024 MinCiencia y sus modificaciones; Resolución Exenta N°08/2025 Subsecretaría de Economía y sus modificaciones.
#### Ctx
kb_gn_027_guia-frpd.md

## Marco Regulatorio
### ID
REG-MARCO-GENERAL
### Purp
Detallar fundamento jurídico y normativo cada vía financiamiento, establecer jerarquía reglas gobiernan asignación recursos
### Marco Transversal
#### ID
REG-TRANSVERSAL
#### Def
Normas carácter general proveen marco fundamental toda inversión regional
#### Pilares Normativos
#### LOC GORE
#### ID
REG-LOC-GORE
#### Nombre
Ley Orgánica Constitucional Gobiernos Regionales (DFL 1-19.175)
#### Fnd
Otorga GORE facultad "Decidir inversión" (Art.16f), "Ejecutar programas regionales" (Art.20k)
#### Req
Conecta administración fondos (FNDR) con obligación evaluación técnica (Art.75)
#### DL 1263
#### ID
REG-DL-1263
#### Nombre
Decreto Ley N°1.263 (Adm. Financiera Estado)
#### Fnd
Establece base SNI, exige informe favorable iniciativas inversión (Art.19bis)
#### Ref
- DEF-SNI
- DEF-MDSYF
#### Ley Presupuestos
#### ID
REG-LEY-PRESUP
#### Nombre
Ley Presupuestos Sector Público (Anual)
#### Fnd
Instrumento operativo asigna recursos, establece reglas específicas (Glosas)
#### Ref
- DEF-FNDR
- DEF-FRPD
#### Glosa 03
#### ID
REG-GLOSA-03
#### Prohib
Usar recursos inversión regional para financiar préstamos o gastos en personal o bienes y servicios de consumo de entidades receptoras, ni para constituir/efectuar aportes/comprar sociedades o empresas, salvo autorizaciones expresas en glosas.
#### Ctx
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-03
#### Normas Generales 2026
#### ID
REG-NORMAS-GENERALES-2026
#### Nombre
Ley de Presupuestos 2026 - Normas Generales
#### Fnd
Reglas transversales (licitación por umbrales, decretos/transferencias, autorizaciones previas DIPRES).
#### Ctx
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART06
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART07
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART12
### Base SNI C33
#### ID
REG-SNI-C33
#### Ref Mecanismos
- MEC-SNI-GENERAL
- MEC-C33
#### Fundamentos
#### SNI
#### ID
REG-FND-SNI
#### Src
DL 1.263 Art.19bis, Ley 20.530 (Rol SES/MDSyF)
#### Req
Evaluación técnico-económica todo proyecto capital
#### Ref
- DEF-FNDR
- DEF-FRPD
#### Circular 33
#### ID
REG-FND-C33
#### Src
Acto administrativo MINHAC, Circular N°33/2009
#### Req
Provee vía simplificada evaluación IPRs específicas
#### Ref
- DEF-IPR
- DEF-ANF
### Base Glosa06 Directa
#### ID
REG-GLOSA06-DIRECTA
#### Ref Mecanismo
MEC-G06-DIRECTA
#### Fundamentos
#### Glosa 06
#### ID
REG-FND-GLOSA06
#### Src
Ley de Presupuestos 2026 Partida 31 Glosa 06 (GN-LEY-PPTO-2026-P31-GLO-06).
#### Req Habilitacion
Habilita uso recursos inversión programas ejecución directa
#### Ref
- DEF-SUBT24
- DEF-GORE
- RATE-RF
- DEF-DIPRES
- DEF-SES
#### Req Evaluacion
Exige RF programas nuevos o reformulados
#### Circular 22
#### ID
REG-FND-CIRC22
#### Src
Acto administrativo, Oficio Circular N°22 (o vigente)
#### Ref DIPRES
DEF-DIPRES
#### Ref RF
RATE-RF
#### Req
Detalla procedimiento evaluación ex-ante (Perfil y Diseño) obtener RF
### Base Transferencia Publico
#### ID
REG-TRANSFER-PUB
#### Ref Mecanismo
MEC-TRANSFER-PUB
#### Fundamentos
#### Glosa 06 Letra C
#### ID
REG-FND-GLOSA06-C
#### Src
Ley de Presupuestos 2026 Partida 31 Glosa 06 (GN-LEY-PPTO-2026-P31-GLO-06).
#### Req
Exime explícitamente "transferencias otras entidades públicas y gobierno central" evaluación ex-ante
#### Ref
- DEF-DIPRES
- DEF-SES
#### Ctx
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25
#### Guia GORE
#### ID
REG-FND-GUIA-GORE-TRANSFER
#### Src
Documento normativo interno
#### Ref GORE
DEF-GORE
#### Ctx
kb_gn_001_guia-transferencia-programas.md
#### Req
Establece procedimiento postulación, admisibilidad, evaluación técnica/financiera interna reemplaza evaluación Circular 22
### Base FRIL
#### ID
REG-FRIL
#### Ref Mecanismo
MEC-FRIL
#### Fundamentos
#### Glosa 12
#### ID
REG-FND-GLOSA12
#### Src
Ley de Presupuestos 2026 Partida 31 Glosa 12 (GN-LEY-PPTO-2026-P31-GLO-12).
#### Req Transferencias
Regula transferencias municipalidades proyectos infraestructura menor
#### Ref
- DEF-FNDR
- ORG-MUNICIPALIDAD
- RATE-RS
- DEF-UTM
#### Req Exencion
#### Ref
- FRIL-EXENCION-RS
- FRIL-TOPE-COSTO
#### Guia FRIL
#### ID
REG-FND-GUIA-FRIL
#### Src
Lineamientos operativos detallados SUBDERE
#### Ref SUBDERE
ORG-SUBDERE
### Base Subvencion 8pct
#### ID
REG-SUBV8
#### Ref Mecanismo
MEC-SUBV8
#### Fundamentos
#### Glosa 07
#### ID
REG-FND-GLOSA07
#### Src
Ley de Presupuestos 2026 Partida 31 Glosa 07 (GN-LEY-PPTO-2026-P31-GLO-07).
#### Req Asignacion
Regula asignación hasta 8% inversión FNDR subvencionar actividades
#### Req Concurso
Establece concurso público como regla general asignación
#### Req Exencion
Exime iniciativas evaluación Glosa 06 y SNI
### Base FRPD
#### ID
REG-FRPD
#### Ref Mecanismo
MEC-FRPD
#### Fundamentos
#### Ley Royalty
#### ID
REG-FND-LEY-ROYALTY
#### Src
Ley N°21.591 (Royalty Minero), ley permanente
#### Req
Crea FRPD, define propósito exclusivo inversión productiva y desarrollo económico
#### Glosa 13
#### ID
REG-FND-GLOSA13
#### Src
Ley de Presupuestos 2026 Partida 31 Glosa 13 (GN-LEY-PPTO-2026-P31-GLO-13).
#### Req Operativo
Norma uso operativo recursos FRPD año
#### Req Transferencia
Faculta transferencia directa iniciativas seleccionadas CORFO/ANID
#### Resolucion SUBCTCI
#### ID
REG-FND-RES-SUBCTCI
#### Src
Resolución Exenta N°33/2024 MinCiencia y sus modificaciones; Resolución Exenta N°08/2025 Subsecretaría de Economía y sus modificaciones; Decreto N°1699/2025 MH.
#### Req
Define lineamientos, ámbitos acción, instituciones habilitadas ejecutar fondos FRPD I+D+i

## Procesos Evaluacion
### ID
EVAL-PROCESOS
### Purp
Detallar procesos validación técnica/económica IPR debe superar antes obtener financiamiento según vía escogida
### Evaluacion SNI
#### ID
EVAL-SNI
#### Ref Mecanismos
- MEC-SNI-GENERAL
- MEC-FRIL
- MEC-C33
#### Proceso General
#### Responsable
#### ID
EVAL-SNI-RESP
#### Ref
DEF-MDSYF
#### Objetivo
#### ID
EVAL-SNI-OBJ
#### Def
Analizar rentabilidad socioeconómica iniciativa inversión
#### Resultado
#### ID
EVAL-SNI-RES
#### Def
Recomendación Satisfactoria (RS) o Admisibilidad (AD), "pase" obtener financiamiento
#### Ref
- RATE-RS
- RATE-AD
#### Metodologias
#### ID
EVAL-SNI-METOD
#### Def
Metodologías específicas SNI (ej. VAN, CAE)
#### Plataforma
#### ID
EVAL-SNI-PLAT
#### Ref
PLAT-BIP
#### Excepciones Vias Simplificadas
#### Exencion FRIL
#### ID
EVAL-SNI-EXCEP-FRIL
#### Cond
Proyectos municipales <5.000 UTM
#### Res
No requieren informe favorable MDSyF, pero deben ingresar información necesaria al SNI para control/registro.
#### Ref
MEC-FRIL
#### Procedimientos Especiales C33
#### ID
EVAL-SNI-EXCEP-C33
#### Cond
IPRs Conservación, Estudios Básicos, ANF, Emergencias
#### Res
Utilizan procedimientos evaluación agilizados o simplificados
#### Ref
MEC-C33
### Evaluacion Glosa06 Directa
#### ID
EVAL-G06-DIRECTA
#### Ref Mecanismo
MEC-G06-DIRECTA
#### Proceso General
#### Responsable
#### ID
EVAL-G06-RESP
#### Ref
- DEF-DIPRES
- DEF-SES
#### Objetivo
#### ID
EVAL-G06-OBJ
#### Def
Analizar calidad diseño (coherencia, pertinencia) programa nuevo o reformulado
#### Resultado
#### ID
EVAL-G06-RES
#### Def
Recomendación Favorable (RF) habilita solicitud recursos
#### Metodologia
#### ID
EVAL-G06-METOD
#### Def
Marco Lógico
#### Plataforma
#### ID
EVAL-G06-PLAT
#### Def
Formularios Perfil y Diseño
#### Fundamento
#### Ref
REG-FND-CIRC22
### Evaluacion Transferencia Publico
#### ID
EVAL-TRANSFER-PUB
#### Ref Mecanismo
MEC-TRANSFER-PUB
#### Proceso General
#### Fundamento Habilitacion
#### ID
EVAL-TRANSFER-FND
#### Def
Habilitado exención Glosa 06 letra c
#### Ref
REG-FND-GLOSA06-C
#### Responsable
#### ID
EVAL-TRANSFER-RESP
#### Def
Unidades técnicas GORE (Departamento Análisis y Evaluación - DAE, Comité Pertinencia)
#### Objetivo
#### ID
EVAL-TRANSFER-OBJ
#### Def
Asegurar pertinencia estratégica y factibilidad técnica/financiera propuesta
#### Proceso 3 Fases
#### ID
EVAL-TRANSFER-PROC-3F
#### Ref
REQ-TRANSFER-EVAL-GORE
#### Resultado
#### ID
EVAL-TRANSFER-RES
#### Def
Emisión Informe Técnico Favorable (ITF) habilita gestión financiamiento
#### Calificaciones Posibles
#### ID
EVAL-TRANSFER-CALIF
#### Items
- Recomendado Favorablemente
- Recomendado con Observaciones
- No Recomendado
#### Warn No RS
#### ID
EVAL-TRANSFER-WARN-NO-RS
#### Def
Resultado NO es Recomendación Satisfactoria (RS) SNI
#### Metodologia
#### ID
EVAL-TRANSFER-METOD
#### Def
Marco Lógico y criterios definidos guía GORE
#### Ref MML
DEF-MML
#### Plataforma
#### ID
EVAL-TRANSFER-PLAT
#### Def
Plataforma postulación GORE (ej. GESDOC)
#### Fuente
#### Ctx
kb_gn_001_guia-transferencia-programas.md
### Evaluacion Especial Exenta
#### ID
EVAL-ESPECIAL-EXENTA
#### Subvenciones 8pct
#### ID
EVAL-EXENTA-SUBV8
#### Ref
- MEC-SUBV8
- REQ-SUBV8-EVAL-COMPETITIVA
- SUBV8-RES-EXENCION
#### Iniciativas FRPD
#### ID
EVAL-EXENTA-FRPD
#### Ref
MEC-FRPD
#### Proc
Pueden tener mecanismos propios concurso o asignación, especialmente si alinean convocatorias CORFO/ANID

## Arbol Decision
### ID
TREE-SELECTOR-IPR
### Purp
Proveer secuencia lógica preguntas guiar formulador hacia mecanismo más probable y adecuado
### Warn
Guía orientación. Decisión final requiere consulta unidades técnicas GORE
### Paso1 Naturaleza IPR
#### ID
TREE-P1-NATURALEZA
#### Pregunta Guia
¿Propósito principal crear/mejorar activo físico o intangible durable ("cosa") o entregar servicio/prestación forma continua?
#### Decisiones
#### Si Activo Durable
#### ID
TREE-P1-DEC-ACTIVO
#### Res
Ir a Ruta PROYECTOS
#### Ref
TREE-RUTA-PROYECTOS
#### Si Servicio Prestacion
#### ID
TREE-P1-DEC-SERVICIO
#### Res
Ir a Ruta PROGRAMAS
#### Ref
TREE-RUTA-PROGRAMAS
### Ruta Proyectos
#### ID
TREE-RUTA-PROYECTOS
#### Pregunta 1 Municipal FRIL
#### ID
TREE-PROY-P1-FRIL
#### Pregunta
¿Ejecutor Municipalidad, costo <5.000 UTM, proyecto infraestructura?
#### Si Cumple
#### Res
Vía más probable FRIL
#### Ref
MEC-FRIL
#### Warn Recordar
#### Ref
- FRIL-REQ-POSTULACION
- FRIL-PROHIB
- FRIL-EXENCION-RS
- FRIL-REQ-SNI
#### Pregunta 2 Procedimientos Especiales
#### ID
TREE-PROY-P2-C33
#### Pregunta
¿IPR es Conservación, Estudio Básico, Adquisición Activos Aislada, o Reconstrucción?
#### Si Cumple
#### Res
Vía probable Procedimientos Especiales (Circular 33 / NIP)
#### Ref
MEC-C33
#### Warn Verificar
#### Ref
EVAL-SNI-EXCEP-C33
#### Pregunta 3 Foco Productivo
#### ID
TREE-PROY-P3-FRPD
#### Pregunta
¿IPR foco principal productividad/innovación/competitividad económica, postulada entidad habilitada?
#### Si Cumple
#### Res
Fuente fondos natural FRPD (Capital)
#### Ref
MEC-FRPD
#### Warn Recordar
#### Ref
- REQ-FRPD-EVAL-MULTIFASICA
- FRPD-CASO-FOMENTO
#### Pregunta 4 Ninguna Anterior
#### ID
TREE-PROY-P4-SNI
#### Pregunta
¿Ninguna anteriores (ej. construcción hospital, puente)?
#### Si Cumple
#### Res
Vía obligatoria SNI General
#### Ref
MEC-SNI-GENERAL
#### Warn Recordar
#### Ref
- PROC-MADURACION-SNI
- PROC-NIVELES-EVAL-SNI
### Ruta Programas
#### ID
TREE-RUTA-PROGRAMAS
#### Pregunta 1 Organizacion Comunitaria
#### ID
TREE-PROG-P1-SUBV8
#### Pregunta
¿Ejecutor organización comunitaria o privada sin fines lucro, IPR ajusta líneas Cultura/Deporte/Social?
#### Si Cumple
#### Res
Vía más probable Subvención 8% FNDR (vía concurso)
#### Ref
MEC-SUBV8
#### Warn Recordar
#### Ref
- SUBV8-COND-ASIG-DIR
- SUBV8-REQ-CONVENIOS-ART24
#### Pregunta 2 Ejecucion GORE
#### ID
TREE-PROG-P2-G06
#### Pregunta
¿Ejecutor propio GORE, entregará servicios directamente?
#### Si Cumple
#### Res
Vía obligatoria Ejecución Directa GORE (Glosa 06)
#### Ref
MEC-G06-DIRECTA
#### Warn Recordar
#### Ref
- REQ-G06-MML
- REQ-G06-EVAL-BIFASICA
- G06-REQ-TOPE-ADM-5PCT
#### Pregunta 3 Entidad Publica
#### ID
TREE-PROG-P3-TRANSFER
#### Pregunta
¿Ejecutor otra entidad pública (Municipio, Servicio Público, U.Estatal)?
#### Si Cumple
#### Res
Vía obligatoria Transferencia Entidad Pública
#### Ref
MEC-TRANSFER-PUB
#### Warn Recordar
#### Ref
- REQ-TRANSFER-EVAL-GORE
- TRANSFER-TOPE-PERSONAL
- REG-GLOSA-03
#### Pregunta 4 Foco Productivo
#### ID
TREE-PROG-P4-FRPD
#### Pregunta
¿IPR foco principal productividad/innovación/competitividad económica, postulada entidad habilitada?
#### Si Cumple
#### Res
Fuente fondos natural FRPD (Programático)
#### Ref
MEC-FRPD
#### Warn Recordar
#### Ref
- REQ-FRPD-EVAL-MULTIFASICA
- FRPD-CASO-FOMENTO
- FRPD-REQ-PROVISION-33-03
- FRPD-REQ-TRANSFER-DIRECTA
### Criterios Validacion Complementarios
#### ID
TREE-CRITERIOS-VALIDACION
#### Alineamiento Estrategico
#### ID
TREE-VALID-ALINEAMIENTO
#### Req
IPR debe ser coherente Estrategia Regional Desarrollo (ERD) y otros planes regionales
#### Magnitud Complejidad
#### ID
TREE-VALID-MAGNITUD
#### Req
IPRs gran envergadura y complejidad técnica sugieren robustez (y plazos) SNI General
#### Warn Licitacion Publica
#### ID
TREE-VALID-LICITACION
#### Cond
Si el monto supera umbrales de licitación pública obligatoria, ajustar estrategia de compras y plazos: Proyectos/Programas de inversión >1.000 UTM; Estudios Básicos >500 UTM (salvo emergencias según legislación).
#### Ctx
kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART06
#### Urgencia
#### ID
TREE-VALID-URGENCIA
#### Cond
Urgencia calificada puede activar procedimientos emergencia (vía proyectos) o asignaciones directas (vía subvenciones 8%)
#### Ctx
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-14
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-07
#### Transparencia y Reporting
#### ID
TREE-VALID-TRANSPARENCIA
#### Req
Considerar obligaciones de publicación y reportes periódicos asociados a Subt. 24/31/33, umbrales (p.ej. 500 UTM) y transferencias del 8% y FRPD, según Ley de Presupuestos vigente.
#### Ctx
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-16
#### Disponibilidad Presupuestaria
#### ID
TREE-VALID-PRESUPUESTO
#### Req
Selección final siempre supeditada disponibilidad fondos línea financiamiento correspondiente

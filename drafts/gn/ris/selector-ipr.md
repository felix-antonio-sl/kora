---
_manifest:
  urn: urn:gn:kb:selector-ipr
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
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
    cr: 2.19
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 6
    meat_count: 582
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__selector-ipr.md.json
---

# Selector de Vías de Financiamiento — IPR GORE Ñuble

## Definiciones Centralizadas

### Definicion
Conceptos clave transversales documentales

### GORE

#### Definicion
Gobierno Regional. Órgano autónomo encargado de la administración superior de cada región de Chile.

### IPR

#### Definicion
Iniciativa de Proyectos Regionales. Término genérico para cualquier iniciativa (proyecto o programa) que busca financiamiento del GORE.

### FNDR

#### Definicion
Fondo Nacional de Desarrollo Regional. Principal fuente de financiamiento para la inversión pública regional en Chile.

### FRPD

#### Definicion
Fondo Regional para la Productividad y el Desarrollo (FRPD). Fondo específico para iniciativas de productividad y desarrollo, innovación, competitividad, ciencia y tecnología.

### SNI

#### Definicion
Sistema Nacional de Inversiones. Marco normativo y metodológico para la evaluación y priorización de la inversión pública en Chile.

### MDSyF

#### Definicion
Ministerio de Desarrollo Social y Familia. Organismo central encargado de la evaluación técnico-económica de proyectos de inversión pública.

### DIPRES

#### Definicion
Dirección de Presupuestos. Organismo técnico del Ministerio de Hacienda encargado de la formulación, ejecución y control del Presupuesto del Sector Público.

### SES

#### Definicion
Subsecretaría de Evaluación Social. Parte del MDSyF, responsable de la evaluación social de proyectos y programas.

### BIP

#### Definicion
Banco Integrado de Proyectos. Plataforma informática del SNI donde se registran y gestionan las iniciativas de inversión pública.

### UTM

#### Definicion
Unidad Tributaria Mensual. Unidad de cuenta reajustable utilizada en Chile para fines tributarios y multas.

### CLP

#### Definicion
Peso Chileno. Moneda oficial de Chile.

### Subt24

#### Definicion
Subtítulo 24. Transferencias Corrientes. Partida presupuestaria para gastos de operación y transferencias sin contrapartida de capital.

### Subt31

#### Definicion
Subtítulo 31. Inversión Real. Partida presupuestaria para la adquisición de activos no financieros (inversión directa).

### Subt33

#### Definicion
Subtítulo 33. Transferencias de Capital. Partida presupuestaria para transferencias destinadas a financiar inversión.

### ANF

#### Definicion
Activos No Financieros. Bienes durables que no son financieros (ej. edificios, maquinaria, vehículos).

### IDI

#### Definicion
Iniciativa de Inversión. Sinónimo de proyecto de inversión en el contexto del SNI.

### PPR

#### Definicion
Programa Público Regional. Iniciativa de gasto corriente o mixto ejecutada por el GORE o transferida a terceros.

### MML

#### Definicion
Metodología Marco Lógico. Herramienta de planificación y gestión de proyectos y programas.

### CAE

#### Definicion
Costo Anual Equivalente. Indicador utilizado en evaluación de proyectos para comparar alternativas con vidas útiles diferentes.

### NIP

#### Definicion
Normas de Inversión Pública. Conjunto de regulaciones y directrices que rigen el proceso de inversión pública.

### STS

#### Definicion
Structured Text Specification. Formato de especificación de texto estructurado.

### KODA

#### Definicion
Knowledge Object Document Architecture. Arquitectura de documento para objetos de conocimiento.

### Municipalidad

#### Definicion
Municipalidad u otra entidad municipal que puede ejecutar proyectos o programas financiados con recursos del GORE.

### SUBDERE

#### Definicion
Subsecretaría de Desarrollo Regional y Administrativo. Órgano responsable de lineamientos operativos del FRIL, entre otros fondos.

### Plataforma BIP

#### Definicion
Plataforma informática del Banco Integrado de Proyectos.

## Contexto General

### Proposito
Orientar selección estratégica mecanismo financiamiento

### Ref GORE
DEF-GORE

### Ref IPR
DEF-IPR

### Dest
Formuladores, planificadores, decisores

### Objetivos
Proveer marco discernimiento PREVIO formulación detallada determinar vía financiamiento idónea

### Pregunta Guia

#### Definicion
¿Dada IPR, qué vía más adecuada?

#### Ref IPR
DEF-IPR

#### Ref SNI
DEF-SNI

### Principio Rector

#### Definicion
Correcta clasificación naturaleza IPR (proyecto vs programa) y ejecutor determina vía financiamiento y proceso evaluación aplicable

#### Ref IPR
DEF-IPR

#### Ref SNI
DEF-SNI

#### Ref MML
DEF-MML

#### Prohibiciones
Este documento NO es guía formulación detallada

#### Resultados
Elección informada optimiza alineación, agiliza aprobación, maximiza impacto regional

## Catalogo Mecanismos

### Definicion
Portafolio mecanismos aplicación fondos inversión regional, cada uno con propósito, regulación, proceso evaluación específico

### Ref GORE
DEF-GORE

### Ref FNDR
DEF-FNDR

### Ref FRPD
DEF-FRPD

### IPR Proyecto

#### Definicion
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

#### Contexto
kb_gn_024_guia_idi_sni.md

#### Mecanismo SNI General

#### Proposito
Financiar proyectos inversión que por complejidad o monto no califican vías simplificadas

#### Warn Principio Proporcionalidad

#### Definicion
SNI NO es proceso único. Rigor se adapta según magnitud proyecto

#### Contexto
kb_gn_024_guia_idi_sni.md#KB-GN-024-SNI-PROPORCIONALIDAD-01

#### Proceso Maduracion Preinversional

#### Definicion
Proyectos complejos deben madurar por etapas estudio para reducir incertidumbre

#### Proceso
Idea → Perfil → Prefactibilidad → Factibilidad

#### Niveles Profundidad Evaluacion

#### Definicion
SNI aplica distintos niveles análisis. Proyectos simples tienen requisitos reducidos, complejos exigen mayor rigor

#### Contexto
kb_gn_024_guia_idi_sni.md#KB-GN-024-SNI-PROPORCIONALIDAD-01

#### Req Evaluacion

#### Ref Evaluador
DEF-MDSYF

#### Res Nombre
RATE (Resultado Análisis Técnico-Económico)

#### RATE Posibles

#### RS

#### Definicion
Recomendado Satisfactoriamente - Aprobado financiamiento

#### FI

#### Definicion
Falta Información - Devuelto con observaciones subsanar

#### OT

#### Definicion
Objetado Técnicamente - Rechazado problemas fondo

#### AD

#### Definicion
Admisibilidad - Estado que acredita cumplimiento mínimo para control y registro sin evaluación socioeconómica completa.

#### Fundamento
DL 1.263 Art.19bis

#### Ref NIP
DEF-NIP

#### Contexto
kb_gn_024_guia_idi_sni.md

#### Mecanismo FRIL

#### Proposito
Agilizar financiamiento proyectos infraestructura menor escala

#### Dest
Exclusivo ejecución

#### Ref Ejecutor
ORG-MUNICIPALIDAD

#### Caracteristicas

#### Tope Costo

#### Definicion
Proyectos costo total <5.000 UTM

#### Tope Regional Nuble
4.545 UTM

#### Monto Minimo
$100.000.000 CLP

#### Exencion RS

#### Definicion
Proyectos municipales <5.000 UTM no requieren informe favorable MDSyF. Debe ingresarse al SNI información necesaria para control/registro.

#### Ventaja Estrategica Conservacion

#### Definicion
Para Proyectos Conservación calificados, vía más ágil porque NO requiere AD

#### Prohibiciones

#### Items
- NO financia adquisición activos aislados (vehículos, equipamiento no indispensable obra)
- Costo activos no financieros NO puede superar 10% costo total proyecto
- NO financia proyectos fraccionados por etapas para eludir umbrales

#### Req Postulacion

#### Definicion
Proceso postulación vía concursos calendarizados (llamados) con cupos limitados comuna, evaluación mérito GORE

#### Advertencias
NO es asignación automática

#### Req Registro SNI

#### Definicion
Ingreso de información necesaria al SNI para fines de control/registro (no depende de contar con informe favorable MDSyF en el tramo <5.000 UTM).

#### Fundamento
Ley de Presupuestos 2026 Partida 31 Glosa 12 (GN-LEY-PPTO-2026-P31-GLO-12): Resolución Exenta N°15.051/2023 SUBDERE; Oficio Ordinario N°2/26.01.2024 MH y MDSyF e instructivo asociado.

#### Contexto
kb_gn_026_guia-fril.md

#### Mecanismo Circular33

#### Proposito
Simplificar y agilizar evaluación/financiamiento IPRs tipo proyecto características específicas menor complejidad

#### Warn Modificacion Normativa

#### Definicion
Grado simplificación y autonomía modificado por normativa vigente, especialmente Conservaciones y Emergencias

#### Aplicabilidad

#### Estudios Basicos

#### Advertencias
Sujeto restricciones. Estudios propio GORE financian con presupuesto funcionamiento. Estudios terceros requieren autorización especial DIPRES

#### Adquisicion ANF

#### Definicion
Adquisición ANF que NO forman parte proyecto mayor

#### Ref ANF
DEF-ANF

#### Ref DIPRES
DEF-DIPRES

#### Advertencias
Modificaciones presupuestarias requieren visación

#### Req Cofinanciamiento

#### Definicion
Exige cofinanciamiento ≥20% costo total por institución solicitante

#### Req Certificados

#### Requisitos
- Si corresponde a compra de nuevos activos no financieros: incorporar certificado de disponibilidad presupuestaria para gastos recurrentes emitido por el Ministerio o Subsecretaría respectiva.
- Compras para Fuerzas de Orden y Seguridad Pública: certificado de pertinencia emitido por el Ministerio de Seguridad Pública.
- Activos no financieros para Bomberos: certificado de pertinencia técnica emitido por la Junta Nacional de Bomberos de Chile.
- Compra de terrenos: efectuar coordinación con SERVIU regional cuando corresponda.

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-09

#### Proyectos Conservacion

#### Warn Perdida Autonomia

#### Definicion
Aunque vía simplificada sin evaluación técnico-económica completa, normativa vigente exige ingreso BIP para obtener estado AD como requisito registro control

#### Condiciones Viabilidad

#### Cond Costo

#### Definicion
Costo reparación ≤30% costo reponer activo completo

#### Cond Vida Util

#### Definicion
Si activo cumplió vida útil, requiere estudio CAE demuestre mantener más conveniente que reponer

#### Ref CAE
DEF-CAE

#### Ref SNI
DEF-SNI

#### Advertencias
Si supera 30% costo, debe ir evaluación SNI completa

#### Proyectos Reconstruccion

#### Prohibiciones
Vía NO financia fases Respuesta o Rehabilitación inmediata. Estas gestionan directamente con DIPRES

#### Ref DIPRES
DEF-DIPRES

#### Resultados
Permite vías evaluación más rápidas/simplificadas que proceso SNI completo, pero con nuevas dependencias organismos centrales

#### Fundamento
Circular N°33/2009 MINHAC, Ley de Presupuestos 2026 (Ley N°21.796).

#### Ref NIP
DEF-NIP

#### Contexto
kb_gn_029_guia-circ33.md

### IPR Programa

#### Definicion
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

#### Definicion
Depende críticamente QUIÉN ejecuta iniciativa

#### Plataforma Primaria
Formularios Perfil/Diseño, Plataformas postulación

#### Ref GORE
DEF-GORE

#### Warn Division Vias

#### Definicion
PPR divide en dos vías mutuamente excluyentes según ejecutor

#### Ref PPR
DEF-PPR

#### Mecanismo Glosa06 Directa

#### Proposito
Financiar programas donde GORE es responsable principal implementación y entrega servicios

#### Dest
Programas ejecutados directamente GORE (con personal y recursos propios)

#### Denominaciones Comunes

#### Items
- Programa Público Regional (PPR) Ejecución Directa
- Programa Vía Glosa 06
- Programa Evaluación Ex-Ante

#### Warn No Confundir

#### Definicion
NO confundir con 'Programa Inversión' SNI. Evaluación ex-ante PPR se rige por DIPRES/SES (RF), y la oferta programática ejecutada directamente por GORE está sujeta al Sistema de Evaluación y Monitoreo del MDSyF y DIPRES.

#### Req Evaluacion Bifasica

#### Definicion
Proceso bifásico evaluación ex-ante

#### Fase1 Perfil

#### Proceso
Presentar Formulario Perfil a DIPRES/SES para primer filtro pertinencia

#### Fase2 Diseno

#### Proceso
Solo si perfil aprobado, elaborar/presentar Formulario Diseño detallado para evaluación fondo

#### Res Objetivo
Recomendación Favorable (RF)

#### Resultado Recomendacion Favorable

#### Definicion
Recomendación Favorable - Dictamen DIPRES/SES que habilita uso de recursos vía Glosa 06.

#### Req Metodologia

#### Definicion
Formulación obligatoria bajo MML

#### Ref MML
DEF-MML

#### Req Excepciones Evaluacion Ex Ante

#### Cpt
- Se exceptuarán del proceso de evaluación ex-ante: programas que hayan iniciado su ejecución en años anteriores; subvenciones asociadas al Concurso de Vinculación con la Comunidad 8%; transferencias a universidades, municipalidades, otras entidades públicas y gobierno central e instituciones privadas beneficiarias sin fines de lucro; ayudas tempranas e iniciativas de fomento productivo vinculadas a emergencias y desastres naturales (en coordinación con el Ministerio del Interior).

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-06

#### Req Tope Administracion 5pct

#### Definicion
Podrá destinarse hasta un 5% del monto total de la transferencia a gastos que demande la administración de las iniciativas en el Gobierno Regional (personal, bienes y servicios de consumo y adquisición de activos no financieros, asociados con la ejecución del programa). El personal contratado a honorarios con cargo a este 5% tendrá la calidad de agente público.

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-06

#### Warn Convenios Transferencias

#### Advertencias
Cuando existan convenios de transferencia con instituciones privadas, aplicar obligaciones y prohibiciones de convenios/rendición establecidas en la Ley de Presupuestos vigente (incluye rendición vía Sistema de Rendición Electrónica de Cuentas).

#### Contexto
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25

#### Fundamento
Ley de Presupuestos 2026 Partida 31 Glosa 06 (GN-LEY-PPTO-2026-P31-GLO-06), Oficio Circular N°22 (o vigente).

#### Ref DIPRES
DEF-DIPRES

#### Contexto
kb_gn_025_guia-programas.md

#### Mecanismo Transferencia Publico

#### Proposito
Financiar programas donde entidad pública distinta GORE ejecuta iniciativa

#### Dest
Instituciones públicas (Servicios Públicos, Municipalidades, Universidades Estado)

#### Denominaciones Comunes

#### Items
- Transferencia Programa Instituciones Públicas
- Programa Ejecución Indirecta
- Programa Exención Glosa 06 letra c

#### Warn Exencion No Simplifica

#### Definicion
Exención evaluación central (DIPRES/SES) NO implica proceso simple. Reemplazada por riguroso proceso evaluación interno GORE

#### Caracteristicas

#### Fnd Exencion

#### Definicion
Exención evaluación ex-ante DIPRES/SES según Glosa 06 letra c

#### Req Evaluacion GORE

#### Definicion
Proceso formal GORE multifásico

#### Proceso
- 1) Admisibilidad Documental
- 2) Pertinencia Estratégica Comité Regional
- 3) Evaluación Técnica Diseño (MML)

#### Res Culmina
Informe Técnico Favorable (ITF) interno

#### Req Metodologia

#### Definicion
Formulación obligatoria bajo Metodología Marco Lógico (MML)

#### Prohib SNI

#### Definicion
NO usa metodología SNI ni BIP

#### Restricciones Gasto

#### Definicion
Uso fondos estrictamente regulado

#### Tope Personal

#### Definicion
Tope máximo 5% contratación personal a honorarios por entidad pública receptora. Vínculo cesa de pleno derecho al finalizar el convenio de transferencia.

#### Contexto
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-06
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART07

#### Modalidad Transferencia Municipal

#### Definicion
Para municipalidades, transferencia directa fondos (no consolidable)

#### Advertencias
NO exime riguroso proceso evaluación interno GORE que reemplaza evaluación central

#### Contexto
kb_gn_001_guia-transferencia-programas.md

#### Mecanismo Subvencion 8pct

#### Proposito
Subvencionar actividades acotadas interés comunitario, NO programas públicos complejos

#### Dest
Principalmente instituciones privadas sin fines lucro, organizaciones comunitarias. Municipalidades acceso fondos específicos con reglas/montos diferenciados

#### Warn Error Conceptual

#### Definicion
Vía NO financia "Programas Públicos Regionales" (PPR) con lógica resolución problemas estructurales, sino "actividades" corta duración (ej. talleres, festivales, campañas)

#### Req Evaluacion Competitiva

#### Definicion
Proceso altamente formalizado y competitivo basado en mérito según bases concursales GORE.

#### Proc Portafolio

#### Definicion
Organizado como portafolio múltiples fondos temáticos (Cultura, Deporte, Social, Seguridad, etc.)

#### Def Caracteristicas
Cada fondo con presupuesto, reglas, montos máximos proyecto varían según área y tipo organización postulante

#### Proc Seleccion Puntaje

#### Definicion
Selección basada sistema puntaje. Iniciativas deben superar umbral calidad para considerarse

#### Prohib Restricciones

#### Items
- Restricciones elegibilidad estrictas (ej. 2 años antigüedad organizaciones)
- Restricciones gasto (ej. NO financiar proyectos únicamente compra equipamiento)

#### Res Exencion

#### Definicion
Exento evaluación SNI y evaluación ex-ante programas DIPRES/SES

#### Cond Asignacion Directa

#### Condiciones
Se podrá asignar hasta un 10% de los recursos del Concurso de Vinculación con la Comunidad 8% para financiar, previo acuerdo del Consejo Regional, mediante asignaciones directas actividades asociadas con casos emblemáticos, excepcionales y emergentes (sujeto a lo dispuesto en Resolución N°72/08.01.2025 DIPRES y sus modificaciones).

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-07

#### Req Convenios y Rendicion

#### Requisitos
- Convenios de transferencia deben cumplir obligaciones y prohibiciones del Art. 24 (incluye rendiciones a través del Sistema de Rendición Electrónica de Cuentas de la CGR).
- Para instituciones privadas ejecutoras de políticas públicas, considerar requisitos adicionales (incluye garantías cuando el monto transferido supere 1.000 UTM).

#### Contexto
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25

#### Fundamento
Ley de Presupuestos 2026 Partida 31 Glosa 07 (GN-LEY-PPTO-2026-P31-GLO-07).

#### Contexto
kb_gn_028_instructivo-subvencion-8.md

### IPR Productivo

#### Definicion
Iniciativas (proyectos o programas) orientadas inversión productiva y desarrollo económico regional

#### Fnd Recursos

#### Definicion
Fondo Regional para la Productividad y el Desarrollo (FRPD)

#### Mecanismo FRPD

#### Proposito
Financiar IPRs diversificación productiva, desarrollo económico, investigación/ciencia/tecnología/innovación (I+D+i)

#### Warn Acceso Restringido

#### Definicion
Acceso altamente restringido. Solo pueden postular instituciones explícitamente habilitadas normativa SUBCTCI (principalmente agencias fomento, institutos investigación, universidades acreditadas). NO vía acceso universal

#### Ambitos

#### Items
- Fomento productivo
- Desarrollo capital humano
- Apoyo competitividad regional
- I+D+i

#### Req Evaluacion Multifasica

#### Definicion
Proceso selección multifásico y competitivo, previo cualquier evaluación fondo

#### Fase1 Admisibilidad Admin

#### Proceso
Filtro documental y requisitos básicos

#### Fase2 Admisibilidad Tecnica

#### Proceso
Concurso puntaje ante comité evaluador determinar "Elegibilidad"

#### Fase3 Evaluacion GORE

#### Proceso
Revisión fondo iniciativas "Elegibles"

#### Casos Evaluacion

#### Caso CTCI

#### Definicion
Iniciativas Ciencia/Tecnología/Conocimiento/Innovación seleccionadas concurso

#### Resultados
Exentas evaluación ex-ante DIPRES/SES o SNI. Aprobación concurso es final

#### Caso Fomento General

#### Definicion
Iniciativas NO califican CTCI

#### Requisitos
Ganar concurso previo es solo PREREQUISITO obtener derecho iniciar proceso evaluación estándar completo (Vía Ref: MEC-SNI-GENERAL si proyecto capital, Vía Programas si servicios)

#### Req Provision Sin Distribuir

#### Definicion
Distribución inicial debe contemplar provisión sin distribuir en Ítem 33.03 para FRPD, desde donde se reasignan recursos.

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-13

#### Req Transferencia Directa Concursos

#### Definicion
Faculta transferencias directas para iniciativas seleccionadas en concursos (p.ej. CORFO/ANID), conforme a normativa vigente y ejecutores habilitados.

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-13

#### Fundamento
Ley N°21.591 (Royalty Minero); Ley de Presupuestos 2026 Partida 31 Glosa 13 (GN-LEY-PPTO-2026-P31-GLO-13): Decreto N°1699/2025 MH; Resolución Exenta N°33/2024 MinCiencia y sus modificaciones; Resolución Exenta N°08/2025 Subsecretaría de Economía y sus modificaciones.

#### Contexto
kb_gn_027_guia-frpd.md

## Marco Regulatorio

### Proposito
Detallar fundamento jurídico y normativo cada vía financiamiento, establecer jerarquía reglas gobiernan asignación recursos

### Marco Transversal

#### Definicion
Normas carácter general proveen marco fundamental toda inversión regional

#### Pilares Normativos

#### LOC GORE

#### Fundamento
Otorga GORE facultad "Decidir inversión" (Art.16f), "Ejecutar programas regionales" (Art.20k)

#### Requisitos
Conecta administración fondos (FNDR) con obligación evaluación técnica (Art.75)

#### DL 1263

#### Fundamento
Establece base SNI, exige informe favorable iniciativas inversión (Art.19bis)

#### Ley Presupuestos

#### Fundamento
Instrumento operativo asigna recursos, establece reglas específicas (Glosas)

#### Glosa 03

#### Prohibiciones
Usar recursos inversión regional para financiar préstamos o gastos en personal o bienes y servicios de consumo de entidades receptoras, ni para constituir/efectuar aportes/comprar sociedades o empresas, salvo autorizaciones expresas en glosas.

#### Contexto
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-03

#### Normas Generales 2026

#### Fundamento
Reglas transversales (licitación por umbrales, decretos/transferencias, autorizaciones previas DIPRES).

#### Contexto
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART06
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART07
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART12

### Base SNI C33

#### Ref Mecanismos
- MEC-SNI-GENERAL
- MEC-C33

#### Fundamentos

#### SNI

#### Requisitos
Evaluación técnico-económica todo proyecto capital

#### Circular 33

#### Requisitos
Provee vía simplificada evaluación IPRs específicas

### Base Glosa06 Directa

#### Ref Mecanismo
MEC-G06-DIRECTA

#### Fundamentos

#### Glosa 06

#### Req Habilitacion
Habilita uso recursos inversión programas ejecución directa

#### Req Evaluacion
Exige RF programas nuevos o reformulados

#### Circular 22

#### Ref DIPRES
DEF-DIPRES

#### Ref RF
RATE-RF

#### Requisitos
Detalla procedimiento evaluación ex-ante (Perfil y Diseño) obtener RF

### Base Transferencia Publico

#### Ref Mecanismo
MEC-TRANSFER-PUB

#### Fundamentos

#### Glosa 06 Letra C

#### Requisitos
Exime explícitamente "transferencias otras entidades públicas y gobierno central" evaluación ex-ante

#### Contexto
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24
- kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25

#### Guia GORE

#### Ref GORE
DEF-GORE

#### Contexto
kb_gn_001_guia-transferencia-programas.md

#### Requisitos
Establece procedimiento postulación, admisibilidad, evaluación técnica/financiera interna reemplaza evaluación Circular 22

### Base FRIL

#### Ref Mecanismo
MEC-FRIL

#### Fundamentos

#### Glosa 12

#### Req Transferencias
Regula transferencias municipalidades proyectos infraestructura menor

#### Guia FRIL

#### Ref SUBDERE
ORG-SUBDERE

### Base Subvencion 8pct

#### Ref Mecanismo
MEC-SUBV8

#### Fundamentos

#### Glosa 07

#### Req Asignacion
Regula asignación hasta 8% inversión FNDR subvencionar actividades

#### Req Concurso
Establece concurso público como regla general asignación

#### Req Exencion
Exime iniciativas evaluación Glosa 06 y SNI

### Base FRPD

#### Ref Mecanismo
MEC-FRPD

#### Fundamentos

#### Ley Royalty

#### Requisitos
Crea FRPD, define propósito exclusivo inversión productiva y desarrollo económico

#### Glosa 13

#### Req Operativo
Norma uso operativo recursos FRPD año

#### Req Transferencia
Faculta transferencia directa iniciativas seleccionadas CORFO/ANID

#### Resolucion SUBCTCI

#### Requisitos
Define lineamientos, ámbitos acción, instituciones habilitadas ejecutar fondos FRPD I+D+i

## Procesos Evaluacion

### Proposito
Detallar procesos validación técnica/económica IPR debe superar antes obtener financiamiento según vía escogida

### Evaluacion SNI

#### Ref Mecanismos
- MEC-SNI-GENERAL
- MEC-FRIL
- MEC-C33

#### Proceso General

#### Objetivo

#### Definicion
Analizar rentabilidad socioeconómica iniciativa inversión

#### Resultado

#### Definicion
Recomendación Satisfactoria (RS) o Admisibilidad (AD), "pase" obtener financiamiento

#### Metodologias

#### Definicion
Metodologías específicas SNI (ej. VAN, CAE)

#### Excepciones Vias Simplificadas

#### Exencion FRIL

#### Condiciones
Proyectos municipales <5.000 UTM

#### Resultados
No requieren informe favorable MDSyF, pero deben ingresar información necesaria al SNI para control/registro.

#### Procedimientos Especiales C33

#### Condiciones
IPRs Conservación, Estudios Básicos, ANF, Emergencias

#### Resultados
Utilizan procedimientos evaluación agilizados o simplificados

### Evaluacion Glosa06 Directa

#### Ref Mecanismo
MEC-G06-DIRECTA

#### Proceso General

#### Objetivo

#### Definicion
Analizar calidad diseño (coherencia, pertinencia) programa nuevo o reformulado

#### Resultado

#### Definicion
Recomendación Favorable (RF) habilita solicitud recursos

#### Metodologia

#### Definicion
Marco Lógico

#### Plataforma

#### Definicion
Formularios Perfil y Diseño

### Evaluacion Transferencia Publico

#### Ref Mecanismo
MEC-TRANSFER-PUB

#### Proceso General

#### Fundamento Habilitacion

#### Definicion
Habilitado exención Glosa 06 letra c

#### Responsable

#### Definicion
Unidades técnicas GORE (Departamento Análisis y Evaluación - DAE, Comité Pertinencia)

#### Objetivo

#### Definicion
Asegurar pertinencia estratégica y factibilidad técnica/financiera propuesta

#### Resultado

#### Definicion
Emisión Informe Técnico Favorable (ITF) habilita gestión financiamiento

#### Calificaciones Posibles

#### Items
- Recomendado Favorablemente
- Recomendado con Observaciones
- No Recomendado

#### Warn No RS

#### Definicion
Resultado NO es Recomendación Satisfactoria (RS) SNI

#### Metodologia

#### Definicion
Marco Lógico y criterios definidos guía GORE

#### Ref MML
DEF-MML

#### Plataforma

#### Definicion
Plataforma postulación GORE (ej. GESDOC)

### Evaluacion Especial Exenta

#### Iniciativas FRPD

#### Proceso
Pueden tener mecanismos propios concurso o asignación, especialmente si alinean convocatorias CORFO/ANID

## Arbol Decision

### Proposito
Proveer secuencia lógica preguntas guiar formulador hacia mecanismo más probable y adecuado

### Advertencias
Guía orientación. Decisión final requiere consulta unidades técnicas GORE

### Paso1 Naturaleza IPR

#### Pregunta Guia
¿Propósito principal crear/mejorar activo físico o intangible durable ("cosa") o entregar servicio/prestación forma continua?

#### Decisiones

#### Si Activo Durable

#### Resultados
Ir a Ruta PROYECTOS

#### Si Servicio Prestacion

#### Resultados
Ir a Ruta PROGRAMAS

### Ruta Proyectos

#### Pregunta 1 Municipal FRIL

#### Pregunta
¿Ejecutor Municipalidad, costo <5.000 UTM, proyecto infraestructura?

#### Si Cumple

#### Resultados
Vía más probable FRIL

#### Pregunta 2 Procedimientos Especiales

#### Pregunta
¿IPR es Conservación, Estudio Básico, Adquisición Activos Aislada, o Reconstrucción?

#### Si Cumple

#### Resultados
Vía probable Procedimientos Especiales (Circular 33 / NIP)

#### Pregunta 3 Foco Productivo

#### Pregunta
¿IPR foco principal productividad/innovación/competitividad económica, postulada entidad habilitada?

#### Si Cumple

#### Resultados
Fuente fondos natural FRPD (Capital)

#### Pregunta 4 Ninguna Anterior

#### Pregunta
¿Ninguna anteriores (ej. construcción hospital, puente)?

#### Si Cumple

#### Resultados
Vía obligatoria SNI General

### Ruta Programas

#### Pregunta 1 Organizacion Comunitaria

#### Pregunta
¿Ejecutor organización comunitaria o privada sin fines lucro, IPR ajusta líneas Cultura/Deporte/Social?

#### Si Cumple

#### Resultados
Vía más probable Subvención 8% FNDR (vía concurso)

#### Pregunta 2 Ejecucion GORE

#### Pregunta
¿Ejecutor propio GORE, entregará servicios directamente?

#### Si Cumple

#### Resultados
Vía obligatoria Ejecución Directa GORE (Glosa 06)

#### Pregunta 3 Entidad Publica

#### Pregunta
¿Ejecutor otra entidad pública (Municipio, Servicio Público, U.Estatal)?

#### Si Cumple

#### Resultados
Vía obligatoria Transferencia Entidad Pública

#### Pregunta 4 Foco Productivo

#### Pregunta
¿IPR foco principal productividad/innovación/competitividad económica, postulada entidad habilitada?

#### Si Cumple

#### Resultados
Fuente fondos natural FRPD (Programático)

### Criterios Validacion Complementarios

#### Alineamiento Estrategico

#### Requisitos
IPR debe ser coherente Estrategia Regional Desarrollo (ERD) y otros planes regionales

#### Magnitud Complejidad

#### Requisitos
IPRs gran envergadura y complejidad técnica sugieren robustez (y plazos) SNI General

#### Warn Licitacion Publica

#### Condiciones
Si el monto supera umbrales de licitación pública obligatoria, ajustar estrategia de compras y plazos: Proyectos/Programas de inversión >1.000 UTM; Estudios Básicos >500 UTM (salvo emergencias según legislación).

#### Contexto
kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART06

#### Urgencia

#### Condiciones
Urgencia calificada puede activar procedimientos emergencia (vía proyectos) o asignaciones directas (vía subvenciones 8%)

#### Contexto
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-14
- kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-07

#### Transparencia y Reporting

#### Requisitos
Considerar obligaciones de publicación y reportes periódicos asociados a Subt. 24/31/33, umbrales (p.ej. 500 UTM) y transferencias del 8% y FRPD, según Ley de Presupuestos vigente.

#### Contexto
kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-16

#### Disponibilidad Presupuestaria

#### Requisitos
Selección final siempre supeditada disponibilidad fondos línea financiamiento correspondiente

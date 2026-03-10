---
_manifest:
  urn: urn:gn:kb:transferencia-ppr
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_gn_001_transferencia_ppr_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- transferencia-fondos
- ppr
- fndr
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_001_transferencia_ppr_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_001_transferencia_ppr_koda.yml: ecb09f8e8d9ac97425808b6d67cdb20d04dd6eb260c1752568c93674bb924ebb
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.91
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 6
    meat_count: 581
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__transferencia-ppr.md.json
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:transferencia-ppr
---

# Transferencia de Programas Públicos Regionales (PPR) a Entidades Públicas
## Glosario PPR Transferencia
- **Proposito:** Definir conceptos, siglas y normas clave recurrentes en la guía de transferencia de Programas Públicos Regionales (PPR).
### Terminos
| ID | Sigla | Cpt | Def |
| --- | --- | --- | --- |
| GN-PPR-GLOS-PPR | PPR | Programa Público Regional | Conjunto integrado y articulado de acciones, prestaciones y beneficios destinados a un propósito específico en una población objetivo, para resolver un problema o necesidad. |
| GN-PPR-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fuente de financiamiento de proyectos y programas regionales administrada por los Gobiernos Regionales. |
| GN-PPR-GLOS-GORE | GORE | Gobierno Regional | Administración superior de la región, con personalidad jurídica y patrimonio propio, responsable de la inversión y programas regionales. |
| GN-PPR-GLOS-DAE | DAE | Departamento de Análisis y Evaluación | Unidad del GORE responsable de la evaluación técnica de programas y proyectos. |
| GN-PPR-GLOS-DIPIR | DIPIR | División de Presupuesto e Inversión Regional | División encargada del presupuesto de inversión y de la oferta programática regional. |
| GN-PPR-GLOS-DIPRES | DIPRES | Dirección de Presupuestos | Órgano técnico del Ministerio de Hacienda a cargo de la formulación, ejecución y control del Presupuesto del Sector Público. |
| GN-PPR-GLOS-ERD | ERD | Estrategia Regional de Desarrollo | Instrumento estratégico que orienta las prioridades de desarrollo regional y con el que deben alinearse los PPR. |
| GN-PPR-GLOS-SNI | SNI | Sistema Nacional de Inversiones | Marco y plataforma para la evaluación técnico-económica de proyectos de inversión pública (IDI). |
| GN-PPR-GLOS-IDI | IDI | Iniciativa de Inversión | Proyecto de inversión en obras o activos, sujeto a evaluación en el SNI, distinto de los PPR de gasto corriente o mixto regulados en esta guía. |
| GN-PPR-GLOS-MML | MML | Metodología de Marco Lógico | Metodología obligatoria para el diseño de PPR, basada en diagnóstico, árbol de problemas, objetivos, componentes, actividades e indicadores. |
| GN-PPR-GLOS-ITF | ITF | Informe Técnico Favorable | Informe emitido por la DAE que valida técnicamente una propuesta de PPR para que pueda avanzar a la etapa de financiamiento; no equivale a una Recomendación Satisfactoria (RS) del SNI. |
| GN-PPR-GLOS-GESDOC | GESDOC | Gestor Documental del GORE | Plataforma institucional del GORE Ñuble para el ingreso y gestión de documentación de postulaciones. |
| GN-PPR-GLOS-SISREC | SISREC | Sistema de Rendición Electrónica de Cuentas | Plataforma de la Contraloría General de la República para la rendición de transferencias de Subtítulos 24 y 33. |

## Parte 1 Marco General y Objeto
### Proposito y Alcance Guia
- **Proposito:** Estandarizar el procedimiento de postulación, evaluación y transferencia de fondos FNDR para la ejecución de Programas Públicos Regionales (PPR) por parte de entidades públicas.
- **Fundamento:** Glosa 06, Partida 31, Ley de Presupuestos 2026 (Ley N°21.796)., Oficio Circular N°22 DIPRES.
- **Contexto:** La guía regula específicamente los PPR (gasto corriente o mixto para la entrega de servicios) que, por ser ejecutados por un tercero público, están exentos de la evaluación ex-ante de DIPRES/SES. En consecuencia, la evaluación de mérito y diseño de estas iniciativas es competencia del Gobierno Regional de Ñuble.
- **Advertencias:** Ámbito de aplicación estricto: este documento no aplica para proyectos de inversión (IDI) ni programas de ejecución directa del GORE.
- **Referencias:** GN-PPR-GLOS-FNDR, GN-PPR-GLOS-GORE
#### Exclusiones Ambito
#### Casos
| Cpt | Def |
| --- | --- |
| Proyectos de Inversión (IDI) | Iniciativas de gasto de capital (obras, activos) regidas por el Sistema Nacional de Inversiones (SNI). Su transferencia sigue otros procedimientos. |
| Programas de Ejecución Directa GORE | Programas ejecutados directamente por el GORE que sí requieren el ciclo de evaluación ex-ante de DIPRES/SES. |
### Entidades Postulantes Habilitadas
- **Dest:** Municipalidades de la Región de Ñuble., Otros servicios públicos y entidades del Estado con competencia para ejecutar programas sociales, culturales o de fomento.
- **Fundamento:** Decreto Ley 1.263 de 1975 (Ley de Administración Financiera del Estado)., Glosa 06 de Inversión Regional ("transferencias a otras entidades públicas y al gobierno central").
#### Ejemplos
| Ex |
| --- |
| Universidades Estatales. |
### Definicion PPR Transferible
- **Definicion:** Conjunto integrado y articulado de acciones, prestaciones y beneficios (componentes) destinados a lograr un propósito específico en una población objetivo, de modo de resolver un problema o atender una necesidad que la afecte.
- **Requisitos:** Duración definida y finita.
- **Prohibiciones:** No debe constituir acciones permanentes de la entidad receptora, las cuales deben ser financiadas con su presupuesto regular.
### Criterios Focalizacion Inversion
- **Fundamento:** Art. 74 del DFL 1-19.175 de 2005.
- **Contexto:** El FNDR opera como programa de inversiones públicas para el desarrollo regional y la compensación territorial.
- **Referencias:** GN-PPR-GLOS-FNDR, GN-PPR-GLOS-ERD
- **Requisitos:** El propósito del programa debe solucionar un problema regional definido, que permita su identificación, demostración y tenga indicadores de cumplimiento., La formulación debe focalizarse en la disminución de brechas de un problema claramente definido., La cobertura debe considerar el aspecto regional del FNDR y la dimensión del problema., Debe existir coherencia con la Estrategia Regional de Desarrollo (ERD) Ñuble 2022-2030, el Plan de Gobierno Regional y/o la Estrategia Regional de CTCI., Se debe poner énfasis en equidad de acceso y pertinencia de beneficiarios, con mecanismos de selección transparentes y probos., Debe considerarse una capacidad de gestión óptima con máxima optimización de recursos, cumpliendo principios de eficiencia y eficacia.
### Plazos Postulacion
- **Dln:** La postulación de programas para financiamiento con cargo al presupuesto del año 2026 se recibirá hasta el 30 de septiembre de 2026.
- **Condiciones:** Propuestas ingresadas post-fecha, si son recomendadas favorablemente, podrían ser consideradas para el siguiente ejercicio presupuestario, sujeto a la normativa vigente.

## Parte 2 Proceso Postulacion y Evaluacion GORE
- **Proposito:** Describir el flujo que debe seguir una entidad pública para postular un PPR a financiamiento GORE y el proceso de evaluación interna que este último realizará para asegurar la pertinencia y calidad de la propuesta.
### Metodologia Formulacion Obligatoria MML
- **Requisitos:** Las propuestas de PPR deben ser formuladas utilizando la Metodología de Marco Lógico (MML).
- **Advertencias:** No se debe utilizar la Ficha IDI, el código BIP ni la metodología de evaluación de proyectos de inversión para este tipo de iniciativas. La postulación no se realiza en el Banco Integrado de Proyectos (BIP).
- **Fuentes:** kb_gn_025_guia-programas_sts.md
- **Rec:** Se sugiere fuertemente a las entidades formuladoras capacitarse en MML para asegurar la calidad de sus propuestas.
### Documentacion Requerida Postulacion
- **Requisitos:** La postulación debe realizarse mediante la plataforma GESDOC del GORE, adjuntando la documentación mínima definida a continuación.
#### Plataforma
- **Cpt:** Plataforma GESDOC del GORE Ñuble.
- **Referencias:** GN-PPR-GLOS-GESDOC
#### Documentos Clave
| N | ID | Nombre | Ref-SFD |
| --- | --- | --- | --- |
| 1 | STS-KB-GN-PPR-DOC-01-OFICIO-CONDUCTOR | Oficio Conductor del Representante Legal | N/A |
| 2 | STS-KB-GN-PPR-DOC-02-FORM-PPR | Formulario de Diseño de Programa Público (PPR) | FORM-PPR-TRANSFER-PUBLIC-2026-V1 |
| 3 | STS-KB-GN-PPR-DOC-03-PRESUPUESTO | Presupuesto Detallado (Excel y PDF) | N/A |
| 4 | STS-KB-GN-PPR-DOC-04-COTIZACIONES | Cotizaciones de Respaldo | N/A |
| 5 | STS-KB-GN-PPR-DOC-05-PERFILES | Perfil y Descripción de Cargos | FORM-ANEXO1-PERFIL-CARGOS-V1 |
| 6 | STS-KB-GN-PPR-DOC-06-PATROCINIO | Certificado de Pertinencia y Patrocinio GORE | FORM-PPR-PATROCINIO-GORE-V1 |
| 7 | STS-KB-GN-PPR-DOC-07-DJ-RENDICIONES | Declaración Jurada de Rendiciones y SISREC | FORM-PPR-RENDICIONES-DJ-V1 |
| 8 | STS-KB-GN-PPR-DOC-08-DJ-NO-FRACCION | Certificado de No Fraccionamiento de Programas | FORM-PPR-NO-FRACCION-DJ-V1 |
| 9 | STS-KB-GN-PPR-DOC-09-COMPROMISO-FINANCIERO | Certificado de Compromiso Financiero | FORM-PPR-FINANZAS-COMP-V1 |
| 10 | STS-KB-GN-PPR-DOC-10-DOCS-LEGALES | Documentos Legales de la Entidad (Estatutos, Personería) | N/A |
| 11 | STS-KB-GN-PPR-DOC-11-OTROS-ANEXOS | Otros Anexos (si aplica) | N/A |
### Proceso Evaluacion Interna GORE
- **Contexto:** Dado que estos programas están exentos de evaluación central, el GORE realiza un proceso de evaluación de admisibilidad, pertinencia y mérito técnico, para resguardar el correcto uso de los fondos públicos.
#### Pasos
| Step | Nombre | Resp | Act |
| --- | --- | --- | --- |
| 1 | Admisibilidad Documental | Departamento de Análisis y Evaluación (DAE). | Verificar que la postulación contiene toda la documentación requerida en la sección 2.2 y que ha sido ingresada correctamente. Las postulaciones incompletas serán devueltas para subsanación en un plazo acotado. |
| 2 | Evaluación de Pertinencia Estratégica | Comité de Pertinencia Regional (o instancia que lo reemplace). | Evaluar la alineación del programa con la Estrategia Regional de Desarrollo (ERD), el Plan de Gobierno Regional y las prioridades políticas definidas para el año. |
| 3 | Evaluación Técnica de Diseño | Departamento de Análisis y Evaluación (DAE). | Revisión de fondo de la propuesta. |
#### Resultado Evaluacion
- **Definicion:** La evaluación culmina con un Informe Técnico Favorable (ITF) emitido por la DAE.
- **Advertencias:** Este informe NO es un RATE RS. Es un documento interno del GORE que valida técnicamente la propuesta para que pueda avanzar a la etapa de financiamiento.
- **Calificaciones Posibles:** Recomendado Favorablemente: La propuesta es sólida y se recomienda para su aprobación presupuestaria., Recomendado con Observaciones: La propuesta es pertinente pero requiere ajustes para ser financiada. La entidad postulante deberá subsanar las observaciones en un plazo definido., No Recomendado: La propuesta presenta debilidades técnicas o de pertinencia insalvables que no la hacen elegible para financiamiento.

## Parte 3 Restricciones Normativas y Financieras
### Restricciones Generales
- **Prohibiciones:** Postular programas cuyo objetivo o naturaleza sea distinto al descrito en la ley o decreto de creación de la institución.
- **Condiciones:** Instituciones con convenios vigentes con el GORE deben acreditar su estado de rendiciones de cuentas.
- **Fundamento:** Resolución N°30 de 2015 de la Contraloría General de la República (CGR).
### Restricciones de Gasto
- **Contexto:** Los recursos FNDR transferidos para programas tienen las siguientes restricciones de gasto:
- **Prohibiciones:** Otorgar préstamos o constituir/comprar sociedades con cargo a los recursos transferidos.
- **Condiciones:** Gastos en Personal: la entidad receptora puede usar hasta un 5% del total de la transferencia para contratar personal a honorarios para la gestión del programa., Gastos de Administración: el GORE puede destinar hasta un 5% del monto total a gastos de administración propios para la gestión y seguimiento. Este monto no forma parte de la transferencia.
- **Fundamento:** Glosa 06, Partida 31, Ley de Presupuestos 2026 (Ley N°21.796).
- **Referencias:** GN-PPR-GLOS-FNDR
### Restricciones de Probidad
- **Condiciones:** La subcontratación es permitida solo para actividades que no constituyen el objeto principal del programa, debe estar justificada y detallada en el convenio.
- **Prohibiciones:** Subcontratar con personas jurídicas relacionadas (matriz, filial, etc. según Ley 18.046) o con personas naturales que tengan conflictos de interés por parentesco con autoridades regionales o directivos de la institución postulante., Contratar para la ejecución del programa a cónyuges, convivientes civiles, o parientes hasta el tercer grado de consanguinidad y segundo de afinidad de autoridades y funcionarios directivos del GORE o de la institución postulante.
- **Referencias:** GN-PPR-GLOS-GORE

## Parte 4 Formalizacion Ejecucion y Seguimiento
### Aprobacion Presupuestaria y Convenio
#### Proceso
| Step | Nombre | Act |
| --- | --- | --- |
| 1 | Priorización y Aprobación de Recursos | Los PPR con Informe Técnico Favorable (ITF) son presentados por la DIPIR al Gobernador(a) y, si corresponde por normativa presupuestaria, al Consejo Regional para la aprobación de los fondos. |
| 2 | Elaboración de Convenio de Transferencia | El Departamento de Presupuesto del GORE elabora un convenio que formaliza la transferencia, el cual debe ser suscrito por los representantes legales de ambas instituciones. |
| 3 | Contenido Mínimo del Convenio | |
### Transferencia Recursos y Ejecucion
- **Mecanismo:** La transferencia de fondos se realiza según lo estipulado en el convenio, usualmente contra la presentación de estados de avance o cumplimiento de hitos.
- **Responsables:** La entidad pública receptora es la responsable de la ejecución técnica y financiera del programa, cumpliendo la normativa de compras públicas que le aplique., El GORE, a través de su división patrocinante, supervisa el avance y cumplimiento del convenio.
### Seguimiento y Rendicion
- **Responsables:** La entidad ejecutora debe rendir cuenta de los fondos al GORE en los plazos y formatos estipulados en el convenio.
- **Fundamento:** La rendición se rige por la Resolución N°30 de 2015 de la CGR y sus modificaciones.
- **Mecanismo:** El GORE podrá exigir la rendición vía plataforma SISREC o en formato físico, según se defina en el convenio.
- **Fuentes:** [Gestión de Rendiciones de Cuentas - GORE Ñuble](urn:gn:kb:gestion-rendiciones)
- **Referencias:** GN-PPR-GLOS-SISREC

## Parte 5 Formularios Estandarizados PPR
- **Contexto:** Los formatos estandarizados para la postulación se encontrarán disponibles en la página web del Gobierno Regional de Ñuble. Su estructura detallada es la siguiente.
### Formulario Diseno Programa Publico PPR
- **Ref SFD Guide:** GUIDE-SFD-STS-MASTER-01
#### Campos
| ID | Seccion | Field-Label | Field-Type | Field-Constraint | Field-Instr |
| --- | --- | --- | --- | --- | --- |
| FORM-PPR-TRANSFER-S1-NOMBRE-PROGRAMA | Sección 1: Identificación del Programa | Nombre del Programa | Text | Req: mandatory. | |
| FORM-PPR-TRANSFER-S1-MONTO-FNDR | Sección 1: Identificación del Programa | Monto total solicitado FNDR (M$) | Number | Req: mandatory. | |
| FORM-PPR-TRANSFER-S1-APORTE-PROPIO | Sección 1: Identificación del Programa | Aporte Propio / Otros Aportes (M$) | Number | Req: optional. | |
| FORM-PPR-TRANSFER-S1-PLAZO-EJECUCION | Sección 1: Identificación del Programa | Plazo de ejecución (meses) | Number | Req: mandatory. Min-Val: 1. | |
| FORM-PPR-TRANSFER-S1-ALINEACION-ERD | Sección 1: Identificación del Programa | Alineación con ERD (Indicar Eje, Lineamiento, Objetivo) | TextArea | Req: mandatory. | |
| FORM-PPR-TRANSFER-S2-INSTITUCION | Sección 2: Institución Postulante | Institución o Servicio Postulante | Text | Req: mandatory. | |
| FORM-PPR-TRANSFER-S2-OBJETO-SOCIAL | Sección 2: Institución Postulante | Objeto social de la institución (Resumen según estatuto/ley) | TextArea | Req: mandatory. | |
| FORM-PPR-TRANSFER-S2-FUNDAMENTO-TRANSFERENCIA | Sección 2: Institución Postulante | Fundamento de la solicitud de transferencia (Justificar por qué su institución es la idónea para ejecutar el programa). | TextArea | Req: mandatory. | |
| FORM-PPR-TRANSFER-S3-PROBLEMA-CENTRAL | Sección 3: Diagnóstico y Problema (MML) | Definición del problema central que afecta a la comunidad. | TextArea | Req: mandatory. | Redactar como estado negativo, claro y preciso. Debe estar respaldado por datos. |
| FORM-PPR-TRANSFER-S3-ANALISIS-CAUSAL | Sección 3: Diagnóstico y Problema (MML) | Análisis Causal: Causas y Efectos del Problema | TextArea | Req: mandatory. | Describir las causas directas e indirectas que explican el problema, y los efectos que este genera. Adjuntar diagrama de árbol de problemas si es necesario. |
| FORM-PPR-TRANSFER-S3-POBLACION | Sección 3: Diagnóstico y Problema (MML) | Caracterización y Cuantificación de la Población | TextArea | Req: mandatory. | Describir y cuantificar la población potencial, la población objetivo y los beneficiarios anuales, indicando fuentes de datos. |
| FORM-PPR-TRANSFER-S4-PROPOSITO | Sección 4: Diseño de la Intervención (MML) | Propósito del programa (Objetivo General) | TextArea | Req: mandatory. | Debe ser la reversión en positivo del problema central. Único, medible y orientado a la población objetivo. |
| FORM-PPR-TRANSFER-S4-COMPONENTES | Sección 4: Diseño de la Intervención (MML) | Componentes del Programa | Repeater | | Añada una fila por cada Componente (producto o servicio) que entregará el programa. |
| FORM-PPR-TRANSFER-S4-MATRIZ-MML | Sección 4: Diseño de la Intervención (MML) | Matriz de Marco Lógico | File | Req: mandatory. | Adjuntar la Matriz de Marco Lógico completa (Fin, Propósito, Componentes, Actividades) con sus respectivos Indicadores, Medios de Verificación y Supuestos. |
| FORM-PPR-TRANSFER-S5-MODELO-GESTION | Sección 5: Operatividad y Presupuesto | Modelo de Gestión y Carta Gantt | TextArea | Req: mandatory. | Describir cómo se implementará el programa, el flujo del beneficiario, y adjuntar una Carta Gantt detallada de actividades y financiera. |
| FORM-PPR-TRANSFER-S5-PRESUPUESTO | Sección 5: Operatividad y Presupuesto | Detalle del Presupuesto por Componente y Actividad | File | Req: mandatory. | Adjuntar planilla Excel con el desglose del presupuesto, justificando cada ítem de gasto y su coherencia con las actividades de la MML. |
| FORM-PPR-TRANSFER-S6-FIRMA-FORMULADOR | Sección 6: Firmas | Nombre, firma y timbre del Formulador | Static-Text | | Espacio reservado para firma. |
| FORM-PPR-TRANSFER-S6-CONTACTO-FORMULADOR | Sección 6: Firmas | Fono y Mail contacto formulador | Text | Req: mandatory. | |
| FORM-PPR-TRANSFER-S6-FIRMA-REPRESENTANTE | Sección 6: Firmas | Nombre firma y timbre del jefe de Servicio o Representante de la Institución | Static-Text | | Espacio reservado para firma. |
| FORM-PPR-TRANSFER-S6-CONTACTO-REPRESENTANTE | Sección 6: Firmas | Fono y Mail contacto representante | Text | Req: mandatory. | |
### Anexo Perfil y Descripcion de Cargos
- **Ref SFD Guide:** GUIDE-SFD-STS-MASTER-01
#### Campos
| ID | Seccion | Field-Label | Field-Type | Field-Instr | Field-Constraint |
| --- | --- | --- | --- | --- | --- |
| FORM-ANEXO1-S1-PERFILES-01 | Sección 1: Perfiles de Cargo | Perfiles Requeridos para la Iniciativa | Repeater | Añada una entrada por cada tipo de cargo requerido. | |
| FORM-ANEXO1-S1-NOMBRE-CARGO-01 | Sección 1: Perfiles de Cargo | Nombre del cargo | Text | | Req: mandatory. |
| FORM-ANEXO1-S1-NUMERO-CARGOS-01 | Sección 1: Perfiles de Cargo | N° de Cargos | Number | | Req: mandatory. Min-Val: 1. |
| FORM-ANEXO1-S1-DEPTO-SUPERVISOR-01 | Sección 1: Perfiles de Cargo | Departamento supervisor | Text | | Req: mandatory. |
| FORM-ANEXO1-S1-PERFIL-CARGO-01 | Sección 1: Perfiles de Cargo | Perfil del Cargo | TextArea | Detallar la formación, experiencia y competencias requeridas. | Req: mandatory. |
| FORM-ANEXO1-S1-PERIODO-CONTRATACION-01 | Sección 1: Perfiles de Cargo | Periodo de contratación | Text | Ej: 12 meses, media jornada. | Req: mandatory. |
| FORM-ANEXO1-S1-OBJETIVO-CARGO-01 | Sección 1: Perfiles de Cargo | Objetivo del cargo | TextArea | | Req: mandatory. |
| FORM-ANEXO1-S1-PRODUCTOS-ASOCIADOS-01 | Sección 1: Perfiles de Cargo | Productos asociados a la contratación | TextArea | Listar los entregables o productos verificables. | Req: mandatory. |
| FORM-ANEXO1-S2-FIRMA-REP-LEGAL-01 | Sección 2: Firma | Nombre, firma y timbre del representante legal | Static-Text | Espacio reservado para la firma manuscrita. | |
### Certificado Pertinencia y Patrocinio GORE
- **Ref SFD Guide:** GUIDE-SFD-STS-MASTER-01
#### Campos
| ID | Seccion | Field-Label | Field-Type | Field-Constraint |
| --- | --- | --- | --- | --- |
| FORM-PPR-PATROCINIO-S1-NOMBRE-PROGRAMA | Sección 1: Información del Programa | NOMBRE DEL PROGRAMA | Text | Req: mandatory. |
| FORM-PPR-PATROCINIO-S1-INSTITUCION | Sección 1: Información del Programa | INSTITUCIÓN POSTULANTE | Text | Req: mandatory. |
| FORM-PPR-PATROCINIO-S1-PROPOSITO | Sección 1: Información del Programa | PROPÓSITO DEL PROGRAMA | TextArea | Req: mandatory. |
| FORM-PPR-PATROCINIO-S1-MONTO-FNDR | Sección 1: Información del Programa | MONTO TOTAL SOLICITADO FNDR (M$) | Number | Req: mandatory. |
| FORM-PPR-PATROCINIO-S2-DIVISION-GORE | Sección 2: Evaluación de Pertinencia de la División GORE | División GORE Patrocinante | Text | Req: mandatory. |
| FORM-PPR-PATROCINIO-S2-JUSTIFICACION-PERTINENCIA | Sección 2: Evaluación de Pertinencia de la División GORE | Justificar la ejecución del programa, describiendo su pertinencia y alineación con los objetivos estratégicos de la División y la Estrategia Regional de Desarrollo. | TextArea | Req: mandatory. |
| FORM-PPR-PATROCINIO-S2-SINERGIA-DUPLICIDAD | Sección 2: Evaluación de Pertinencia de la División GORE | ¿Se identifica sinergia o duplicidad con otras iniciativas GORE en curso? Detallar. | TextArea | Req: mandatory. |
| FORM-PPR-PATROCINIO-S3-FIRMA-JEFE-DIVISION | Sección 3: Firma | Nombre, firma y timbre del Jefe de División patrocinante GORE | Static-Text | |
### Declaracion Jurada Rendiciones
- **Ref SFD Guide:** GUIDE-SFD-STS-MASTER-01
#### Campos
| ID | Seccion | Field-Label | Field-Type | Field-Constraint |
| --- | --- | --- | --- | --- |
| FORM-PPR-REN-S1-INSTR | Sección 1: Identificación | | | |
| FORM-PPR-REN-S1-NOMBRE-PROGRAMA | Sección 1: Identificación | Nombre del Programa | Text | Req: mandatory. |
| FORM-PPR-REN-S1-NOMBRE-REPRESENTANTE | Sección 1: Identificación | Nombre del Representante Legal | Text | Req: mandatory. |
| FORM-PPR-REN-S1-INSTITUCION | Sección 1: Identificación | Institución a la que representa | Text | Req: mandatory. |
| FORM-PPR-REN-S2-ESTADO-RENDICIONES | Sección 2: Declaración | La institución que represento actualmente, mantiene rendiciones de cuenta pendiente con el Gobierno Regional de Ñuble. | Radio | Req: mandatory. |
| FORM-PPR-REN-S2-AVISO-CAUCION | Sección 2: Declaración | Aviso sobre Caución | Static-Text | |
| FORM-PPR-REN-S2-COMPROMISO-RES30 | Sección 2: Declaración | Declaro estar en conocimiento de los alcances y responsabilidades establecidas en la Resolución N°30 de 2015 de la Contraloría General de la República. | Checkbox | Req: mandatory. |
| FORM-PPR-REN-S2-COMPROMISO-SISREC | Sección 2: Declaración | Declaro que, en caso de ser aprobada, las rendiciones del programa deben realizarse por medio de plataforma SISREC de la Contraloría General de la República. | Checkbox | Req: mandatory. |
| FORM-PPR-REN-S3-FIRMA-REP-LEGAL | Sección 3: Firma | Nombre, firma y timbre del representante legal | Static-Text | |
### Declaracion Jurada No Fraccionamiento
- **Ref SFD Guide:** GUIDE-SFD-STS-MASTER-01
#### Campos
| ID | Seccion | Field-Label | Field-Type | Field-Constraint |
| --- | --- | --- | --- | --- |
| FORM-PPR-NOFRACC-S1-INSTR | Sección 1: Identificación | | | |
| FORM-PPR-NOFRACC-S1-NOMBRE-PROGRAMA | Sección 1: Identificación | Nombre del Programa | Text | Req: mandatory. |
| FORM-PPR-NOFRACC-S1-NOMBRE-REPRESENTANTE | Sección 1: Identificación | Nombre del Representante Legal | Text | Req: mandatory. |
| FORM-PPR-NOFRACC-S1-INSTITUCION | Sección 1: Identificación | Institución a la que representa | Text | Req: mandatory. |
| FORM-PPR-NOFRACC-S2-DECLARACION-NOFRACC | Sección 2: Declaración | Declaro QUE EL PROGRAMA POSTULADO ABORDA UN OBJETIVO Y PROBLEMA ÚNICO, Y NO CONSTITUYE UN FRACCIONAMIENTO DE UNA INICIATIVA MAYOR. | Checkbox | Req: mandatory. |
| FORM-PPR-NOFRACC-S2-ACLARACION | Sección 2: Declaración | Aclaración sobre propósito único | Static-Text | |
| FORM-PPR-NOFRACC-S3-FIRMA-REP-LEGAL | Sección 3: Firma | Nombre, firma y timbre del representante legal | Static-Text | |
### Certificado Compromiso Presupuesto y Finanzas
- **Ref SFD Guide:** GUIDE-SFD-STS-MASTER-01
#### Campos
| ID | Seccion | Field-Label | Field-Type | Field-Constraint |
| --- | --- | --- | --- | --- |
| FORM-PPR-FIN-S1-INSTR | Sección 1: Identificación | | | |
| FORM-PPR-FIN-S1-NOMBRE-PROGRAMA | Sección 1: Identificación | Nombre del Programa | Text | Req: mandatory. |
| FORM-PPR-FIN-S1-NOMBRE-ENCARGADO-FINANZAS | Sección 1: Identificación | Nombre del Encargado de Presupuesto o Finanzas | Text | Req: mandatory. |
| FORM-PPR-FIN-S1-CARGO-ENCARGADO | Sección 1: Identificación | Cargo | Text | Req: mandatory. |
| FORM-PPR-FIN-S1-INSTITUCION | Sección 1: Identificación | Institución a la que representa | Text | Req: mandatory. |
| FORM-PPR-FIN-S2-INTENCION-CAPACIDAD | Sección 2: Declaración de Compromiso | Declaro que el servicio tiene la intención y capacidad administrativa para recibir la transferencia desde el Gobierno Regional de Ñuble y administrarla en una cuenta o centro de costo separado. | Checkbox | Req: mandatory. |
| FORM-PPR-FIN-S2-MONTO-FNDR | Sección 2: Declaración de Compromiso | Monto FNDR solicitado (M$) | Number | Req: mandatory. |
| FORM-PPR-FIN-S2-MONTO-APORTE-PROPIO | Sección 2: Declaración de Compromiso | Monto Aporte Propio (M$) | Number | Req: mandatory. |
| FORM-PPR-FIN-S2-AUTORIZACION-APORTE-PROPIO | Sección 2: Declaración de Compromiso | Declaro que el aporte propio se encuentra autorizado y estará disponible según la programación financiera presentada. | Checkbox | Req: conditional. Visible si Monto Aporte Propio > 0. |
| FORM-PPR-FIN-S2-NO-RESP-GORE | Sección 2: Declaración de Compromiso | Declaro que, en caso de ejecutar el programa, no será responsabilidad del Gobierno Regional el financiamiento posterior al término del mismo. | Checkbox | Req: mandatory. |
| FORM-PPR-FIN-S2-CONTINUIDAD-GASTO-CORRIENTE | Sección 2: Declaración de Compromiso | Declaro que, en caso de que la entidad decida continuar la iniciativa post-convenio, los costos serán cargados al presupuesto regular del servicio. | Checkbox | Req: mandatory. |
| FORM-PPR-FIN-S3-FIRMA-JEFE-ADMON-FIN | Sección 3: Firma | Nombre, firma y timbre del Jefe de División o Departamento de Administración y Finanzas | Static-Text | |

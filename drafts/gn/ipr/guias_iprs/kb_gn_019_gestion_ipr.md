---
_manifest:
  urn: urn:gorenuble:gn:gestion-ipr:1.0.0
version: 1.0.0
status: draft
tags:
- koda-spec
- koraficated
lang: es
---

**Ctx:** Guía operacional completa para la gestión de Intervenciones Públicas Regionales (IPR) en el GORE Ñuble, desde el ingreso hasta el cierre y evaluación ex-post.

<!-- ID: GN-IPR-GESTION-OPERACIONAL-01 -->

<!-- ID: KODA-LLM-PARSER-01 -->

## Glosario IPR Gestion
<!-- ID: GN-IPR-GLOSARIO-01 -->
**Purp:** Definir conceptos y siglas operativas recurrentes en la gestión de IPR.

### Terminos
#### Intervención Pública Regional
<!-- ID: GN-IPR-GLOS-IPR -->
**Sigla:** IPR

**Def:** Término paraguas para cualquier acción (proyecto, programa, estudio) financiada por el GORE para objetivos de desarrollo.

#### Iniciativa de Inversión
<!-- ID: GN-IPR-GLOS-IDI -->
**Sigla:** IDI

**Def:** Tipo de IPR asociada a proyectos de capital (obras, activos).

#### Programa Público Regional
<!-- ID: GN-IPR-GLOS-PPR -->
**Sigla:** PPR

**Def:** Tipo de IPR de gasto corriente o mixto (servicios, subvenciones).

#### Postulación de IPR
<!-- ID: GN-IPR-GLOS-POSTULACION -->
**Sigla:** Postulación

**Def:** IPR presentada para evaluación, antes de clasificación o aprobación.

#### Recomendación Satisfactoria
<!-- ID: GN-IPR-GLOS-RS -->
**Sigla:** RS

**Def:** Resultado favorable de evaluación SNI/MDSF para IDI de mayor envergadura.

#### Recomendación Favorable
<!-- ID: GN-IPR-GLOS-RF -->
**Sigla:** RF

**Def:** Resultado favorable de evaluación de programas en Glosa 06 u otros mecanismos.

#### Admisible para financiamiento (Conservación)
<!-- ID: GN-IPR-GLOS-AD -->
**Sigla:** AD

**Def:** Resultado favorable de evaluación MDSF para proyectos de conservación; habilita financiamiento sin ser RS.

#### Certificado de Disponibilidad Presupuestaria
<!-- ID: GN-IPR-GLOS-CDP -->
**Sigla:** CDP

**Def:** Documento del Depto. Presupuesto que acredita fondos para financiar una IPR.

#### Banco Integrado de Proyectos
<!-- ID: GN-IPR-GLOS-BIP -->
**Sigla:** BIP

**Def:** Sistema para registro y seguimiento de IDI.

#### Sistema de Información para la Gestión Financiera del Estado
<!-- ID: GN-IPR-GLOS-SIGFE -->
**Sigla:** SIGFE

**Def:** Sistema contable-financiero donde se registra ejecución presupuestaria.

#### Sistema de Rendición Electrónica de Cuentas
<!-- ID: GN-IPR-GLOS-SISREC -->
**Sigla:** SISREC

**Def:** Plataforma de la Contraloría General de la República para rendiciones de cuentas de transferencias.

#### División de Presupuesto e Inversión Regional
<!-- ID: GN-IPR-GLOS-DIPIR -->
**Sigla:** DIPIR

**Def:** División GORE responsable de presupuesto de inversión y gestión de IPR.

#### División de Planificación y Desarrollo Regional
<!-- ID: GN-IPR-GLOS-DIPLADE -->
**Sigla:** DIPLADE

**Def:** División que lidera planificación y presidencia del Comité Directivo Regional.

#### Consejo Regional
<!-- ID: GN-IPR-GLOS-CORE -->
**Sigla:** CORE

**Def:** Órgano colegiado que aprueba o rechaza financiamiento de IPR según normativa y acuerdos regionales.

#### Comité Directivo Regional
<!-- ID: GN-IPR-GLOS-CDR -->
**Sigla:** CDR

**Def:** Instancia técnico-política interna para filtro de pertinencia estratégica de IPR.

#### Ministerio de Desarrollo Social y Familia
<!-- ID: GN-IPR-GLOS-MDSF -->
**Sigla:** MDSF

**Def:** Organismo responsable de evaluación técnico-económica de IDI en el SNI.

#### Estados de admisibilidad IPR
<!-- ID: GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD -->
**Def:** Categorías clave: PRE-ADMISIBLE CDR, NO PRE-ADMISIBLE CDR, ADMISIBLE, ADMISIBLE CON OBSERVACIONES, INADMISIBLE.

#### Estados de financiamiento IPR
<!-- ID: GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO -->
**Def:** Categorías clave: PARA REVISIÓN TÉCNICA, EN CARTERA PRE-ADMISIBLE, ENVIADO A MDSF, APROBADO TÉCNICAMENTE (RS/RF/AD/Exento RS), CARTERA ENVIADA A CORE, CERTIFICADO CORE OK, ENVIADO A FINANCIAMIENTO, TRANSFERENCIA PROGRAMADA, CONVENIO FORMALIZADO.

## Proceso Gestion Operacional IPR
<!-- ID: GN-IPR-PROCESO-END-TO-END -->
**Purp:** Estandarizar el flujo completo de gestión de IPR en GORE Ñuble: desde el ingreso hasta el cierre.

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-IDI
- GN-IPR-GLOS-PPR

**Res:**
- Secuencia clara de fases, actores, decisiones y documentos clave.
- Trazabilidad normativa y documental de cada hito.

**Fnd:**
- LOC GORE (Art. 16, 24, 36, 78).
- DL N°1.263/1975 (Art. 19 bis).
- Ley 20.530 (Crea MDSF).
- Glosas 01, 06, 07 Ley de Presupuestos 2026 (Partida 31).
- Normas Generales Ley de Presupuestos 2026 (Art. 23-26).
- Res. 30/2015 CGR (Rendiciones).
- Normativa DIPRES/MDSF sobre SNI, BIP, procedimientos especiales.

**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-NORMAS-GENERALES

### Fases
| Ref |
| --- |
| GN-IPR-FASE1-INGRESO |
| GN-IPR-FASE2-EVAL |
| GN-IPR-FASE3-FINANC |
| GN-IPR-FASE4-GESTION-PPT |
| GN-IPR-FASE5-EJECUCION |
| GN-IPR-FASE6-MODIFICACIONES |
| GN-IPR-FASE7-CIERRE |

### Fase 1 Ingreso Pertinencia Admisibilidad
<!-- ID: GN-IPR-FASE1-INGRESO -->
**Purp:** Recepcionar, registrar y filtrar postulaciones de IPR para decidir cuáles avanzan a evaluación técnica.

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-POSTULACION

**Res:**
- Lista de IPR con registro formal y trazabilidad.
- Clasificación estratégica inicial y decisión de admisibilidad formal.

**Fnd:**
- LOC GORE Art. 16 y 24.

#### Secciones
##### 2.1 Recepción y Registro
<!-- ID: GN-IPR-F1-RECEPCION-REGISTRO -->
**Purp:** Formalizar ingreso de postulaciones y derivarlas a DIPIR.

**Ref:**
- GN-IPR-GLOS-POSTULACION
- GN-IPR-GLOS-DIPIR

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Unidad Formuladora (Externa) | GN-IPR-GLOS-IPR, GN-IPR-GLOS-POSTULACION | Preparar y presentar IPR según guías del mecanismo de financiamiento. | Oficio y antecedentes completos presentados al GORE. |
| 2 | Oficina de Partes GORE | GN-IPR-GLOS-DIPIR | Recepcionar oficio y documentación física/digital., Asignar número de ingreso único en sistema de gestión documental (ej. SGDOC)., Derivar antecedentes completos a Jefatura DIPIR. | Postulación registrada y derivada formalmente a DIPIR. |
| 3 | Jefatura DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-CDR | Registrar datos básicos de la IPR en sistema de seguimiento interno., Poner la postulación a disposición del Comité Directivo Regional (CDR). | Postulación disponible para revisión del CDR. |

##### 2.2 Análisis de Pertinencia Estratégica (Filtro Político-Técnico)
<!-- ID: GN-IPR-F1-PERTINENCIA-CDR -->
**Purp:** Evaluar alineación de la IPR con prioridades estratégicas antes de invertir en evaluación técnica.

**Resp_Principal:** Comité Directivo Regional (CDR).

**Ref:**
- GN-IPR-GLOS-CDR
- GN-IPR-GLOS-DIPLADE
- GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Jefatura DIPLADE | GN-IPR-GLOS-DIPLADE | Recibir listado de postulaciones ingresadas., Convocar a sesión del CDR como presidente de la instancia. | CDR convocado con cartera de IPR a revisar. |
| 2 | CDR | GN-IPR-GLOS-CDR, GN-IPR-GLOS-IPR | Analizar cada IPR desde perspectiva técnico-política., Evaluar coherencia con ERD y prioridades estratégicas del GORE., Evaluar viabilidad preliminar y pertinencia., Generar acta de sesión con categorización y observaciones por IPR. | `PRE-ADMISIBLE CDR`, `NO PRE-ADMISIBLE CDR` |
| 3 | Jefatura DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Recibir acta del CDR., Para IPR PRE-ADMISIBLES, evaluar marco presupuestario disponible y cartera de inversiones vigente., Priorizar IPR para revisión técnica según relevancia y factibilidad de financiamiento. | `PARA REVISIÓN TÉCNICA`, `EN CARTERA PRE-ADMISIBLE` |

##### 2.3 Revisión de Admisibilidad Formal (Filtro Documental)
<!-- ID: GN-IPR-F1-ADMISIBILIDAD-FORMAL -->
**Purp:** Verificar requisitos formales y documentales exigidos por el mecanismo de financiamiento.

**Ref:**
- GN-IPR-GLOS-DIPIR
- GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Jefatura de Preinversión (DIPIR) | GN-IPR-GLOS-DIPIR | Recibir instrucción de Jefatura DIPIR para iniciar revisión., Asignar la IPR a analista competente según tipología., Formalizar apoyos interdivisionales si se requieren. | IPR derivada formalmente a analista. |
| 2 | Analista de Preinversión (DIPIR) | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD | Realizar revisión documental exhaustiva., Verificar cumplimiento de requisitos de la guía operativa del mecanismo., Comprobar correcta carga en Carpeta Digital del BIP cuando aplique. | `ADMISIBLE`, `ADMISIBLE CON OBSERVACIONES`, `INADMISIBLE` |
| 3 | Unidad Formuladora (Externa) | GN-IPR-GLOS-IPR, GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD | Corregir antecedentes dentro del plazo definido por el GORE. | Documentación subsanada. |
| 4 | Jefatura de Preinversión (DIPIR) | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Si estado final es INADMISIBLE, elaborar y despachar oficio de inadmisibilidad., Si es ADMISIBLE o subsanada, declarar estado PARA EVALUACIÓN TÉCNICA. | `INADMISIBLE INFORMADO`, `LISTA PARA FASE 2` |

### Fase 2 Evaluacion Tecnica Economica
<!-- ID: GN-IPR-FASE2-EVAL -->
**Purp:** Analizar en profundidad la IPR para determinar calidad, viabilidad y conveniencia, aplicando principio de proporcionalidad.

**Fnd:**
- Art. 19 bis DL N°1.263/1975.
- Ley 20.530 (Crea MDSF).

**Warn:**
- Proceso y criterios varían según nivel de proporcionalidad y mecanismo de financiamiento.

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-IDI
- GN-IPR-GLOS-PPR
- GN-IPR-GLOS-MDSF
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

#### Tracks
##### 3.1 Track A – SNI (Análisis Estándar y Enriquecido, Nivel 2 y 3)
<!-- ID: GN-IPR-F2-TRACK-A-SNI -->
**Purp:** Evaluar IDI de mayor envergadura que requieren RS de MDSF.

**Ref:**
- GN-IPR-GLOS-IDI
- GN-IPR-GLOS-MDSF
- GN-IPR-GLOS-RS
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Analista GORE (DIPIR) | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-IDI, GN-IPR-GLOS-ESTADOS-ADMISIBILIDAD | Revisión de fondo considerando antecedentes de Fase 1., Verificar cumplimiento de RIS y metodologías SNI aplicables., Asegurar calidad de estudios preinversionales (Perfil, Prefactibilidad, etc.)., Elaborar Acta de Admisibilidad interna GORE. | `ADMISIBLE PARA ENVÍO A MDSF`, `INADMISIBLE` |
| 2 | Jefatura DIPIR / Gobernador/a | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-MDSF | Elaborar y visar oficio solicitando evaluación ex ante al SEREMI MDSF., Gestionar cadena de V°B° interno y firma del Gobernador/a. | Oficio despachado a MDSF. |
| 3 | Jefatura de Preinversión (DIPIR) | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-BIP, GN-IPR-GLOS-MDSF | Registrar formalmente la 'Informar Postulación' en el BIP. | Iniciativa `ENVIADO A MDSF` en BIP. |
| 4 | Analista MDSF | GN-IPR-GLOS-MDSF, GN-IPR-GLOS-RS | Realizar evaluación de admisibilidad (plazo orientativo: 5 días)., Realizar análisis técnico-económico (ATE) (plazo orientativo: 10 días). | RATE: `RS`, `FI`, u `OT`. |
| 5 | Unidad Formuladora / Analista GORE | GN-IPR-GLOS-IPR, GN-IPR-GLOS-RS, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Si RS: registrar aprobación técnica y preparar paso a financiamiento., Si FI u OT: apoyar a la Unidad Formuladora en subsanar observaciones (plazo máx. 60 días hábiles). | `APROBADO TÉCNICAMENTE (RS)`, `OBSERVACIONES SUBSANADAS` |
| 6 | Jefatura de Preinversión (DIPIR) | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-BIP, GN-IPR-GLOS-RS | Monitorear BIP para obtener resultado de MDSF., Informar cartera con RS a Jefatura DIPIR para preparación de presentación al Gobernador/a. | Cartera RS disponible para priorización. |

##### 3.2 Track B – Programas Públicos Regionales (Glosa 06)
<!-- ID: GN-IPR-F2-TRACK-B-PPR -->
**Purp:** Evaluar programas de gasto corriente/mixto ejecutados por el GORE según proceso bifásico DIPRES/SES.

**Ref:**
- GN-IPR-GLOS-PPR
- GN-IPR-GLOS-RF
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

**Req:**
- Se podrá destinar hasta un 5% del monto total de la transferencia a gastos de administración de las iniciativas en el Gobierno Regional, según glosa aplicable.
- Con cargo a esta transferencia se podrá contratar en la entidad pública receptora a personal a honorarios cuyo vínculo cesará una vez finalizado el convenio, dentro del límite establecido por la glosa aplicable.
- Cuando corresponda, considerar la calidad de agente público para honorarios según glosa aplicable.

**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-06

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | División Proponente GORE / DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-PPR | Elaborar Formulario de Perfil de Programa Público GORE. | Formulario de Perfil enviado a DIPRES/SES. |
| 2 | DIPRES / SES |  | Evaluar si iniciativa corresponde a programa y si es pertinente. | Aprobado: solicitud formal a GORE para elaborar Diseño., Rechazado: proceso se detiene. |
| 3 | División Proponente GORE / DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-PPR | Elaborar Formulario de Diseño con Metodología de Marco Lógico. | Formulario de Diseño enviado. |
| 4 | DIPRES / SES |  | Revisión iterativa de diseño., Emisión de observaciones y recepción de subsanaciones. | Calificación final: `RF`, `OT` o `FI`. |
| 5 | División Proponente GORE / DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-RF, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Subsanar observaciones hasta lograr RF. | `APROBADO TÉCNICAMENTE (RF)` |

##### 3.3 Track C – Vías Simplificadas y Procedimientos Especiales
<!-- ID: GN-IPR-F2-TRACK-C-ESPECIALES -->
**Purp:** Detallar procesos de evaluación para mecanismos agilizados.

**Ref:**
- GN-IPR-GLOS-IDI
- GN-IPR-GLOS-MDSF
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

###### Subtracks
###### Proyectos < 5.000 UTM (Exención de RS)
<!-- ID: GN-IPR-F2-C-5000UTM -->
**Ref:**
- GN-IPR-GLOS-IDI
- GN-IPR-GLOS-RS
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Unidad Formuladora | GN-IPR-GLOS-IDI | Postular proyecto en BIP a etapa Ejecución o Diseño. | IDI postulada con descriptor específico. |
| 2 | Unidad Formuladora | GN-IPR-GLOS-IDI, GN-IPR-GLOS-BIP | Cargar en BIP estudio preinversional simplificado y demás antecedentes exigidos. | Carpeta digital completa. |
| 3 | Institución Financiera (GORE) | GN-IPR-GLOS-MDSF | Enviar carta de responsabilidad a MDSF declarando ausencia de impedimentos y fraccionamiento. | Carta enviada a MDSF. |
| 4 | DIPIR GORE | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-IDI | Verificar cumplimiento del procedimiento y antecedentes. | `APROBADO TÉCNICAMENTE (Exento RS)` |

###### Proyectos de Conservación
<!-- ID: GN-IPR-F2-C-CONSERVACION -->
**Ref:**
- GN-IPR-GLOS-IDI
- GN-IPR-GLOS-AD
- GN-IPR-GLOS-MDSF

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Unidad Formuladora | GN-IPR-GLOS-IDI | Postular IDI en BIP con proceso 'Conservación'. | IDI postulada correctamente. |
| 2 | Analista GORE (DIPIR) | GN-IPR-GLOS-DIPIR | Revisar coherencia de postulación con instructivo de conservación. | V°B° para envío a MDSF. |
| 3 | Jefatura DIPIR / GORE | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-MDSF | Enviar oficio a MDSF solicitando evaluación de admisibilidad. | IDI `ENVIADA A MDSF` en BIP. |
| 4 | Analista MDSF | GN-IPR-GLOS-MDSF, GN-IPR-GLOS-AD, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Verificar que IDI clasifique como conservación., Emitir RATE AD. | `APROBADO TÉCNICAMENTE (AD)` |

###### FRIL, 8% FNDR, FRPD y Circular 33
<!-- ID: GN-IPR-F2-C-FRIL-8FNDR-FRPD-CIRC33 -->
**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-07
- urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-12

###### Elementos
| Cpt | Def |
| --- | --- |
| FRIL. | Evaluación de mérito realizada por el GORE según instructivo. Aprobación técnica interna. Considerar informe favorable del MDSF cuando aplique financiamiento vía transferencias de capital (FRIL), según glosa aplicable. |
| 8% FNDR. | Concurso público con bases y pautas específicas; evalúa y puntúa iniciativas. |
| FRPD (Royalty). | Fondo evaluado según bases del concurso FRPD. |
| Circular 33 (ANF, Estudios). | Tramitación vía DIPRES y V°B° DIPRES como aprobación técnica GORE. |

### Fase 3 Financiamiento y Aprobacion Presupuestaria
<!-- ID: GN-IPR-FASE3-FINANC -->
**Purp:** Gestionar asignación de recursos presupuestarios para IPR con aprobación técnica, incluyendo aprobación CORE cuando aplique.

**Fnd:**
- LOC GORE Art. 36 y 78.
- Glosa 01, Partida 31, Ley Presupuestos 2026.

**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-partida-31:1.0.0#GN-LEY-PPTO-2026-P31-GLO-01

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-CORE
- GN-IPR-GLOS-CDP
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

#### Secciones
##### 4.1 Modificaciones Presupuestarias sin Acuerdo Obligatorio CORE
<!-- ID: GN-IPR-F3-SIN-CORE -->
**Ref:**
- GN-IPR-GLOS-CDP
- GN-IPR-GLOS-DIPIR

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Jefatura DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-CDP | Analizar cartera de IPR con aprobación técnica., Solicitar al Depto. Presupuesto la emisión del CDP. | Solicitud de CDP enviada. |
| 2 | Jefatura Depto. Presupuesto (DAF) | GN-IPR-GLOS-CDP | Verificar disponibilidad de fondos., Elaborar y enviar CDP a unidad solicitante. | CDP emitido. |
| 3 | Jefatura de Preinversión / Unidad Patrocinante | GN-IPR-GLOS-IPR, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Recibir CDP., Enviar memo al Depto. Presupuesto instruyendo iniciar tramitación de modificación presupuestaria. | `ENVIADO A FINANCIAMIENTO` |

##### 4.2 Iniciativas con Aprobación Obligatoria del CORE
<!-- ID: GN-IPR-F3-CON-CORE -->
**Ref:**
- GN-IPR-GLOS-CORE
- GN-IPR-GLOS-DIPIR
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Jefatura DIPIR | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-IPR | Analizar cartera de IPR con aprobación técnica., Solicitar preparación de documentación para CORE. | `INSTRUCCIÓN PARA PREPARAR ENVÍO A CORE` |
| 2 | Jefatura de Preinversión (DIPIR) | GN-IPR-GLOS-DIPIR | Elaborar carpeta CORE (oficios, fichas IDI, antecedentes de respaldo). | `CARTERA DISPONIBLE PARA ENVÍO A CORE` |
| 3 | Jefatura DIPIR / Gobernador/a | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-CORE | Presentar cartera al Gobernador/a para V°B° final., Firmar oficio y enviar formalmente cartera al CORE. | `CARTERA ENVIADA A CORE` |
| 4 | CORE | GN-IPR-GLOS-CORE, GN-IPR-GLOS-IPR | Analizar cartera en comisiones y sesión plenaria., Votar aprobación o rechazo del financiamiento. | `IPR APROBADAS/RECHAZADAS` |
| 5 | Secretario/a Ejecutivo CORE | GN-IPR-GLOS-CORE, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Comunicar resultados y emitir Certificado de Acuerdo CORE., Usar formato estandarizado de certificado indicado por DIPRES para el año presupuestario vigente. | `CERTIFICADO CORE OK` |
| 6 | Jefatura DIPIR / Jefatura Preinversión | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-IPR | Con certificado CORE, solicitar al Depto. Presupuesto la creación de asignación presupuestaria. | `ENVIADA A CREACIÓN PPT.` |

### Fase 4 Gestion Presupuestaria y Formalizacion
<!-- ID: GN-IPR-FASE4-GESTION-PPT -->
**Purp:** Traducir aprobación de financiamiento en actos administrativos y convenios que permitan ejecutar y transferir recursos.

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

#### Secciones
##### 5.1 Tramitación de Actos Administrativos (Decretos y Resoluciones)
<!-- ID: GN-IPR-F4-ACTOS-ADMIN -->
###### Tabla Pasos
| Step | Resp | Activities | Output |
| --- | --- | --- | --- |
| 1 | Profesional Depto. Presupuesto | Elaborar borrador de Resolución (modificación interna) o solicitud a DIPRES para Decreto (afecta Partida 31). | Borrador de Resolución / Solicitud de Decreto. |
| 2 | DAF / DIPIR / Unidad de Control |  | Acto visado internamente. |
| 3 | Gobernador/a | Firmar resolución interna o oficio a DIPRES para tramitación del Decreto. | Acto firmado. |
| 4 | GORE / DIPRES / CGR | Si Resolución GORE: enviar a DIPRES para visación y a CGR para Toma de Razón., Si Decreto DIPRES: DIPRES elabora, envía a CGR para Toma de Razón y publica. | `RESOLUCIÓN/DECRETO CON TOMA DE RAZÓN` |

##### 5.2 Elaboración y Firma de Convenio
<!-- ID: GN-IPR-F4-CONVENIO -->
**Warn:**
- La transferencia de recursos solo puede materializarse después de la total tramitación del convenio.

**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART23
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART24
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART25
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART26

###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Profesional Depto. Presupuesto | GN-IPR-GLOS-IPR | Con asignación presupuestaria asegurada, elaborar borrador de Convenio de Transferencia. | Borrador de Convenio. |
| 2 | DIPIR / Jurídico / Unidad Técnica Receptora | GN-IPR-GLOS-DIPIR | Revisar y visar borrador del convenio. | Convenio visado internamente. |
| 3 | Gabinete / Oficina de Partes |  | Coordinar firma de convenio entre Gobernador/a y representante legal de entidad receptora. | `CONVENIO FIRMADO` |

##### 5.3 Formalización Final y Devengo Presupuestario
<!-- ID: GN-IPR-F4-FORMALIZACION-DEVENGO -->
**Purp:** Tramitar actos que aprueban convenio y aplicar reglas de devengo.

**Ref:**
- GN-IPR-GLOS-SIGFE
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

###### Tabla Pasos
| Step | Resp | Activities | Output |
| --- | --- | --- | --- |
| 1 | Profesional Depto. Presupuesto | Elaborar Resolución que aprueba convenio y lo deja formalmente vigente. | Borrador de Resolución de aprobación. |
| 2 | GORE / CGR | Firmar resolución., Si corresponde según normativa CGR aplicable, enviar a CGR para Toma de Razón. | `CONVENIO FORMALIZADO (TRAMITADO)` |
| 3 | Profesional DAF / DIPIR | Programar transferencias considerando: | `TRANSFERENCIA PROGRAMADA` |

### Fase 5 Ejecucion y Seguimiento
<!-- ID: GN-IPR-FASE5-EJECUCION -->
**Purp:** Monitorear desarrollo de la IPR, asegurando cumplimiento técnico y uso correcto de recursos.

**Fnd:**
- Ley 19.886 (Compras Públicas).
- Res. 30/2015 CGR (Rendiciones).

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-BIP
- GN-IPR-GLOS-SIGFE
- GN-IPR-GLOS-SISREC

#### Secciones
##### 6.1 Inicio del Proyecto y Reuniones de Coordinación
<!-- ID: GN-IPR-F5-INICIO-COORDINACION -->
###### Tabla Pasos
| Step | Resp | Activities | Output |
| --- | --- | --- | --- |
| 1 | División Patrocinante / Depto. Inversiones | Antes del inicio, chequear documentación técnica aprobada (EE.TT., planos, etc.). | Revisión conforme de antecedentes. |
| 2 | División Patrocinante / Depto. Presupuesto / Unidad Técnica Receptora | Convocar reunión formal GORE–UT receptora., Aclarar roles, responsabilidades, plazos, hitos de control y procedimientos de rendición. | Acta de reunión con acuerdos. |
| 3 | Supervisor/a del Proyecto (GORE) | Crear carpeta de seguimiento (digital/física) con todos los antecedentes del proyecto. | Carpeta de seguimiento creada. |

##### 6.2 Licitación y Adjudicación (cuando aplica)
<!-- ID: GN-IPR-F5-LICITACION -->
**Req:**
- Proyectos y programas de inversión: licitación pública obligatoria cuando el monto sea superior a 1.000 UTM, salvo excepciones por emergencia según normativa aplicable.
- Estudios básicos: licitación pública obligatoria cuando el monto sea superior a 500 UTM, salvo excepciones por emergencia según normativa aplicable.

**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART06

###### Tabla Pasos
| Step | Resp | Activities | Output |
| --- | --- | --- | --- |
| 1 | Unidad Técnica Receptora | Elaborar bases de licitación y publicar en Mercado Público., Gestionar proceso de licitación para contratar ejecución. | Licitación adjudicada. |
| 2 | Unidad Técnica Receptora | Firmar contrato con adjudicatario. | Contrato firmado. |
| 3 | Unidad Técnica Receptora | Formalizar inicio de ejecución física (Entrega de Terreno u Orden de Inicio). | Acta de Entrega de Terreno u Orden de Inicio. |

##### 6.3 Seguimiento y Supervisión
<!-- ID: GN-IPR-F5-SEGUIMIENTO -->
###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Supervisor/a del Proyecto (GORE) | GN-IPR-GLOS-BIP | Realizar visitas a terreno periódicas., Revisar informes de avance de la UT., Gestionar Estados de Pago cuando aplique., Actualizar BIP con % de avance físico. | Informes de visita y supervisión, avance en BIP. |
| 2 | Analista Financiero (DAF/DIPIR) | GN-IPR-GLOS-SIGFE, GN-IPR-GLOS-SISREC | Monitorear ejecución presupuestaria en SIGFE., Revisar rendiciones de cuentas en SISREC., Alertar sobre sub-ejecución o desviaciones. | Informes de ejecución financiera. |
| 3 | Comité de Seguimiento (si aplica) |  | Realizar reuniones periódicas GORE–UT para revisar estado integral de la IPR. | Actas de reunión con acuerdos y planes de acción. |

### Fase 6 Gestion de Modificaciones IPR
<!-- ID: GN-IPR-FASE6-MODIFICACIONES -->
**Purp:** Gestionar formalmente cambios durante la ejecución, asegurando viabilidad y legalidad.

**Fnd:**
- LOC GORE Art. 36.
- Glosa 01 Ley de Presupuestos 2026 (Partida 31).

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-DIPIR
- GN-IPR-GLOS-CORE
- GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO

#### Secciones
##### 7.1 Solicitud de Modificación
<!-- ID: GN-IPR-F6-SOLICITUD -->
###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Unidad Técnica Receptora | GN-IPR-GLOS-IPR | Detectar necesidad de modificación (sobrecosto, obra adicional, imprevisto, etc.)., Preparar informe técnico y financiero que justifique la modificación. | Informe de solicitud de modificación. |
| 2 | Unidad Técnica Receptora | GN-IPR-GLOS-IPR | Enviar oficio al Gobernador/a solicitando formalmente la modificación, adjuntando informe y antecedentes (nuevos presupuestos, planos, etc.). | Solicitud formal ingresada al GORE. |

##### 7.2 Evaluación de la Modificación (Reevaluación)
<!-- ID: GN-IPR-F6-REEVALUACION -->
###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Supervisor/a GORE / Analista DIPIR | GN-IPR-GLOS-DIPIR | Analizar pertinencia y justificación técnica de la modificación., Verificar que no altere sustancialmente el objetivo del proyecto. | Informe técnico GORE sobre modificación. |
| 2 | DIPIR / DIPLADE | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-DIPLADE | Si cambio es significativo, reevaluar conveniencia de la IPR., Verificar si nuevo costo total supera umbrales que exigen nuevo pronunciamiento CORE o SNI. | Pronunciamiento técnico sobre viabilidad de modificación. |
| 3 | Jefatura DIPIR / GORE | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-CORE | Con base en informes técnicos, aprobar o rechazar la modificación. | Decisión formal sobre modificación. |

##### 7.3 Tramitación de la Modificación
<!-- ID: GN-IPR-F6-TRAMITACION -->
###### Tabla Pasos
| Step | Resp | Ref | Cond | Activities | Output |
| --- | --- | --- | --- | --- | --- |
| 1 | DIPIR / CORE | GN-IPR-GLOS-DIPIR, GN-IPR-GLOS-CORE, GN-IPR-GLOS-ESTADOS-FINANCIAMIENTO | Solo si modificación implica aumento de presupuesto. | Repetir proceso de solicitud de financiamiento y, si aplica, paso por CORE. | Fondos adicionales aprobados. |
| 2 | DAF / Depto. Presupuesto |  |  | Tramitar modificación presupuestaria (Resolución/Decreto)., Modificar convenio de transferencia según corresponda. | Convenio y presupuesto modificados y tramitados. |

### Fase 7 Cierre y Evaluacion ExPost
<!-- ID: GN-IPR-FASE7-CIERRE -->
**Purp:** Formalizar finalización de la IPR y generar lecciones aprendidas mediante evaluación ex-post cuando corresponda.

**Fnd:**
- Res. 30/2015 CGR.

**Ref:**
- GN-IPR-GLOS-IPR
- GN-IPR-GLOS-CORE
- GN-IPR-GLOS-SISREC

#### Secciones
##### 8.1 Cierre Técnico
<!-- ID: GN-IPR-F7-CIERRE-TECNICO -->
###### Tabla Pasos
| Step | Resp | Ref | Activities | Output |
| --- | --- | --- | --- | --- |
| 1 | Unidad Técnica Receptora | GN-IPR-GLOS-IPR | Realizar recepción provisoria y definitiva de obras al contratista., Tras período de garantía, formalizar recepción definitiva. | Acta de Recepción Definitiva de Obras. |
| 2 | Unidad Técnica / Supervisor GORE | GN-IPR-GLOS-IPR | Elaborar informe final de ejecución (productos, metas, resultados)., Validar informe por parte del Supervisor GORE. | Informe final técnico aprobado. |

##### 8.2 Cierre Financiero y Administrativo
<!-- ID: GN-IPR-F7-CIERRE-FINANCIERO -->
**Src:**
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART24
- urn:gorenuble:gn:ley-presupuestos-2026-normas-generales:1.0.0#GN-LEY-PPTO-2026-ART26

###### Tabla Pasos
| Step | Resp | Ref | Activities | Src | Output |
| --- | --- | --- | --- | --- | --- |
| 1 | Unidad Técnica Receptora | GN-IPR-GLOS-SISREC | Presentar rendición final de cuentas en SISREC CGR, sin saldos por rendir. | Normativa CGR de rendiciones y manual interno de gestión de rendiciones del GORE. | Rendición final presentada. |
| 2 | Analista Financiero GORE (DAF) | GN-IPR-GLOS-SISREC | Revisar y aprobar rendición final según guía específica., Solicitar reintegro de saldos no utilizados o gastos rechazados., Pronunciarse de manera fundada sobre la rendición dentro del plazo máximo aplicable, salvo que el convenio establezca un plazo diferente. | Procedimientos internos y normativa CGR vigente. | Rendición final aprobada y saldos reintegrados. |
| 3 | Profesional Depto. Presupuesto | GN-IPR-GLOS-IPR | Elaborar resolución que aprueba la rendición de cuentas y declara cierre del convenio. |  | Resolución de Cierre de Convenio. |
| 4 | DAF / Entidad Receptora |  | Una vez cerrado el convenio, gestionar devolución de garantías. |  | Garantías devueltas. |

##### 8.3 Evaluación Ex-Post
<!-- ID: GN-IPR-F7-EVAL-EXPOST -->
###### Tabla Pasos
| Step | Resp | Activities | Output |
| --- | --- | --- | --- |
| 1 | MDSF / GORE | Seleccionar IPR relevantes para evaluación ex-post. | Muestra de IPR a evaluar. |
| 2 | Equipo Evaluador Externo/Interno | Realizar estudio comparando situación 'con proyecto' vs. 'sin proyecto'. | Informe de Evaluación Ex-Post. |
| 3 | GORE / SNI | Utilizar conclusiones y lecciones aprendidas para mejorar formulación y evaluación de futuras IPR. | Lecciones aprendidas incorporadas al ciclo de inversión. |

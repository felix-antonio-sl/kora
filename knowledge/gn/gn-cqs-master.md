---
_manifest:
  urn: urn:gn:kb:gn-cqs-master
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: ontologies/onto_gorenuble/goreNubleCQs_Master.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- competency-questions
- consultas
- knowledge
- gn
lang: es
extensions:
  gn:
    source_paths:
    - ontologies/onto_gorenuble/goreNubleCQs_Master.yml
    source_hashes:
      ontologies/onto_gorenuble/goreNubleCQs_Master.yml: 54ff9c22ace906e6a52ad6b0c08c11ff59cadc67a90e4605ba777f2a0e142bb0
    source_type: ontology_yaml
    transformation_mode: derive_ttl_scope
    fs: 100
    cr: 3.07
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Preguntas de competencia maestras del bundle ontologico GN.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 23
    meat_count: 1038
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gn-cqs-master.md.json
---

# Catálogo Maestro de Competency Questions

## Scope
Preguntas de competencia maestras del bundle ontologico GN.

## Resumen
- Total CQs: 472
- Dominios: 20
- Existencial: 172
- Relacional: 138
- Temporal: 69
- Agregacion: 93

## 01 Estructura Organizacional
- Existenciales: 8 | Relacionales: 8 | Temporales: 4 | Agregacion: 8
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-001 | ¿Qué es un Gobierno Regional (GORE)? |
| Existencial | CQ-002 | ¿Qué es una División dentro del GORE? |
| Relacional | CQ-009 | ¿Qué divisiones componen el GORE Ñuble? |
| Relacional | CQ-010 | ¿Qué departamentos pertenecen a la DIPIR? |
| Temporal | CQ-017 | ¿Cuándo fue creado el GORE Ñuble? |
| Temporal | CQ-018 | ¿Cuál es el período de mandato del Gobernador Regional? |
| Agregación | CQ-021 | ¿Cuántas divisiones tiene el GORE Ñuble? |
| Agregación | CQ-022 | ¿Cuántos departamentos tiene la DIPIR? |

## 02 IPR
- Existenciales: 10 | Relacionales: 10 | Temporales: 5 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-029 | ¿Qué es una IPR (Intervención Pública Regional)? |
| Existencial | CQ-030 | ¿Qué es un IDI (Iniciativa de Inversión)? |
| Relacional | CQ-039 | ¿Qué relación existe entre IPR y mecanismo de financiamiento? |
| Relacional | CQ-040 | ¿Qué entidad formula una IPR? |
| Temporal | CQ-049 | ¿Cuáles son las etapas del ciclo de vida de una IPR? |
| Temporal | CQ-050 | ¿Cuál es la secuencia de fases de una IDI (Prefactibilidad, Factibilidad, Diseño, Ejecución)? |
| Agregación | CQ-054 | ¿Cuántas IPR están en cartera del GORE Ñuble? |
| Agregación | CQ-055 | ¿Cuántas IPR están en estado de ejecución? |

## 03 Financiamiento
- Existenciales: 10 | Relacionales: 7 | Temporales: 4 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-061 | ¿Qué es el FNDR (Fondo Nacional de Desarrollo Regional)? |
| Existencial | CQ-062 | ¿Qué es el FRIL (Fondo Regional de Iniciativa Local)? |
| Relacional | CQ-071 | ¿Qué relación existe entre tipo de IPR y mecanismo de financiamiento aplicable? |
| Relacional | CQ-072 | ¿Qué relación tiene el FNDR con la Ley de Presupuestos? |
| Temporal | CQ-078 | ¿Cuál es el calendario presupuestario anual del FNDR? |
| Temporal | CQ-079 | ¿Cuándo se realizan los llamados FRIL en el año? |
| Agregación | CQ-082 | ¿Cuál es el presupuesto total FNDR de Ñuble para el año vigente? |
| Agregación | CQ-083 | ¿Cuál es el monto disponible para FRIL en el año vigente? |

## 04 Evaluacion
- Existenciales: 12 | Relacionales: 7 | Temporales: 5 | Agregacion: 6
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-089 | ¿Qué es el SNI (Sistema Nacional de Inversiones)? |
| Existencial | CQ-090 | ¿Qué es el BIP (Banco Integrado de Proyectos)? |
| Relacional | CQ-101 | ¿Qué organismo realiza la evaluación SNI (MDSF)? |
| Relacional | CQ-102 | ¿Qué organismo realiza la evaluación de programas (DIPRES/SES)? |
| Temporal | CQ-108 | ¿Cuál es el plazo de MDSF para evaluación de admisibilidad? |
| Temporal | CQ-109 | ¿Cuál es el plazo de MDSF para análisis técnico-económico? |
| Agregación | CQ-113 | ¿Cuántos tracks de evaluación existen según tipo de IPR? |
| Agregación | CQ-114 | ¿Cuántos niveles de proporcionalidad define MDSF? |

## 05 Aprobacion
- Existenciales: 6 | Relacionales: 6 | Temporales: 3 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-119 | ¿Qué es el proceso de priorización de IPR? |
| Existencial | CQ-120 | ¿Qué es un Acuerdo CORE? |
| Relacional | CQ-125 | ¿Qué instancia aprueba IPR >7.000 UTM? |
| Relacional | CQ-126 | ¿Qué instancia aprueba IPR ≤7.000 UTM? |
| Temporal | CQ-131 | ¿Cuándo sesiona el CORE para aprobar IPR? |
| Temporal | CQ-132 | ¿Cuál es el plazo de CGR para Toma de Razón? |
| Agregación | CQ-134 | ¿Cuántas IPR fueron aprobadas por el CORE en el año vigente? |
| Agregación | CQ-135 | ¿Cuál es el monto total aprobado por el CORE? |

## 06 Convenios
- Existenciales: 5 | Relacionales: 5 | Temporales: 3 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-141 | ¿Qué es un Convenio de Transferencia? |
| Existencial | CQ-142 | ¿Qué es un Convenio Mandato? |
| Relacional | CQ-146 | ¿Qué entidades pueden ser receptoras de transferencias? |
| Relacional | CQ-147 | ¿Qué relación existe entre tipo de convenio y tipo de entidad receptora? |
| Temporal | CQ-151 | ¿Cuál es el plazo para firma del convenio tras aprobación? |
| Temporal | CQ-152 | ¿Cuál es el plazo para primera transferencia tras firma? |
| Agregación | CQ-154 | ¿Cuántos convenios vigentes tiene el GORE? |
| Agregación | CQ-155 | ¿Cuál es el monto total transferido en el año? |

## 07 Ejecucion
- Existenciales: 6 | Relacionales: 5 | Temporales: 4 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-161 | ¿Qué es el seguimiento de una IPR? |
| Existencial | CQ-162 | ¿Qué es un informe de avance? |
| Relacional | CQ-167 | ¿Qué unidad GORE realiza el seguimiento de IPR? |
| Relacional | CQ-168 | ¿Qué relación existe entre ejecutor e informes de avance? |
| Temporal | CQ-172 | ¿Con qué periodicidad se entregan informes de avance? |
| Temporal | CQ-173 | ¿Cuál es el plazo máximo de ejecución de un proyecto FRIL? |
| Agregación | CQ-176 | ¿Cuántas IPR están en ejecución actualmente? |
| Agregación | CQ-177 | ¿Cuál es el porcentaje promedio de avance físico de IPR en ejecución? |

## 08 Rendicion
- Existenciales: 5 | Relacionales: 4 | Temporales: 3 | Agregacion: 6
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-183 | ¿Qué es el SISREC (Sistema de Rendición Electrónica de Cuentas)? |
| Existencial | CQ-184 | ¿Qué es una rendición de cuentas? |
| Relacional | CQ-188 | ¿Qué entidades deben rendir cuentas al GORE? |
| Relacional | CQ-189 | ¿Qué unidad GORE revisa las rendiciones? |
| Temporal | CQ-192 | ¿Cuál es el plazo para rendir cuentas tras término de ejecución? |
| Temporal | CQ-193 | ¿Cuál es el plazo para subsanar reparos de rendición? |
| Agregación | CQ-195 | ¿Cuántas rendiciones pendientes existen con el GORE? |
| Agregación | CQ-196 | ¿Cuál es el monto total de rendiciones pendientes? |

## 09 Normativo
- Existenciales: 8 | Relacionales: 8 | Temporales: 3 | Agregacion: 6
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-201 | ¿Qué es la LOC GORE (Ley 19.175)? |
| Existencial | CQ-202 | ¿Qué es la Ley de Presupuestos (21.796)? |
| Relacional | CQ-209 | ¿Qué leyes regulan las atribuciones del GORE? |
| Relacional | CQ-210 | ¿Qué normas regulan la evaluación de proyectos SNI? |
| Temporal | CQ-217 | ¿Cuál es la vigencia de la Ley de Presupuestos? |
| Temporal | CQ-218 | ¿Cuándo fue promulgada la LOC GORE? |
| Agregación | CQ-220 | ¿Cuántas leyes principales regulan el funcionamiento del GORE? |
| Agregación | CQ-221 | ¿Cuántas resoluciones CGR aplican a transferencias? |

## 10 TDE
- Existenciales: 8 | Relacionales: 6 | Temporales: 3 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-226 | ¿Qué es la TDE (Transformación Digital del Estado)? |
| Existencial | CQ-227 | ¿Qué es la Ley de TDE (21.180)? |
| Relacional | CQ-234 | ¿Qué relación tiene TDE con los procedimientos administrativos? |
| Relacional | CQ-235 | ¿Qué organismos están obligados a implementar TDE? |
| Temporal | CQ-240 | ¿Cuándo entró en vigencia la Ley TDE para GORE? |
| Temporal | CQ-241 | ¿Cuáles son las etapas de implementación de TDE en GORE? |
| Agregación | CQ-243 | ¿Cuántos trámites GORE están digitalizados? |
| Agregación | CQ-244 | ¿Cuántos usuarios utilizan GESDOC en el GORE? |

## 11 Gestion Operacional IPR
- Existenciales: 10 | Relacionales: 8 | Temporales: 5 | Agregacion: 3
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-250 | ¿Qué es una IPR según la guía operacional? |
| Existencial | CQ-251 | ¿Qué es un IDI (Iniciativa de Inversión) en contexto GORE? |
| Relacional | CQ-260 | ¿Quién preside el Comité Directivo Regional (CDR)? |
| Relacional | CQ-261 | ¿Qué relación existe entre la DIPIR y el proceso de evaluación técnica? |
| Temporal | CQ-268 | ¿Cuál es el plazo orientativo de MDSF para evaluación de admisibilidad (Track A)? |
| Temporal | CQ-269 | ¿Cuál es el plazo orientativo para el Análisis Técnico-Económico de MDSF? |
| Agregación | CQ-273 | ¿Cuántas fases tiene el proceso end-to-end de gestión de IPR? |
| Agregación | CQ-274 | ¿Cuántos tracks de evaluación técnica existen según el tipo de IPR? |

## 12 Selector Vias Financiamiento
- Existenciales: 10 | Relacionales: 6 | Temporales: 3 | Agregacion: 3
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-276 | ¿Qué es el FNDR según el selector? |
| Existencial | CQ-277 | ¿Qué es el FRPD según el selector? |
| Relacional | CQ-286 | ¿Qué relación existe entre tipo de IPR (Proyecto vs Programa) y vía de financiamiento? |
| Relacional | CQ-287 | ¿Qué mecanismo aplica cuando el ejecutor es una Municipalidad para proyectos <5.000 UTM? |
| Temporal | CQ-292 | ¿Cuál es el período de vigencia de un RS FRIL? |
| Temporal | CQ-293 | ¿Cuántos días tiene el municipio desde la firma del convenio FRIL para licitar? |
| Agregación | CQ-295 | ¿Cuántos mecanismos de financiamiento principales existen para IPR Proyecto? |
| Agregación | CQ-296 | ¿Cuántas categorías de instituciones están habilitadas para postular al FRPD? |

## 13 Guia IDI SNI
- Existenciales: 12 | Relacionales: 7 | Temporales: 3 | Agregacion: 3
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-298 | ¿Qué es el Principio de Proporcionalidad en el SNI? |
| Existencial | CQ-299 | ¿Qué es la Situación Base Optimizada? |
| Relacional | CQ-310 | ¿Qué relación existe entre nivel de proporcionalidad (0-3) y profundidad del análisis SNI? |
| Relacional | CQ-311 | ¿Qué actores institucionales participan en el ciclo SNI (MDSF, DIPRES, GORE)? |
| Temporal | CQ-317 | ¿Cuáles son las etapas de preinversión de una IDI? |
| Temporal | CQ-318 | ¿Cuáles son las fases principales del ciclo de vida de una IDI? |
| Agregación | CQ-320 | ¿Cuántos niveles de profundidad de evaluación define el MDSF? |
| Agregación | CQ-321 | ¿Cuántos tipos de IDI existen según clasificación presupuestaria Subtítulo 31? |

## 14 PPR Ejecucion Directa
- Existenciales: 9 | Relacionales: 6 | Temporales: 3 | Agregacion: 3
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-323 | ¿Qué es un PPR de Ejecución Directa GORE? |
| Existencial | CQ-324 | ¿Qué es el Formulario de Perfil de un PPR? |
| Relacional | CQ-332 | ¿Qué relación tiene DIPRES/SES con la evaluación ex ante de PPR? |
| Relacional | CQ-333 | ¿Cómo se vincula el problema central con los componentes del programa? |
| Temporal | CQ-338 | ¿Cuáles son las fases del ciclo de vida de un PPR? |
| Temporal | CQ-339 | ¿Cuál es el plazo para enviar el Diseño tras notificación de DIPRES/SES? |
| Agregación | CQ-341 | ¿Cuántas fases tiene el proceso bifásico de evaluación ex ante (Perfil + Diseño)? |
| Agregación | CQ-342 | ¿Cuántos principios rectores de formulación se definen para PPR? |

## 15 FRIL
- Existenciales: 8 | Relacionales: 6 | Temporales: 5 | Agregacion: 6
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-344 | ¿Qué es el FRIL (Fondo Regional de Iniciativa Local)? |
| Existencial | CQ-345 | ¿Qué es un BNUP (Bien Nacional de Uso Público)? |
| Relacional | CQ-352 | ¿Qué relación existe entre monto máximo FRIL y el tope regional de Ñuble (4.545 UTM)? |
| Relacional | CQ-353 | ¿Qué servicio emite el certificado de pertinencia técnica para proyectos deportivos formativos? |
| Temporal | CQ-358 | ¿Cuál es el plazo máximo del GORE para emitir el primer RATE FRIL? |
| Temporal | CQ-359 | ¿Cuál es el plazo para subsanar observaciones FI/OT en FRIL? |
| Agregación | CQ-363 | ¿Cuál es el monto máximo por proyecto FRIL en la Región de Ñuble? |
| Agregación | CQ-364 | ¿Cuál es el monto mínimo por proyecto FRIL? |

## 16 FRPD
- Existenciales: 7 | Relacionales: 6 | Temporales: 3 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-369 | ¿Qué es el FRPD (Fondo Regional para la Productividad y el Desarrollo)? |
| Existencial | CQ-370 | ¿Qué es la exención de evaluación ex ante para iniciativas CTCI? |
| Relacional | CQ-376 | ¿Qué instituciones están habilitadas para postular al FRPD según SUBCTCI? |
| Relacional | CQ-377 | ¿Qué relación tiene el FRPD con la Ley de Royalty Minero (21.591)? |
| Temporal | CQ-382 | ¿Cuál es el plazo máximo de ejecución de una iniciativa FRPD? |
| Temporal | CQ-383 | ¿Cuál es el plazo para formular consultas tras publicación del concurso FRPD? |
| Agregación | CQ-385 | ¿Cuántos sectores prioritarios define el concurso FRPD 2025? |
| Agregación | CQ-386 | ¿Cuántos focos prioritarios contempla el concurso FRPD? |

## 17 Transferencia PPR
- Existenciales: 6 | Relacionales: 5 | Temporales: 2 | Agregacion: 3
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-392 | ¿Qué es un PPR Transferible a entidad pública? |
| Existencial | CQ-393 | ¿Qué es el ITF (Informe Técnico Favorable) interno del GORE? |
| Relacional | CQ-398 | ¿Qué relación tiene la Glosa 06 letra c con la exención de evaluación ex ante? |
| Relacional | CQ-399 | ¿Qué proceso reemplaza la evaluación Circular 22 para PPR transferidos? |
| Temporal | CQ-403 | ¿Cuál es la fecha límite para postular PPR a financiamiento 2026? |
| Temporal | CQ-404 | ¿Qué ocurre con propuestas ingresadas post-fecha límite si son recomendadas favorablemente? |
| Agregación | CQ-405 | ¿Cuál es el porcentaje máximo de la transferencia para contratación de personal a honorarios? |
| Agregación | CQ-406 | ¿Cuál es el porcentaje máximo para gastos de administración del GORE? |

## 18 Concurso 8 Porciento
- Existenciales: 11 | Relacionales: 6 | Temporales: 3 | Agregacion: 7
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-408 | ¿Qué es el Concurso Vinculación con la Comunidad 8%? |
| Existencial | CQ-409 | ¿Qué son las subvenciones FNDR 8%? |
| Relacional | CQ-419 | ¿Qué relación existe entre antigüedad de la organización (2 años) y elegibilidad? |
| Relacional | CQ-420 | ¿Qué restricción de postulación múltiple aplica a organizaciones privadas sin fines de lucro? |
| Temporal | CQ-425 | ¿Cuál es el plazo general de ejecución de iniciativas 8%? |
| Temporal | CQ-426 | ¿Con cuánta anticipación debe coordinarse la invitación a actos de inicio/cierre? |
| Agregación | CQ-428 | ¿Cuál es el monto total disponible para instituciones privadas en el Concurso 8% 2025? |
| Agregación | CQ-429 | ¿Cuál es el monto asignado al Fondo de Seguridad Ciudadana (privados)? |

## 19 Circular 33
- Existenciales: 10 | Relacionales: 7 | Temporales: 3 | Agregacion: 6
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-435 | ¿Qué es el Oficio Circular 33 del Ministerio de Hacienda? |
| Existencial | CQ-436 | ¿Qué son los Estudios Propios del Giro bajo C33? |
| Relacional | CQ-445 | ¿Qué relación existe entre subtítulo 22 y estudios propios del giro? |
| Relacional | CQ-446 | ¿Qué relación tiene el subtítulo 29 con la adquisición de ANF? |
| Temporal | CQ-452 | ¿Cuál es la antigüedad máxima permitida para el Certificado de Dominio Vigente? |
| Temporal | CQ-453 | ¿Cuál es la antigüedad máxima para el Certificado de Avalúo Fiscal? |
| Agregación | CQ-455 | ¿Cuál es el porcentaje mínimo de aporte propio para ANF (financiamiento compartido)? |
| Agregación | CQ-456 | ¿Cuál es el porcentaje máximo del proyecto que puede destinarse a equipamiento (conservación)? |

## 20 Umbrales Transversal
- Existenciales: 3 | Relacionales: 3 | Temporales: 1 | Agregacion: 5
| Tipo | ID | Pregunta |
| --- | --- | --- |
| Existencial | CQ-461 | ¿Qué es el umbral de 5.000 UTM para exención de RS? |
| Existencial | CQ-462 | ¿Qué es el umbral de 7.000 UTM para aprobación obligatoria CORE? |
| Relacional | CQ-464 | ¿Qué relación existe entre monto del proyecto y requisito de Toma de Razón CGR? |
| Relacional | CQ-465 | ¿Qué relación tiene el umbral de 5.000 UTM con FRIL y proyectos municipales? |
| Temporal | CQ-472 | ¿Cuál es la fecha de actualización del valor UTM usado como referencia para umbrales? |
| Agregación | CQ-467 | ¿Cuál es el tope de 5% para gastos de administración en Glosa 06? |
| Agregación | CQ-468 | ¿Cuál es el tope de 5% para contratación de personal a honorarios en transferencias? |

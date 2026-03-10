---
_manifest:
  urn: urn:gn:kb:gn-cqs-master-p03
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: ontologies/onto_gorenuble/goreNubleCQs_Master.yml
version: 2.0.0
status: draft
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
    cr: 1.36
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Preguntas de competencia maestras del bundle ontologico GN.
    dependencies: []
    expected_sections:
    - Contenido
    document_family: cq_catalog
    publication_class: knowledge
    skeleton_count: 21
    meat_count: 1024
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gn-cqs-master.md.json
  kora:
    shard_index: 3
    shard_count: 4
    shard_root_urn: urn:gn:kb:gn-cqs-master
---

# Catálogo Maestro de Preguntas de Competencia - Parte 03

## 12 Selector Vias Financiamiento

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-276 | ¿Qué es el FNDR según el selector? |
| CQ-277 | ¿Qué es el FRPD según el selector? |
| CQ-278 | ¿Qué es el SNI según el selector? |
| CQ-279 | ¿Qué diferencia hay entre Subtítulo 24, 31 y 33? |
| CQ-280 | ¿Qué es un RATE AD (Admisibilidad)? |
| CQ-281 | ¿Qué es un RATE RF (Recomendación Favorable)? |
| CQ-282 | ¿Qué es la Glosa 06 y qué financia? |
| CQ-283 | ¿Qué es la Glosa 07 (8% FNDR)? |
| CQ-284 | ¿Qué es la Glosa 12 (FRIL)? |
| CQ-285 | ¿Qué es la Glosa 13 (FRPD)? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-286 | ¿Qué relación existe entre tipo de IPR (Proyecto vs Programa) y vía de financiamiento? |
| CQ-287 | ¿Qué mecanismo aplica cuando el ejecutor es una Municipalidad para proyectos <5.000 UTM? |
| CQ-288 | ¿Qué evaluador corresponde para programas de ejecución directa GORE (Glosa 06)? |
| CQ-289 | ¿Qué relación tiene el SNI con proyectos FRPD tipo CTCI vs Fomento General? |
| CQ-290 | ¿Qué restricción de probidad vincula a los postulantes FRPD con autoridades GORE? |
| CQ-291 | ¿Qué dependencia normativa tiene FRIL respecto de SUBDERE? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-292 | ¿Cuál es el período de vigencia de un RS FRIL? |
| CQ-293 | ¿Cuántos días tiene el municipio desde la firma del convenio FRIL para licitar? |
| CQ-294 | ¿Cuál es el plazo de ejecución máximo permitido para iniciativas FRPD? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-295 | ¿Cuántos mecanismos de financiamiento principales existen para IPR Proyecto? |
| CQ-296 | ¿Cuántas categorías de instituciones están habilitadas para postular al FRPD? |
| CQ-297 | ¿Cuántos fondos temáticos componen el Concurso 8%? |

## 13 Guia IDI SNI

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-298 | ¿Qué es el Principio de Proporcionalidad en el SNI? |
| CQ-299 | ¿Qué es la Situación Base Optimizada? |
| CQ-300 | ¿Qué es el VAN social? |
| CQ-301 | ¿Qué es el CAE (Costo Anual Equivalente)? |
| CQ-302 | ¿Qué es un RIS (Requisito de Información Sectorial)? |
| CQ-303 | ¿Qué tipos de problemas reconoce el SNI (Cobertura vs Calidad)? |
| CQ-304 | ¿Qué es el Análisis de Separabilidad de componentes? |
| CQ-305 | ¿Qué son los precios sociales y quién los publica? |
| CQ-306 | ¿Qué es el horizonte de evaluación de un proyecto? |
| CQ-307 | ¿Qué es el valor residual de un proyecto? |
| CQ-308 | ¿Qué es el BIPS (Banco Integrado de Programas Sociales)? |
| CQ-309 | ¿Qué es la Metodología de Marco Lógico (MML)? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-310 | ¿Qué relación existe entre nivel de proporcionalidad (0-3) y profundidad del análisis SNI? |
| CQ-311 | ¿Qué actores institucionales participan en el ciclo SNI (MDSF, DIPRES, GORE)? |
| CQ-312 | ¿Qué relación tiene la Situación Sin Proyecto con la Situación Con Proyecto? |
| CQ-313 | ¿Cómo se vincula el VAN social con la decisión de inversión pública? |
| CQ-314 | ¿Qué metodología se usa para comparar alternativas con distinta vida útil? |
| CQ-315 | ¿Qué subsistemas componen el SNI? |
| CQ-316 | ¿Qué relación existe entre Análisis Costo-Beneficio (ACB) y Análisis Costo-Eficiencia (ACE)? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-317 | ¿Cuáles son las etapas de preinversión de una IDI? |
| CQ-318 | ¿Cuáles son las fases principales del ciclo de vida de una IDI? |
| CQ-319 | ¿En qué momento del ciclo se realiza la evaluación ex post? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-320 | ¿Cuántos niveles de profundidad de evaluación define el MDSF? |
| CQ-321 | ¿Cuántos tipos de IDI existen según clasificación presupuestaria Subtítulo 31? |
| CQ-322 | ¿Cuántos subsistemas tiene el SNI? |

## 14 PPR Ejecucion Directa

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-323 | ¿Qué es un PPR de Ejecución Directa GORE? |
| CQ-324 | ¿Qué es el Formulario de Perfil de un PPR? |
| CQ-325 | ¿Qué es el Formulario de Diseño de un PPR? |
| CQ-326 | ¿Qué significa la calificación RF en evaluación de programas? |
| CQ-327 | ¿Qué significa la calificación OT (Objetado Técnicamente)? |
| CQ-328 | ¿Qué es la población potencial vs población objetivo vs beneficiarios anuales? |
| CQ-329 | ¿Qué es el propósito de un programa según MML? |
| CQ-330 | ¿Qué es un componente de programa? |
| CQ-331 | ¿Qué es un indicador SMART? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-332 | ¿Qué relación tiene DIPRES/SES con la evaluación ex ante de PPR? |
| CQ-333 | ¿Cómo se vincula el problema central con los componentes del programa? |
| CQ-334 | ¿Qué relación existe entre árbol de problemas y árbol de objetivos? |
| CQ-335 | ¿Qué vinculación debe tener un PPR con la ERD? |
| CQ-336 | ¿Qué rol cumple la División GORE patrocinante en un PPR? |
| CQ-337 | ¿Cómo se relacionan los indicadores SMART con el monitoreo del programa? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-338 | ¿Cuáles son las fases del ciclo de vida de un PPR? |
| CQ-339 | ¿Cuál es el plazo para enviar el Diseño tras notificación de DIPRES/SES? |
| CQ-340 | ¿Cuál es el plazo para corregir y reenviar tras retroalimentación? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-341 | ¿Cuántas fases tiene el proceso bifásico de evaluación ex ante (Perfil + Diseño)? |
| CQ-342 | ¿Cuántos principios rectores de formulación se definen para PPR? |
| CQ-343 | ¿Cuántas dimensiones de indicadores de desempeño existen? |

## 15 FRIL

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-344 | ¿Qué es el FRIL (Fondo Regional de Iniciativa Local)? |
| CQ-345 | ¿Qué es un BNUP (Bien Nacional de Uso Público)? |
| CQ-346 | ¿Qué es un ITO (Inspector Técnico de Obra)? |
| CQ-347 | ¿Qué categorías de proyectos FRIL existen? |
| CQ-348 | ¿Qué subcategorías incluye el grupo Desarrollo Territorial? |
| CQ-349 | ¿Qué subcategorías incluye el grupo Medio Ambiente? |
| CQ-350 | ¿Qué significa el estado NV (No Vigente) en FRIL? |
| CQ-351 | ¿Qué significa el estado IN (Incumplimiento de Normativa)? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-352 | ¿Qué relación existe entre monto máximo FRIL y el tope regional de Ñuble (4.545 UTM)? |
| CQ-353 | ¿Qué servicio emite el certificado de pertinencia técnica para proyectos deportivos formativos? |
| CQ-354 | ¿Qué servicio emite el certificado de pertinencia para infraestructura de salud? |
| CQ-355 | ¿Qué relación tiene SUBDERE con la visación de metodología FRIL? |
| CQ-356 | ¿Qué vinculación debe declarar el proyecto FRIL con la ERD y el PLADECO? |
| CQ-357 | ¿Qué restricciones de terreno aplican para proyectos en predios privados bajo Ley Indígena? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-358 | ¿Cuál es el plazo máximo del GORE para emitir el primer RATE FRIL? |
| CQ-359 | ¿Cuál es el plazo para subsanar observaciones FI/OT en FRIL? |
| CQ-360 | ¿Cuántos días tiene el municipio para presentar licitación tras firma del convenio? |
| CQ-361 | ¿Cuándo se desarrolla el 1er Llamado FRIL 2025? |
| CQ-362 | ¿Cuándo se desarrolla el 2do Llamado FRIL 2025? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-363 | ¿Cuál es el monto máximo por proyecto FRIL en la Región de Ñuble? |
| CQ-364 | ¿Cuál es el monto mínimo por proyecto FRIL? |
| CQ-365 | ¿Cuántas iniciativas puede postular cada comuna en período regular? |
| CQ-366 | ¿Cuál es el monto total máximo a postular por comuna en período regular? |
| CQ-367 | ¿Cuántas comunas componen la Región de Ñuble? |
| CQ-368 | ¿Cuántos grupos de categorías FRIL existen? |

## 16 FRPD

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-369 | ¿Qué es el FRPD (Fondo Regional para la Productividad y el Desarrollo)? |
| CQ-370 | ¿Qué es la exención de evaluación ex ante para iniciativas CTCI? |
| CQ-371 | ¿Qué significa Caso 1 – Innovación, CTCI en bifurcación post-selección? |
| CQ-372 | ¿Qué significa Caso 2 – Fomento Productivo General? |
| CQ-373 | ¿Qué es la Resolución Exenta N°33 de SUBCTCI? |
| CQ-374 | ¿Qué tipos de investigación reconoce el FRPD (básica, aplicada, desarrollo experimental)? |
| CQ-375 | ¿Qué tipos de innovación financia el FRPD? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-376 | ¿Qué instituciones están habilitadas para postular al FRPD según SUBCTCI? |
| CQ-377 | ¿Qué relación tiene el FRPD con la Ley de Royalty Minero (21.591)? |
| CQ-378 | ¿Qué vinculación estratégica debe tener una iniciativa FRPD con ERD y ER-CTCI? |
| CQ-379 | ¿Qué organismos componen la Comisión Evaluadora FRPD? |
| CQ-380 | ¿Qué prohibiciones de parentesco aplican a postulantes FRPD respecto del Gobernador y CORE? |
| CQ-381 | ¿Qué relación tiene CORFO/ANID con transferencias directas FRPD? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-382 | ¿Cuál es el plazo máximo de ejecución de una iniciativa FRPD? |
| CQ-383 | ¿Cuál es el plazo para formular consultas tras publicación del concurso FRPD? |
| CQ-384 | ¿Cuál es el plazo máximo de respuesta a consultas FRPD? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-385 | ¿Cuántos sectores prioritarios define el concurso FRPD 2025? |
| CQ-386 | ¿Cuántos focos prioritarios contempla el concurso FRPD? |
| CQ-387 | ¿Cuál es el quórum mínimo de la Comisión Evaluadora FRPD? |
| CQ-388 | ¿Cuál es el puntaje mínimo de elegibilidad en admisibilidad técnica FRPD? |
| CQ-389 | ¿Cuál es el porcentaje máximo del monto total que puede destinarse a remuneraciones FRPD? |
| CQ-390 | ¿Cuántas iniciativas puede postular cada institución al FRPD? |
| CQ-391 | ¿Cuál es el límite de gastos administrativos sobre el total postulado FRPD? |

## 17 Transferencia PPR

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-392 | ¿Qué es un PPR Transferible a entidad pública? |
| CQ-393 | ¿Qué es el ITF (Informe Técnico Favorable) interno del GORE? |
| CQ-394 | ¿Qué diferencia hay entre ITF y RATE RS? |
| CQ-395 | ¿Qué es el Formulario de Diseño de Programa Público (PPR) para transferencias? |
| CQ-396 | ¿Qué entidades pueden ser receptoras de transferencias PPR? |
| CQ-397 | ¿Qué significa la exención de evaluación central (DIPRES/SES) para transferencias a entidades públicas? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-398 | ¿Qué relación tiene la Glosa 06 letra c con la exención de evaluación ex ante? |
| CQ-399 | ¿Qué proceso reemplaza la evaluación Circular 22 para PPR transferidos? |
| CQ-400 | ¿Qué división GORE debe emitir el Certificado de Pertinencia y Patrocinio? |
| CQ-401 | ¿Qué relación existe entre DAE y la evaluación técnica de diseño de PPR transferidos? |
| CQ-402 | ¿Qué vinculación debe existir entre el objeto social de la entidad postulante y el programa? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-403 | ¿Cuál es la fecha límite para postular PPR a financiamiento 2026? |
| CQ-404 | ¿Qué ocurre con propuestas ingresadas post-fecha límite si son recomendadas favorablemente? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-405 | ¿Cuál es el porcentaje máximo de la transferencia para contratación de personal a honorarios? |
| CQ-406 | ¿Cuál es el porcentaje máximo para gastos de administración del GORE? |
| CQ-407 | ¿Cuántos documentos mínimos se requieren para postular un PPR transferible? |

---
_manifest:
  urn: urn:gn:kb:gn-cqs-master
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
    shard_index: 1
    shard_count: 4
    shard_root_urn: urn:gn:kb:gn-cqs-master
---

# Catálogo Maestro de Preguntas de Competencia


## Resumen
Preguntas de competencia maestras del bundle ontologico GN.

### Estadísticas
- Total de CQs: 472
- Dominios: 20
- Existenciales: 164
- Relacionales: 126
- Temporales: 68
- Agregacion: 114

## 01 Estructura Organizacional

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-001 | ¿Qué es un Gobierno Regional (GORE)? |
| CQ-002 | ¿Qué es una División dentro del GORE? |
| CQ-003 | ¿Qué es un Departamento dentro de una División? |
| CQ-004 | ¿Qué es la DIPIR (División de Presupuesto e Inversión Regional)? |
| CQ-005 | ¿Qué es el DAE (Departamento de Análisis y Evaluación)? |
| CQ-006 | ¿Qué es el CORE (Consejo Regional)? |
| CQ-007 | ¿Qué es el CDR (Comité Directivo Regional)? |
| CQ-008 | ¿Qué es una Unidad Formuladora? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-009 | ¿Qué divisiones componen el GORE Ñuble? |
| CQ-010 | ¿Qué departamentos pertenecen a la DIPIR? |
| CQ-011 | ¿Quién preside el CDR? |
| CQ-012 | ¿Qué divisiones participan en el CDR? |
| CQ-013 | ¿Qué relación jerárquica existe entre División y Departamento? |
| CQ-014 | ¿Qué unidades dependen del Gobernador Regional? |
| CQ-015 | ¿Qué relación tiene el CORE con la aprobación de iniciativas? |
| CQ-016 | ¿Qué unidad es responsable de la evaluación técnica de proyectos? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-017 | ¿Cuándo fue creado el GORE Ñuble? |
| CQ-018 | ¿Cuál es el período de mandato del Gobernador Regional? |
| CQ-019 | ¿Cuál es el período de mandato de los Consejeros Regionales? |
| CQ-020 | ¿Con qué periodicidad sesiona el CORE? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-021 | ¿Cuántas divisiones tiene el GORE Ñuble? |
| CQ-022 | ¿Cuántos departamentos tiene la DIPIR? |
| CQ-023 | ¿Cuántos consejeros regionales tiene el CORE de Ñuble? |
| CQ-024 | ¿Cuántas comunas componen la Región de Ñuble? |
| CQ-025 | ¿Cuántas provincias tiene la Región de Ñuble? |
| CQ-026 | ¿Cuántos funcionarios tiene el GORE Ñuble? |
| CQ-027 | ¿Cuántos miembros componen el CDR? |
| CQ-028 | ¿Cuántas unidades formuladoras están registradas en la región? |

## 02 IPR

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-029 | ¿Qué es una IPR (Intervención Pública Regional)? |
| CQ-030 | ¿Qué es un IDI (Iniciativa de Inversión)? |
| CQ-031 | ¿Qué es un PPR (Programa Público Regional)? |
| CQ-032 | ¿Qué es un Estudio Básico? |
| CQ-033 | ¿Qué es un Proyecto de Inversión? |
| CQ-034 | ¿Qué es una Ficha IDI? |
| CQ-035 | ¿Qué es el código BIP? |
| CQ-036 | ¿Qué es el Perfil de un programa? |
| CQ-037 | ¿Qué es el Diseño de un programa? |
| CQ-038 | ¿Qué tipos de IPR existen según su naturaleza? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-039 | ¿Qué relación existe entre IPR y mecanismo de financiamiento? |
| CQ-040 | ¿Qué entidad formula una IPR? |
| CQ-041 | ¿Qué entidad evalúa una IPR? |
| CQ-042 | ¿Qué entidad ejecuta una IPR? |
| CQ-043 | ¿Qué relación tiene una IPR con la ERD? |
| CQ-044 | ¿Qué relación tiene una IPR con el PLADECO comunal? |
| CQ-045 | ¿Qué división GORE patrocina una IPR? |
| CQ-046 | ¿Qué relación existe entre IDI y SNI? |
| CQ-047 | ¿Qué relación existe entre PPR y BIPS? |
| CQ-048 | ¿Qué vinculación tiene el código BIP con el ciclo de vida de la IPR? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-049 | ¿Cuáles son las etapas del ciclo de vida de una IPR? |
| CQ-050 | ¿Cuál es la secuencia de fases de una IDI (Prefactibilidad, Factibilidad, Diseño, Ejecución)? |
| CQ-051 | ¿Cuál es la secuencia de fases de un PPR (Perfil, Diseño, Ejecución)? |
| CQ-052 | ¿Cuándo se asigna el código BIP a una iniciativa? |
| CQ-053 | ¿Cuándo se realiza la evaluación ex post de una IPR? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-054 | ¿Cuántas IPR están en cartera del GORE Ñuble? |
| CQ-055 | ¿Cuántas IPR están en estado de ejecución? |
| CQ-056 | ¿Cuántas IPR fueron aprobadas en el año presupuestario vigente? |
| CQ-057 | ¿Cuál es el monto total de inversión regional en IPR? |
| CQ-058 | ¿Cuántas IPR están clasificadas como IDI vs PPR? |
| CQ-059 | ¿Cuántas IPR por comuna existen en la región? |
| CQ-060 | ¿Cuántas IPR por sector/área temática existen? |

## 03 Financiamiento

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-061 | ¿Qué es el FNDR (Fondo Nacional de Desarrollo Regional)? |
| CQ-062 | ¿Qué es el FRIL (Fondo Regional de Iniciativa Local)? |
| CQ-063 | ¿Qué es el FRPD (Fondo Regional para la Productividad y el Desarrollo)? |
| CQ-064 | ¿Qué es el Subtítulo 24 (Transferencias Corrientes)? |
| CQ-065 | ¿Qué es el Subtítulo 31 (Iniciativas de Inversión)? |
| CQ-066 | ¿Qué es el Subtítulo 33 (Transferencias de Capital)? |
| CQ-067 | ¿Qué es la Glosa 06 (Programas de Ejecución Directa)? |
| CQ-068 | ¿Qué es la Glosa 07 (Subvenciones 8%)? |
| CQ-069 | ¿Qué es la Glosa 12 (FRIL)? |
| CQ-070 | ¿Qué es la Glosa 13 (FRPD)? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-071 | ¿Qué relación existe entre tipo de IPR y mecanismo de financiamiento aplicable? |
| CQ-072 | ¿Qué relación tiene el FNDR con la Ley de Presupuestos? |
| CQ-073 | ¿Qué entidades pueden acceder al FRIL? |
| CQ-074 | ¿Qué entidades pueden acceder al FRPD? |
| CQ-075 | ¿Qué relación tiene el FRPD con la Ley de Royalty Minero? |
| CQ-076 | ¿Qué glosa aplica para transferencias a municipios? |
| CQ-077 | ¿Qué glosa aplica para transferencias a privados sin fines de lucro? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-078 | ¿Cuál es el calendario presupuestario anual del FNDR? |
| CQ-079 | ¿Cuándo se realizan los llamados FRIL en el año? |
| CQ-080 | ¿Cuándo se realiza el concurso FRPD? |
| CQ-081 | ¿Cuándo se realiza el concurso 8%? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-082 | ¿Cuál es el presupuesto total FNDR de Ñuble para el año vigente? |
| CQ-083 | ¿Cuál es el monto disponible para FRIL en el año vigente? |
| CQ-084 | ¿Cuál es el monto disponible para FRPD en el año vigente? |
| CQ-085 | ¿Cuál es el monto disponible para el Concurso 8%? |
| CQ-086 | ¿Cuál es el porcentaje de ejecución presupuestaria FNDR? |
| CQ-087 | ¿Cuántos mecanismos de financiamiento administra el GORE? |
| CQ-088 | ¿Cuántas glosas presupuestarias aplican al GORE Ñuble? |

## 04 Evaluacion

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-089 | ¿Qué es el SNI (Sistema Nacional de Inversiones)? |
| CQ-090 | ¿Qué es el BIP (Banco Integrado de Proyectos)? |
| CQ-091 | ¿Qué es un RATE (Resultado de Análisis Técnico-Económico)? |
| CQ-092 | ¿Qué significa RS (Recomendado Satisfactoriamente)? |
| CQ-093 | ¿Qué significa RF (Recomendación Favorable)? |
| CQ-094 | ¿Qué significa FI (Falta Información)? |
| CQ-095 | ¿Qué significa OT (Objetado Técnicamente)? |
| CQ-096 | ¿Qué significa AD (Admisible)? |
| CQ-097 | ¿Qué significa IN (Inadmisible)? |
| CQ-098 | ¿Qué es la evaluación de Admisibilidad? |
| CQ-099 | ¿Qué es la evaluación de Pertinencia? |
| CQ-100 | ¿Qué es la evaluación Técnico-Económica? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-101 | ¿Qué organismo realiza la evaluación SNI (MDSF)? |
| CQ-102 | ¿Qué organismo realiza la evaluación de programas (DIPRES/SES)? |
| CQ-103 | ¿Qué unidad GORE realiza la evaluación FRIL? |
| CQ-104 | ¿Qué relación existe entre RATE y estado de la IPR? |
| CQ-105 | ¿Qué metodología de evaluación aplica según tipo de proyecto? |
| CQ-106 | ¿Qué relación existe entre nivel de proporcionalidad y profundidad de análisis? |
| CQ-107 | ¿Qué track de evaluación aplica según tipo de IPR? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-108 | ¿Cuál es el plazo de MDSF para evaluación de admisibilidad? |
| CQ-109 | ¿Cuál es el plazo de MDSF para análisis técnico-económico? |
| CQ-110 | ¿Cuál es el plazo para subsanar observaciones FI/OT? |
| CQ-111 | ¿Cuál es el plazo del GORE para emitir RATE FRIL? |
| CQ-112 | ¿Cuál es la vigencia de un RS? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-113 | ¿Cuántos tracks de evaluación existen según tipo de IPR? |
| CQ-114 | ¿Cuántos niveles de proporcionalidad define MDSF? |
| CQ-115 | ¿Cuántas metodologías sectoriales de evaluación existen? |
| CQ-116 | ¿Cuántos estados RATE posibles existen? |
| CQ-117 | ¿Cuántas IPR fueron evaluadas con RS en el año vigente? |
| CQ-118 | ¿Cuál es la tasa de aprobación (RS) de IPR evaluadas? |

## 05 Aprobacion

### Existenciales
| ID | Pregunta |
| --- | --- |
| CQ-119 | ¿Qué es el proceso de priorización de IPR? |
| CQ-120 | ¿Qué es un Acuerdo CORE? |
| CQ-121 | ¿Qué es una Resolución Exenta? |
| CQ-122 | ¿Qué es el CDP (Certificado de Disponibilidad Presupuestaria)? |
| CQ-123 | ¿Qué es el umbral de 7.000 UTM? |
| CQ-124 | ¿Qué es la Toma de Razón de CGR? |

### Relacionales
| ID | Pregunta |
| --- | --- |
| CQ-125 | ¿Qué instancia aprueba IPR >7.000 UTM? |
| CQ-126 | ¿Qué instancia aprueba IPR ≤7.000 UTM? |
| CQ-127 | ¿Qué unidad emite el CDP? |
| CQ-128 | ¿Qué relación existe entre aprobación CORE y Resolución Exenta? |
| CQ-129 | ¿Qué IPR requieren Toma de Razón de CGR? |
| CQ-130 | ¿Qué criterios de priorización aplica el CDR? |

### Temporales
| ID | Pregunta |
| --- | --- |
| CQ-131 | ¿Cuándo sesiona el CORE para aprobar IPR? |
| CQ-132 | ¿Cuál es el plazo de CGR para Toma de Razón? |
| CQ-133 | ¿Cuál es el plazo entre aprobación CORE y emisión de Resolución? |

### Agregacion
| ID | Pregunta |
| --- | --- |
| CQ-134 | ¿Cuántas IPR fueron aprobadas por el CORE en el año vigente? |
| CQ-135 | ¿Cuál es el monto total aprobado por el CORE? |
| CQ-136 | ¿Cuántas IPR fueron aprobadas por delegación del Gobernador? |
| CQ-137 | ¿Cuántas Resoluciones Exentas fueron emitidas en el año? |
| CQ-138 | ¿Cuántas IPR requirieron Toma de Razón? |
| CQ-139 | ¿Cuál es el quórum de aprobación del CORE? |
| CQ-140 | ¿Cuántas sesiones de CORE se realizaron en el año? |

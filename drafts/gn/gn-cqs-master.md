---
_manifest:
  urn: urn:gn:kb:gn-cqs-master
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
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
    cr: 73.49
    run_id: gn-smoke
    review_gate: manual
    scope_statement: Preguntas de competencia maestras del bundle ontologico GN.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 23
    meat_count: 1038
    fat_count: 0
    preserved_facts:
    - Dom_01_Estructura_Organizacional.Agregacion[0].ID=CQ-021
    - Dom_01_Estructura_Organizacional.Agregacion[0].Q=¿Cuántas divisiones tiene el
      GORE Ñuble?
    - Dom_01_Estructura_Organizacional.Agregacion[1].ID=CQ-022
    - Dom_01_Estructura_Organizacional.Agregacion[1].Q=¿Cuántos departamentos tiene
      la DIPIR?
    - Dom_01_Estructura_Organizacional.Agregacion[2].ID=CQ-023
    - Dom_01_Estructura_Organizacional.Agregacion[2].Q=¿Cuántos consejeros regionales
      tiene el CORE de Ñuble?
    - Dom_01_Estructura_Organizacional.Agregacion[3].ID=CQ-024
    - Dom_01_Estructura_Organizacional.Agregacion[3].Q=¿Cuántas comunas componen la
      Región de Ñuble?
    - Dom_01_Estructura_Organizacional.Agregacion[4].ID=CQ-025
    - Dom_01_Estructura_Organizacional.Agregacion[4].Q=¿Cuántas provincias tiene la
      Región de Ñuble?
    - Dom_01_Estructura_Organizacional.Agregacion[5].ID=CQ-026
    - Dom_01_Estructura_Organizacional.Agregacion[5].Q=¿Cuántos funcionarios tiene
      el GORE Ñuble?
    - Dom_01_Estructura_Organizacional.Agregacion[6].ID=CQ-027
    - Dom_01_Estructura_Organizacional.Agregacion[6].Q=¿Cuántos miembros componen
      el CDR?
    - Dom_01_Estructura_Organizacional.Agregacion[7].ID=CQ-028
    - Dom_01_Estructura_Organizacional.Agregacion[7].Q=¿Cuántas unidades formuladoras
      están registradas en la región?
    - Dom_01_Estructura_Organizacional.Existenciales[0].ID=CQ-001
    - Dom_01_Estructura_Organizacional.Existenciales[0].Q=¿Qué es un Gobierno Regional
      (GORE)?
    - Dom_01_Estructura_Organizacional.Existenciales[1].ID=CQ-002
    - Dom_01_Estructura_Organizacional.Existenciales[1].Q=¿Qué es una División dentro
      del GORE?
    - Dom_01_Estructura_Organizacional.Existenciales[2].ID=CQ-003
    - Dom_01_Estructura_Organizacional.Existenciales[2].Q=¿Qué es un Departamento
      dentro de una División?
    - Dom_01_Estructura_Organizacional.Existenciales[3].ID=CQ-004
    - Dom_01_Estructura_Organizacional.Existenciales[3].Q=¿Qué es la DIPIR (División
      de Presupuesto e Inversión Regional)?
    - Dom_01_Estructura_Organizacional.Existenciales[4].ID=CQ-005
    - Dom_01_Estructura_Organizacional.Existenciales[4].Q=¿Qué es el DAE (Departamento
      de Análisis y Evaluación)?
    - Dom_01_Estructura_Organizacional.Existenciales[5].ID=CQ-006
    - Dom_01_Estructura_Organizacional.Existenciales[5].Q=¿Qué es el CORE (Consejo
      Regional)?
    - Dom_01_Estructura_Organizacional.Existenciales[6].ID=CQ-007
    - Dom_01_Estructura_Organizacional.Existenciales[6].Q=¿Qué es el CDR (Comité Directivo
      Regional)?
    - Dom_01_Estructura_Organizacional.Existenciales[7].ID=CQ-008
    - Dom_01_Estructura_Organizacional.Existenciales[7].Q=¿Qué es una Unidad Formuladora?
    - Dom_01_Estructura_Organizacional.ID=GN-CQS-DOM-01
    - Dom_01_Estructura_Organizacional.Relacionales[0].ID=CQ-009
    - Dom_01_Estructura_Organizacional.Relacionales[0].Q=¿Qué divisiones componen
      el GORE Ñuble?
    - Dom_01_Estructura_Organizacional.Relacionales[1].ID=CQ-010
    - Dom_01_Estructura_Organizacional.Relacionales[1].Q=¿Qué departamentos pertenecen
      a la DIPIR?
    - Dom_01_Estructura_Organizacional.Relacionales[2].ID=CQ-011
    - Dom_01_Estructura_Organizacional.Relacionales[2].Q=¿Quién preside el CDR?
    - Dom_01_Estructura_Organizacional.Relacionales[3].ID=CQ-012
    - Dom_01_Estructura_Organizacional.Relacionales[3].Q=¿Qué divisiones participan
      en el CDR?
    - Dom_01_Estructura_Organizacional.Relacionales[4].ID=CQ-013
    - Dom_01_Estructura_Organizacional.Relacionales[4].Q=¿Qué relación jerárquica
      existe entre División y Departamento?
    - Dom_01_Estructura_Organizacional.Relacionales[5].ID=CQ-014
    - Dom_01_Estructura_Organizacional.Relacionales[5].Q=¿Qué unidades dependen del
      Gobernador Regional?
    - Dom_01_Estructura_Organizacional.Relacionales[6].ID=CQ-015
    - Dom_01_Estructura_Organizacional.Relacionales[6].Q=¿Qué relación tiene el CORE
      con la aprobación de iniciativas?
    - Dom_01_Estructura_Organizacional.Relacionales[7].ID=CQ-016
    - Dom_01_Estructura_Organizacional.Relacionales[7].Q=¿Qué unidad es responsable
      de la evaluación técnica de proyectos?
    - Dom_01_Estructura_Organizacional.Temporales[0].ID=CQ-017
    - Dom_01_Estructura_Organizacional.Temporales[0].Q=¿Cuándo fue creado el GORE
      Ñuble?
    - Dom_01_Estructura_Organizacional.Temporales[1].ID=CQ-018
    - Dom_01_Estructura_Organizacional.Temporales[1].Q=¿Cuál es el período de mandato
      del Gobernador Regional?
    - Dom_01_Estructura_Organizacional.Temporales[2].ID=CQ-019
    - Dom_01_Estructura_Organizacional.Temporales[2].Q=¿Cuál es el período de mandato
      de los Consejeros Regionales?
    - Dom_01_Estructura_Organizacional.Temporales[3].ID=CQ-020
    - Dom_01_Estructura_Organizacional.Temporales[3].Q=¿Con qué periodicidad sesiona
      el CORE?
    - Dom_02_IPR.Agregacion[0].ID=CQ-054
    - Dom_02_IPR.Agregacion[0].Q=¿Cuántas IPR están en cartera del GORE Ñuble?
    - Dom_02_IPR.Agregacion[1].ID=CQ-055
    - Dom_02_IPR.Agregacion[1].Q=¿Cuántas IPR están en estado de ejecución?
    - Dom_02_IPR.Agregacion[2].ID=CQ-056
    - Dom_02_IPR.Agregacion[2].Q=¿Cuántas IPR fueron aprobadas en el año presupuestario
      vigente?
    - Dom_02_IPR.Agregacion[3].ID=CQ-057
    - Dom_02_IPR.Agregacion[3].Q=¿Cuál es el monto total de inversión regional en
      IPR?
    - Dom_02_IPR.Agregacion[4].ID=CQ-058
    - Dom_02_IPR.Agregacion[4].Q=¿Cuántas IPR están clasificadas como IDI vs PPR?
    - Dom_02_IPR.Agregacion[5].ID=CQ-059
    - Dom_02_IPR.Agregacion[5].Q=¿Cuántas IPR por comuna existen en la región?
    - Dom_02_IPR.Agregacion[6].ID=CQ-060
    - Dom_02_IPR.Agregacion[6].Q=¿Cuántas IPR por sector/área temática existen?
    - Dom_02_IPR.Existenciales[0].ID=CQ-029
    - Dom_02_IPR.Existenciales[0].Q=¿Qué es una IPR (Intervención Pública Regional)?
    - Dom_02_IPR.Existenciales[1].ID=CQ-030
    - Dom_02_IPR.Existenciales[1].Q=¿Qué es un IDI (Iniciativa de Inversión)?
    - Dom_02_IPR.Existenciales[2].ID=CQ-031
    - Dom_02_IPR.Existenciales[2].Q=¿Qué es un PPR (Programa Público Regional)?
    - Dom_02_IPR.Existenciales[3].ID=CQ-032
    - Dom_02_IPR.Existenciales[3].Q=¿Qué es un Estudio Básico?
    - Dom_02_IPR.Existenciales[4].ID=CQ-033
    - Dom_02_IPR.Existenciales[4].Q=¿Qué es un Proyecto de Inversión?
    - Dom_02_IPR.Existenciales[5].ID=CQ-034
    - Dom_02_IPR.Existenciales[5].Q=¿Qué es una Ficha IDI?
    - Dom_02_IPR.Existenciales[6].ID=CQ-035
    - Dom_02_IPR.Existenciales[6].Q=¿Qué es el código BIP?
    - Dom_02_IPR.Existenciales[7].ID=CQ-036
    - Dom_02_IPR.Existenciales[7].Q=¿Qué es el Perfil de un programa?
    - Dom_02_IPR.Existenciales[8].ID=CQ-037
    - Dom_02_IPR.Existenciales[8].Q=¿Qué es el Diseño de un programa?
    - Dom_02_IPR.Existenciales[9].ID=CQ-038
    - Dom_02_IPR.Existenciales[9].Q=¿Qué tipos de IPR existen según su naturaleza?
    - Dom_02_IPR.ID=GN-CQS-DOM-02
    - Dom_02_IPR.Relacionales[0].ID=CQ-039
    - Dom_02_IPR.Relacionales[0].Q=¿Qué relación existe entre IPR y mecanismo de financiamiento?
    - Dom_02_IPR.Relacionales[1].ID=CQ-040
    - Dom_02_IPR.Relacionales[1].Q=¿Qué entidad formula una IPR?
    - Dom_02_IPR.Relacionales[2].ID=CQ-041
    - Dom_02_IPR.Relacionales[2].Q=¿Qué entidad evalúa una IPR?
    - Dom_02_IPR.Relacionales[3].ID=CQ-042
    - Dom_02_IPR.Relacionales[3].Q=¿Qué entidad ejecuta una IPR?
    - Dom_02_IPR.Relacionales[4].ID=CQ-043
    - Dom_02_IPR.Relacionales[4].Q=¿Qué relación tiene una IPR con la ERD?
    - Dom_02_IPR.Relacionales[5].ID=CQ-044
    - Dom_02_IPR.Relacionales[5].Q=¿Qué relación tiene una IPR con el PLADECO comunal?
    - Dom_02_IPR.Relacionales[6].ID=CQ-045
    - Dom_02_IPR.Relacionales[6].Q=¿Qué división GORE patrocina una IPR?
    - Dom_02_IPR.Relacionales[7].ID=CQ-046
    - Dom_02_IPR.Relacionales[7].Q=¿Qué relación existe entre IDI y SNI?
    - Dom_02_IPR.Relacionales[8].ID=CQ-047
    - Dom_02_IPR.Relacionales[8].Q=¿Qué relación existe entre PPR y BIPS?
    - Dom_02_IPR.Relacionales[9].ID=CQ-048
    - Dom_02_IPR.Relacionales[9].Q=¿Qué vinculación tiene el código BIP con el ciclo
      de vida de la IPR?
    - Dom_02_IPR.Temporales[0].ID=CQ-049
    - Dom_02_IPR.Temporales[0].Q=¿Cuáles son las etapas del ciclo de vida de una IPR?
    - Dom_02_IPR.Temporales[1].ID=CQ-050
    - Dom_02_IPR.Temporales[1].Q=¿Cuál es la secuencia de fases de una IDI (Prefactibilidad,
      Factibilidad, Diseño, Ejecución)?
    - Dom_02_IPR.Temporales[2].ID=CQ-051
    - Dom_02_IPR.Temporales[2].Q=¿Cuál es la secuencia de fases de un PPR (Perfil,
      Diseño, Ejecución)?
    - Dom_02_IPR.Temporales[3].ID=CQ-052
    - Dom_02_IPR.Temporales[3].Q=¿Cuándo se asigna el código BIP a una iniciativa?
    - Dom_02_IPR.Temporales[4].ID=CQ-053
    - Dom_02_IPR.Temporales[4].Q=¿Cuándo se realiza la evaluación ex post de una IPR?
    - Dom_03_Financiamiento.Agregacion[0].ID=CQ-082
    - Dom_03_Financiamiento.Agregacion[0].Q=¿Cuál es el presupuesto total FNDR de
      Ñuble para el año vigente?
    - Dom_03_Financiamiento.Agregacion[1].ID=CQ-083
    - Dom_03_Financiamiento.Agregacion[1].Q=¿Cuál es el monto disponible para FRIL
      en el año vigente?
    - Dom_03_Financiamiento.Agregacion[2].ID=CQ-084
    - Dom_03_Financiamiento.Agregacion[2].Q=¿Cuál es el monto disponible para FRPD
      en el año vigente?
    - Dom_03_Financiamiento.Agregacion[3].ID=CQ-085
    - Dom_03_Financiamiento.Agregacion[3].Q=¿Cuál es el monto disponible para el Concurso
      8%?
    - Dom_03_Financiamiento.Agregacion[4].ID=CQ-086
    - Dom_03_Financiamiento.Agregacion[4].Q=¿Cuál es el porcentaje de ejecución presupuestaria
      FNDR?
    - Dom_03_Financiamiento.Agregacion[5].ID=CQ-087
    - Dom_03_Financiamiento.Agregacion[5].Q=¿Cuántos mecanismos de financiamiento
      administra el GORE?
    - Dom_03_Financiamiento.Agregacion[6].ID=CQ-088
    - Dom_03_Financiamiento.Agregacion[6].Q=¿Cuántas glosas presupuestarias aplican
      al GORE Ñuble?
    - Dom_03_Financiamiento.Existenciales[0].ID=CQ-061
    - Dom_03_Financiamiento.Existenciales[0].Q=¿Qué es el FNDR (Fondo Nacional de
      Desarrollo Regional)?
    - Dom_03_Financiamiento.Existenciales[1].ID=CQ-062
    - Dom_03_Financiamiento.Existenciales[1].Q=¿Qué es el FRIL (Fondo Regional de
      Iniciativa Local)?
    - Dom_03_Financiamiento.Existenciales[2].ID=CQ-063
    - Dom_03_Financiamiento.Existenciales[2].Q=¿Qué es el FRPD (Fondo Regional para
      la Productividad y el Desarrollo)?
    - Dom_03_Financiamiento.Existenciales[3].ID=CQ-064
    - Dom_03_Financiamiento.Existenciales[3].Q=¿Qué es el Subtítulo 24 (Transferencias
      Corrientes)?
    - Dom_03_Financiamiento.Existenciales[4].ID=CQ-065
    - Dom_03_Financiamiento.Existenciales[4].Q=¿Qué es el Subtítulo 31 (Iniciativas
      de Inversión)?
    - Dom_03_Financiamiento.Existenciales[5].ID=CQ-066
    - Dom_03_Financiamiento.Existenciales[5].Q=¿Qué es el Subtítulo 33 (Transferencias
      de Capital)?
    - Dom_03_Financiamiento.Existenciales[6].ID=CQ-067
    - Dom_03_Financiamiento.Existenciales[6].Q=¿Qué es la Glosa 06 (Programas de Ejecución
      Directa)?
    - Dom_03_Financiamiento.Existenciales[7].ID=CQ-068
    - Dom_03_Financiamiento.Existenciales[7].Q=¿Qué es la Glosa 07 (Subvenciones 8%)?
    - Dom_03_Financiamiento.Existenciales[8].ID=CQ-069
    - Dom_03_Financiamiento.Existenciales[8].Q=¿Qué es la Glosa 12 (FRIL)?
    - Dom_03_Financiamiento.Existenciales[9].ID=CQ-070
    - Dom_03_Financiamiento.Existenciales[9].Q=¿Qué es la Glosa 13 (FRPD)?
    - Dom_03_Financiamiento.ID=GN-CQS-DOM-03
    - Dom_03_Financiamiento.Relacionales[0].ID=CQ-071
    - Dom_03_Financiamiento.Relacionales[0].Q=¿Qué relación existe entre tipo de IPR
      y mecanismo de financiamiento aplicable?
    - Dom_03_Financiamiento.Relacionales[1].ID=CQ-072
    - Dom_03_Financiamiento.Relacionales[1].Q=¿Qué relación tiene el FNDR con la Ley
      de Presupuestos?
    - Dom_03_Financiamiento.Relacionales[2].ID=CQ-073
    - Dom_03_Financiamiento.Relacionales[2].Q=¿Qué entidades pueden acceder al FRIL?
    - Dom_03_Financiamiento.Relacionales[3].ID=CQ-074
    - Dom_03_Financiamiento.Relacionales[3].Q=¿Qué entidades pueden acceder al FRPD?
    - Dom_03_Financiamiento.Relacionales[4].ID=CQ-075
    - Dom_03_Financiamiento.Relacionales[4].Q=¿Qué relación tiene el FRPD con la Ley
      de Royalty Minero?
    - Dom_03_Financiamiento.Relacionales[5].ID=CQ-076
    - Dom_03_Financiamiento.Relacionales[5].Q=¿Qué glosa aplica para transferencias
      a municipios?
    - Dom_03_Financiamiento.Relacionales[6].ID=CQ-077
    - Dom_03_Financiamiento.Relacionales[6].Q=¿Qué glosa aplica para transferencias
      a privados sin fines de lucro?
    - Dom_03_Financiamiento.Temporales[0].ID=CQ-078
    - Dom_03_Financiamiento.Temporales[0].Q=¿Cuál es el calendario presupuestario
      anual del FNDR?
    - Dom_03_Financiamiento.Temporales[1].ID=CQ-079
    - Dom_03_Financiamiento.Temporales[1].Q=¿Cuándo se realizan los llamados FRIL
      en el año?
    - Dom_03_Financiamiento.Temporales[2].ID=CQ-080
    - Dom_03_Financiamiento.Temporales[2].Q=¿Cuándo se realiza el concurso FRPD?
    - Dom_03_Financiamiento.Temporales[3].ID=CQ-081
    - Dom_03_Financiamiento.Temporales[3].Q=¿Cuándo se realiza el concurso 8%?
    - Dom_04_Evaluacion.Agregacion[0].ID=CQ-113
    - Dom_04_Evaluacion.Agregacion[0].Q=¿Cuántos tracks de evaluación existen según
      tipo de IPR?
    - Dom_04_Evaluacion.Agregacion[1].ID=CQ-114
    - Dom_04_Evaluacion.Agregacion[1].Q=¿Cuántos niveles de proporcionalidad define
      MDSF?
    - Dom_04_Evaluacion.Agregacion[2].ID=CQ-115
    - Dom_04_Evaluacion.Agregacion[2].Q=¿Cuántas metodologías sectoriales de evaluación
      existen?
    - Dom_04_Evaluacion.Agregacion[3].ID=CQ-116
    - Dom_04_Evaluacion.Agregacion[3].Q=¿Cuántos estados RATE posibles existen?
    - Dom_04_Evaluacion.Agregacion[4].ID=CQ-117
    - Dom_04_Evaluacion.Agregacion[4].Q=¿Cuántas IPR fueron evaluadas con RS en el
      año vigente?
    - Dom_04_Evaluacion.Agregacion[5].ID=CQ-118
    - Dom_04_Evaluacion.Agregacion[5].Q=¿Cuál es la tasa de aprobación (RS) de IPR
      evaluadas?
    - Dom_04_Evaluacion.Existenciales[0].ID=CQ-089
    - Dom_04_Evaluacion.Existenciales[0].Q=¿Qué es el SNI (Sistema Nacional de Inversiones)?
    - Dom_04_Evaluacion.Existenciales[1].ID=CQ-090
    - Dom_04_Evaluacion.Existenciales[1].Q=¿Qué es el BIP (Banco Integrado de Proyectos)?
    - Dom_04_Evaluacion.Existenciales[2].ID=CQ-091
    - Dom_04_Evaluacion.Existenciales[2].Q=¿Qué es un RATE (Resultado de Análisis
      Técnico-Económico)?
    - Dom_04_Evaluacion.Existenciales[3].ID=CQ-092
    - Dom_04_Evaluacion.Existenciales[3].Q=¿Qué significa RS (Recomendado Satisfactoriamente)?
    - Dom_04_Evaluacion.Existenciales[4].ID=CQ-093
---

# 01 Estructura Organizacional

## Scope
Preguntas de competencia maestras del bundle ontologico GN.

## Triples
- `_manifest`
- `LLM_Parsing_Instructions`
- `Dom_01_Estructura_Organizacional`
- `Dom_02_IPR`
- `Dom_03_Financiamiento`
- `Dom_04_Evaluacion`
- `Dom_05_Aprobacion`
- `Dom_06_Convenios`
- `Dom_07_Ejecucion`
- `Dom_08_Rendicion`
- `Dom_09_Normativo`
- `Dom_10_TDE`
- `Dom_11_Gestion_Operacional_IPR`
- `Dom_12_Selector_Vias_Financiamiento`
- `Dom_13_Guia_IDI_SNI`
- `Dom_14_PPR_Ejecucion_Directa`
- `Dom_15_FRIL`
- `Dom_16_FRPD`
- `Dom_17_Transferencia_PPR`
- `Dom_18_Concurso_8_Porciento`
- `Dom_19_Circular_33`
- `Dom_20_Umbrales_Transversal`
- `Resumen_Estadistico`

---
_manifest:
  urn: urn:gn:kb:matriz-integracion-organica
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/00_meta/kb_gn_999_matriz_integracion_organica_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- taxonomia
- indice-artefactos
- gobernanza
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/00_meta/kb_gn_999_matriz_integracion_organica_koda.yml
    source_hashes:
      domains/gn/00_meta/kb_gn_999_matriz_integracion_organica_koda.yml: 7975c99427d63597e7fb85b971e34c34f77b14aa74df25014dded0fb3262afdc
    source_type: koda_yaml
    transformation_mode: korafy_koda_hybrid
    fs: 100
    cr: 1.47
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Matriz editorial de integracion organica; mantener como artefacto
      de control.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 14
    meat_count: 557
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__matriz-integracion-organica.md.json
---

# Matriz de Integración Orgánica del Conocimiento GORE Ñuble
## Taxonomia Conocimiento
### ID
GN-TAXONOMIA-01
### Purp
Clasificación jerárquica de las 13 áreas de conocimiento del GORE Ñuble.
### Nivel 1 Fundamentos
#### ID
TAX-N1-FUNDAMENTOS
#### Def
Conocimiento base sobre qué es y cómo funciona un GORE.
#### Areas
- intro
- legal
- estadocl
### Nivel 2 Estrategia
#### ID
TAX-N2-ESTRATEGIA
#### Def
Visión de largo plazo y planificación estratégica.
#### Areas
- estrategia
- social
- estadisticas
### Nivel 3 Operacion
#### ID
TAX-N3-OPERACION
#### Def
Gestión operativa del día a día.
#### Areas
- gestion
- presupuesto
- ipr
- juridico
### Nivel 4 Habilitadores
#### ID
TAX-N4-HABILITADORES
#### Def
Capacidades transversales que habilitan la operación.
#### Areas
- arquitectura
- comunicaciones
- tde

## Indice Artefactos
### ID
GN-INDICE-01
### Intro
#### ID
IDX-INTRO
#### Titulo
Introducción y Fundamentos
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_000 | urn:gn:kb:intro-gores-nuble | Guía Integral GORE Ñuble | intro/kb_gn_000_intro_gores_nuble_koda.yml | KODA | Guía técnico-operativa integral: marco constitucional, estructura GORE, contexto Ñuble, autoridades. |
| kb_gn_013 | urn:gn:kb:vision-desarrollo-nuble | Visión de Desarrollo Ñuble | intro/kb_gn_013_vision_desarrollo_nuble_koda.yml | KODA | Visión estratégica de desarrollo para la Región de Ñuble. |
| kb_gn_900 | urn:gn:kb:gore-ideal | GORE Ideal | intro/kb_gn_900_gore_ideal_koda.yml | KODA | Modelo aspiracional del GORE, buenas prácticas y referentes. |
### Legal
#### ID
IDX-LEGAL
#### Titulo
Marco Legal y Normativo
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_031 | urn:gn:kb:loc-gore | LOC GORE | legal/kb_gn_031_loc_gore_koda.yml | KODA | Ley Orgánica Constitucional sobre Gobiernos Regionales (Ley 19.175). |
| kb_gn_200 | urn:gn:kb:marco-legal-gores | Marco Legal GOREs | legal/kb_gn_200_marco_legal_gores_koda.yml | KODA | Compilación del marco legal aplicable a los Gobiernos Regionales. |
### Estadocl
#### ID
IDX-ESTADOCL
#### Titulo
Estructura del Estado de Chile
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_core_007 | urn:mgmt:kb:estructura-estado-chile | Estructura del Estado de Chile | ../../estadocl/kb_core_007_estructura_estado_chile_koda.yml | KODA | Organización general del Estado chileno: poderes, niveles, instituciones. |
### Estrategia
#### ID
IDX-ESTRATEGIA
#### Titulo
Planificación Estratégica
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_006 | urn:gn:kb:erd-nuble-2024-2030 | ERD Ñuble 2024-2030 | estrategia/kb_gn_006_erd_nuble_2024_2030_koda.yml | KODA | Estrategia Regional de Desarrollo 2024-2030: ejes, objetivos, metas. |
| kb_gn_056 | urn:gn:kb:nuble-250 | Ñuble250 | estrategia/kb_gn_056_nuble250_koda.yml | KODA | Plan de Aceleración Regional Ñuble250. |
### Social
#### ID
IDX-SOCIAL
#### Titulo
Diagnóstico Social
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_004 | urn:gn:kb:problemas-sociales-cl | Problemas Sociales Chile | social/kb_gn_004_problemas_sociales_cl_koda.yml | KODA | Diagnóstico de problemas sociales en Chile con foco regional. |
### Estadisticas
#### ID
IDX-ESTADISTICAS
#### Titulo
Indicadores y Estadísticas
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_005 | urn:gn:kb:indicadores-nuble | Indicadores Ñuble | estadisticas/kb_gn_005_indicadores_nuble_koda.yml | KODA | Indicadores socioeconómicos, demográficos y de desarrollo de Ñuble. |
### Gestion
#### ID
IDX-GESTION
#### Titulo
Gestión Institucional
#### Artefactos
-
  #### Id
  kb_gn_014
  #### Urn
  urn:gn:kb:glosario-gore-nuble
  #### Titulo
  Glosario GORE Ñuble
  #### Path
  gestion/kb_gn_014_glosario_gore_nuble_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Canon terminológico jurídico-administrativo: ~140 términos definidos.
  #### XRef
  - GLOS-TERM-*
-
  #### Id
  kb_gn_017
  #### Urn
  urn:gn:kb:manual-induccion-gore-nuble-2026
  #### Titulo
  Manual de Inducción 2025
  #### Path
  gestion/kb_gn_017_manual_induccion_gore_nuble_2025_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Guía de inducción para nuevos funcionarios del GORE Ñuble.
-
  #### Id
  kb_gn_009
  #### Urn
  urn:gn:kb:cuentas-publicas-2021-2024
  #### Titulo
  Cuentas Públicas 2021-2024
  #### Path
  gestion/kb_gn_009_cuentas_publicas_2021_2024_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Síntesis de cuentas públicas del período 2021-2024.
-
  #### Id
  kb_gn_015
  #### Urn
  urn:gn:kb:flujos-aprobacion-documentos
  #### Titulo
  Sistema de Aprobaciones
  #### Path
  gestion/kb_gn_015_aprobaciones_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Matrices de aprobación y flujos de autorización.
-
  #### Id
  kb_gn_020
  #### Urn
  urn:gn:kb:gestion-rendiciones
  #### Titulo
  Gestión de Rendiciones
  #### Path
  gestion/kb_gn_020_gestion_rendiciones_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Procedimientos para rendición de cuentas (SISREC).
-
  #### Id
  kb_gn_035
  #### Urn
  urn:gn:kb:estrategia-gestion
  #### Titulo
  Estrategia de Gestión
  #### Path
  gestion/kb_gn_035_estrategia_gestion_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Plan de gestión institucional del GORE.
#### Manuales Operativos
#### ID
IDX-MANUALES
#### Def
Manuales de procedimientos por área funcional.
#### Artefactos
| id | titulo | urn | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| manual_1_1 | Manual Presupuesto | urn:gn:kb:manual-presupuesto | gestion/kb_gn_043_manual_presupuesto_koda.yml | KODA | Procedimientos de gestión presupuestaria. |
| manual_1_2 | Manual Contabilidad | urn:gn:kb:manual-contabilidad | gestion/kb_gn_044_manual_contabilidad_koda.yml | KODA | Procedimientos contables y registro. |
| manual_1_3 | Manual Tesorería | urn:gn:kb:manual-tesoreria | gestion/kb_gn_045_manual_tesoreria_koda.yml | KODA | Procedimientos de tesorería y pagos. |
| manual_2_1 | Manual Compras | urn:gn:kb:manual-compras | gestion/kb_gn_046_manual_compras_koda.yml | KODA | Procedimientos de compras y contrataciones. |
| manual_2_2 | Manual Inventarios | urn:gn:kb:manual-inventarios-bodegas | gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml | KODA | Gestión de inventarios. |
| manual_2_3 | Manual Activo Fijo | urn:gn:kb:manual-activo-fijo | gestion/kb_gn_041_manual_activo_fijo_koda.yml | KODA | Control de activos fijos. |
| manual_2_4 | Manual Flotas | urn:gn:kb:manual-flotas | gestion/kb_gn_047_manual_flotas_koda.yml | KODA | Gestión de vehículos y flotas. |
| manual_3_1 | Manual Ciclo de Vida | urn:gn:kb:manual-ciclo-vida | gestion/kb_gn_048_manual_ciclo_vida_koda.yml | KODA | Ciclo de vida del funcionario. |
| manual_3_2 | Manual Remuneraciones | urn:gn:kb:manual-remuneraciones | gestion/kb_gn_049_manual_remuneraciones_koda.yml | KODA | Gestión de remuneraciones. |
| manual_3_3 | Manual Tiempo y Ausentismo | urn:gn:kb:manual-asistencia | gestion/kb_gn_051_manual_asistencia_koda.yml | KODA | Control de asistencia y ausentismo. |
| manual_3_4 | Manual Desarrollo Organizacional | urn:gn:kb:manual-desarrollo-organizacional | gestion/kb_gn_042_manual_desarrollo_organizacional_koda.yml | KODA | Desarrollo organizacional y capacitación. |
| manual_3_5 | Manual Bienestar | urn:gn:kb:manual-bienestar | gestion/kb_gn_052_manual_bienestar_koda.yml | KODA | Programas de bienestar funcionario. |
### Presupuesto
#### ID
IDX-PRESUPUESTO
#### Titulo
Gestión Presupuestaria
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_018 | urn:gn:kb:gestion-prpto | Gestión Presupuestaria | presupuesto/kb_gn_018_gestion_prpto_koda.yml | KODA | Marco general de gestión presupuestaria del GORE. |
| kb_gn_210 | urn:gn:kb:ley-presupuestos-2026-partida-31 | Ley Presupuestos 2026 - Partida 31 | presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml | KODA | Extracto de la Ley de Presupuestos 2026, Partida 31 (GOREs). |
| kb_gn_211 | urn:gn:kb:ley-presupuestos-2026-normas-generales | Ley Presupuestos 2026 - Normas Generales | presupuesto/kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml | KODA | Normas generales de ejecución presupuestaria. |
### Ipr
#### ID
IDX-IPR
#### Titulo
Inversión Pública Regional
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_001 | urn:gn:kb:transferencia-ppr | Transferencia PPR | ipr/kb_gn_001_transferencia_ppr_koda.yml | KODA | Procedimiento de transferencia de programas públicos regionales. |
| kb_gn_011 | urn:gn:kb:selector-ipr | Selector IPR | ipr/kb_gn_011_selector_ipr_koda.yml | KODA | Árbol de decisión para clasificar IPR (IDI vs PPR). |
| kb_gn_019 | urn:gn:kb:gestion-ipr | Gestión IPR | ipr/kb_gn_019_gestion_ipr_koda.yml | KODA | Ciclo completo de gestión de inversión pública regional. |
| kb_gn_024 | urn:gn:kb:guia-idi-sni-sts | Guía IDI/SNI | ipr/kb_gn_024_guia_idi_sni_koda.yml | KODA | Guía para formulación de iniciativas de inversión en SNI. |
| kb_gn_025 | urn:gn:kb:guia-programas-directos-gore | Guía Programas | ipr/kb_gn_025_guia_programas_koda.yml | KODA | Guía para formulación de programas públicos. |
| kb_gn_026 | urn:gn:kb:guia-fril-2025-sts | Guía FRIL | ipr/kb_gn_026_guia_fril_koda.yml | KODA | Guía del Fondo Regional de Iniciativa Local. |
| kb_gn_027 | urn:gn:kb:guia-frpd-nuble | Guía FRPD | ipr/kb_gn_027_guia_frpd_koda.yml | KODA | Guía del Fondo Regional para la Productividad y el Desarrollo. |
| kb_gn_028 | urn:gn:kb:instructivo-subvencion-8-2025-sts | Instructivo Subvención 8% | ipr/kb_gn_028_instructivo_subvencion_8_koda.yml | KODA | Instructivo para subvenciones del 8% FNDR. |
| kb_gn_029 | urn:gn:kb:guia-circular-33-sts | Guía Circular 33 | ipr/kb_gn_029_guia_circ33_koda.yml | KODA | Guía de la Circular 33 sobre evaluación socioeconómica. |
#### Repertorio Intervenciones
#### ID
IDX-RIS
#### Def
Repertorio de Intervenciones Sectoriales
#### Path
ipr/kb_gn_010_ris/
#### Artefactos
| id | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- |
| kb_gn_010_index | RIS - Índice | ipr/kb_gn_010_ris/kb_gn_010_ris_index_koda.yml | KODA | Índice del repertorio de intervenciones sectoriales. |
| kb_gn_010_artcult | RIS - Arte y Cultura | ipr/kb_gn_010_ris/kb_gn_010_ris_artcult_koda.yml | KODA | Intervenciones en arte y cultura. |
| kb_gn_010_deportes | RIS - Deportes | ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml | KODA | Intervenciones en deportes. |
| kb_gn_010_edpub | RIS - Espacios Públicos | ipr/kb_gn_010_ris/kb_gn_010_ris_edpub_koda.yml | KODA | Intervenciones en espacios públicos. |
| kb_gn_010_empub | RIS - Edificación Pública | ipr/kb_gn_010_ris/kb_gn_010_ris_empub_koda.yml | KODA | Intervenciones en edificación pública. |
| kb_gn_010_patrimonio | RIS - Patrimonio | ipr/kb_gn_010_ris/kb_gn_010_ris_patrimonio_koda.yml | KODA | Intervenciones en patrimonio. |
| kb_gn_010_pmdt | RIS - PMDT | ipr/kb_gn_010_ris/kb_gn_010_ris_pmdt_koda.yml | KODA | Programa de Mejoramiento del Desarrollo Territorial. |
| kb_gn_010_proginv | RIS - Programas de Inversión | ipr/kb_gn_010_ris/kb_gn_010_ris_proginv_koda.yml | KODA | Programas de inversión regionales. |
| kb_gn_010_proyinv | RIS - Proyectos de Inversión | ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml | KODA | Proyectos de inversión regionales. |
### Juridico
#### ID
IDX-JURIDICO
#### Titulo
Actos Jurídicos
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_100 | urn:gn:kb:modelos-actos-juridicos | Modelos de Actos Jurídicos | juridico/kb_gn_100_modelos_actos_juridicos_koda.yml | KODA | Templates de resoluciones, convenios y otros actos administrativos. |
### Arquitectura
#### ID
IDX-ARQUITECTURA
#### Titulo
Arquitectura y Procesos
#### Artefactos
-
  #### Id
  kb_gn_050
  #### Urn
  urn:gn:kb:aceleracion-regional
  #### Titulo
  Aceleración Regional
  #### Path
  arquitectura/kb_gn_050_aceleracion_regional_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Plan de aceleración de capacidades del GORE.
-
  #### Id
  kb_gn_080
  #### Urn
  urn:gn:kb:cies-sitia
  #### Titulo
  CIES/SITIA
  #### Path
  arquitectura/kb_gn_080_cies_sitia_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Sistemas CIES y SITIA: inteligencia y análisis territorial.
-
  #### Id
  kb_gn_090
  #### Urn
  urn:gn:kb:gestion-info-geoespacial
  #### Titulo
  Gestión Geoespacial
  #### Path
  arquitectura/kb_gn_090_gestion_informacion_geoespacial_koda.yml
  #### Tipo
  KODA
  #### Resumen
  Gestión de información geoespacial e IDE regional.
-
  #### Id
  catalog_procesos
  #### Titulo
  Catálogo de Procesos
  #### Path
  arquitectura/catalog_procesos_gore.yml
  #### Tipo
  YAML
  #### Resumen
  Índice de todos los procesos GORE documentados.
#### BPMN Procesos
#### ID
IDX-BPMN
#### Def
Diagramas BPMN de procesos institucionales
#### Path
arquitectura/bpmn/
#### Artefactos
-
  #### Id
  D01
  #### Titulo
  Actos Administrativos
  #### Urn
  urn:gn:kb:bpmn-d01-actos-administrativos
  #### Path
  ../../../../sources/gn/arquitectura/bpmn/D01_actos_administrativos.md
  #### Koda path
  arquitectura/bpmn/D01_actos_administrativos_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de emisión de actos administrativos.
-
  #### Id
  D02
  #### Titulo
  Ciclo Presupuestario
  #### Urn
  urn:gn:kb:bpmn-d02-ciclo-presupuestario
  #### Path
  arquitectura/bpmn/D02_ciclo_presupuestario.md
  #### Koda path
  arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso del ciclo presupuestario anual.
-
  #### Id
  D03
  #### Titulo
  Gestión IPR
  #### Urn
  urn:gn:kb:bpmn-d03-gestion-ipr
  #### Path
  arquitectura/bpmn/D03_gestion_ipr.md
  #### Koda path
  arquitectura/bpmn/D03_gestion_ipr_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de gestión de inversión pública regional.
-
  #### Id
  D04
  #### Titulo
  Compras y Contrataciones
  #### Urn
  urn:gn:kb:bpmn-d04-compras-contrataciones
  #### Path
  arquitectura/bpmn/D04_compras_contrataciones.md
  #### Koda path
  arquitectura/bpmn/D04_compras_contrataciones_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de compras y contrataciones.
-
  #### Id
  D05
  #### Titulo
  Inventarios y Activo Fijo
  #### Urn
  urn:gn:kb:bpmn-d05-inventarios-activo-fijo
  #### Path
  arquitectura/bpmn/D05_inventarios_activo_fijo.md
  #### Koda path
  arquitectura/bpmn/D05_inventarios_activo_fijo_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de control de inventarios.
-
  #### Id
  D06
  #### Titulo
  Flota Vehicular
  #### Urn
  urn:gn:kb:bpmn-d06-flota-vehicular
  #### Path
  arquitectura/bpmn/D06_flota_vehicular.md
  #### Koda path
  arquitectura/bpmn/D06_flota_vehicular_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de gestión de flota.
-
  #### Id
  D07
  #### Titulo
  Recursos Humanos
  #### Urn
  urn:gn:kb:bpmn-d07-rrhh
  #### Path
  arquitectura/bpmn/D07_rrhh.md
  #### Koda path
  arquitectura/bpmn/D07_rrhh_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Procesos de gestión de RRHH.
-
  #### Id
  D08
  #### Titulo
  Rendiciones
  #### Urn
  urn:gn:kb:bpmn-d08-rendiciones
  #### Path
  arquitectura/bpmn/D08_rendiciones.md
  #### Koda path
  arquitectura/bpmn/D08_rendiciones_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de rendición de cuentas.
-
  #### Id
  D09
  #### Titulo
  CIES/SITIA
  #### Urn
  urn:gn:kb:bpmn-d09-cies-sitia
  #### Path
  arquitectura/bpmn/D09_cies_sitia.md
  #### Koda path
  arquitectura/bpmn/D09_cies_sitia_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Procesos de inteligencia territorial.
-
  #### Id
  D10
  #### Titulo
  Geoespacial/IDE
  #### Urn
  urn:gn:kb:bpmn-d10-geoespacial-ide
  #### Path
  arquitectura/bpmn/D10_geoespacial_ide.md
  #### Koda path
  arquitectura/bpmn/D10_geoespacial_ide_koda.yml
  #### Tipo
  BPMN
  #### Resumen
  Proceso de gestión geoespacial.
-
  #### Id
  bpmn_index
  #### Titulo
  Índice BPMN
  #### Path
  arquitectura/bpmn/_index.yml
  #### Tipo
  YAML
  #### Resumen
  Índice de procesos BPMN.
### Comunicaciones
#### ID
IDX-COMUNICACIONES
#### Titulo
Comunicaciones Institucionales
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_008 | urn:gn:kb:comunicaciones-oc | Comunicaciones Oficinas de Comunicaciones | comunicaciones/kb_gn_008_comunicaciones_oc_koda.yml | KODA | Roles y funciones del área de comunicaciones. |
| kb_gn_030 | urn:gn:kb:guia-comunicaciones | Guía de Comunicaciones | comunicaciones/kb_gn_030_guia_comunicaciones_koda.yml | KODA | Manual de estilo y protocolos de comunicación institucional. |
### Tde
#### ID
IDX-TDE
#### Titulo
Transformación Digital
#### Artefactos
| id | urn | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- | --- |
| kb_gn_710 | urn:gn:kb:informe-estado-inicial-gore-pre-td | Estado Inicial Pre-TD | tde/kb_gn_710_informe_estado_inicial_gore_pre_td_koda.yml | KODA | Diagnóstico del estado inicial del GORE previo a transformación digital. |
| kb_gn_720 | urn:gn:kb:estrategia-td-ia | Estrategia TD+IA | tde/kb_gn_720_estrategia_td_ia_koda.yml | KODA | Estrategia de Transformación Digital e Inteligencia Artificial. |
### Data
#### ID
IDX-DATA
#### Titulo
Datos Estructurados
#### Artefactos
| id | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- |
| kb_gn_002 | Noticias GORE | ../../../../sources/gn/data/kb_gn_002_noticias.csv | CSV | Histórico de noticias institucionales. |
| kb_gn_003 | IDIs Históricas | data/kb_gn_003_idis.csv | CSV | Base de datos de iniciativas de inversión históricas. |
| kb_gn_012 | Programas Vigentes | data/kb_gn_012_progs_vigentes.csv | CSV | Listado de programas públicos regionales vigentes. |
| kb_gn_110 | Convenios 2022-2025 | data/kb_gn_110_convenios_2022_2025.csv | CSV | Base de datos de convenios del período 2022-2025. |

## Grafo Dependencias
### ID
GN-GRAFO-01
### Def
Relaciones semánticas principales entre artefactos.
### Relaciones
| source | target | tipo | nota |
| --- | --- | --- | --- |
| kb_gn_000 | * | fundamenta | La guía intro es prerrequisito conceptual para todo el corpus. |
| kb_gn_014 | ['kb_gn_018', 'kb_gn_019', 'kb_gn_020'] | define_términos | El glosario define la terminología usada en gestión. |
| kb_gn_031 | ['kb_gn_210', 'kb_gn_211'] | norma | LOC GORE es el marco para ejecución presupuestaria. |
| kb_gn_006 | ['kb_gn_019', 'kb_gn_011'] | orienta | La ERD orienta la priorización de inversiones. |
| IDX-BPMN | manual_* | describe_proceso | BPMN proporciona visión de proceso, manuales el detalle. |
| kb_gn_720 | ['kb_gn_080', 'kb_gn_090'] | habilita | Estrategia TD+IA habilita sistemas de inteligencia. |

## Schema
### ID
IDX-SCHEMA
### Titulo
Esquemas de Validación
### Artefactos
| id | titulo | path | tipo | resumen |
| --- | --- | --- | --- | --- |
| koda_schema | KODA Schema | ../../schemas/koda-schema.json | JSON | Esquema JSON para validación de artefactos KODA. |

---
_manifest:
  urn: "urn:kora:kb:gn-matriz-rescate-transformacion"
  provenance:
    created_by: "Codex"
    created_at: "2026-03-08"
    source: "Analisis comparativo entre /Users/felixsanhueza/Developer/gorenuble/knowledge y /Users/felixsanhueza/Developer/kora/knowledge/gn"
version: "0.1.0"
status: draft
tags: [gn, migracion, rescate, trazabilidad, conocimiento]
lang: "es"
extensions: {}
---

# Matriz de Rescate de Transformacion GN

## Criterio

| Estado | Significado | Accion base |
| --- | --- | --- |
| `R1` | Rescatable con retrazado y normalizacion | Reemitir desde fuente explicita al formato KORA/MD actual. No confiar en el frontmatter actual. |
| `R2` | Rescatable pero requiere revision por mezcla, compresion o renombre semantico | Comparar cuerpo actual con fuente; si hay mezcla de fuentes, regenerar con procedencia explicita. |
| `R3` | Rederivar o rehacer | No usar el `.md` actual como canon. Regenerar desde fuente de verdad o redisenar el artefacto objetivo. |

## Hallazgos base

- El corpus actual `knowledge/gn` contiene `77` artefactos `.md`.
- El corpus fuente `gorenuble/knowledge` contiene `83` archivos en `domains/gn`, `14` artefactos ontologicos en `ontologies/onto_gorenuble`, `3` en `core`, `4` `.csv`, `1` `.json` y `1` `.xml`.
- Los `77` artefactos actuales incumplen el frontmatter base vigente de KORA/MD por ausencia de `extensions: {}`.
- La procedencia actual es demasiado generica (`source: "GORE Ñuble"`), por lo que la migracion no es auditable.

## Matriz por destino actual

### BPMN

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/bpmn/bpmn-d01-actos-administrativos.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D01_actos_administrativos_koda.yml` | `R1` | Rederivar con nombre estable y frontmatter actual. |
| `knowledge/gn/bpmn/bpmn-d02-ciclo-presupuestario.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D02_ciclo_presupuestario_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d03-gestion-ipr.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D03_gestion_ipr_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d04-compras-contrataciones.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D04_compras_contrataciones_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d05-inventarios-activo-fijo.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D05_inventarios_activo_fijo_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d06-flota-vehicular.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D06_flota_vehicular_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d07-rrhh.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D07_rrhh_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d08-rendiciones.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D08_rendiciones_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d09-cies-sitia.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D09_cies_sitia_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-d10-geoespacial-ide.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/D10_geoespacial_ide_koda.yml` | `R1` | Rederivar con trazabilidad explicita. |
| `knowledge/gn/bpmn/bpmn-index.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/bpmn/_index.yml` | `R1` | Regenerar indice desde los 10 BPMN definitivos. |

### Gestion

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/gestion/flujos-aprobacion-documentos.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_015_aprobaciones_koda.yml` | `R2` | Revisar compresion editorial; regenerar con `source_path` exacto. |
| `knowledge/gn/gestion/gestion-info-geoespacial.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/kb_gn_090_gestion_informacion_geoespacial_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/gestion/gestion-ipr.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_019_gestion_ipr_koda.yml` | `R1` | Reemitir desde KODA con procedencia exacta. |
| `knowledge/gn/gestion/gestion-prpto-2026.md` | `gorenuble/knowledge/domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml` | `R1` | Reemitir desde KODA con procedencia exacta. |
| `knowledge/gn/gestion/gestion-prpto.md` | `gorenuble/knowledge/domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_koda.yml` | `R1` | Reemitir desde KODA con procedencia exacta. |
| `knowledge/gn/gestion/gestion-rendiciones.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_020_gestion_rendiciones_koda.yml` | `R1` | Reemitir desde KODA con procedencia exacta. |
| `knowledge/gn/gestion/glosas-gores-2026.md` | `gorenuble/knowledge/domains/gn/03_operacion/presupuesto/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml` | `R2` | Revisar si debe vivir en `normativa/`; regenerar con lineage exacto. |
| `knowledge/gn/gestion/transferencia-ppr.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_001_transferencia_ppr_koda.yml` | `R1` | Reemitir desde KODA con procedencia exacta. |

### Raiz

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/gn-cqs-master.md` | `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleCQs_Master.yml` | `R3` | Rederivar como artefacto derivado de ontologia; no tratar el `.md` actual como canon. |

### Gobernanza

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/gobernanza/aceleracion-regional.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/kb_gn_050_aceleracion_regional_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/cies-sitia.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/arquitectura/kb_gn_080_cies_sitia_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/comunicaciones-oc.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/comunicaciones/kb_gn_008_comunicaciones_oc_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/cuentas-publicas-2021-2024.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_009_cuentas_publicas_2021_2024_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/erd-nuble-2024-2030.md` | `gorenuble/knowledge/domains/gn/02_estrategia/estrategia/kb_gn_006_erd_nuble_2024_2030_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/estrategia-gestion.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_035_estrategia_gestion_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/estrategia-td-ia.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/tde/kb_gn_720_estrategia_td_ia_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/glosario-gore-nuble.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_014_glosario_gore_nuble_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/glosario-ipr-consolidado.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/otroglosario.yml` | `R2` | Revisar construccion y naming; rederivar glosario con politica terminologica clara. |
| `knowledge/gn/gobernanza/gore-ideal.md` | `gorenuble/knowledge/domains/gn/01_fundamentos/intro/kb_gn_900_gore_ideal_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/indicadores-nuble.md` | `gorenuble/knowledge/domains/gn/02_estrategia/estadisticas/kb_gn_005_indicadores_nuble_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/informe-estado-inicial-gore-pre-td.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/tde/kb_gn_710_informe_estado_inicial_gore_pre_td_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/intro-gores-nuble.md` | `gorenuble/knowledge/domains/gn/01_fundamentos/intro/kb_gn_000_intro_gores_nuble_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/matriz-integracion-organica.md` | `gorenuble/knowledge/domains/gn/00_meta/kb_gn_999_matriz_integracion_organica_koda.yml` | `R2` | Mantener como referencia editorial e inventario; regenerar despues del corpus definitivo. |
| `knowledge/gn/gobernanza/nuble-250.md` | `gorenuble/knowledge/domains/gn/02_estrategia/estrategia/kb_gn_056_nuble250_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/gobernanza/omega-ipr-gestion-fusion.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml` | `R2` | Verificar si debe seguir existiendo como artefacto KORA/MD o si pasa a capa ontologica. |
| `knowledge/gn/gobernanza/organigrama.md` | `gorenuble/knowledge/domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml` + `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleOrgData.ttl` | `R2` | Revisar mezcla YAML+TTL; si se mantiene un solo artefacto, declarar ambas procedencias. |
| `knowledge/gn/gobernanza/plan-potenciamiento-dgi.md` | `gorenuble/knowledge/domains/gn/dgi/kb_gn_plan_potenciamiento_dgi_koda.yml` + dependencias `core/gestion/*` | `R2` | Reemitir con dependencias explicitas a `lean6` y `meyer-org-structure`. |
| `knowledge/gn/gobernanza/problemas-sociales-cl.md` | `gorenuble/knowledge/domains/gn/02_estrategia/social/kb_gn_004_problemas_sociales_cl_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/gobernanza/vision-desarrollo-nuble.md` | `gorenuble/knowledge/domains/gn/01_fundamentos/intro/kb_gn_013_vision_desarrollo_nuble_koda.yml` | `R1` | Reemitir desde fuente directa. |

### Guias

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/guias/guia-circular-33-sts.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_029_guia_circ33_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/guias/guia-comunicaciones.md` | `gorenuble/knowledge/domains/gn/04_habilitadores/comunicaciones/kb_gn_030_guia_comunicaciones_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/guias/guia-fril-2025-sts.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/guias/guia-frpd-nuble.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_027_guia_frpd_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/guias/guia-idi-sni-sts.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_024_guia_idi_sni_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/guias/guia-programas-directos-gore.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_025_guia_programas_koda.yml` | `R1` | Reemitir y normalizar naming. |
| `knowledge/gn/guias/instructivo-subvencion-8-2025-sts.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_028_instructivo_subvencion_8_koda.yml` | `R1` | Reemitir y normalizar naming. |

### Manuales

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/manuales/manual-activo-fijo.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_041_manual_activo_fijo_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-asistencia.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_051_manual_asistencia_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-bienestar.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_052_manual_bienestar_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-ciclo-vida.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_048_manual_ciclo_vida_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-compras.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-contabilidad.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_044_manual_contabilidad_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-desarrollo-organizacional.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_042_manual_desarrollo_organizacional_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-flotas.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_047_manual_flotas_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-induccion-gore-nuble-2026.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_017_manual_induccion_gore_nuble_2025_koda.yml` | `R2` | Revisar mismatch de nombre/anio; regenerar desde el artefacto KODA que ya declara 2026. |
| `knowledge/gn/manuales/manual-inventarios-bodegas.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_040_manual_inventarios_bodegas_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-operacional-dgi.md` | `gorenuble/knowledge/domains/gn/dgi/kb_gn_manual_operacional_dgi_koda.yml` | `R1` | Reemitir desde fuente directa con lineage exacto. |
| `knowledge/gn/manuales/manual-presupuesto.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml` | `R1` | Reemitir desde fuente directa con lineage exacto. |
| `knowledge/gn/manuales/manual-remuneraciones.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_049_manual_remuneraciones_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/manuales/manual-tesoreria.md` | `gorenuble/knowledge/domains/gn/03_operacion/gestion/kb_gn_045_manual_tesoreria_koda.yml` | `R1` | Reemitir desde fuente directa. |

### Normativa

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/normativa/dictamenes-cgr-gore.md` | `gorenuble/knowledge/domains/gn/03_operacion/juridico/kb_gn_101_dictamenes_cgr_gore_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/normativa/ley-presupuestos-2026-normas-generales.md` | `gorenuble/knowledge/domains/gn/03_operacion/presupuesto/kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/normativa/ley-presupuestos-2026-partida-31.md` | `gorenuble/knowledge/domains/gn/03_operacion/presupuesto/kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/normativa/loc-gore.md` | `gorenuble/knowledge/domains/gn/01_fundamentos/legal/kb_gn_031_loc_gore_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/normativa/marco-legal-gores.md` | `gorenuble/knowledge/domains/gn/01_fundamentos/legal/kb_gn_200_marco_legal_gores_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/normativa/modelos-actos-juridicos.md` | `gorenuble/knowledge/domains/gn/03_operacion/juridico/kb_gn_100_modelos_actos_juridicos_koda.yml` | `R1` | Reemitir desde fuente directa. |

### RIS

| Destino actual | Fuente principal | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `knowledge/gn/ris/ris-artcult.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_artcult_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-deportes.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-edpub.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_edpub_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-empub.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_empub_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-index.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_index_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-patrimonio.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_patrimonio_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-pmdt.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_pmdt_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-proginv.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proginv_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/ris-proyinv.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml` | `R1` | Reemitir desde fuente directa. |
| `knowledge/gn/ris/selector-ipr.md` | `gorenuble/knowledge/domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml` | `R1` | Reemitir desde fuente directa. |

## Fuentes relevantes hoy sin representacion limpia

### Ontologia, datos y schema

| Fuente | Tipo | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleOntology.ttl` | `TTL` | `R3` | Definir si se conserva como fuente externa o se crean artefactos KORA/MD derivados por modulo. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleOrgData.ttl` | `TTL` | `R3` | Usar como fuente declarada para artefactos organizacionales y consultas. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleIPRData.ttl` | `TTL` | `R3` | Definir artefactos derivados para estados IPR, mecanismos y casos. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleLegalData.ttl` | `TTL` | `R3` | Separar normativa derivada de datos legales derivados. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleApprovalData.ttl` | `TTL` | `R3` | Revisar relacion con aprobaciones y BPMN. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleReferenceData.ttl` | `TTL` | `R3` | Declarar su rol como vocabulario o datos de referencia. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleRenditionData.ttl` | `TTL` | `R3` | Conectar con `gestion-rendiciones` y BPMN D08. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleDipirOntology.ttl` | `TTL` | `R3` | Decidir si se mantiene en capa ontologica o se resume en KORA/MD. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleDipirRules.ttl` | `TTL` | `R3` | Tratar como reglas de dominio; no esconder en narrativas. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleShapes.ttl` | `TTL` | `R3` | Mantener como validacion de grafo, no convertir a prosa salvo resumen tecnico. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/goreNubleBundle.ttl` | `TTL` | `R3` | Tratar como ensamblado tecnico del grafo. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/alignmentGnubTde.ttl` | `TTL` | `R3` | Definir si requiere artefacto KORA/MD de alineamiento. |
| `gorenuble/knowledge/ontologies/onto_gorenuble/catalog-v001.xml` | `XML` | `R3` | Mantener como metaartefacto tecnico; documentar solo si aporta operativamente. |
| `gorenuble/knowledge/schemas/koda-schema.json` | `JSON Schema` | `R3` | No migrar como conocimiento GN; referenciar como dependencia tecnica. |
| `gorenuble/knowledge/domains/gn/05_data_raw/kb_gn_002_noticias.csv` | `CSV` | `R3` | Definir si se expone como dataset o si solo alimenta indices. |
| `gorenuble/knowledge/domains/gn/05_data_raw/kb_gn_003_idis.csv` | `CSV` | `R3` | Definir artefacto de datos o resumen analitico reproducible. |
| `gorenuble/knowledge/domains/gn/05_data_raw/kb_gn_012_progs_vigentes.csv` | `CSV` | `R3` | Definir artefacto de datos o resumen analitico reproducible. |
| `gorenuble/knowledge/domains/gn/05_data_raw/kb_gn_110_convenios_2022_2025.csv` | `CSV` | `R3` | Definir artefacto de datos o resumen analitico reproducible. |

### Core y auxiliares

| Fuente | Tipo | Estado | Accion recomendada |
| --- | --- | --- | --- |
| `gorenuble/knowledge/core/gestion/kb_gn_lean6_core_koda.yml` | `KODA YAML` | `R3` | No perderlo; usar como dependencia declarada de `plan-potenciamiento-dgi`. |
| `gorenuble/knowledge/core/gestion/kb_gn_meyer_org_structure_koda.yml` | `KODA YAML` | `R3` | No perderlo; usar como dependencia declarada de `plan-potenciamiento-dgi`. |
| `gorenuble/knowledge/core/gestion/kb_gn_mw_waissbluth_koda.yml` | `KODA YAML` | `R3` | Evaluar si debe generar artefactos derivados o quedar como referencia de diseno. |
| `gorenuble/knowledge/domains/estadocl/kb_core_007_estructura_estado_chile_koda.yml` | `KODA YAML` | `R3` | Integrar fuera de `knowledge/gn`; hoy solo aparece citado en la matriz. |
| `gorenuble/knowledge/domains/gn/01_fundamentos/intro/omega_gore_nuble_mermaid.md` | `Markdown auxiliar` | `R3` | Evaluar como insumo visual, no como artefacto final. |
| `gorenuble/knowledge/domains/gn/03_operacion/gestion/terminos.md` | `Markdown auxiliar` | `R3` | Revisar relacion con glosarios; probablemente fusionar o descartar con criterio. |

## Prioridad sugerida de reconstruccion

1. `CQs` + `BPMN`
2. `manuales` + `gestion`
3. `normativa`
4. `gobernanza` con casos `R2`
5. `ontologias`, `csv`, `core` y artefactos tecnicos

## Regla operativa propuesta

- Ningun artefacto nuevo debe quedar con `source: "GORE Ñuble"` como unica procedencia.
- Cada artefacto debe declarar al menos:
  - `source_path`
  - `source_type`
  - `transformation_mode`
  - `notes` si mezcla multiples fuentes
- Los `R2` y `R3` no deben migrarse en lote sin politica previa de derivacion.

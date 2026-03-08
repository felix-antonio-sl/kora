---
_manifest:
  urn: urn:gn:kb:dictamenes-cgr-gore
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/juridico/kb_gn_101_dictamenes_cgr_gore_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- contraloria
- jurisprudencia
- dictamenes
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/juridico/kb_gn_101_dictamenes_cgr_gore_koda.yml
    source_hashes:
      domains/gn/03_operacion/juridico/kb_gn_101_dictamenes_cgr_gore_koda.yml: e07623fa1ffd5eb5c8c0e3f48660809711c33053081fcccc0d17af9f1c50b098
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.3
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 5
    meat_count: 66
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/normativa__dictamenes-cgr-gore.md.json
---

# Dictámenes CGR para Gobiernos Regionales
## LLM Parsing Instructions
### Propósito
Catálogo de dictámenes de Contraloría General de la República (CGR) 
aplicables a Gobiernos Regionales. Uso: fundamentar informes jurídicos,
resoluciones y consultas de legalidad.

### Formato Cita
Dictamen CGR N° XXXXX de YYYY
### Advertencia
Los dictámenes pueden ser modificados por jurisprudencia posterior.
Siempre verificar vigencia en www.contraloria.cl/pdfbuscador/


## Dictamenes
### Convenios GORE Municipio
| id | fecha | materia | extracto | aplicacion |
| --- | --- | --- | --- | --- |
| CGR-031584-2019 | 2019-11-22 | Transferencia de recursos GORE a Municipios | El GORE puede transferir recursos a Municipalidades para ejecución 
de proyectos de interés regional, siempre que:
1. Exista convenio de transferencia aprobado por CORE.
2. Se defina claramente el objeto y obligación de rendir.
3. El proyecto cuente con RS favorable en el SNI.
 | Fundamentar resoluciones de convenios GORE-Municipio |
| CGR-052891-2020 | 2020-08-14 | Competencia GORE vs Municipal en proyectos | El GORE no puede ejecutar directamente funciones municipales, pero 
puede financiar proyectos vía convenio cuando el interés regional 
lo justifique (Art. 67 LOC 19.175).
 | Delimitar competencias en proyectos de escala local |
### Toma de Razon
-
  #### Id
  CGR-015234-2021
  #### Fecha
  2021-04-12
  #### Materia
  Umbral de Toma de Razón en GOREs
  #### Extracto
  Los actos administrativos del GORE que superen 5.000 UTM están 
afectos a Toma de Razón. Bajo ese umbral, pueden ser exentos 
conforme a Resolución CGR N° 7 de 2019.

  #### Aplicacion
  Determinar si resolución es afecta o exenta
  #### Umbral utm
  5000
-
  #### Id
  CGR-089123-2022
  #### Fecha
  2022-12-01
  #### Materia
  Convenios de programación y Toma de Razón
  #### Extracto
  Los convenios de programación suscritos por GOREs están afectos 
a Toma de Razón independiente del monto, por su naturaleza 
plurianual y vinculante.

  #### Aplicacion
  Clasificación de convenios de programación
### Delegacion
| id | fecha | materia | extracto | aplicacion |
| --- | --- | --- | --- | --- |
| CGR-044567-2020 | 2020-06-30 | Delegación de firma del Gobernador Regional | El Gobernador Regional puede delegar la firma de resoluciones 
exentas al Administrador Regional, conforme Art. 26 bis LOC 19.175.
La delegación debe constar en resolución afecta.
 | Fundamentar resoluciones de delegación |
### IPR
| id | fecha | materia | extracto | aplicacion |
| --- | --- | --- | --- | --- |
| CGR-078456-2021 | 2021-10-15 | Modificación de proyectos FNDR en ejecución | Las modificaciones sustanciales a proyectos FNDR en ejecución 
requieren nuevo acuerdo CORE cuando afecten monto, plazo o alcance 
de manera significativa (+20% presupuesto o +6 meses plazo).
 | Evaluar necesidad de volver a CORE |
| CGR-023789-2023 | 2023-03-28 | Rendición de cuentas en transferencias | El GORE es responsable subsidiario de las rendiciones de entidades 
receptoras de transferencias. Debe exigir rendición dentro de 60 días 
y tiene facultad de cobro ejecutivo.
 | Procedimiento de rendiciones en transferencias |
### Personal
| id | fecha | materia | extracto | aplicacion |
| --- | --- | --- | --- | --- |
| CGR-056789-2022 | 2022-07-20 | Contratación de personal a honorarios en GOREs | La contratación a honorarios en GOREs se rige por Art. 11 Ley 18.834.
Solo procede para tareas específicas, no habituales, de la institución.
No pueden desempeñar funciones de planta.
 | Evaluar procedencia de contratación a honorarios |

## Indice por Materia
### Convenios
- CGR-031584-2019
- CGR-052891-2020
### Toma de Razon
- CGR-015234-2021
- CGR-089123-2022
### Delegacion
- CGR-044567-2020
### IPR
- CGR-078456-2021
- CGR-023789-2023
### Personal
- CGR-056789-2022

## Notas de Uso
- Estos dictámenes son ejemplos representativos de jurisprudencia CGR.
- Para casos específicos, siempre consultar el buscador oficial de CGR.
- La numeración sigue el formato real de CGR: N° de dictamen - año.
- Actualizar periódicamente con nueva jurisprudencia relevante.

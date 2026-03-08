---
_manifest:
  urn: urn:gn:kb:ris-edpub
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_edpub_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- edificacion-publica
- infraestructura
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_edpub_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_edpub_koda.yml: fea492e4633214c96c97e8181045caff49bf315949a07ed88a85c4fbee28fb8e
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.18
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 13
    meat_count: 90
    fat_count: 0
    preserved_facts:
    - Creation-Date=2025-11-28
    - Ctx=Requisitos de información para proyectos de Edificación Pública que ingresan
      al Sistema Nacional de Inversiones (SNI), versión 2024.
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=GN-RIS-EDPUB-2024-01
    - "LLM_Parsing_Instructions.Content=BEGIN_LLM_INSTRUCTIONS\nYou are an AI agent\
      \ consuming a KODA artifact. Parse with absolute fidelity.\n\nFIDELITY: Preserve\
      \ meat (essential information) and skeleton (structure: headers, IDs, lists,\
      \ tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).\n\
      \nLEXICON (expand before processing):\n  Act->Action, Cause->Cause, Cond->Condition,\
      \ Cpt->Concept, Ctx->Context,\n  Def->Definition, Dep->Dependency, Dest->Destination,\
      \ Dln->Deadline,\n  Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,\n\
      \  Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,\n  Nat->Nature,\
      \ Obj->Objective, Proc->Process, Prohib->Prohibition,\n  Purp->Purpose, Ref->Reference,\
      \ Req->Requirement, Res->Result,\n  Resp->Responsible, Src->Source, Warn->Warning.\n\
      \nREFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS\
      \ document. External documents and legal sources are mentioned as contextual\
      \ information under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.\n\nLANGUAGE\
      \ POLICY: Keywords in English (and abbreviated forms as listed), content in\
      \ original language (Spanish). Never translate content.\nEND_LLM_INSTRUCTIONS\n"
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-GN-RIS-EDPUB-2024-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Model-Collaborator=KODA-TRANSFORMER
    - Modification-Date=2025-11-28
    - RIS_Edificacion_Publica_2024.Alcance.ID=RIS-EDPUB-2024-ALCANCE-01
    - RIS_Edificacion_Publica_2024.Alcance.Meta=Optimizar cumplimiento de actividades
      organizacionales.
    - RIS_Edificacion_Publica_2024.Alcance.Nota-Dudas=Aspectos no tratados se resuelven
      por Jefatura de la División de Evaluación Social de Inversiones.
    - RIS_Edificacion_Publica_2024.Alcance.Prop=Ampliar capacidad y mejorar dependencias
      institucionales.
    - RIS_Edificacion_Publica_2024.Fuente-URL=https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf
    - RIS_Edificacion_Publica_2024.ID=RIS-EDPUB-2024-META-01
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Accesibilidad.Normativa[0]=Ley
      N°20.530, art. 13.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Accesibilidad.Normativa[1]=DS
      N° 47 de 1992 (Ordenanza General de Urbanismo y Construcciones - OGUC).
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Accesibilidad.Normativa[2]=DS
      N° 50 de 2015 (MINVU).
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Accesibilidad.Req=Proveer
      libre acceso y circulación para personas con capacidades diferentes.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Arquitectura-Sustentable.Meta=Minimizar
      impacto ambiental y dependencia de hidrocarburos.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Arquitectura-Sustentable.Prop=Uso
      eficiente de energía, agua y otros recursos.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Arquitectura-Sustentable.Req-Diseño=Integrado
      (climatización, iluminación, sanitario, aguas lluvias, estructuras, redes, energías
      renovables, paisajismo).
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Clasificacion-BIP.Descriptor=Edificación
      Pública.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Clasificacion-BIP.Sector=Multisectorial.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Clasificacion-BIP.Subsector=Administración
      Multisector.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Competencia-Analisis.Nivel-Nacional=Análisis
      conjunto con Nivel Central del MDSF.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.Competencia-Analisis.Nivel-Regional-Comunal=Análisis
      por Secretarías Regionales Ministeriales de Desarrollo Social.
    - RIS_Edificacion_Publica_2024.Orientaciones_Sectoriales.ID=RIS-EDPUB-2024-ORIENTACIONES-SECTORIALES-01
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.ID=RIS-EDPUB-2024-POSTULACION-DISEÑO-01
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[0].Enunciado=Req-1:
      Formulación del proyecto conforme a requisitos de información para etapa de
      diseño.'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[0].ID=Req-1
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[1].Enunciado=Req-2:
      Uso de "Metodología de Edificación Pública" y "Metodología de Riesgo de Desastre".'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[1].ID=Req-2
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[2].Enunciado=Req-3:
      Proyección de dotación de servicio (demanda proyectada de equipos, equipamiento
      y m² según necesidades, misión del servicio y carga de trabajo).'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[2].ID=Req-3
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[3].Enunciado=Req-4:
      Acreditación situación legal del inmueble (según "Requisitos Genéricos sobre
      las Propiedades en que se Proyectan Edificaciones").'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[3].ID=Req-4
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[4].Enunciado=Req-5:
      Cumplimiento de "Antecedentes Técnicos Requeridos para Proyectos que Consideran
      Edificación".'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[4].ID=Req-5
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[5].Enunciado=Req-6:
      Carta de compromiso de traslado al nuevo recinto por cada servicio involucrado.'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[5].ID=Req-6
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[6].Enunciado=Req-7:
      Documento firmado por responsables de la administración de la infraestructura
      (jefes de servicios participantes).'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno.Req-Generales[6].ID=Req-7
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.ID=RIS-EDPUB-2024-POSTULACION-DISEÑO-EJEC-CONJUNTA-01
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.Req-Generales[0].Enunciado=Req-1:
      Formulación del proyecto conforme a requisitos de información para etapa de
      diseño (con estimaciones de fuentes secundarias y usando metodologías correspondientes).'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.Req-Generales[0].ID=Req-1
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.Req-Generales[1].Enunciado=Req-2:
      Presentar lo solicitado en el "Instructivo para postulación de proyectos a etapa
      de ejecución con diseño referencial".'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.Req-Generales[1].ID=Req-2
    - 'RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.Req-Generales[2].Enunciado=Req-3:
      Incluir consideraciones de eficiencia energética y otros aspectos pertinentes
      contenidos en los "Antecedentes Técnicos Requeridos para Proyectos que Consideran
      Edificación".'
    - RIS_Edificacion_Publica_2024.Postulacion_Diseno_Ejecucion_Conjunta.Req-Generales[2].ID=Req-3
    - RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.ID=RIS-EDPUB-2024-POSTULACION-EJECUCION-01
    - 'RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[0].Enunciado=Req-1:
      Formulación del proyecto conforme a "Metodología de Edificación Pública" y "Metodología
      de Riesgo de Desastre" (para etapa de ejecución).'
    - RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[0].ID=Req-1
    - 'RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[1].Enunciado=Req-2:
      Cumplir requisitos de etapa de diseño (aplicable si se concentra funcionamiento
      de varios servicios públicos).'
    - RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[1].ID=Req-2
    - 'RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[1].Nota=Nota:
      Aplica si no se postuló a Diseño en SNI.'
    - 'RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[2].Enunciado=Req-3:
      Presentar antecedentes según "Antecedentes Técnicos Requeridos para Proyectos
      que Consideran Edificación" para ejecución.'
    - RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[2].ID=Req-3
    - 'RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[3].Enunciado=Req-4:
      Cuadro comparativo entre programa arquitectónico aprobado y diseño resultante,
      con justificación de diferencias.'
    - RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[3].ID=Req-4
    - 'RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[4].Enunciado=Req-5:
      Cronograma de Actividades o Carta Gantt.'
    - RIS_Edificacion_Publica_2024.Postulacion_Ejecucion.Req-Generales[4].ID=Req-5
    - RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.ID=RIS-EDPUB-2024-POSTULACION-PREFACT-FACT-01
    - 'RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.Req-Generales[0].Detalle[0]=Metodologia-1:
      "Metodología de Edificación Pública".'
    - 'RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.Req-Generales[0].Detalle[1]=Metodologia-2:
      "Metodología de Riesgo de Desastre".'
    - 'RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.Req-Generales[0].Enunciado=Req-1:
      Formulación del proyecto conforme a:'
    - RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.Req-Generales[0].ID=Req-1
    - 'RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.Req-Generales[1].Enunciado=Req-2:
      Considerar estimaciones e información de fuentes secundarias.'
    - RIS_Edificacion_Publica_2024.Postulacion_Prefactibilidad_Factibilidad.Req-Generales[1].ID=Req-2
    - RIS_Edificacion_Publica_2024.Prop-Doc=Establecer requisitos para proyectos de
      edificación pública que buscan ampliar capacidad y mejorar dependencias institucionales.
    - Source.Ctx_Required[0]=https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf
    - Source.Primary-Source=kb_gn_010_ris.md (sección RIS-EDPUB-2024)
    - Status=Draft
    - Version=1.0.0
    - _manifest.compatibility.breaking_changes_from=null
    - _manifest.compatibility.min_consumer_version=1.0.0
    - _manifest.dependencies.requires[0].reason=KODA/Spec format compliance
    - _manifest.dependencies.requires[0].urn=urn:knowledge:koda:core:spec:1.0.0
    - _manifest.dependencies.requires[1].reason=Transformation methodology reference
    - _manifest.dependencies.requires[1].urn=urn:knowledge:koda:core:transform:1.0.0
    - _manifest.federation.license=Institutional Use
    - _manifest.federation.visibility=internal
    - _manifest.provenance.created_at=2025-11-28
    - _manifest.provenance.created_by=FS
    - _manifest.provenance.last_modified_at=2025-11-28
    - _manifest.provenance.signature=null
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/kb_gn_010_ris_edpub_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:ris-edpub:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# RIS Edificación Pública (SNI 2024)
## ID
GN-RIS-EDPUB-2024-01

## Version
1.0.0

## Status
Draft

## Human Creator
FS

## Human Editor
FS

## Model Collaborator
KODA-TRANSFORMER

## Creation Date
2025-11-28

## Modification Date
2025-11-28

## Ctx
Requisitos de información para proyectos de Edificación Pública que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-EDPUB-2024)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-EDPUB-2024-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing):
  Act->Action, Cause->Cause, Cond->Condition, Cpt->Concept, Ctx->Context,
  Def->Definition, Dep->Dependency, Dest->Destination, Dln->Deadline,
  Ex->Example, Fnd->Foundation, ID->ID, Instr->Instruction,
  Just->Justification, Mech->Mechanism, Mssn->Mission, Mdl->Model,
  Nat->Nature, Obj->Objective, Proc->Process, Prohib->Prohibition,
  Purp->Purpose, Ref->Reference, Req->Requirement, Res->Result,
  Resp->Responsible, Src->Source, Warn->Warning.

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. External documents and legal sources are mentioned as contextual information under Ctx:, Ctx_Required:, Ctx_Optional: or Src:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## RIS Edificacion Publica 2024
### ID
RIS-EDPUB-2024-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_-_Proyectos_de_Edificacion_publica_-_26-04-2024.pdf
### Prop Doc
Establecer requisitos para proyectos de edificación pública que buscan ampliar capacidad y mejorar dependencias institucionales.
### Alcance
#### ID
RIS-EDPUB-2024-ALCANCE-01
#### Prop
Ampliar capacidad y mejorar dependencias institucionales.
#### Meta
Optimizar cumplimiento de actividades organizacionales.
#### Nota Dudas
Aspectos no tratados se resuelven por Jefatura de la División de Evaluación Social de Inversiones.
### Orientaciones Sectoriales
#### ID
RIS-EDPUB-2024-ORIENTACIONES-SECTORIALES-01
#### Arquitectura Sustentable
#### Req Diseño
Integrado (climatización, iluminación, sanitario, aguas lluvias, estructuras, redes, energías renovables, paisajismo).
#### Prop
Uso eficiente de energía, agua y otros recursos.
#### Meta
Minimizar impacto ambiental y dependencia de hidrocarburos.
#### Accesibilidad
#### Req
Proveer libre acceso y circulación para personas con capacidades diferentes.
#### Normativa
- Ley N°20.530, art. 13.
- DS N° 47 de 1992 (Ordenanza General de Urbanismo y Construcciones - OGUC).
- DS N° 50 de 2015 (MINVU).
#### Competencia Analisis
#### Nivel Regional Comunal
Análisis por Secretarías Regionales Ministeriales de Desarrollo Social.
#### Nivel Nacional
Análisis conjunto con Nivel Central del MDSF.
#### Clasificacion BIP
#### Sector
Multisectorial.
#### Subsector
Administración Multisector.
#### Descriptor
Edificación Pública.
### Postulacion Prefactibilidad Factibilidad
#### ID
RIS-EDPUB-2024-POSTULACION-PREFACT-FACT-01
#### Req Generales
-
  #### ID
  Req-1
  #### Enunciado
  Req-1: Formulación del proyecto conforme a:
  #### Detalle
  - Metodologia-1: "Metodología de Edificación Pública".
  - Metodologia-2: "Metodología de Riesgo de Desastre".
-
  #### ID
  Req-2
  #### Enunciado
  Req-2: Considerar estimaciones e información de fuentes secundarias.
### Postulacion Diseno
#### ID
RIS-EDPUB-2024-POSTULACION-DISEÑO-01
#### Req Generales
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Formulación del proyecto conforme a requisitos de información para etapa de diseño. |
| Req-2 | Req-2: Uso de "Metodología de Edificación Pública" y "Metodología de Riesgo de Desastre". |
| Req-3 | Req-3: Proyección de dotación de servicio (demanda proyectada de equipos, equipamiento y m² según necesidades, misión del servicio y carga de trabajo). |
| Req-4 | Req-4: Acreditación situación legal del inmueble (según "Requisitos Genéricos sobre las Propiedades en que se Proyectan Edificaciones"). |
| Req-5 | Req-5: Cumplimiento de "Antecedentes Técnicos Requeridos para Proyectos que Consideran Edificación". |
| Req-6 | Req-6: Carta de compromiso de traslado al nuevo recinto por cada servicio involucrado. |
| Req-7 | Req-7: Documento firmado por responsables de la administración de la infraestructura (jefes de servicios participantes). |
### Postulacion Ejecucion
#### ID
RIS-EDPUB-2024-POSTULACION-EJECUCION-01
#### Req Generales
-
  #### ID
  Req-1
  #### Enunciado
  Req-1: Formulación del proyecto conforme a "Metodología de Edificación Pública" y "Metodología de Riesgo de Desastre" (para etapa de ejecución).
-
  #### ID
  Req-2
  #### Enunciado
  Req-2: Cumplir requisitos de etapa de diseño (aplicable si se concentra funcionamiento de varios servicios públicos).
  #### Nota
  Nota: Aplica si no se postuló a Diseño en SNI.
-
  #### ID
  Req-3
  #### Enunciado
  Req-3: Presentar antecedentes según "Antecedentes Técnicos Requeridos para Proyectos que Consideran Edificación" para ejecución.
-
  #### ID
  Req-4
  #### Enunciado
  Req-4: Cuadro comparativo entre programa arquitectónico aprobado y diseño resultante, con justificación de diferencias.
-
  #### ID
  Req-5
  #### Enunciado
  Req-5: Cronograma de Actividades o Carta Gantt.
### Postulacion Diseno Ejecucion Conjunta
#### ID
RIS-EDPUB-2024-POSTULACION-DISEÑO-EJEC-CONJUNTA-01
#### Req Generales
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Formulación del proyecto conforme a requisitos de información para etapa de diseño (con estimaciones de fuentes secundarias y usando metodologías correspondientes). |
| Req-2 | Req-2: Presentar lo solicitado en el "Instructivo para postulación de proyectos a etapa de ejecución con diseño referencial". |
| Req-3 | Req-3: Incluir consideraciones de eficiencia energética y otros aspectos pertinentes contenidos en los "Antecedentes Técnicos Requeridos para Proyectos que Consideran Edificación". |

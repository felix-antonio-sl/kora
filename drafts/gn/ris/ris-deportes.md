---
_manifest:
  urn: urn:gn:kb:ris-deportes
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- deportes
- infraestructura
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml: 5989871f8a4ad10e44d060d4f8547ae81b9b4f9a7e9ad5c54891275b83fbcf1f
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.21
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 13
    meat_count: 117
    fat_count: 0
    preserved_facts:
    - Creation-Date=2025-11-28
    - Ctx=Requisitos y criterios de evaluación para proyectos de infraestructura deportiva
      que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.
    - Human-Creator=FS
    - Human-Editor=FS
    - ID=GN-RIS-DEPORTES-2024-01
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
    - LLM_Parsing_Instructions.ID=KODA-LLM-PARSER-GN-RIS-DEPORTES-2024-01
    - LLM_Parsing_Instructions.Prohib=Using for artifact creation or translation.
    - LLM_Parsing_Instructions.Req=Mandatory block following Metadata.
    - Model-Collaborator=KODA-TRANSFORMER
    - Modification-Date=2025-11-28
    - 'RIS_Deportes_2024.Alcance.Def-Aumento-Oferta[0]=Criterio: Incremento en número
      de deportistas atendidos simultáneamente.'
    - 'RIS_Deportes_2024.Alcance.Def-Aumento-Oferta[1]=Exclusion: No se considera
      aumento si solo mejora confort (ej: iluminación, camarines) sin intensificar
      uso.'
    - RIS_Deportes_2024.Alcance.Evaluacion-Metodologia=Metodología de Formulación
      y Evaluación de Proyectos de Infraestructura Deportiva.
    - RIS_Deportes_2024.Alcance.ID=RIS-DEPORTES-2024-ALCANCE-01
    - 'RIS_Deportes_2024.Alcance.Modalidades-Deportivas[0]=Modalidad-1: Deporte formativo.'
    - 'RIS_Deportes_2024.Alcance.Modalidades-Deportivas[1]=Modalidad-2: Deporte recreativo.'
    - 'RIS_Deportes_2024.Alcance.Modalidades-Deportivas[2]=Modalidad-3: Deporte competitivo.'
    - 'RIS_Deportes_2024.Alcance.Modalidades-Deportivas[3]=Modalidad-4: Deporte de
      alto rendimiento.'
    - 'RIS_Deportes_2024.Alcance.Modalidades-Deportivas[4]=Nota-Clasificacion: Un
      proyecto puede atender varias modalidades. Se clasifica por tamaño/estándar
      o costo.'
    - RIS_Deportes_2024.Alcance.Proyectos-Deportivos=Edificación para práctica física
      y deportiva.
    - 'RIS_Deportes_2024.Alcance.Proyectos-Formacion-Educacional[0].Enunciado=Req-1:
      Integrados en establecimientos educacionales.'
    - RIS_Deportes_2024.Alcance.Proyectos-Formacion-Educacional[0].ID=Req-1
    - 'RIS_Deportes_2024.Alcance.Proyectos-Formacion-Educacional[1].Enunciado=Req-2:
      Deben ser abiertos a la comunidad.'
    - RIS_Deportes_2024.Alcance.Proyectos-Formacion-Educacional[1].ID=Req-2
    - 'RIS_Deportes_2024.Alcance.Proyectos-Formacion-Educacional[2].Enunciado=Req-3:
      Operables de forma autónoma (administración, financiamiento, accesos propios
      a vía pública).'
    - RIS_Deportes_2024.Alcance.Proyectos-Formacion-Educacional[2].ID=Req-3
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alta_Competencia.Caracteristicas[0]=Cond-Aforo-Cerradas:
      >1.500 personas.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alta_Competencia.Caracteristicas[1]=Cond-Aforo-Abiertas:
      >2.500 personas.'
    - RIS_Deportes_2024.Criterios_Evaluacion.Alta_Competencia.Evaluacion[0]=Prorrateo
      similar a escala mayor.
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alta_Competencia.Evaluacion[1]=Criterio-CAE-Deportista:
      hasta 0,12 UTM.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alta_Competencia.Evaluacion[2]=Criterio-Espectadores:
      Análisis mediante indicadores VAN y TIR.'
    - RIS_Deportes_2024.Criterios_Evaluacion.Alta_Competencia.ID=RIS-DEPORTES-2024-EVALUACION-ALTA-COMPETENCIA-01
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Evaluacion[0]=Req:
      Respaldados por políticas y autoridades deportivas nacionales.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Evaluacion[1]=Criterio-CAE-Deportista-CER:
      Puede incrementarse hasta 30% con enfoque en alto rendimiento.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Evaluacion[2]=Criterio-CAE-Deportista-CAR:
      Sin limitación.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Evaluacion[3]=Criterio-Espectadores-CAR:
      Evaluados con VAN y TIR.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Evaluacion[4]=Rec:
      Uso de tecnologías para optimizar costos de operación y mantención.'
    - RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.ID=RIS-DEPORTES-2024-EVALUACION-ALTO-RENDIMIENTO-01
    - RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Niveles[0]=Regional
      (CER).
    - RIS_Deportes_2024.Criterios_Evaluacion.Alto_Rendimiento.Niveles[1]=Nacional
      (CAR).
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Mayor-Costo-Eficiencia-Deportista-Espectador[0]=Cond-Aforo-Cerradas:
      hasta 1.500 personas.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Mayor-Costo-Eficiencia-Deportista-Espectador[1]=Cond-Aforo-Abiertas:
      hasta 2.500 personas.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Mayor-Costo-Eficiencia-Deportista-Espectador[2]=Criterio-Evaluacion-Separada:
      CAE-Deportista 0,075 UTM; CAE-Espectador 0,11 UTM.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Mediana-Costo-Eficiencia-Deportista[0]=Cond-1:
      Inversión en instalaciones existentes.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Mediana-Costo-Eficiencia-Deportista[1]=Cond-2:
      Aforo limitado (<500 en cerrados, <1.500 en abiertos).'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Mediana-Costo-Eficiencia-Deportista[2]=Criterio-CAE-Deportista:
      Costo máximo 0,075 UTM.'
    - 'RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.Escala-Menor-Analisis-Simplificado[0]=Cond:
      Proyectos de 5.000 a 8.000 UTM sin aumento de oferta.'
    - RIS_Deportes_2024.Criterios_Evaluacion.Formativo_Recreativo.ID=RIS-DEPORTES-2024-EVALUACION-FORMATIVO-RECREATIVO-01
    - RIS_Deportes_2024.Criterios_Evaluacion.ID=RIS-DEPORTES-2024-EVALUACION-01
    - RIS_Deportes_2024.Criterios_Evaluacion.Optimizacion.Ejemplos=Iluminación LED,
      generadores, protección de canchas, calderas, deshumidificación, paneles fotovoltaicos,
      control de acceso.
    - RIS_Deportes_2024.Criterios_Evaluacion.Optimizacion.ID=RIS-DEPORTES-2024-EVALUACION-OPTIMIZACION-01
    - RIS_Deportes_2024.Criterios_Evaluacion.Optimizacion.Prop=Mejorar eficiencia
      operativa y generar ahorros o ingresos reales.
    - RIS_Deportes_2024.Fuente-URL=https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf
    - RIS_Deportes_2024.ID=RIS-DEPORTES-2024-META-01
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.Areas-Espectadores.Uso-Presencial[0]=Accesos,
      graderías, circulaciones, boleterías, puntos de venta, baños, estacionamientos.
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.Areas-Espectadores.Uso-Transmision[0]=Espacios
      para trabajo radial, televisivo, periodístico (puntos de prensa, salas especializadas,
      ascensores especiales).
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.Areas-Mixtas[0]=Administración,
      seguridad, iluminación, urbanización, muros, losas, estacionamientos.
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.Areas-Uso-Deportivo.Componentes-Esenciales[0]=Espacios
      de juego (dimensiones, altura requerida).
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.Areas-Uso-Deportivo.Componentes-Esenciales[1]=Equipos,
      equipamientos, instalaciones accesorias (camarines, baños, áreas de ejercicios,
      bodegas, oficinas, primeros auxilios, accesos, circulaciones, estacionamientos).
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.Areas-Uso-Deportivo.Componentes-Opcionales-Alto-Rendimiento[0]=Habitaciones,
      alimentación, lavandería, estudios, entretención, atención especializada física/psicológica.
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Componentes_Instalaciones_Deportivas.ID=RIS-DEPORTES-2024-ORIENTACIONES-COMPONENTES-01
    - RIS_Deportes_2024.Orientaciones_Sectoriales.Desglose_Presupuestos_Prorrateo.ID=RIS-DEPORTES-2024-ORIENTACIONES-PRORRATEO-01
    - 'RIS_Deportes_2024.Orientaciones_Sectoriales.Desglose_Presupuestos_Prorrateo.Paso-A-Superficies-Atribuibles[0]=Accion:
      Clasificar áreas según destino (deportistas, espectadores, mixtas).'
    - 'RIS_Deportes_2024.Orientaciones_Sectoriales.Desglose_Presupuestos_Prorrateo.Paso-A-Superficies-Atribuibles[1]=Regla-Mixtas:
      Repartir 50% de superficie a componente deportista y 50% a componente espectador.'
    - 'RIS_Deportes_2024.Orientaciones_Sectoriales.Desglose_Presupuestos_Prorrateo.Paso-B-Costo-Medio-Superficie[0]=Accion-1:
      Extraer partidas del presupuesto atribuibles a cada componente.'
    - 'RIS_Deportes_2024.Orientaciones_Sectoriales.Desglose_Presupuestos_Prorrateo.Paso-B-Costo-Medio-Superficie[1]=Accion-2:
      Sumar costos prorrateados de áreas mixtas y partidas directas.'
    - 'RIS_Deportes_2024.Orientaciones_Sectoriales.Desglose_Presupuestos_Prorrateo.Paso-B-Costo-Medio-Superficie[2]=Prop:
      Permite calcular indicadores CAE diferenciados (deportista y espectador).'
    - RIS_Deportes_2024.Orientaciones_Sectoriales.ID=RIS-DEPORTES-2024-ORIENTACIONES-01
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[0].Enunciado=Req-1:
      Formulación y evaluación (usar "Planilla evaluación-sector deporte" o "Metodología
      General").'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[0].ID=Req-1
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[1].Enunciado=Req-2:
      Antecedentes técnicos (según "Antecedentes Técnicos para Proyectos que consideran
      Edificación").'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[1].ID=Req-2
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[2].Enunciado=Req-3:
      Certificación de propiedad del terreno.'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[2].ID=Req-3
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[3].Enunciado=Req-4:
      Presupuesto detallado de consultoría de diseño (incluye personal, horas, gastos
      adm.).'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[3].ID=Req-4
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[4].Enunciado=Req-5:
      Términos de referencia para la consultoría.'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[4].ID=Req-5
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[5].Enunciado=Req-6:
      Carta Gantt (incluye licitación, contratación, revisión).'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[5].ID=Req-6
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[6].Enunciado=Req-7:
      Calendario de financiamiento (incluye asignaciones y gastos adm.).'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[6].ID=Req-7
    - 'RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[7].Enunciado=Req-8:
      Plan de gestión (según instrucciones del "Plan de Gestión").'
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.Antecedentes-Req[7].ID=Req-8
    - RIS_Deportes_2024.Postulacion_Etapas.Diseno.ID=RIS-DEPORTES-2024-POSTULACION-DISEÑO-01
    - 'RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[0].Enunciado=Req-1:
      Presentación directa a ejecución (usando "Planilla evaluación-sector deporte"
      o "Metodología General").'
    - RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[0].ID=Req-1
    - 'RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[1].Enunciado=Req-2:
      Antecedentes técnicos (según "Antecedentes Técnicos para Proyectos que consideran
      Edificación").'
    - RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[1].ID=Req-2
    - 'RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[2].Enunciado=Req-3:
      Listado valorizado de equipamiento y equipos (con especificaciones).'
    - RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[2].ID=Req-3
    - 'RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[3].Enunciado=Req-4:
      Plan de gestión (según "Plan de Gestión").'
    - RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.Antecedentes-Req[3].ID=Req-4
    - RIS_Deportes_2024.Postulacion_Etapas.Ejecucion.ID=RIS-DEPORTES-2024-POSTULACION-EJECUCION-01
    - RIS_Deportes_2024.Postulacion_Etapas.ID=RIS-DEPORTES-2024-POSTULACION-01
    - RIS_Deportes_2024.Postulacion_Etapas.Prefactibilidad_Factibilidad.ID=RIS-DEPORTES-2024-POSTULACION-PREFACT-FACT-01
    - RIS_Deportes_2024.Postulacion_Etapas.Prefactibilidad_Factibilidad.Req=Seguir
      Normas, Instrucciones y Procedimientos (NIP) de Inversión Pública.
    - RIS_Deportes_2024.Prop-Doc=Establecer requisitos y criterios de evaluación para
      proyectos de infraestructura deportiva.
    - Source.Ctx_Required[0]=https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf
    - Source.Primary-Source=kb_gn_010_ris.md (sección RIS-DEPORTES-2024)
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
    - _manifest.resolution.canonical_url=file://knowledge/domains/gn/kb_gn_010_ris_deportes_koda.yml
    - _manifest.urn=urn:knowledge:gorenuble:gn:ris-deportes:1.0.0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
---

# RIS Infraestructura Deportiva (SNI 2024)
## ID
GN-RIS-DEPORTES-2024-01

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
Requisitos y criterios de evaluación para proyectos de infraestructura deportiva que ingresan al Sistema Nacional de Inversiones (SNI), versión 2024.

## Source
### Primary Source
kb_gn_010_ris.md (sección RIS-DEPORTES-2024)
### Ctx Required
- https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-GN-RIS-DEPORTES-2024-01
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


## RIS Deportes 2024
### ID
RIS-DEPORTES-2024-META-01
### Fuente URL
https://sni.gob.cl/storage/docs/RIS__Proyectos_Deportes_2024.pdf
### Prop Doc
Establecer requisitos y criterios de evaluación para proyectos de infraestructura deportiva.
### Alcance
#### ID
RIS-DEPORTES-2024-ALCANCE-01
#### Proyectos Deportivos
Edificación para práctica física y deportiva.
#### Evaluacion Metodologia
Metodología de Formulación y Evaluación de Proyectos de Infraestructura Deportiva.
#### Modalidades Deportivas
- Modalidad-1: Deporte formativo.
- Modalidad-2: Deporte recreativo.
- Modalidad-3: Deporte competitivo.
- Modalidad-4: Deporte de alto rendimiento.
- Nota-Clasificacion: Un proyecto puede atender varias modalidades. Se clasifica por tamaño/estándar o costo.
#### Proyectos Formacion Educacional
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Integrados en establecimientos educacionales. |
| Req-2 | Req-2: Deben ser abiertos a la comunidad. |
| Req-3 | Req-3: Operables de forma autónoma (administración, financiamiento, accesos propios a vía pública). |
#### Def Aumento Oferta
- Criterio: Incremento en número de deportistas atendidos simultáneamente.
- Exclusion: No se considera aumento si solo mejora confort (ej: iluminación, camarines) sin intensificar uso.
### Orientaciones Sectoriales
#### ID
RIS-DEPORTES-2024-ORIENTACIONES-01
#### Componentes Instalaciones Deportivas
#### ID
RIS-DEPORTES-2024-ORIENTACIONES-COMPONENTES-01
#### Areas Uso Deportivo
#### Componentes Esenciales
- Espacios de juego (dimensiones, altura requerida).
- Equipos, equipamientos, instalaciones accesorias (camarines, baños, áreas de ejercicios, bodegas, oficinas, primeros auxilios, accesos, circulaciones, estacionamientos).
#### Componentes Opcionales Alto Rendimiento
- Habitaciones, alimentación, lavandería, estudios, entretención, atención especializada física/psicológica.
#### Areas Espectadores
#### Uso Presencial
- Accesos, graderías, circulaciones, boleterías, puntos de venta, baños, estacionamientos.
#### Uso Transmision
- Espacios para trabajo radial, televisivo, periodístico (puntos de prensa, salas especializadas, ascensores especiales).
#### Areas Mixtas
- Administración, seguridad, iluminación, urbanización, muros, losas, estacionamientos.
#### Desglose Presupuestos Prorrateo
#### ID
RIS-DEPORTES-2024-ORIENTACIONES-PRORRATEO-01
#### Paso A Superficies Atribuibles
- Accion: Clasificar áreas según destino (deportistas, espectadores, mixtas).
- Regla-Mixtas: Repartir 50% de superficie a componente deportista y 50% a componente espectador.
#### Paso B Costo Medio Superficie
- Accion-1: Extraer partidas del presupuesto atribuibles a cada componente.
- Accion-2: Sumar costos prorrateados de áreas mixtas y partidas directas.
- Prop: Permite calcular indicadores CAE diferenciados (deportista y espectador).
### Criterios Evaluacion
#### ID
RIS-DEPORTES-2024-EVALUACION-01
#### Formativo Recreativo
#### ID
RIS-DEPORTES-2024-EVALUACION-FORMATIVO-RECREATIVO-01
#### Escala Menor Analisis Simplificado
- Cond: Proyectos de 5.000 a 8.000 UTM sin aumento de oferta.
#### Escala Mediana Costo Eficiencia Deportista
- Cond-1: Inversión en instalaciones existentes.
- Cond-2: Aforo limitado (<500 en cerrados, <1.500 en abiertos).
- Criterio-CAE-Deportista: Costo máximo 0,075 UTM.
#### Escala Mayor Costo Eficiencia Deportista Espectador
- Cond-Aforo-Cerradas: hasta 1.500 personas.
- Cond-Aforo-Abiertas: hasta 2.500 personas.
- Criterio-Evaluacion-Separada: CAE-Deportista 0,075 UTM; CAE-Espectador 0,11 UTM.
#### Alta Competencia
#### ID
RIS-DEPORTES-2024-EVALUACION-ALTA-COMPETENCIA-01
#### Caracteristicas
- Cond-Aforo-Cerradas: >1.500 personas.
- Cond-Aforo-Abiertas: >2.500 personas.
#### Evaluacion
- Prorrateo similar a escala mayor.
- Criterio-CAE-Deportista: hasta 0,12 UTM.
- Criterio-Espectadores: Análisis mediante indicadores VAN y TIR.
#### Alto Rendimiento
#### ID
RIS-DEPORTES-2024-EVALUACION-ALTO-RENDIMIENTO-01
#### Niveles
- Regional (CER).
- Nacional (CAR).
#### Evaluacion
- Req: Respaldados por políticas y autoridades deportivas nacionales.
- Criterio-CAE-Deportista-CER: Puede incrementarse hasta 30% con enfoque en alto rendimiento.
- Criterio-CAE-Deportista-CAR: Sin limitación.
- Criterio-Espectadores-CAR: Evaluados con VAN y TIR.
- Rec: Uso de tecnologías para optimizar costos de operación y mantención.
#### Optimizacion
#### ID
RIS-DEPORTES-2024-EVALUACION-OPTIMIZACION-01
#### Prop
Mejorar eficiencia operativa y generar ahorros o ingresos reales.
#### Ejemplos
Iluminación LED, generadores, protección de canchas, calderas, deshumidificación, paneles fotovoltaicos, control de acceso.
### Postulacion Etapas
#### ID
RIS-DEPORTES-2024-POSTULACION-01
#### Prefactibilidad Factibilidad
#### ID
RIS-DEPORTES-2024-POSTULACION-PREFACT-FACT-01
#### Req
Seguir Normas, Instrucciones y Procedimientos (NIP) de Inversión Pública.
#### Diseno
#### ID
RIS-DEPORTES-2024-POSTULACION-DISEÑO-01
#### Antecedentes Req
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Formulación y evaluación (usar "Planilla evaluación-sector deporte" o "Metodología General"). |
| Req-2 | Req-2: Antecedentes técnicos (según "Antecedentes Técnicos para Proyectos que consideran Edificación"). |
| Req-3 | Req-3: Certificación de propiedad del terreno. |
| Req-4 | Req-4: Presupuesto detallado de consultoría de diseño (incluye personal, horas, gastos adm.). |
| Req-5 | Req-5: Términos de referencia para la consultoría. |
| Req-6 | Req-6: Carta Gantt (incluye licitación, contratación, revisión). |
| Req-7 | Req-7: Calendario de financiamiento (incluye asignaciones y gastos adm.). |
| Req-8 | Req-8: Plan de gestión (según instrucciones del "Plan de Gestión"). |
#### Ejecucion
#### ID
RIS-DEPORTES-2024-POSTULACION-EJECUCION-01
#### Antecedentes Req
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Presentación directa a ejecución (usando "Planilla evaluación-sector deporte" o "Metodología General"). |
| Req-2 | Req-2: Antecedentes técnicos (según "Antecedentes Técnicos para Proyectos que consideran Edificación"). |
| Req-3 | Req-3: Listado valorizado de equipamiento y equipos (con especificaciones). |
| Req-4 | Req-4: Plan de gestión (según "Plan de Gestión"). |

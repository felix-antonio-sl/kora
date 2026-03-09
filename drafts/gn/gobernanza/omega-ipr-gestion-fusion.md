---
_manifest:
  urn: urn:gn:kb:omega-ipr-gestion-fusion
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- finanzas-publicas
- gestion-ipr
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_omega_ipr_gestion_fusion.yml: 3ab92b1ccdacc60070e0a8796dd54bb600e956cf0e3f6a4b50b606bc23610385
    source_type: ontology_yaml
    transformation_mode: derive_ttl_scope
    fs: 100
    cr: 10.76
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Fusion semantica IPR/Gestion; requiere validacion de alcance.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 8
    meat_count: 637
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__omega-ipr-gestion-fusion.md.json
---

# Ontología Ω-IPR: Gestión y Fusión de Financiamiento

## Scope
Fusion semantica IPR/Gestion; requiere validacion de alcance.

## Resumen
- Tipo: Ω-Ontology
- Schema: `Omega schema 2.0.0`
- Basado en: 3 artefactos
- Omega objects: 5

## Ω-IPR
- Tipo: Ω-Object
- Descripción: Intervención Pública Regional: unidad atómica de financiamiento del GORE
- Subtipos: 6
  - `Ω-IDI` Iniciativa de Inversión
  - `Ω-PPR` Programa Público Regional
  - `Ω-ESTUDIO` Estudio Básico
  - `Ω-ANF` Adquisición de Activos No Financieros
  - `Ω-CONSERVACION` Proyecto de Conservación

## Ω-MECANISMO
- Tipo: Ω-Object (Fiber Index)
- Descripción: Vía de financiamiento que determina reglas, proceso y sistema de evaluación
- Fibras proyectos: 7
  - `MEC-SNI-GENERAL` SNI General
  - `MEC-FRIL` Fondo Regional de Infraestructura Local
  - `MEC-C33-CONSERVACION` Circular 33 - Conservación
  - `MEC-C33-ANF` Circular 33 - Activos No Financieros
  - `MEC-C33-ESTUDIOS` Circular 33 - Estudios Básicos
- Fibras programas: 5
  - `MEC-G06-DIRECTA` Glosa 06 - Ejecución Directa
  - `MEC-TRANSFER-PUB` Transferencia a Entidad Pública
  - `MEC-SUBV8` 8% FNDR - Vinculación Comunitaria
  - `MEC-FRPD-PROGRAMA` FRPD - Programas Productivos
  - `MEC-EMERGENCIA` Ayudas Tempranas y Emergencias

## Ω-DICTAMEN
- Tipo: Ω-Object (Effect Constructor)
- Descripción: Resultado de evaluación según sistema aplicable
- Sistemas: 4
  - `RATE` Resultado Análisis Técnico-Económico
  - `RF` Recomendación Favorable
  - `ITF` Informe Técnico Favorable
  - `CONCURSO` Evaluación Competitiva por Mérito

## Ω-ACTOR
- Tipo: Ω-Object (Agent)
- Descripción: Agentes que participan en el ciclo de vida IPR
- Autoridades GORE: 2
  - `GOBERNADOR` Máxima autoridad regional, firma actos administrativos
  - `ADMIN-REGIONAL` Administrador/a Regional, coordinación operativa
- Divisiones GORE: 7
  - `DIPIR` División de Presupuesto e Inversión Regional
  - `DIPLADE` División de Planificación y Desarrollo Regional
  - `DAF` División de Administración y Finanzas
  - `PREINVERSION` Jefatura/Depto. de Preinversión (DIPIR)
  - `PRESUPUESTO` Depto. de Presupuesto (DAF)
- Instancias colegiadas: 5
  - `CDR` Comité Directivo Regional (filtro pertinencia)
  - `CORE` Consejo Regional (aprobación financiamiento)
  - `COMITE-PERTINENCIA` Evaluación de pertinencia estratégica
  - `COMITE-EVALUADOR` Evaluación competitiva (concursos)
  - `JUNTA-CALIFICADORA` Calificación de funcionarios
- Organismos externos: 7
  - `MDSF` Ministerio de Desarrollo Social y Familia (RATE)
  - `SES` Subsecretaría de Evaluación Social
  - `DIPRES` Dirección de Presupuestos (RF, visaciones)
  - `CGR` Contraloría General (Toma de Razón, SISREC)
  - `SUBDERE` Subsecretaría de Desarrollo Regional (FRIL)
- Ejecutores: 8
  - `UT-RECEPTORA` Unidad Técnica Receptora del convenio
  - `MUNICIPALIDAD` Ejecutor FRIL y transferencias municipales
  - `SERVICIO-PUBLICO` Servicio público receptor
  - `UNIVERSIDAD` Universidad estatal/acreditada
  - `ORG-COMUNITARIA` Organización comunitaria (8%)
- Roles operativos: 6
  - `UNIDAD-FORMULADORA` Entidad que formula y presenta la IPR
  - `SUPERVISOR-GORE` Profesional que supervisa ejecución
  - `ANALISTA-DIPIR` Analista de preinversión
  - `ANALISTA-MDSF` Evaluador externo SNI
  - `SECRETARIO-CORE` Emite certificados de acuerdo CORE

## Ω-DOCUMENTO
- Tipo: Ω-Object
- Instancias: 9
  - ``
  - ``
  - ``
  - ``
  - ``

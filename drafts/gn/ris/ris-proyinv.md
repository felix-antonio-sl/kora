---
_manifest:
  urn: urn:gn:kb:ris-proyinv
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- sni
- inversiones
- proyectos-inversion
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_proyinv_koda.yml: 2ff418c2537e09c49caf194bbbe8fbc0320a4f95c3b5a1ab0f146a993f46e33f
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.09
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 2
    meat_count: 88
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-proyinv.md.json
---

# RIS Genéricas — Proyectos de Inversión (SNI 2023)
## Source
### Contexto requerido
- https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
- https://sni.gob.cl/requisitos-de-informacion-por-sector

## RIS Proyectos Inversion 2023
### Fuente URL
https://sni.gob.cl/storage/docs/RIS_genericas_para_proyectos_de_inversion_2023.pdf
### Prop Doc
Establecer requisitos de información para la formulación y presentación de Proyectos de Inversión en sus distintas fases y etapas.
### Ciclo Vida Proyecto
#### Estados
- Estado-1-Preinversion: Preparación y evaluación para determinar viabilidad.
- Estado-2-Inversion: Diseño y ejecución de obras.
- Estado-3-Operacion: Puesta en marcha (marcha blanca) y operación en régimen.
#### Etapas Preinversion
- Etapa-1-Perfil
- Etapa-2-Prefactibilidad
- Etapa-3-Factibilidad
#### Etapas Inversion
- Etapa-1-Diseño
- Etapa-2-Ejecucion
#### Etapas Operacion
- Etapa-1-Puesta-en-marcha
- Etapa-2-Operacion-en-regimen
### Fase Preinversion
#### Estudio Preinversional
#### Cont Req
- Item-1: Perfil del proyecto (cuando se postula a prefactibilidad).
- Item-2: Respaldo con metodología aplicable (general o específica).
#### TDR Estudio
#### Prop
Definir información básica y actividades del estudio.
#### Cont Req
- Antecedentes-Generales/Item-1: Estudios previos (nombre, consultora, año, resumen, versión más reciente).
- Antecedentes-Generales/Item-2: Estimación de costos de inversión.
- Identificacion-Problema: Definición del problema.
- Objetivos: Generales y específicos.
- Diag-1: Diagnóstico situación actual.
- Var-1: Definición y análisis de variables (oferta, demanda, proyecciones, brechas).
- Sol-1: Análisis de alternativas de solución.
- Opt-1: Análisis de tamaño óptimo, localización y momento de inversión.
- Cost-Ben-1: Identificación y valorización de costos y beneficios (directos e indirectos).
- Eval-1: Evaluación técnico-económica de cada alternativa.
- Sel-1: Selección mejor alternativa (con profundización en etapa de factibilidad).
- Res-1: Resumen y conclusiones.
#### Cronograma Actividades
#### Formato
Carta Gantt.
#### Detalle Req
Fuentes de financiamiento, especificación de jornada (completa, parcial, etc.).
#### Resultados Esperados
#### Enfoque
Vinculados directamente a contenidos y objetivos del estudio.
#### Implicancias Ambientales
#### Requisitos
Evaluación de impactos ambientales del proyecto.
#### Presupuesto Detallado
#### Formato
Desglose por asignaciones.
#### Cont Req
- Asig-Gastos-Administrativos/Item-1: Consultorías, personal (profesionales, técnicos, administrativos).
- Asig-Gastos-Administrativos/Item-2: Otros gastos administrativos, gastos generales, utilidades.
- Asig-Consultorias/Item-1: Costo total, desagregando perfiles y unidades de medida (horas o unidades).
#### Obs Req
- Obs-1: Incluir costos de estudios ambientales (EIA, DIA) si corresponde.
- Obs-2: Costo total debe incluir impuestos.
- Obs-3: Alinear a Clasificador Presupuestario (ficha IDI).
### Fase Inversion
#### Etapa Diseno
#### Docs Base Req
- Doc-1: Estudio preinversional (perfil, prefactibilidad o factibilidad).
- Doc-2: Programa arquitectónico (según especificaciones sectoriales).
- Doc-3: Plano de emplazamiento y de zona (incluye áreas de influencia y servicios).
#### Cronograma Req
Carta Gantt con duración en meses.
#### Calendario Inv Req
Detalle por asignaciones (incluir monto para terreno si aplica).
#### TDR Consultoria Req
Para contratación de especialistas (arquitectura, ingeniería, especialidades).
#### Presupuesto Detallado Req
#### Desglose Asignaciones
- Gastos-Administrativos: Consultorías (incluye personal desagregado por nivel y otros gastos: materiales, insumos, difusión).
- Gastos-Administrativos: Revisores independientes (según normativa).
#### Obs Req
- Unidades de medida: horas (RRHH) o unidades globales (otros).
- Incluir impuestos.
#### Etapa Ejecucion
#### Docs Req
- Doc-1: Estudio preinversional actualizado con resultados de etapa de diseño.
- Doc-2: Resultados completos de diseño (planos, especificaciones técnicas, presupuestos visados).
#### Soportes Req
Cotizaciones para equipos y equipamiento.
#### Cronograma Act Req
Detallado por actividad, con estimaciones de tiempo y fuentes de financiamiento.
#### Presupuesto Proyecto Req
#### Desglose Asignaciones
- Gastos-Administrativos
- Consultorias
- Terrenos (incluye expropiación o adquisición)
- Obras-Civiles (incluye servidumbres, redes, etc.)
- Equipamiento (mobiliario integrado al proyecto)
- Equipos (máquinas, hardware, software)
- Vehiculos (si forman parte del proyecto)
- Otros-Gastos (gastos adicionales no contemplados)
#### Obs Req
- Unidades de medida varían (horas, m², N° unidades, global, etc.).
- Costo total debe incluir impuestos.
#### Fichas Registros Req
- Coherencia con antecedentes de respaldo y fichas del IDI.
### Documentos Apoyo
#### Req Especificos
| ID | Enunciado |
| --- | --- |
| Req-1 | Req-1: Requisitos genéricos sobre propiedades en edificaciones. |
| Req-2 | Req-2: Antecedentes técnicos para proyectos con edificación. |
| Req-3 | Req-3: Instructivo para proyectos que postulan a Pago Contra Recepción. |
#### Fuentes URL
- Fuente-1-RIS: https://sni.gob.cl/requisitos-de-informacion-por-sector
- Fuente-2-Herramientas: https://sni.gob.cl/herramientas-de-apoyo-para-la-formulacion
- Fuente-3-Metodologias: https://sni.gob.cl/metodologias-por-sector

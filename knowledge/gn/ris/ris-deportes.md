---
_manifest:
  urn: urn:gn:kb:ris-deportes
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/ipr/kb_gn_010_ris/kb_gn_010_ris_deportes_koda.yml
version: 2.0.0
status: published
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
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__ris-deportes.md.json
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

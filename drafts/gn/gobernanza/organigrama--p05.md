---
_manifest:
  urn: urn:gn:kb:organigrama-p05
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml; ontologies/onto_gorenuble/goreNubleOrgData.ttl
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- organigrama
- institucional
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml
    - ontologies/onto_gorenuble/goreNubleOrgData.ttl
    source_hashes:
      domains/gn/01_fundamentos/intro/kb_gn_002_organigrama_koda.yml: 7b2c3c0ca3bf951a0d091021bfc7b8a4561e2cd99b10d89982535a8cf29f3435
      ontologies/onto_gorenuble/goreNubleOrgData.ttl: f15a877cfd6af0118b1cdb93aafd1391f4b8d956e7f001eb74f5b1dd09019cf1
    source_type: mixed
    transformation_mode: korafy_composite
    fs: 100
    cr: 1.74
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Organigrama operativo y estructura organica observables en la
      fuente KODA y el slice TTL organizacional.
    dependencies: []
    expected_sections:
    - Contenido
    document_family: organigram
    publication_class: knowledge
    skeleton_count: 3
    meat_count: 767
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gobernanza__organigrama.md.json
  kora:
    shard_index: 5
    shard_count: 5
    shard_root_urn: urn:gn:kb:organigrama
---

# Organigrama Institucional GORE Ñuble - Parte 05

## Unidad de Control de Rendiciones

### Depende de
- [-> Departamento de Finanzas]

Seguimiento y control de rendiciones de cuentas.

### Acciones
- Seguimiento, monitoreo, control y contabilización de rendiciones de cuentas ingresadas al Gobierno Regional.
- Asegurar uso de recursos conforme a normativa vigente, de forma eficiente, transparente y oportuna.

### Resultados
- Resguarda correcta administración de fondos públicos.

## Unidad de Adquisiciones

### Depende de
- [-> Departamento de Finanzas]

Procesos de compras de bienes y servicios.

### Acciones
- Ejecutar procesos de adquisiciones de bienes y servicios necesarios para funcionamiento institucional.
- Publicar y monitorear contrataciones especialmente encomendadas provenientes del programa de inversiones, junto a unidad técnica designada.

### Objetivos
- Eficiencia.
- Transparencia.
- Probidad.

### Requisitos
- Apego a Ley de Compras Públicas y su reglamento.

## Unidad de Operaciones

### Depende de
- [-> Departamento de Finanzas]

Infraestructura física, flota vehicular y tecnologías de la información.

### Acciones
- Gestionar infraestructura física (edificios e instalaciones) y flota de vehículos institucionales.
- Coordinar mantenimiento preventivo, correctivo y respuesta a emergencias.
- Asegurar operatividad, funcionalidad y seguridad de recursos físicos institucionales.
- Gestionar y mantener infraestructura TI: red, servidores, hardware, software, sistemas de información.
- Gestionar políticas de seguridad informática y protección de datos institucionales.
- Desarrollar soluciones tecnológicas alineadas con objetivos estratégicos del Gobierno Regional.

## Departamento de Finanzas

### Depende de
- [-> Division de Administracion y Finanzas]

Revisión y control de información presupuestaria, contable y financiera.

### Acciones
- Supervisar elaboración y ejecución del presupuesto.
- Gestionar registro contable y elaboración de estados financieros.
- Analizar situación económica para toma de decisiones.
- Implementar políticas de control para seguridad de activos.
- Optimizar uso de recursos.

### Resultados
Garante de salud financiera y transparencia institucional.

### Unidades dependientes
- [-> Unidad de Tesoreria]
- [-> Unidad de Contabilidad y Finanzas]
- [-> Unidad de Control de Rendiciones]
- [-> Unidad de Adquisiciones]
- [-> Unidad de Operaciones]

## Division de Administracion y Finanzas

Gestión administrativa y financiera; presupuesto de funcionamiento; servicios generales; personal.

### Resultados
Sustenta funcionamiento eficiente y transparente del Gobierno Regional.

### Unidades dependientes
- [-> Oficina de Partes]
- [-> Departamento de Gestion y Desarrollo de Personas]
- [-> Departamento de Finanzas]

---
_manifest:
  urn: urn:gn:kb:guia-circular-33-sts-p03
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/03_operacion/ipr/kb_gn_029_guia_circ33_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- circular-33
- fndr
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_029_guia_circ33_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_029_guia_circ33_koda.yml: f6b6ff85f6ff27498cd9c8a7749a3e5f60ea1f9afaea6dd68a833227c9d6dea6
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.16
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 3
    meat_count: 477
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/guias__guia-circular-33-sts.md.json
  kora:
    shard_index: 3
    shard_count: 5
    shard_root_urn: urn:gn:kb:guia-circular-33-sts
---

# Guía Operativa Circular 33 GORE Ñuble - Parte 03

## Doc 12 Cert Tecnico Mal Estado
- **Contexto:** Aplica sólo para reposición de activo.
- **Definicion:** Informe sobre el estado actual del activo a reponer.
- **Requisitos:** Emitido por profesional competente (interno o externo)., Debe incluir bitácora de fallas y razones para la reposición.
- **Proceso:** Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC.

## Doc 13 Planilla Costo Marginal
- **Contexto:** Aplica sólo para reposición de activo.
- **Definicion:** Cálculo del costo de mantener vigente el ANF un año adicional, argumentando optimización de la situación base.
- **Proceso:** Formato Excel libre; cargar en BIP (subcarpeta 'Evaluación Económica') y GESDOC.

## Doc 14 Cert Compromiso Baja Activo
- **Contexto:** Aplica sólo para reposición de activo.
- **Definicion:** Compromiso de que el activo antiguo no seguirá en operaciones una vez financiada la iniciativa.
- **Ctx Adicional:** Si postula Municipalidad, debe ser avalado por Concejo Municipal.
- **Proceso:** Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC.

## Doc 15 Cert Compromiso Costo Op Mant
- **Definicion:** Documento con detalle de costos de operación y mantención de la alternativa seleccionada.
- **Requisitos:** Utilizar precios privados., Indicar nombre de la iniciativa y código BIP., Incluir montos para todo el período de vida útil del proyecto.
- **Contexto:** Si postula Municipalidad, debe ser emitido por Concejo Municipal u organización usuaria., Si postula otro servicio, debe ser emitido por Jefe de Servicio con visación de Finanzas.
- **Proceso:** Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC.

## Doc 16 Cert Pertinencia
- **Requisitos:** Emitido por servicios competentes o por el alcalde, según tipo de proyecto.
- **Proposito:** Acreditar que el proyecto no se asocia a otra iniciativa de inversión ni tiene doble financiamiento.
- **Mdl:** |Tipo de Proyecto|Servicio/Municipalidad Emisora|
|-|-|
|Deportivos (formativo/competitivo)|Instituto Nacional de Deportes|
|Deportivos (recreativo)|Municipalidad|
|Infraestructura de salud|SEREMI de Salud|
|Infraestructura educacional|SEREMI de Educación|
|Obras en cauces de ríos|DOH, Asociación de Canalistas|
|Obras viales rurales|Dirección de Vialidad|
|Obras viales urbanas|SERVIU|
|Redes alcantarillado/agua potable|SEREMI de Salud, DOH, Empresa Sanitaria|

- **Proceso:** Formato libre; cargar en BIP (subcarpeta 'Anexos') y GESDOC.

## Doc 17 Form Conservacion
- **Definicion:** Formulario metodológico para proyectos de conservación (Anexo 4).
- **Referencias:** Formato disponible en sitio web del GORE Ñuble (GORENUBLE-GUIA-C33-ANEXOS-FORMULARIOS-01).

## Doc 18 Informe MANVU SIMP
- **Contexto:** Aplica sólo a conservación de vialidad urbana.
- **Definicion:** Informe del software MANVU SIMP para proyectos de mantenimiento vial urbano.
- **Fuentes:** Solicitado por Oficio C33 y NIP.
- **Proceso:** Imprimir resultados en PDF y cargar en BIP (subcarpeta 'Anexos').

## Doc 19 Cert Terreno
- **Requisitos:** Escritura de propiedad, dominio vigente y avalúo fiscal actualizados (<60 días).
- **Cpt:** Para Bien Nacional de Uso Público (BNUP), presentar certificado DOM que acredite condición., Si no está bajo tuición municipal, adjuntar concesión o autorización de uso., Para caminos vecinales, adjuntar documentos que acrediten cumplimiento del Decreto 293 del MOP.
- **Proceso:** Cargar en BIP (subcarpeta 'Terrenos') y GESDOC.

## Doc 20 Cert Participacion Ciudadana
- **Requisitos:** Realizar al menos una instancia de Participación Ciudadana (recomendable dos)., Debe existir reunión con beneficiarios, municipio y representante de División de Desarrollo Social del GORE como ministro de fe.
- **Proceso:** Cargar certificado firmado en BIP (subcarpeta 'Anexos').

## Doc 21 Visacion Servicio
- **Requisitos:** Proyectos que involucren competencia de otros servicios deben acreditar su aprobación., Para riberas (lagos, ríos, playas), se requiere concesión de uso., Intervenciones en cursos de agua pueden requerir visación de Gobernación Marítima., Proyectos con resolución sanitaria (plantas de tratamiento, piscinas) deben presentar proyecto aprobado por SEREMI de Salud., Conservación de graderías (>100 personas) requiere memoria de cálculo., Construcción en área rural requiere Informe Favorable para la Construcción (Art. 55 LGUC).
- **Proceso:** Cargar antecedentes con timbres de visación en BIP y GESDOC.

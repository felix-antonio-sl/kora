---
_manifest:
  urn: urn:gn:kb:guia-fril-2025-sts-p05
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- fril
- infraestructura
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml: 3aca0ba1ca44ad48be392f8c310805f0410020dcd31808b08db83934122ed97e
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.38
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 4
    meat_count: 798
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/guias__guia-fril-2025-sts.md.json
  kora:
    shard_index: 5
    shard_count: 7
    shard_root_urn: urn:gn:kb:guia-fril-2025-sts
---

# Instructivo FRIL 2025 – Región de Ñuble - Parte 05

## Placa Informativa
- **Requisitos:** Instalar al menos una placa informativa.
- **Spec:** Material: acero fotograbado bajo relieve., Medidas mínimas: 80 cm (ancho) x 60 cm (alto)., Debe usar marco oficial del GORE descargable desde sitio web.
- **Contenido:** Nombre del proyecto y logos (GORE y organización) del mismo tamaño., Frase: 'Iniciativa realizada con apoyo del Gobierno Regional de Ñuble, siendo Gobernador (nombre del Gobernador Regional)'.

## Obra Gruesa
- **Requisitos:** Describir todas las partidas de la obra en concordancia con el presupuesto oficial.
- **Ex:** Fundaciones: hormigón premezclado con parámetros de dosificación, docilidad y control de calidad.
- **Auth:** Se debe solicitar autorización a la ITO antes de llenar fundaciones.
- **Advertencias:** La ITO puede ordenar demolición de estructuras con segregaciones o desniveles.
- **Prohibiciones:** No se aceptan demoliciones posteriores para pasar instalaciones; deben dejarse espacios previstos.

## Firmas
- **Requisitos:** El documento debe ser firmado por Profesional Responsable y Director(a) de SECPLA, indicando nombre, RUT y profesión.

## Anexo 3 Presupuesto Oficial
- **Proposito:** Definir la estructura y desglose de partidas mandatorio para el presupuesto de proyectos FRIL.

## Formato
- **Frmt:** Presupuesto en formatos Excel y PDF, según secciones de documentación del instructivo.

## Encabezado
- **Requisitos:** Nombre del Proyecto (según Ficha IDI)., Código BIP., Comuna., Mandante., Fecha.

## Columnas Obligatorias
- **Requisitos:** ITEM, DESCRIPCION, UNIDAD, CANTIDAD, PRECIO UNITARIO, PRECIO TOTAL

## Estructura Partidas
- **Cpt:** Estructura jerárquica de ítems y sub-ítems del presupuesto.

## Tabla Resumen
- **Contexto:** La planilla debe contemplar, al menos, los siguientes grupos de partidas, siguiendo el detalle del instructivo:
- **Grupos:** 1 GASTOS GENERALES (letrero de obra, ensayos de laboratorio, fletes, permisos y derechos, utilidades)., 2 OBRAS PROVISIONALES (instalaciones y construcciones provisorias)., 3 TRABAJOS PREVIOS (limpieza, escarpe, nivelación, demoliciones)., 4 OBRA GRUESA (excavaciones, hormigones, moldajes, enfierraduras, estructuras, albañilería, tabiquería, techumbre)., 5 TERMINACIONES (revestimientos, puertas, ventanas, pinturas)., 6 INSTALACIONES (alcantarillado, agua potable, electricidad, gas, climatización)., 7 OBRAS EXTERIORES (cierros, pavimentos exteriores, áreas verdes, iluminación exterior)., 8 EQUIPAMIENTO Y EQUIPOS., 9 OTROS (ítems específicos adicionales).

## Resumen Costos
- **Requisitos:** Presentar COSTO NETO como suma de todos los precios totales., Calcular IVA 19% sobre costo neto., Calcular COSTO TOTAL PROYECTO como suma de costo neto + IVA.

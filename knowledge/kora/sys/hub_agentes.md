---
urn: urn:kora:kb:hub-agentes
created_by: FS
date: 2026-01-29
source: KORA system config
version: 2.0.0
status: published
tags: [kora, sistema, configuracion]
lang: es
---

# Hub de Agentes TDE

## Contexto Operativo
- **ID**: TDE_HUB_AGENTES_CTX_001
- **Objetivo**: Operación a escala de KB `tde` (artefactos KODA/Spec).
- **Alcance**: Transformación, auditoría, consulta y mantenimiento de coherencia.
- **Integración**: Orquestación entre agentes especializados y editores humanos.

## Roles de Agentes
- **KODA_TRANSFORMER**
  - **Propósito**: Ejecución workflow transformación 029 (Fuentes → KODA).
  - **Acciones**: Lectura fuentes, producción borradores YAML, aplicación fases 1-3.
  - **Referencia**: urn:knowledge:koda:sys:workflow_wikiguias:1.0.0#TDE_WORKFLOW_WIKIGUIAS_GLOBAL_001
- **TDE_AUDITOR_KB**
  - **Propósito**: Aseguramiento calidad (FS=100%, TER≥30%, RD≥2.0).
  - **Acciones**: Fase 4 workflow 029, detección MEAT faltante, reportes auditoría.
- **TDE_ROUTER_ORQUESTADOR**
  - **Propósito**: Enrutamiento tareas alto nivel.
  - **Acciones**: Clasificación tareas, asignación a especialistas, consolidación resultados.
- **TDE_EXPLORER_QA**
  - **Propósito**: Respuesta consultas sobre KB.
  - **Acciones**: Localización artefactos Tier1, composición respuestas alta fidelidad.
- **TDE_INDEXADOR**
  - **Propósito**: Mantenimiento índices, embeddings y catálogos.
  - **Acciones**: Sincronización URNs y metadatos con `catalog_master_tde`.

## Flujos Principales
### Transformación Fuente a KODA
1. Recepción fuente (ORQUESTADOR).
2. Clasificación y mapeo (1:1, 1:n, n:1).
3. Transformación fases 1-3 (KODA_TRANSFORMER).
4. Validación fase 4 (TDE_AUDITOR_KB).
5. Aplicación parches controlada.

### Auditoría Periódica KB
1. Planificación por lote o antigüedad.
2. Ejecución auditoría vs Metadata_Original (TDE_AUDITOR_KB).
3. Generación reportes hallazgos/parches.
4. Cierre y revalidación artefactos.

### Consulta QA sobre KB
1. Recepción consulta usuario.
2. Delegación contexto y artefactos (ORQUESTADOR → TDE_EXPLORER_QA).
3. Retrieval Tier1 y construcción respuesta con citas ID.
4. Registro patrones para mejora XRef/Lexicon.

## Gestión de Archivos y Catálogos
- **Ubicación**: Árbol YAML en `knowledge/core` y `knowledge/domains`.
- **Reglas**:
  - Modificaciones solo mediante herramientas controladas (`apply_patch`, `write_to_file`).
  - Actualización obligatoria de `_manifest.provenance` y `Metadata_Original`.
  - Sincronización inmediata de índices tras cambios.

## Seguridad y Control
- **Clasificación**: Activo de información crítico.
- **Políticas**: Control de cambios, respaldos, trazabilidad de commits y parches.
- **Normativa**: urn:knowledge:koda:legal:nt_seguridad_ciberseguridad:1.0.0

## Articulación Workflow 029
- **Asignación**: Fases 1-3 (KODA_TRANSFORMER), Fase 4 (TDE_AUDITOR_KB).
- **Apoyo**: Intervención humana en ambigüedades.
- **Patrones**: Uso de `Patrones_Mapping_Fuentes_Artefactos` para decisiones consistentes.

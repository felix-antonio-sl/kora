---
_manifest:
  urn: urn:kora:kb:hub-agentes
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: KORA system config
version: 2.0.0
status: published
tags:
- kora
- sistema
- configuracion
- sys
- hub
lang: es
---

# Hub de Agentes TDE

ID: TDE-HUB-AGENTES-030 | Dominio: tde_lineamientos
XRef: urn:kora:kb:workflow-wikiguias, urn:tde:kb:nt-seguridad-ciberseguridad

## Contexto Operativo

- KB `tde`: artefactos KODA/Spec (normas técnicas, guías, estrategias, plataformas compartidas).
- Operación a escala requiere Hub de agentes cooperando: transformación, auditoría, consulta, mantenimiento.
- Agentes complementan trabajo de editores humanos sobre mismo árbol de YAML.

## Roles de Agentes

| Agente | Propósito | Responsabilidad Workflow 029 |
|--------|-----------|------------------------------|
| KODA_TRANSFORMER | Transformar fuentes Markdown/PDF a KODA | Fases 1–3 (Análisis, Telegrafización, Deduplicación) |
| TDE_AUDITOR_KB | Asegurar FS=100%, TER≥30%, RD≥2.0 | Fase 4 (Validación); reportes de hallazgos MEAT |
| TDE_ROUTER_ORQUESTADOR | Enrutar tareas de alto nivel entre agentes | Clasificar, asignar, consolidar resultados |
| TDE_EXPLORER_QA | Responder consultas sobre KB `tde` | Retrieval Tier1; citar IDs de bloques |
| TDE_INDEXADOR | Mantener índices, embeddings, catálogos | Sincronizar URNs y metadatos con catalog_master_tde |

XRef KODA_TRANSFORMER: urn:kora:kb:workflow-wikiguias#TDE_WORKFLOW_WIKIGUIAS_GLOBAL_001

Métricas TDE_AUDITOR_KB:
- % artefactos auditados sobre total
- N° hallazgos MEAT por artefacto

## Flujos Principales

### Transformación Fuente a KODA (ID: TDE_HUB_AGENTES_FLUJOS_001)

1. Recepción fuente (ORQUESTADOR); clasificación y mapeo 1:1, 1:n o n:1.
2. KODA_TRANSFORMER ejecuta Fases 1–3 → borrador YAML.
3. TDE_AUDITOR_KB ejecuta Fase 4 (Validación).
4. Aplicación de parches mediante herramientas controladas (`apply_patch`, `write_to_file`).

### Auditoría Periódica KB

1. Planificación por lote temático, tipo de documento o antigüedad.
2. TDE_AUDITOR_KB compara artefactos vs fuentes declaradas en Metadata_Original.
3. Generación de reportes de hallazgos y parches propuestos.
4. Cierre de hallazgos tras actualización y revalidación.

### Consulta QA sobre KB

1. Recepción pregunta usuario → ORQUESTADOR delega a TDE_EXPLORER_QA con contexto.
2. TDE_EXPLORER_QA: retrieval Tier1 + respuesta citando IDs de bloques relevantes.
3. Registro de patrones de uso para enriquecer XRef y Lexicon.

## Gestión de Archivos y Catálogos (ID: TDE_HUB_AGENTES_FS_001)

- Árbol YAML: `knowledge/core` y `knowledge/domains`.
- Req: Modificaciones solo mediante herramientas controladas; nunca escritura directa sin registro.
- Req: Actualizar `_manifest.provenance` y `Metadata_Original` cuando cambien fuentes o URNs.
- Req: TDE_INDEXADOR actualiza índices y catálogos ante altas/bajas/modificaciones.

## Seguridad y Control de Cambios (ID: TDE_HUB_AGENTES_SEC_001)

- Clasificación: activo de información crítico.
- Políticas: control de cambios, respaldos, trazabilidad de commits y parches.
- Normativa: urn:tde:kb:nt-seguridad-ciberseguridad; GU-CIBER-001.

## Articulación con Workflow 029 (ID: TDE_HUB_AGENTES_ART_029_001)

- Fases 1–3: KODA_TRANSFORMER (con apoyo humano en ambigüedades).
- Fase 4: TDE_AUDITOR_KB.
- Patrón de decisión de mapeo (1:1, 1:n, n:1): usar `Patrones_Mapping_Fuentes_Artefactos` del workflow 029.
- XRef_Required: urn:kora:kb:workflow-wikiguias

## Glosario

| Término | Ref | XRef |
|---------|-----|------|
| Servicios digitales | TDE_DEF_SERVICIOS_DIGITALES | urn:gov:kb:lexicon-wikiguias#TDE_DEF_SERVICIOS_DIGITALES |

XRef relacionados: urn:tde:kb:guia-sistema-tde-2025, urn:tde:kb:guia-marco-gestion-datos

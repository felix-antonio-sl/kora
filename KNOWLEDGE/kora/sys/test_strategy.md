---
_manifest:
  urn: urn:kora:kb:test-strategy
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
- test
lang: es
---

# Estrategia de Pruebas KB TDE (wikiguias)

ID: TDE-TEST-STRATEGY-WIKIGUIAS-031 | Dominio: tde_lineamientos
XRef_Required: urn:kora:kb:workflow-wikiguias, urn:kora:kb:hub-agentes

## Métricas Base (ID: TDE_TEST_WIKIGUIAS_METRICAS_001)

| Métrica | Definición | Objetivo |
|---------|-----------|----------|
| FS (Fidelity Score) | % de MEAT de la fuente presente en el artefacto | FS=100% en todos los artefactos certificados |
| TER (Token Efficiency Ratio) | (tokens_KODA / tokens_fuente) × 100 | TER≥30% promedio por tipo (norma, guía, plataforma) |
| RD (Reference Density) | Promedio Ref/XRef/Ctx por bloque Tier1 significativo | RD≥2.0 en normas/estrategias/plataformas; RD≥1.0 en piezas breves |

Rec: Registrar FS, TER, RD por artefacto; mantener tablero agregado por categoría.

## Suite 1: Sintaxis y Estructura (ID: TDE_TEST_WIKIGUIAS_SUITE_001)

- YAML_Syntax_Valid: parseo sin errores (indentación, tipos, listas); bloque `_manifest` presente y bien formado (urn, domain, type, provenance).
- Core_Fields_Present: cada artefacto declara ID, Version, Status, Human-Creator, Model-Collaborator; Status ∈ {Draft, Published, Deprecated}.
- Internal_Refs_Consistent: todos los campos `Ref` apuntan a IDs existentes dentro del mismo artefacto.

## Suite 2: Fidelidad MEAT (ID: TDE_TEST_WIKIGUIAS_SUITE_002)

XRef_Required: urn:kora:kb:workflow-wikiguias

- Source_Declared: cada artefacto declara al menos un archivo fuente en `_manifest.provenance.source_file(s)` y, cuando exista, `source_url`.
- MEAT_Coverage_Audit: comparación sistemática MEAT fuente vs KODA (muestreo estratificado en fuentes extensas); no deben detectarse hechos, requisitos, definiciones o procesos ausentes en el artefacto.
  - Resultado: FS por artefacto (ideal 100%); listado de hallazgos MEAT con propuesta de parche si FS<100%.
  - Rec: Automatizar con TDE_AUDITOR_KB; revisión manual muestral en normas y plataformas críticas.

## Suite 3: TER y RD (ID: TDE_TEST_WIKIGUIAS_SUITE_003)

- TER_Calculation: calcular tokens_fuente y tokens_KODA con mismo tokenizador; generar TER por artefacto y por categoría (normas, guías, plataformas, estrategias).
  - Warn: Marcar artefactos con TER<25% como candidatos a revisión.
- RD_Calculation: calcular promedio Ref/XRef/Ctx por bloque Tier1; alertar cuando RD<umbral objetivo.
  - Rec: Usar resultados para enriquecer XRef en iteraciones futuras.

## Suite 4: Coherencia de Referencias y Dominios (ID: TDE_TEST_WIKIGUIAS_SUITE_004)

- XRef_Target_Exists: cada XRef/XRef_Required apunta a URN listada en catalog_master_tde.yml u otro catálogo relevante; reportar XRef rotas o huérfanas.
- Domain_Consistency: verificar domain="tde_lineamientos" en todos los artefactos de lineamientos; reportar inconsistencias.

## Suite 5: Certificación Global KB (ID: TDE_TEST_WIKIGUIAS_SUITE_005)

Condiciones de aceptación:
- Cobertura mínima: 100% de normas técnicas Ley 21.180, reglamento DS4, estrategias principales y plataformas compartidas clave en estado Draft o Published.
- FS=100% en todas las categorías críticas (normas, reglamento, plataformas compartidas, estrategias base).
- TER promedio por categoría ≥30%; ningún artefacto crítico con TER<25%.
- RD≥2.0 en normas, reglamento, estrategias y plataformas; RD≥1.0 en resto.
- 0 errores de sintaxis YAML; 0 Ref/XRef rotas.

Resultado: Informe de certificación con estado global (Aprobado/Observado/Rechazado), métricas agregadas y lista de artefactos bloqueantes.

## Integración con Hub de Agentes (ID: TDE_TEST_WIKIGUIAS_HUB_001)

XRef_Required: urn:kora:kb:hub-agentes

- Suite 2 y Suite 3: TDE_AUDITOR_KB con ejecución periódica (semanal o tras lotes de cambios).
- Suite 1 y Suite 4: pipelines CI/CD que validan cambios antes de fusionarlos en rama principal.
- Suite 5: hito de certificación antes de declarar KB `tde` lista para producción.

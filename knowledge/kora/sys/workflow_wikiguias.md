---
urn: urn:kora:kb:workflow-wikiguias
created_by: FS
date: 2026-01-29
source: KORA system config
version: 2.0.0
status: published
tags: [kora, sistema, configuracion]
lang: es
---

# TDE-WORKFLOW-WIKIGUIAS-029

## Objetivo
Estandarizar transformación de corpus wikiguias a KORA/Spec.
Métricas objetivo: FS=100%, TER≥30%, RD≥2.0.

## Workflow Global (TDE_WORKFLOW_WIKIGUIAS_GLOBAL_001)
- Mssn: Transformación progresiva corpus wikiguias a KB KODA/TDE.
- Obj:
  - FS=100% (Fidelidad MEAT).
  - TER≥30% (Eficiencia tokens).
  - RD≥2.0 (Densidad referencias).
- Fases: Análisis, Telegrafización, Deduplicación, Validación.

## Métricas (TDE_WORKFLOW_WIKIGUIAS_METRICAS_001)
- **FS (Fidelity Score)**: % de MEAT fuente en KORA. Target: 100%.
- **TER (Token Efficiency Ratio)**: (tokens_KORA / tokens_fuente) * 100. Target: ≥30%.
- **RD (Reference Density)**: Promedio Ref/XRef/Ctx por bloque Tier1. Target: ≥2.0 (estratégicos), ≥1.0 (breves).

## Fase 1: Análisis (TDE_WORKFLOW_WIKIGUIAS_F1_001)
- **Paso 1: Tipificación**
  - Identificar tipo fuente (Norma, Guía, Estrategia).
  - Identificar dominio TDE (Seguridad, Datos, Plataformas).
- **Paso 2: Estructura y MEAT**
  - Esquema jerárquico fuente.
  - Marcar: Def, Obj, Req, Proc, Metric.
  - Separar MEAT vs FAT (retórica).
- **Paso 3: Decisión Mapping**
  - 1:1: Cohesivo.
  - 1:n: Descomposición lineamientos.
  - n:1: Consolidación fuentes.

## Fase 2: Telegrafización (TDE_WORKFLOW_WIKIGUIAS_F2_001)
- **Paso 1: Mapping Tier1**
  - Mapear a bloques: Ctx, Def, Obj, Purp, Req, Rec, Act, Res, Warn.
- **Paso 2: Telegrafía Semántica**
  - Frases cortas, completas.
  - Eliminar redundancias retóricas.
  - Tablas a listas de parámetros MEAT.
- **Paso 3: Inyección XRef y Lexicon**
  - Referenciar Lexicon TDE existente.
  - Agregar Ctx_Required/XRef_Required a normas base.

## Fase 3: Deduplicación (TDE_WORKFLOW_WIKIGUIAS_F3_001)
- **Paso 1: Chequeo contra KB**
  - Buscar bloques equivalentes antes de crear.
- **Paso 2: Consolidación**
  - Consolidar conceptos compartidos (DDU, PISEE) en Lexicon central.
- **Paso 3: Mapping n:1**
  - Artefacto único para múltiples manuales plataforma.

## Fase 4: Validación (TDE_WORKFLOW_WIKIGUIAS_F4_001)
- **Paso 1: Sintaxis**: Correctitud MD/KORA, IDs únicos, Refs válidas.
- **Paso 2: MEAT**: Verificación bloque a bloque FS=100%.
- **Paso 3: Métricas**: Estimar TER y calcular RD.
- **Paso 4: Validación Cruzada**: Coherencia inter-artefactos.

## Patrones de Mapeo (TDE_WORKFLOW_WIKIGUIAS_PATTERNS_001)
- **Norma Técnica**: 1:1 a Lineamiento KORA.
- **Guía Operativa**: 1:1 operacionalizando norma (XRef_Required).
- **Plataforma**: n:1 para múltiples manuales (Habilitación, Integración).
- **Estrategias**: 1:n generando lineamientos temáticos.

## Articulación Agentes (TDE_WORKFLOW_WIKIGUIAS_AGENTES_001)
- Fase 1: Humano (ambigüedad).
- Fase 2/3: Automática (KODA-TRANSFORMER).
- Fase 4: Mixta (Sintaxis auto + Calidad humana).

---
urn: kora:kb:test-strategy
created_by: FS
created_at: 2026-01-29
source: KORA system config
version: 2.0.0
status: published
tags: [kora, sistema, configuracion]
lang: es
---

# Estrategia de Pruebas KORA (Sistema)

## Métricas Base
- **FS (Fidelity Score):** 100% de MEAT de la fuente presente en el artefacto. Objetivo: FS=100%.
- **TER (Token Efficiency Ratio):** (tokens_KORA / tokens_fuente) * 100. Objetivo: TER≥30% promedio.
- **RD (Reference Density):** Referencias por bloque Tier1. Objetivo: RD≥2.0 (normas/estrategias), RD≥1.0 (otros).

## Suites de Prueba

### Suite Sintaxis y Estructura
- **YAML_Syntax_Valid:** Validación de parseo YAML y bloque _manifest.
- **Core_Fields_Present:** Presencia de ID, Version, Status, Human-Creator, Model-Collaborator.
- **Internal_Refs_Consistent:** Verificación de que Ref apuntan a IDs internos existentes.

### Suite Fidelidad MEAT
- **Source_Declared:** Declaración de archivos fuente y URLs en el manifest.
- **MEAT_Coverage_Audit:** Comparación sistemática fuente vs KORA. FS ideal 100%.

### Suite TER y RD
- **TER_Calculation:** Cálculo de eficiencia por artefacto y categoría. Alerta si TER<25%.
- **RD_Calculation:** Cálculo de densidad de referencias. Alerta si RD bajo umbral.

### Suite Coherencia de Referencias
- **XRef_Target_Exists:** Validación de que XRef apuntan a URNs en catálogos maestros.
- **Domain_Consistency:** Verificación de consistencia en el campo domain.

## Certificación Global KB
- **Cobertura:** 100% de normas críticas, estrategias y plataformas clave.
- **FS:** ≥100% en categorías críticas.
- **TER:** Promedio ≥30%; mínimo 25% en artefactos críticos.
- **RD:** ≥2.0 en normas/estrategias; ≥1.0 en resto.
- **Integridad:** 0 errores YAML y 0 referencias rotas (Ref/XRef).

## Operación y Agentes
- **Agente Auditor:** Ejecución de suites de fidelidad y métricas.
- **CI/CD:** Validación automática de sintaxis y referencias en cada commit.
- **Hitos:** Certificación obligatoria previa a paso a producción.

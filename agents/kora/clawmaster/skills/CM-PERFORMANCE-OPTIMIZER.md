---
_manifest:
  urn: "urn:kora:skill:clawmaster-performance-optimizer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-PERFORMANCE-OPTIMIZER

## Proposito
Evalua y optimiza el rendimiento de una instancia OpenClaw en 8 ejes. Produce mejoras con impacto estimado, implementa las aprobadas.

## I/O

- **Input:** instancia: string | null (identificador de instancia, null=local), baseline: AuditReport | null
- **Output:** OptimizationReport (ver Signature Output)

## Procedimiento

### Paso 1: Baseline Metrics
- `openclaw status --all` — estado general
- `openclaw sessions --active 60` — sesiones activas
- `openclaw doctor` — health check
- Medir tiempos de respuesta (test message round-trip)

### Paso 2: Evaluar Ejes

| Eje | Metrica | Threshold Warning | Threshold Critical | Referencia |
|-----|---------|-------------------|--------------------|------------|
| **Token Economy** | Tokens/respuesta promedio | >4K | >8K | Cap 4 §4.4, Cap 20 |
| **Context Window** | % utilizado en sesiones activas | >70% | >90% | Cap 3 §3.5 |
| **Model Selection** | Modelo vs use case | Haiku en razonamiento complejo | Opus en chat trivial | Cap 4 §4.2, Cap 20 §20.2 |
| **Bootstrap Size** | Chars totales AGENTS+SOUL+USER+TOOLS+IDENTITY | >15K | >25K | Cap 2 §2.3 |
| **Session Management** | Sesiones activas sin actividad | >50 idle | >100 idle | Cap 3 §3.4 |
| **Memory Config** | Tamano sqlite-vec DB | >500MB sin QMD | >1GB | Cap 5 §5.3 |
| **Compaction** | Auto-compaction habilitado | Disabled | N/A | Cap 3 §3.5 |
| **Sandbox Overhead** | Modo sandbox vs necesidad | Strict sin tools peligrosos | N/A | Cap 7 §7.3 |

### Paso 3: Diagnosticar Bottlenecks
Para cada eje en WARNING o CRITICAL:
1. Identificar causa raiz
2. Cuantificar impacto (tokens ahorrados, latencia reducida, sesiones liberadas)
3. Clasificar esfuerzo: TRIVIAL (config change) | MODERADO (refactor bootstrap) | MAYOR (cambio arquitectural)

### Paso 4: Proponer Mejoras
Tabla de mejoras ordenada por impacto/esfuerzo:

| # | Eje | Mejora | Impacto Estimado | Esfuerzo | Riesgo |
|---|-----|--------|------------------|----------|--------|
| 1 | ... | ... | ... | ... | ... |

### Paso 5: Implementar Aprobadas
- Aplicar cambios de configuracion
- Para bootstrap: reducir, modularizar, lazy-load skills
- Para modelos: ajustar model routing por contexto
- Para sesiones: configurar auto-pruning, compaction
- Para memoria: habilitar QMD, optimizar embeddings

### Paso 6: Verificar
- Re-medir metricas baseline
- Comparar antes/despues
- `openclaw doctor` — confirmar health

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| baseline | object | Metricas baseline pre-optimizacion |
| ejes_evaluados | string[] | Ejes evaluados con resultado |
| bottlenecks | string[] | Cuellos de botella identificados |
| mejoras_aplicadas | string[] | Mejoras implementadas |
| metricas_post | {delta_tokens, delta_latencia, delta_sesiones} | Delta metricas post-optimizacion |
| verificacion | string | Resultado doctor post-optimizacion |

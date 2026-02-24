---
_manifest:
  urn: "urn:kora:skill:clawmaster-code-contributor:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CODE-CONTRIBUTOR

## Proposito
Analiza el codebase de OpenClaw, identifica areas de mejora, evalua viabilidad y valor, y produce propuestas concretas (issue specs o PR drafts con diff conceptual) para contribuir al proyecto.

## Procedimiento

### Paso 1: Identificar Area de Mejora

| Tipo | Ejemplos | Fuente de Deteccion |
|------|----------|---------------------|
| **Bug fix** | Comportamiento incorrecto, edge case, regression | Uso operacional, issues existentes, logs |
| **Feature** | Funcionalidad nueva, canal adicional, provider nuevo | Necesidad operacional, roadmap, community requests |
| **Refactor** | Codigo duplicado, abstracciones pobres, tech debt | Analisis de codebase, code review |
| **Docs** | Documentacion incorrecta, faltante, desactualizada | Discrepancia docs vs comportamiento real |
| **Performance** | Bottleneck, uso excesivo de recursos, latencia | Profiling, metricas operacionales |
| **DX** | Mensajes de error pobres, config confusa, CLI UX | Experiencia operacional directa |

### Paso 2: Analizar Codebase
- `oc_repo_search` para localizar archivos relevantes
- Entender la arquitectura afectada:
  - TypeScript ESM monorepo
  - Gateway-centric (packages/gateway/)
  - Channel adapters (packages/channels/)
  - Model providers (packages/providers/)
  - Shared utilities (packages/shared/)
  - CLI (packages/cli/)
- Leer codigo existente, tests relacionados, issues abiertos

### Paso 3: Evaluar Viabilidad y Valor

| Criterio | Evaluacion |
|----------|------------|
| Impacto | Cuantos usuarios afecta, severidad |
| Complejidad | LOC estimadas, archivos afectados, riesgo de regresion |
| Alineacion | Consistente con arquitectura y filosofia del proyecto |
| Duplicacion | No existe ya issue/PR abierto para esto |
| Test coverage | Tests existentes que cubren el area, tests nuevos necesarios |

Clasificar: QUICK_WIN (alto impacto, baja complejidad) | WORTHWHILE (alto impacto, alta complejidad) | NICE_TO_HAVE (bajo impacto, baja complejidad) | DEFER (bajo impacto, alta complejidad)

### Paso 4: Producir Propuesta

**Para Bug Fix / Feature — Issue Spec:**
```markdown
## Descripcion
[Que pasa / que deberia pasar]

## Reproduccion (si bug)
1. Paso 1
2. Paso 2
3. Resultado actual vs esperado

## Propuesta de Solucion
[Approach tecnico, archivos afectados, cambios conceptuales]

## Archivos Afectados
- packages/gateway/src/... — [cambio]
- packages/channels/src/... — [cambio]

## Tests
- [ ] Test caso nominal
- [ ] Test edge case
- [ ] Test regresion
```

**Para Refactor / Performance — PR Draft:**
```markdown
## Motivacion
[Por que este cambio mejora el proyecto]

## Cambios
[Diff conceptual: que cambia, que se mueve, que se elimina]

## Impacto
[Metricas esperadas: tokens, latencia, LOC, complejidad]

## Migration Path
[Si hay breaking changes, como migrar]
```

### Paso 5: Presentar al Usuario
- Resumen ejecutivo: tipo, impacto, esfuerzo
- Propuesta completa formateada
- Recomendacion: proceder o diferir
- Si aprobado: guiar creacion de issue/PR en GitHub

## Output
Propuesta lista. Reporte: {tipo, area, clasificacion: QUICK_WIN|WORTHWHILE|NICE_TO_HAVE|DEFER, propuesta: issue_spec|pr_draft, archivos_afectados[], impacto_estimado}.

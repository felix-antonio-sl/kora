---
_manifest:
  urn: "urn:fxsl:skill:refactorer-code-analyzer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CODE-ANALYZER

## Proposito
Analiza una zona del codebase calculando metricas de calidad estructural e identificando oportunidades de refactoring priorizadas.

## Input/Output
- **Input:** Zona del codebase (directorio, modulo o conjunto de archivos). Contexto: CONVENTIONS.md, ARCHITECTURE.md.
- **Output:** Reporte de analisis con metricas, oportunidades priorizadas y recomendacion de accion.

## Procedimiento

### Paso 1: Complejidad Ciclomatica
- Calcular complejidad ciclomatica por funcion/metodo.
- Umbral de alerta: >10 (moderada), >20 (alta), >30 (critica).
- Listar funciones ordenadas por complejidad descendente.
- Calcular promedio y distribucion de la zona.

### Paso 2: Deteccion de Duplicacion
- Identificar bloques duplicados (>=5 lineas identicas o near-duplicate >80% similitud).
- Agrupar clones por cluster (mismo fragmento en N ubicaciones).
- Calcular % de duplicacion sobre total de lineas de la zona.
- Umbral de alerta: >10% (moderada), >20% (alta).

### Paso 3: Consistencia de Naming
- Verificar convenciones de naming contra CONVENTIONS.md: camelCase/snake_case, prefijos, sufijos.
- Detectar nombres ambiguos: variables de 1-2 caracteres (excepto iteradores), nombres genericos (data, temp, result, item).
- Detectar inconsistencias: mismo concepto con nombres diferentes en archivos distintos.

### Paso 4: Adherencia a Patrones
- Verificar patrones definidos en ARCHITECTURE.md: estructura de modulos, separacion de concerns, dependency injection.
- Detectar anti-patrones: god functions (>50 lineas), deep nesting (>3 niveles), feature envy, shotgun surgery.
- Verificar tipado: usos de `any`, `object`, tipos sin refinar.

### Paso 5: Priorizacion
- Construir matriz impacto/esfuerzo (2x2) para cada oportunidad detectada.
- Impacto: cuanto mejora la mantenibilidad (metricas delta estimado).
- Esfuerzo: cuantas lineas/archivos afecta, riesgo de regresion.
- Priorizar: alto impacto + bajo esfuerzo primero (quick wins).

## Signature Output

```markdown
## Analisis: {zona}

### Metricas
| Metrica | Valor | Umbral | Estado |
|---------|-------|--------|--------|
| Complejidad ciclomatica (promedio) | {n} | <10 | {ok|alerta|critico} |
| Complejidad ciclomatica (max) | {n} | <20 | {ok|alerta|critico} |
| Duplicacion | {n}% | <10% | {ok|alerta|critico} |
| Naming inconsistente | {n} violaciones | 0 | {ok|alerta} |
| Anti-patrones | {n} detectados | 0 | {ok|alerta} |

### Oportunidades (priorizado impacto/esfuerzo)
| # | Tipo | Descripcion | Impacto | Esfuerzo | Archivos |
|---|------|-------------|---------|----------|----------|
| 1 | {tipo} | {descripcion} | {alto|medio|bajo} | {XS|S|M|L} | {archivos} |
```

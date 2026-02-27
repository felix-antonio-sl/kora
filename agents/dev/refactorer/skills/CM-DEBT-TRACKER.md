---
_manifest:
  urn: "urn:dev:skill:refactorer-debt-tracker:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-DEBT-TRACKER

## Proposito
Cataloga, clasifica y rastrea la reduccion de deuda tecnica a lo largo de Cycles. Genera reportes para la Retrospectiva Analitica.

## Input/Output
- **Input:** Items de deuda detectados en sesion (del CM-CODE-ANALYZER y CM-REFACTOR-EXECUTOR). Catalogo previo si existe.
- **Output:** Catalogo actualizado de deuda tecnica, tendencia del Cycle, reporte para Retrospectiva Analitica.

## Procedimiento

### Paso 1: Catalogar Items
- Registrar cada item de deuda tecnica detectado con:
  - **ID:** Identificador unico (DEBT-{zona}-{nnn}).
  - **Descripcion:** Que es el problema (1 linea).
  - **Tipo:** complejidad | duplicacion | naming | dependencias | patrones | tipos.
  - **Severidad:** CRITICA (bloquea desarrollo) | ALTA (degradacion activa) | MEDIA (molestia recurrente) | BAJA (mejora cosmetica).
  - **Esfuerzo:** XS (<30min) | S (30min-2h) | M (2h-4h) | L (4h-8h) | XL (>8h).
  - **Archivo(s):** Archivos afectados.
  - **Metricas:** Valores concretos que cuantifican el problema (ej: complejidad=18, duplicacion=34%).
  - **Estado:** pendiente | en_progreso | resuelto.

### Paso 2: Clasificar y Priorizar
- Ordenar por severidad descendente, luego por ratio impacto/esfuerzo.
- Agrupar por tipo para identificar patrones sistemicos:
  - Si >3 items del mismo tipo → problema sistemico, no puntual.
  - Si >50% de items son del mismo tipo → priorizar resolucion de raiz.

### Paso 3: Rastrear Tendencia del Cycle
- Calcular metricas de tendencia:
  - Items resueltos en este Cycle.
  - Items nuevos detectados en este Cycle.
  - Delta neto: resueltos - nuevos. Positivo = mejora. Negativo = degradacion.
  - Deuda acumulada: total items pendientes.
- Comparar con Cycle anterior si hay datos disponibles.

### Paso 4: Generar Reporte para Retrospectiva Analitica
- Resumen ejecutivo: estado general de salud del codebase.
- Metricas clave: complejidad promedio, duplicacion %, items de deuda por severidad.
- Tendencia: grafico textual de evolucion (si hay datos de multiples Cycles).
- Top 5 items criticos pendientes.
- Recomendaciones: que abordar en el proximo Cycle.

## Invariantes
- Todo item DEBE tener metricas concretas. Sin numeros no hay deuda cuantificada.
- La tendencia DEBE ser objetiva. Delta neto positivo = mejora, negativo = degradacion.
- El reporte NO DEBE incluir juicios subjetivos. Solo datos y recomendaciones basadas en datos.

## Signature Output

```markdown
## Catalogo de Deuda Tecnica: {zona}

### Items
| ID | Tipo | Severidad | Esfuerzo | Descripcion | Archivo(s) | Estado |
|----|------|-----------|----------|-------------|------------|--------|
| DEBT-{zona}-001 | {tipo} | {sev} | {esf} | {desc} | {archivos} | {estado} |

### Tendencia del Cycle
| Metrica | Valor |
|---------|-------|
| Items resueltos | {n} |
| Items nuevos | {n} |
| Delta neto | {+/-n} |
| Deuda acumulada | {n} items |

### Top 5 Criticos Pendientes
1. {DEBT-ID}: {descripcion} — {severidad}/{esfuerzo}

### Recomendaciones Proximo Cycle
1. {recomendacion basada en datos}
```

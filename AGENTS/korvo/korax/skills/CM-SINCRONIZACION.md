---
_manifest:
  urn: urn:korvo:skill:cm-sincronizacion:2.0.0
  type: lazy_load_endofunctor
---

## Proposito

Sincronizacion estrategica quincenal sobre entidades PCA v4.1. Evalua completitud() de Objetivos, throughput 14d por tipo de entidad, bloqueos cross-project, y guia decisiones estrategicas del operador mediante 4 preguntas.

## Input/Output

- **Input:** periodo 14d, entidades activas (UTs, Proyectos, Objetivos, Contribuciones)
- **Output:** ReporteSync { completitudes: Record<ObjetivoId, number | null>, throughput_14d: Throughput, alertas: Alerta[], candidatos_bancarrota: EntidadResumen[] }

## Procedimiento

### Paso 1: Preparar reporte

1. Calcular completitud() para cada Objetivo (PROPOSITO y RESULTADO).
2. Throughput 14d: UTs completadas vs UTs creadas. Balance neto.
3. Bloqueos: UTs bloqueadas > 7d, bloqueos cross-project.
4. Proyectos: estado de cada Proyecto activo, UTs pendientes/bloqueadas/completadas.
5. Contribuciones: constitutivas rotas, instrumentales sin progreso.
6. Candidatos a bancarrota: entidades estancadas > 30d sin movimiento.

### Paso 2: 4 preguntas estrategicas

Guiar al operador:

1. *"Siguen siendo estos tus objetivos?"* — Revisar PROPOSITOS y RESULTADOS vigentes. Si alguno ya no aplica, proponer descarte (Polo B para Proyectos asociados).
2. *"Estas moviendo piedras grandes o solo grava?"* — Bloques DEEP completados en 14d. Si < 2, alertar deficit de profundidad.
3. *"Bancarrota selectiva?"* — Presentar candidatos: UTs pendientes > 30d, Proyectos pausados > 30d, RESULTADOS sin progreso > 14d. Operador decide mantener o descartar.
4. *"Renegociaciones?"* — UTs bloqueadas por terceros, compromisos que ya no puede/quiere cumplir.

### Paso 3: Aplicar decisiones

1. Ejecutar descartes, pausas, reasignaciones confirmadas por el operador.
2. Si se descarta Proyecto: aplicar Polo B (INV-13).
3. Actualizar Contribuciones afectadas.

**Nota:** /sync DEBE ejecutarse siempre con el operador presente. El operador decide, Korax facilita.

**Duracion:** 45-60 minutos.

## Signature Output

```
📊 SINCRONIZACION QUINCENAL

## Objetivos
| Objetivo | Tipo | completitud() | Estado |
| --- | --- | --- | --- |
| <titulo> | PROPOSITO | 65% | ✓ |
| <titulo> | RESULTADO | 30% | ⚠️ estancado |

## Throughput (14d)
- UTs completadas: <n>
- UTs creadas: <n>
- Balance: <±n>
- Bloques DEEP: <n>

## Proyectos
| Proyecto | UTs activas | Bloqueadas | Completadas |
| --- | --- | --- | --- |

## Alertas
<lista>

## Candidatos a Bancarrota
<lista de entidades estancadas>
```

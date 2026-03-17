---
_manifest:
  urn: urn:korvo:skill:cm-deteccion-colapso:2.0.0
  type: lazy_load_endofunctor
---

## Proposito

Evaluacion booleana de senales de sobrecarga sobre metricas PCA v4.1. Determina si el sistema DEBE activar S-COLLAPSE (INV-06: >= 3 senales).

## Input/Output

- **Input:** estado de entidades (Candidatos, UTs, Proyectos, historial de interaccion)
- **Output:** CollapseEval { senales: bool[5], conteo: int, resultado: "NORMAL" | "COLAPSO" }

## Procedimiento

1. Evaluar 5 senales booleanas:

| # | Senal | Umbral | Metrica PCA v4.1 |
| --- | --- | --- | --- |
| 1 | Buffer explosivo | >30 Candidatos + creciendo | count(Candidato where estado=capturado) |
| 2 | UTs bloqueadas | >50% UTs pendientes bloqueadas | count(UT where estado=bloqueada) / count(UT where estado in pendiente,bloqueada) |
| 3 | Bloques DEEP = 0 | 2+ semanas sin bloque MK completado | count(UT where MK in modo and estado=completada and completada_en > 14d_ago) |
| 4 | completitud estancada | Algun RESULTADO sin progreso > 14d | completitud(resultado_id) sin cambio en 14d |
| 5 | Bloqueos cross-project | Bloqueo entre Proyectos > 7d | UT.bloqueada_por pertenece a otro Proyecto, duracion > 7d |

2. Contar senales activas.
3. Si >= 3 -> resultado: COLAPSO. Proponer transicion a S-COLLAPSE al operador.
4. Si < 3 -> resultado: NORMAL. Reportar estado.

**Duracion:** <1 minuto (evaluacion automatica).

## Signature Output

```
🔍 Evaluacion de colapso:
- Buffer: {✓|✗} (<n> candidatos)
- Bloqueo UTs: {✓|✗} (<n>% bloqueadas)
- DEEP: {✓|✗} (<n> bloques en 14d)
- Estancamiento: {✓|✗} (<n> objetivos sin progreso)
- Cross-project: {✓|✗} (<n> bloqueos >7d)
Senales: <n>/5 -> {NORMAL|COLAPSO}
```

---
_manifest:
  urn: "urn:kora:agent-bootstrap:korax-cm-deteccion-colapso:1.0.0"
  type: "lazy_load_endofuntor"
---

## Purpose

Evaluación booleana de señales de sobrecarga del operador. Determina si el sistema **DEBE** activar S_COLLAPSE (INV-07).

## Input/Output

- **Input:** state: {gtd_files, interaction_history}
- **Output:** evaluation: CollapseEval {señales: bool[5], conteo: int, resultado: NORMAL|COLAPSO}

## Procedure

1. Evaluar 5 señales booleanas:

| # | Señal | Umbral |
|---|---|---|
| 1 | Buffer explosivo | >30 items + creciendo |
| 2 | Waiting acumulado | >8 items |
| 3 | Bloques DEEP = 0 | 2 semanas seguidas |
| 4 | Todo urgente | >50% items marcados alta criticidad |
| 5 | Horarios nocturnos | >3 interacciones después de 23:00 |

2. Contar señales activas.
3. Si ≥3 → resultado: COLAPSO. Disparar transición a S_COLLAPSE.
4. Si <3 → resultado: NORMAL. Reportar estado.

**Duración:** <1 minuto (evaluación automática).

## Signature Output

```
🔍 Evaluación de colapso:
- Buffer: {✓|✗} ({n} items)
- Waiting: {✓|✗} ({n} items)
- DEEP: {✓|✗} ({n} bloques en 14d)
- Urgente: {✓|✗} ({n}% alta criticidad)
- Nocturno: {✓|✗} ({n} interacciones post-23:00)
Señales: {n}/5 → {NORMAL|COLAPSO}
```

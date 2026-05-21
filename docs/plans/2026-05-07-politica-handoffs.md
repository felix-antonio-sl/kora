---
_manifest:
  urn: "urn:kora:kb:politica-handoffs-v1"
  provenance:
    created_by: "FS"
    created_at: "2026-05-07"
    source: "Derivada del plan de poda KORA version A. Responde a handoff inflation detectada en abril 2026 (20 handoffs en 17 dias vs 1 invocacion productiva)."
  version: "1.0.0"
  status: publicado
  family: note
  tags: [governance, handoffs, disciplina, poda-version-a]
---

# Politica de handoffs — version A (celula unica)

## Regla

1 handoff por semana operativa como maximo. El handoff semanal debe documentar
una decision que cambie el comportamiento de una celula viva (urgenciologo,
ifml, salubrista) o una mejora medible de infraestructura (toolchain, spec).

## Justificacion

20 handoffs en 17 dias con ratio handoff:decision-relevante degradado
constituyen throughput sin outcome. Cada handoff consume atencion del operador
que no se aplica a evals pendientes.

## Excepciones

- Handoffs de cierre de canario (no cuentan contra el limite semanal).
- Handoffs de remediacion de incidente (no cuentan, pero requieren post-mortem).

## Revision

Esta politica se revisa trimestralmente o cuando KORA pase de 3 a 5 celulas
con loop eval cerrado, lo que ocurra primero.

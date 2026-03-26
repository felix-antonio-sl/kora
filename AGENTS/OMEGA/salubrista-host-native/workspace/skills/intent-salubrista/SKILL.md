---
name: intent-salubrista
description: Use this skill when the user needs a public health or health-system request classified by dominant intent, operational scale, requested product, or whether it should route to HAH specialization before deeper analysis.
---

# intent-salubrista

Determine:

- dominant intent: `epi | system | design | implementation | evaluation | vigilance | product | report | end | clarify`
- primary scale: `unidad | establecimiento | red | territorio | nacional | multi | na`
- operational object
- product type when relevant
- whether the request should route to `salubrista_hah`

If the request does not provide enough information to distinguish scale or dominant intent, return `clarificacion_requerida = true` and explain the missing minimum.

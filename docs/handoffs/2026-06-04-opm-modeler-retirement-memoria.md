---
_manifest:
  urn: "urn:kora:kb:memoria-opm-modeler-retirement-2026-06-04"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Memoria operativa derivada del retiro de opm-modeler y fortalecimiento de modelamiento-opm."
version: "1.0.0"
status: publicado
tags: [memoria, opm, modelamiento-opm, opm-modeler, despliegue]
lang: es
extensions:
  kora:
    family: note
---

# Memoria 2026-06-04 - retiro opm-modeler

- `opm-modeler` no tiene fuente KORA productiva; era una skill externa Clawhub
  v1.0.0 desplegada en workspaces OpenClaw.
- Su unico aporte util fue el wizard SD explicito: clasificacion de sistema,
  beneficiario/affectee, atributo de valor, benefit-providing object, problem
  occurrence y gate de cierre.
- Ese aporte fue absorbido en `modelamiento-opm` v1.4.2 y en
  `referencias/wizard-sd.md`; no conservar `opm-modeler` como skill runtime.
- `opm-modeler` fue retirado de los despliegues OpenClaw encontrados bajo
  `/home/felix/openclaw-fleet` y
  `/home/felix/Developer/projects/openclaw-fleet`.
- `modelamiento-opm` quedo desplegado en Claude Code, Codex, OpenCode,
  OpenClaw main y workspaces `allan-kelly`, `fugaz`, `gtd-integral`,
  `salubrista` y `steipete`.
- Handoff completo:
  `docs/handoffs/2026-06-04-opm-modeler-retirement.md`.

---
_manifest:
  urn: "urn:kora:kb:prompt-continuacion-2026-06-04-hospitalista-runtime-canon"
  provenance:
    created_by: "Codex"
    created_at: "2026-06-04"
    source: "Prompt breve de continuacion derivado del handoff 2026-06-04 hospitalista runtime canon."
version: "1.0.0"
status: publicado
tags: [prompt-continuacion, handoff, agentes, openclaw]
lang: es
extensions:
  kora:
    family: note
---

# Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde
docs/handoffs/2026-06-04-hospitalista-runtime-canon.md.

Primero lee AGENTS.md y CLAUDE.md. Verifica host con
`python3 toolchain/kora host`. Luego revisa el handoff citado.

Estado clave: `urn:salud:artefacto:medico-hospitalista` sigue siendo la fuente
KORA del agente clinico, pero su runtime OpenClaw canonico es `hospitalista`
en `/home/felix/openclaw-fleet/workspaces/hospitalista/`. No recrear
`workspaces/medico-hospitalista/`; quedo archivado como duplicado de baja
fidelidad. La skill `urn:salud:artefacto:hospitalista` sigue siendo una
habilidad separada de red/flujo/capacidad.

Pendiente sugerido: resolver en un commit separado los cambios OPM no
relacionados que quedaron fuera de este cierre y revisar el estado sucio del
repo externo /home/felix/openclaw-fleet si se requiere versionarlo.
```

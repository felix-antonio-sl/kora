---
_manifest:
  urn: "urn:kora:kb:memoria-operativa-2026-05-26-normalizacion-recuperacion-kora"
  provenance:
    created_by: "Codex"
    created_at: "2026-05-26"
    source: "Memoria operativa consolidada desde el pase de normalizacion/recuperacion KORA y su handoff explicito."
version: "1.0.0"
status: publicado
tags: [memoria-operativa, recuperacion, normalizacion, staging]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-05-26-normalizacion-recuperacion-kora"
---

# Memoria operativa - normalizacion y recuperacion KORA 2026-05-26

## Hechos consolidados

- `recovery-inventory` existe como comando reproducible para comparar KORA
canonico contra runtimes locales Codex, Claude Code y OpenClaw.
- Los gaps de `_manifest.provenance.source` en knowledge canonico bajaron a 0.
- `_FRAGUA/_archivo`, `_BUILD` y `_rebuild_required` ya no contaminan el gate de
construccion como fuentes vigentes.
- `jobs-web-ux`, `database-designer`, `agent-architect` y `polymath` son los
candidatos de recuperacion con mejor senal y quedan como borradores staging.
- Codex `.system` skills quedan fuera de KORA por diseno.
- OpenClaw `main` y memorias runtime requieren redaccion y curadoria manual.

## Invariantes para la siguiente sesion

- No promover staging sin revision de fuente, namespace y composicion.
- No convertir runtime output en fuente canonica.
- No incluir secretos, PII, endpoints sensibles ni memorias runtime completas en
artefactos KORA.
- Cualquier promocion debe cerrar con:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
```

## Decision pendiente central

La pregunta no es si los candidatos existen. Existen y estan inventariados. La
pregunta es que hacer con ellos:

- promover como artefacto nuevo;
- fusionar con artefacto canonico existente;
- dejar en staging para fuente futura;
- descartar por redundancia, riesgo o baja calidad.

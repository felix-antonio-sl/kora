---
_manifest:
  urn: "urn:kora:kb:specs-en-pausa-readme"
  provenance:
    created_by: "FS"
    created_at: "2026-05-07"
    source: "Decision operativa derivada del plan de poda KORA version A: archivar runtime-extensions sin uso productivo declarado en los 3 targets activos."
version: "1.0.0"
status: publicado
tags: [governance, decisiones-archivadas, runtime-extensions, poda-version-a, gemini, mastra, agentskills]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:claude-code-runtime-extension"
    - "urn:kora:kb:codex-runtime-extension"
    - "urn:agengai:kb:openclaw-runtime-extension"
---

# Specs runtime en pausa

## Resumen

Cuatro runtime-extensions archivadas el 2026-05-07 por la poda KORA version A. La decision operativa de Felix designa tres targets activos (`claude-code`, `codex`, `openclaw`); las cuatro extensions de este directorio quedan fuera del compromiso de uso productivo hasta que aparezca cliente nombrado con valor validado.

| Spec archivada | URN | Razon de pausa |
|---|---|---|
| `gemini-runtime-extension.md` | `urn:kora:kb:gemini-runtime-extension` | Sin uso productivo registrado; sin cliente nombrado |
| `mastra-runtime-extension.md` | `urn:kora:kb:mastra-runtime-extension` | Sin uso productivo registrado; sin cliente nombrado |
| `agentskills-runtime-extension.md` | `urn:kora:kb:agentskills-runtime-extension` | Plataforma agentskills.io disponible pero sin uso productivo en la celula activa |

## Contrato del archivo

Las specs estan **archivadas, no eliminadas**. El catalogo y el grafo siguen resolviendo sus URN. La diferencia operativa:

- **NO** son destino activo de transmutacion. La toolchain emite warning si se invoca `kora transmute --target {gemini|mastra|agentskills}`.
- **NO** se mantienen sincronizadas con cambios en `harness-spec`, `autoria-spec` o `transmutation-spec` salvo decision explicita de desarchivo.
- **SI** quedan disponibles para lectura como referencia de diseño.

## Condiciones de desarchivo

Una spec se desarchiva cuando se cumplen ambas:

1. **Cliente nombrado con valor validado**: existe un escenario concreto donde el target produce outcome (no solo output). Ej: "GORE Nuble migra agente X a Mastra en mes Z para entregar Y".
2. **Capacidad de mantenerla viva**: el operador asume el costo de revisar la spec en cada upgrade de `harness-spec` / `transmutation-spec`.

Sin ambas, la spec permanece archivada.

## Procedimiento de desarchivo

```bash
# 1. Mover spec de vuelta a runtime/
git mv governance/decisiones-archivadas/specs-en-pausa/{nombre}-runtime-extension.md runtime/

# 2. Auditar contra specs vigentes (harness-spec, autoria-spec, transmutation-spec).
# 3. Remover el target de PAUSED_TARGETS en toolchain/kora_lib/transmute.py.
# 4. Re-correr kora check --strict y la suite de tests.
# 5. Commit con razon del desarchivo y cliente nombrado.
```

## Trazabilidad

- decision raiz: poda KORA version A (allan-kelly, 2026-05-07)
- handoff de referencia: pendiente al cierre de la poda
- commit que ejecuta el archivado: ver `git log` para el commit chore(governance) del 2026-05-07
- targets activos vigentes: `claude-code`, `codex`, `openclaw`

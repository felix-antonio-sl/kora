---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-28-kora-governance-spec-upgrade"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Memoria operativa compacta del upgrade de specs, checks y transmutacion."
version: "1.0.0"
status: publicado
tags: [operational-memory, gobernanza, specs, autoria, checks]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-28-kora-governance-spec-upgrade"
    - "urn:kora:kb:agent-skill-construction-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:transmutation-spec"
---

# Memoria Operativa - KORA Governance/Spec Upgrade

## Hechos durables

1. La construccion agentica KORA produce IR canonico primero:
   `AGENT.md`/`SKILL.md` conforme a `autoria-spec`.
2. `agent-skill-construction-spec` gobierna el proceso pre-transmutacion.
3. `canario` no es parte del gate de construccion; la preocupacion se expresa
   como verificacion runtime posterior.
4. La absorcion de insumos externos o historicos no copia envelopes: conserva
   intencion, conocimiento, interfaz, estado y riesgo dentro de `artefacto`.
5. El check positivo para shape de construccion es
   `construction-authoring-shape`.
6. `a-autoria` es idempotente sobre el corpus productivo activo.
7. `v2-agentfile` no debe reintroducir overlays retirados; normaliza a
   `vector_ontologico` y `presentacion`.
8. Los outputs `_BUILD/` y runtime siguen siendo derivados regenerables.

## Comandos de continuidad

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 -m unittest discover -s tests
python3 toolchain/kora migrate --profile a-autoria --dry-run
```

Para revisar un draft concreto antes de promocion:

```bash
python3 toolchain/kora check --scope artifact --phase verify --path artifacts/agents/_FRAGUA/INBOX/<id>
```

## No reabrir

- No volver a poner `canario-spec` como dependencia de construccion.
- No convertir KODA o cualquier formato externo en seccion propia de la spec de
  construccion.
- No usar `harness_vector` o `presentation` en artefactos productivos activos.

## Referencia principal

Usar `docs/reports/handoff-2026-04-28-kora-governance-spec-upgrade.md` como
estado de cierre para retomar esta linea.

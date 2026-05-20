---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-19-cierre-estructural-post-reorg-v5"
  provenance:
    created_by: "OpenAI Codex (encarnando cat-thinking)"
    created_at: "2026-04-19"
    source: "Prompt de continuidad posterior al cierre estructural post-reorg v5."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, continuation, artifacts, promotion, backlog]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-cierre-estructural-post-reorg-v5"
    - "urn:kora:kb:operational-memory-2026-04-19-cierre-estructural-post-reorg-v5"
---

# Prompt de continuacion — post cierre estructural

Copiar y pegar el siguiente bloque como primer mensaje de la proxima sesion.

---

## Prompt a pegar

```text
Encarnate en artifacts/skills/_TALLER/INBOX/cat-thinking y opera
sobre KORA (/home/felix/kora, rama master, actualizada al commit de cierre
estructural del 2026-04-19 o posterior).

Contexto:

- Las tres olas iniciales ya estaban cerradas en `origin/master`.
- El cierre estructural del 2026-04-19 ya materializo y conecto:
  - H6 `qa-spec`
  - H5 `multiagente-spec`
  - H2 `procesos-spec`
  - H13 `risk-register-spec`
  - H23 `mastra-runtime-extension` + `fidelidad-mastra`
  - H7 curacion del KB hasta `0` huerfanos reales

Leer primero:

- docs/reports/handoff-2026-04-19-cierre-estructural-post-reorg-v5.md
- docs/reports/operational-memory-2026-04-19-cierre-estructural-post-reorg-v5.md

Verificacion minima obligatoria antes de tocar nada:

    python3 toolchain/kora check --strict
    python3 -m unittest discover -s tests
    python3 toolchain/kora kb-graph --json --orphans

Contrato esperado al arranque:

- `check --strict` = 16/16 verde
- `unittest` = 299 OK (skipped=2)
- `kb-graph` = 0 huerfanos reales y 0 aristas rotas

Si cualquiera falla, diagnosticar drift antes de avanzar. No parchar sintomas.

Backlog recomendado ahora que el bloque estructural mayor ya esta cerrado:

1. `H2-artifacts`: clasificar los `168 CM-*` embebidos en agentes productivos
   en:
   - promover a `artifacts/skills/` los reutilizables
   - absorber al `AGENT.md` los de uso unico
   - descartar legacy no justificable

2. `Promocion staging`:
   - 21 agentes en `artifacts/agents/_FRAGUA/INBOX/`
   - 7 skills en `artifacts/skills/_TALLER/INBOX/`

3. Menores diferibles:
   - `H9` TracesRequirement
   - `H17` catalogo de patrones de skills
   - `H20` wiring diagrams Mermaid
   - `H22` modelo organizacional Part IX

Metodologia:

- modo `audit` + `formalize`
- sin romanticismo por lo legacy
- no mezclar cambios ajenos de `artifacts/knowledge/fxsl/opm/opm-ssot-es/*`
- cualquier cambio debe dejar `check --strict` verde antes de commit

Primera pregunta al usuario:

¿Arrancamos por deuda de artefactos (`168 CM-*`), por promocion de staging, o
por uno de los menores (`H9/H17/H20/H22`)?
```

---

## Notas

- Este prompt ya no abre el backlog estructural mayor: lo asume cerrado.
- Si el usuario quiere otro frente, no asumir: preguntar y acotar perimetro.

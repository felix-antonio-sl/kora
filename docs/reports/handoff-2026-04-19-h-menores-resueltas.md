---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-19-h-menores-resueltas"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Cierre de H9, H17, H20 y H22 posterior al bloque de portabilidad asegurada."
version: "1.0.0"
status: publicado
tags: [handoff, h9, h17, h20, h22, wiring, requirements, organizacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-portabilidad-asegurada"
    - "urn:kora:kb:operational-memory-2026-04-19-h-menores-resueltas"
  refines:
    - "urn:kora:kb:handoff-2026-04-19-portabilidad-asegurada"
---

# Handoff explicito — H9 H17 H20 H22 resueltas

## Resumen ejecutivo

Esta sesion cierra los cuatro hallazgos menores que quedaron diferidos tras el
cierre estructural y el bloque de portabilidad:

- `H9` — `TracesRequirement`
- `H17` — catalogo de patrones de skills
- `H20` — wiring diagrams Mermaid
- `H22` — modelo organizacional Part IX

La estrategia no fue homogenea. Se resolvieron con el tipo de artefacto que
corresponde a cada uno:

- `H9`: extension semantica de `knowledge-spec` + soporte de grafo
- `H17`: artefacto de conocimiento derivado de productivo + staging
- `H20`: extension de toolchain + docs generados
- `H22`: artefacto formal de modelo organizacional

## Cambios consolidados

### H9 — trazabilidad de requirements

Se extendio `serialization/knowledge-spec.md` con la relacion
`relations.traces_requirements`, cuya proyeccion grafica es el edge
`TracesRequirement`.

Se actualizaron:

- `toolchain/kora_lib/kb_graph.py`
- `toolchain/kora_lib/graph.py`
- `toolchain/kora_lib/promote.py`

Ademas se publicaron dos artefactos:

- `artifacts/knowledge/kora/sys/requirement-traceability-model.md`
- `artifacts/knowledge/kora/sys/req-knowledge-graph-must-materialize-traces.md`

Resultado observable:

- el `repo-graph.json` ahora contiene `TracesRequirement`
- el `kb-graph` materializa `traces_requirements: 1`

### H17 — catalogo de patrones de skills

Se publico:

- `artifacts/knowledge/kora/sys/catalogo-patrones-skills.md`

Decision epistemica explicitada en el propio artefacto:

- la base empirica combina `atomize` productiva con el staging activo de
  `_TALLER/INBOX/` y `_FRAGUA/INBOX/`
- no se finge que el catalogo provenga solo de productivo, porque la muestra
  productiva de skills sigue siendo demasiado pequena

Patrones destilados:

- skill-productor
- skill de traduccion estructural
- skill guiada por corpus
- skill con productor y gate
- skill de progressive disclosure

### H20 — wiring diagrams Mermaid

Se extendio `toolchain/kora_lib/reports.py` para generar una vista materializada
del wiring del fleet productivo, reutilizando el `repo-graph` existente en vez
de inventar un DSL nuevo.

Outputs nuevos:

- `docs/generated/agent-wiring.json`
- `docs/generated/agent-wiring-mermaid.md`

Contenido:

- handoffs `RoutesToAgent` entre workspaces productivos
- invocaciones `InvokesSkill` proyectadas como subgrafo de skills

### H22 — modelo organizacional de KORA

Se publico:

- `artifacts/knowledge/kora/sys/modelo-organizacional-kora.md`

La tesis del artefacto es que KORA debe modelarse como sistema
sociotecnico/organizacional compuesto por:

- constitucion
- ontologia
- serializacion
- runtime
- productivo
- staging
- toolchain

y que su lectura mas util es una organizacion de transformaciones gobernadas,
no un simple repo ni un organigrama ornamental.

## Verificacion final

Comandos corridos al cierre:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Resultado verificado:

- `check --strict`: `Checks run: 17`, `Passed: 17`, `Failed: 0`
- `unittest`: `Ran 302 tests`, `OK (skipped=2)`
- `kb-graph`: `Nodes 525`, `Edges 668`, `Orphans real 0`, `Broken edges 0`

## Invariantes nuevas

1. `TracesRequirement` ya es parte del vocabulario operativo del grafo.
2. El wiring del fleet productivo ya tiene representacion Mermaid generada por
   toolchain; futuros handoffs deben seguir proyectando sin excepciones manuales.
3. El catalogo de patrones de skills puede usarse como criterio de curaduria
   para promociones desde `_TALLER` y `_FRAGUA`.
4. El modelo organizacional de KORA existe ya como artefacto direccionable y
   puede citarse en cierres futuros sin rehacer la teoria desde cero.

## Siguiente frente recomendado

Con estructura, portabilidad y menores cerrados, la secuencia natural queda:

1. `H2-artifacts`: clasificar `168 CM-*` embebidos en productivos
2. Promocion de staging:
   - `21` agentes en `_FRAGUA/INBOX/`
   - `7` skills en `_TALLER/INBOX/`

No quedan razones fuertes para seguir postergando ese frente.

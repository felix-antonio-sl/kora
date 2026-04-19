---
_manifest:
  urn: "urn:kora:kb:req-knowledge-graph-must-materialize-traces"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-04-19"
    source: "Requirement minima para H9: el grafo KORA debe poder materializar trazas de requirement sin ambiguedad."
version: "1.0.0"
status: publicado
tags: [requirement, graph, traceability, kora]
lang: es
extensions:
  kora:
    family: note
    requirement:
      kind: structural
relations:
  cites:
    - "urn:kora:kb:knowledge-spec"
---

# Requirement — el grafo de KORA debe materializar trazas de requirement

## Requirement

Todo requirement direccionable que un artefacto declara implementar o verificar
DEBE poder aparecer como edge `TracesRequirement` en el grafo derivado de KORA.

## Rationale

Sin esta flecha, la traza vertical `requirement -> realizacion/verificacion`
queda colapsada en `cites` o `depends`, que no distinguen cumplimiento de mero
soporte.

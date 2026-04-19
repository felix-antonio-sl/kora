---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-19-h-menores-resueltas"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Prompt autocontenido para retomar KORA despues del cierre de H9 H17 H20 H22."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, h2-artifacts, staging, kora]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-h-menores-resueltas"
    - "urn:kora:kb:operational-memory-2026-04-19-h-menores-resueltas"
---

# Prompt de proxima sesion

Copiar el bloque en `<prompt>` como mensaje inicial de la proxima sesion sobre
`/home/felix/kora`.

<prompt>
Encarnate en artifacts/skills/_TALLER/INBOX/arquitecto-categorico y opera
sobre KORA (/home/felix/kora, rama master, HEAD posterior al cierre de H9 H17
H20 H22 del 2026-04-19).

Contexto:

- Cierre estructural 2026-04-19 ya absorbido.
- Portabilidad Linux x macOS ya absorbida.
- H9/H17/H20/H22 ya resueltas:
  - `TracesRequirement` existe en knowledge-spec y repo-graph
  - catalogo de patrones de skills publicado
  - wiring Mermaid generado en docs/generated
  - modelo organizacional KORA publicado

Leer primero:

- docs/reports/handoff-2026-04-19-h-menores-resueltas.md
- docs/reports/operational-memory-2026-04-19-h-menores-resueltas.md

Verificacion minima obligatoria antes de tocar nada:

    python3 toolchain/kora check --strict
    python3 -m unittest discover -s tests
    python3 toolchain/kora kb-graph --json --orphans

Contrato esperado:

- `check --strict` = 17/17 verde
- `unittest` = 302 OK (skipped=2)
- `kb-graph` = 0 huerfanos reales, 0 aristas rotas, `traces_requirements=1`

Si falla algo:

1. `git status`
2. `git log --oneline -5`
3. correr el test especifico con `-v`

Siguiente trabajo recomendado:

1. `H2-artifacts`: clasificar los `168 CM-*` embebidos en agentes productivos en:
   - promover a `artifacts/skills/`
   - absorber al `AGENT.md`
   - descartar legacy no justificable

2. Promocion staging:
   - `21` agentes en `artifacts/agents/_FRAGUA/INBOX/`
   - `7` skills en `artifacts/skills/_TALLER/INBOX/`

Metodologia:

- modo `audit` + `formalize`
- no mezclar drift ajeno de `artifacts/knowledge/fxsl/opm/opm-ssot-es/*`
- cualquier cambio debe dejar `check --strict` verde
- si aparece un nuevo patron reusable en staging, confrontarlo contra
  `catalogo-patrones-skills.md` en vez de reinventar taxonomia

Primera pregunta al usuario:

¿Arrancamos por `H2-artifacts` o por promocion de staging?
</prompt>

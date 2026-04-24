---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-24-arquitecto-categorico-disciplina-trazas"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-24"
    source: "Memoria operativa compacta del cierre de disciplina de trazas formales para arquitecto-categorico."
version: "1.0.0"
status: publicado
tags: [operational-memory, arquitecto-categorico, formal-layer, trazas]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-24-arquitecto-categorico-disciplina-trazas"
    - "urn:kora:kb:next-session-prompt-2026-04-24-arquitecto-categorico-disciplina-trazas"
---

# Memoria operativa - arquitecto-categorico y trazas formales

## Snapshot

| Item | Estado |
|------|--------|
| Repo | `/home/felix/kora` |
| Branch de cierre | `master` |
| Skill objetivo | `artifacts/skills/_TALLER/REVIEW/arquitecto-categorico` |
| Decision central | `Traces to:` solo hacia Formal Layer KORA |
| ICAS/FXSL | permitido como `Rationale:` auxiliar |
| Check nuevo | `formal-trace-discipline` |
| Tests nuevos | cobertura de registry y disciplina del skill |
| Estado de promocion | no promovido; sigue en REVIEW |
| Limpieza aplicada | duplicados seguros y skills legacy duplicadas ya eliminadas |

## Hechos durables

1. La Formal Layer oficial de KORA es
   `artifacts/knowledge/kora/categorical-foundations/`.
2. `artifacts/knowledge/fxsl/cat/` no debe aparecer como destino normativo de
   `Traces to:`.
3. `arquitecto-categorico` puede usar ICAS/FXSL como corpus auxiliar bajo
   `Rationale:`.
4. El corpus ICAS declarado para el skill contiene 24 URNs `urn:fxsl:kb:icas-*`.
5. `check --strict` incluye ahora `formal-trace-discipline`.
6. Los commits `c8de240`, `38ce1e9` y `1cd6c13` dejaron staging mas liviano sin
   romper checks.

## Validacion base

- `python3 toolchain/kora check --strict`: verde con 20 checks.
- `python3 toolchain/kora validate --profile strict`: 17 workspaces validos, 0
  invalidos.
- `python3 -m unittest discover -s tests`: verde con suite completa y 2 skipped.
- `python3 toolchain/kora kb-graph --json --orphans`: sin broken edges ni ciclos
  `depends`.

## Continuidad

La siguiente sesion debe tratar este cierre como una remediacion estructural ya
aplicada. Cualquier cambio posterior deberia partir por mantener el invariante:
`Traces to:` es una relacion formal KORA; ICAS/FXSL explica o inspira, pero no
norma directamente.

Siguiente limpieza recomendada: `.pyc` trackeados en `toolchain/`, luego decidir
si `toolchain/file_movement_map.json` y `HANDOFF-2026-04-23.md` siguen viviendo
en sus rutas actuales.

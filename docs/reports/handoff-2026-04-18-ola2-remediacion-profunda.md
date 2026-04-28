---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-18-ola2-remediacion-profunda"
  provenance:
    created_by: "Claude Opus 4.7 (encarnando cat-thinking)"
    created_at: "2026-04-18"
    source: "Cierre de la remediación profunda post-auditoría ICAS-BoK: 15 frentes ejecutados en dos commits (2812c09 arranque + 2a38143 profunda)."
version: "1.0.0"
status: publicado
tags: [handoff, remediacion, ola-2, auditoria-icas, coalgebra, vector-laws, agentskills, closeout]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:agentskills-runtime-extension"
  refines:
    - "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
---

# Handoff explícito — Remediación profunda ola-2 (post-auditoría ICAS-BoK)

## Resumen ejecutivo

Sesión del **18 de abril de 2026** (cuarta ola del día, encarnando
`cat-thinking` en modo `audit` + `formalize`) ejecuta una
**auditoría categorial profunda** del ICAS-BoK completo aplicado a KORA
y remedia **15 de 23 hallazgos** en dos commits atómicos y coherentes.

Los 8 hallazgos restantes quedan declarados como deuda diferida — todos
requieren **diseño dedicado** (spec nueva, acuerdo de monoide, curación
humana), no son remediables en sesión única.

Estado estable resultante:

1. **Strict 15/15 verde** + 295 tests verdes.
2. **Los 7 productivos son objetos coalgebraicos formales** (Part IV ICAS-BoK
   materializado — no solo declarado en prosa).
3. **Las 5 leyes inter-eje de harness-spec §4.1** están enforzadas
   mecánicamente por primera vez.
4. **Agentskills.io tiene spec formal** + transmutor byte-identical +
   check de fidelidad + round-trip verifier.
5. **Cohort fleet deriva del filesystem** — `clawforge` deja de ser
   omitido por hardcoding.

## Cambios consolidados

### Commit 1 — `2812c09` (ola-2 arranque)

Siete frentes remediables identificados en primer audit:

1. **Dedup staging sin romanticismo**: 41 agentes + 42 skills → 21 + 7
   (purga de 53 directorios sin archivo canónico; reducción 66%).
2. **`autoria-spec v1.1 §3.5`**: shape coalgebraico opcional (`plan.fsm`,
   `interfaz.polinomio`, `invariantes.sub_coalgebra_segura`).
3. **Check `coalgebra-conformance`**: verifica termination del FSM +
   cierre de sub-coalgebra de safety cuando declaradas.
4. **Check `fidelidad-agentskills`** + target `agentskills` del transmutor:
   proyección byte-identical con renames es→en canónicos (§5.5).
5. **`kora kb-graph --orphans`**: clasificación root/intencional/real;
   exclusión de `_SCRIPTORIUM` del grafo.
6. **`kora deprecate`**: dual formal de promote con régimen completo.
7. **`kora promote --cohort <ns>`**: batch promotion con preserva-
   composicionalidad (aborta al primer fallo).
8. **Gobernanza §5.1 — Olas**: lifecycle a escala formalizado.

### Commit 2 — `2a38143` (ola-2 profunda)

Ocho frentes post-auditoría categorial detallada:

- **H4 — Purga `harness_vector` legacy**: los 7 productivos tenían doble
  vector (canónico + fake). `migrate --perfil a-autoria` reaplicado
  eliminó el residuo.
- **H1 — Check `vector-laws`**: 5 leyes inter-eje de harness-spec §4.1
  (Π≥3⟹Μ≥1; Ξ=4⟹Λ≥1; Φ≥2⟹Μ≥1; acc≥2⟹trans≥2; Λ=3⟹Σᵢ≥2).
- **H11 — Disonancia atlas**: curator/clawforge/forgemaster declaraban
  `arnes_categorico: orquestador` con Ξ=2 Λ=0. Renombrados a `persona`
  (coherente con vector observado).
- **H12 — Cohort fleet derivado**: `OPERATING_CORE_COHORTS` se computa
  desde filesystem. `clawforge` ahora aparece en `operating-core-contracts.md`.
- **H15 — `agentskills-runtime-extension.md v1.0`**: spec nueva que
  formaliza dominio (Π≤2 Μ≤1 Ξ≤2 Λ=0 Φ≤1), renames (campos, subdirs,
  secciones), invariantes (idempotencia, no-mutación, no-LLM).
- **H3 — Shape coalgebraico en los 7 productivos**: `plan.fsm` +
  `interfaz.polinomio` + `sub_coalgebra_segura` derivados mecánicamente
  desde el shape existente. Los 7 pasan `coalgebra-conformance`.
  Script one-shot en `toolchain/migrate_coalgebra.py`.
- **H14 — `kora roundtrip-check`**: verifica dualidad
  `T_agentskills ∘ Lift_agentskills ≈ id` por fingerprint (name,
  description, body semántico, file hashes normalizados).
- **H8 — API observable opcional** (autoria §3.5.1): Yoneda operativo.
- **H16 — Familia `adr`** (md-spec v8.1 §5.6): Architecture Decision
  Record como subperfil de `note` con factorización categórica.

## Perímetro final de los dos commits

Commit `2812c09`:
- `artifacts/agents/_FRAGUA/INBOX/*` (dedup deletes + _perfiles relocation)
- `artifacts/skills/_TALLER/INBOX/*` (dedup deletes)
- `toolchain/kora_lib/{checks,cli,kb_graph,promote,transmute}.py`
- `specs/{autoria-spec,gobernanza}.md`

Commit `2a38143`:
- `artifacts/agents/{kora,gn}/*/AGENT.md` (7 productivos con shape coalgebraico + legacy purgado)
- `toolchain/kora_lib/{checks,cli,config,transmute}.py`
- `toolchain/migrate_coalgebra.py` (nuevo)
- `specs/{autoria-spec,md-spec,agentskills-runtime-extension}.md`
- `tests/{test_artifacts,test_operating_core_scenarios}.py`

## Verificación ejecutada

- `python3 toolchain/kora index` → 603 artifacts indexados.
- `python3 toolchain/kora check --strict` → **15/15 verde** (checks_run=15, passed=15, failed=0).
- `python3 toolchain/kora roundtrip-check --agent kora/atomize` → OK.
- `python3 -m unittest discover -s tests` → **295 tests OK** (skipped=2 condicional).
- `python3 toolchain/kora sync-docs` → docs regeneradas.
- `python3 toolchain/kora kb-graph --json --orphans` → clasificación
  emitida (318 huérfanos reales documentados).

## Estado de los 7 productivos después de la remediación

Todos con:
- URN canónico `urn:{ns}:artefacto:{name}`.
- `vector_ontologico` (solo, sin `harness_vector` legacy).
- `atlas.{arnes_categorico, forma_material}` coherente con vector.
- `artefacto.{perfil, plan, interfaz, contexto, invariantes}` completo.
- `artefacto.plan.fsm` con `{inicial, terminales, transiciones}` normalizado.
- `artefacto.interfaz.polinomio` derivado de herramientas.
- `artefacto.invariantes.sub_coalgebra_segura` (lista de estados seguros).
- `extensions.kora.verificacion_coalgebraica: true`.
- **Pasan `coalgebra-conformance` + `vector-laws` + `autoria-conformance`**.

| Workspace | Arnés | Estados | Terminales |
|-----------|-------|---------|------------|
| kora/guardian | persona | 4 | S-END |
| kora/forgemaster | persona | 4 | S-END |
| kora/curator | persona | 11 | S-END |
| kora/custodio | persona | 4 | S-END |
| kora/clawforge | persona | 4 | S-END |
| gn/goreologo | persona | 4 | S-END |
| gn/digitrans | persona | 4 | S-END |

## Deuda diferida (NO remediable en sesión única)

Los 8 hallazgos pendientes requieren diseño dedicado:

| # | Hallazgo | Razón de diferimiento |
|---|----------|------------------------|
| H2 | `procesos-spec` — functoriality de los 9 procesos | Requiere inventario explícito de invariantes por proceso |
| H5 | `multiagente-spec` — sheaf de coreografía multi-agente | Spec nueva grande (session types + Poly) |
| H6 | `qa-spec` — quality attributes enriquecidos | Requiere acuerdo sobre monoide de enrichment (Cost? Bool? [0,1]?) |
| H7 | Curación de 318 huérfanos reales kb-graph | Tarea humana de clasificación por namespace |
| H9 | Edge `TracesRequirement` | Requiere concepto formal de "requirement" en KORA |
| H13 | Risk register como Kleisli arrows | Depende de H6 (quality attributes primero) |
| H17 | Catálogo de patrones de skills | Necesita ≥3 skills productivos para destilar patrones |
| H20 | Wiring diagrams Mermaid de handoffs | Extensión de `sync-docs` + convenciones |
| H22 | Modelo organizacional Part IX | Spec nueva (KORA se modela a sí misma) |
| H23 | Wrappers frontier (Mastra, LangGraph, Vercel AI SDK) | 1 wrapper por runtime; priorizar Mastra |

## Invariantes del cierre

Este handoff declara estas invariantes para la próxima sesión:

1. **Strict es verdad**: cualquier commit futuro debe mantener `kora check --strict` verde.
2. **Shape coalgebraico es norma**: nuevos productivos nacen con `plan.fsm` + `interfaz.polinomio` + `sub_coalgebra_segura` ya declarados.
3. **Legacy purgado no vuelve**: `harness_vector`, `presentation` (en), `SOUL.md`, `TOOLS.md`, etc., son inválidos post-autoria v1.1. Cualquier reintroducción es regresión.
4. **Cohort deriva de filesystem**: no hardcodear listas de workspaces productivos en `config.py`.
5. **Perímetro limpio por commit**: regenerables (`catalog/`, `docs/generated/*`, `_BUILD/`) se excluyen de commits de código.

## Archivos clave a leer en próxima sesión

Para retomar sin recargar contexto:

- `/home/felix/.claude/projects/-home-felix-kora/memory/MEMORY.md` — índice.
- `/home/felix/.claude/projects/-home-felix-kora/memory/project_ola2_remediation.md` — detalle de las dos olas.
- Este handoff (`urn:kora:kb:handoff-2026-04-18-ola2-remediacion-profunda`).
- Auditoría categorial profunda (respuesta detallada en transcript de esta sesión) — 23 hallazgos clasificados por Parte ICAS-BoK.

## Pipeline mínimo para reanudar

```bash
cd /home/felix/kora
python3 toolchain/kora check --strict   # debe estar 15/15 verde
python3 -m unittest discover -s tests # debe estar 295 OK
python3 toolchain/kora kb-graph --orphans # para ver 318 huérfanos reales
```

Si cualquiera de estos no sale como se declara aquí, **investigar drift antes de tocar**.

# Prompt de Continuacion — auditoria categorial KORA

Retoma desde `docs/handoffs/2026-06-08-auditoria-categorial-frente1.md`.

## Frente 2 pendiente (rec. 1, critico, requiere decision HITL)

El drift de fundamento entre `ontology/harness-spec.md` y la Formal Layer oficial
(`artifacts/knowledge/kora/categorical-foundations/`):

- harness-spec funda PMI×LFS con `cites: urn:fxsl:kb:icas-*` (corpus auxiliar,
  NO normativo segun CLAUDE.md).
- La Formal Layer oficial modela la F-coalgebra de agente, sin mencionar
  PMI×LFS.
- El check `formal-trace-discipline` vigila `Traces to:` pero no `cites:` —
  harness-spec escapo al guardian.

**Dos opciones honestas:**
1. Absorber PMI×LFS a `categorical-foundations/` con poset-producto, 5 leyes y
   `Traces to:` desde harness-spec. Mas trabajo; choca con freeze parcial de
   harness.
2. Rebajar el claim a "fundado en corpus auxiliar, pendiente de absorcion."

Decide el operador. No editar harness sin ADR explicita.

## Contexto auxiliar

- Informe de auditoria: `docs/audit/2026-06-07-auditoria-categorial-kora.md`
- Meta-evaluacion 360°: `docs/audit/_meta/sintesis-meta-evaluacion.md`
- Inventario de claims: `docs/audit/_meta/claims-master.md`
- Matriz NxN: `docs/audit/_meta/matriz-nxn.md`
- Rec. 4/5/7 de la auditoria tambien abiertas (ver informe).

Antes de cualquier edicion, ejecutar gates KORA: `check --strict`, suite completa.

# Prompt de Continuacion — refinamientos editoriales meta-auditoria

Retoma desde
`docs/handoffs/2026-06-08-refinamientos-editoriales-meta-auditoria.md`.

## Pendiente principal

**Frente 2 — drift harness-spec ↔ Formal Layer** (rec. 1 de polymath, requiere
decision HITL):

El fundamento categorial de `ontology/harness-spec.md` usa
`cites: urn:fxsl:kb:icas-*` (corpus auxiliar, no normativo) mientras la Formal
Layer oficial (`artifacts/knowledge/kora/categorical-foundations/`) modela la
F-coalgebra de agente sin mencionar PMI×LFS. El check `formal-trace-discipline`
no cubre `cites:`.

Dos opciones: (1) absorber PMI×LFS a categorical-foundations/ con `Traces to:`
— requiere levantar freeze parcial de harness con ADR; (2) rebajar el claim a
"fundado en corpus auxiliar, pendiente de absorcion".

Decide el operador.

## Contexto

- Handoff previo (Frente 1):
  `docs/handoffs/2026-06-08-auditoria-categorial-frente1.md`
- Meta-evaluacion 360°: `docs/audit/_meta/sintesis-meta-evaluacion.md`
- Inventario de claims: `docs/audit/_meta/claims-master.md`
- Matriz NxN: `docs/audit/_meta/matriz-nxn.md`

Antes de cualquier edicion: `python3 toolchain/kora check --strict`, suite
completa.

# Prompt de Continuacion — refinamientos editoriales meta-auditoria

Retoma desde
`docs/handoffs/2026-06-08-refinamientos-editoriales-meta-auditoria.md`.

Frentes 1 y 2 de la auditoria polymath se transfirieron a otra linea. Este
prompt solo cubre lo pendiente de la meta-evaluacion 360°.

## Pendiente — colimite curado y cierre de huecos (§10 de la sintesis)

### Hueco mas grave: Formal Layer oficial

La meta-evaluacion identifico que **ninguna** de las 8 auditorias abrio la
Formal Layer oficial (`artifacts/knowledge/kora/categorical-foundations/`), en
particular `06-audit-invariants` y `07-behavioral-preservation`. Estos
documentos **refutarian o confirmarian el hallazgo central** del conjunto ("la
deuda critica es de verificacion, no de diseno"). Es la omision mas grave del
colimite.

Tarea: auditar la Formal Layer oficial contra las specs vivas y determinar si
los invariantes de auditoria y la preservacion comportamental que declara estan
mecanizados, declarados o ausentes.

### Huecos secundarios

- Auditar `procesos-spec` y `risk-register-spec` (tocadas de refilon).
- Auditar el **toolchain (codigo)**, no solo el texto de las specs: varios
  claims sobre que hace el toolchain se afirmaron sin auditar `toolchain/`.

### Colimite curado

Producir documento unico que pegue los mejores hallazgos verificados de las 8
auditorias, con `deep` como base, injertando los 5 claims unicos valiosos
identificados en §10.2 y corrigiendo los errores falsables listados en §10.3.

## Contexto

- Meta-evaluacion 360°: `docs/audit/_meta/sintesis-meta-evaluacion.md`
- Inventario de claims: `docs/audit/_meta/claims-master.md`
- Matriz NxN: `docs/audit/_meta/matriz-nxn.md`
- Handoff previo (Frente 1, para referencia historica):
  `docs/handoffs/2026-06-08-auditoria-categorial-frente1.md`

Antes de cualquier edicion: `python3 toolchain/kora check --strict`, suite
completa.

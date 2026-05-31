# Docs

`docs/` es una capa documental auxiliar de KORA. No es fuente normativa ni
fuente operativa canonica del repo; para gestion del repo usa el `CLAUDE.md`
top-level.

## Precedencia

Cuando exista tension entre `docs/` y otra parte del repo, la precedencia es:

1. `governance/`
2. `ontology/`
3. `serialization/`
4. `runtime/`
5. `artifacts/`
6. `toolchain/` y `tests/`
7. `docs/`

## Subdirectorios

### `docs/generated/`

Salidas regenerables producidas por la CLI.

Reglas:

- No editar a mano.
- Si se desactualiza, regenerar.
- Si contradice al filesystem o al catalogo, corrige la fuente o el generador.

### `docs/handoffs/`

Snapshots operativos vivos, nombrados como `YYYY-MM-DD-*.md`.

Reglas:

- Sirven para continuidad de sesion.
- No reemplazan a `CLAUDE.md`, la CLI ni las specs.
- La politica vigente vive en `docs/plans/2026-05-07-politica-handoffs.md`.

### `docs/plans/`

Bitacora de diseno y planificacion.

Reglas:

- Puede describir estado futuro o trabajo en curso.
- No debe usarse como fuente normativa ni como evidencia de materializacion.
- `docs/plans/_archivo/` conserva material historico sin autoridad operativa.

## Mantenimiento

Despues de cambios estructurales importantes:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
```

Usa `python3 toolchain/kora sync-docs` solo cuando quieras regenerar salidas
publicas en `docs/generated/`.

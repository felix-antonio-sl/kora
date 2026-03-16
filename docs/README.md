# Docs

`docs/` es una capa documental auxiliar de KORA. Su funcion es registrar salidas derivadas, planes de trabajo y reportes de corridas. No es la fuente normativa ni la fuente operativa canonica del repo.

## Precedencia

Cuando exista tension entre `docs/` y otra parte del repo, la precedencia es:

1. `specs/`
2. `AGENTS/`
3. `KNOWLEDGE/`
4. `catalog/`
5. `scripts/` y schemas aplicables
6. `docs/`

Consecuencia: `docs/` documenta, resume o planifica, pero no gobierna el comportamiento del sistema.

## Subdirectorios

### `docs/generated/`

Salidas regenerables producidas por la CLI, principalmente via `python3 scripts/kora sync-docs`.

Incluye, entre otros:

- estadisticas vivas del repo
- grafo derivado del catalogo
- auditorias de agentes
- contratos del operating core
- ledgers derivados

Reglas:

- No editar a mano.
- Si se desactualiza, regenerar.
- Si contradice al filesystem o al catalogo, el problema esta en la fuente o en la toolchain, no se corrige manualmente aqui.

### `docs/plans/`

Bitacora de diseno y planificacion. Aqui viven:

- blueprints
- planes de implementacion
- handoffs
- notas de remediacion
- planes de source mapping

Reglas:

- Puede describir estado futuro o trabajo en curso.
- No debe usarse como fuente normativa ni como evidencia de que algo ya fue materializado.
- Conviene nombrar archivos con prefijo de fecha `YYYY-MM-DD-<tema>.md`.

### `docs/reports/`

Reportes puntuales de corridas, auditorias o reparaciones.

Reglas:

- Son evidencia historica de una operacion concreta.
- Pueden ser JSON, Markdown u otro formato de salida de tooling.
- No reemplazan la validacion viva del repo.

## Uso correcto

Usa `docs/` para:

- explicar estado derivado del repo
- dejar trazabilidad de planes y decisiones de trabajo
- conservar evidencia de corridas tecnicas

No uses `docs/` para:

- definir reglas del sistema
- fijar interfaces de agentes
- reemplazar manifests, catalogo o knowledge publicado
- mantener a mano metricas o inventarios que la CLI ya genera

## Mantenimiento

Despues de cambios estructurales importantes:

```bash
python3 scripts/kora index
python3 scripts/kora validate --profile strict
python3 scripts/kora sync-docs
```

Si se agrega un nuevo tipo de artefacto bajo `docs/`, debe quedar claro si es:

- derivado regenerable
- plan de trabajo
- reporte de evidencia

Si no cae en una de esas tres clases, probablemente pertenece en otra parte del repo.

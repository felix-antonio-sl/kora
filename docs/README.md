# Docs

`docs/` es una capa documental auxiliar de KORA. Su funcion es registrar
salidas derivadas, planes de trabajo y reportes de corridas. No es la fuente
normativa ni la fuente operativa canonica del repo.

## Precedencia

Cuando exista tension entre `docs/` y otra parte del repo, la precedencia es:

1. `governance/`
2. `ontology/`
3. `serialization/`
4. `runtime/`
5. `artifacts/`
6. `toolchain/` y `tests/`
7. `docs/`

Consecuencia: `docs/` documenta, resume o preserva evidencia, pero no gobierna
el comportamiento del sistema.

## Subdirectorios

### `docs/generated/`

Salidas regenerables producidas por la CLI, principalmente via
`python3 toolchain/kora sync-docs`.

Incluye, entre otros:

- estadisticas vivas del repo
- grafo derivado del catalogo
- auditorias de agentes
- contratos del operating core
- ledgers derivados

Reglas:

- No editar a mano.
- Si se desactualiza, regenerar.
- Solo deben vivir aqui artefactos materializados por la toolchain activa.
- Si contradice al filesystem o al catalogo, el problema esta en la fuente o en
  la toolchain, no se corrige manualmente aqui.

### `docs/plans/`

Bitacora de diseno y planificacion. Aqui viven:

- blueprints
- planes de implementacion
- handoffs de trabajo futuro
- notas de remediacion
- planes de source mapping

Reglas:

- Puede describir estado futuro o trabajo en curso.
- No debe usarse como fuente normativa ni como evidencia de que algo ya fue
  materializado.
- Conviene nombrar archivos con prefijo de fecha `YYYY-MM-DD-<tema>.md`.

### `docs/reports/`

Reportes puntuales de corridas, auditorias, analisis estructurales o
reparaciones.

Reglas:

- Son evidencia historica de una operacion concreta.
- Pueden ser JSON, Markdown u otro formato de salida de tooling o analisis
  manual.
- No reemplazan la validacion viva del repo.
- Los analisis no regenerables pertenecen aqui, no en `docs/generated/`.

## Uso correcto

Usa `docs/` para:

- explicar estado derivado del repo
- dejar trazabilidad de planes y decisiones de trabajo
- conservar evidencia de corridas tecnicas o analisis historicos

No uses `docs/` para:

- definir reglas del sistema
- fijar interfaces de agentes
- reemplazar manifests, catalogo o knowledge publicado
- mantener a mano metricas o inventarios que la CLI ya genera

## Mantenimiento

Despues de cambios estructurales importantes:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora sync-docs
```

Si se agrega un nuevo tipo de artefacto bajo `docs/`, debe quedar claro si es:

- derivado regenerable
- plan de trabajo
- reporte de evidencia historica

Si no cae en una de esas tres clases, probablemente pertenece en otra parte del
repo.

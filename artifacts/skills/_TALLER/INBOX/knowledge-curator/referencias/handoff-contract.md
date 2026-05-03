# Handoff Contract

## Contrato de entrada esperado

Cuando `curation-conductor` delega a `knowledge-curator`, el handoff debería
dejar explícito:

- `scope = knowledge`
- `family = KB normal`
- `functor = F`
- `staging = INBOX | REVIEW | published-repair`
- `source_path` o `draft_path`
- `intent = create | repair | improve | re-audit`
- `desired_outcome` si existe

## Regla de aceptación

`knowledge-curator` acepta ejecutar solo cuando el contrato implica curación
descriptiva de `KB normal`.

## Regla de rechazo

Si el contrato o diagnóstico mínimo da alguno de estos resultados, no ejecutar
la ruta y devolver handoff:

| Señal | Resultado |
|---|---|
| `family = atomic` | handoff a `atomize` |
| material prescriptivo o fundacional | `rerouted_to_spec` |
| familia ambigua no resuelta | `pending` |

## Contrato de salida

La salida hacia `curation-conductor` o hacia el operador debe incluir:

- `draft_path`
- `urn`
- `family`
- `audit_summary`
- `outcome`
- `next_step`

## Regla de cierre

La skill cierra en `REVIEW`. Si el borrador queda listo para publicar, declara
`ready_to_promote`, pero no ejecuta la promoción como sustituto de
`kora promote`.

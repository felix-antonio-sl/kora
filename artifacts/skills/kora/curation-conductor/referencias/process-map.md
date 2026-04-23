# Process Map

## Fuente normativa mínima

- `governance/gobernanza.md`
- `ontology/harness-spec.md`
- `serialization/md-spec.md`
- `serialization/knowledge-spec.md`
- `artifacts/knowledge/kora/sys/pipeline-ingesta.md`

## Mapa del proceso

1. **Diagnóstico y gate de scope**
   - si el input es descriptivo y corresponde al pipeline de `artifacts/knowledge/` -> continuar
   - si el input es prescriptivo, fundacional o de gobierno -> `rerouted_to_spec`

2. **Intake**
   - si el input es crudo -> `_SCRIPTORIUM/INBOX`
   - si ya está estructurado como draft -> `_SCRIPTORIUM/REVIEW`

3. **Selección de familia**
   - `KB normal`
   - `atomic`

4. **Selección de funtor**
   - descriptivo -> `F` koraficación
   - prescriptivo fuera de scope -> reroute a `spec`

5. **Selección de productor**
   - `atomic` -> `atomize`
   - `KB normal` -> curación guiada descriptiva

6. **Validación**
   - lint/shape
   - relaciones
   - fidelidad
   - gates de publicación

7. **Promoción**
   - si pasa gates -> `kora promote`
   - si no pasa -> vuelve a `REVIEW` o `repair`

## Estados finales

- `pending`
- `processing`
- `ready_to_promote`
- `published`
- `needs_repair`
- `rerouted_to_spec`

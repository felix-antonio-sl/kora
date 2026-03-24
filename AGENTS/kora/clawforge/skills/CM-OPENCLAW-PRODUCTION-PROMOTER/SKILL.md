---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-production-promoter:1.0.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - oc_docs_search
        - spec_consult
        - workspace_read
        - artifact_read
        - artifact_write
      requires: []
      references:
        - references/promotion-basis.md
      assets:
        - assets/production-promotion-checklist.md
        - assets/production-backlog-template.yml
---

# CM-OPENCLAW-PRODUCTION-PROMOTER

## Proposito

Evaluar si un agente `OpenClaw` esta listo para promoción a producción y, si no lo está, emitir un backlog priorizado de endurecimiento con criterios de salida y modo de adopción recomendado.

## Input/Output

- **Input:** agent_path: string, contract_path: string?, target_mode: string (pilot|assisted-prod|autonomous-prod)
- **Output:** ProductionPromotionReport

## Procedimiento

1. Consultar `references/promotion-basis.md` para fijar la base normativa y factual de la promoción.
2. Usar `assets/production-promotion-checklist.md` como checklist maestra.
3. Evaluar el agente y su contrato contra 10 ejes:
   - calidad real del handoff y de las skills operativas
   - `dry-run` antes de mutaciones locales
   - fixtures y escenarios de contrato
   - detección de colisiones
   - política de restart
   - executor o frontera explícita de config/runtime
   - verificación post-cambio
   - perfil mínimo seguro del propio `clawforge`
   - escenarios reales end-to-end
   - modo de adopción explícito
4. Clasificar cada eje en `ready`, `partial` o `missing`.
5. Emitir backlog priorizado:
   - `P0`: bloquea promoción
   - `P1`: no bloquea `pilot`, sí bloquea `assisted-prod`
   - `P2`: endurecimiento deseable
6. Si se entrega `target_mode`, declarar elegibilidad actual o no.
7. Escribir el backlog usando `assets/production-backlog-template.yml` cuando se deba persistir como artefacto.

## Signature Output

```yaml
promotion:
  target_mode: "assisted-prod"
  readiness: "partial"
  eligible_now: false
  blockers:
    - "dry_run_obligatorio_no_automatizado"
  backlog:
    P0: []
    P1: []
    P2: []
  exit_criteria:
    - "doctor_y_status_deep_ok"
```

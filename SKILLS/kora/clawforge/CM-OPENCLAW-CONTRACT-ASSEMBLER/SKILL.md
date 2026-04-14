---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-contract-assembler:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-CONTRACT-ASSEMBLER

## Proposito

Ensamblar un `platform_contract` OpenClaw a partir de fragmentos estructurados emitidos por las skills especializadas, preservando proveniencia y sin colisiones silenciosas.

## Input/Output

- **Input:** base_contract: object, fragments: object[]
- **Output:** ContractAssemblyReport

## Procedimiento

1. Partir desde el template base del contrato.
2. Aplicar merge por dominios:
   - `config_projection.gateway`
   - `config_projection.sandbox`
   - `config_projection.tools`
   - `config_projection.agents.defaults`
   - `config_projection.agents.list`
   - `config_projection.channels`
   - `managed_installs.*`
   - `deployment_hints.*`
   - `provenance.*`
3. Registrar proveniencia por fragmento para cada bloque materializado.
4. Si dos fragmentos intentan fijar el mismo scalar con valores distintos, marcar colision y NO resolverla implicitamente.
5. Devolver contrato ensamblado + lista de colisiones + trazabilidad.

## Signature Output

```yaml
assembly:
  status: "OK"
  assembled_contract: {}
  collisions: []
  provenance:
    channels.telegram: "CM-OPENCLAW-TELEGRAM-ARCHITECT"
```

---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-contract-emitter:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-CONTRACT-EMITTER

## Proposito

Persistir `platform_contract`, fragmentos especializados, reportes de validacion y patches en un layout estable de staging para reuso posterior.

## Input/Output

- **Input:** output_dir: string, assembled_contract: object, fragments: object[], validation: object?
- **Output:** ContractEmissionReport

## Procedimiento

1. Crear layout estable de staging:
   - `contracts/platform-contract.yml`
   - `fragments/*.yml`
   - `validation/contract-validation.yml`
   - `patches/*.yml`
2. Escribir el contrato ensamblado como fuente de verdad operativa en staging.
3. Escribir cada fragmento especializado por separado para facilitar reuso incremental.
4. Si existe un patch incremental vigente, escribirlo bajo `patches/` con nombre determinista.
5. Emitir manifest de archivos escritos y rutas reutilizables.

## Signature Output

```yaml
emission:
  status: "OK"
  files_written:
    - "contracts/platform-contract.yml"
    - "fragments/telegram.yml"
    - "validation/contract-validation.yml"
  reusable_paths:
    contract: "contracts/platform-contract.yml"
    fragments_dir: "fragments/"
    patches_dir: "patches/"
```

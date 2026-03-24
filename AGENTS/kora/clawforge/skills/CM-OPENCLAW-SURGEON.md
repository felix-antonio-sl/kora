---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-surgeon:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-SURGEON

## Proposito
Aplicar fixes minimos sobre workspace o contrato OpenClaw-oriented, incluyendo remediaciones previas a deploy.

## Input/Output
- **Input:** issue: object, agent_path: string
- **Output:** FixReport

## Procedimiento
1. Clasificar si el problema es bootstrap, contract, topology o drift.
2. Corregir el minimo conjunto de componentes necesarios.
3. Revalidar el componente tocado y reenviar a `S-VALIDATE`.

## Signature Output
```yaml
fix:
  applied: true
  touches:
    - "AGENTS.md"
```

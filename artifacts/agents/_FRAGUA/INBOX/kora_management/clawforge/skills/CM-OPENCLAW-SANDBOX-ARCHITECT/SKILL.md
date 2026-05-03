---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-sandbox-architect:1.0.0
  type: lazy_load_endofunctor
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - oc_docs_search
        - spec_consult
      requires: []
      references:
        - references/sandbox-architecture-map.md
      assets:
        - assets/sandbox-config-fragment-template.json5
---

# CM-OPENCLAW-SANDBOX-ARCHITECT

## Proposito

Definir la arquitectura de sandbox, tool policy y subagentes para un agente OpenClaw, distinguiendo con precision entre donde corren las tools, cuales existen y cuando `elevated` es aceptable.

## Input/Output

- **Input:** objetivo: string, trust_boundary: string, topology: string
- **Output:** SandboxArchitectureReport

## Procedimiento

1. Consultar `references/sandbox-architecture-map.md`.
2. Elegir backend y scope:
   - `docker`
   - `ssh`
   - `openshell`
   - `scope: session|agent|shared`
3. Definir:
   - `config_projection.sandbox.*`
   - `config_projection.tools.profile`
   - `config_projection.tools.allow/deny`
   - `config_projection.tools.elevated.*`
   - `subagents.allowAgents`
4. Separar siempre:
   - sandbox = donde corre
   - tool policy = que existe
   - elevated = escape hatch solo para `exec`
5. Si se usa `openshell`, decidir `mirror` vs `remote` y documentar cual workspace queda canonico.
6. Emitir riesgo si:
   - se propone `docker.sock`
   - se usa `elevated` como sustituto de policy
   - se comparte scope donde deberia haber aislamiento por agente
7. Emitir salida mecanizable en tres bloques:
   - `config_fragment`
   - `contract_fragment`
   - `validation_checks`
8. Usar `assets/sandbox-config-fragment-template.json5` como shape de referencia.

## Signature Output

```yaml
sandbox:
  backend: "docker"
  config_fragment:
    sandbox:
      mode: "all"
      backend: "docker"
      scope: "agent"
      workspaceAccess: "rw"
    tools:
      profile: "coding"
      elevated:
        enabled: false
  contract_fragment:
    deployment_hints:
      sandbox:
        backend: "docker"
        remote_canonical: false
      bind_mounts: []
      manual_inputs_required: []
  validation_checks:
    - "sandbox_vs_tool_policy_segregado"
    - "elevated_no_relaja_tools"
  warnings: []
```

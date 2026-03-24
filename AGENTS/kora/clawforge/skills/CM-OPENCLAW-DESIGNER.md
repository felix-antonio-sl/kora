---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-designer:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-DESIGNER

## Proposito
Disenar un agente KORA cuyo target runtime es OpenClaw, incluyendo topologia y surfaces nativas esperadas.

## Input/Output
- **Input:** requisitos: string
- **Output:** OpenClawBlueprint

## Procedimiento
1. Consumir el knowledge report de entrada para fijar baseline factual OpenClaw cuando la solicitud dependa de features de plataforma.
2. Definir dominio, rol y fronteras del agente.
3. Consumir el topology report de entrada para decidir:
   - `single-gateway-multi-agent`
   - `isolated-gateway`
   - `remote`
   - `trusted-proxy`
4. Si el agente interactua por Telegram, consumir el telegram architecture report de entrada para fijar ACL durable, UX y topologia de topics/cuentas.
5. Si el agente requiere tooling sensible o aislamiento especial, consumir el sandbox architecture report de entrada.
6. Si el agente depende de plugins, bundles o skills externos, consumir el managed installs report de entrada.
7. Modelar explicitamente:
   - que vive en bootstrap
   - que vive en config nativa
   - que vive en installs gestionados
   - que queda fuera como runtime state
8. Emitir blueprint que ya incluya surfaces nativas esperadas y riesgos topologicos.

## Signature Output
```yaml
blueprint:
  topology: "single-gateway-multi-agent"
  native_surfaces:
    - "agents.list[]"
    - "tools.*"
    - "sandbox.*"
  specialized_axes:
    - "telegram"
    - "sandbox"
    - "managed_installs"
```

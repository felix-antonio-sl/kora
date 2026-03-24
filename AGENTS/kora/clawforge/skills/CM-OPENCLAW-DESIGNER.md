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
1. Consultar primero `CM-OPENCLAW-KNOWLEDGE-NAVIGATOR` para fijar baseline factual OpenClaw cuando la solicitud dependa de features de plataforma.
2. Definir dominio, rol y fronteras del agente.
3. Usar `CM-OPENCLAW-TOPOLOGIST` para decidir:
   - `single-gateway-multi-agent`
   - `isolated-gateway`
   - `remote`
   - `trusted-proxy`
4. Si el agente interactua por Telegram, usar `CM-OPENCLAW-TELEGRAM-ARCHITECT` para fijar ACL durable, UX y topologia de topics/cuentas.
5. Si el agente requiere tooling sensible o aislamiento especial, usar `CM-OPENCLAW-SANDBOX-ARCHITECT`.
6. Si el agente depende de plugins, bundles o skills externos, usar `CM-OPENCLAW-PLUGIN-BUNDLE-MANAGER`.
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

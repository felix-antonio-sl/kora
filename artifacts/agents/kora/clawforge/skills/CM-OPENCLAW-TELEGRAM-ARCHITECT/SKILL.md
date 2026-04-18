---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-telegram-architect:1.0.0
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
        - references/telegram-ops-map.md
      assets:
        - assets/telegram-config-fragment-template.json5
---

# CM-OPENCLAW-TELEGRAM-ARCHITECT

## Proposito

Disenar, configurar y auditar la capa Telegram de un agente OpenClaw usando como base la documentacion oficial del canal y las restricciones KORA/OpenClaw vigentes.

## Input/Output

- **Input:** objetivo: string, perfil_agente: string, modo: dm|group|forum|multi-account
- **Output:** TelegramArchitectureReport

## Procedimiento

1. Consultar `references/telegram-ops-map.md` para seleccionar las paginas oficiales relevantes.
2. Resolver primero el patron de acceso:
   - owner-bot
   - multi-operator
   - grupos o topics
   - multi-account
3. Derivar config nativa:
   - `dmPolicy`
   - `allowFrom`
   - `groupPolicy`
   - `groupAllowFrom`
   - `replyToMode`
   - `chunkMode`
   - `textChunkLimit`
   - `streaming`
   - `silentErrorReplies`
   - `defaultAccount` y overrides por cuenta si aplica
4. Si la necesidad exige topics persistentes, ACP bindings o approvals por chat, documentar la surface exacta de OpenClaw y no degradarla a instrucciones sueltas en `TOOLS.md`.
5. Emitir advertencias si:
   - el patron depende solo de pairing y no de ACL durable
   - hay mezcla ambigua entre DM, grupos y topics
   - se omite `defaultAccount` en multi-account
   - la UX propuesta contradice el baseline OpenClaw actual
6. Emitir salida mecanizable en tres bloques:
   - `config_fragment`
   - `contract_fragment`
   - `validation_checks`
7. Usar `assets/telegram-config-fragment-template.json5` como shape de referencia para el fragmento de config.

## Signature Output

```yaml
telegram:
  pattern: "owner-bot"
  config_fragment:
    channels:
      telegram:
        dmPolicy: "allowlist"
        allowFrom: ["123456789"]
        chunkMode: "length"
        silentErrorReplies: true
  contract_fragment:
    deployment_hints:
      channel:
        provider: "telegram"
        mode: "dm"
      manual_inputs_required: []
  validation_checks:
    - "allowFrom_numerico"
    - "dmPolicy_durable"
  warnings: []
```

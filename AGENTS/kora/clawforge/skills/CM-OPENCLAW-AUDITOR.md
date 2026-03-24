---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-auditor:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-AUDITOR

## Proposito
Auditar conformidad de un agente OpenClaw-oriented contra specs KORA y extension OpenClaw, incluyendo runtime health y drift operativo cuando aplique.

## Input/Output
- **Input:** agent_path: string, contract_path: string?
- **Output:** OpenClawAuditReport

## Procedimiento
1. Verificar segregacion de bootstrap y `config.json`.
2. Verificar `native-first`, `contract sufficiency` y `runtime state excluded`.
3. Cruzar la decision topologica con el topology report de entrada.
4. Verificar configuracion de Telegram y otros canales con el telegram architecture report de entrada cuando el agente los use.
5. Verificar sandbox, tool policy y elevated con el sandbox architecture report de entrada.
6. Verificar `managed_installs` y surfaces plugin/bundle con el managed installs report de entrada.
7. Verificar topologia recomendada, config viva, health del gateway y drift entre fuente/contract/runtime.
8. Emitir PASS|WARN|FAIL con correcciones priorizadas.

## Signature Output
```yaml
audit:
  result: "PASS"
  findings: []
  axes_checked:
    - "topology"
    - "sandbox"
    - "managed_installs"
```

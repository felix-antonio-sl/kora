---
_manifest:
  urn: urn:kora:skill:clawforge-openclaw-auditor:1.0.0
  type: lazy_load_endofunctor
---

# CM-OPENCLAW-AUDITOR

## Proposito
Auditar conformidad de un agente OpenClaw-oriented contra specs KORA y extension OpenClaw, incluyendo runtime health y drift operativo cuando aplique.

## Input/Output
- **Input:** agent_path: string, contract_path: string?, topology_report: object?, telegram_report: object?, sandbox_report: object?, managed_installs_report: object?, runtime_evidence: object?
- **Output:** OpenClawAuditReport

## Procedimiento
1. Verificar segregacion de bootstrap y `config.json`.
2. Verificar `native-first`, `contract sufficiency` y `runtime state excluded`.
3. Cruzar la decision topologica con `topology_report`.
4. Verificar configuracion de Telegram y otros canales con `telegram_report` cuando el agente los use.
5. Verificar sandbox, tool policy y elevated con `sandbox_report`.
6. Verificar `managed_installs` y surfaces plugin/bundle con `managed_installs_report`.
7. Verificar topologia recomendada, config viva, health del gateway y drift entre fuente/contract/runtime usando `runtime_evidence` cuando exista.
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

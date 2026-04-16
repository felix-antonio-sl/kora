# Sandbox Architecture Map

Fuentes oficiales prioritarias para sandbox, tools y subagentes OpenClaw.

## Sandboxing

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/sandboxing.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/openshell.md`

## Politica de tools y elevated

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/sandbox-vs-tool-policy-vs-elevated.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/gateway/configuration-reference.md`

## Multi-agent y subagentes

- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/subagents.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/tools/multi-agent-sandbox-tools.md`
- `KNOWLEDGE/agengai/openclaw/documentacion-oficial/concepts/multi-agent.md`

## Regla

1. Nunca confundir sandbox con tool policy.
2. `elevated` no concede tools nuevas.
3. `openshell mirror|remote` cambia el workspace canonico efectivo; eso debe quedar documentado en el contrato.

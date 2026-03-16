---
title: Validation Report Template
status: internal
lang: es
---

# Validation Report Template

## Resultado

- Workspace: `{workspace}`
- Resultado global: `PASS|FAIL`
- Baseline: `agent-spec-md v8.4.0 / skill-spec-md v4.0.0 / gobernanza.md v3.2.0`

## Checks

| ID | Nombre | Veredicto | Detalle |
| --- | --- | --- | --- |
| 1 | `{check_name}` | `PASS|FAIL|WARN|SKIP` | `{detail}` |

## Issues

| Severidad | Componente | Campo | Mensaje | Correccion |
| --- | --- | --- | --- | --- |
| `ERROR|WARNING` | `{component}` | `{field}` | `{message}` | `{fix}` |

## Resumen

- PASS: `{pass_count}`
- FAIL: `{fail_count}`
- WARN: `{warn_count}`
- SKIP: `{skip_count}`

# KORA Operating Core Contracts

Este documento es generado por `scripts/kora sync-docs`. No editar a mano.

## Resumen

- Workspaces cubiertos: 13
- Estados declarados: 96
- Tools semanticas declaradas: 83
- Handoffs declarados: 42

## Auditoria meta-kora

- Meta agentes auditados: 4
- Meta agentes en nucleo operativo endurecido: 4
- Meta agentes auxiliares explicitamente descopados: 0

| Workspace | Estatus | Estados | Skills | Tools | Handoffs | Motivo |
|-----------|---------|---------|--------|-------|----------|--------|
| kora/guardian | operating_core | 4 | 3 | 3 | 3 | Nucleo operativo constitucional: gobierna coherencia de specs, precedencia y validacion fundacional. |
| kora/forgemaster | operating_core | 11 | 15 | 10 | 3 | Nucleo operativo: disena, crea, valida y entrega handoff al custodio. |
| kora/curator | operating_core | 11 | 11 | 7 | 2 | Nucleo operativo: korafica, audita y entrega handoff al custodio. |
| kora/custodio | operating_core | 8 | 8 | 8 | 2 | Nucleo operativo: cierra salud, catalogo e ingesta del repo. |

## Cohorte kora

| Workspace | Estados | Tools | Handoffs |
|-----------|---------|-------|----------|
| kora/guardian | 4 | 3 | 3 |
| kora/forgemaster | 11 | 10 | 3 |
| kora/curator | 11 | 7 | 2 |
| kora/custodio | 8 | 8 | 2 |

## Cohorte dev

| Workspace | Estados | Tools | Handoffs |
|-----------|---------|-------|----------|
| dev/planner | 8 | 7 | 3 |
| dev/coder | 7 | 8 | 2 |
| dev/reviewer | 6 | 8 | 2 |
| dev/sentinel | 7 | 7 | 3 |

## Cohorte ops

| Workspace | Estados | Tools | Handoffs |
|-----------|---------|-------|----------|
| ops/orquestador-swarm | 7 | 7 | 6 |
| ops/verificador | 8 | 7 | 5 |
| ops/security | 7 | 7 | 4 |

## Cohorte domain_canary

| Workspace | Estados | Tools | Handoffs |
|-----------|---------|-------|----------|
| gn/goreologo | 4 | 2 | 7 |
| gn/digitrans | 8 | 2 | 0 |

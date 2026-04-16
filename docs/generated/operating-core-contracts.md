# KORA Operating Core Contracts

Este documento es generado por `scripts/kora sync-docs`. No editar a mano.

## Resumen

- Workspaces cubiertos: 6
- Estados declarados: 49
- Tools semanticas declaradas: 32
- Handoffs declarados: 12

## Auditoria meta-kora

- Meta agentes auditados: 4
- Meta agentes en nucleo operativo endurecido: 4
- Meta agentes auxiliares explicitamente descopados: 0

| Workspace | Estatus | Estados | Skills | Tools | Handoffs | Motivo |
|-----------|---------|---------|--------|-------|----------|--------|
| kora/guardian | operating_core | 4 | 4 | 3 | 3 | Nucleo operativo constitucional: gobierna coherencia de specs, precedencia y validacion fundacional. |
| kora/forgemaster | operating_core | 11 | 16 | 10 | 4 | Nucleo operativo: disena, crea, valida y entrega handoff al custodio. |
| kora/curator | operating_core | 11 | 11 | 7 | 2 | Nucleo operativo: korafica, audita y entrega handoff al custodio. |
| kora/custodio | operating_core | 8 | 8 | 8 | 2 | Nucleo operativo: cierra salud, catalogo e ingesta del repo. |

## Cohorte kora

| Workspace | Estados | Tools | Handoffs |
|-----------|---------|-------|----------|
| kora/guardian | 4 | 3 | 3 |
| kora/forgemaster | 11 | 10 | 4 |
| kora/curator | 11 | 7 | 2 |
| kora/custodio | 8 | 8 | 2 |

## Cohorte domain_canary

| Workspace | Estados | Tools | Handoffs |
|-----------|---------|-------|----------|
| gn/goreologo | 7 | 2 | 1 |
| gn/digitrans | 8 | 2 | 0 |

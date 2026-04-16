# Agent Audit

Este documento es generado por `scripts/kora sync-docs`. No editar a mano.

## Resumen global

- Fecha: 2026-04-17
- Cohortes auditadas: meta-kora, dev, ops, domains
- Reglas absorbidas sin hallazgos manuales: 9
- Reglas aun no institucionalizadas: 1

## Top 5 deudas sistemicas

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 1 | gn/goreologo | agent_fix |

## Top 5 falsos verdes del validator actual

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 1 | gn/goreologo | agent_fix |

## Cohorte meta-kora

- Workspaces auditados: 4
- `validate --profile strict` verde: si
- Hallazgos manuales: 0
- P1: 0 | P2: 0 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

## Cohorte dev

- Workspaces auditados: 0
- `validate --profile strict` verde: si
- Hallazgos manuales: 0
- P1: 0 | P2: 0 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

## Cohorte ops

- Workspaces auditados: 0
- `validate --profile strict` verde: si
- Hallazgos manuales: 0
- P1: 0 | P2: 0 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

## Cohorte domains

- Workspaces auditados: 2
- `validate --profile strict` verde: si
- Hallazgos manuales: 1
- P1: 1 | P2: 0 | P3: 0

### Subgrupo gn

- Workspaces: 2
- Hallazgos: 1

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| gn/goreologo | Destino de control no declarado | P1 | AGENTS/gn/goreologo/AGENTS.md:65 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 1 | gn/goreologo | agent_fix |

### Subgrupo pro

- Workspaces: 0
- Hallazgos: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

### Subgrupo salud

- Workspaces: 0
- Hallazgos: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

### Subgrupo fxsl

- Workspaces: 0
- Hallazgos: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

### Subgrupo korvo

- Workspaces: 0
- Hallazgos: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| - | Sin hallazgos manuales nuevos | - | - | - | - |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| - | - | 0 | - | - |

## Rollout de enforcement

- Pasar a lint: Destino de control no declarado
- Mantener manual: ninguno

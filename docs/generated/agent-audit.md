# Agent Audit

Este documento es generado por `scripts/kora sync-docs`. No editar a mano.

## Resumen global

- Fecha: 2026-04-14
- Cohortes auditadas: meta-kora, dev, ops, domains
- Reglas absorbidas sin hallazgos manuales: 5
- Reglas aun no institucionalizadas: 5

## Top 5 deudas sistemicas

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 58 | fxsl/arquitecto-automatizacion-organizacional, fxsl/arquitecto-sistemas-informacion, fxsl/ingeniero-sistemas-composicional, fxsl/ontologista-gist, gn/ar-virtual, gn/asesor-juridico | agent_fix |
| Destino de control no declarado | P1 | 6 | gn/dgi-virtual, gn/gestor-ipr-360, gn/goreologo, salud/medico-urgencias | agent_fix |
| Skill compone otro skill operativamente | P2 | 1 | korvo/korax | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 1 | ops/clawstack | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 1 | fxsl/neriomath | agent_fix |

## Top 5 falsos verdes del validator actual

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 58 | fxsl/arquitecto-automatizacion-organizacional, fxsl/arquitecto-sistemas-informacion, fxsl/ingeniero-sistemas-composicional, fxsl/ontologista-gist, gn/ar-virtual, gn/asesor-juridico | agent_fix |
| Destino de control no declarado | P1 | 6 | gn/dgi-virtual, gn/gestor-ipr-360, gn/goreologo, salud/medico-urgencias | agent_fix |
| Skill compone otro skill operativamente | P2 | 1 | korvo/korax | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 1 | ops/clawstack | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 1 | fxsl/neriomath | agent_fix |

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

- Workspaces auditados: 1
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

- Workspaces auditados: 1
- `validate --profile strict` verde: si
- Hallazgos manuales: 1
- P1: 1 | P2: 0 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| ops/clawstack | Skill degenerado recibe o emite estado FSM | P1 | AGENTS/ops/clawstack/skills/CM-CONTEXT-MANAGER.md:13 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Skill degenerado recibe o emite estado FSM | P1 | 1 | ops/clawstack | agent_fix |

## Cohorte domains

- Workspaces auditados: 18
- `validate --profile strict` verde: si
- Hallazgos manuales: 66
- P1: 65 | P2: 1 | P3: 0

### Subgrupo gn

- Workspaces: 8
- Hallazgos: 27

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/ar-virtual/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/ar-virtual/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | AGENTS/gn/asesor-juridico/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | AGENTS/gn/asesor-juridico/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | AGENTS/gn/asesor-juridico/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Destino de control no declarado | P1 | AGENTS/gn/dgi-virtual/AGENTS.md:62 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/dgi-virtual/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | AGENTS/gn/erp-gore/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:65 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:69 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:75 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:25 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:27 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gestor-ipr-360/AGENTS.md:29 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gobernador-virtual/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gobernador-virtual/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gobernador-virtual/AGENTS.md:25 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | AGENTS/gn/gobernador-virtual/AGENTS.md:27 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/goreologo | Destino de control no declarado | P1 | AGENTS/gn/goreologo/AGENTS.md:65 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 22 | gn/ar-virtual, gn/asesor-juridico, gn/dgi-virtual, gn/erp-gore, gn/gestor-ipr-360, gn/gobernador-virtual | agent_fix |
| Destino de control no declarado | P1 | 5 | gn/dgi-virtual, gn/gestor-ipr-360, gn/goreologo | agent_fix |

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

- Workspaces: 3
- Hallazgos: 8

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| salud/medico-urgencias | Destino de control no declarado | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:72 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| salud/medico-urgencias | Precedencia de transiciones no declarada | P1 | AGENTS/salud/medico-urgencias/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 7 | salud/medico-urgencias | agent_fix |
| Destino de control no declarado | P1 | 1 | salud/medico-urgencias | agent_fix |

### Subgrupo fxsl

- Workspaces: 6
- Hallazgos: 30

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| fxsl/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-automatizacion-organizacional/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-automatizacion-organizacional/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-automatizacion-organizacional/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-automatizacion-organizacional/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-automatizacion-organizacional/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-automatizacion-organizacional/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:25 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/neriomath | Skill degenerado clasifica transiciones o continuidad FSM | P1 | AGENTS/fxsl/neriomath/skills/CM-CLASIFICADOR.md:12 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ontologista-gist/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ontologista-gist/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ontologista-gist/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ontologista-gist/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ontologista-gist/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | AGENTS/fxsl/ontologista-gist/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 29 | fxsl/arquitecto-automatizacion-organizacional, fxsl/arquitecto-sistemas-informacion, fxsl/ingeniero-sistemas-composicional, fxsl/ontologista-gist | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 1 | fxsl/neriomath | agent_fix |

### Subgrupo korvo

- Workspaces: 1
- Hallazgos: 1

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| korvo/korax | Skill compone otro skill operativamente | P2 | AGENTS/korvo/korax/skills/CM-CLOSE.md:19 | Eliminar la invocacion operativa a otro CM y mover la secuencia o routing a AGENTS.md; el skill solo debe usar criterios del dominio o la spec rectora. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Skill compone otro skill operativamente | P2 | 1 | korvo/korax | agent_fix |

## Rollout de enforcement

- Pasar a lint: Destino de control no declarado, Precedencia de transiciones no declarada, Skill compone otro skill operativamente, Skill degenerado clasifica transiciones o continuidad FSM, Skill degenerado recibe o emite estado FSM
- Mantener manual: ninguno

# Agent Audit

Este documento es generado por `scripts/kora sync-docs`. No editar a mano.

## Resumen global

- Fecha: 2026-03-09
- Cohortes auditadas: meta-kora, dev, ops, domains
- Reglas absorbidas sin hallazgos manuales: 6
- Reglas aun no institucionalizadas: 3

## Top 5 deudas sistemicas

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 14 | fxsl/pensador-generador, gn/dgi-virtual, gn/estratega-comunicacional, gn/gestor-ipr-360, gn/goreologo, pro/abogado-legislacion-medica | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 10 | korvo/korax, ops/deployer, ops/integrador, ops/orquestador-swarm, ops/security, ops/verificador | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 8 | ops/observer, pro/salubrista, pro/salubrista-hah | agent_fix |

## Top 5 falsos verdes del validator actual

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 14 | fxsl/pensador-generador, gn/dgi-virtual, gn/estratega-comunicacional, gn/gestor-ipr-360, gn/goreologo, pro/abogado-legislacion-medica | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 10 | korvo/korax, ops/deployer, ops/integrador, ops/orquestador-swarm, ops/security, ops/verificador | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 8 | ops/observer, pro/salubrista, pro/salubrista-hah | agent_fix |

## Cohorte meta-kora

- Workspaces auditados: 6
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

- Workspaces auditados: 7
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

- Workspaces auditados: 7
- `validate --profile strict` verde: si
- Hallazgos manuales: 13
- P1: 13 | P2: 0 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| ops/deployer | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/deployer/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/deployer | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/deployer/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/integrador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/integrador/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/integrador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/integrador/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/observer/skills/CM-CONTEXT-MANAGER.md:12 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/observer/skills/CM-CONTEXT-MANAGER.md:22 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/observer/skills/CM-CONTEXT-MANAGER.md:23 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/observer/skills/CM-CONTEXT-MANAGER.md:39 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/orquestador-swarm | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/orquestador-swarm/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/security | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/security/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/security | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/security/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/verificador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/verificador/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/verificador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/ops/verificador/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Skill degenerado recibe o emite estado FSM | P1 | 9 | ops/deployer, ops/integrador, ops/orquestador-swarm, ops/security, ops/verificador | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 4 | ops/observer | agent_fix |

## Cohorte domains

- Workspaces auditados: 25
- `validate --profile strict` verde: si
- Hallazgos manuales: 19
- P1: 19 | P2: 0 | P3: 0

### Subgrupo gn

- Workspaces: 13
- Hallazgos: 7

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| gn/dgi-virtual | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/dgi-virtual/AGENTS.md:58 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/estratega-comunicacional | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/estratega-comunicacional/AGENTS.md:57 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/gestor-ipr-360/AGENTS.md:59 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/gestor-ipr-360/AGENTS.md:61 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/gestor-ipr-360/AGENTS.md:67 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/goreologo | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/goreologo/AGENTS.md:44 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/goreologo | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/gn/goreologo/AGENTS.md:50 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 7 | gn/dgi-virtual, gn/estratega-comunicacional, gn/gestor-ipr-360, gn/goreologo | agent_fix |

### Subgrupo pro

- Workspaces: 4
- Hallazgos: 9

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| pro/abogado-legislacion-medica | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/abogado-legislacion-medica/AGENTS.md:49 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/abogado-legislacion-medica | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/abogado-legislacion-medica/AGENTS.md:55 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/medico-urgencias | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/medico-urgencias/AGENTS.md:68 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/salubrista | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/salubrista/AGENTS.md:62 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/salubrista | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/salubrista/skills/CM-INTENT-FIRS.md:17 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| pro/salubrista | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/salubrista/skills/CM-INTENT-FIRS.md:37 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| pro/salubrista-hah | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/salubrista-hah/AGENTS.md:70 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/salubrista-hah | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/salubrista-hah/skills/CM-INTENT-FIRS.md:17 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| pro/salubrista-hah | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/pro/salubrista-hah/skills/CM-INTENT-FIRS.md:48 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 5 | pro/abogado-legislacion-medica, pro/medico-urgencias, pro/salubrista, pro/salubrista-hah | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 4 | pro/salubrista, pro/salubrista-hah | agent_fix |

### Subgrupo fxsl

- Workspaces: 7
- Hallazgos: 2

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| fxsl/pensador-generador | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/fxsl/pensador-generador/AGENTS.md:51 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| fxsl/pensador-generador | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/agents/fxsl/pensador-generador/AGENTS.md:57 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Destino de control no declarado | P1 | 2 | fxsl/pensador-generador | agent_fix |

### Subgrupo korvo

- Workspaces: 1
- Hallazgos: 1

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| korvo/korax | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/agents/korvo/korax/skills/CM-BANCARROTA.md:12 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Skill degenerado recibe o emite estado FSM | P1 | 1 | korvo/korax | agent_fix |

## Rollout de enforcement

- Pasar a lint: Destino de control no declarado, Skill degenerado clasifica transiciones o continuidad FSM, Skill degenerado recibe o emite estado FSM
- Mantener manual: ninguno

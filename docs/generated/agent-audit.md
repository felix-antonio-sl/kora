# Agent Audit

Este documento es generado por `scripts/kora sync-docs`. No editar a mano.

## Resumen global

- Fecha: 2026-03-15
- Cohortes auditadas: meta-kora, dev, ops, domains
- Reglas absorbidas sin hallazgos manuales: 5
- Reglas aun no institucionalizadas: 5

## Top 5 deudas sistemicas

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 191 | dev/analyst, dev/coder, dev/planner, dev/refactorer, dev/reviewer, dev/sentinel | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 12 | korvo/korax, ops/clawstack, ops/deployer, ops/integrador, ops/orquestador-swarm, ops/security | agent_fix |
| Destino de control no declarado | P1 | 11 | gn/dgi-virtual, gn/estratega-comunicacional, gn/gestor-ipr-360, gn/goreologo, ops/clawstack, pro/abogado-legislacion-medica | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 4 | ops/observer | agent_fix |
| Skill compone otro skill operativamente | P2 | 1 | ops/orquestador-swarm | agent_fix |

## Top 5 falsos verdes del validator actual

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 191 | dev/analyst, dev/coder, dev/planner, dev/refactorer, dev/reviewer, dev/sentinel | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 12 | korvo/korax, ops/clawstack, ops/deployer, ops/integrador, ops/orquestador-swarm, ops/security | agent_fix |
| Destino de control no declarado | P1 | 11 | gn/dgi-virtual, gn/estratega-comunicacional, gn/gestor-ipr-360, gn/goreologo, ops/clawstack, pro/abogado-legislacion-medica | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 4 | ops/observer | agent_fix |
| Skill compone otro skill operativamente | P2 | 1 | ops/orquestador-swarm | agent_fix |

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

- Workspaces auditados: 7
- `validate --profile strict` verde: si
- Hallazgos manuales: 40
- P1: 40 | P2: 0 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| dev/analyst | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/analyst/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/analyst | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/analyst/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/analyst | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/analyst/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/analyst | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/analyst/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/analyst | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/analyst/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/analyst | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/analyst/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/coder | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/coder/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/coder | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/coder/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/coder | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/coder/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/coder | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/coder/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/coder | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/coder/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/coder | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/coder/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/planner | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/planner/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/refactorer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/refactorer/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/refactorer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/refactorer/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/refactorer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/refactorer/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/refactorer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/refactorer/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/refactorer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/refactorer/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/reviewer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/reviewer/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/reviewer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/reviewer/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/reviewer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/reviewer/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/reviewer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/reviewer/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/reviewer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/reviewer/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/sentinel | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/sentinel/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/sentinel | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/sentinel/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/sentinel | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/sentinel/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/sentinel | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/sentinel/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/sentinel | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/sentinel/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/sentinel | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/sentinel/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/tester | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/tester/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/tester | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/tester/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/tester | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/tester/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/tester | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/tester/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| dev/tester | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/dev/tester/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 40 | dev/analyst, dev/coder, dev/planner, dev/refactorer, dev/reviewer, dev/sentinel | agent_fix |

## Cohorte ops

- Workspaces auditados: 9
- `validate --profile strict` verde: si
- Hallazgos manuales: 68
- P1: 67 | P2: 1 | P3: 0

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| ops/ci-assistant | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/ci-assistant/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/ci-assistant | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/ci-assistant/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/ci-assistant | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/ci-assistant/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/ci-assistant | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/ci-assistant/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/ci-assistant | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/ci-assistant/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:25 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawmaster | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawmaster/AGENTS.md:27 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/clawstack | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawstack/AGENTS.md:68 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| ops/clawstack | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawstack/skills/CM-CONTEXT-MANAGER.md:13 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/clawstack | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/clawstack/skills/CM-LIFECYCLE-ORCHESTRATOR.md:13 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/deployer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/deployer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/deployer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/deployer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/deployer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/deployer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/deployer | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/deployer | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/deployer/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/integrador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/integrador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/integrador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/integrador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/integrador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/integrador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/integrador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/integrador/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/observer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/observer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/observer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/observer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/observer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/observer | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/skills/CM-CONTEXT-MANAGER.md:12 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/skills/CM-CONTEXT-MANAGER.md:22 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/skills/CM-CONTEXT-MANAGER.md:23 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/observer | Skill degenerado clasifica transiciones o continuidad FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/observer/skills/CM-CONTEXT-MANAGER.md:39 | Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral. | agent_fix |
| ops/orquestador-swarm | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/orquestador-swarm | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/orquestador-swarm | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/orquestador-swarm | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/orquestador-swarm | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/orquestador-swarm | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/orquestador-swarm | Skill compone otro skill operativamente | P2 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/skills/CM-CIRCUIT-BREAKER-MANAGER.md:25 | Eliminar la invocacion operativa a otro CM y mover la secuencia o routing a AGENTS.md; el skill solo debe usar criterios del dominio o la spec rectora. | agent_fix |
| ops/orquestador-swarm | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/orquestador-swarm/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/security | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/security | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/security | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/security | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/security | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/security | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/security | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/security | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/security/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| ops/verificador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/skills/CM-CONTEXT-MANAGER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |
| ops/verificador | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/ops/verificador/skills/CM-INTENT-CLASSIFIER.md:11 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 51 | ops/ci-assistant, ops/clawmaster, ops/deployer, ops/integrador, ops/observer, ops/orquestador-swarm | agent_fix |
| Skill degenerado recibe o emite estado FSM | P1 | 11 | ops/clawstack, ops/deployer, ops/integrador, ops/orquestador-swarm, ops/security, ops/verificador | agent_fix |
| Skill degenerado clasifica transiciones o continuidad FSM | P1 | 4 | ops/observer | agent_fix |
| Destino de control no declarado | P1 | 1 | ops/clawstack | agent_fix |
| Skill compone otro skill operativamente | P2 | 1 | ops/orquestador-swarm | agent_fix |

## Cohorte domains

- Workspaces auditados: 24
- `validate --profile strict` verde: si
- Hallazgos manuales: 111
- P1: 111 | P2: 0 | P3: 0

### Subgrupo gn

- Workspaces: 13
- Hallazgos: 72

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/ar-virtual/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/ar-virtual/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/ar-virtual/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/ar-virtual/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/ar-virtual/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/ar-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/ar-virtual/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/arquitecto-automatizacion-organizacional/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/arquitecto-automatizacion-organizacional/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/arquitecto-automatizacion-organizacional/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/arquitecto-automatizacion-organizacional/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/arquitecto-automatizacion-organizacional/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/arquitecto-automatizacion-organizacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/arquitecto-automatizacion-organizacional/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/asesor-juridico/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/asesor-juridico/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/asesor-juridico/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/asesor-juridico | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/asesor-juridico/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/banca-inversion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/banca-inversion/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/banca-inversion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/banca-inversion/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/banca-inversion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/banca-inversion/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/banca-inversion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/banca-inversion/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/banca-inversion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/banca-inversion/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:58 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/dgi-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/dgi-virtual/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/eacs | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/eacs/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/eacs | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/eacs/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/eacs | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/eacs/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/eacs | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/eacs/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/eacs | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/eacs/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/eacs | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/eacs/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/erp-gore | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/erp-gore/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/estratega-comunicacional | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:57 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/estratega-comunicacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/estratega-comunicacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/estratega-comunicacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/estratega-comunicacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/estratega-comunicacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/estratega-comunicacional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/estratega-comunicacional/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:59 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:61 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:67 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:25 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gestor-ipr-360 | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gestor-ipr-360/AGENTS.md:27 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gobernador-virtual/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gobernador-virtual/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gobernador-virtual/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/gobernador-virtual | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/gobernador-virtual/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/goreologo | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/goreologo/AGENTS.md:44 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/goreologo | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/goreologo/AGENTS.md:50 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| gn/goreologo | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/goreologo/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/goreologo | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/goreologo/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| gn/visionario | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/gn/visionario/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 65 | gn/ar-virtual, gn/arquitecto-automatizacion-organizacional, gn/asesor-juridico, gn/banca-inversion, gn/dgi-virtual, gn/eacs | agent_fix |
| Destino de control no declarado | P1 | 7 | gn/dgi-virtual, gn/estratega-comunicacional, gn/gestor-ipr-360, gn/goreologo | agent_fix |

### Subgrupo pro

- Workspaces: 4
- Hallazgos: 15

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| pro/abogado-legislacion-medica | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:49 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/abogado-legislacion-medica | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:55 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/abogado-legislacion-medica | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/abogado-legislacion-medica | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/abogado-legislacion-medica | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/abogado-legislacion-medica | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/abogado-legislacion-medica | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/abogado-legislacion-medica/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Destino de control no declarado | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:68 | Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| pro/medico-urgencias | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/pro/medico-urgencias/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 12 | pro/abogado-legislacion-medica, pro/medico-urgencias | agent_fix |
| Destino de control no declarado | P1 | 3 | pro/abogado-legislacion-medica, pro/medico-urgencias | agent_fix |

### Subgrupo fxsl

- Workspaces: 6
- Hallazgos: 23

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/arquitecto-sistemas-informacion | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/arquitecto-sistemas-informacion/AGENTS.md:25 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:21 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ingeniero-sistemas-composicional | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ingeniero-sistemas-composicional/AGENTS.md:23 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ontologista-gist/AGENTS.md:9 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ontologista-gist/AGENTS.md:11 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ontologista-gist/AGENTS.md:13 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ontologista-gist/AGENTS.md:15 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ontologista-gist/AGENTS.md:17 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |
| fxsl/ontologista-gist | Precedencia de transiciones no declarada | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/fxsl/ontologista-gist/AGENTS.md:19 | Anotar `[prioridad n]` en cada rama evaluable o declarar exclusion mutua explicita entre las condiciones del estado. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Precedencia de transiciones no declarada | P1 | 23 | fxsl/arquitecto-sistemas-informacion, fxsl/ingeniero-sistemas-composicional, fxsl/ontologista-gist | agent_fix |

### Subgrupo korvo

- Workspaces: 1
- Hallazgos: 1

| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |
|-----------|-------|-----|-----------|------------|--------|
| korvo/korax | Skill degenerado recibe o emite estado FSM | P1 | /Users/felixsanhueza/Developer/kora/AGENTS/korvo/korax/skills/CM-BANCARROTA.md:12 | Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md. | agent_fix |

Hallazgos repetidos:

| Regla | Sev | Casos | Workspaces | Cierre |
|-------|-----|-------|------------|--------|
| Skill degenerado recibe o emite estado FSM | P1 | 1 | korvo/korax | agent_fix |

## Rollout de enforcement

- Pasar a lint: Destino de control no declarado, Precedencia de transiciones no declarada, Skill compone otro skill operativamente, Skill degenerado clasifica transiciones o continuidad FSM, Skill degenerado recibe o emite estado FSM
- Mantener manual: ninguno

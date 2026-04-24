---
_manifest:
  urn: "urn:korvo:kb:korax-v2-primitivo-snapshot"
  provenance:
    created_by: "FS"
    created_at: "2026-04-23"
    source: "artifacts/knowledge/_SCRIPTORIUM/INBOX/korax-v2-primitivo/ — snapshot historico del agente korax v2.0 bajo el regimen legacy agentfile v1 (bootstrap_agents/bootstrap_user/SOUL/TOOLS); incluye AGENTS.md, config.json, SOUL.md, TOOLS.md, USER.md, skills/"
version: "2.0.0"
status: borrador
tags: [korax, v2-primitivo, snapshot, agentfile-v1, legacy, korvo]
lang: es
extensions:
  kora:
    family: note
relations:
  supersedes: []
  cites:
    - "urn:korvo:artefacto:korax"
---

# Korax v2 Primitivo — Snapshot Historico

## Naturaleza del artefacto

Registro historico del agente korax en su version 2.0.0 bajo el regimen legacy **agentfile v1** (pre-unification). Conserva la topologia `AGENTS.md + SOUL.md + USER.md + TOOLS.md + config.json + skills/` hoy deprecada por `autoria-spec v1.2`.

Esta nota existe por trazabilidad historica. El artefacto agentico productivo es `urn:korvo:artefacto:korax` (v2.0.0 migrado al shape unified) en `artifacts/agents/_FRAGUA/REVIEW/korax/AGENT.md`.

## Contenido original

El material fuente vive en `artifacts/knowledge/_SCRIPTORIUM/INBOX/korax-v2-primitivo/`:

- `AGENTS.md` — workflow y FSM WF-KORAX (13 estados + modificador `delegation_scope`).
- `SOUL.md` — identidad, tono, paradigma operativo.
- `USER.md` — bootstrap del operador (Felix).
- `TOOLS.md` — herramientas declaradas.
- `config.json` — configuracion OpenClaw.
- `skills/` — skills promovidas del workspace.

## FSM WF-KORAX (extracto)

| Estado | Descripcion | Modulo PCA |
|--------|-------------|------------|
| S_IDLE | Agente inactivo | — |
| S_CAPTURE | Procesando captura al buffer | Buffer |
| S_TRIAGE | Sesion de triaje asistido | Compuerta |
| S_PLAN | Planificacion matutina | Ejecucion |
| S_EXECUTE | Proteccion de bloque de ejecucion | Ejecucion |
| S_SYNC | Sincronizacion estrategica | Sincronizacion |
| S_CLOSE | Ritual de cierre vespertino | Ejecucion |
| S_CHAOS | Modo caos (agente silenciado) | Modo Caos |
| S_ABANDON | Reactivacion por abandono | Emergencia |
| S_COLLAPSE | Modo emergencia por colapso | Emergencia |
| S_ADVISE | Asesoria en dominio de vida | Vida |
| S_SOLVE | Resolucion estructurada | Vida |
| S_COMPANION | Acompanamiento empatico | Vida |

`delegation_scope` es fibra de U (no estado). Valores: `none`, `triage`, `plan`, `maintenance`, `full`.

## Estado

Este snapshot **NO** es reutilizable como agente activo: la FSM y el frontmatter requieren migracion a `autoria-spec v1.2`. Si se desea materializar esta FSM en el korax actual, incorporarla via promocion del agente con bump major a v3.0.

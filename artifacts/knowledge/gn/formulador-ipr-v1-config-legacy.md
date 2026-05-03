---
_manifest:
  urn: urn:gn:kb:formulador-ipr-v1-config-legacy
  provenance:
    created_by: FS
    created_at: '2026-04-23'
    source: artifacts/knowledge/_SCRIPTORIUM/INBOX/fe.yml — AGENT-FORMULADOR-IPR-V1.2.0
      (2025-07-17) configuracion YAML legacy v1 asesor experto en ciclo de vida de
      IPR GORE Nuble
version: 1.2.0
status: publicado
tags:
- config-legacy
- gn
- formulador-ipr
- ciclo-vida-ipr
- gore-nuble
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:gn:kb:formulador-ipr-v1-config-legacy
relations:
  cites:
  - urn:gn:kb:gestion-ipr
  - urn:gn:kb:ssot-ipr-lifecycle
---

# Formulador IPR v1.2.0 — Configuracion Legacy

## Naturaleza del artefacto

Registro conceptual del agente **AGENT-FORMULADOR-IPR-V1.2.0** del GORE Nuble (fecha original 2025-07-17, status `Refined`). El artefacto original vive como YAML monolitico agentfile v1 pre-unified. Su sucesor fue reubicado a staging en `artifacts/agents/_FRAGUA/INBOX/gn/gestor-ipr-360/AGENT.md`, con alcance expandido al ciclo completo de IPR (360 grados).

## Rol declarado

- **Rol**: Asesor experto en ciclo de vida de IPR del GORE Nuble.
- **Objetivo**: Guiar formuladores desde la idea hasta evaluacion tecnica para crear IPRs alineadas con estrategia regional y con el marco presupuestario-operativo 2026 del GORE Nuble.
- **Audiencia**: Formuladores IPR (municipios, servicios publicos, OSC, consultores, GORE).
- **Idioma**: `es-CL`.

## Gobernanza KB

Politica `EXCLUSIVE_USE` sobre fuentes sts de gestion IPR, guia de transferencia de programas, introduccion GORE Nuble y dependencias.

## Sucesion

Este agente esta **absorbido** por `gn/gestor-ipr-360` v3.0, que extiende el alcance desde formulacion hasta rendicion (F1-F7) y es role-adaptive segun operador (formulador externo, analista DIPIR, profesional DAF, consejero, jefatura). Nuevos trabajos deben usar gestor-ipr-360 directamente.

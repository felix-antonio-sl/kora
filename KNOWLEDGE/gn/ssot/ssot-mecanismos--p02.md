---
_manifest:
  urn: urn:gn:kb:ssot-mecanismos-p02
  provenance:
    created_by: FS
    created_at: '2026-03-10'
    source: omega_gore_nuble_mermaid.md v2.6.0, goreNubleIPRData.ttl, GORE_OS/CLAUDE.md
version: 1.1.1
status: published
tags:
- ssot
- mecanismos
- tracks
- fril
- frpd
- subv8
- c33
- ppr
- sni
- evaluacion
lang: es
extensions:
  gn:
    family: ssot
    bundle: urn:gn:kb:ssot-master
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:ssot-mecanismos
relations:
  cites:
  - urn:gn:kb:ssot-legal
---


# SSOT — Reglas operativas por mecanismo de financiamiento - Parte 02

## Restricciones operativas cruzadas

| Mecanismo | Restricción | Consecuencia |
|-----------|------------|--------------|
| FRIL | Fraccionamiento prohibido | Rechazo postulación |
| FRIL | Plazo licitación 90 días | Caducidad asignación |
| Glosa 06 | Admin GORE max 5% | Rechazo DIPRES |
| Transfer | Honorarios max 5% | Ajuste o rechazo |
| Subv8 | Rendiciones pendientes | Inhabilidad total (bloqueo) |
| C33 | Cofinanciamiento ANF 20% ([ver legal](urn:gn:kb:ssot-legal)) | Requisito habilitante |
| FRPD | Garantía >1.000 UTM | 5% total + 90d post-término |

## Catálogo unificado de mecanismos

| Track | Costo típico | Ejecutor | Plazo ejecución |
|-------|-------------|----------|----------------|
| A — SNI | >15K UTM | GORE/Terceros | 12-36 meses |
| B — C33 | Variable | GORE | Variable |
| C — FRIL | <4.545 UTM | Municipalidad | 12-18 meses |
| D1 — Glosa 06 | Variable | GORE (directo) | 8-12 meses |
| D2 — Transfer | <$15M típico | Entidad pública | 8-12 meses |
| E1 — Subv8 | <$8M | OSC/Municipio | 8-9 meses |
| E2 — FRPD | Variable | Inst. habilitada | ≤30 meses |

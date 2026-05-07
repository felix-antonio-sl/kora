---
_manifest:
  urn: urn:salud:kb:informatica-medica-normativa-chilena
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Zotero + web MINSAL. Leyes 21.663, 21.719, 21.541, 21.668, 21.180, 21.331.
      Decreto 12. RIS/SNI 2025.
  version: 1.0.0
version: 1.0.0
status: publicado
family: normative
tags:
- salud
- normativa
- chile
- interoperabilidad
- ciberseguridad
- hodom
lang: es
relations:
  cites:
  - urn:salud:kb:informatica-medica-indice
  - urn:salud:kb:hodom-reglamento-ds1-2022
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:informatica-medica-normativa-chilena
---

# Normativa Chilena de IT en Salud — HODOM-HSC

## Leyes aplicables

### Ley 21.668 — Interoperabilidad Ficha Clinica
Obliga interoperabilidad entre todos los prestadores. HODOM debe interoperar
con el sistema hospitalario. Estandares: HL7 FHIR R4, SNOMED CT, EMPI.

### Ley 21.541 — Salud Digital
Telemedicina reconocida. Receta electronica. Identidad digital del paciente.

### Ley 21.663 — Ciberseguridad
HODOM como servicio esencial: SGSI continuo, planes de continuidad certificables,
reporte de incidentes al CSIRT en <3h.

### Ley 21.719 — Datos Personales
Datos de salud = sensibles. Consentimiento, confidencialidad, derechos ARCO.

### Decreto 12 — Interoperabilidad
Arquitectura nacional, perfiles FHIR Core CL, servicios terminologicos.

### RIS/SNI 2025
Conjunto minimo de datos, estandares de codificacion, formatos de intercambio.

## Implicaciones para software HODOM-HSC

1. FHIR R4 nativo con perfiles Core CL chileno
2. SNOMED CT para codificacion clinica
3. SGSI + planes de continuidad documentados
4. Consentimiento informado digital y confidencialidad
5. Interoperabilidad bidireccional HODOM ↔ hospital

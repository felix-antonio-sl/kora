---
_manifest:
  urn: urn:salud:kb:estandares-it-receta-electronica
  provenance:
    created_by: FS
    created_at: '2026-05-08'
    source: SNRE IG 0.9.6 (MINSAL, draft). Ley 21.541 Salud Digital. consulta_reglamento_receta_electronica.pdf
  version: 1.0.0
version: 1.0.0
status: publicado
family: note
tags:
- salud
- receta-electronica
- snre
- fhir
- interoperabilidad
- chile
lang: es
relations:
  cites:
  - urn:salud:kb:estandares-it-indice
  - urn:salud:kb:informatica-medica-normativa-chilena
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:estandares-it-receta-electronica
---

# Receta Electronica — SNRE v0.9.6

Sistema Nacional de Receta Electronica. Guia de Implementacion FHIR para
prescripcion electronica en Chile.

## Marco legal

- **Ley 21.541** (Salud Digital, 2024): establece la receta electronica como obligatoria
- **Reglamento en consulta publica** (2026): detalla requisitos tecnicos
- **SNRE** v0.9.6: guia FHIR para implementacion

## Recursos FHIR involucrados

| Recurso | Uso |
|---------|-----|
| **MedicationRequest** | Prescripcion del medico |
| **Medication** | Medicamento especifico |
| **MedicationDispense** | Dispensacion en farmacia |
| **Patient** | Paciente (con RUN) |
| **Practitioner** | Medico prescriptor (con RUN) |
| **PractitionerRole** | Rol y lugar de prescripcion |
| **Coverage** | Cobertura (FONASA, ISAPRE) |

## Flujo de receta electronica

1. **Prescripcion**: medico crea MedicationRequest en sistema clinico (HODOM)
2. **Validacion**: CDSS verifica interacciones, alergias, dosis
3. **Firma**: firma electronica avanzada del medico
4. **Transmision**: a repositorio nacional (SNRE)
5. **Dispensacion**: farmacia consulta SNRE y dispensa
6. **Registro**: MedicationDispense confirma dispensacion

## Implicaciones para HODOM-HSC

- El medico HODOM prescribe en domicilio → receta electronica obligatoria
- Medicamentos administrados por cuidador → deben quedar registrados en SNRE
- Medicacion EV ambulatoria → prescribe igual que cualquier receta
- Opioides y controlados → receta retenida con receta electronica (doble via)
- Firma electronica: el medico HODOM necesita token o clave unica

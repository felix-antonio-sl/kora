---
_manifest:
  urn: urn:salud:kb:estandares-it-core-cl
  provenance:
    created_by: FS
    created_at: '2026-05-08'
    source: 'Guia de Implementacion Core CL FHIR R4 v1.9.4 (MINSAL, trial-use). Web:
      cl_core_1_9_4.html'
  version: 1.0.0
version: 1.0.0
status: publicado
family: note
tags:
- salud
- fhir
- core-cl
- chile
- interoperabilidad
- perfil
lang: es
relations:
  cites:
  - urn:salud:kb:estandares-it-indice
  - urn:salud:kb:informatica-medica-normativa-chilena
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:estandares-it-core-cl
---

# Core CL — Perfil FHIR Chileno v1.9.4

Guia de Implementacion del perfil base FHIR R4 para Chile. Define las
restricciones y extensiones sobre los recursos FHIR estandar para el
contexto normativo y operacional chileno.

## Recursos perfilados

### Paciente (Patient)

Extensiones chilenas obligatorias:
- **RUN**: Rol Unico Nacional como identificador primario (no usar MRN generico)
- **Nacionalidad**: extension para nacionalidad chilena o extranjera
- **Pueblo originario**: pertenencia a pueblo indigena reconocido por CONADI
- **Prevision**: FONASA, ISAPRE, FFAA, particular (usando Coverage)
- **Direccion**: formato chileno (calle, numero, comuna, region)
- **Telefono**: formato +56

Restricciones:
- `identifier.system` = `https://api.minsal.cl/v1/fhir/masterfile/run`
- `identifier.value` = RUN sin puntos, con digito verificador
- `name` al menos un nombre oficial
- `gender` obligatorio (male | female | other | unknown)

### Prestador (Practitioner)

- **RUN** como identificador profesional
- **Especialidad**: codificada con SNOMED CT o catalogo MINSAL
- **Registro**: numero de registro profesional (Superintendencia de Salud)
- **Organizacion**: referencia al PractitionerRole con la Organization

### Organizacion (Organization)

- **Codigo DEIS**: identificador unico del establecimiento
- **Tipo**: hospital, consultorio, CESFAM, CECOSF, HODOM, etc.
- **SSR**: Servicio de Salud de Referencia
- **Comuna**: codigo territorial MINSAL

### Documento Clinico (DocumentReference)

- **Tipo**: epicrisis, nota evolucion, informe, receta, interconsulta
- **Especialidad**: codificada SNOMED CT
- **Establecimiento**: codigo DEIS
- **Periodo**: fecha de atencion

## Extensiones Core CL para HODOM

Para HODOM-HSC especificamente:
- `hodom-episode`: extension para episodio de hospitalizacion domiciliaria
- `hodom-caregiver`: cuidador principal como RelatedPerson
- `hodom-visit`: recurso Encounter con tipo HOME (domicilio)
- `hodom-device`: dispositivos medicos en domicilio (Device)

## Niveles de conformidad

| Nivel | Descripcion | Requerido para |
|-------|-------------|----------------|
| **SHALL** | Obligatorio en todos los sistemas | RUN, DEIS, genero |
| **SHOULD** | Recomendado | Nacionalidad, prevision, pueblo originario |
| **MAY** | Opcional | Extensiones especificas de dominio |

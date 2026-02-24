---
_manifest:
  urn: urn:tde:kb:metadatos-documentos
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- transformacion-digital
- metadatos
- gestion-documental
- expediente-electronico
- chile
- tde
lang: es
---

# Guía Técnica de Metadatos para Documentos y Expedientes

## Contexto y Marco Normativo
- Operacionaliza la Norma Técnica de Documentos y Expedientes Electrónicos (DS 10/2023) bajo la Ley 21.180 (Transformación Digital).
- Basada en estándares internacionales ISO 15489 (Gestión de documentos) e ISO 23081 (Metadatos para gestión de documentos).
- Aplica a todos los órganos de la administración del Estado (OAE).


## Propósito de los Metadatos
- Garantizar disponibilidad, recuperación, accesibilidad, conservación e interoperabilidad de la información pública.
- Permiten descripción precisa del contexto, estructura y contenido de documentos y expedientes electrónicos durante todo su ciclo de vida, incluyendo su transferencia al Archivo Nacional.


## Modelo de Entidades
- **Expediente**: conjunto organizado de documentos de un procedimiento administrativo.
- **Documento**: unidad de información registrada en un expediente.
- **Actor**: institución o persona responsable de creación, custodia o gestión.
- **Relación**: asociación entre entidades relevante para la gestión documental.

## Clasificación de Metadatos
### Niveles de Obligatoriedad
- **Obligatorios**: esenciales; deben estar presentes siempre.
    - Expedientes: 18 elementos.
    - Documentos: 12 elementos.
- **Condicionales**: obligatorios si se cumple una condición específica documentada.
    - Expedientes: 5 elementos.
    - Documentos: 16 elementos.
- **Sugeridos**: complementarios para descripciones detalladas.
    - Expedientes: 6 elementos.
    - Documentos: 18 elementos.

### Indicadores Especiales
- **AN**: requeridos por el Archivo Nacional para transferencia digital.
- **MU**: permiten múltiples valores (ej. múltiples actores relacionados).

## Estructura de Metadatos (Resumen)
### Grupos para Expedientes (29 elementos totales)
- **Identificación**: ID único, código de serie, número, estado, título.
- **Descripción**: resumen, asunto global.
- **Temporalidad**: fechas de creación y finalización (formato ISO 8601).
- **Caracterización**: tipo de expediente, mecanismo de incorporación.

### Grupos para Documentos (46 elementos totales)
- **Identificación y Descripción**: similares a expediente, nivel unidad.
- **Técnicos**: tamaño (Kb), formato, soporte.
- **Seguridad**: firma electrónica, niveles de acceso.
- **Relacionales**: vínculo con expediente y otros documentos.

## Obligaciones de Implementación
- **Permanencia**: metadatos deben conservarse mientras exista el documento/expediente.
- **No sobrescritura**: prohibido destruir trazabilidad en plataformas de gestión.
- **Estandarización**: usar formatos XML/JSON alineados a la Norma Técnica para interoperabilidad.
- **Fechas**: uso obligatorio de ISO 8601 (aaaa-mm-dd hh:mm:ss).
- **Gestión**: cambios al esquema deben pasar por control de cambios formal.

## Recomendaciones Técnicas
- Diseñar interfaces que minimicen errores de registro en metadatos obligatorios.
- Documentar extensiones locales del modelo de metadatos institucional.
- Asegurar exportación compatible con sistemas del Archivo Nacional.
- Implementar modelos de datos que reflejen flags AN (Archivo Nacional) y MU (Múltiple).

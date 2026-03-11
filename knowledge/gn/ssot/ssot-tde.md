---
_manifest:
  urn: "urn:gnub:kb:ssot-tde"
  provenance:
    created_by: "FS"
    created_at: "2026-03-10"
    source: "Ley 21.180, Ley 19.799, digital.gob.cl, omega_gore_nuble_mermaid.md v2.6.0"
version: "1.0.0"
status: draft
tags: [ssot, tde, transformacion-digital, fea, gesdoc, interoperabilidad, clave-unica]
lang: es
extensions:
  gnub:
    family: ssot
    bundle: "urn:gnub:kb:ssot-master"
---

# SSOT — Transformación Digital del Estado (TDE)

## Resumen

Marco de digitalización del Estado chileno aplicado al GORE Ñuble. Ley 21.180 obliga procedimientos electrónicos, FEA, expedientes digitales e interoperabilidad. Plazo implementación total: 31 dic 2027. 8 conceptos clave, 6 plataformas relevantes. Dominio mayoritariamente externo al GORE — solo ESP_TD en DGI gestiona la implementación interna.

## TDE — Definición

Proceso impulsado por la Ley 21.180 que obliga a todos los órganos de la Administración del Estado a realizar procedimientos administrativos en formato electrónico. Elimina el papel. Incluye expedientes electrónicos, firma electrónica, interoperabilidad y notificaciones digitales.

## Ley 21.180 — Transformación Digital del Estado

| Atributo | Valor |
|----------|-------|
| Publicación | 11 de noviembre de 2019 |
| Reglamento | 11 de diciembre de 2021 |
| Vigencia | 9 de junio de 2022 (180 días post-reglamento) |
| Plazo implementación total | 31 de diciembre de 2027 (Ley 21.464, 6 fases en 4 años) |

### Obligaciones para GOREs

- Caracterizar procedimientos administrativos
- Comunicaciones oficiales electrónicas vía plataforma
- Expedientes electrónicos
- Inicio digital de procedimientos
- Interoperabilidad vía PISEE
- FEA obligatoria para actos administrativos

## FEA (Firma Electrónica Avanzada)

Firma electrónica certificada por prestador acreditado. Creada con medios bajo exclusivo control del titular. Vincula unívocamente al firmante y detecta modificaciones posteriores.

| Atributo | Valor |
|----------|-------|
| Base legal | Ley 19.799 (Documentos Electrónicos y Firma Electrónica) |
| Validez | Instrumento público — presunción legal de autoría e integridad |
| Obligatoriedad post-TDE | Actos administrativos del Estado requieren FEA |

Uso en GORE Ñuble: firma de Gobernador/a en resoluciones, firma de Encargado Ejecutor y Encargado Otorgante en rendiciones SISREC.

[impl: CLAUDE.md §Rule 32 — SecurityHeadersMiddleware. GORE_OS no implementa FEA directamente — depende de certificadores externos]

## Documento electrónico oficial

Toda representación de un hecho, imagen o idea creada, enviada, comunicada o recibida por medios electrónicos, almacenada de modo idóneo para uso posterior (Ley 19.799).

Documentos con FEA de todos los intervinientes: calidad de instrumento público. FEA simple admisible para comunicaciones; FEA avanzada requerida para instrumentos públicos.

## Expediente electrónico

Sistema donde escritos, documentos, actos y actuaciones del procedimiento administrativo se registran electrónicamente (Ley 21.180). Garantiza registro íntegro, orden sucesivo, fidelidad, preservación y reproducción.

## GESDOC (Gestión Documental Electrónica)

Categoría genérica — no es un software único. Implementaciones:

| Sistema | Proveedor | Función |
|---------|-----------|---------|
| SGDOC | Subsecretaría de Hacienda | Software público de gestión documental |
| DocDigital | División de Gobierno Digital (SEGPRES) | Comunicaciones oficiales electrónicas (oficios, resoluciones, dictámenes) |

Guía Técnica de Gestión Documental del Estado (Archivo Nacional + Hacienda + SEGPRES) define estándares mínimos.

En GORE Ñuble: Oficina de Partes asigna número registro SGDOC.

## Clave Única

Contraseña única para identificación digital de ciudadanos ante el Estado chileno. Provee Identidad Electrónica Única (RUN + clave).

| Atributo | Valor |
|----------|-------|
| Proveedor | Servicio de Registro Civil e Identificación |
| Administrador | División de Gobierno Digital (SEGPRES) |
| Alcance | +1.000 trámites en distintas instituciones |
| Obtención | Presencial o 100% en línea |

[impl: GORE_OS no integra Clave Única — listado como gap en CLAUDE.md §Coverage]

## Interoperabilidad / PISEE

Capacidad de sistemas heterogéneos del Estado para intercambiar procesos o datos.

| Plataforma | Descripción |
|-----------|-------------|
| PISEE 1.0 | Modelo centralizado (operativo desde 2009) |
| PISEE 2.0 | Modelo descentralizado — nodos de interoperabilidad en cada organismo |

Red de interoperabilidad: conexiones directas y seguras vía internet. Organismos como proveedores/consumidores de datos.

[impl: GORE_OS no integra PISEE — listado como gap en CLAUDE.md §Coverage]

## Plataformas digitales relevantes para GORE

| Plataforma | Administrador | Uso GORE |
|-----------|--------------|----------|
| SISREC | CGR | Rendiciones de cuentas |
| BIP | MDSF (SNI) | Registro de iniciativas de inversión |
| SIGFE | DIPRES | Contabilidad y ejecución presupuestaria |
| Mercado Público | ChileCompra | Compras y licitaciones públicas |
| DocDigital | Gob. Digital | Comunicaciones oficiales |
| Clave Única | Registro Civil | Autenticación ciudadana |

## Rol DGI en TDE

ESP_TD (Especialista en Transformación Digital, sort_order 8) lidera la implementación interna. [ver roles DGI](urn:gnub:kb:ssot-dgi)

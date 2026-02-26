---
_manifest:
  urn: urn:gov:kb:datosgob
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: wikiguias.digital.gob.cl
version: 2.0.0
status: published
tags:
- datos-abiertos
- plataforma-compartida
- gobierno-digital
- chile
- knowledge
lang: es
---

# Portal de Datos Abiertos del Estado — Datos.gob.cl

Fuente: WikiGuías SGD — `urn:gov:kb:datosgob`
URL: https://datos.gob.cl/
Responsable: Secretaría de Gobierno Digital (SGD), Ministerio de Hacienda.

## Contexto y Definiciones

Datos.gob.cl es el portal de datos abiertos de la SGD. Centraliza catálogos y conjuntos de datos abiertos de los órganos de la Administración del Estado, financiados con recursos públicos, disponibles sin restricciones indebidas de uso.

| Término | Definición |
|---|---|
| Dato abierto | Dato digital con características técnicas y jurídicas que permiten su uso, reutilización y redistribución libre por cualquier persona u órgano del Estado, en cualquier momento y lugar |
| Catálogo de datos abiertos | Repositorio que centraliza, almacena y disponibiliza conjuntos de datos abiertos, estructurados y descritos por metadatos |
| Conjunto de datos abiertos | Colección de datos en formatos de uso común, relacionados entre sí y descritos por sus metadatos |

Objetivos del portal:
- Facilitar acceso, uso, reutilización y redistribución de datos públicos
- Impulsar transparencia, participación e innovación a partir de datos del Estado
- Alinear publicación de datos con estándares internacionales de datos abiertos

## Estándares y Requisitos

Aplican a los datos y conjuntos publicados en Datos.gob.cl y a plataformas institucionales de datos abiertos.

Requisitos de publicación:
- Los portales o plataformas institucionales de datos abiertos deben garantizar que sus datos estén referenciados y sincronizados en la plataforma de la SGD.
- Los datos abiertos deben publicarse en formatos abiertos que alcancen al menos 3 estrellas en la clasificación de Tim Berners-Lee, privilegiando formatos no propietarios.
- Cada catálogo, conjunto de datos y recurso debe describirse mediante metadatos estructurados (DCAT y Dublin Core) incluyendo al menos: título, descripción, cobertura, fechas, responsable, frecuencia de actualización y URL de acceso.

## Metadatos por Nivel

### Catálogo

| Metadato | Descripción | Nivel | Ejemplo |
|---|---|---|---|
| Cobertura geográfica | Ámbito geográfico de los datos del catálogo (País, Región, Provincia, Comuna) | Recomendado | Chile, Región Metropolitana |
| N° visitas | Visitas acumuladas al catálogo | Recomendado | 1000 |

### Conjunto de Datos

| Metadato | Descripción | Nivel | Ejemplo |
|---|---|---|---|
| Fecha de la versión | Fecha de la edición de la versión | Obligatorio | 2023-01-01 |

### Recurso

| Metadato | Descripción | Nivel | Ejemplo |
|---|---|---|---|
| Diccionario de variables | Lista de campos que contiene un recurso tabular (no aplica a distribuciones que no sean tablas) | Obligatorio | fecha, estación, temperatura_max, temperatura_min |
| Formato del recurso | Formato del archivo del recurso | Recomendado | CSV |

## Licenciamiento

Requisitos:
- Los datos y conjuntos de datos abiertos de los OAEs deben ponerse a disposición mediante licencias de dominio público o licencias abiertas que permitan uso y reutilización amplia.
- En ausencia de asignación explícita, los conjuntos de datos se aperturan bajo licencia Creative Commons Zero (CC0 1.0).
- Cuando sea necesario usar una licencia distinta, la entidad debe solicitar y justificar esta situación ante la SGD.

Licencias compatibles recomendadas: PDDL-1.0, CC BY 4.0, ODC-By 1.0.

## Uso en Proyectos TIC (EVALTIC)

Referencia: Guía Técnica EVALTIC (`urn:tde:kb:guia-evaltic`).

Requisitos:
- Si una iniciativa TIC requiere publicar conjuntos de datos, debe contemplar la publicación directa o vía servicios en Datos.gob.cl.
- Al formular proyectos TIC, las instituciones deben evaluar siempre el uso de plataformas y servicios compartidos provistos por la SGD: Datos.gob, ClaveÚnica, DocDigital, SIMPLE, FirmaGob y PISEE.

Recomendación: incorporar explícitamente la publicación en Datos.gob.cl en la formulación y seguimiento de proyectos TIC evaluados a través de EVALTIC.

## Gobernanza y Habilitación Institucional

Recomendaciones:
- Designar responsables institucionales para la administración del catálogo y publicaciones en Datos.gob.cl.
- Coordinar con la SGD los pasos formales y técnicos para la integración inicial (vía CeroFilas y capacitaciones específicas).
- Alinear la gobernanza de datos abiertos con los roles y estructuras definidas en el marco MGDE y en la Estrategia de Datos de la Administración del Estado.
- Tratar catálogos y conjuntos publicados en Datos.gob.cl como activos dentro del marco MGDE, con responsables, clasificaciones y políticas de actualización.
- Incorporar metas de publicación y reutilización de datos abiertos en el Plan de Transformación Digital institucional (STD 2025).

## Articulación con Marco TDE

XRef relacionados:
- `urn:tde:kb:guia-marco-gestion-datos` — Marco de Gestión de Datos del Estado
- `urn:gov:kb:datos-administracion-estado` — Estrategia de Datos
- `urn:tde:kb:guia-sistema-tde-2025` — Sistema TDE 2025
- `urn:tde:kb:guia-evaltic` — Evaluación TIC

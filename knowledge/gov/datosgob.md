---
_manifest:
  urn: "urn:gov:kb:datosgob"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "wikiguias.digital.gob.cl"
version: "2.0.0"
status: published
tags: [datos-abiertos, plataforma-compartida, gobierno-digital, chile]
lang: es
---

# Portal de Datos Abiertos (Datos.gob.cl)

Plataforma central del Estado chileno para la publicación de catálogos y conjuntos de datos abiertos bajo estándares de interoperabilidad y licencias libres.

## Definiciones Base

| Término | Definición |
| :--- | :--- |
| Dato Abierto | Dato digital con características técnicas y jurídicas para uso, reutilización y redistribución libre. |
| Catálogo | Repositorio que centraliza y disponibiliza conjuntos de datos estructurados. |
| Conjunto de Datos | Colección de datos representados en formatos comunes y descritos por metadatos. |

## Objetivos Estratégicos
* Garantizar acceso y reutilización de datos públicos.
* Impulsar transparencia e innovación ciudadana.
* Estandarizar la publicación según marcos internacionales.

## Requisitos de Publicación
* **Referenciación:** Plataformas institucionales deben sincronizarse con Datos.gob.cl.
* **Calidad:** Mínimo 3 estrellas (Tim Berners-Lee); privilegiar formatos no propietarios.
* **Metadatos:** Uso obligatorio de esquemas estructurados (DCAT, Dublin Core).
* **Licenciamiento:** Predominio de dominio público o Creative Commons Zero (CC0 1.0). Uso de otras licencias requiere justificación ante SGD.

## Metadatos Estándar

### Nivel Catálogo
| Metadato | Requisito | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| Cobertura geográfica | Recomendado | Ámbito geográfico (País, Región, Comuna) | Chile, Santiago |
| N° visitas | Recomendado | Acumulado de interacciones | 1000 |

### Nivel Conjunto de Datos
| Metadato | Requisito | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| Fecha de versión | Obligatorio | Fecha de edición de la versión actual | 2023-01-01 |

### Nivel Recurso
| Metadato | Requisito | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| Diccionario variables | Obligatorio | Lista de campos para recursos tabulares | fecha, temperatura |
| Formato del recurso | Recomendado | Extensión del archivo | CSV |

## Integración en Proyectos TIC
* **Evaluación EVALTIC:** Iniciativas que generen datos deben considerar su publicación en Datos.gob.cl.
* **Priorización:** Evaluar uso de Datos.gob como servicio compartido antes de desarrollar soluciones propias.

## Gobernanza e Implementación
* **Responsables:** Designar administradores institucionales para el catálogo.
* **Coordinación:** Trámites iniciales vía CeroFilas y capacitaciones con SGD.
* **Alineación:** Integrar con el Marco para la Gestión de Datos del Estado (MGDE) y el Plan de Transformación Digital (STD 2025).

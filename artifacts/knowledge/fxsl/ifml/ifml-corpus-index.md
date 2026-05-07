---
_manifest:
  urn: urn:fxsl:kb:ifml-corpus-index
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Sintesis del corpus IFML koraficado a partir de Ifml-In-A-Nutshell (manual
      del estandar IFML/OMG); INBOX/ifml-in-a-nutshell-fx.md
version: 1.0.0
status: publicado
tags:
- ifml
- omg
- frontend
- modeling
- indice
- corpus
lang: es
extensions:
  kora:
    family: note
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:fxsl:kb:ifml-corpus-index
relations:
  cites:
  - urn:fxsl:kb:ifml-fundamentos
  - urn:fxsl:kb:ifml-view-containers
  - urn:fxsl:kb:ifml-view-components
  - urn:fxsl:kb:ifml-actions-events
  - urn:fxsl:kb:ifml-extensiones-desktop
  - urn:fxsl:kb:ifml-extensiones-web
  - urn:fxsl:kb:ifml-extensiones-mobile
  - urn:fxsl:kb:ifml-patrones
---

# Corpus IFML — indice

Indice de la capa de conocimiento KORA sobre **IFML (Interaction Flow Modeling Language)**, estandar OMG basado en MDA para la especificacion del front-end de aplicaciones interactivas independientemente de su realizacion tecnologica.

Los nombres de constructos IFML se preservan en ingles (`ViewContainer`, `ViewComponent`, `NavigationFlow`, etc.) por ser terminos del estandar OMG. La prosa explicativa y los patrones se entregan en español.

## Alcance del corpus

IFML modela cinco aspectos de la interfaz:

- composicion de la vista (`ViewContainer` y anidamiento)
- contenido publicado (`ViewComponent`, `DataBinding`, `ContentBinding`)
- eventos soportados (`ViewElementEvent`, `ActionEvent`, `SystemEvent`)
- acciones disparadas (`Action`, `ActionEvent`)
- bindings entre interfaz y logica de negocio (`ParameterBinding`, `ParameterBindingGroup`)

Todos los aspectos se condensan en un unico tipo de diagrama: el **Interaction Flow Diagram**.

<!-- kora-canario-marker: 2026-05-07-ifml-deep-opm-pro-baseline-v1 -->

## Mapa de artefactos

| Capa | URN | Familia | Cubre |
| --- | --- | --- | --- |
| Fundamentos | [`urn:fxsl:kb:ifml-fundamentos`](urn:fxsl:kb:ifml-fundamentos) | guide | Principios de diseño, MVC, ejemplo Bookstore, rol de IFML en el ciclo de desarrollo |
| Composicion de la UI | [`urn:fxsl:kb:ifml-view-containers`](urn:fxsl:kb:ifml-view-containers) | guide | `ViewContainer`, anidamiento, `Window`, `Context`, `Viewpoint`, patrones organizativos OD/OW/OM |
| Contenido y navegacion | [`urn:fxsl:kb:ifml-view-components`](urn:fxsl:kb:ifml-view-components) | guide | `ViewComponent`, `DataBinding`, `ParameterBinding`, `Form`, patrones CN/DE/CS |
| Acciones y eventos | [`urn:fxsl:kb:ifml-actions-events`](urn:fxsl:kb:ifml-actions-events) | guide | `Action`, `ActionEvent`, `SystemEvent`, patrones CM (Object Creation/Deletion/Modification, Notification) |
| Extensiones desktop | [`urn:fxsl:kb:ifml-extensiones-desktop`](urn:fxsl:kb:ifml-extensiones-desktop) | guide | `OnFocusLost`, drag & drop, `Tree`, `Table`, `EditableSelectionField` |
| Extensiones web | [`urn:fxsl:kb:ifml-extensiones-web`](urn:fxsl:kb:ifml-extensiones-web) | guide | `Page`, `Area`, `SiteView`, `WebNavigationFlow`, `DynamicSortedList`, `ScrollableList`, `NestedList` |
| Extensiones mobile | [`urn:fxsl:kb:ifml-extensiones-mobile`](urn:fxsl:kb:ifml-extensiones-mobile) | guide | Context dimensions, `MapView`, `Marker`, `Path`, gestos, multiscreen |
| Catalogo de patrones | [`urn:fxsl:kb:ifml-patrones`](urn:fxsl:kb:ifml-patrones) | catalog | Tabla cifrada de patrones (O*, CN-*, DE-*, CS-*, CM-*, IA-*, SES-*, SOC-*, GEO-*) |

## Convencion de nombres

Los patrones IFML usan codigo `XY-Z`:

- **X**: categoria del patron (`O` interface organization, `CN` content/navigation, `DE` data entry, `CS` content search, `CM` content management, `IA` identity/auth, `SES` session, `SOC` social, `GEO` geo).
- **Y**: plataforma de origen (`D` desktop, `W` web, `M` mobile). Omitido si el patron es cross-platform.
- **Z**: mnemonico del patron especifico.

Ejemplo: `OD-SWA` = Organization, Desktop, Simple Work Area.

## Procedencia

Fuente unica del corpus: `Ifml-In-A-Nutshell` (libro de referencia del estandar IFML, Brambilla & Fraternali). El material original esta en ingles; la koraficacion preserva los nombres de constructos del estandar y traduce la prosa explicativa al español.

## Aplicabilidad

Este corpus alimenta la skill IFML (con capacidades de diagnostico, diseño y aplicacion de soluciones IFML durante el desarrollo de aplicaciones interactivas: web, desktop, mobile, multiscreen). La skill se construye en una fase posterior; mientras tanto el corpus puede consultarse directamente como referencia tecnica.

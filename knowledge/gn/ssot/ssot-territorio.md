---
_manifest:
  urn: "urn:gnub:kb:ssot-territorio"
  provenance:
    created_by: "FS"
    created_at: "2026-03-10"
    source: "goreNubleOrgData.ttl, omega_gore_nuble_mermaid.md v2.6.0, Ley 21.033"
version: "1.0.0"
status: draft
tags: [ssot, territorio, provincias, comunas, nuble]
lang: es
extensions:
  gnub:
    family: ssot
    bundle: "urn:gnub:kb:ssot-master"
---

# SSOT — Territorio GORE Ñuble

## Resumen

Región de Ñuble: 3 provincias, 21 comunas. Creada por Ley 21.033 (2017, vigencia 2018) por escisión de la Provincia de Ñuble desde la Región del Biobío. Superficie 13.178,5 km². Capital: Chillán. Sin conflictos entre fuentes — datos estables y consistentes.

## Ficha territorial

| Atributo | Valor | Fuente |
|----------|-------|--------|
| Creación | Ley 21.033 (promulgada 05-09-2017, vigencia 06-09-2018) | Ley 21.033 |
| Origen | Escisión Provincia de Ñuble desde Región del Biobío | Ley 21.033 |
| Superficie | 13.178,5 km² (menor región continental) | INE |
| Población | 512.289 habitantes (Censo 2017) | INE |
| Capital | Chillán | Ley 21.033 |
| Provincias | 3 | Ley 21.033 |
| Comunas | 21 | Ley 21.033 |
| Índice envejecimiento | 97,6 (vs 79,0 nacional) | CASEN |
| Ruralidad | 28,7% (vs 11,3% nacional) | INE |
| Pobreza por ingresos | 12,1% (vs 6,5% nacional) | CASEN |

## Provincias y comunas

### Provincia de Diguillín

Capital: Bulnes. 9 comunas.

Chillán, Chillán Viejo, Bulnes, El Carmen, Pemuco, Pinto, Quillón, San Ignacio, Yungay.

### Provincia de Itata

Capital: Quirihue. 7 comunas.

Cobquecura, Coelemu, Ninhue, Portezuelo, Quirihue, Ránquil, Tréguaco.

### Provincia de Punilla

Capital: San Carlos. 5 comunas.

Coihueco, Ñiquén, San Carlos, San Fabián, San Nicolás.

## Tipos de impacto territorial

Definidos en GORE_OS (`core.ipr_territory`), 4 tipos de impacto per IPR. Ontología no los modela — extensión de implementación.

[impl: `GET /api/catalogs/territories` retorna 25 entidades (3 provincias + 21 comunas + 1 región). UNIQUE constraint `uq_ipr_territory_impact`. CLAUDE.md §Rule 17]

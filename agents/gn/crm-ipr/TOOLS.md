---
_manifest:
  urn: "urn:gn:agent-bootstrap:crm-ipr-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB -> LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Ciclo IPR, IDI, BIP, fases proyecto | urn:gn:kb:gestion-ipr |
| Seleccion FNDR/FRPD/FRIL, que fondo usar | urn:gn:kb:selector-ipr |
| PPR, transferencias, convenios terceros | urn:gn:kb:transferencia-ppr |
| Rendiciones, SISREC, CGR, documentos cierre | urn:gn:kb:gestion-rendiciones |
| Formulacion IDI, fichas SNI, requisitos tecnicos | urn:gn:kb:guia-idi-sni-sts |
| Programas directos GORE | urn:gn:kb:guia-programas-directos-gore |
| FRIL 2025, iniciativas locales, municipios | urn:gn:kb:guia-fril-2025-sts |
| FRPD, productividad, diversificacion | urn:gn:kb:guia-frpd-nuble |
| Subvencion Art. 8, 2025 | urn:gn:kb:instructivo-subvencion-8-2025-sts |
| Circular 33, requisitos tecnicos STS | urn:gn:kb:guia-circular-33-sts |
| RIS, requisitos sectoriales, metodologias | urn:gn:kb:ris-index |
| RIS proyectos inversion | urn:gn:kb:ris-proyinv |
| ERD, ejes estrategicos, alineacion regional | urn:gn:kb:erd-nuble-2024-2030 |

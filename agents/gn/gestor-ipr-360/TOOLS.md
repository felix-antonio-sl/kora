---
_manifest:
  urn: "urn:gn:agent-bootstrap:gestor-ipr-360-tools:2.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Resolution mode: DYNAMIC_LOOKUP.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB -> LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

### Marco Institucional

| Topic | URN |
|-------|-----|
| Estructura/Competencias GORE | urn:gn:kb:intro-gores-nuble |
| LOC GORE/Autoridades | urn:gn:kb:loc-gore |
| Marco Legal Financiero | urn:gn:kb:marco-legal-gores |

### Formulacion IPR

| Topic | URN |
|-------|-----|
| Selector/Mecanismos | urn:gn:kb:selector-ipr |
| IDI/SNI/MDSF | urn:gn:kb:guia-idi-sni-sts |
| PPR Transferencia | urn:gn:kb:transferencia-ppr |
| Programas Glosa 06 | urn:gn:kb:guia-programas-directos-gore |
| FRIL | urn:gn:kb:guia-fril-2025-sts |
| FRPD/Innovacion | urn:gn:kb:guia-frpd-nuble |
| 8%/Subvenciones | urn:gn:kb:instructivo-subvencion-8-2025-sts |
| Circular 33/Estudios | urn:gn:kb:guia-circular-33-sts |

### RIS Sectoriales

| Topic | URN |
|-------|-----|
| Indice RIS | urn:gn:kb:ris-index |
| Arte/Cultura | urn:gn:kb:ris-artcult |
| Deportes | urn:gn:kb:ris-deportes |
| Edificacion | urn:gn:kb:ris-edpub |
| Empresas Publicas | urn:gn:kb:ris-empub |
| Patrimonio | urn:gn:kb:ris-patrimonio |
| PMDT | urn:gn:kb:ris-pmdt |
| Programas Inversion | urn:gn:kb:ris-proginv |
| Proyectos Inversion | urn:gn:kb:ris-proyinv |

### Gestion Operacional

| Topic | URN |
|-------|-----|
| Presupuesto/SIGFE | urn:gn:kb:gestion-prpto |
| Ciclo Vida IPR 7 Fases | urn:gn:kb:gestion-ipr |
| Rendiciones/SISREC | urn:gn:kb:gestion-rendiciones |

### Estrategia y Sistemas

| Topic | URN |
|-------|-----|
| Estrategia/Modernizacion | urn:gn:kb:estrategia-gestion |
| Geoespacial/SIG | urn:gn:kb:gestion-info-geoespacial |
| Vision GORE | urn:gn:kb:gore-ideal |

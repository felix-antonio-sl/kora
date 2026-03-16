---
_manifest:
  urn: "urn:gn:agent-bootstrap:gestor-ipr-360-tools:3.0.0"
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
| RIS Transporte | urn:gn:kb:ris-transporte |
| RIS Vivienda y Urbanismo | urn:gn:kb:ris-vivienda-urbanismo |
| RIS Agua y Saneamiento | urn:gn:kb:ris-agua-saneamiento |
| RIS Vialidad | urn:gn:kb:ris-vialidad |
| RIS Genericos | urn:gn:kb:ris-genericos |
| RIS Educacion | urn:gn:kb:ris-educacion |
| RIS Seguridad y Justicia | urn:gn:kb:ris-seguridad-justicia |
| RIS Equipamiento Social | urn:gn:kb:ris-equipamiento-social |
| RIS Energia y Comunicaciones | urn:gn:kb:ris-energia-comunicaciones |
| RIS Salud | urn:gn:kb:ris-salud |
| RIS Cultura, Deporte y Turismo | urn:gn:kb:ris-cultura-deporte-turismo |

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
| Vision GORE | urn:gn:kb:gore-ideal |

### Inversion Estrategica y Territorio

| Topic | URN |
|-------|-----|
| ERD, ejes estrategicos, vision 2030 | urn:gn:kb:erd-nuble-2024-2030 |
| Nuble 250, proyectos emblematicos | urn:gn:kb:nuble-250 |
| Ley Presupuestos, Partida 31, umbrales | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Glosas GORE, Ley Presupuestos | urn:gn:kb:ley-presupuestos-2026-glosas-gore |

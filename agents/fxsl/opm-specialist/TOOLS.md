---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:opm-specialist-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string → path: string
- **Cuando usar:** Despues de kb_route o cuando el usuario ya entrega una URN valida y se necesita resolverla a path fisico.
- **Cuando NO usar:** Cuando aun no se ha clasificado el tema o cuando el contenido ya fue resuelto en el turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Siempre resolver antes de acceder KB.

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema OPM y seleccionar la URN primaria de la KB antes de invocar catalog_resolve.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| OPM, Object Process Methodology, ISO 19450, objetos, procesos, enlaces, OPD, OPL, SD, modelado conceptual, MBSE | urn:fxsl:kb:opm-methodology |

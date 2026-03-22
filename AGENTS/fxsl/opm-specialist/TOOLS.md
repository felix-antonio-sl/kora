---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:opm-specialist-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** `urn: string -> path: string`
- **Parametros:** `urn` conceptual de la KB OPM a resolver.
- **Cuando usar:** Despues de `kb_route` o cuando el usuario ya entrega una URN valida y se necesita resolverla a path fisico.
- **Cuando NO usar:** Cuando aun no se ha clasificado el tema o cuando el contenido ya fue resuelto en el turno actual.
- **Descripcion funcional:** Resuelve una URN valida del catalogo a la ruta local del artefacto OPM correspondiente.
- **Notas:** `catalog_master_*.yml` es la fuente de verdad. Resolver antes de acceder a la KB.

## kb_route

- **Firma:** `query_topic: string -> urn: string`
- **Parametros:** `query_topic` con el tema OPM a clasificar.
- **Cuando usar:** Clasificar tema OPM y seleccionar la URN primaria de la KB antes de invocar `catalog_resolve`.
- **Cuando NO usar:** Cuando el tema ya fue mapeado en el turno actual.
- **Descripcion funcional:** Asigna el tema OPM a la fuente KB primaria del corpus autorizado.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| OPM ISO 19450, entidades, enlaces, OPL, OPD, estados, procesos, objetos, transformacion, habilitacion, refinamiento, SD, metodologia | urn:fxsl:kb:opm-iso-19450 |
| OPCloud, herramienta, tutorial, wizard, simulacion, interfaz, navegacion, diagramas | urn:fxsl:kb:opcloud-tutorial-videos |

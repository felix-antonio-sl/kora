---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:abogado-legislacion-medica-tools:1.0.0"
  type: "bootstrap_tools"
---

## search_kb

- **Firma:** query: string -> KBEntry[]
- **Cuando usar:** Resolver cualquier consulta juridica que requiera contenido de las KBs de legislacion medica. Invocar tras clasificar consulta para obtener contenido normativo especifico.
- **Cuando NO usar:** Para busquedas web o contenido fuera del dominio legislacion laboral medica.
- **Notas:** Resolucion via catalogo como SOURCE_OF_TRUTH. Routing segun categoria: estatutos -> intro-estatutos, derechos -> deberes-prohibiciones, remuneraciones -> remuneraciones, acoso -> acoso-laboral, etc.

## resolve_urn

- **Firma:** urn: string -> file_path: string
- **Cuando usar:** Resolver cualquier URN a su path fisico antes de acceder al contenido. Primer paso obligatorio antes de consultar KB.
- **Cuando NO usar:** Si el path ya fue resuelto en el turno actual. No usar para URNs fuera del catalogo.
- **Notas:** Catalogo catalog_master_kora.yml es SOURCE_OF_TRUTH. Fallback a routing estatico solo si catalogo no disponible.

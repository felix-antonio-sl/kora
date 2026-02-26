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

## kb_route

- **Firma:** query_topic: string → urn: string
- **Cuando usar:** Clasificar tema de consulta juridica → resolver URN → priorizar KB antes de invocar search_kb.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Indice general, navegacion entre materias | `urn:legal:kb:index` |
| Estatutos funcionarios, jerarquia normativa, vinculo laboral | `urn:legal:kb:intro-estatutos` |
| Deberes, prohibiciones, incompatibilidades funcionarias | `urn:legal:kb:deberes-prohibiciones` |
| Ingreso, carrera funcionaria, calificaciones, ascensos | `urn:legal:kb:ingreso-carrera` |
| Jornada laboral, turnos, calificaciones desempeno | `urn:legal:kb:jornada-calificaciones` |
| Remuneraciones, asignaciones, bonificaciones medicas | `urn:legal:kb:remuneraciones` |
| Acoso laboral, acoso sexual, violencia en el trabajo | `urn:legal:kb:acoso-laboral` |
| Responsabilidad administrativa, sumarios, sanciones | `urn:legal:kb:responsabilidad-admin` |
| Terminacion de funciones, despido, cesacion, renuncia | `urn:legal:kb:terminacion` |
| Proteccion maternidad, fuero maternal, postnatal | `urn:legal:kb:maternidad` |
| Contratacion publica, licitaciones, convenios | `urn:legal:kb:contratacion-publica` |
| Feriados, permisos administrativos, licencias medicas | `urn:legal:kb:feriados-permisos` |
| Derechos especiales, garantias constitucionales laborales | `urn:legal:kb:derechos-especiales` |
| Becas, PAO, formacion de especialistas medicos | `urn:legal:kb:formacion-especialistas` |
| Ley Karin (21.643), prevencion acoso, protocolo denuncia | `urn:legal:kb:ley-21643` |
| Ley 15.076, estatuto medicos funcionarios | `urn:legal:kb:ley-15076` |
| Ley 19.664, medicos EDF, sistema alta direccion salud | `urn:legal:kb:ley-19664` |
| Confianza legitima, principio proteccion, expectativas | `urn:legal:kb:confianza-legitima` |

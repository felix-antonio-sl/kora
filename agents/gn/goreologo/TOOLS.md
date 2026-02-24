---
_manifest:
  urn: "urn:gn:agent-bootstrap:goreologo-tools:2.4.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path. catalog_master_kora.yml = SOURCE_OF_TRUTH.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar intent del usuario -> area taxonomica via routing map -> seleccionar artefacto -> resolver URN. Siempre consultar Matriz de Integracion Organica como indice primario: Taxonomia_Conocimiento -> Indice_Artefactos -> {area} -> Artefactos.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Intent / Nivel | Area | URN |
|----------------|------|-----|
| Introduccion, GOREs, Nuble, autoridades, historia, contexto | intro (N1) | urn:gn:kb:intro-gores-nuble |
| Organigrama, jerarquia, divisiones, departamentos | intro (N1) | urn:gn:kb:organigrama |
| LOC, ley, normativa, juridico, competencias, marco legal, reforma | legal (N1) | urn:gn:kb:loc-gore |
| Marco legal GOREs | legal (N1) | urn:gn:kb:marco-legal-gores |
| Modelos actos juridicos, resoluciones, decretos, convenios | juridico (N3) | urn:gn:kb:modelos-actos-juridicos |
| Estado Chile, poderes, estructura nacional, descentralizacion | estadocl (N1) | urn:mgmt:kb:estructura-estado-chile |
| ERD, vision, desarrollo, planificacion, Nuble250, estrategia, GORE ideal | estrategia (N2) | urn:gn:kb:erd-nuble-2024-2030 |
| GORE ideal | estrategia (N2) | urn:gn:kb:gore-ideal |
| Nuble 250 | estrategia (N2) | urn:gn:kb:nuble-250 |
| Aceleracion regional | estrategia (N2) | urn:gn:kb:aceleracion-regional |
| Vision desarrollo Nuble | estrategia (N2) | urn:gn:kb:vision-desarrollo-nuble |
| Problemas sociales, diagnostico social, brechas, vulnerabilidad | social (N2) | urn:gn:kb:problemas-sociales-cl |
| Indicadores, estadisticas, datos, demografia | estadisticas (N2) | urn:gn:kb:indicadores-nuble |
| Manual, induccion, glosario, cuentas publicas | gestion (N3) | urn:gn:kb:manual-induccion-gore-nuble-2026 |
| Glosario GORE | gestion (N3) | urn:gn:kb:glosario-gore-nuble |
| Rendiciones, SISREC | gestion (N3) | urn:gn:kb:gestion-rendiciones |
| Cuentas publicas | gestion (N3) | urn:gn:kb:cuentas-publicas-2021-2024 |
| Flujos aprobacion, visado | gestion (N3) | urn:gn:kb:flujos-aprobacion-documentos |
| Presupuesto, FNDR, SIGFE, finanzas, partida 31, subtitulo | presupuesto (N3) | urn:gn:kb:gestion-prpto |
| Ley presupuestos partida 31 | presupuesto (N3) | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Ley presupuestos normas generales | presupuesto (N3) | urn:gn:kb:ley-presupuestos-2026-normas-generales |
| IPR, inversion, proyectos, circular 33, RIS, IDI, BIP, FRIL, FRPD, PPR | ipr (N3) | urn:gn:kb:gestion-ipr |
| Selector IPR | ipr (N3) | urn:gn:kb:selector-ipr |
| Transferencia PPR | ipr (N3) | urn:gn:kb:transferencia-ppr |
| RIS index | ipr (N3) | urn:gn:kb:ris-index |
| RIS proyectos inversion | ipr (N3) | urn:gn:kb:ris-proyinv |
| RIS programas inversion | ipr (N3) | urn:gn:kb:ris-proginv |
| RIS empresas publicas | ipr (N3) | urn:gn:kb:ris-empub |
| RIS PMDT | ipr (N3) | urn:gn:kb:ris-pmdt |
| RIS educacion publica | ipr (N3) | urn:gn:kb:ris-edpub |
| RIS arte cultura | ipr (N3) | urn:gn:kb:ris-artcult |
| RIS patrimonio | ipr (N3) | urn:gn:kb:ris-patrimonio |
| RIS deportes | ipr (N3) | urn:gn:kb:ris-deportes |
| Guia IDI SNI STS | guias (N3) | urn:gn:kb:guia-idi-sni-sts |
| Guia programas directos GORE | guias (N3) | urn:gn:kb:guia-programas-directos-gore |
| Guia FRIL 2025 | guias (N3) | urn:gn:kb:guia-fril-2025-sts |
| Guia FRPD Nuble | guias (N3) | urn:gn:kb:guia-frpd-nuble |
| Instructivo subvencion 8% | guias (N3) | urn:gn:kb:instructivo-subvencion-8-2025-sts |
| Guia circular 33 | guias (N3) | urn:gn:kb:guia-circular-33-sts |
| Procesos, sistemas, geoespacial, CIES, SITIA | arquitectura (N4) | urn:gn:kb:cies-sitia |
| Gestion info geoespacial | arquitectura (N4) | urn:gn:kb:gestion-info-geoespacial |
| Comunicaciones, prensa, difusion, redes sociales | comunicaciones (N4) | urn:gn:kb:guia-comunicaciones |
| Comunicaciones OC | comunicaciones (N4) | urn:gn:kb:comunicaciones-oc |
| TDE, Ley 21.180, ClaveUnica, digital, transformacion, ciberseguridad | tde (N4) | urn:gn:kb:estrategia-td-ia |
| Informe estado inicial GORE pre-TD | tde (N4) | urn:gn:kb:informe-estado-inicial-gore-pre-td |
| Estrategia gestion | gestion (N3) | urn:gn:kb:estrategia-gestion |
| Inventarios, bodegas | gestion (N3) | urn:gn:kb:manual-inventarios-bodegas |
| Activo fijo | gestion (N3) | urn:gn:kb:manual-activo-fijo |
| Desarrollo organizacional | gestion (N3) | urn:gn:kb:manual-desarrollo-organizacional |
| Matriz integracion organica (INDICE PRIMARIO) | index | urn:gn:kb:matriz-integracion-organica |

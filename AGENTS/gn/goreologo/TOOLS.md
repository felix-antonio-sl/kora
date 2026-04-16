---
_manifest:
  urn: "urn:gn:agent-bootstrap:goreologo-tools:3.2.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path. catalog_master_kora.yml = SOURCE_OF_TRUTH.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar intent del usuario -> area taxonomica via routing map -> seleccionar artefacto -> resolver URN en catalogo. El routing map de este bootstrap es la referencia primaria y `catalog_master_kora.yml` sigue siendo el SSOT de resolucion.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Intent / Nivel | Area | URN |
|----------------|------|-----|
| Introduccion, GOREs, Nuble, autoridades, historia, contexto | intro (N1) | urn:gn:kb:intro-gores-nuble |
| Organigrama, jerarquia, divisiones, departamentos | intro (N1) | urn:gn:kb:organigrama |
| LOC, ley, normativa, juridico, competencias, marco legal, reforma | legal (N1) | urn:gn:kb:loc-gore |
| Marco legal GOREs | legal (N1) | urn:gn:kb:marco-legal-gores |
| Modelos actos juridicos, resoluciones, decretos, convenios | juridico (N3) | urn:gn:kb:modelos-actos-juridicos |
| Estado Chile, poderes, estructura nacional, descentralizacion | estadocl (N1) | urn:gn:kb:estructura-estado-chile |
| ERD, vision, desarrollo, planificacion, Nuble250, estrategia, GORE ideal | estrategia (N2) | urn:gn:kb:erd-nuble-2024-2030 |
| GORE ideal | estrategia (N2) | urn:gn:kb:gore-ideal |
| Nuble 250 | estrategia (N2) | urn:gn:kb:nuble-250 |
| Vision desarrollo Nuble | estrategia (N2) | urn:gn:kb:vision-desarrollo-nuble |
| Manual, induccion, glosario, cuentas publicas | gestion (N3) | urn:gn:kb:manual-induccion-gore-nuble-2026 |
| Rendiciones, SISREC | gestion (N3) | urn:gn:kb:gestion-rendiciones |
| Cuentas publicas | gestion (N3) | urn:gn:kb:cuentas-publicas-2021-2024 |
| Flujos aprobacion, visado | gestion (N3) | urn:gn:kb:flujos-aprobacion-documentos |
| Presupuesto, FNDR, SIGFE, finanzas, partida 31, subtitulo | presupuesto (N3) | urn:gn:kb:gestion-prpto |
| Ley presupuestos partida 31 | presupuesto (N3) | urn:gn:kb:ley-presupuestos-2026-partida-31 |
| Ley presupuestos normas generales | presupuesto (N3) | urn:gn:kb:ley-presupuestos-2026-normas-generales |
| IPR, inversion, proyectos, circular 33, RIS, IDI, BIP, FRIL, FRPD, PPR | ipr (N3) | urn:gn:kb:gestion-ipr |
| Selector IPR | ipr (N3) | urn:gn:kb:selector-ipr |
| Transferencia PPR | ipr (N3) | urn:gn:kb:transferencia-ppr |
| Guia IDI SNI STS | guias (N3) | urn:gn:kb:guia-idi-sni-sts |
| Guia programas directos GORE | guias (N3) | urn:gn:kb:guia-programas-directos-gore |
| Guia FRIL 2025 | guias (N3) | urn:gn:kb:guia-fril-2025-sts |
| Guia FRPD Nuble | guias (N3) | urn:gn:kb:guia-frpd-nuble |
| Instructivo subvencion 8% | guias (N3) | urn:gn:kb:instructivo-subvencion-8-2025-sts |
| Guia circular 33 | guias (N3) | urn:gn:kb:guia-circular-33-sts |
| Comunicaciones, prensa, difusion, redes sociales | comunicaciones (N4) | urn:gn:kb:guia-comunicaciones |
| Comunicaciones OC | comunicaciones (N4) | urn:gn:kb:comunicaciones-oc |
| Estrategia gestion | gestion (N3) | urn:gn:kb:estrategia-gestion |
| Modernizacion Estado, Waissbluth | gestion (N3) | urn:gn:kb:modernizacion-estado-waissbluth |
| Glosas GORE, Ley Presupuestos | presupuesto (N3) | urn:gn:kb:ley-presupuestos-2026-glosas-gore |
| RIS Transporte | ipr (N3) | urn:gn:kb:ris-transporte |
| RIS Vivienda y Urbanismo | ipr (N3) | urn:gn:kb:ris-vivienda-urbanismo |
| RIS Agua y Saneamiento | ipr (N3) | urn:gn:kb:ris-agua-saneamiento |
| RIS Vialidad | ipr (N3) | urn:gn:kb:ris-vialidad |
| RIS Genericos | ipr (N3) | urn:gn:kb:ris-genericos |
| RIS Educacion | ipr (N3) | urn:gn:kb:ris-educacion |
| RIS Seguridad y Justicia | ipr (N3) | urn:gn:kb:ris-seguridad-justicia |
| RIS Equipamiento Social | ipr (N3) | urn:gn:kb:ris-equipamiento-social |
| RIS Energia y Comunicaciones | ipr (N3) | urn:gn:kb:ris-energia-comunicaciones |
| RIS Salud | ipr (N3) | urn:gn:kb:ris-salud |
| RIS Cultura, Deporte y Turismo | ipr (N3) | urn:gn:kb:ris-cultura-deporte-turismo |
| Compras, contrataciones, licitaciones | operacional (N3) | urn:gn:kb:manual-compras-contrataciones |
| Contabilidad, SIGFE, cierre financiero | operacional (N3) | urn:gn:kb:manual-contabilidad |
| Tesoreria, pagos, ingresos | operacional (N3) | urn:gn:kb:manual-tesoreria |
| RRHH, gestion personas, remuneraciones | operacional (N3) | urn:gn:kb:manual-gestion-personas |
| Inventarios, activo fijo, bodegas | operacional (N3) | urn:gn:kb:manual-inventarios-activo-fijo |
| Flota vehicular, servicios generales | operacional (N3) | urn:gn:kb:manual-flota-servicios-generales |
| BPMN actos administrativos | procesos (N3) | urn:gn:kb:bpmn-actos-administrativos |
| CIES SITIA seguridad publica | procesos (N3) | urn:gn:kb:bpmn-cies-sitia |
| Geoespacial IDE Geonodo SIG | procesos (N3) | urn:gn:kb:bpmn-geoespacial-ide |
| Indicadores regionales comunales | estrategia (N2) | urn:gn:kb:indicadores-nuble |
| Convenios, estados, cuotas, FSM | ipr (N3) | urn:gn:kb:convenios-estados-fases |
| Actores externos, SEREMIAs, servicios, plazos | intro (N1) | urn:gn:kb:ecosistema-instituciones |
| Matriz comparativa mecanismos, arbol decision | ipr (N3) | urn:gn:kb:mecanismos-matriz-decision |
| Dictamenes CGR, contraloria, jurisprudencia administrativa | juridico (N3) | urn:gn:kb:dictamenes-cgr-gore |
| Ley presupuestos GORE Nuble, marco operativo regional | presupuesto (N3) | urn:gn:kb:ley-presupuestos-2026-gore-nuble |
| Manual operacional DGI, gestion institucional | gestion (N3) | urn:gn:kb:manual-operacional-dgi |
| Plan potenciamiento DGI, mejoramiento | gestion (N3) | urn:gn:kb:plan-potenciamiento-dgi |
| Lean Six Sigma, mejora continua, DMAIC | gestion (N3) | urn:gn:kb:lean6-gestion-core |
| Estructura organizacional, principios, Meyer | gestion (N3) | urn:gn:kb:meyer-estructura-organizacional |
| SSOT indice maestro, fuente de verdad consolidada | ssot (N2) | urn:gn:kb:ssot-master |
| SSOT actos administrativos | ssot (N3) | urn:gn:kb:ssot-actos-admin |
| SSOT convenios GORE | ssot (N3) | urn:gn:kb:ssot-convenios |
| SSOT DGI gestion institucional | ssot (N3) | urn:gn:kb:ssot-dgi |
| SSOT ecosistema institucional | ssot (N2) | urn:gn:kb:ssot-ecosistema |
| SSOT ciclo vida IPR inversion | ssot (N3) | urn:gn:kb:ssot-ipr-lifecycle |
| SSOT marco normativo legal | ssot (N3) | urn:gn:kb:ssot-legal |
| SSOT mecanismos financiamiento | ssot (N3) | urn:gn:kb:ssot-mecanismos |
| SSOT procesos operativos | ssot (N3) | urn:gn:kb:ssot-operaciones |
| SSOT estructura organica | ssot (N2) | urn:gn:kb:ssot-organica |
| SSOT presupuesto | ssot (N3) | urn:gn:kb:ssot-presupuesto |
| SSOT relaciones inter-dominio | ssot (N2) | urn:gn:kb:ssot-relaciones-dominio |
| SSOT rendiciones SISREC | ssot (N3) | urn:gn:kb:ssot-rendiciones |
| SSOT transformacion digital TDE | ssot (N3) | urn:gn:kb:ssot-tde |
| SSOT territorio Nuble | ssot (N2) | urn:gn:kb:ssot-territorio |

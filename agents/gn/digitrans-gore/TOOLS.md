---
_manifest:
  urn: "urn:gn:agent-bootstrap:digitrans-gore-tools:1.0.0"
  type: "bootstrap_tools"
---

## catalog_resolve

- **Firma:** urn: string -> path: string
- **Cuando usar:** Toda consulta KB requiere resolucion URN via catalogo. Cadena: URN -> buscar catalog -> extraer file -> retornar path.
- **Cuando NO usar:** Datos ya en contexto o tema ya mapeado en turno actual.
- **Notas:** catalog_master_*.yml = SOURCE_OF_TRUTH. Resolucion federada: buscar en tde, orko, gn, gov.

## kb_route

- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Clasificar tema -> resolver URN -> priorizar KB -> LLM solo pegamento.
- **Cuando NO usar:** Tema ya mapeado en turno actual.
- **Routing Map:**

| Topic | URN |
|-------|-----|
| Ley 21.180, obligaciones TDE, plazos | urn:tde:kb:ley-21180 |
| Norma documentos, expedientes, D10 | urn:tde:kb:nt-documentos-expedientes |
| Interoperabilidad, D12, PISEE | urn:tde:kb:nt-interoperabilidad |
| ClaveUnica, autenticacion | urn:tde:kb:claveunica |
| SIMPLE, SGD, tramites | urn:tde:kb:simple-saas |
| CPAT, madurez digital | urn:tde:kb:cpat-completa |
| ORKO, metodologia, playbooks | urn:orko:kb:orko-metodologia |
| Governance, artefactos KORA | urn:kora:kb:gobernanza |
| GORE, estructura, contexto | urn:gn:kb:intro-gores-nuble |
| Ley 19.880, procedimientos | urn:tde:kb:ley-19880 |
| Datos personales, Ley 21.719 | urn:legal:kb:ley-21719-datos-personales |
| Autenticacion, norma tecnica | urn:tde:kb:nt-autenticacion |
| Seguridad, ciberseguridad NT | urn:tde:kb:nt-seguridad-ciberseguridad |
| DocDigital, documentos | urn:tde:kb:docdigital |
| PISEE, interoperabilidad plataforma | urn:tde:kb:pisee |
| Reglamento TDE, DS4 | urn:tde:kb:reglamento-ds4 |
| CPAT Nuble, catalogo local | urn:tde:kb:catalogo-cpat-nuble |
| SIMPLE SaaS OAE | urn:tde:kb:simple-saas-oae |
| ORKO fundamentos | urn:orko:kb:orko-fundamentos |
| ORKO arquitectura | urn:orko:kb:orko-arquitectura |
| ORKO playbooks | urn:orko:kb:orko-playbooks |
| Estrategia TD IA GORE | urn:gn:kb:estrategia-td-ia |
| Estado inicial GORE pre-TD | urn:gn:kb:informe-estado-inicial-gore-pre-td |
| Principios y objetivos TDE | urn:tde:kb:principios-objetivos |
| Introduccion TDE gobierno | urn:gov:kb:intro-tde |

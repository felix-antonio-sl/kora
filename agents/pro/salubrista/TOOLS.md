---
_manifest:
  urn: "urn:pro:agent-bootstrap:salubrista-tools:1.0.0"
  type: "bootstrap_tools"
---

## kb_route

- **Firma:** topic: string -> urn: string
- **Cuando usar:** Primer paso semantico para resolver el corpus rector antes del analisis. Usar en problemas de epidemiologia aplicada, vigilancia, gestion, diseno, implementacion y evaluacion de sistemas sanitarios.
- **Cuando NO usar:** Si el mismo tema ya fue resuelto y recuperado en el turno actual.
- **Routing map gestion-redes:**

| Topic | URN |
|-------|-----|
| Gobernanza de red, modelo de atencion integrado, procesos transversales, calidad, digital, finanzas, RRHH, gestion del cambio, investigacion | `urn:pro:kb:gestion-redes-general` |
| Unidades ambulatorias, hospitalarias, articulacion de dispositivos y niveles de atencion | `urn:pro:kb:gestion-redes-unidades` |
| Red de urgencias, SAMU, triage, protocolos tiempo-dependientes, MCI, desastres | `urn:pro:kb:gestion-redes-urgencias` |
| Red de salud mental, continuidad, crisis, rehabilitacion psicosocial, derechos, legislacion | `urn:pro:kb:gestion-redes-salud-mental` |
| KPIs, BPMN, plantillas operativas, FHIR/HL7, simulacion, modelo de madurez digital | `urn:pro:kb:gestion-redes-herramientas` |
| Indice general, glosario, normativa CL + internacional, contextualizacion local | `urn:pro:kb:gestion-redes-indice` |

- **Routing map salud publica aplicada:**

| Topic | URN |
|-------|-----|
| Epidemiologia aplicada, analisis poblacional, riesgos, puentes metodologicos, pensamiento sistemico y razonamiento sanitario integrado | `urn:pro:kb:firs-framework-integrado-razonamiento-salud` |

## knowledge_retrieval

- **Firma:** urn: string -> content: string
- **Cuando usar:** Recuperar el contenido del corpus inmediatamente despues de `kb_route`. Util para secciones especificas de gestion-redes o del framework integrado antes de complementar con modelo o web.
- **Cuando NO usar:** Si el contenido ya esta en contexto de turno actual.

## web_search

- **Firma:** query: string -> SearchResult[]
- **Cuando usar:** Complementar corpus con evidencia actualizada, normativa local vigente, datos epidemiologicos actuales, benchmarks operativos o documentos tecnicos recientes no cubiertos por el corpus. Citar fuente web en output.
- **Cuando NO usar:** Si el corpus ya cubre adecuadamente el tema. No usar web para reemplazar el corpus, solo para extenderlo o verificar vigencia.
- **Notas:** Preferir OPS, OMS, MINSAL, IHI, NICE, AHRQ, Cochrane, ministerios de salud, organismos tecnicos y journals indexados.

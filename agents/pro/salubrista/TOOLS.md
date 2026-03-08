---
_manifest:
  urn: "urn:pro:agent-bootstrap:salubrista-tools:1.0.0"
  type: "bootstrap_tools"
---

## kb_route

- **Firma:** topic: string → urn: string
- **Cuando usar:** Toda consulta sobre gestión de redes asistenciales, unidades, urgencias, salud mental, herramientas/KPIs. Primer paso ante cualquier problema de Dim III o con componente de red. Consultar ANTES de web o conocimiento del modelo.
- **Cuando NO usar:** Si tema ya mapeado en turno actual. Si la pregunta es puramente de razonamiento clínico sin componente de red.
- **Routing map:**

| Topic | URN |
|-------|-----|
| Gobernanza de red, modelo atención integrado, procesos transversales, calidad, digital, finanzas, RRHH, gestión del cambio, investigación | `urn:pro:kb:gestion-redes-general` |
| Unidades ambulatorias (APS/CESFAM), hospitalarias (agudos/UCI), hospitalización domiciliaria (HaH) | `urn:pro:kb:gestion-redes-unidades` |
| Red de urgencias, SUH, EMS/SAMU, triage (ESI), protocolos tiempo-dependientes (ACV/SCA/Sepsis/Trauma), MCI, desastres | `urn:pro:kb:gestion-redes-urgencias` |
| Red de salud mental, continuidad, intervención en crisis, TUS, SM infanto-juvenil, adulto mayor, rehabilitación psicosocial, derechos, legislación | `urn:pro:kb:gestion-redes-salud-mental` |
| KPIs, BPMN, plantillas operativas, FHIR/HL7, simulación, modelo de madurez digital | `urn:pro:kb:gestion-redes-herramientas` |
| Índice general, glosario, normativa CL + internacional, contextualización local | `urn:pro:kb:gestion-redes-indice` |

## kb_route

- **Firma:** topic: string → urn:pro:kb:firs-framework-integrado-razonamiento-salud
- **Cuando usar:** Toda consulta sobre razonamiento clínico (Dim I), epidemiología/inferencia causal/modelado (Dim II), gestión sanitaria macro (Dim III), ejes transversales, puentes metodológicos, tensiones estructurales del framework.
- **Cuando NO usar:** Si FIRS ya consultado en turno actual para el mismo tema.

## knowledge_retrieval

- **Firma:** urn: string → content: string
- **Cuando usar:** Recuperar sección específica del corpus después de kb_route. Útil para capítulos específicos (ej: `urn:pro:kb:gestion-redes-urgencias §22` para protocolo SCA) o secciones del FIRS (ej: §3.4 sesgos, §4.1 inferencia causal).
- **Cuando NO usar:** Si contenido ya en contexto de turno actual.

## web_search

- **Firma:** query: string → SearchResult[]
- **Cuando usar:** Complementar blueprint con evidencia actualizada, guías recientes, datos epidemiológicos actuales, normativa local vigente no cubierta por el corpus, estudios de prevalencia actuales. SIEMPRE subordinado al blueprint: verificar coherencia con gestión-redes antes de integrar al análisis. Citar fuente web en output.
- **Cuando NO usar:** Si el blueprint ya cubre adecuadamente el tema. No usar web para reemplazar el corpus — solo para extenderlo.
- **Notas:** Habilitado por defecto. Preferir fuentes: OPS, OMS, IHI, NICE, AHRQ, Cochrane, MINSAL, ministerios de salud, journals indexados (Lancet, NEJM, BMJ, JAMA, Rev Panam Salud Pública).

---
_manifest:
  urn: "urn:pro:agent-bootstrap:salubrista-hah-tools:1.0.0"
  type: "bootstrap_tools"
---

## kb_route (hospitalización domiciliaria)

- **Firma:** topic: string → urn: string
- **Cuando usar:** Todo problema HD específico — criterios ingreso/egreso, cargo DT, operaciones domiciliarias, IAAS domiciliaria, REAS, protocolos dispositivos invasivos, normativa chilena HD, evidencia internacional HaH. Consultar ANTES que web o modelo.
- **Cuando NO usar:** Si tema ya mapeado en turno actual. Si el problema es de gestión de red general sin componente HD específico.
- **Routing map HaH:**

| Topic | URN |
|-------|-----|
| Índice general, glosario HD, normativa chilena HD, control versiones | `urn:pro:kb:hodom-indice` |
| Situación HD en Chile 2024-2026: epidemiología, normativa, producción DEIS, financiamiento MCC/GRD, brechas | `urn:pro:kb:hodom-situacion-chile` |
| Modelo HaH internacional: Johns Hopkins, Cochrane, CMS AHCAH, operaciones, tecnología RPM/IoT, economía backfill, barreras, futuro | `urn:pro:kb:hodom-manual-hah` |
| Cargo DT: requisitos legales, responsabilidad art. 7, RRHH, inducción, PAC, infraestructura, farmacia, IAAS, REAS, flujo clínico, registros obligatorios, manuales, seguridad personal terreno | `urn:pro:kb:hodom-director-tecnico` |

## kb_route (gestión de redes)

- **Firma:** topic: string → urn: string
- **Cuando usar:** Problemas de gestión de redes asistenciales generales, o HD en contexto de red. Consultar ANTES que web o modelo.
- **Cuando NO usar:** Si tema ya mapeado en turno actual o si el corpus HaH cubre el tema.
- **Routing map gestión-redes:**

| Topic | URN |
|-------|-----|
| Gobernanza de red, modelo atención integrado, procesos, calidad, digital, finanzas, RRHH, cambio | `urn:pro:kb:gestion-redes-general` |
| Unidades ambulatorias (APS/CESFAM), hospitalarias, HaH (Cap. 17) | `urn:pro:kb:gestion-redes-unidades` |
| Red urgencias, SUH, EMS/SAMU, triage, protocolos tiempo-dependientes, MCI, desastres | `urn:pro:kb:gestion-redes-urgencias` |
| Red salud mental, continuidad, crisis, TUS, derechos | `urn:pro:kb:gestion-redes-salud-mental` |
| KPIs, BPMN, plantillas, FHIR/HL7, simulación, modelo de madurez | `urn:pro:kb:gestion-redes-herramientas` |
| Índice general, glosario, normativa | `urn:pro:kb:gestion-redes-indice` |

## kb_route (FIRS)

- **Firma:** topic: string → urn:pro:kb:firs-framework-integrado-razonamiento-salud
- **Cuando usar:** Razonamiento clínico (Dim I), epidemiológico/causal (Dim II), gestión macro (Dim III), ejes transversales, puentes metodológicos, tensiones estructurales del framework.
- **Cuando NO usar:** Si FIRS ya consultado en turno actual para el mismo tema.

## knowledge_retrieval

- **Firma:** urn: string → content: string
- **Cuando usar:** Recuperar sección específica del corpus después de kb_route. En HaH: ej. `urn:pro:kb:hodom-director-tecnico §7` para art. 7 DS 1/2022. En gestión-redes: sección específica de capítulo.
- **Cuando NO usar:** Si contenido ya en contexto de turno actual.

## web_search

- **Firma:** query: string → SearchResult[]
- **Cuando usar:** Complementar corpus con evidencia actualizada, normativa MINSAL más reciente, datos epidemiológicos actuales, estudios HaH publicados, benchmarks internacionales. SIEMPRE subordinado al corpus: verificar coherencia antes de integrar. Citar fuente web en output.
- **Cuando NO usar:** Si el corpus ya cubre adecuadamente el tema.
- **Notas:** Habilitado por defecto. Para HaH: preferir Johns Hopkins, Cochrane, CMS, MINSAL.gov.cl, journals (Lancet, NEJM, BMJ, JAMA, Ann Intern Med). Para gestión: OPS, OMS, IHI, NICE, AHRQ.

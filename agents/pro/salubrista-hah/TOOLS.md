---
_manifest:
  urn: "urn:pro:agent-bootstrap:salubrista-hah-tools:1.0.0"
  type: "bootstrap_tools"
---

## kb_route

- **Firma:** topic: string -> urn: string
- **Cuando usar:** Primer paso semantico para resolver el corpus rector antes del analisis. Usar en problemas de hospitalizacion integrada, gestion de camas, continuidad del cuidado, hospitalizacion domiciliaria, implementacion y evaluacion.
- **Cuando NO usar:** Si el mismo tema ya fue resuelto y recuperado en el turno actual.
- **Routing map hospitalizacion integrada:**

| Topic | URN |
|-------|-----|
| Gobernanza hospitalaria, procesos transversales, calidad, RRHH, gestion del cambio, operacion de establecimientos | `urn:pro:kb:gestion-redes-general` |
| Unidades hospitalarias, hospitalizacion, articulacion de modalidades, HaH, continuidad funcional entre dispositivos | `urn:pro:kb:gestion-redes-unidades` |
| Red de urgencias, ingresos hospitalarios, SAMU, descompensaciones, rescate y transiciones tiempo-sensibles | `urn:pro:kb:gestion-redes-urgencias` |
| KPIs, BPMN, simulacion, plantillas operativas, madurez digital y soporte instrumental | `urn:pro:kb:gestion-redes-herramientas` |
| Indice general, glosario, normativa y contextualizacion local | `urn:pro:kb:gestion-redes-indice` |

- **Nota:** Este bloque es el baseline del componente intrahospitalario. Si el caso exige detalle hospitalario especifico no cubierto por estos URNs, declararlo y complementar con `web_search`.

- **Routing map HD / hospital-domicilio:**

| Topic | URN |
|-------|-----|
| Reglamento base HD: autorizacion, direccion tecnica, ingreso/egreso, articulado central | `urn:pro:kb:hodom-reglamento-ds1-2022` |
| Decreto aprobatorio y fundamento juridico de la norma tecnica HD 2024 | `urn:pro:kb:hodom-decreto-exento-31-2024` |
| Norma tecnica HD 2024: personal, infraestructura, equipamiento, registros, protocolos, PAC, seguridad | `urn:pro:kb:hodom-norma-tecnica-2024` |
| Direccion Tecnica HD: art. 7-10, RRHH, manuales, fiscalizacion, sucesion, operacion local del DT | `urn:pro:kb:hodom-direccion-tecnica` |
| Modelo HaH de alta complejidad: benchmarks, operaciones, RPM/IoT, pathways, backfill y continuidad | `urn:pro:kb:hodom-manual-alta-complejidad` |
| Situacion de Chile 2024-2026: DEIS, financiamiento, GRD/MCC, brechas de red | `urn:pro:kb:hodom-situacion-chile-2026` |

- **Routing map salud publica aplicada:**

| Topic | URN |
|-------|-----|
| Epidemiologia aplicada, riesgos, brotes, razonamiento sanitario integrado y pensamiento sistemico | `urn:pro:kb:firs-framework-integrado-razonamiento-salud` |

## knowledge_retrieval

- **Firma:** urn: string -> content: string
- **Cuando usar:** Recuperar el contenido del corpus inmediatamente despues de `kb_route`. En problemas de hospitalizacion integrada, recuperar primero gestion-redes y sumar corpus HD cuando la trayectoria hospital-domicilio o la normativa sean relevantes.
- **Cuando NO usar:** Si el contenido ya esta en contexto de turno actual.

## web_search

- **Firma:** query: string -> SearchResult[]
- **Cuando usar:** Complementar corpus con evidencia actualizada, normativa MINSAL vigente, datos epidemiologicos actuales, benchmarks de hospitalizacion integrada o estudios recientes de HD y continuidad del cuidado. Citar fuente web en output.
- **Cuando NO usar:** Si el corpus ya cubre adecuadamente el tema. No usar web para reemplazar el corpus; solo para extenderlo o verificar vigencia.
- **Notas:** Preferir MINSAL, OPS, OMS, IHI, NICE, AHRQ, Cochrane, Johns Hopkins, CMS y journals indexados. Usar especialmente cuando el problema requiera detalle intrahospitalario no disponible en `gestion-redes-*` o vigencia normativa/benchmark actual.

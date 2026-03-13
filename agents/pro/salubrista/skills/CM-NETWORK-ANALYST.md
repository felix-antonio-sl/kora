---
_manifest:
  urn: urn:pro:skill:salubrista-network-analyst:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-NETWORK-ANALYST

## Proposito
Analizar o disenar sistemas sanitarios complejos en distintas escalas: unidades, establecimientos, redes y territorios. Integra pensamiento sistemico, gestion sanitaria, arquitectura funcional y lectura operativa para diagnosticar funcionamiento o proponer rediseños coherentes con la demanda, la epidemiologia y la capacidad instalada.

## Input/Output
- **Input:** mode: "analysis"|"design", problema: string, contexto: object
- **Output:** SystemResult { escala: string, foco: string, analisis: string, recomendaciones: string[], kpis_propuestos: string[], riesgos: string[], implementacion_requerida: bool }

## Procedimiento
1. RESOLVER `kb_route` hacia el corpus gestion-redes mas pertinente al problema y recuperar el contenido con `knowledge_retrieval`.
2. POSICIONAR la escala: unidad / establecimiento / red / territorio / multi.
3. IF mode = `analysis`:
   - mapear demanda, oferta, capacidad, flujos, nodos y dependencias
   - identificar cuellos de botella, fragmentacion, brechas de coordinacion y fallas de continuidad
   - explicitar efectos no intencionales y comportamiento emergente
4. IF mode = `design`:
   - definir objetivo sanitario y funcional
   - proponer cartera de servicios, roles, nodos, complejidad, derivacion y gobernanza
   - alinear el diseno con epidemiologia, demanda real, restricciones y escalabilidad
5. APLICAR pensamiento sistemico:
   - interdependencias entre niveles
   - tradeoffs entre eficiencia, equidad, oportunidad y resiliencia
   - puntos de apalancamiento del sistema
6. PROPONER recomendaciones y KPIs:
   - cobertura, acceso, continuidad, tiempos, uso de capacidad, experiencia usuaria, seguridad, equidad
7. IDENTIFICAR si el resultado requiere plan de implementacion detallado:
   - IF el cambio exige fases, responsables o pilotaje -> `implementacion_requerida = true`
8. OUTPUT: escala, foco, analisis, recomendaciones, KPIs, riesgos e indicador de implementacion requerida.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| escala | string | unidad / establecimiento / red / territorio / multi |
| foco | string | analisis sistemico o diseno |
| analisis | string | Diagnostico o propuesta estructural |
| recomendaciones | string[] | Recomendaciones accionables |
| kpis_propuestos | string[] | Indicadores sugeridos |
| riesgos | string[] | Riesgos y efectos no intencionales |
| implementacion_requerida | bool | True si hace falta plan operativo detallado |

---
_manifest:
  urn: urn:pro:skill:salubrista-product-builder:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-PRODUCT-BUILDER

## Proposito
Construir productos estructurados de copiloto para decision sanitaria: mapas de brechas y riesgos, tableros de monitoreo, informes de politica sanitaria y escenarios de decision. Convierte analisis disperso en artefactos directamente utilizables por autoridades o equipos directivos.

## Input/Output
- **Input:** contenido_analisis: object, tipo_producto: "gap_map"|"risk_map"|"monitoring_dashboard"|"policy_brief"|"decision_scenarios", audiencia: string
- **Output:** Product { tipo_producto, estructura, componentes: string[], criterios_uso: string[], trazabilidad: string[], disclaimer }

## Procedimiento
1. RECIBIR el contenido acumulado de sesion desde analisis epidemiologico, sistemico, diseno, implementacion, evaluacion o vigilancia.
2. IDENTIFICAR audiencia y decision objetivo.
3. IF `tipo_producto = gap_map`:
   - organizar brechas por escala, impacto, urgencia, dependencia y responsable
4. IF `tipo_producto = risk_map`:
   - organizar riesgos por probabilidad, impacto, poblacion afectada, mitigacion y senales de alerta
5. IF `tipo_producto = monitoring_dashboard`:
   - definir KPIs, formula, meta, periodicidad, fuente, alertas y criterio de accion
6. IF `tipo_producto = policy_brief`:
   - estructurar problema, contexto, opciones, tradeoffs, recomendacion, implicancias de implementacion y riesgos
7. IF `tipo_producto = decision_scenarios`:
   - construir alternativas comparables con supuestos, beneficios, riesgos, costo operacional y condiciones de exito
8. VERIFICAR:
   - la escala y la audiencia estan claras
   - el producto no confunde hallazgo con decision final
   - la trazabilidad y los supuestos son visibles
9. OUTPUT: producto estructurado, componentes, criterios de uso, trazabilidad y disclaimer.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| tipo_producto | string | gap_map / risk_map / monitoring_dashboard / policy_brief / decision_scenarios |
| estructura | string | Forma general del producto |
| componentes | string[] | Campos o secciones del producto |
| criterios_uso | string[] | Como leer o usar el producto para decidir |
| trazabilidad | string[] | Evidencia y normativa citada |
| disclaimer | string | Producto de apoyo tecnico; la decision final corresponde a la conduccion humana |

---
name: hospital-system-analyst
description: Analizar o diseñar sistemas de hospitalizacion integrados considerando capacidad, camas, estada, transiciones, reingresos, continuidad del cuidado y trayectoria hospital-domicilio. Usar cuando el problema dominante sea el sistema de hospitalizacion como continuo asistencial.
user-invocable: false
---

# Hospital System Analyst

## Procedimiento

1. Leer `kb/INDEX.md` y el corpus local pertinente.
2. Si el problema involucra continuidad hospital-domicilio o HD, complementar con `reference/legacy-salubrista/` y `memory/`.
3. Si el detalle requerido no esta cubierto por el corpus local, declararlo como limite y complementar con `web_search`.
4. Posicionar la escala: unidad, establecimiento, red, territorio, nacional o multi.
5. Identificar modalidad dominante: hospital, domicilio, transicion o integrada.
6. Si el modo es `analysis`, mapear demanda, capacidad, camas, estada, altas demoradas, rescates y reingresos.
7. Si el modo es `design`, definir objetivo funcional y proponer rutas, criterios, nodos, roles y gobernanza.
8. Verificar `modality_fit`: no usar HD como descarga indiscriminada.
9. Proponer KPIs y riesgos.
10. Marcar si hace falta profundizar en HD o en implementacion.

## Salida esperada

- `escala`
- `modalidad_dominante`
- `analisis`
- `recomendaciones`
- `kpis_propuestos`
- `riesgos`
- `componente_hah_requerido`
- `implementacion_requerida`

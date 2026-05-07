---
canario: firs-baseline
runtime: claude-code
subagent: firs-razonamiento-sanitario
subagent_source: ~/.claude/skills/firs-razonamiento-sanitario/SKILL.md
subagent_source_urn: urn:salud:artefacto:firs-razonamiento-sanitario
transmuted_at: 2026-05-07T00:00:00+00:00
baseline_captured_at: pending
baseline_status: pending
invocation_mode: interactivo
capture_mechanism: session log (claude-code + skill loaded)
kb_edit_propagation: pendiente
canario_marker: 2026-05-07-firs-baseline-v1
---

# Canario baseline — firs-razonamiento-sanitario (claude-code)

Fixture para la primera invocacion con eval de la skill FIRS.

## Prompt canonico

Carga la skill firs-razonamiento-sanitario. Aplica el framework FIRS al
siguiente problema:

"Un servicio de urgencias pediatrico reporta un aumento del 40% en consultas
por crisis asmaticas en invierno comparado con verano. La tasa de hospitalizacion
por asma en la comuna es de 18 por 10,000 habitantes, el doble del promedio
nacional. El 60% de los ninos hospitalizados viven en hogares con calefaccion
a lena. La cobertura del programa de asma infantil alcanza al 30% de la
poblacion objetivo."

Aplica las tres escalas del framework FIRS (micro: clinica individual, meso:
servicio de urgencias, macro: salud publica/comuna) para estructurar el
analisis. Identifica si hay falacia ecologica en alguna interpretacion y
propon intervenciones diferenciadas por escala.

## Knowledge Contract esperado

- urn:salud:kb:salubrista
- urn:salud:kb:salubrista-body-of-knowledge
- urn:salud:kb:salubrista-fuentes-base-curadas
- urn:salud:kb:salubrista-fuente-salud-publica-global
- urn:salud:kb:salubrista-fuente-management-engineering
- urn:salud:kb:gestion-redes-general
- urn:salud:kb:gestion-redes-urgencias
- urn:salud:kb:gestion-redes-herramientas
- urn:salud:kb:health-systems-science-fundamentos

## Gate multinivel

| # | Criterio | Pregunta operacional |
|---|----------|----------------------|
| 1 | Trazabilidad al corpus | Cita al menos 2 URNs con tool calls? |
| 2 | Separacion de escalas | Distingue claramente intervenciones micro (clinica del nino asmatico), meso (gestion de urgencias pediatricas) y macro (cobertura poblacional, determinantes ambientales)? |
| 3 | Deteccion de falacia ecologica | Advierte que no se puede inferir riesgo individual desde datos poblacionales (falacia ecologica)? |
| 4 | Intervenciones diferenciadas | Propone intervenciones distintas para cada escala, no una solucion unica? |
| 5 | Respeto del corpus | No inventa epidemiologia ni politicas publicas fuera del corpus? |

## Output de referencia esperado

### Escala micro (clinica individual)

- Cada nino con crisis asmatica: manejo agudo segun guia, plan de accion,
  educacion en inhaladores, control ambiental del hogar
- No hay falacia: el dato poblacional no predice el caso individual

### Escala meso (servicio de urgencias)

- 40% aumento invernal: predecible, planificar refuerzo de turnos y salas ERA
- Tasa de hospitalizacion 18/10,000 (2x nacional): posible sobre-hospitalizacion
  o falta de manejo ambulatorio efectivo
- 60% con calefaccion a lena: factor ambiental abordable con intervencion

### Escala macro (salud publica)

- 30% cobertura del programa: brecha de 70%. Intervencion: ampliar cobertura,
  eliminar barreras de acceso
- Calefaccion a lena como determinante ambiental: politica de subsidio de
  calefaccion limpia + regulacion de emisiones

## Lazo Kelly reproducible

1. Cargar skill firs-razonamiento-sanitario en sesion claude-code
2. Invocar con el prompt canonico
3. Verificar: tres escalas diferenciadas, falacia ecologica advertida,
   intervenciones distintas por escala
4. Registrar: kora record-invocation --agent-urn urn:salud:artefacto:firs-razonamiento-sanitario

## Deuda registrada

1. Invocacion manual. Automatizar requiere soporte programatico.
2. Escenario unico. Ampliar con caso de salud mental o cardiovascular.

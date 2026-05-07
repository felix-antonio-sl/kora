---
canario: salubrista-baseline
runtime: claude-code
subagent: salubrista
subagent_source: ~/.claude/agents/salubrista.md
subagent_source_urn: urn:salud:artefacto:salubrista
transmuted_at: 2026-05-07T00:00:00+00:00
baseline_captured_at: pending
baseline_status: pending
invocation_mode: interactivo
capture_mechanism: session log (claude-code tool calls)
kb_edit_propagation: pendiente
canario_marker: 2026-05-07-salubrista-baseline-v1
---

# Canario baseline — salubrista (claude-code)

Fixture del input y criterios de aceptacion para la primera invocacion
productiva con eval del agente salubrista.

## Prompt canonico

Activa el modo salubrista general. Un director de servicio de salud regional
te consulta: "Tenemos 3 hospitales en la red: H1 (alta complejidad, 400 camas,
ocupacion 92%), H2 (mediana complejidad, 250 camas, ocupacion 78%), H3 (baja
complejidad, 120 camas, ocupacion 65%). Las urgencias de H1 tienen boarding
time promedio de 8.5 horas. Las listas de espera para cirugia electiva son
de 14 meses en H1 y 9 meses en H2. Quiero saber: (a) diagnostico estructural,
(b) intervenciones de capacidad priorizadas, (c) si HODOM aplica como valvula."

Responde usando exclusivamente el corpus salubrista.

## Knowledge Contract esperado

- urn:salud:kb:salubrista
- urn:salud:kb:salubrista-atlas-integrado
- urn:salud:kb:salubrista-body-of-knowledge
- urn:salud:kb:gestion-redes-general
- urn:salud:kb:gestion-redes-unidades
- urn:salud:kb:gestion-redes-urgencias
- urn:salud:kb:gestion-redes-herramientas
- urn:salud:kb:hodom-direccion-tecnica
- urn:salud:kb:hodom-norma-tecnica-2024
- urn:salud:kb:management-engineering-ext-capacidad
- urn:salud:kb:health-systems-science-operativa
- urn:salud:kb:health-systems-science-fundamentos

No debe inventar cifras, protocolos ni normativa fuera del corpus.

## Gate multinivel

| # | Criterio | Pregunta operacional |
|---|----------|----------------------|
| 1 | Trazabilidad al corpus | Cita al menos 3 URNs con tool calls de lectura? |
| 2 | Diagnostico estructural | Identifica el desbalance H1 vs H2/H3 y el boarding time como cuello de botella sistemico? |
| 3 | Recomendaciones con fundamento | Propone intervenciones especificas (load leveling, pooling, fast track) citando el corpus? |
| 4 | Evaluacion HODOM | Aplica criterios de la norma tecnica chilena? Distingue candidatos viables? |
| 5 | Respeto del conocimiento_permitido | No inventa URNs, normativa extranjera ni protocolos fuera del corpus? |

## Output de referencia esperado

### Diagnostico estructural

- H1 opera en zona de riesgo (ocupacion mayor a 85%). Es el cuello de botella.
- Boarding time de 8.5h es 2x el benchmark (menor a 4h).
- H2 y H3 subutilizados (65-78%). Capacidad ociosa en la red.
- Lista de espera quirurgica de 14 meses: sintoma de quirofanos saturados.

### Recomendaciones esperadas

- Load leveling: redistribuir cirugia electiva a H2
- Pooling: unificar lista de espera regional
- Fast track en urgencias H1 para casos ESI 4-5
- HODOM como valvula: pacientes cronicos estables candidatos segun norma tecnica
- Reducir variabilidad: protocolizar altas, estandarizar ingresos

## Lazo Kelly reproducible

1. Verificar despliegue: ls ~/.claude/agents/salubrista.md
2. Invocar en sesion fresca de claude-code con el prompt canonico
3. Verificar output: diagnostico estructural, al menos 3 URNs, recomendacion HODOM
4. Registrar: kora record-invocation --agent-urn urn:salud:artefacto:salubrista

## Deuda registrada

1. Canario manual (invocacion interactiva). Automatizar requiere soporte programatico.
2. Escenario unico. Ampliar con caso de red rural.

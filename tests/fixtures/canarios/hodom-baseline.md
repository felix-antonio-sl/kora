---
canario: hodom-baseline
runtime: claude-code
subagent: hospitalizacion-domiciliaria
subagent_source: ~/.claude/skills/hospitalizacion-domiciliaria/SKILL.md
subagent_source_urn: urn:salud:artefacto:hospitalizacion-domiciliaria
transmuted_at: 2026-05-07T00:00:00+00:00
baseline_captured_at: pending
baseline_status: pending
invocation_mode: interactivo
capture_mechanism: session log (claude-code + skill loaded)
kb_edit_propagation: pendiente
canario_marker: 2026-05-07-hodom-baseline-v1
---

# Canario baseline — hospitalizacion-domiciliaria (claude-code)

Fixture para la primera invocacion con eval de la skill hospitalizacion-domiciliaria.

## Prompt canonico

Carga la skill hospitalizacion-domiciliaria. Un director de hospital regional
quiere implementar una unidad HODOM y te consulta:

"Tenemos 35 pacientes cronicos estables que ocupan camas de medicina interna
con estancias de 18-45 dias. La mayoria son pacientes post-ACV, EPOC reagudizado
resuelto, infecciones urinarias completando tratamiento EV, o ulceras por presion
en curacion. Quiero saber: (a) cuantos de estos 35 serian candidatos a HODOM
segun la norma tecnica chilena, (b) que estructura minima necesito (dotacion,
equipamiento, protocolos), (c) cuales son los criterios de exclusion absoluta
segun el reglamento DS1-2022."

Responde usando exclusivamente el corpus HODOM (normativa chilena + direccion
tecnica) y el corpus de continuidad post-aguda.

## Knowledge Contract esperado

- urn:salud:kb:hodom-reglamento-ds1-2022
- urn:salud:kb:hodom-decreto-exento-31-2024
- urn:salud:kb:hodom-norma-tecnica-2024
- urn:salud:kb:hodom-direccion-tecnica
- urn:salud:kb:hodom-manual-alta-complejidad
- urn:salud:kb:hodom-situacion-chile-2026
- urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss
- urn:salud:kb:post-agudo-ltss-indice
- urn:salud:kb:post-agudo-ltss-transiciones

No debe inventar criterios ni usar normativa extranjera si no esta en el corpus.

## Gate multinivel

| # | Criterio | Pregunta operacional |
|---|----------|----------------------|
| 1 | Trazabilidad al corpus | Cita al menos 3 URNs del corpus HODOM con tool calls? |
| 2 | Criterios de inclusion/exclusion | Aplica los criterios de la norma tecnica chilena (no criterios genericos)? Distingue exclusion absoluta vs relativa? |
| 3 | Estructura minima | Describe dotacion, equipamiento y protocolos segun la direccion tecnica del corpus? |
| 4 | Marco normativo | Cita el reglamento DS1-2022 y el decreto 31-2024 como base legal? |
| 5 | Respeto del corpus | No inventa normativa, cifras ni criterios fuera del corpus chileno? |

## Output de referencia esperado

- Criterios de inclusion: estabilidad clinica, soporte familiar/cuidador,
  entorno domiciliario seguro, accesibilidad geografica, consentimiento
- Criterios de exclusion absoluta: inestabilidad hemodinamica, necesidad de
  monitorizacion invasiva continua, ventilacion mecanica, falta de cuidador
- Estructura minima: medico director, enfermera coordinadora, kinesiologo,
  TENS, protocolos de ingreso/egreso/escalamiento
- Marco legal: reglamento DS1-2022 establece la figura, decreto 31-2024
  aprueba la norma tecnica, norma tecnica 2024 detalla estandares

## Lazo Kelly reproducible

1. Cargar skill hospitalizacion-domiciliaria en sesion claude-code
2. Invocar con el prompt canonico
3. Verificar output: criterios inclusion/exclusion segun norma chilena,
   estructura minima, marco normativo citado
4. Registrar: kora record-invocation --agent-urn urn:salud:artefacto:hospitalizacion-domiciliaria

## Deuda registrada

1. Invocacion manual. Automatizar requiere soporte programatico.
2. Escenario unico. Ampliar con caso pediatrico o rural.

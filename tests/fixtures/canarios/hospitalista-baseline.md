---
canario: hospitalista-baseline
runtime: claude-code
subagent: hospitalista
subagent_source: ~/.claude/skills/hospitalista/SKILL.md
subagent_source_urn: urn:salud:artefacto:hospitalista
transmuted_at: 2026-05-07T00:00:00+00:00
baseline_captured_at: pending
baseline_status: pending
invocation_mode: interactivo
capture_mechanism: session log (claude-code + skill loaded)
kb_edit_propagation: pendiente
canario_marker: 2026-05-07-hospitalista-baseline-v1
---

# Canario baseline — hospitalista (claude-code)

Fixture para la primera invocacion con eval de la skill hospitalista cargada
en sesion de claude-code junto al agente salubrista.

## Prompt canonico

Carga la skill hospitalista. Un jefe de servicio de medicina interna te consulta:

"Tenemos 42 camas de medicina interna con ocupacion promedio del 96%.
La estancia media es de 8.3 dias. Hay 12 pacientes con estancia mayor a 14 dias
que estan clinicamente estables pero esperando cupo en centros de rehabilitacion
o HODOM. El servicio de urgencias nos presiona para admitir mas rapido. Tasa de
readmision a 30 dias: 22%. Que intervenciones recomiendas para descongestionar
el servicio?"

Responde usando el corpus de gestion de redes, management engineering y HODOM.

## Knowledge Contract esperado

- urn:salud:kb:salubrista
- urn:salud:kb:salubrista-atlas-integrado
- urn:salud:kb:salubrista-body-of-knowledge
- urn:salud:kb:salubrista-fuentes-base-curadas
- urn:salud:kb:salubrista-fuente-management-engineering
- urn:salud:kb:salubrista-fuente-continuidad-post-aguda-ltss
- urn:salud:kb:gestion-redes-general
- urn:salud:kb:gestion-redes-unidades
- urn:salud:kb:gestion-redes-urgencias
- urn:salud:kb:gestion-redes-herramientas
- urn:salud:kb:management-engineering-ext-capacidad
- urn:salud:kb:health-systems-science-operativa

## Gate multinivel

| # | Criterio | Pregunta operacional |
|---|----------|----------------------|
| 1 | Trazabilidad al corpus | Cita al menos 3 URNs con tool calls? |
| 2 | Diagnostico de capacidad | Identifica la ocupacion 96% como critica, la ALOS de 8.3 como posiblemente excesiva, y los 12 pacientes bloqueados como cuello de botella de alta? |
| 3 | Intervenciones especificas | Propone criterios de alta oportuna, activacion HODOM para los 12, y analisis de readmisiones? |
| 4 | Vinculacion con urgencias | Conecta el problema de capacidad del servicio con el boarding time en urgencias? |
| 5 | Respeto del corpus | No inventa protocolos, cifras ni normativa fuera del corpus? |

## Output de referencia esperado

- ALOS 8.3 dias con 12 pacientes >14 dias: hay pacientes que no necesitan cama
  de agudos sino continuidad de cuidados (HODOM, rehabilitacion, LTSS)
- Readmision 22%: investigar si las altas son prematuras para liberar camas
- Propuesta: evaluar los 12 pacientes con criterios HODOM de la norma tecnica.
  Los que califiquen → alta a HODOM. Los que no → gestionar cupo en post-agudo.
- Vinculacion urgencias-servicio: el boarding time no se resuelve admitiendo
  mas rapido sino acelerando las altas (pull vs push)

## Lazo Kelly reproducible

1. Cargar skill hospitalista en sesion claude-code
2. Invocar con el prompt canonico
3. Verificar output: ALOS analizada, criterios HODOM para los 12, conexion urgencias
4. Registrar: kora record-invocation --agent-urn urn:salud:artefacto:hospitalista

## Deuda registrada

1. Invocacion manual. Automatizar requiere soporte programatico.
2. Un solo escenario. Ampliar con caso de UCI/UTI.

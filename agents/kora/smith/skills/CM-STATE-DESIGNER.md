---
_manifest:
  urn: "urn:kora:skill:smith-state-designer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-STATE-DESIGNER

## Proposito
Disenha la maquina de estados (FSM) del agente a partir de los modos comportamentales identificados en FTCF, garantizando alcanzabilidad, minimalidad y estados terminales correctos.

## Procedimiento
1. Identificar modos comportamentales del agente desde FTCF-Funcion: cada modo distinto = candidato a estado.
2. Definir `initial_state` = S-DISPATCHER obligatorio (punto de entrada y reorientacion).
3. Disenhar estados: nombre (S-NOMBRE), accion principal, precondicion de entrada.
4. Aplicar constraints:
   - process <= 5 pasos por estado (mas logica → CM separado).
   - Minimo obligatorio: S-DISPATCHER + S-END.
   - Cada estado debe ser alcanzable desde S-DISPATCHER.
   - Estados terminales: solo S-END (trans: [terminal]).
5. Disenhar transiciones: `IF condicion → S-ESTADO`. Cubrir casos: exito, iteracion, cambio de tarea, error.
6. Verificar alcanzabilidad: trazar camino desde S-DISPATCHER a cada estado.
7. Presentar FSM como tabla: Estado | Accion | Transiciones.

## Output
FSM completa con: lista de estados, initial_state, tabla de transiciones, verificacion de alcanzabilidad. Formato listo para poblar `workflows_states` en agent.yaml.

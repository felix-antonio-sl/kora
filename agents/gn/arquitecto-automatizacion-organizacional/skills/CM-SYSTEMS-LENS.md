---
_manifest:
  urn: "urn:gn:skill:arquitecto-automatizacion-organizacional-systems-lens:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ver organizaciones como sistemas dinamicos categoricos. Aplicar framework formal para modelar estructura, interfaces, dinamicas y composicion.

## I/O

- **Input:** Descripcion de organizacion, departamento o proceso a modelar
- **Output:** Modelo de sistema dinamico con estados, interfaces, dinamicas y composicion

## Procedimiento

1. Identificar Sistema Dinamico = (States, Interfaces, Dynamics):
   - States: configuraciones posibles del subsistema
   - Interfaces: (Inputs, Outputs) — lo que entra y sale
   - Dynamics: update(state, input) -> state'

2. Modelar Composicion:
   - Output de A -> Input de B
   - Wiring diagrams para visualizar composicion
   - Identificar dependencias entre subsistemas

3. Analizar Comportamiento:
   - Trajectory = secuencia de estados
   - Steady state = estado que no cambia
   - Identificar ciclos y puntos de equilibrio

4. Definir Functor de Automatizacion: Manual -> Automatizado
   - Preserva interfaces (mismos inputs/outputs)
   - Mejora dynamics (mas rapido, menos errores)

5. Responder preguntas guia:
   - Cuales son los estados posibles de este subsistema?
   - Que inputs recibe y que outputs produce?
   - Como cambia el estado dado un input?
   - Como se conecta con otros subsistemas?

## Signature Output

Modelo formal: States + Interfaces + Dynamics + Composition (diagrama wiring) + Trayectorias identificadas + Oportunidades de automatizacion.

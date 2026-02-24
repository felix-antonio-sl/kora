---
_manifest:
  urn: "urn:kora:skill:smith-cm-designer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CM-DESIGNER

## Proposito
Identifica que logica dentro de los estados debe extraerse a Cognitive Modules (CMs) y disenha cada CM con su firma, trigger y comportamiento encapsulado.

## Procedimiento
1. Revisar cada estado de la FSM: si la accion tiene > 5 pasos o logica reutilizable → extraer a CM.
2. Evaluar inclusion de CMs estandar segun Knowledge Mode:
   - CATALOG-RESOLVER: siempre (resolucion URN → path).
   - KB-GUIDANCE: si KB_BASED o HYBRID (guiar consulta a KB correcta).
   - WEB-SEARCH: si WEB_AUGMENTED o HYBRID (busqueda externa citada).
   - LLM-BOUNDARY: si LLM_NATIVE (delimitar hallucination, indicar incertidumbre).
   - CONTEXT-MANAGER: siempre (deteccion de cambio de tarea entre turnos).
3. Para cada CM nuevo: definir nombre (CM-NOMBRE), proposito (1 linea), inputs, outputs, logica (<=5 pasos).
4. Aplicar regla de encapsulacion: `_meta expose: false` en todos los CMs. CMs no se nombran al usuario.
5. Verificar que cada CM es cohesivo (una responsabilidad) y que no duplica logica de otro CM.
6. Documentar dependencias entre CMs si las hay.

## Output
Lista de CMs del agente: nombre, proposito, inputs/outputs, logica resumida, flag expose:false. Listos para poblar `reasoning_processes` en agent.yaml.

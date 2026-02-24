---
_manifest:
  urn: "urn:gn:skill:digitrans-gore-intake:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTAKE

## Proposito

Clasificar consulta entrante en S-DISPATCHER determinando tipo de solicitud, urgencia y ambito tematico para enrutar al estado correcto de la FSM.

## Procedimiento

1. Recibir consulta del usuario en S-DISPATCHER
2. Clasificar tipo de solicitud: diagnostico_madurez | cumplimiento_normativo | plataformas_tde | desarrollo_acelerado | consulta_general | terminar
3. Evaluar urgencia: alta (plazo legal) | media (proyecto activo) | baja (exploratoria)
4. Determinar ambito: Ley 21.180 | normas tecnicas | ClaveUnica | SIMPLE | DocDigital | PISEE | CPAT | ORKO | general
5. Emitir tupla clasificada (tipo, urgencia, ambito) para decision de transicion en S-DISPATCHER

## Output

Tupla (tipo, urgencia, ambito) que alimenta la decision de transicion del S-DISPATCHER hacia el estado destino correspondiente.

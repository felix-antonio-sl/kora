---
_manifest:
  urn: "urn:kora:skill:guardian-intent-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTENT-CLASSIFIER

## Proposito

Clasificar la intencion del usuario en el estado S-DISPATCHER para enrutar al estado FSM correcto del guardian KORA.

## Procedimiento

1. Leer mensaje del usuario e identificar verbo/objetivo principal
2. Clasificar intencion: EVALUATE (propuesta cambio) | DEFEND (principio cuestionado) | AUDIT (verificar consistencia) | DIAGNOSE (error/drift detectado) | IMPROVE (generar evolucion) | EDUCATE (aprender framework) | REPRESENT (consulta sobre KORA) | END (terminar sesion)
3. Evaluar nivel del usuario: NOVATO (desconoce terminologia) | INTERMEDIO (conoce conceptos) | AVANZADO (domina spec)
4. Identificar componente KORA involucrado: Spec | Agent | Hub | Life | Test | Federation | general
5. Si la intencion es ambigua, formular pregunta de clarificacion minima

## Output

Intencion clasificada con nivel y componente. Enrutamiento al estado FSM correspondiente. Si ambigua: pregunta de clarificacion de una linea.

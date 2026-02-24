---
_manifest:
  urn: "urn:kora:skill:transformer-task-classifier:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-TASK-CLASSIFIER

## Proposito

Clasificar la tarea de koraficacion solicitada en S-DISPATCHER para enrutar al flujo correcto del transformer y establecer el tipo de input esperado.

## Procedimiento

1. Leer mensaje del usuario e identificar objetivo principal
2. Clasificar tarea: TRANSFORM (documento fuente → KORA/MD) | AUDIT (artefacto KORA existente → validar) | COMPARE (documento original + artefacto KORA → fidelidad) | CONSULT (pregunta sobre proceso KORA/Spec) | END (cerrar sesion)
3. Identificar tipo de input disponible o requerido:
   - documento_texto: texto plano, PDF, markdown sin estructura KORA
   - artefacto_koda: YAML/MD ya transformado con manifiestos
   - ambos: original + version transformada para comparacion
4. Determinar objetivo especifico: nuevo_artefacto | validar_existente | comparar_fidelidad
5. Si el input no coincide con la tarea declarada: solicitar clarificacion especifica

## Output

Tarea clasificada (TRANSFORM | AUDIT | COMPARE | CONSULT | END) + tipo de input + objetivo especifico. Solicitud de input faltante si aplica.

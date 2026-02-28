---
_manifest:
  urn: "urn:pro:skill:medico-urgencias-context-manager:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar contexto conversacional multi-turno en sesiones de urgencia. Detectar cambio de paciente vs continuacion caso, mantener estado de retorno post-clarificacion, y gestionar cierre limpio de sesion.

## I/O

- **Input:** Mensaje usuario + contexto_sesion_actual (paciente_activo, estado_retorno, historial_pacientes)
- **Output:** CONTEXT_DECISION: accion (nuevo_paciente|continuar|retorno_clarificacion|cierre), contexto_actualizado

## Procedimiento

### Escenario 1: Deteccion cambio de paciente

Indicadores de nuevo paciente:
1. Nuevas etiquetas XML completas (<historia_antigua> + <informacion_atencion> + <tipo_output>)
2. Datos demograficos incompatibles (edad, sexo, antecedentes radicalmente diferentes)
3. Patologia sin relacion con caso actual
4. Usuario indica explicitamente nuevo paciente

Accion: archivar contexto paciente anterior, inicializar contexto nuevo paciente, resetear estado FSM a S-RECEPTOR.

### Escenario 2: Continuacion mismo paciente

Indicadores de continuacion:
1. Datos complementarios compatibles con caso actual
2. Solicitud de tipo_output diferente para mismo paciente
3. Correccion o actualizacion de datos previos
4. Respuesta a clarificacion solicitada

Accion: actualizar contexto paciente activo, mantener estado FSM actual o transicionar segun tipo_output.

### Escenario 3: Retorno post-clarificacion

Cuando S-CLARIFICADOR solicito dato:
1. Registrar estado_retorno (estado FSM origen)
2. Registrar dato_solicitado (que se pidio)
3. Al recibir respuesta: validar que responde a lo solicitado
4. Si respuesta = "OMITIR": continuar sin dato, ajustar output
5. Si respuesta valida: incorporar dato, restaurar estado_retorno

Accion: restaurar estado FSM registrado, incorporar dato recibido al contexto.

### Escenario 4: Cierre sesion

Indicadores de cierre:
1. Usuario solicita explicitamente terminar
2. tipo_output no reconocido despues de clarificacion

Accion: confirmar cierre, emitir disclaimer, transicionar a S-END.

### Reglas contexto

- Nunca mezclar datos entre pacientes diferentes
- Mantener separacion estricta de contextos por paciente
- Estado de retorno: LIFO (ultimo clarificador pendiente se resuelve primero)
- Si ambiguedad en cambio de paciente: preguntar al usuario

## Signature Output

```
CONTEXT_DECISION:
  accion: [nuevo_paciente|continuar|retorno_clarificacion|cierre]
  paciente_activo: [id_sesion paciente actual]
  estado_retorno: [estado FSM si aplica, null si no]
  dato_incorporado: [dato recibido si retorno_clarificacion]
  contexto_actualizado: [resumen estado contexto]
```

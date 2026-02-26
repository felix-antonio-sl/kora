---
_manifest:
  urn: "urn:kora:skill:clawmaster-context-manager:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-MANAGER

## Proposito
Gestiona contexto multi-turno para sesiones de soporte OpenClaw. Detecta cambios de tema, preserva estado de instancia entre turnos, y rutea transiciones de estado FSM.

## I/O

- **Input:** mensaje_actual: string (mensaje del usuario), estado_fsm: FSMState, contexto_sesion: SessionContext | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento

### Deteccion de Cambio
Comparar mensaje actual vs estado FSM activo:

| Patron | Clasificacion | Accion |
|--------|--------------|--------|
| Misma instancia, mismo tema | CONTINUAR | Permanecer en estado actual |
| Misma instancia, tema diferente | NUEVO | Evaluar si requiere cambio de estado |
| Instancia diferente | CAMBIO_INSTANCIA | Guardar contexto anterior, iniciar nuevo |
| Volver a tema anterior | ATRAS | Restaurar contexto previo |
| Finalizar | TERMINAR | → S-END |
| Fuera de OpenClaw | FUERA | Rejection scope |

### Estado Persistente
Preservar entre turnos:
- `plataforma`: OS y metodo de instalacion detectado
- `version_openclaw`: version instalada
- `canales_activos`: canales configurados y su estado
- `modelo_principal`: modelo/provider en uso
- `config_snapshot`: ultimo estado de config relevante
- `issues_abiertos`: problemas detectados no resueltos
- `historial_acciones`: log de acciones ejecutadas en sesion

### Transiciones

```
CONTINUAR → mantener estado FSM, seguir procedimiento
NUEVO → CM-INTENT-CLASSIFIER → reclasificar → S-{nuevo_estado}
CAMBIO_INSTANCIA → preservar contexto_anterior, → S-DISPATCHER
ATRAS → restaurar contexto_anterior, → S-{estado_anterior}
TERMINAR → S-END
FUERA → rejection, → S-DISPATCHER
```

### Heuristica de Deteccion
- Palabras clave de cambio: "otra cosa", "ahora", "cambiando de tema", "tambien"
- Palabras clave de continuidad: "y tambien", "ademas", "sobre eso mismo"
- Palabras clave de retorno: "volviendo a", "retomando", "lo anterior"
- Palabras clave de cierre: "listo", "gracias", "eso es todo", "terminamos"
- Indicadores de instancia: IPs, hostnames, nombres de proyecto distintos

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| clasificacion | enum(CONTINUAR\|NUEVO\|CAMBIO_INSTANCIA\|ATRAS\|TERMINAR\|FUERA) | Tipo de cambio de contexto |
| estado_anterior | string | Estado FSM antes de transicion |
| estado_nuevo | string \| null | Estado FSM destino |
| contexto_preservado | string[] | Keys del contexto preservado |

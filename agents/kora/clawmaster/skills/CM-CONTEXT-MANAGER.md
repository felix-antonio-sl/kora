---
_manifest:
  urn: urn:kora:skill:clawmaster-context-manager:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-CONTEXT-MANAGER

## Proposito
Gestiona contexto multi-turno para sesiones de soporte OpenClaw. Detecta cambios de tema y preserva contexto de instancia entre turnos.

## Input/Output
- **Input:** mensaje_actual: string (mensaje del usuario), foco_actual: string | null, contexto_sesion: SessionContext | null
- **Output:** ContextClassification (ver Signature Output)

## Procedimiento
### Deteccion de Cambio
Comparar mensaje actual vs foco operativo activo:

| Patron | Clasificacion | Accion |
|--------|--------------|--------|
| Misma instancia, mismo tema | CONTINUAR | Mantener foco actual |
| Misma instancia, tema diferente | NUEVO | Revisar foco de trabajo |
| Instancia diferente | CAMBIO_INSTANCIA | Guardar contexto anterior e iniciar nuevo foco |
| Volver a tema anterior | ATRAS | Restaurar contexto previo |
| Finalizar | TERMINAR | Marcar cierre solicitado |
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

### Gestion del foco

- CONTINUAR -> mantener foco de trabajo
- NUEVO -> marcar revision del foco
- CAMBIO_INSTANCIA -> preservar contexto anterior e iniciar nuevo foco
- ATRAS -> restaurar referencia semantica previa
- TERMINAR -> marcar cierre solicitado
- FUERA -> aplicar rejection semantico

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
| foco_anterior | string \| null | Referencia semantica al foco previo |
| requiere_revision_de_foco | bool | True si el trabajo actual debe reinterpretarse |
| contexto_preservado | string[] | Keys del contexto preservado |

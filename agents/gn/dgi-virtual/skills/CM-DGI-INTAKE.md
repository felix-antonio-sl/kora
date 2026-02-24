---
_manifest:
  urn: "urn:gn:skill:dgi-virtual-dgi-intake:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-DGI-INTAKE

## Proposito
Diagnosticar y clasificar toda solicitud entrante al DGI Virtual: area funcional, tipo de ayuda requerida, urgencia y division de origen.

## Procedimiento
1. Saludar brevemente como DGI Virtual e invitar a exponer la consulta.
2. Identificar area DGI involucrada: Control de Gestion, Modernizacion de Procesos, Transformacion Digital o Navegacion Social.
3. Clasificar tipo de solicitud: diagnostico, propuesta, orientacion metodologica, validacion o derivacion.
4. Determinar urgencia: inmediata (operacion bloqueada), normal (planificacion) o exploratoria (mejora futura).
5. Registrar division o unidad de origen si se indica.
6. Confirmar clasificacion con el usuario antes de derivar al estado FSM correspondiente.

## Output
Clasificacion confirmada: [Area DGI] + [Tipo solicitud] + [Urgencia] + [Division]. Derivacion al estado FSM apropiado (S-CONTROL, S-PROCESOS, S-DIGITAL, S-ARQUITECTURAL, S-PRODUCCION o S-NAVEGACION).

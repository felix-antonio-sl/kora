---
_manifest:
  urn: "urn:kora:skill:orquestador-generico-role-suggester:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-ROLE-SUGGESTER

## Proposito

Mapear participantes de la orquestacion a roles funcionales segun sus capacidades declaradas en el catalogo KORA, para optimizar la colaboracion multi-agente.

## Procedimiento

1. Recibir lista de participantes (URNs) y objetivo de la orquestacion
2. Para cada participante: resolver URN via catalog, leer capacidades declaradas en su SOUL.md/AGENTS.md
3. Mapear capacidades a roles disponibles:
   - ANALISTA: examina, diagnostica, descompone problemas
   - DISENADOR: propone soluciones, arquitectura, estructura
   - IMPLEMENTADOR: genera artefactos, codigo, contenido
   - VALIDADOR: verifica, audita, controla calidad
   - SINTETIZADOR: integra perspectivas, resume, cohesiona
4. Si un participante puede cubrir multiples roles: asignar rol principal segun objetivo
5. Detectar gaps: roles necesarios para el objetivo sin participante asignado
6. Presentar mapeo para confirmacion del usuario antes de iniciar orquestacion

## Output

Tabla participante → rol + justificacion de la asignacion + gaps detectados (roles sin cobertura). Requiere confirmacion del usuario.

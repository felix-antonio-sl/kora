---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-deprecator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-AGENT-DEPRECATOR

## Proposito
Gestiona el retiro ordenado de un agente KORA: identifica dependencias, marca deprecated, propone migracion, archiva.

## Procedimiento
1. IDENTIFICAR DEPENDENCIAS: Buscar en catalogo y otros agentes referencias al agente objetivo (URNs, adjunciones, sub_agents).
2. EVALUAR IMPACTO: ¿Cuantos agentes dependen de este? ¿Hay sucesor definido? ¿Hay usuarios activos?
3. PROPONER MIGRACION: Si hay sucesor, documentar mapping de capacidades antiguo→nuevo. Si no hay sucesor, advertir.
4. MARCAR DEPRECATED: Agregar status: deprecated en frontmatter de todos los archivos del workspace. Agregar nota de redireccion en AGENTS.md.
5. ACTUALIZAR REFERENCIAS: En agentes dependientes, actualizar adjunciones/sub_agents apuntando al sucesor.
6. NOTIFICAR: Generar resumen de deprecacion con lista de cambios realizados.

## Output
Reporte de deprecacion: {agente, sucesor, dependencias_encontradas: [], migraciones_realizadas: [], status: deprecated}.

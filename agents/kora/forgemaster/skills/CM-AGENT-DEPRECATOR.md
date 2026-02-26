---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-deprecator:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-AGENT-DEPRECATOR

## Proposito
Gestiona el retiro ordenado de un agente KORA: identifica dependencias, marca deprecated, propone migracion, archiva.

## I/O

- **Input:** agent_path: string (ruta al workspace del agente a deprecar), sucesor_urn: string | null (URN del agente sucesor si existe)
- **Output:** DeprecationReport (ver Signature Output)

## Procedimiento
1. IDENTIFICAR DEPENDENCIAS: Buscar en catalogo y otros agentes referencias al agente objetivo (URNs, wiring, sub_agents).
2. EVALUAR IMPACTO: ¿Cuantos agentes dependen de este? ¿Hay sucesor definido? ¿Hay usuarios activos?
3. PROPONER MIGRACION: Si hay sucesor, documentar mapping de capacidades antiguo→nuevo. Si no hay sucesor, advertir.
4. MARCAR DEPRECATED: Agregar status: deprecated y deprecated_by en frontmatter de todos los archivos del workspace.
5. ACTUALIZAR REFERENCIAS: En agentes dependientes, actualizar wiring/sub_agents apuntando al sucesor.
6. NOTIFICAR: Generar resumen de deprecacion con lista de cambios realizados.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| agente | string | Nombre del agente deprecado |
| sucesor | string\|null | URN del sucesor si existe |
| dependencias_encontradas | string[] | Agentes que referenciaban al deprecado |
| migraciones_realizadas | string[] | Cambios en agentes dependientes |
| status | enum(deprecated) | Status final |

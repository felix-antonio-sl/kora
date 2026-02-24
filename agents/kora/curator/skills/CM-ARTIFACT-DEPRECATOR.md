---
_manifest:
  urn: "urn:kora:skill:curator-artifact-deprecator:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-ARTIFACT-DEPRECATOR

## Proposito
Gestiona el fin de vida de artefactos de conocimiento: identifica dependencias, marca deprecated, agrega redireccion y propone migracion.

## Procedimiento
1. IDENTIFICAR DEPENDENCIAS:
   - Buscar en catalogo: ¿que otros artefactos referencian este URN?
   - Buscar en agentes: ¿algun config.json lista este URN en allowed_kb?
   - Buscar en skills: ¿algun CM referencia este artefacto?
2. EVALUAR IMPACTO:
   - Cantidad de dependencias.
   - Criticidad de las dependencias (specs fundacionales > KBs > guias).
   - ¿Existe sucesor? ¿El conocimiento migro a otro artefacto?
3. MARCAR DEPRECATED:
   - Cambiar status: published → deprecated en frontmatter.
   - Agregar nota de deprecacion al inicio del cuerpo:
     ```markdown
     > **DEPRECATED** — Este artefacto esta deprecado desde {fecha}.
     > Sucesor: [{nombre}]({urn_sucesor}) (si aplica).
     > Razon: {motivo}.
     ```
4. PROPONER MIGRACION (si hay sucesor):
   - Listar artefactos que referencian el URN deprecado.
   - Para cada uno: proponer actualizacion de referencia al sucesor.
   - Para config.json de agentes: proponer actualizacion de allowed_kb.
5. REGISTRAR: ejecutar kora index para actualizar catalogo.

## Output
Artefacto deprecado. Reporte: {urn_deprecado, dependencias_encontradas[], sucesor_urn?, migraciones_propuestas[], catalogo_actualizado: bool}.

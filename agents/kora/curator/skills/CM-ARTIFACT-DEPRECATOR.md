---
_manifest:
  urn: "urn:kora:skill:curator-artifact-deprecator:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-ARTIFACT-DEPRECATOR

## Proposito
Gestiona el fin de vida de artefactos de conocimiento: identifica dependencias, marca deprecated, agrega redireccion y propone migracion.

## I/O

- **Input:** artefacto_urn: URN (artefacto a deprecar), razon: string, sucesor_urn: URN | null
- **Output:** DeprecationReport (ver Signature Output)

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
5. REGISTRAR: Indicar al usuario: ejecutar `kora index` para actualizar catalogo.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| urn_deprecado | URN | URN del artefacto deprecado |
| dependencias_encontradas | string[] | Artefactos que referencian el URN |
| sucesor_urn | URN \| null | URN del sucesor (si aplica) |
| migraciones_propuestas | string[] | Actualizaciones de referencia sugeridas |
| catalogo_actualizado | bool | Si el usuario ejecuto kora index |

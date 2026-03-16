---
_manifest:
  urn: urn:kora:skill:forgemaster-artifact-emitter:1.0.0
  type: lazy_load_endofunctor
---

# CM-ARTIFACT-EMITTER

## Proposito
Escribe artefactos derivados de transmutacion al directorio de output, generando el manifest de sincronizacion `_transmutation.yml` con metadata de trazabilidad.

## Input/Output
- **Input:** artifacts: TransmutedArtifact[] (artefactos generados por adapter), output_dir: string, source_analysis: WorkspaceAnalysis
- **Output:** EmissionReport (ver Signature Output)

## Procedimiento
1. Validar directorio de output: crear si no existe, verificar permisos de escritura.
2. Para cada artefacto en artifacts[]:
   - Verificar que contenido no contiene frontmatter YAML KORA residual (R2).
   - Escribir archivo en ruta especificada dentro de output_dir.
   - Registrar ruta y hash del artefacto escrito.
3. Generar `_transmutation.yml` con:
   ```yaml
   source:
     agent: {namespace}/{nombre}
     path: {agent_path}
     hashes: {componente: SHA-256 de cada archivo fuente}
   target:
     platform: {openclaw|anthropic}
     output_dir: {ruta}
     artifacts: [{path, hash}]
   metadata:
     transmitted_at: {ISO-8601}
     agent_spec_version: {version de agent-spec-md usada}
     runtime_spec_version: {version de runtime-spec-md usada}
     transmutador_version: 1.0.0
   ```
4. Escribir `_transmutation.yml` en output_dir.
5. Presentar tabla resumen: archivo | tipo | tamano | hash.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| files_written | string[] | Rutas de archivos escritos |
| manifest_path | string | Ruta del _transmutation.yml |
| total_files | number | Cantidad de archivos generados |
| total_bytes | number | Tamano total en bytes |

---
_manifest:
  urn: urn:kora:skill:forgemaster-artifact-emitter:1.1.0
  type: lazy_load_endofunctor
---

# CM-ARTIFACT-EMITTER

## Proposito
Escribe artefactos derivados de transmutacion al directorio de output y es el unico responsable de generar el manifest de sincronizacion `_transmutation.yml` con metadata de trazabilidad.

## Input/Output
- **Input:** artifacts: TransmutedArtifact[] (artefactos generados por adapter), output_dir: string, source_analysis: WorkspaceAnalysis, manifest_overrides: object | null
- **Output:** EmissionReport (ver Signature Output)

## Procedimiento
1. Validar directorio de output: crear si no existe, verificar permisos de escritura. **R-TRANSMUTE-6**: output_dir DEBE ser un directorio de staging (default: `{kora_repo}/output/{namespace}-{agent}/`). Rechazar si output_dir apunta a paths de produccion (`/srv/`, containers, volumes Docker). El deploy a produccion es responsabilidad de ops/clawstack.
2. Para cada artefacto en artifacts[]:
   - Rechazar si algun artefacto intenta materializar `_transmutation.yml`; el manifest lo emite exclusivamente este Skill.
   - Verificar que contenido no contiene frontmatter YAML KORA residual (runtime-spec §9.2).
   - Escribir archivo en ruta especificada dentro de output_dir.
   - Registrar ruta y hash del artefacto escrito.
3. Generar `_transmutation.yml` fusionando metadata base + `manifest_overrides` del adapter:
   ```yaml
   source:
     agent: {namespace}/{nombre}
     path: {agent_path}
     hashes: {componente: SHA-256 de cada archivo fuente}
   target:
     platform: {manifest_overrides.platform}
     output_dir: {ruta}
     artifacts: [{path, hash}]
   metadata:
     transmitted_at: {ISO-8601}
     agent_spec_version: {version de agent-spec-md usada}
     runtime_spec_version: {version de runtime-spec-md usada}
     transmutador_version: 1.0.0
   ```
   - Campos target-specific (`deployment_hints`, `exclusions`, `enforcement_gaps`, `behavioral_equivalence`, etc.) vienen en `manifest_overrides`.
4. Escribir `_transmutation.yml` en output_dir.
5. Verificar que ningun artefacto emitido contiene frontmatter KORA ni _manifest residual (runtime-spec §9.2, skill-spec §6 inv.7).
6. Presentar tabla resumen: archivo | tipo | tamano | hash.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| files_written | string[] | Rutas de archivos escritos |
| manifest_path | string | Ruta del _transmutation.yml |
| total_files | number | Cantidad de archivos generados |
| total_bytes | number | Tamano total en bytes |

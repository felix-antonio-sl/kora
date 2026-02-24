---
_manifest:
  urn: "urn:kora:skill:curator-artifact-editor:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-ARTIFACT-EDITOR

## Proposito
Modifica artefactos de conocimiento existentes preservando todos los invariantes de la spec correspondiente. Gestiona versionamiento semantico.

## Procedimiento
1. LEER artefacto completo. Clasificar tipo (descriptivo/prescriptivo).
2. IDENTIFICAR alcance del cambio:
   - Contenido: agregar/modificar/eliminar informacion en el cuerpo.
   - Estructura: reorganizar headings, promover prosa a tabla, dividir/fusionar secciones.
   - Frontmatter: actualizar tags, source, status.
3. EVALUAR impacto en invariantes:
   - Fidelidad: ¿el cambio pierde informacion? Si es eliminacion, ¿la info es realmente obsoleta?
   - SSOT: ¿el cambio introduce duplicacion?
   - Independencia chunk: ¿el cambio rompe autosuficiencia de algun ##?
   - Referencias: ¿el cambio invalida URN o refs internas?
4. APLICAR modificacion:
   - Preservar estilo telegrafico (KORA/MD) o normativo (KORA/Spec-MD).
   - Preservar idioma del artefacto.
   - Si prescriptivo: keywords RFC 2119 en negrita, par Correcto/Incorrecto si aplica.
5. BUMP VERSION (SemVer):
   - Patch: correccion sin cambio informativo/normativo.
   - Minor: info/regla nueva compatible con lo existente.
   - Major: cambio que invalida lecturas previas.
6. VERIFICAR resultado contra checklist correspondiente (invocar CM-ARTIFACT-AUDITOR mentalmente).

## Output
Artefacto editado con version bumped. Reporte: {cambios_aplicados[], version_anterior, version_nueva, invariantes_preservados: bool}.

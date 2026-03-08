---
_manifest:
  urn: "urn:kora:kb:md-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "KORA categorical-foundations 05, KORA/Gobernanza v3.0.0"
version: "4.0.0"
status: published
tags: [spec, markdown, conocimiento, rag, frontmatter]
lang: es
---

# KORA/MD v4.0.0

## 1. Definicion

KORA/MD es el formato de artefactos descriptivos del ecosistema KORA. Optimiza almacenamiento, indexación y recuperación para humanos y LLMs sin mezclar concerns de ejecución.

KORA/MD gobierna conocimiento, no workspaces, ni runtime, ni configuración operativa.

## 2. Modelo del artefacto

Todo artefacto KORA/MD tiene dos capas:

1. Frontmatter YAML base.
2. Cuerpo de conocimiento Markdown.

### 2.1 Frontmatter base

```yaml
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencia}"
version: "{semver}"
status: draft|published|deprecated
tags: [{tag1}, {tag2}, {tag3}]
lang: "{iso-639-1}"
extensions: {}
---
```

Reglas:

1. El régimen de identidad es conceptual: URN tripartito + versión fuera del URN.
2. El sobre base es cerrado.
3. Metadata adicional **DEBE** residir en `extensions.{namespace}`.
4. `tags` **DEBE** contener al menos 3 tags semánticos.
5. `lang` describe el idioma del cuerpo.
6. `source` describe la procedencia humana o documental del conocimiento.

## 3. Catálogo y fuente de verdad

El filesystem con manifests es la fuente de verdad. El catálogo es una vista materializada derivada.

Consecuencias:

- `kora index` reconstruye el catálogo; no revela una verdad superior.
- Un artefacto existe por estar bien formado en el repo, no por aparecer primero en el catálogo.
- El catálogo **DEBERIA** mantenerse completo y regenerable.

## 4. Cuerpo de conocimiento

El cuerpo **DEBE** privilegiar estructura recuperable sobre prosa ornamental.

Permitido:

- headings
- listas
- tablas
- definiciones
- fórmulas
- ejemplos mínimos

Desaconsejado:

- transiciones narrativas
- relleno editorial
- referencias vagas sin ancla

La inteligibilidad humana sigue siendo valiosa; KORA/MD no obliga a telegráfico caricaturesco si eso destruye precisión o recuperabilidad.

## 5. Referencias

Tipos permitidos:

- interna: `[-> Seccion]`
- KORA: `[Descripcion](urn:{ns}:{type}:{id})`
- externa: `[Descripcion](https://...)`

Reglas:

1. Las referencias internas **DEBEN** apuntar a headings existentes.
2. Las referencias KORA **NO DEBEN** incluir versión en artefactos conceptuales.
3. Los fragments `#...` **DEBERIAN** usarse solo cuando aportan precisión real.

## 6. Chunking y recuperación

Un `##` define la unidad primaria de recuperación. Cada `##` **DEBERIA** ser comprensible de forma casi aislada:

- sujeto claro,
- alcance claro,
- dependencia explícita cuando exista,
- acrónimos definidos o enlazados.

## 7. Versionado

- Corrección editorial sin cambio semántico: patch
- Adición compatible de conocimiento: minor
- Reestructuración incompatible o cambio semántico mayor: major

## 8. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Frontmatter valido | Cumple el sobre base y usa `extensions` para metadata extra | schema | Corregir frontmatter |
| Regimen de identidad | URN tripartito y version fuera del URN | schema | Migrar identidad |
| Catalogo derivado | El artefacto es indexable y regenerable por CLI | lint | Corregir manifest o indexador |
| Referencias validas | URNs, headings y fragments resuelven | lint | Corregir referencias |
| Chunk recuperable | Cada `##` es recuperable sin anafora crítica | manual | Reescribir sección |
| Tags semanticos | Hay al menos 3 tags útiles | lint | Agregar tags |

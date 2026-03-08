---
_manifest:
  urn: "urn:kora:kb:spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "RFC 2119, KORA categorical-foundations 05, KORA/Gobernanza v3.0.0"
version: "4.0.0"
status: published
tags: [spec, formato, prescriptivo, enforcement, traces]
lang: es
---

# KORA/Spec-MD v4.0.0

## 1. Definicion

KORA/Spec-MD es el formato de ley operativa del ecosistema KORA. Sirve para especificaciones, protocolos y documentos prescriptivos. No describe hechos; gobierna comportamientos, contratos y validaciones.

## 2. Estructura

Todo documento KORA/Spec-MD **DEBE** tener:

1. Frontmatter YAML base.
2. Cuerpo prescriptivo Markdown.

### 2.1 Frontmatter base

Campos obligatorios:

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

- El sobre base es cerrado.
- Metadata adicional **DEBE** vivir dentro de `extensions.{namespace}`.
- El URN de KORA/Spec-MD es conceptual y usa el régimen tripartito.

## 3. Lenguaje normativo

Keywords permitidas:

- **DEBE**
- **NO DEBE**
- **DEBERIA**
- **NO DEBERIA**
- **PUEDE**

Toda regla normativa **DEBE** usar una de esas keywords o ser claramente auxiliar.

Texto auxiliar permitido:

- `Correcto:`
- `Incorrecto:`
- `Rationale:`
- tablas de validacion
- definiciones

Hedging normativo (`quizas`, `idealmente`, `seria bueno`) **NO DEBE** reemplazar una keyword.

## 4. Trazabilidad y rationale

### 4.1 `Traces to:`

Una regla con justificacion formal oficial **DEBERIA** incluir:

```markdown
Traces to: formal/{doc} §{seccion} ({teorema})
```

Reglas:

1. `Traces to:` **DEBE** apuntar solo a la Formal Layer oficial.
2. Una regla pragmatica **NO DEBE** fingir respaldo formal.
3. La ausencia de `Traces to:` no debilita una regla; solo indica que su justificacion es operacional o pragmatica.

### 4.2 `Rationale:`

`Rationale:` explica motivos conceptuales, ergonomicos o auxiliares. No agrega obligaciones nuevas. Es el lugar correcto para intuiciones provenientes de `fxsl/cat` no absorbidas oficialmente.

## 5. Enforcement

Toda tabla de validacion nueva o reescrita **DEBE** incluir una columna `Enforcement`.

Valores permitidos:

- `schema`
- `lint`
- `runtime`
- `manual`

## 6. Gramatica minima

Todo documento KORA/Spec-MD **DEBE** incluir, en este orden logico:

1. `## Definicion`
2. `##` secciones normativas
3. `## Validacion`

Se recomienda adicionalmente:

- `## Definiciones`
- `## Ejemplos`
- `## Migracion`

## 7. Versionado

- Cambio editorial sin impacto normativo: patch
- Regla nueva compatible: minor
- Cambio incompatible de ley: major

## 8. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Frontmatter valido | Cumple el sobre base y usa `extensions` para metadata extra | schema | Corregir frontmatter |
| Keyword explicita | Toda obligación importante usa keyword RFC 2119 | lint | Reescribir regla |
| Traces oficiales | `Traces to:` solo referencia Formal Layer oficial | lint | Corregir o reemplazar por `Rationale:` |
| Rationale no normativo | `Rationale:` no introduce deberes nuevos | manual | Mover regla al cuerpo normativo |
| Enforcement declarado | Toda tabla nueva o reescrita incluye columna `Enforcement` | lint | Completar tabla |
| Versionado coherente | El bump de `version` corresponde al impacto normativo | manual | Ajustar SemVer |

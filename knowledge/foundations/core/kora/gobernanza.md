---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "RFC 2119, Anthropic Prompt Engineering Guide, OpenAPI Extension Patterns"
version: 1.0.0
status: published
tags: [gobernanza, ecosistema, precedencia, extensiones, inyeccion-llm]
lang: es
---

# Gobernanza del Ecosistema KORA v1.0

## 1. Definición

Este documento define las reglas de convivencia entre los artefactos del ecosistema KORA. Gobierna tres dominios que no pertenecen a ninguna especificación individual sino al ecosistema como un todo:

1. **Precedencia** — Qué documento gobierna cuando dos se contradicen.
2. **Inyección a LLMs** — Cómo se entregan los artefactos KORA al contexto de un LLM.
3. **Extensiones** — Cómo un namespace extiende las reglas base sin romper compatibilidad.

### 1.1 Alcance

Este documento aplica a todos los artefactos que siguen las especificaciones KORA/MD o KORA/Spec-MD. No aplica a artefactos externos al ecosistema KORA.

---

## 2. Catálogo de Artefactos Fundacionales

El ecosistema KORA se sostiene sobre los siguientes documentos fundacionales:

| URN                           | Tipo       | Governs                                               |
| ----------------------------- | ---------- | ----------------------------------------------------- |
| `urn:kora:kb:md-spec`         | Spec       | Formato de artefactos de conocimiento descriptivo     |
| `urn:kora:kb:spec-md`         | Spec       | Formato de documentos prescriptivos                   |
| `urn:kora:kb:wf-koraficacion` | Workflow   | Estrategia de ejecución para transformación a KORA/MD |
| `urn:kora:kb:gobernanza`      | Gobernanza | Precedencia, inyección y extensiones (este documento) |

---

## 3. Precedencia Inter-Documentos

### 3.1 Regla General

Cuando dos artefactos KORA contienen reglas que se contradicen, la resolución sigue este orden de precedencia (mayor a menor):

1. **Este documento** (`urn:kora:kb:gobernanza`) — Prevalece sobre todo. Define las meta-reglas.
2. **La especificación del tipo de artefacto** — `md-spec.md` para artefactos descriptivos, `spec-md.md` para prescriptivos. Cada una gobierna su dominio.
3. **Workflows y guías derivadas** — Documentos operativos que implementan las especificaciones. No pueden contradecirlas.
4. **Extensiones de namespace** — Reglas específicas de un namespace. No pueden contradecir las capas superiores.

### 3.2 Conflicto Entre Especificaciones

Si `md-spec.md` y `spec-md.md` contienen reglas mutuamente contradictorias sobre un mismo tema, cada una **DEBE** prevalecer sobre la otra exclusivamente dentro de su dominio:

- Para artefactos de conocimiento descriptivo → prevalece `md-spec.md`.
- Para documentos prescriptivos → prevalece `spec-md.md`.

Si el conflicto no puede resolverse por dominio (afecta a ambos tipos), este documento de gobernanza **DEBE** ser actualizado con una resolución explícita.

### 3.3 Regla de Silencio

Si una especificación no dice nada sobre un tema, eso no significa permiso. El silencio **NO DEBE** interpretarse como autorización. Ante la duda, la opción más restrictiva compatible con el espíritu de la especificación prevalece.

---

## 4. Inyección a LLMs

### 4.1 Principio General

Los artefactos KORA están diseñados para ser consumidos por LLMs, pero la forma en que se entregan al contexto del modelo depende del runtime. Este documento define patrones recomendados, no obligaciones de formato.

### 4.2 Separación Frontmatter / Cuerpo

El frontmatter YAML **DEBERÍA** ser procesado por el orquestador (indexador, CLI, pipeline RAG) y no incluido en el texto que recibe el LLM. El frontmatter contiene metadata de máquina; el LLM consume el cuerpo.

### 4.3 Patrones de Inyección por Runtime

| Runtime                | Patrón Recomendado                               | Notas                                                                                |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **OpenClaw**           | Artefactos como Skills (`SKILL.md` wrapper)      | Carga on-demand, no en bootstrap permanente                                          |
| **Claude (Anthropic)** | XML tags para delimitar secciones                | Claude fue entrenado con XML; `<rules>`, `<context>`, `<examples>` mejoran precisión |
| **GPT (OpenAI)**       | Markdown con headers claramente jerarquizados    | Los modelos GPT responden bien a Markdown estructurado nativo                        |
| **Gemini (Google)**    | Markdown nativo, prompts con estructura definida | Similar a GPT; sin preferencia declarada por delimitadores                           |
| **RAG genérico**       | Chunking por `##`, stripping de frontmatter      | Estándar para cualquier pipeline de vectorización                                    |

### 4.4 Wrappers Opcionales

Cuando un artefacto KORA se inyecta como skill en un runtime que soporta delimitadores, el wrapper **PUEDE** envolver el contenido con tags del runtime sin alterar el artefacto fuente:

```xml
<!-- Wrapper para Claude -->
<kora_spec>
[contenido del artefacto KORA sin frontmatter]
</kora_spec>
```

El artefacto fuente en disco permanece inalterado. El wrapper se genera dinámicamente en el momento de la inyección.

---

## 5. Extensiones por Namespace

### 5.1 Principio

Un namespace **PUEDE** definir reglas prescriptivas adicionales que aplican exclusivamente a los artefactos de ese namespace. Ninguna extensión **DEBE** contradecir las especificaciones base (`md-spec.md`, `spec-md.md`).

### 5.2 Formato de Extensión

Una extensión de namespace se materializa como un artefacto KORA/Spec-MD con las siguientes restricciones:

- URN: `urn:{namespace}:kb:ext-{nombre}`
- **DEBE** referenciar explícitamente la especificación base que extiende.
- **DEBE** declarar en §1 que es una extensión, no un reemplazo.
- Solo **PUEDE** agregar reglas o restringir las existentes. No **PUEDE** relajarlas.

**Correcto:** Una extensión que agrega un campo obligatorio al frontmatter para el namespace `gn`:

```yaml
# En urn:gn:kb:ext-frontmatter
# Extiende: urn:kora:kb:md-spec

# Además de los campos base, los artefactos gn DEBEN incluir:
region: "nuble"
```

**Incorrecto:** Una extensión que permite headings de profundidad `#####` (viola `md-spec.md` §4.1).

### 5.3 Precedencia de Extensiones

Las extensiones aplican **solo dentro del namespace que las define**. Un artefacto `urn:gn:kb:protocolo-seguridad` se valida contra:

1. `urn:kora:kb:md-spec` (base)
2. `urn:gn:kb:ext-frontmatter` (extensión del namespace gn)

Un artefacto `urn:tde:kb:guia-implementacion` no está sujeto a las extensiones de `gn`.

---

## 6. Validación del Ecosistema

| Check                          | Criterio                                                | Acción si falla                      |
| ------------------------------ | ------------------------------------------------------- | ------------------------------------ |
| Sin contradicciones inter-spec | `md-spec.md` y `spec-md.md` no se contradicen           | Resolución en §3.2 de este documento |
| Extensiones compatibles        | Ninguna extensión relaja reglas base                    | Rechazar extensión                   |
| Nombres de extensión           | URN sigue patrón `urn:{ns}:kb:ext-{nombre}`             | Renombrar                            |
| Wrappers no alteran fuente     | El artefacto en disco está inalterado                   | Revertir cambios al fuente           |
| Frontmatter no inyectado       | El texto que recibe el LLM no contiene YAML frontmatter | Verificar pipeline de inyección      |

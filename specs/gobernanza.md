---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "RFC 2119, Anthropic Prompt Engineering Guide, OpenAPI Extension Patterns"
version: "1.2.0"
status: published
tags: [gobernanza, ecosistema, precedencia, extensiones, inyeccion-llm]
lang: es
---

# Gobernanza del Ecosistema KORA v1.2.0

## 1. Definición

> Este documento es prescriptivo y **ESTÁ GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md).

Este documento define las reglas de convivencia entre los artefactos del ecosistema KORA. Gobierna tres dominios que no pertenecen a ninguna especificación individual sino al ecosistema como un todo:

1. **Precedencia** — Qué documento gobierna cuando dos se contradicen.
2. **Inyección a LLMs** — Cómo se entregan los artefactos KORA al contexto de un LLM.
3. **Extensiones** — Cómo un namespace extiende las reglas base sin romper compatibilidad.

### 1.1 Alcance

Este documento aplica a todos los artefactos que siguen las especificaciones KORA/MD o KORA/Spec-MD. No aplica a artefactos externos al ecosistema KORA.

---

## 2. Definiciones

La tabla de esta sección **DEBE** incluir todo término clave con significado preciso dentro de este documento:

**Correcto:** `El documento usa "Precedencia" y "Wrapper"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Runtime" como término clave y no existe entrada para "Runtime".`

| Término                | Definición                                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Artefacto**          | Archivo Markdown unitario con frontmatter KORA y cuerpo de contenido, gobernado por KORA/MD o KORA/Spec-MD    |
| **Precedencia**        | Orden jerárquico que determina qué documento prevalece cuando dos contienen reglas contradictorias              |
| **Extensión**          | Artefacto KORA/Spec-MD que agrega o restringe reglas dentro de un namespace sin contradecir las bases          |
| **Wrapper**            | Envoltorio generado dinámicamente que adapta un artefacto KORA al formato de un runtime sin alterar la fuente  |
| **Inyección**          | Acto de entregar un artefacto KORA al contexto de un LLM para su consumo                                      |
| **Namespace**          | Primer segmento lógico de un URN; delimita el dominio al que pertenece el recurso (`gn`, `tde`, `kora`)       |
| **Runtime**            | Entorno de ejecución de un LLM (OpenClaw, Claude, GPT, Gemini) que consume artefactos KORA                    |
| **Especificación base** | Documento fundacional que define reglas para un tipo de artefacto (`md-spec.md`, `spec-md.md`)                |
| **Meta-regla**         | Regla de este documento que gobierna la interacción entre especificaciones, no el contenido de una sola        |
| **Funtor G (koraficación)** | Funtor definido en `spec-md.md` que transforma documentos humanos en artefactos KORA/MD (Koraficación). Símbolo: G. |
| **Funtor G₂ (agentificación)** | Funtor definido en `agent-spec-md.md` que transforma YAML monolíticos KODA en workspaces KORA (Agentificación). Símbolo: G₂. |

> **Nota sobre colisión de funtores G:** El ecosistema KORA tiene actualmente dos funtores denominados variantes de G. Para eliminar la ambigüedad, se **DEBERÍA** renombrar el funtor de koraficación en `spec-md.md` a **K** (Kristalization functor) en una futura revisión de esa especificación, reservando G / G₂ para la familia de agentificación en `agent-spec-md.md`. Esta nota es informativa hasta que se actualice `spec-md.md`.

---

## 3. Catálogo de Artefactos Fundacionales

El ecosistema KORA se sostiene sobre los siguientes documentos fundacionales:

| URN                           | Tipo       | Gobierna                                              |
| ----------------------------- | ---------- | ----------------------------------------------------- |
| `urn:kora:kb:md-spec`         | Spec       | Formato de artefactos de conocimiento descriptivo     |
| `urn:kora:kb:spec-md`         | Spec       | Formato de documentos prescriptivos                   |
| `urn:kora:kb:agent-spec-md`   | Spec       | Arquitectura categórica de agentes LLM               |
| `urn:kora:kb:gobernanza`      | Gobernanza | Precedencia, inyección y extensiones (este documento) |

---

## 4. Precedencia Inter-Documentos

### 4.1 Regla General

Cuando dos artefactos KORA contienen reglas que se contradicen, la resolución sigue este orden de precedencia (mayor a menor):

1. **Este documento** (`urn:kora:kb:gobernanza`) — Prevalece sobre todo. Define las meta-reglas.
2. **Las especificaciones del tipo de artefacto** — `md-spec.md` para artefactos descriptivos, `spec-md.md` para prescriptivos. Cada una gobierna su dominio.
   - 2a. **`agent-spec-md.md`** — Especificación que gobierna exclusivamente los workspaces de agentes (directorios `agents/`). Prevalece sobre las extensiones de namespace en todo lo que concierne a la arquitectura interna de un agente (componentes FSM, SOUL, TOOLS, config, skills). No puede contradecir `md-spec.md` ni `spec-md.md`.
3. **Secciones operativas y guías derivadas** — Secciones de ejecución dentro de las especificaciones y guías derivadas. No pueden contradecir las reglas declarativas de la misma especificación.
4. **Extensiones de namespace** — Reglas específicas de un namespace. No pueden contradecir las capas superiores.

### 4.2 Conflicto Entre Especificaciones

Si `md-spec.md` y `spec-md.md` contienen reglas mutuamente contradictorias sobre un mismo tema, cada una **DEBE** prevalecer sobre la otra exclusivamente dentro de su dominio:

- Para artefactos de conocimiento descriptivo → prevalece `md-spec.md`.
- Para documentos prescriptivos → prevalece `spec-md.md`.

Si el conflicto no puede resolverse por dominio (afecta a ambos tipos), este documento de gobernanza **DEBE** ser actualizado con una resolución explícita.

### 4.3 Regla de Silencio

Si una especificación no dice nada sobre un tema, eso no significa permiso. El silencio **NO DEBE** interpretarse como autorización. Ante la duda, la opción más restrictiva compatible con el espíritu de la especificación prevalece.

**Correcto:** `md-spec.md no menciona imágenes → se interpretan como no permitidas (opción restrictiva).`
**Incorrecto:** `md-spec.md no menciona imágenes → se asume que están permitidas por omisión.`

### 4.4 Excepción: Bootstrap URNs de Agentes

Los archivos de bootstrap de agentes (catalogados con `type: agent-bootstrap`) **PUEDEN** usar el formato extendido de cuatro segmentos:

```
urn:{namespace}:agent-bootstrap:{nombre}:{version}
```

Esta excepción al formato tripartito estándar (`urn:{ns}:{type}:{id}`) es legítima porque:

- Los workspaces de agentes requieren versionado explícito para garantizar **bisimulación**: dos versiones del mismo agente pueden coexistir y ser comparadas formalmente.
- El segmento `{version}` no es metadata opcional; es parte del identificador estructural del workspace.

**Correcto:** `urn:gn:agent-bootstrap:goreologo-agents:2.4.0`
**Incorrecto:** `urn:gn:agent-bootstrap:goreologo-agents` (omite versión, impide bisimulación)

Esta excepción aplica **únicamente** a artefactos con `type: agent-bootstrap`. Todos los demás artefactos DEBEN usar el formato tripartito.

---

## 5. Inyección a LLMs

### 5.1 Principio General

Los artefactos KORA están diseñados para ser consumidos por LLMs, pero la forma en que se entregan al contexto del modelo depende del runtime. Este documento define patrones recomendados, no obligaciones de formato.

### 5.2 Separación Frontmatter / Cuerpo

El frontmatter YAML **DEBERÍA** ser procesado por el orquestador (indexador, CLI, pipeline RAG) y no incluido en el texto que recibe el LLM. El frontmatter contiene metadata de máquina; el LLM consume el cuerpo.

**Correcto:** `El pipeline RAG parsea el frontmatter para indexación y entrega solo el cuerpo Markdown al LLM.`
**Incorrecto:** `El pipeline inyecta el artefacto completo (frontmatter + cuerpo) en el contexto del LLM.`

### 5.3 Patrones de Inyección por Runtime

| Runtime                | Patrón Recomendado                               | Notas                                                                                |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------ |
| **OpenClaw**           | Artefactos como Skills (`SKILL.md` wrapper)      | Carga on-demand, no en bootstrap permanente                                          |
| **Claude (Anthropic)** | XML tags para delimitar secciones                | Claude fue entrenado con XML; `<rules>`, `<context>`, `<examples>` mejoran precisión |
| **GPT (OpenAI)**       | Markdown con headers claramente jerarquizados    | Los modelos GPT responden bien a Markdown estructurado nativo                        |
| **Gemini (Google)**    | Markdown nativo, prompts con estructura definida | Similar a GPT; sin preferencia declarada por delimitadores                           |
| **RAG genérico**       | Chunking por `##`, stripping de frontmatter      | Estándar para cualquier pipeline de vectorización                                    |

### 5.4 Wrappers Opcionales

Cuando un artefacto KORA se inyecta como skill en un runtime que soporta delimitadores, el wrapper **PUEDE** envolver el contenido con tags del runtime sin alterar el artefacto fuente:

```xml
<!-- Wrapper para Claude -->
<kora_spec>
[contenido del artefacto KORA sin frontmatter]
</kora_spec>
```

El artefacto fuente en disco permanece inalterado. El wrapper se genera dinámicamente en el momento de la inyección.

---

## 6. Extensiones por Namespace

### 6.1 Principio

Un namespace **PUEDE** definir reglas prescriptivas adicionales que aplican exclusivamente a los artefactos de ese namespace. Ninguna extensión **DEBE** contradecir las especificaciones base (`md-spec.md`, `spec-md.md`).

### 6.2 Formato de Extensión

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

### 6.3 Precedencia de Extensiones

Las extensiones aplican **solo dentro del namespace que las define**. Un artefacto `urn:gn:kb:marco-legal-gores` se valida contra:

1. `urn:kora:kb:md-spec` (base)
2. `urn:gn:kb:gestion-ipr` (extensión del namespace gn, si existe)

Un artefacto `urn:tde:kb:sistema-tde-2025` no está sujeto a las extensiones de `gn`.

---

## 7. Validación del Ecosistema

| Check                          | Criterio                                                | Acción si falla                      |
| ------------------------------ | ------------------------------------------------------- | ------------------------------------ |
| Sin contradicciones inter-spec | `md-spec.md` y `spec-md.md` no se contradicen           | Resolución en §4.2 de este documento |
| Extensiones compatibles        | Ninguna extensión relaja reglas base                    | Rechazar extensión                   |
| Nombres de extensión           | URN sigue patrón `urn:{ns}:kb:ext-{nombre}`             | Renombrar                            |
| Wrappers no alteran fuente     | El artefacto en disco está inalterado                   | Revertir cambios al fuente           |
| Frontmatter no inyectado       | El texto que recibe el LLM no contiene YAML frontmatter | Verificar pipeline de inyección      |

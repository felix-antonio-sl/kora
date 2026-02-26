---
_manifest:
  urn: "urn:kora:kb:gobernanza"
  provenance:
    created_by: "FS"
    created_at: "2026-02-26"
    source: "RFC 2119, Anthropic Prompt Engineering Guide, OpenAPI Extension Patterns, KORA categorical-foundations 00-05"
version: "2.1.0"
status: published
tags: [gobernanza, ecosistema, precedencia, extensiones, inyeccion-llm, skill, cross-platform, traceability]
lang: es
---

# Gobernanza del Ecosistema KORA v2.1.0

## 1. Definicion

> Este documento es prescriptivo y **ESTA GOBERNADO** por [KORA/Spec-MD](urn:kora:kb:spec-md).

Este documento define las reglas de convivencia entre los artefactos del ecosistema KORA. Gobierna cuatro dominios que no pertenecen a ninguna especificacion individual sino al ecosistema como un todo:

1. **Precedencia** — Que documento gobierna cuando dos se contradicen.
2. **Inyeccion a LLMs** — Como se entregan los artefactos KORA al contexto de un LLM.
3. **Extensiones** — Como un namespace extiende las reglas base sin romper compatibilidad.
4. **Cross-platform deployment** — Como los agentes KORA se despliegan en multiples runtimes preservando equivalencia comportamental.

Traces to: formal/05 §1.2 (Bounded Lattice theorem — gobernanza = top)

### 1.1 Alcance

Este documento aplica a todos los artefactos que siguen las especificaciones KORA/MD o KORA/Spec-MD. No aplica a artefactos externos al ecosistema KORA.

---

## 2. Definiciones

La tabla de esta seccion **DEBE** incluir todo termino clave con significado preciso dentro de este documento:

**Correcto:** `El documento usa "Precedencia" y "Wrapper"; ambos aparecen definidos en esta tabla.`
**Incorrecto:** `El documento usa "Runtime" como termino clave y no existe entrada para "Runtime".`

| Termino | Definicion |
| --- | --- |
| **Artefacto** | Archivo Markdown unitario con frontmatter KORA y cuerpo de contenido, gobernado por KORA/MD o KORA/Spec-MD |
| **Precedencia** | Orden jerarquico que determina que documento prevalece cuando dos contienen reglas contradictorias |
| **Extension** | Artefacto KORA/Spec-MD que agrega o restringe reglas dentro de un namespace sin contradecir las bases |
| **Wrapper** | Envoltorio generado dinamicamente que adapta un artefacto KORA al formato de un runtime sin alterar la fuente |
| **Inyeccion** | Acto de entregar un artefacto KORA al contexto de un LLM para su consumo |
| **Namespace** | Primer segmento logico de un URN; delimita el dominio al que pertenece el recurso (`gn`, `tde`, `kora`) |
| **Runtime** | Entorno de ejecucion de un LLM (OpenClaw, Claude, GPT, Gemini) que consume artefactos KORA |
| **Especificacion base** | Documento fundacional que define reglas para un tipo de artefacto (`md-spec.md`, `spec-md.md`) |
| **Meta-regla** | Regla de este documento que gobierna la interaccion entre especificaciones, no el contenido de una sola |
| **Koraficacion** | Proceso de transformar documentos humanos en artefactos KORA/MD. Definido en `md-spec.md` §6. Preserva toda informacion eliminando entropia comunicativa |
| **Agentificacion** | Proceso de construir o migrar agentes al formato workspace KORA. Definido en `agent-spec-md.md` §12. Opera en dos modos: construccion desde cero y transmutacion de legado |
| **Cristalizacion** | Proceso de convertir decisiones implicitas, practicas informales y restricciones en reglas explicitas con keywords RFC 2119. Definido en `spec-md.md` §1.2 |
| **Skill** | Unidad de capacidad cognitiva invocable bajo evaluacion diferida; puede ser degenerado (CM puro) o extendido (directorio con SKILL.md). Definido en [skill-spec-md](urn:kora:kb:skill-spec-md) |
| **Formal Layer** | Capa de conocimiento categorico-matematico (documentos 00-05 en `knowledge/kora/categorical-foundations/`) que provee justificacion formal a las reglas operacionales. Es conocimiento descriptivo gobernado por KORA/MD, no governance |
| **Traces to** | Convencion de trazabilidad definida en [spec-md](urn:kora:kb:spec-md) §1.3 que conecta una regla operacional con su justificacion en la Formal Layer. Una regla con traza tiene respaldo matematico; una regla sin traza es pragmatica |

---

## 3. Catalogo de Artefactos Fundacionales

El ecosistema KORA se sostiene sobre los siguientes documentos fundacionales:

| URN | Tipo | Gobierna |
| --- | --- | --- |
| `urn:kora:kb:md-spec` | Spec | Formato de artefactos de conocimiento descriptivo |
| `urn:kora:kb:spec-md` | Spec | Formato de documentos prescriptivos |
| `urn:kora:kb:agent-spec-md` | Spec | Arquitectura de agentes LLM |
| `urn:kora:kb:skill-spec-md` | Spec | Formato de Skills y relacion CM/Skill |
| `urn:kora:kb:runtime-spec-md` | Spec | Deployment cross-platform y equivalencia comportamental |
| `urn:kora:kb:swarm-spec-md` | Spec | Orquestacion multi-agente: swarms, golden paths, circuit breakers, backpressure |
| `urn:kora:kb:gobernanza` | Gobernanza | Precedencia, inyeccion, extensiones y cross-platform (este documento) |
| `urn:kora:kb:cat-foundations` | Knowledge | Capa formal categorica (6 documentos: 00-05). Conocimiento descriptivo, no governance |

---

## 4. Precedencia Inter-Documentos

### 4.1 Regla General

Cuando dos artefactos KORA contienen reglas que se contradicen, la resolucion sigue este orden de precedencia (mayor a menor):

1. **Este documento** (`urn:kora:kb:gobernanza`) — Prevalece sobre todo. Define las meta-reglas.
2. **Las especificaciones del tipo de artefacto** — `md-spec.md` para artefactos descriptivos, `spec-md.md` para prescriptivos. Cada una gobierna su dominio.
   - 2a. **`agent-spec-md.md`** — Especificacion que gobierna exclusivamente los workspaces de agentes (directorios `agents/`). Prevalece sobre las extensiones de namespace en todo lo que concierne a la arquitectura interna de un agente. No puede contradecir `md-spec.md` ni `spec-md.md`.
   - 2b. **`skill-spec-md.md`** — Especificacion que gobierna el formato y ciclo de vida de Skills (archivos CM-*.md y directorios de Skills extendidos). Prevalece sobre extensiones de namespace en todo lo que concierne a Skills. No puede contradecir `agent-spec-md.md`, `md-spec.md` ni `spec-md.md`.
   - 2c. **`runtime-spec-md.md`** — Especificacion que gobierna el deployment cross-platform de agentes KORA. Prevalece sobre extensiones de namespace en todo lo que concierne a adapters de plataforma y wrappers de inyeccion. No puede contradecir las capas superiores.
   - 2d. **`swarm-spec-md.md`** — Especificacion que gobierna la orquestacion multi-agente: swarms, golden paths, circuit breakers y backpressure. Prevalece sobre extensiones de namespace en todo lo que concierne a coordinacion de multiples agentes. No puede contradecir las capas superiores.
3. **Secciones operativas y guias derivadas** — Secciones de ejecucion dentro de las especificaciones y guias derivadas. No pueden contradecir las reglas declarativas de la misma especificacion.
4. **Extensiones de namespace** — Reglas especificas de un namespace. No pueden contradecir las capas superiores.

Traces to: formal/05 §1.2 (Bounded Lattice theorem)

### 4.2 Conflicto Entre Especificaciones

Si `md-spec.md` y `spec-md.md` contienen reglas mutuamente contradictorias sobre un mismo tema, cada una **DEBE** prevalecer sobre la otra exclusivamente dentro de su dominio:

- Para artefactos de conocimiento descriptivo -> prevalece `md-spec.md`.
- Para documentos prescriptivos -> prevalece `spec-md.md`.

Si el conflicto no puede resolverse por dominio (afecta a ambos tipos), este documento de gobernanza **DEBE** ser actualizado con una resolucion explicita.

Traces to: formal/05 §1.3 (Domain Disjointness theorem)

### 4.3 Regla de Silencio

Si una especificacion no dice nada sobre un tema, eso no significa permiso. El silencio **NO DEBE** interpretarse como autorizacion. Ante la duda, la opcion mas restrictiva compatible con el espiritu de la especificacion prevalece.

**Correcto:** `md-spec.md no menciona imagenes -> se interpretan como no permitidas (opcion restrictiva).`
**Incorrecto:** `md-spec.md no menciona imagenes -> se asume que estan permitidas por omision.`

Traces to: formal/05 §1.4 (Restrictive Default theorem)

### 4.4 Excepcion: Bootstrap URNs de Agentes

Los archivos de bootstrap de agentes (catalogados con `type: agent-bootstrap`) **PUEDEN** usar el formato extendido de cuatro segmentos:

```
urn:{namespace}:agent-bootstrap:{nombre}:{version}
```

Esta excepcion al formato tripartito estandar (`urn:{ns}:{type}:{id}`) es legitima porque:

- Los workspaces de agentes requieren versionado explicito para garantizar **equivalencia comportamental**: dos versiones del mismo agente pueden coexistir y ser comparadas.
- El segmento `{version}` no es metadata opcional; es parte del identificador estructural del workspace.

**Correcto:** `urn:gn:agent-bootstrap:goreologo-agents:2.4.0`
**Incorrecto:** `urn:gn:agent-bootstrap:goreologo-agents` (omite version)

Esta excepcion aplica **unicamente** a artefactos con `type: agent-bootstrap`. Todos los demas artefactos DEBEN usar el formato tripartito.

Traces to: formal/01 §5.2 (Substitutability theorem — bisimulation requires version-distinguishable identities)

### 4.5 La Formal Layer como Conocimiento

La capa formal categorica (`knowledge/kora/categorical-foundations/`, documentos 00-05) es **conocimiento descriptivo** gobernado por KORA/MD. **NO** es governance ni prescripcion. Su rol es:

1. Proveer justificacion matematica a reglas operacionales via la convencion `Traces to:`.
2. Servir como referencia de verificacion cuando se modifica una regla operacional que tiene traza formal.
3. Documentar la estructura categorica del ecosistema sin imponer obligaciones por si misma.

Las reglas operacionales residen en las specs (este documento, spec-md, md-spec, agent-spec-md, skill-spec-md, runtime-spec-md). La Formal Layer justifica pero **NO DEBE** gobernar directamente.

---

## 5. Inyeccion a LLMs

### 5.1 Principio General

Los artefactos KORA estan disenados para ser consumidos por LLMs, pero la forma en que se entregan al contexto del modelo depende del runtime. Este documento define patrones recomendados, no obligaciones de formato. Para detalles de deployment por plataforma, ver [runtime-spec-md](urn:kora:kb:runtime-spec-md).

### 5.2 Separacion Frontmatter / Cuerpo

El frontmatter YAML **DEBERIA** ser procesado por el orquestador (indexador, CLI, pipeline RAG) y no incluido en el texto que recibe el LLM. El frontmatter contiene metadata de maquina; el LLM consume el cuerpo.

**Correcto:** `El pipeline RAG parsea el frontmatter para indexacion y entrega solo el cuerpo Markdown al LLM.`
**Incorrecto:** `El pipeline inyecta el artefacto completo (frontmatter + cuerpo) en el contexto del LLM.`

### 5.3 Patrones de Inyeccion por Runtime

| Runtime | Patron Recomendado | Notas |
| --- | --- | --- |
| **OpenClaw** | Artefactos como Skills (`SKILL.md` wrapper) | Carga on-demand, no en bootstrap permanente |
| **Claude (Anthropic)** | XML tags para delimitar secciones | Claude fue entrenado con XML; `<rules>`, `<context>`, `<examples>` mejoran precision |
| **GPT (OpenAI)** | Markdown con headers claramente jerarquizados | Los modelos GPT responden bien a Markdown estructurado nativo |
| **Gemini (Google)** | Markdown nativo, prompts con estructura definida | Similar a GPT; sin preferencia declarada por delimitadores |
| **RAG generico** | Chunking por `##`, stripping de frontmatter | Estandar para cualquier pipeline de vectorizacion |

Para detalle completo de adaptacion por plataforma, ver [runtime-spec-md](urn:kora:kb:runtime-spec-md) §4-§7.

### 5.4 Wrappers Opcionales

Cuando un artefacto KORA se inyecta como skill en un runtime que soporta delimitadores, el wrapper **PUEDE** envolver el contenido con tags del runtime sin alterar el artefacto fuente:

```xml
<!-- Wrapper para Claude -->
<kora_spec>
[contenido del artefacto KORA sin frontmatter]
</kora_spec>
```

El artefacto fuente en disco permanece inalterado. El wrapper se genera dinamicamente en el momento de la inyeccion.

---

## 6. Extensiones por Namespace

### 6.1 Principio

Un namespace **PUEDE** definir reglas prescriptivas adicionales que aplican exclusivamente a los artefactos de ese namespace. Ninguna extension **DEBE** contradecir las especificaciones base (`md-spec.md`, `spec-md.md`).

### 6.2 Formato de Extension

Una extension de namespace se materializa como un artefacto KORA/Spec-MD con las siguientes restricciones:

- URN: `urn:{namespace}:kb:ext-{nombre}`
- **DEBE** referenciar explicitamente la especificacion base que extiende.
- **DEBE** declarar en §1 que es una extension, no un reemplazo.
- Solo **PUEDE** agregar reglas o restringir las existentes. No **PUEDE** relajarlas.

**Correcto:** Una extension que agrega un campo obligatorio al frontmatter para el namespace `gn`:

```yaml
# En urn:gn:kb:ext-frontmatter
# Extiende: urn:kora:kb:md-spec

# Ademas de los campos base, los artefactos gn DEBEN incluir:
region: "nuble"
```

**Incorrecto:** Una extension que permite headings de profundidad `#####` (viola `md-spec.md` §4.1).

### 6.3 Precedencia de Extensiones

Las extensiones aplican **solo dentro del namespace que las define**. Un artefacto `urn:gn:kb:marco-legal-gores` se valida contra:

1. `urn:kora:kb:md-spec` (base)
2. `urn:gn:kb:gestion-ipr` (extension del namespace gn, si existe)

Un artefacto `urn:tde:kb:guia-sistema-tde-2025` no esta sujeto a las extensiones de `gn`.

---

## 7. Validacion del Ecosistema

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| Sin contradicciones inter-spec | `md-spec.md` y `spec-md.md` no se contradicen | Resolucion en §4.2 de este documento |
| Extensiones compatibles | Ninguna extension relaja reglas base | Rechazar extension |
| Nombres de extension | URN sigue patron `urn:{ns}:kb:ext-{nombre}` | Renombrar |
| Wrappers no alteran fuente | El artefacto en disco esta inalterado | Revertir cambios al fuente |
| Frontmatter no inyectado | El texto que recibe el LLM no contiene YAML frontmatter | Verificar pipeline de inyeccion |
| Trazabilidad valida | Toda regla con `Traces to:` referencia un documento y seccion existentes en la Formal Layer | Corregir referencia o eliminar traza |
| Catalogo actualizado | Todo artefacto fundacional de §3 esta registrado en el catalogo | Ejecutar `scripts/kora index` |

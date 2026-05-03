---
_manifest:
  urn: urn:kora:kb:pipeline-ingesta
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: KORA pipeline design
version: 1.0.0
status: published
tags:
- pipeline
- ingesta
- intake
- funtor
- workflow
- cristalizacion
- koraficacion
lang: es
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:pipeline-ingesta
relations:
  cites:
  - urn:kora:kb:autoria-spec
  - urn:kora:kb:md-spec
  - urn:kora:kb:spec-md
---


# Pipeline de Ingesta — Infraestructura de Transformacion de Artefactos v1.0.0

## 1. Definicion

Este documento define la infraestructura operativa que soporta la ejecucion de los funtores F ([KORA/MD](urn:kora:kb:md-spec) §6, koraficacion) y G ([KORA/Spec-MD](urn:kora:kb:spec-md) §1.2, cristalizacion). El pipeline establece las 4 zonas fisicas del monorepo por las que transita un documento desde su llegada hasta su publicacion como artefacto KORA.

### 1.1 Alcance

Este pipeline **DEBE** aplicarse a todo documento externo que ingrese al monorepo KORA para ser transformado en un artefacto de conocimiento. Gobierna la trazabilidad, el ciclo de vida y la organizacion fisica de los archivos durante la transformacion.

**NO DEBE** aplicarse a agentes (gobernados por [autoria-spec](urn:kora:kb:autoria-spec) §12), specs fundacionales (residen en `specs/`), ni skills (residen en `skills/`).

**Correcto:** `Usar este pipeline para transformar un PDF de normativa en un artefacto KORA/MD publicado.`
**Incorrecto:** `Usar este pipeline para crear un nuevo agente KORA (ver autoria-spec §12).`

---

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| **Pipeline de ingesta** | Secuencia de 4 zonas fisicas (inbox → source → drafts → knowledge) que gobierna el flujo de documentos hacia artefactos publicados |
| **Zona** | Directorio de nivel superior en el monorepo con semantica y reglas especificas |
| **Objeto crudo** | Archivo recien llegado sin procesamiento: PDF, libro, dataset, documento externo |
| **Extracto curado** | Contenido extraido de un objeto crudo, listo para transformacion via funtor F o G |
| **Artefacto WIP** | Artefacto en proceso de transformacion con frontmatter KORA y `status: draft` |
| **Artefacto publicado** | Artefacto verificado con frontmatter KORA y `status: published`, registrado en catalogo |
| **Funtor F** | Transformacion `DocHumano → KORA/MD` definida en [KORA/MD](urn:kora:kb:md-spec) §6 (koraficacion, descriptivo) |
| **Funtor G** | Transformacion `{Decisiones ∪ Practicas ∪ Restricciones} → KORA/Spec-MD` definida en [KORA/Spec-MD](urn:kora:kb:spec-md) §1.2 (cristalizacion, prescriptivo) |
| **Manifiesto** | Bloque YAML frontmatter con `_manifest`, `version`, `status`, `tags`, `lang` |
| **Provenance** | Campo `_manifest.provenance.source` que traza el artefacto a su archivo en ` |

---

## 3. Topologia del Pipeline

```
inbox/ → source/ → drafts/ → knowledge/
(aterrizaje) (dominio F|G) (en proceso) (publicado)
```

### 3.1 Zona 1: `inbox/`

Zona de aterrizaje para objetos crudos. **NO DEBE** contener metadata KORA. **NO DEBE** organizarse por namespace — los objetos aun no tienen destino definido.

| Propiedad | Valor |
| --- | --- |
| Contenido permitido | Cualquier archivo: PDF, DOCX, HTML, CSV, TXT, MD sin frontmatter |
| Metadata KORA | Prohibida |
| Organizacion | Plana (sin subdirectorios por namespace) |
| Indexado por catalogo | No — excluido de `kora index` |
| Ciclo de vida | Temporal — los objetos se procesan y eliminan o archivan |

**Correcto:** `Depositar un PDF de 300 paginas en inbox/ para procesamiento posterior.`
**Incorrecto:** `Depositar un artefacto con frontmatter KORA en inbox/ (debe ir a drafts/).`

### 3.2 Zona 2: `

Extractos curados listos para transformacion. Organizados por namespace destino, espejando ` **NO DEBE** contener metadata KORA.

| Propiedad | Valor |
| --- | --- |
| Contenido permitido | Markdown curado, texto plano extraido de objetos crudos |
| Metadata KORA | Prohibida |
| Organizacion | Por namespace: ` espejando ` |
| Indexado por catalogo | No — excluido de `kora index` |
| Ciclo de vida | Permanente — sirve como fuente de verdad para trazabilidad |

**Correcto:** `Extraer un capitulo de un libro PDF (inbox/) y colocarlo como .md en 
**Incorrecto:** `Colocar un PDF completo sin procesar en source/ (debe ir a inbox/).`

Un documento **PUEDE** saltar `inbox/` e ir directo a ` si ya es un extracto curado (markdown listo para transformacion).

### 3.3 Zona 3: `

Artefactos en proceso de transformacion. **DEBE** contener frontmatter KORA con `status: draft`. Organizado por namespace, espejando `

| Propiedad | Valor |
| --- | --- |
| Contenido permitido | Artefactos KORA/MD o KORA/Spec-MD con frontmatter |
| Metadata KORA | Obligatoria (`status: draft`) |
| Organizacion | Por namespace: ` espejando ` |
| Indexado por catalogo | No — excluido de `kora index` |
| Ciclo de vida | Temporal — los artefactos se iteran hasta pasar verificacion, luego se promueven a ` |

El campo `_manifest.provenance.source` **DEBE** apuntar al archivo correspondiente en `, cerrando la cadena de trazabilidad.

**Correcto:** ` con status: draft y provenance.source: 
**Incorrecto:** ` sin frontmatter (es source/, no draft).`

### 3.4 Zona 4: `

Artefactos publicados y verificados. **DEBE** contener frontmatter KORA con `status: published`. Registrados en el catalogo via `kora index`.

| Propiedad | Valor |
| --- | --- |
| Contenido permitido | Artefactos KORA/MD o KORA/Spec-MD verificados |
| Metadata KORA | Obligatoria (`status: published`) |
| Organizacion | Por namespace: ` |
| Indexado por catalogo | Si — unica zona que alimenta el catalogo |
| Ciclo de vida | Permanente — artefactos publicados, versionados via SemVer |

**Correcto:** ` con status: published, URN registrada en catalogo.`
**Incorrecto:** ` con status: draft (debe estar en drafts/).`

---

## 4. Ciclo de Vida del Artefacto

### 4.1 Estados

Todo artefacto en el pipeline **DEBE** encontrarse en exactamente uno de los siguientes estados:

| Estado | Zona fisica | Manifiesto | Indexado |
| --- | --- | --- | --- |
| `PENDING` | ` (sin correspondencia en drafts/ ni knowledge/) | No | No |
| `PROCESSING` | ` con `status: draft` | Si | No |
| `PUBLISHED` | ` con `status: published` | Si | Si |
| `ORPHAN` | Catalogo apunta a ` inexistente | Si | Si (invalido) |

### 4.2 Transiciones

```
PENDING → PROCESSING Crear artefacto en drafts/ con frontmatter (status: draft)
PROCESSING → PROCESSING Iterar cristalizacion/koraficacion en drafts/
PROCESSING → PUBLISHED Mover artefacto a knowledge/, cambiar status: draft → published, ejecutar kora index
PUBLISHED → ORPHAN Si se elimina el source sin actualizar provenance (estado invalido)
```

Un artefacto **NO DEBE** transitar de `PENDING` a `PUBLISHED` sin pasar por `PROCESSING`. La zona ` es obligatoria para toda transformacion.

**Correcto:** `source → drafts (cristalizar, verificar, iterar) → knowledge (publicar).`
**Incorrecto:** `source → knowledge (publicar sin verificacion en drafts/).`

---

## 5. Seleccion de Funtor

El tipo de documento fuente determina el funtor de transformacion:

| Naturaleza del documento | Funtor | Formato destino | Spec gobernante |
| --- | --- | --- | --- |
| Descriptivo (hechos, datos, procedimientos) | F (koraficacion) | KORA/MD | [md-spec](urn:kora:kb:md-spec) §6 |
| Prescriptivo (reglas, restricciones, obligaciones) | G (cristalizacion) | KORA/Spec-MD | [spec-md](urn:kora:kb:spec-md) §1.2 |

La seleccion **DEBE** realizarse antes de iniciar la transformacion. Un documento **NO DEBE** transformarse con el funtor incorrecto.

**Correcto:** `Documento con keywords RFC 2119 y reglas → Funtor G → KORA/Spec-MD.`
**Incorrecto:** `Documento prescriptivo con reglas → Funtor F → KORA/MD (elimina prosa normativa necesaria).`

---

## 6. Trazabilidad

### 6.1 Cadena de Provenance

Todo artefacto publicado **DEBE** mantener una cadena de trazabilidad completa:

```

 └─ _manifest.provenance.source → 
 └─ (si aplica) objeto crudo original en inbox/ (ya removido o archivado)
```

El campo `provenance.source` **DEBE** ser una ruta relativa desde la raiz del monorepo.

**Correcto:** `source: "
**Incorrecto:** `source: "~/Downloads/files/chapter0-operador-solitario.md"`

### 6.2 Permanencia de Sources

Los archivos en ` **NO DEBEN** eliminarse tras la publicacion del artefacto. Sirven como fuente de verdad para auditorias de fidelidad y re-transformaciones.

---

## 7. Monitoreo: `kora intake`

El subcomando `kora intake` **DEBE** reportar el estado de cada archivo en ` cruzando con ` y `

```bash
python3 toolchain/kora intake
```

Output esperado:

```
=== KORA Intake Status ===

 [PUBLISHED] → (urn:fxsl:kb:file)
 [PROCESSING] → 
 [PENDING] 
 [ORPHAN] → (source missing)

Summary: 1 published, 1 processing, 1 pending, 1 orphan(s)
```

---

## 8. Exclusion del Catalogo

Las zonas `inbox/`, ` y ` **DEBEN** estar excluidas del indexado de `kora index`. Solo ` alimenta el catalogo. Los artefactos en ` con `status: draft` **NO DEBEN** ser resolvibles via `kora resolve`.

La razon es que los drafts son trabajo en curso y sus URNs podrian colisionar con versiones publicadas o contener errores no verificados.

**Correcto:**
```
kora resolve "urn:{ns}:kb:{id}" → 
```

**Incorrecto:**
```
kora resolve devuelve un draft en drafts/ (no verificado, no debe ser resolvible)
```

---

## 9. Invariantes

### 9.1 Segregacion de Zonas

Cada zona **DEBE** contener exclusivamente el tipo de contenido definido en [-> 3. Topologia del Pipeline]. Mezclar contenido entre zonas viola la integridad del pipeline.

### 9.2 Unicidad de Provenance

Cada artefacto publicado **DEBE** tener exactamente un `provenance.source`. Dos artefactos distintos **PUEDEN** apuntar al mismo source (si un source genera multiples artefactos).

### 9.3 Espejado de Namespace

La estructura de directorios en ` y ` **DEBE** espejar la de ` El namespace y subdirectorio de un archivo **NO DEBE** cambiar entre zonas.

**Correcto:** ` → → 
**Incorrecto:** ` → (namespace cambio de fxsl a gn).`

---

## 10. Validacion

| Check | Criterio | Accion si falla |
| --- | --- | --- |
| Zonas excluidas | `inbox/`, `, ` no aparecen en catalogo | Verificar exclusion en `toolchain/kora` |
| Provenance valida | Todo artefacto publicado tiene `provenance.source` que resuelve a un archivo existente en ` | Corregir provenance o restaurar source |
| Status coherente | Artefactos en ` tienen `status: draft`; en ` tienen `status: published` | Corregir status |
| Espejado de namespace | Ruta relativa post-zona es identica entre source/, drafts/ y knowledge/ | Reorganizar directorios |
| Sin orphans | `kora intake` reporta 0 orphans | Restaurar source o actualizar provenance |
| Funtor correcto | Documentos descriptivos usan F, prescriptivos usan G | Re-transformar con funtor correcto |

---
_manifest:
  urn: "urn:kora:kb:wf-koraficacion"
  provenance:
    created_by: "FS"
    created_at: "2026-02-22"
    source: "KORA/MD Spec v1.0 — Estrategia de Ejecución"
version: 1.0.0
status: published
tags: [workflow, koraficacion, llm, transformacion, fidelidad]
lang: es
---

# Workflow de Koraficación

## Propósito

Estrategia de ejecución para transformar documentos humanos a KORA/MD con máxima fidelidad. Mitiga las limitaciones probabilísticas de los LLMs mediante segmentación, separación de concerns y verificación mecánica.

## Premisa

La especificación KORA/MD (urn:kora:kb:md-spec) define el QUÉ (propiedades del funtor). Este workflow define el CÓMO (estrategia de ejecución que maximiza la probabilidad de cumplir esas propiedades).

---

## Paso 1: Evaluación del Input

Antes de transformar, clasificar el documento fuente:

| Criterio             | Valor                                | Implicación                                                  |
| -------------------- | ------------------------------------ | ------------------------------------------------------------ |
| Largo del documento  | <5K tokens                           | Koraficación directa (un solo paso)                          |
| Largo del documento  | 5K-15K tokens                        | Koraficación segmentada (por secciones naturales)            |
| Largo del documento  | >15K tokens                          | Koraficación segmentada + validación adversarial obligatoria |
| Estructura existente | Tiene headings claros                | Segmentar por headings del original                          |
| Estructura existente | Prosa monolítica sin headings        | Segmentar por párrafos temáticos (~1-2K tokens/segmento)     |
| Contenido numérico   | Alto (tablas, cifras, leyes, plazos) | Verificación mecánica de fidelidad obligatoria               |
| Contenido numérico   | Bajo (prosa conceptual)              | Verificación mecánica opcional                               |

---

## Paso 2: Segmentación (si aplica)

Para documentos >5K tokens:

1. Identificar los puntos de corte naturales del documento (títulos, capítulos, secciones).
2. Cada segmento debe ser temáticamente coherente y caber dentro de ~3-5K tokens.
3. Numerar los segmentos para trazabilidad: `[Seg-1]`, `[Seg-2]`, ... `[Seg-N]`.

**Regla:** Nunca cortar dentro de una tabla, lista, o párrafo. Siempre cortar entre secciones.

---

## Paso 3: Telegrafización Fiel (Primer Paso LLM)

Para cada segmento (o el documento completo si es <5K):

**Instrucción al LLM:**

```
Transforma el siguiente documento a formato KORA/MD aplicando estas reglas:
- Telegrafizar: comprimir toda prosa a su forma mínima sin perder información.
- Preservar: toda cifra, fecha, plazo, excepción, condición y referencia legal.
- Preservar idioma: el output debe estar en el mismo idioma del input.
- Preservar estructuras: toda lista conserva todos sus ítems. Toda tabla conserva todas sus filas y columnas.
- Promover: convertir prosa comparativa/condicional a tablas o listas.
- NO reorganizar la estructura de secciones. Mantener el orden del original.
- Usar headings telegráficos (sintagmas nominales, no oraciones).
- Prohibido: introducciones, transiciones, hedging, saludos, retórica.

Documento fuente:
[contenido del segmento]
```

**Output:** Segmento koraficado con estructura fiel al original.

---

## Paso 4: Ensamblaje

Si fue segmentado:

1. Concatenar los segmentos koraficados en orden.
2. Agregar el `#` (H1) como título unificado del artefacto.
3. Agregar separadores `---` entre secciones `##`.

---

## Paso 5: Normalización (Segundo Paso LLM — Opcional)

Aplicar solo si el documento original tiene redundancia evidente o estructura subóptima.

**Instrucción al LLM:**

```
El siguiente es un artefacto KORA/MD ya telegrafizado. Tu tarea es ÚNICAMENTE reorganizar la estructura de encabezados para optimizarla:
- Fusionar secciones que tratan el mismo tema.
- Dividir secciones excesivamente largas.
- Eliminar información duplicada (conservar la instancia más completa).
- NO modificar el texto de las celdas, ítems de lista ni definiciones.
- NO agregar ni eliminar información factual.

Artefacto:
[contenido ensamblado]
```

**Output:** Artefacto normalizado.

---

## Paso 6: Inyección de Frontmatter

Agregar el bloque YAML frontmatter al inicio:

```yaml
---
_manifest:
  urn: "urn:{namespace}:kb:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencia del documento original}"
version: 1.0.0
status: draft
tags: [{tag1}, {tag2}, {tag3}]
lang: {código ISO 639-1 del contenido}
---
```

---

## Paso 7: Verificación Mecánica

Checks determinísticos (no dependen de LLM):

| Check                    | Método                                                           | Criterio de falla                     |
| ------------------------ | ---------------------------------------------------------------- | ------------------------------------- |
| Conteo de ítems de lista | `grep -c "^- " source` vs `grep -c "^- " output`                 | Diferencia > 0                        |
| Conteo de filas de tabla | `grep -c "^\|" source` vs `grep -c "^\|" output`                 | output < source (descontando headers) |
| Cifras preservadas       | Extraer `\d+[\.,]?\d*` del source, verificar presencia en output | Cifra ausente                         |
| Fechas preservadas       | Extraer patrones de fecha del source, verificar en output        | Fecha ausente                         |
| Frontmatter válido       | Parsear YAML entre `---` delimitadores                           | Error de parseo                       |
| URN sin versión          | Buscar `urn:.*:.*:.*:` (4+ segmentos) en cuerpo                  | Match encontrado                      |
| Lang coherente           | Campo `lang` vs idioma detectado del contenido                   | Divergencia                           |

---

## Paso 8: Verificación Adversarial (si aplica)

Para documentos >15K tokens o con alto contenido numérico:

**Instrucción al LLM verificador (distinto al transformador):**

```
Compara el documento original con el artefacto KORA/MD generado.
Identifica TODA información presente en el original que NO esté representada en el output.
Lista cada omisión como:
- [LÍNEA/SECCIÓN del original]: [información faltante]

Si no hay omisiones, responde: "FIDELIDAD: COMPLETA"

Original:
[documento fuente]

KORA/MD generado:
[artefacto]
```

Si se detectan omisiones → volver al Paso 3 para los segmentos afectados.

---

## Paso 9: Registro en Catálogo

1. Ejecutar `kora index` para registrar el URN en el catálogo.
2. Cambiar `status: draft` a `status: published` una vez verificado.
3. Commit al monorepo.

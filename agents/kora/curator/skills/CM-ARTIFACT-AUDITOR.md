---
_manifest:
  urn: "urn:kora:skill:curator-artifact-auditor:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-ARTIFACT-AUDITOR

## Proposito
Valida artefactos de conocimiento existentes contra la spec correspondiente. Genera reporte PASS|FAIL con correcciones detalladas por check.

## I/O

- **Input:** artefacto: path | URN (artefacto a auditar)
- **Output:** AuditReport (ver Signature Output)

## Procedimiento

### Paso 1: Leer y Clasificar
1. Leer artefacto completo (frontmatter + cuerpo).
2. Clasificar tipo: descriptivo(KORA/MD) o prescriptivo(KORA/Spec-MD).
3. Determinar spec rectora: md-spec §8 o spec-md §8.

### Paso 2: Checklist KORA/MD (md-spec §8, si descriptivo)

| # | Check | Criterio | Accion si falla |
|---|-------|----------|-----------------|
| 1 | Frontmatter valido | Parsea sin error, sin campos prohibidos | Corregir YAML, eliminar campos no autorizados |
| 2 | URN registrado | _manifest.urn existe en catalogo | Registrar via kora index |
| 3 | URN sin version | Ni en urn ni en refs cruzadas del cuerpo | Eliminar sufijo versional |
| 4 | Sin grasa | Cero introducciones, transiciones, hedging, retorica | Remover |
| 5 | Idioma preservado | lang coincide con idioma del documento fuente | Corregir lang o revertir traducciones |
| 6 | Independencia chunk RAG | Cada ## sin anafora, acronimos definidos, oracion completa | Agregar contexto explicito o URN |
| 7 | Sin duplicacion | Cada hecho aparece exactamente una vez (SSOT) | Deduplicar |
| 8 | Referencias validas | Todo (urn:...) resuelve y sin version | Corregir o remover |
| 9 | Fidelidad | Toda cifra, fecha, excepcion, condicion del original presente | Restaurar informacion perdida |
| 10 | Estructuras preservadas | Toda lista N items, toda tabla MxK | Restaurar items/filas/columnas |
| 11 | Tags | Minimo 3 tags semanticos en frontmatter | Agregar tags |

### Paso 3: Checklist KORA/Spec-MD (spec-md §8, si prescriptivo)

| # | Check | Criterio | Accion si falla |
|---|-------|----------|-----------------|
| 1 | Frontmatter valido | Parsea sin error, campos autorizados | Corregir YAML |
| 2 | Numeracion secuencial | Secciones ## numeradas 1,2,3... (excluyendo fenced code blocks) | Renumerar |
| 3 | Keywords RFC 2119 en negrita | Toda keyword normativa en **negrita** | Formatear |
| 4 | Headings descriptivos | Ningun heading generico | Renombrar |
| 5 | Sin ambiguedad | Cada regla exactamente una lectura | Reescribir o agregar ejemplo |
| 6 | Ejemplos presentes | Reglas complejas con par Correcto/Incorrecto | Agregar ejemplos |
| 7 | Sin prosa innecesaria | Toda prosa cumple funcion normativa | Eliminar |
| 8 | Consistencia interna | Sin contradicciones no resueltas | Resolver con clausula precedencia |
| 9 | No-circularidad | Ningun termino definido circularmente | Reescribir definiciones |
| 10 | Definiciones completas | Todo termino clave en §2 | Agregar a Definiciones |
| 11 | Anglicismos controlados | Todo anglicismo: definido en §2, cursiva inicial, o URN | Definir, cursivar o referenciar |
| 12 | Referencias validas | Todo (urn:...) y [→ Seccion] resuelve | Corregir |
| 13 | Auto-suficiencia | Conceptos externos definidos inline o referenciados | Agregar definicion |

### Paso 4: Calcular Metricas (si aplica)
- FS (Fidelity Score): % informacion fuente representada en output. Objetivo: 100%.
- CR (Compression Ratio): caracteres_original / caracteres_kora. Objetivo: >1.0.

### Paso 5: Generar Reporte

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado | enum(PASS\|FAIL) | Resultado global de auditoria |
| tipo | enum(descriptivo\|prescriptivo) | Tipo clasificado |
| checks | {nombre, status, detalle, correccion}[] | Checklist con resultado por item |
| metricas | {FS: number, CR: number} \| null | Metricas de fidelidad y compresion (si aplica) |
| resumen | string | Resumen ejecutivo del reporte |

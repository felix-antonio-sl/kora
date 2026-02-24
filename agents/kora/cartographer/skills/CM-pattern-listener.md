---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-pattern-listener:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Detectar patrones emergentes en las fuentes de datos: campos repetidos, convenciones de nombrado, relaciones implicitas, vocabulario recurrente.

## Input/Output

- **Input:** Fuentes inventariadas desde S-ESCUCHAR
- **Output:** Lista de patrones emergentes con frecuencia y ejemplos

## Procedimiento

1. Escuchar por campos que aparecen en >50% de archivos
2. Detectar convenciones de nombrado (prefijos, sufijos, case styles)
3. Identificar relaciones implicitas (FKs, referencias cruzadas, IDs compartidos)
4. Anotar vocabulario repetido (estado, etapa, tipo, categoria, codigo, nombre)
5. Detectar estructuras JSON/YAML recurrentes (nesting patterns, array patterns)
6. NO imponer estructura todavia — solo observar y anotar
7. Clasificar patrones por frecuencia y relevancia

## Signature Output

```
**Patrones Emergentes**:
| # | Patron | Tipo | Frecuencia | Ejemplos |
|---|--------|------|------------|----------|
| 1 | [desc] | [campo/nombre/relacion/vocab/estructura] | [N fuentes] | [ejemplos] |
```

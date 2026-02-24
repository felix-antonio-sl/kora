---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-inventory-builder:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Construir inventario completo de fuentes de datos sin filtrar ni juzgar, como base para la fase ESCUCHAR.

## Input/Output

- **Input:** Lista de archivos, documentos, conversaciones proporcionados por usuario desde S-ESCUCHAR
- **Output:** Inventario estructurado por tipo con formato, tamano aproximado, autor si conocido

## Procedimiento

1. Listar TODAS las fuentes sin discriminar
2. Anotar formato de cada fuente (YAML, TTL, MD, SQL, JSON, CSV, conversacion)
3. Anotar tamano aproximado (lineas, paginas, registros)
4. Anotar autor si conocido
5. Agrupar por tipo: docs, schemas, datos, codigo
6. NO FILTRAR todavia — inventario completo es el objetivo
7. Detectar fuentes que podrian contener documento de autoridad (mision, vision, principios)
8. Presentar inventario estructurado

## Signature Output

```
**Inventario de Fuentes**:
| # | Fuente | Formato | Tamano aprox | Tipo | Notas |
|---|--------|---------|--------------|------|-------|
| 1 | [nombre] | [fmt] | [size] | [doc/schema/data/code] | [autor, etc.] |
**Total**: [N] fuentes en [M] tipos
```

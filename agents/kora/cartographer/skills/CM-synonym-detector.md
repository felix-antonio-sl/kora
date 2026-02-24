---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-synonym-detector:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Detectar nombres diferentes que representan el mismo concepto y normalizar a nombre canonico unico.

## Input/Output

- **Input:** Elementos de multiples fuentes (YAML, TTL, SQL) desde S-MAPEAR
- **Output:** Tabla de equivalencias con nombre canonico elegido

## Procedimiento

1. Comparar nombres entre fuentes (YAML vs TTL vs SQL vs MD)
2. Buscar prefijos/namespaces diferentes para mismo concepto
3. Comparar definiciones semanticas aunque nombres difieran
4. Heuristicas: mismo tipo + misma cardinalidad + mismo contexto = probable sinonimo
5. Para cada grupo de sinonimos: elegir nombre canonico segun:
   - Preferir nombre mas descriptivo
   - Preferir convencion del dominio
   - Preferir snake_case para bases de datos
6. Documentar decision de normalizacion

## Signature Output

```
**Tabla de Equivalencias**:
| Nombre Canonico | Sinonimos | Fuentes | Razon |
|----------------|-----------|---------|-------|
| [canonico] | [sin1, sin2, ...] | [fuente1, fuente2] | [razon eleccion] |
```

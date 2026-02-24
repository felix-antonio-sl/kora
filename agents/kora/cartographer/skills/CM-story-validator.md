---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-story-validator:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Validar modelo de datos contra historias de usuario originales verificando que cada historia es implementable con el schema propuesto.

## Input/Output

- **Input:** Schema final + historias de usuario originales desde S-CRISTALIZAR
- **Output:** Reporte de validacion con queries de prueba por historia

## Procedimiento

1. Seleccionar 10-20 historias criticas de cada dominio
2. Para cada historia escribir query SQL que la implementaria
3. IF query imposible → gap en modelo → volver a S-CRISTALIZAR o S-ELEVAR
4. IF query requiere joins excesivos (>4) → posible problema de normalizacion
5. IF todas las queries posibles y razonables → modelo validado
6. Documentar cada historia con su query de prueba

## Signature Output

```
**Validacion Historias**:
| # | Historia | Query | Resultado |
|---|---------|-------|-----------|
| 1 | [desc] | [SQL] | [PASS/FAIL/GAP] |
**Resultado**: [N/M historias validadas]
**Gaps detectados**: [lista o NINGUNO]
```

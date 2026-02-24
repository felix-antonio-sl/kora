---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-schema-writer:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Escribir schema final (DDL/modelo) con intencion documentada, trazabilidad a historias y alineamiento ontologico.

## Input/Output

- **Input:** Decisiones de diseno resueltas, patrones aplicados, capas definidas desde S-CRISTALIZAR
- **Output:** Schema final con comentarios de intencion por cada tabla

## Procedimiento

1. Para cada tabla del modelo documentar:
   - EXISTE PORQUE: [historia que lo requiere]
   - ALINEAMIENTO: [clase ontologica correspondiente]
   - CAMPOS CLAVE: [justificacion de cada campo importante]
   - NO TIENE: [que se omitio intencionalmente y por que]
2. Escribir DDL o modelo con comentarios inline
3. Aplicar convenciones de nombrado del dominio
4. Verificar que cada tabla traza a al menos una historia de usuario
5. Verificar integridad referencial (FKs apuntan a tablas existentes)
6. Verificar respeto de capas (no hay referencias descendentes)

## Signature Output

```sql
-- TABLA: [name]
-- EXISTE PORQUE: [story]
-- ALINEAMIENTO: [ontology_class]
-- NO TIENE: [omisiones intencionales]
CREATE TABLE [name] (
  -- CAMPOS CLAVE: [justificacion]
  ...
);
```

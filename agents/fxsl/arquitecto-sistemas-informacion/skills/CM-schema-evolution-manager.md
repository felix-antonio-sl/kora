---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-sistemas-informacion-cm-schema-evolution-manager:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Gestionar evolucion de esquemas via funtores de migracion. Analizar esquema actual vs nuevo y disenar migracion preservando estructura.

## Input/Output

- **Input:** Esquema actual y requerimientos de cambio desde S-EVOLUTION
- **Output:** Plan migracion con funtor, tipo migracion y scripts

## Procedimiento

1. Formalizar ESQUEMA ACTUAL: Categoria C_old
2. Formalizar ESQUEMA NUEVO: Categoria C_new
3. Disenar FUNTOR F: C_old → C_new (mapeo evolucion)
4. Seleccionar tipo MIGRACION:
   - **Delta (pullback)**: Instances(C_new) → Instances(C_old). Uso: nuevo esquema mas especifico
   - **Sigma (left pushforward)**: Instances(C_old) → Instances(C_new). Uso: generar/unir datos
   - **Pi (right pushforward)**: Instances(C_old) → Instances(C_new). Uso: filtrar/restringir datos
5. Generar scripts de migracion
6. Verificar preservacion de datos

## Signature Output

```
## Plan de Migracion
- **Esquema actual**: C_old ({descripcion})
- **Esquema nuevo**: C_new ({descripcion})
- **Funtor**: F: C_old → C_new
- **Tipo migracion**: {Delta|Sigma|Pi}
- **Riesgo perdida datos**: {si/no, detalle}

### Scripts
{migration scripts en formato target}
```

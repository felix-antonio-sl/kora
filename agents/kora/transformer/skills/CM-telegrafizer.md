---
_manifest:
  urn: "urn:kora:agent-bootstrap:transformer-cm-telegrafizer:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Transformar documento analizado eliminando fat y aplicando keyword markup telegrafizado para generar artefacto KODA denso.

## Input/Output

- **Input:** Documento con analisis meat/fat completado desde S-TELEGRAFIZER
- **Output:** Artefacto KODA preliminar con keyword markup aplicado, fat eliminado, 100% meat preservado

## Procedimiento

1. Eliminar todo fat identificado en fase de analisis
2. Convertir prosa a keyword markup:
   - Tier 1 (obligatorio): ID, Ref, Def, Act, Cond, Res, Req, Ctx, Ex, Purp, Mssn, Obj, Proc, Src, Prohib, Warn, Just, Rec
   - Tier 2 (dominio): terminos especificos del dominio en Snake_Case
3. Aplicar telegrafizacion: oraciones densas sin filler
4. Preservar 100% del meat — verificar que ningun hecho, dato, requisito o definicion se pierda
5. Mantener skeleton: jerarquia, tablas, listas del documento original
6. Generar artefacto KODA preliminar en formato YAML

## Signature Output

```yaml
# Artefacto KODA preliminar
# [metadata block]
# [contenido telegrafizado con keyword markup]
```

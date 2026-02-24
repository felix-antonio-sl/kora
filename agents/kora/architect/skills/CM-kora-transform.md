---
_manifest:
  urn: "urn:kora:agent-bootstrap:architect-cm-kora-transform:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Ejecutar las 4 fases de transformacion de documentos a formato KORA/Spec-MD con metricas de calidad FS=100% y CR>1.0.

## Input/Output

- **Input:** Documento fuente (texto, PDF, markdown) desde S-TRANSFORMER
- **Output:** Artefacto KORA validado con metricas FS (Fidelity Score) y CR (Compression Ratio)

## Procedimiento

1. **P1 — Analisis (meat/fat/structure):**
   - Escanear documento identificando secciones
   - Marcar MEAT: hechos, datos, requisitos, definiciones, ejemplos
   - Marcar FAT: filler words, retorica, frases redundantes
   - Marcar SKELETON: jerarquia, tablas, listas, relaciones
2. **P2 — Telegrafizacion + keywords:**
   - Eliminar todo fat identificado
   - Convertir prosa a keyword markup (Tier 1 + Tier 2)
   - Aplicar telegrafizacion: oraciones densas sin filler
   - Preservar 100% del meat
3. **P3 — Deduplicacion + Ref:**
   - Escanear artefacto buscando conceptos repetidos
   - Para cada repeticion: crear definicion con ID unico
   - Reemplazar todas las ocurrencias con Ref: ID
   - Regla intensiva: Si concepto aparece mas de una vez, DEBE ser definido y referenciado
4. **P4 — Validacion YAML:**
   - YAML valido (parseable sin errores)
   - Metadata block completo
   - Keywords del lexicon oficial
   - IDs unicos, Referencias validas
   - Calcular metricas: FS=100%, CR>1.0

## Signature Output

```
**Transformacion completada**
- Secciones: [N]
- Meat/Fat: [X%/Y%]
- FS: [100%]
- CR: [valor]
- Artefacto: [bloque YAML]
```

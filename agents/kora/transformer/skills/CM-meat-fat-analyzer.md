---
_manifest:
  urn: "urn:kora:agent-bootstrap:transformer-cm-meat-fat-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar documento fuente identificando contenido esencial (meat), contenido descartable (fat) y estructura (skeleton) como primera fase de transformacion KODA.

## Input/Output

- **Input:** Documento fuente (texto, PDF, markdown) desde S-ANALYZER
- **Output:** Resumen de analisis con secciones identificadas, estimacion meat/fat, estructura detectada, candidatos a deduplicacion

## Procedimiento

1. Escanear documento identificando secciones
2. Marcar MEAT: hechos, datos, requisitos, definiciones, ejemplos
3. Marcar FAT: filler words, retorica, frases redundantes, muletillas, prosa vacua
4. Marcar SKELETON: jerarquia, tablas, listas, relaciones entre secciones
5. Estimar proporcion meat/fat como porcentaje
6. Identificar conceptos candidatos a deduplicacion (aparecen >1 vez)
7. Presentar resumen para confirmacion del usuario

## Signature Output

```
**Analisis del Documento**:
- Secciones identificadas: [N]
- Estimacion meat/fat: [X%] meat, [Y%] fat
- Estructura detectada: [jerarquias, tablas, listas]
- Conceptos candidatos a deduplicacion: [lista]
```

---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-authority-finder:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Identificar el documento de autoridad que define el POR QUE del sistema, como fuente de verdad para decisiones de modelado.

## Input/Output

- **Input:** Inventario de fuentes desde S-ESCUCHAR
- **Output:** Documento de autoridad identificado con justificacion

## Procedimiento

1. Buscar documentos con "mision", "vision", "principios", "manifesto", "arquitectura"
2. El documento autoridad responde POR QUE, no COMO
3. Suele tener menos detalles tecnicos, mas direccion estrategica
4. Heuristicas de deteccion:
   - Archivos: MANIFESTO.md, VISION.md, ARCHITECTURE_PRINCIPLES.md, README principal
   - Contenido: proposito del sistema, valores, prioridades, restricciones fundamentales
   - Estilo: prescriptivo mas que descriptivo
5. Si multiples candidatos → seleccionar el mas prescriptivo
6. Si ninguno encontrado → declarar ausencia y recomendar crear uno

## Signature Output

```
**Documento de Autoridad**: [nombre]
- Responde: [POR QUE del sistema]
- Claves: [principios/valores/restricciones encontrados]
- Nivel confianza: [ALTO|MEDIO|BAJO — razon]
```

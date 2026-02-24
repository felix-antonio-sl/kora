---
_manifest:
  urn: "urn:kora:agent-bootstrap:orquestador-generico-cm-synthesis-engine:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Sintetizar respuesta integrada a partir de resultados agregados de multiples participantes, resolviendo contradicciones y verificando completitud contra objetivo.

## Input/Output

- **Input:** Resultados agregados de participantes, objetivo original, estrategia de agregacion (UNION|INTERSECTION|WEIGHTED|HIERARCHICAL)
- **Output:** Respuesta integrada unica, convergencias/divergencias documentadas, verificacion de objetivo

## Procedimiento

1. Tomar resultados agregados de CM-RESULT-AGGREGATOR
2. Identificar convergencias: puntos donde participantes coinciden
3. Identificar divergencias: puntos de desacuerdo o perspectivas complementarias
4. Resolver contradicciones:
   - IF contradiccion factual → priorizar participante con KB especializada
   - IF perspectivas complementarias → integrar como facetas
   - IF conflicto irreconciliable → presentar ambas posiciones
5. Estructurar respuesta alineada al objetivo original
6. Redactar respuesta integrada con atribucion justa
7. Verificar completitud: ¿el objetivo queda cubierto?
8. IF incompleto → senalar gaps y recomendar iteracion

## Signature Output

```
**Objetivo**: [objetivo original]
**Convergencias**: [puntos de acuerdo]
**Divergencias**: [perspectivas complementarias o conflictos]
**Respuesta Integrada**: [sintesis coherente]
**Completitud**: [SI|NO — gaps identificados]
**Proximos pasos**: [acciones recomendadas]
```

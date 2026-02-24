---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-tension-resolver:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Resolver tensiones de diseno de datos usando criterios explicitos para tomar decisiones documentadas.

## Input/Output

- **Input:** Tension de diseno identificada durante S-CRISTALIZAR
- **Output:** Decision documentada con criterio aplicado e implicaciones

## Procedimiento

1. Identificar tension y clasificar:
   - **Normalizacion vs Simplicidad:** IF atributo tiene historia de vida propia → normalizar. IF valor simple → inline.
   - **Especificidad vs Generalidad:** IF estructura identica solo cambia contenido → generalizar (category). IF comportamiento especifico → separar.
   - **Polimorfismo vs Tipado fuerte:** IF estructura igual solo cambia sujeto → polimorfico. IF campos muy distintos → tablas separadas.
   - **Completitud vs Minimalismo:** IF historia lo requiere → incluir. IF es "nice to have" → omitir.
2. Aplicar criterio a caso concreto
3. Documentar decision con razon explicita
4. Evaluar implicaciones: que gana, que pierde, que riesgo asume
5. Verificar coherencia con decisiones previas

## Signature Output

```
**Tension**: [tipo]
**Criterio aplicado**: [descripcion]
**Decision**: [opcion elegida]
**Gana**: [beneficio]
**Pierde**: [costo]
**Coherencia**: [alineada/tension con decision X]
```

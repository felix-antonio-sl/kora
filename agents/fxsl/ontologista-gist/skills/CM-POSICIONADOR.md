---
_manifest:
  urn: "urn:fxsl:skill:ontologista-gist-posicionador:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Establecer posicion dialectica completa antes de operar. Hereda del Pensador-Generador y extiende con posicionamiento ontologico especifico.

## I/O

- **Input:** Solicitud de modelado del usuario, contexto conversacional
- **Output:** Posicion establecida (contexto + praxis + posicion ontologica) para guiar operacion

## Procedimiento

1. CONTEXTO (C1-C4):
   - C1-RECURSOS: herramientas ontologicas, editores, reasoners disponibles
   - C2-PROPOSITO: explorar↔especificar, documentar↔implementar, temporal↔permanente
   - C3-DOMINIO: conocido↔novedoso, estable↔volatil, simple↔complejo
   - C4-CULTURA: formal↔informal, agil↔waterfall, tolerante↔estricto
2. PRAXIS (B1-B4):
   - B1-ALCANCE: que conceptos modelar, que excluir
   - B2-AUDIENCIA: ontologo experto↔desarrollador, fidelidad↔practicidad
   - B3-ESTRATEGIA: top-down (desde Gist)↔bottom-up (desde datos)
   - B4-COMPLETITUD: completo↔MVP, foco↔contexto
3. POSICION ONTOLOGICA:
   - NIVEL: TBox (clases)↔ABox (instancias)↔Reference Data
   - PERSPECTIVA: Gist-centric↔Domain-centric↔Integration
   - ROL: Arquitecto↔Modelador↔Auditor↔Integrador

## Signature Output

```
CONTEXTO: C1={}, C2={}, C3={}, C4={}
PRAXIS: B1={}, B2={}, B3={}, B4={}
POSICION: NIVEL={}, PERSPECTIVA={}, ROL={}
```

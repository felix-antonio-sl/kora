---
_manifest:
  urn: "urn:kora:agent-bootstrap:orquestador-generico-cm-orchestration-engine:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Ejecutar protocolo de orquestacion seleccionado coordinando participantes segun estrategia.

## Input/Output

- **Input:** Participantes con roles asignados, protocolo seleccionado (SECUENCIAL|PARALELO|DINAMICO|CONSENSO), objetivo, contexto compartido
- **Output:** Resultados recolectados de cada participante, evaluacion de suficiencia, decision de continuidad

## Procedimiento

1. Verificar participantes resueltos y roles confirmados
2. Ejecutar segun protocolo:
   - SECUENCIAL: FOR each participante → input=ctx+prev_output → output → chain al siguiente
   - PARALELO: FOR each participante en paralelo → outputs → agregar todos
   - DINAMICO: WHILE not done → invocar siguiente → evaluar resultado → route segun resultado
   - CONSENSO: FOR each participante → perspectivas independientes → negociar convergencia
3. Recolectar outputs de cada participante
4. Evaluar suficiencia: ¿objetivo cubierto?
5. Decidir: continuar(mas iteraciones) | ajustar(cambiar protocolo/roles) | sintetizar(suficientes resultados)
6. IF error en participante → degradar gracefully, continuar con disponibles
7. Registrar trace de ejecucion para atribucion

## Signature Output

```
**Protocolo**: [SECUENCIAL|PARALELO|DINAMICO|CONSENSO]
**Participantes invocados**: [N de M]
**Resultados**:
- [Participante 1 (Rol)]: [resumen resultado]
- [Participante 2 (Rol)]: [resumen resultado]
**Suficiencia**: [SI|NO — razon]
**Decision**: [continuar|ajustar|sintetizar]
```

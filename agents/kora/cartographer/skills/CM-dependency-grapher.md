---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-dependency-grapher:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Construir grafo de dependencias entre elementos del dominio identificando nodos centrales, ancestros, hojas y ciclos.

## Input/Output

- **Input:** Elementos clasificados ontologicamente desde S-MAPEAR
- **Output:** Grafo de dependencias con analisis topologico

## Procedimiento

1. Identificar nodos centrales (alta conectividad — muchas relaciones)
2. Identificar ancestros (clasificadores base — referenciados por muchos)
3. Identificar hojas (entidades terminales — no referenciadas por otros)
4. Detectar ciclos (relaciones bidireccionales — A depende de B y B de A)
5. Construir grafo visual o textual de dependencias
6. Anotar cardinalidades en cada relacion (1:1, 1:N, N:M)
7. Identificar clusters naturales (grupos de nodos fuertemente conectados)

## Signature Output

```
**Grafo de Dependencias**:
- Nodos centrales: [lista con grado]
- Ancestros (bases): [lista]
- Hojas (terminales): [lista]
- Ciclos detectados: [lista o NINGUNO]
- Clusters: [grupos identificados]
[Representacion visual mermaid o textual]
```

---
_manifest:
  urn: "urn:kora:agent-bootstrap:transformer-cm-diff-engine:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Comparar documento original con artefacto KODA para verificar fidelidad de la transformacion identificando hechos preservados, modificados, omitidos y agregados.

## Input/Output

- **Input:** Documento original + artefacto KODA desde S-COMPARATOR
- **Output:** Reporte de fidelidad con conteo de hechos por categoria y Fidelity Score

## Procedimiento

1. Extraer todos los hechos del documento original (requisitos, datos, definiciones, reglas)
2. Verificar presencia de cada hecho en artefacto KODA
3. Clasificar cada hecho:
   - Preservado: presente sin modificacion semantica
   - Modificado: presente con cambio semantico (detalle especifico)
   - Omitido: ausente del artefacto (CRITICO si >0)
   - Agregado: presente en artefacto pero no en original (verificar si inferencia valida)
4. Calcular Fidelity Score: hechos preservados / hechos totales × 100
5. IF omisiones → marcar como CRITICO, listar hechos faltantes
6. IF agregados → verificar si son inferencias validas o contaminacion

## Signature Output

```
**Reporte de Fidelidad**:
- Hechos en original: [N]
- Preservados: [X] ([Y%])
- Modificados: [A] (con detalle)
- Omitidos: [B] (CRITICO si > 0)
- Agregados: [C] (verificar inferencias)
- Fidelity Score: [Z%]
```

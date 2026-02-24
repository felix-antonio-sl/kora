---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:abogado-legislacion-medica-cm-estatuto-selector:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Determinar que estatuto aplica segun vinculo del medico con su empleador. Retorna jerarquia normativa en orden de precedencia.

## Input/Output

- **Input:** Tipo de empleador (SNSS, APS Municipal, FFAA, Carabineros, Privado) + tipo de vinculo (Planta, Contrata, Honorarios, Contrato)
- **Output:** Lista ordenada de estatutos aplicables con precedencia

## Procedimiento

1. Identificar tipo de empleador: SNSS, APS Municipal, FFAA, Carabineros, Privado
2. Identificar tipo de vinculo: Planta, Contrata, Honorarios, Contrato
3. Aplicar matriz de decision:
   - Medico en Servicio de Salud (SNSS): CPR -> LOC 18.575 -> Ley 19.664 -> Ley 15.076 -> EA 18.834 -> Codigo Trabajo
   - Medico en APS Municipal: CPR -> LOC 18.575 -> Ley 19.378 -> Ley 18.883 -> Ley 18.695
   - Medico en FFAA: DFL 1/1997 -> Ley 15.076 -> EA 18.834
   - Medico en Carabineros: CPR -> LOC 18.575 -> Ley 18.961 -> DEC 412/2019 -> Ley 15.076
   - Medico sector privado: CPR -> Codigo del Trabajo -> Reglamento Interno
4. Retornar estatutos aplicables en orden de precedencia

## Signature Output

Tabla con columnas: Orden | Norma | Aplicacion. Ordenada por precedencia normativa descendente.

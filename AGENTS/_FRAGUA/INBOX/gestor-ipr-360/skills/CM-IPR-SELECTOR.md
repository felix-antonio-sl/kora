---
_manifest:
  urn: urn:gn:skill:gestor-ipr-360-ipr-selector:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Clasificar naturaleza y modalidad de una intervencion publica regional para seleccionar instrumento y guia apropiados.

## Input/Output
- **Input:** Idea de proyecto o intervencion con naturaleza y modalidad identificadas
- **Output:** Instrumento IPR seleccionado + guia URN correspondiente

## Procedimiento
ARBOL DECISION:
1. Clasificar Naturaleza: IDI (Iniciativa de Inversion) | PPR (Programa Presupuestario Regional)
2. Clasificar Modalidad: Directa | Transferencia
3. Aplicar reglas:
   - IDI + Directa = SNI Ejecucion Directa → guia-idi-sni-sts
   - IDI + Transferencia + Municipalidad + <4.545 UTM = FRIL → guia-fril-2025-sts
   - IDI + Directa + Conservacion/Reposicion/ANF = Circular 33 → guia-circular-33-sts
   - IDI + Transferencia + Servicio = SNI Transferencia → guia-idi-sni-sts
   - PPR + Transferencia + Servicio = PPR Transferencia → transferencia-ppr
   - PPR + Directa GORE = Programas Glosa 06 → guia-programas-directos-gore
   - I+D + Innovacion = FRPD → guia-frpd-nuble
   - Subvencion + Cultura/Deporte/Social = 8% FNDR → instructivo-subvencion-8-2025-sts
   - Estudio/ANF = Circular 33 → guia-circular-33-sts

NOTA FRPD: FRPD tiene routing especial post-seleccion — CTCI (exenta eval) vs Fomento-Proyecto (→Track A) vs Fomento-Programa (→Track D1).

## Signature Output
Instrumento seleccionado + guia URN + justificacion de clasificacion.

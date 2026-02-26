---
_manifest:
  urn: "urn:fxsl:skill:arquitecto-sistemas-informacion-overlap-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar superposicion entre IS y el Work System que soporta. Clasificar tipo de overlap y determinar implicaciones de diseno.

## I/O

- **Input:** IS en diseno y WS destino desde S-WS-CONTEXT o S-IS-FUNCTIONS
- **Output:** Clasificacion overlap con implicaciones de diseno

## Procedimiento

1. Identificar actividades del WS que el IS automatiza/soporta
2. Clasificar tipo de superposicion:

| Tipo | Descripcion | Ejemplo |
|------|-------------|---------|
| Interfaz simple | IS solo provee interfaz minima al WS | ATM: IS banco <-> WS usuario retirando dinero |
| Superposicion minima | IS automatiza parte especifica del WS | Sistema reservas <-> WS usuario buscando vuelos |
| Superposicion sustancial | IS es parte integral de actividades del WS | EMR <-> WS medico atendiendo pacientes |
| Inclusion completa | IS es el WS o lo contiene completamente | IS cierre financiero automatico |

3. Evaluar implicaciones para diseno del IS
4. Recomendar nivel de funcionalidad IS segun overlap

## Signature Output

```
## Analisis Superposicion IS <-> WS
- **Tipo overlap**: {interfaz simple|minima|sustancial|inclusion completa}
- **Actividades automatizadas**: {lista}
- **Actividades humanas residuales**: {lista}
- **Implicacion diseno**: {recomendacion}
```

---
_manifest:
  urn: urn:ops:skill:clawstack-intent-classifier:1.0.0
  type: lazy_load_endofunctor
---

# CM-INTENT-CLASSIFIER

## Proposito
Clasificar la solicitud legacy para decidir si debe redirigirse a `kora/clawforge` o cerrarse.

## Input/Output
- **Input:** mensaje: string, foco_actual: string | null, contexto_previo: object | null
- **Output:** IntentClassification (ver Signature Output)

## Procedimiento
1. Detectar si el mensaje pide cierre explicito.
2. Si no pide cierre, clasificar la solicitud como `REDIRECT` hacia `kora/clawforge`.
3. Inferir, cuando sea posible, la capacidad operacional original (`deploy`, `provision`, `audit`, `troubleshoot`, `upgrade`, `configure`, `consult`) para preservarla en la redireccion.
4. Marcar confianza baja solo si el mensaje es casi vacio o no contiene ninguna pista util.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| capacidad | enum | REDIRECT, END |
| destino | string | `kora/clawforge` o `END` |
| capacidad_inferida | string | Capacidad operacional original si pudo inferirse |
| confianza | enum | alta, media, baja |
| cierre_solicitado | bool | True si el mensaje indica cierre |

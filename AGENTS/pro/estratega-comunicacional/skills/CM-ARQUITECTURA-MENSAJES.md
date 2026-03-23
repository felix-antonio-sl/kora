---
_manifest:
  urn: urn:pro:skill:estratega-arquitectura-mensajes:1.0.0
  type: lazy_load_endofunctor
---

## Proposito

Disenar el sistema de mensajes: segmentar audiencias, adaptar enfasis, seleccionar canales, definir secuencia y verificar consistencia con la narrativa central.

## Input/Output

- **Input:** Narrativa estrategica definida (o contexto directo del usuario con posicionamiento claro).
- **Output:** ArquitecturaMensajes { segmentacion, adaptaciones, canales, secuencia, consistencia }

## Procedimiento

1. **SEGMENTACION** — Audiencias distintas requieren mensajes distintos. Identificar segmentos por perfil, necesidad y relacion con la organizacion.
2. **ADAPTACION** — Mismo mensaje central, diferente enfasis y profundidad por segmento. Mapear: segmento -> enfasis -> nivel de detalle.
3. **CANALES** — Donde esta cada audiencia, que formato espera. Mapear: segmento -> canal optimo -> formato -> frecuencia.
4. **SECUENCIA** — Que se dice primero, que se reserva, que se repite. Definir timeline comunicacional con hitos.
5. **CONSISTENCIA** — Verificar que todos los mensajes por segmento apuntan a la misma narrativa central. Detectar contradicciones.
6. Establecer prioridades de ejecucion: que segmento primero, que canal primero.

## Signature Output

```
Arquitectura de Mensajes:
SEGMENTOS: <lista segmentos>
| Segmento | Mensaje adaptado | Canal | Formato | Prioridad |
SECUENCIA: <timeline hitos>
CONSISTENCIA: <verificacion>
```

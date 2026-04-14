---
_manifest:
  urn: urn:korvo:skill:cm-close:3.1.0
  type: lazy_load_endofunctor
---

## Proposito

Cierre nocturno con micro-check de senales PCA v4.1 (per S7). Vacia capturas residuales, evalua senales criticas del dia, y ofrece espacio para reflexion breve.

## Input/Output

- **Input:** estado actual de entidades (Candidatos, UTs, Proyectos, Objetivos)
- **Output:** CloseResult { capturas_nuevas: int, alertas: Alerta[], triaje_recordado: bool }

## Procedimiento

1. Preguntar: *"Algo que capturar antes de cerrar?"*
   - Si hay capturas -> ejecutar CM-CAPTURA para cada una.

2. Si no hubo triaje hoy -> recordar suavemente: *"Sin triaje hoy — mañana pendiente."*

3. **Micro-check senales (INV-11, per §7):**
   - UTs bloqueadas > 7d -> alertar con lista.
   - UTs sin actividad > 30d -> alerta suave de drift.
   - UTs con U > 0.8 -> alertar urgencia critica.
   - RESULTADO adverso sin trabajo > 14d -> alertar como candidato a revision.
   - RESULTADO favorable con ventana_fin < 7d -> alertar con urgencia.
   - Objetivo sin contribuciones constitutivas -> alertar trabajo sin ancla.
   - Candidatos en buffer > 30 -> sugerir triaje urgente.
   - Proyecto con todas UTs completadas/descartadas -> senalizar `completado` para confirmacion.

4. Recordar vaciar micro-capturas del dia al buffer.

5. Confirmar cierre.

**Duracion:** 2-5 minutos.

## Signature Output

```
🌙 Cierre del dia.
{⚠️ Sin triaje hoy | ✓ Triaje hecho}
{⚠️ Bloqueos >7d: <lista> | ✓ Sin bloqueos prolongados}
{⚠️ Drift >30d: <lista> | }
{⚠️ Urgencia U>0.8: <lista> | }
{⚠️ RESULTADO adverso sin trabajo: <lista> | }
{⚠️ RESULTADO ventana <7d: <lista> | }
{⚠️ Objetivo sin constitutivas: <lista> | }
{⚠️ Proyecto completable: <lista> | }
{⚠️ Buffer: <N> candidatos | ✓ Buffer OK}
Algo que capturar?
```

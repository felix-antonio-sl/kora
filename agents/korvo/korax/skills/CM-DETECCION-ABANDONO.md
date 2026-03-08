---
_manifest:
  urn: urn:korvo:skill:korax-deteccion-abandono:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Detección y reactivación suave ante abandono del sistema. Escala en 3 niveles calibrados (INV-08: 3d → 7d → 14d, sin saltar niveles).

## Input/Output
- **Input:** last_activity: timestamp, buffer_state: {count, ages}
- **Output:** reactivation: AbandonResult {nivel, mensaje, opciones}

## Procedimiento
### Detección (<1 minuto, automática)

Evaluar nivel según tiempo sin triaje/actividad:

| Nivel | Umbral | Acción |
|---|---|---|
| 1 | ≥3 días sin triaje | Alerta suave: "Han pasado 3 días. Tienes {n} items esperando. ¿Triaje rápido, mañana, o bancarrota del buffer?" |
| 2 | ≥7 días sin triaje | Propuesta de bancarrota selectiva: eliminar todo >7 días, mantener últimos 3 días. |
| 3 | ≥14 días sin actividad | Proponer pausa del sistema o conversación abierta. |

### Rama Autónoma (delegation_scope ⊇ maintenance)

En nivel 1 (≥3 días), Korax **PUEDE** ejecutar triaje rápido automático:
1. Eliminar items >7 días.
2. Mantener items <3 días.
3. Incubar el resto a SOMEDAY.md.
4. **DEBE** reportar acciones al siguiente contacto.

**Duración:** <1 minuto (detección). Reactivación: variable según nivel.

## Signature Output
```
👋 Nivel {1|2|3}: {n} días sin {triaje|actividad}.
Buffer: {n} items ({n} >7 días).
Opciones:
1️⃣ {opción según nivel}
2️⃣ {opción según nivel}
3️⃣ {opción según nivel}
```

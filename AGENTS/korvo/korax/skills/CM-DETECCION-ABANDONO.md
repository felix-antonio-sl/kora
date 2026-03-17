---
_manifest:
  urn: urn:korvo:skill:cm-deteccion-abandono:2.0.0
  type: lazy_load_endofunctor
---

## Proposito

Deteccion y reactivacion suave ante abandono del sistema. Escala en 3 niveles calibrados sobre actividad de entidades PCA v4.1 (INV-07: 3d -> 7d -> 14d, sin saltar niveles).

## Input/Output

- **Input:** ultima actividad sobre entidades (timestamp), estado de Candidatos, UTs y Proyectos
- **Output:** AbandonResult { nivel: 1|2|3, dias_sin_actividad: int, candidatos_pendientes: int, opciones: string[] }

## Procedimiento

### Deteccion (<1 minuto)

Evaluar nivel segun tiempo sin actividad sobre entidades (no archivos):

| Nivel | Umbral | Accion |
| --- | --- | --- |
| 1 | >= 3 dias sin triaje ni completar UT | Alerta suave: *"Han pasado <n> dias. Tienes <n> candidatos esperando. Triaje rapido, manana, o bancarrota del buffer?"* |
| 2 | >= 7 dias sin actividad significativa | Propuesta de bancarrota selectiva: descartar Candidatos > 7d, mantener ultimos 3d. Revisar UTs bloqueadas. |
| 3 | >= 14 dias sin actividad | Proponer pausa del sistema o conversacion abierta. Sin presion. |

### Escalacion

- Nivel 1 -> 2 -> 3 estrictamente secuencial (INV-07). No se salta niveles.
- Cada nivel se evalua una sola vez por umbral alcanzado.
- Si el operador responde en cualquier nivel, se reinicia el contador.

### Co-agencia fija

En todos los niveles, Korax presenta opciones y espera decision del operador. No ejecuta acciones autonomas.

**Duracion:** <1 minuto (deteccion). Reactivacion: variable segun nivel.

## Signature Output

```
👋 Nivel <1|2|3>: <n> dias sin actividad.
Candidatos pendientes: <n>
UTs bloqueadas: <n>
Opciones:
1️⃣ <opcion segun nivel>
2️⃣ <opcion segun nivel>
3️⃣ <opcion segun nivel>
```

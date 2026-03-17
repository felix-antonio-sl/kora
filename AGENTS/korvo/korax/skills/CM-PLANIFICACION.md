---
_manifest:
  urn: urn:korvo:skill:cm-planificacion:4.0.0
  type: lazy_load_endofunctor
---

## Proposito

Planificacion matutina sobre entidades PCA v4.1. Ordena UTs pendientes por P x U, asigna bloques segun modo energetico derivado de UT.modo (FM/SR/MK) y energia del operador. Verifica restricciones de PROPOSITO ancestral (RI-12). Propone Proyecto para RESULTADO nuevo si aplica.

## Input/Output

- **Input:** date: string, UTs pendientes, Proyectos activos, Objetivos con restricciones, energia del operador
- **Output:** PlanDiario { bloques: Bloque[], uts_ordenadas_pxu: UT[] }

## Procedimiento

### Paso 0: Check-in energetico

Antes de planificar, verificar estado del operador:
- *"Como amaneciste? Energia?"* (alto/medio/bajo)
- Si energia baja -> adaptar: priorizar bloques cortos, reducir DEEP, sugerir recuperacion.

### Paso 1: Inventario

1. Obtener UTs con estado "pendiente" de Proyectos activos y UTs free-floating.
2. Excluir UTs de Proyectos pausados (no se presentan en planificacion, §4.3).
3. Obtener UTs con estado "bloqueada" — listar bloqueos si relevantes hoy.
4. Computar P para cada UT pendiente:
   - Si UT sin contribucion: P = 0.2 (work-in-vacuum; alertar).
   - Si UT con contribucion: P = peso(tipo) x nivel_efectivo(resultado).
5. Computar U para cada UT: U = min(1.0, 1/dias_a_deadline). Sin deadline: U = 0. Overdue: U = 1.0.
6. Ordenar UTs por P x U descendente.
7. Si alguna UT tiene U > 0.8: **alertar urgencia critica** y proponer asignacion inmediata.

### Paso 2: Verificacion de restricciones (RI-12)

Para cada UT a presentar:
1. Trazar cadena: UT -> Proyecto -> Contribucion -> RESULTADO -> PROPOSITO (via parent_id).
2. Si PROPOSITO tiene `restricciones`, comparar UT propuesta contra cada restriccion.
3. Si posible violacion: senalizar al operador — *"Esta UT podria violar tu restriccion '<restriccion>'. Proceder?"*
4. Operador confirma o descarta. Korax NO filtra autonomamente.

### Paso 3: Propuesta de bloques

1. Derivar modo energetico de cada UT segun UT.modo:
   - `MK` solo -> DEEP (60-90 min, energia alta)
   - `FM` o `MK+FM` -> SHALLOW (15-45 min, energia media)
   - `SR` (con otros) -> SOCIAL (variable, disponibilidad externa)
2. Filtrar por situacion_temporal (ST) y situacion_fisica (SF) cuando disponibles.
3. Mapear a bloques segun energia:
   - Energia alta: DEEP primero, luego SHALLOW, luego SOCIAL.
   - Energia media: SHALLOW primero, intercalar.
   - Energia baja: solo SHALLOW cortos, maximo 1, sin DEEP.
4. Respetar timebox de cada UT.
5. Aplicar matriz P x U:
   - P alta + U alta: proponer asignacion inmediata.
   - P alta + U baja: programar para proximo bloque DEEP.
   - P baja + U alta: completar rapido.
   - P baja + U baja: diferir, no presentar.
6. Presentar plan como **propuesta** al operador. Korax NO asigna — propone (INV-03).

### Paso 4: Confirmacion

1. Operador confirma, ajusta o rechaza bloques.
2. Si operador confirma bloque inmediato -> transicion a S-EXECUTE.
3. Si hay RESULTADO nuevo sin Proyecto, proponer: *"Quieres crear un Proyecto para organizarlo?"*
4. Si hay RESULTADO sin parent_id, proponer: *"A que PROPOSITO contribuye?"*

**Duracion:** 5 minutos maximo.

## Signature Output

```
☀️ Plan del dia (<date>):
Energia: <nivel>

| Bloque | Modo | UT | Timebox | PxU |
| --- | --- | --- | --- | --- |
| 09:00 | DEEP (MK) | <titulo> | 90min | 0.85 |
| 11:00 | SHALLOW (FM) | <titulo> | 30min | 0.42 |
| 14:00 | SOCIAL (SR) | <titulo> | 45min | 0.35 |

Proyectos activos: <N> | UTs pendientes: <N> | Bloqueadas: <N>
{⚠️ Urgencia critica: <lista> | }
{⚠️ Restriccion: <detalle> | }
```

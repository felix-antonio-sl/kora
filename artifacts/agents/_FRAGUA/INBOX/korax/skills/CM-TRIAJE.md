---
_manifest:
  urn: urn:korvo:skill:cm-triaje:3.1.0
  type: lazy_load_endofunctor
---

## Proposito

Procesar el buffer de Candidatos mediante el arbol de decision N1/N2/N3 (§4.1), transformando cada Candidato en una entidad tipada PCA v4.1 o descartandolo. Co-agencia fija: Korax presenta y senaliza tipo probable por lexico, operador decide.

## Input/Output

- **Input:** buffer de Candidatos con estado "capturado"
- **Output:** SesionTriaje { procesados: int, por_tipo: { ut: int, resultado: int, proposito: int, incubado: int, descartado: int } }

## Procedimiento

1. Contar Candidatos pendientes. Si buffer vacio, reportar y terminar.
2. Para cada Candidato:
   - Marcar estado: `en_triaje`.
   - Presentar al operador y guiar por el arbol de decision.

### Nivel N1 — Descartar?

Presentar el Candidato y preguntar: *"Descartar?"*

- **SI** -> marcar Candidato como `descartado`. Siguiente.
- **NO** -> N2.

### Nivel N2 — Incubar? (> 14 dias)

Preguntar: *"Incubar para mas adelante?"*

- **SI** -> marcar Candidato como `incubado`. Siguiente.
- **NO** -> N3.

### Nivel N3 — Tipo semantico

**Senalizacion lexica:** Korax analiza el texto del Candidato y senaliza tipo probable:

| Patron lexico | Tipo sugerido |
| --- | --- |
| "hacer / revisar / terminar / enviar" | UT |
| "lograr / asegurar / tener / completar" | RESULTADO |
| "riesgo de / problema con / amenaza" | RESULTADO (motivo adverso) |
| "oportunidad de / ventana para" | RESULTADO (motivo favorable) |
| "quiero ser / vision de / aspiramos" | PROPOSITO |

Presentar sugerencia y preguntar: *"Parece una [tipo sugerido]. Correcto, o es [alternativas]?"* Operador confirma o corrige.

- **UT** -> N3-UT
- **RESULTADO** -> N3-RESULTADO
- **PROPOSITO** -> N3-PROPOSITO

### N3-UT — Parametros de la UT

Proponer y confirmar:
- `titulo`: verbo + objeto concreto
- `modo`: combinacion de `FM` (fisico), `SR` (social), `MK` (mental)
- `timebox`: `15 | 30 | 60 | 90` minutos
- `deadline?`: fecha limite si aplica
- `situacion_temporal?`: ventana horaria, dias de semana
- `situacion_fisica?`: lugares, herramientas, conectividad
- `proyecto_id?`: si hay Proyecto activo relevante, proponer asignacion

Crear UT con estado "pendiente" via `crear_objetivo` no aplica; se crea directamente.
Marcar Candidato como `promovido` con `destino_tipo: UT`, `destino_id: <ut_id>` (RI-10).

### N3-RESULTADO — Parametros del RESULTADO

Proponer y confirmar:
- `titulo`: outcome concreto verificable
- `motivo?`: contexto causal
  - Si texto sugiere situacion adversa: `motivo.tipo = adverso`, pedir `urgencia` (alta/media/baja) (RI-08)
  - Si texto sugiere oportunidad: `motivo.tipo = favorable`, pedir `ventana_fin` (RI-09)
  - Si declaracion directa: sin motivo
- `parent_id?`: *"A que PROPOSITO contribuye?"* — proponer PROPOSITO existente o dejar flotante
- Proponer crear Proyecto: *"Quieres crear un Proyecto para organizarlo?"*

Crear Objetivo tipo RESULTADO via `crear_objetivo`.
Marcar Candidato como `promovido` con `destino_tipo: RESULTADO`, `destino_id: <objetivo_id>` (RI-10).

### N3-PROPOSITO — Parametros del PROPOSITO

Proponer y confirmar:
- `titulo`: aspiracion de largo plazo
- `anti_vision?`: *"Que vida te niegas a vivir si no persigues esto?"*
- `restricciones?`: *"Hay limites no negociables?"*

Crear Objetivo tipo PROPOSITO via `crear_objetivo`.
Marcar Candidato como `promovido` con `destino_tipo: PROPOSITO`, `destino_id: <objetivo_id>` (RI-10).

3. Al finalizar todos los Candidatos, reportar conteos.
4. Si >50% fueron descartados, recordar al operador: *"Mas de la mitad descartados. Considera filtrar antes de capturar."* (regla del 50%).

**Nota:** Proyecto NO es salida del triaje. Se crea en planificacion (§3.3).

## Signature Output

```
📊 Triaje completado: <N> procesados
   UT: <n> | RESULTADO: <n> | PROPOSITO: <n> | Incubado: <n> | Descartado: <n>
   Buffer vacio ✓
```

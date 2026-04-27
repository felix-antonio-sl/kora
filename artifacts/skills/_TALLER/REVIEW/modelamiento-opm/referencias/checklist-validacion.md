# Checklist de validacion — V-* criticos + heuristicas

Validacion en tres niveles. Cada nivel cita su capa propietaria y su severity.

## Nivel 1 — Reglas de la capa visual (`urn:fxsl:kb:opd-es`)

Subset critico sobre las 263 reglas V-*. Para cada validacion, cita la regla.

### V-0 a V-10 (gramatica base)

- [ ] **V-1**: cada cosa tiene exactamente uno de `objeto` o `proceso` como tipo.
- [ ] **V-2**: rectangulos rectos = objetos; rectangulos redondeados = procesos.
- [ ] **V-3**: estados son sub-rectangulos redondeados dentro de un objeto.
- [ ] **V-5**: enlaces tienen exactamente un origen y un destino.
- [ ] **V-7**: contornos respetan distintivos de esencia (fisica vs informatica).

### V-11 a V-30 (composicion de enlaces)

- [ ] **V-13**: enlaces procedurales conectan proceso ↔ (objeto | estado).
- [ ] **V-14**: enlaces estructurales conectan cosas del mismo perseverance (objeto-objeto o proceso-proceso).
- [ ] **V-18**: triangulos estructurales (agregacion, generalizacion, clasificacion, exhibicion) tienen hijos visibles.
- [ ] **V-25**: operadores logicos (AND/OR/XOR) en fans de enlaces respetan precedencia.

### V-100 a V-130 (refinamiento entre OPDs)

- [ ] **V-105**: arbol de in-zooming es aciclico.
- [ ] **V-110**: sub-procesos en in-zoom estan ordenados temporalmente (top-down por defecto).
- [ ] **V-115**: links del padre se preservan en el hijo (visibles o referenciados).
- [ ] **V-120**: unfolding mantiene una sola dimension por descomposicion.

### V-200 a V-263 (canon-diagrama, sub-modelo, requisitos)

- [ ] **V-242**: sub-model es el cuarto par canonico de refinamiento-abstraccion.
- [ ] **V-251**: clausura OPD↔OPL local; el modelo compuesto es DAG.
- [ ] **V-252**: cada cosa cross-model tiene URI persistente.

## Nivel 2 — Reglas de la capa semantica (`urn:fxsl:kb:opm-es`)

### Clases de cosas

- [ ] cada cosa pertenece a `objeto`, `proceso` o `estado`. Sin clases inventadas.
- [ ] esencia (fisica/informatica) declarada para cada cosa donde aplique.
- [ ] `agent` es humano u organizacion; nunca maquina. Las maquinas son `instrument`.

### Clases de relaciones

- [ ] enlaces estructurales: `agregacion-participacion`, `generalizacion-especializacion`, `clasificacion-instanciacion`, `exhibicion-caracterizacion`.
- [ ] enlaces procedurales transformadores: `consumption`, `result`, `effect`.
- [ ] enlaces procedurales habilitantes: `agent`, `instrument`.
- [ ] enlaces de control: `condition`, `event`, `exception`, `invocation`.

### Principios

- [ ] **principio de unicidad**: una sola modalidad por hecho (no expresar el mismo hecho con dos relaciones distintas).
- [ ] **principio de minimalidad**: si dos cosas son indistinguibles funcionalmente, son la misma cosa.
- [ ] **principio de teorema objeto-proceso**: toda cosa es objeto o proceso, no ambos.

## Nivel 3 — Heuristicas operativas (`urn:fxsl:kb:manual-metodologico-opm-es`)

### Claridad (cognitive load)

- [ ] cada OPD tiene **≤ 7 ± 2 cosas visibles** (regla de Miller aplicada al modelado).
- [ ] cada OPD tiene **un proceso central distinguible**.
- [ ] enlaces no se cruzan innecesariamente.
- [ ] etiquetas legibles, sin truncar.

### Completitud (covertura del proposito)

- [ ] el modelo expresa **estructura** (que cosas hay y como se relacionan).
- [ ] el modelo expresa **comportamiento** (como cambian las cosas en el tiempo).
- [ ] el modelo expresa **funcion** (para que sirve el sistema).
- [ ] cada cosa relevante para el proposito esta presente en algun nivel del modelo.

### Bimodalidad efectiva

- [ ] cada hecho del OPD tiene su sentencia OPL-ES correspondiente.
- [ ] cada sentencia OPL-ES tiene su realizacion grafica en algun OPD.
- [ ] no hay hechos solo-OPD (graficos sin OPL).
- [ ] no hay hechos solo-OPL (sentencias sin grafico).

## Reporte de validacion

Formato sugerido por validacion:

```
Reporte de validacion — <nombre del modelo> — <fecha>

Capa visual (opd-es): X/Y reglas pasan
  ✗ V-105: ciclo detectado entre in-zoom de Hacer Cafe y de Calentar Agua
  ✗ V-115: link 'Hacer Cafe consume Agua' falta en SD1.1

Capa semantica (opm-es): X/Y reglas pasan
  ✗ Cafetera declarada como agent — debe ser instrument

Heuristicas: X/Y pasan
  ⚠ SD1.2 tiene 11 cosas visibles (>9, recomienda subdividir)
  ✓ bimodalidad efectiva sostenida
```

Si una regla CRITICAL falla → `validar-modelo` retorna fail, vuelve a `refinar-modelo`.
Si solo fallan WARN/heuristicas → entregable pero con anotacion de tradeoffs.

# Mecanismos de refinamiento — los 4 pares canonicos

OPM controla la complejidad por **detalle**, no por aspectos. Cuatro pares de operadores cubren la totalidad del refinamiento. Cada par es un eje refinamiento ↔ abstraccion.

| # | Refinamiento | Abstraccion | Categoria | Direccion |
|---|--------------|-------------|-----------|-----------|
| 1 | In-zooming | Out-zooming | proceso | descomposicion en OPD hijo |
| 2 | Unfolding | Folding | objeto | descomposicion en OPD hijo |
| 3 | State expression | State suppression | objeto | mismo OPD |
| 4 | Sub-model composition | Sub-model decomposition | modelo entero | composicion inter-modelo |

## 1. In-zooming / Out-zooming

**Que hace**: descompone un proceso en sus sub-procesos secuenciales.

**Cuando aplicar**: el proceso del nivel actual es complejo y conviene mostrar como ocurre internamente.

**Como**:
- Crear un OPD hijo etiquetado `SDx.y`.
- En el OPD hijo, el proceso del padre aparece como contenedor.
- Dentro del contenedor, los sub-procesos en orden de ejecucion (de arriba hacia abajo).
- Los transformees y enablers del padre cruzan el contenedor segun pertenecientes a cada sub-proceso.
- Los links que entran/salen del proceso padre se redistribuyen a los sub-procesos correctos.

**OPL-ES**:
```
Hacer Cafe esta hecho de Calentar Agua, Filtrar Cafe.
```

**Restricciones (V-*)**:
- aciclico: el proceso descompuesto no puede aparecer dentro de su propio in-zoom.
- conservacion: los transformees/enablers del padre estan presentes (visibles o referenciados) en el hijo.
- coherencia: los links del padre se preservan o redistribuyen sin perder semantica.

## 2. Unfolding / Folding

**Que hace**: descompone un objeto en su estructura interna (partes, atributos, generalizaciones, instancias).

**Cuando aplicar**: el objeto del nivel actual tiene estructura interna relevante para la pregunta.

**Como**:
- Crear un OPD hijo donde el objeto aparece como contenedor.
- Dentro del contenedor, las partes/atributos como objetos relacionados con triangulos estructurales (agregacion, exhibicion, generalizacion, clasificacion).

**OPL-ES**:
```
Cafe Hecho consta de Liquido y Aroma.
Paciente exhibe Edad, Sexo y Diagnostico.
Vehiculo es de tipo Auto, Camion y Bus.
```

**Restricciones**:
- una sola dimension de descomposicion por unfold: agregacion ≠ generalizacion ≠ exhibicion ≠ clasificacion.
- aciclico: un objeto no se descompone en si mismo recursivamente.

## 3. State expression / suppression

**Que hace**: explicita los estados posibles de un objeto, sin crear nuevo OPD.

**Cuando aplicar**: el objeto cambia de estado por la accion de algun proceso del modelo, y ese cambio importa para la pregunta.

**Como**:
- En el mismo OPD donde aparece el objeto, mostrar sus estados como sub-rectangulos redondeados dentro de el.
- Conectar los procesos a los estados especificos (no al objeto entero) cuando aplica.

**OPL-ES**:
```
Paciente puede estar en no-diagnosticado o en diagnosticado.
Diagnosticar afecta Paciente, cambiandolo de no-diagnosticado a diagnosticado.
```

**Restricciones**:
- los estados son discretos; no usar para variables continuas (esas son atributos).
- todo estado declarado debe ser alcanzable por algun proceso del modelo o ser un estado inicial/terminal explicito.

## 4. Sub-model composition / decomposition

**Que hace**: incluye un modelo OPM externo entero (ya construido y publicado) por **referencia**, no por copia.

**Cuando aplicar**: el sistema actual usa un sub-sistema cuyo modelo OPM ya existe y es independiente.

**Como**:
- Declarar el sub-modelo como una cosa con `<<sub-model>>` o equivalente segun la edicion (ver opd-es §22 / §26).
- Conectar el sub-modelo via su interfaz declarada.
- No duplicar contenido del sub-modelo en el modelo actual.

**OPL-ES**:
```
Sistema de Pago es un sub-modelo cargado y sincronizado.
Resolver Solicitud usa Sistema de Pago.
```

**Restricciones (V-242, V-251, V-252)**:
- los modelos compuestos forman un DAG (acicliclo entre modelos).
- cada cosa referenciable cross-model debe tener identificador persistente (URI/UUID).
- la frontera entre modelo propietario y consumidor es estricta: el consumidor no muta cosas del sub-modelo.

## Criterios de decision

Tabla rapida para elegir el par correcto:

| Sintoma | Mecanismo |
|---------|-----------|
| "el proceso es muy denso, hay que mostrar sus pasos" | in-zooming |
| "el objeto tiene partes/atributos relevantes" | unfolding (escoger dimension) |
| "el objeto cambia de estado y el cambio importa" | state expression |
| "este sistema usa otro sistema completo ya modelado" | sub-model composition |

## Aciclicidad global

El arbol completo de refinamiento (procesos in-zoomed + objetos unfolded + sub-modelos compuestos) debe ser **aciclico**. Si detectas un ciclo, el modelo esta mal estructurado: alguna abstraccion esta faltante o algun nivel esta confundido. Volver al manual metodologico §refinamiento para diagnostico.

## Heuristica middle-out

OPM no obliga top-down ni bottom-up. La practica recomendada (manual §middle-out) es comenzar por el SD y **luego refinar en la direccion donde haya mayor incertidumbre o demanda**, no completar un nivel antes del siguiente.

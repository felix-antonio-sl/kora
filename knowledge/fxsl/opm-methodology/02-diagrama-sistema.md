---
_manifest:
  urn: "urn:fxsl:kb:opm-diagrama-sistema"
  provenance:
    created_by: "kora/curator"
    created_at: "2026-03-06"
    source: "opm_youtube.md + OPM version felix.md + ISO 19450"
version: "1.0.1"
status: published
tags: [opm, iso19450, sd, diagrama-sistema, modelado, procedimiento, refinamiento, sd1, opd-tree]
lang: es
---

# OPM — System Diagram (SD), Modelado y Refinamiento

SD = nivel 0. Punto de partida para cualquier modelo OPM. Vista de alto nivel para todos los stakeholders.

---

## Tres Aspectos del Sistema

Todo modelo OPM representa simultaneamente:

| Aspecto | Pregunta | Que incluye |
|---------|----------|-------------|
| Estructura | ¿Que ES el sistema? | Objetos, partes, relaciones estaticas. Objeto principal (operando) |
| Comportamiento | ¿Como OPERA? | Procesos, subprocesos, relaciones dinamicas. Proceso principal |
| Funcion | ¿Para QUE existe? | Beneficiarios, valor entregado, motivacion. Par (objeto-principal, proceso-principal) |

**Funcion del sistema** = combinacion de estructura y comportamiento. Par (proceso-principal, objeto-principal) conectados por enlace de transformacion.

---

## SD para Sistemas Artificiales (5 Componentes)

Sistema Diagram de sistemas creados por humanos. Nivel 0, minimo de detalles tecnicos.

### 1. Proposito del Sistema
Responde: ¿Para que se desarrollo? ¿Quienes son los beneficiarios?
- Identifica beneficiarios y beneficio especifico.
- Se expresa como cambio de estado en atributo del grupo beneficiario: de estado problematico → satisfactorio.
- OPL: `Processing changes BeneficiaryGroup's Attribute from problematic-state to satisfied-state.`

### 2. Funcion Principal
Responde: ¿Que transforma el proceso principal para entregar el beneficio?
- Par: proceso-principal (verbo gerundio) + objeto-principal (operando).
- La transformacion cambia atributo del objeto de estado problematico a satisfactorio.
- OPL: `Main-Process changes Main-Object from input-state to output-state.`

### 3. Habilitadores del Proceso Principal
Objetos requeridos para que ocurra el proceso principal. No son transformados.
- **Agentes:** humanos o grupos humanos (Agent Link — circulo solido).
- **Instrumentos:** objetos no humanos (Instrument Link — circulo vacio).
- Por defecto, el sistema mismo es instrumento principal. Nombre default: `[Nombre-Proceso] System`.

### 4. Entorno del Sistema
Things externos al sistema que afectan su operacion.
- Representados con contorno discontinuo (dashed) en OPD.
- Afiliacion = environmental.
- Incluye instrumentos ambientales (ej. conexion a internet).

### 5. Ocurrencia del Problema
Espejo del proposito: proceso ambiental que causa el problema que el sistema resuelve.
- Causa que atributo del beneficiario este en estado negativo (input-state del proposito).
- Solo relevante para sistemas artificiales y sociales.

---

## SD para Sistemas Naturales (3 Componentes)

| Componente SD artificial | Equivalente en sistema natural |
|--------------------------|-------------------------------|
| Proposito | **Resultado (Outcome):** puede ser beneficioso o perjudicial. No hay intencion de diseno |
| Funcion principal | Igual: par proceso-principal + objeto-principal |
| Habilitadores | Igual; sin agentes si no hay personas involucradas |
| Entorno | Igual |
| Ocurrencia del problema | **No aplica:** sin intencion de diseno no hay problema a resolver |

---

## Procedimiento de Modelado OPM (9 Pasos)

Secuencia para construir un SD desde cero:

| Paso | Componente | Pregunta | Nota |
|------|-----------|----------|------|
| 1 | Funcion Principal | ¿Cual es el proceso principal? | Nombre en gerundio ("-ing" / "-ando/-iendo") |
| 2 | Beneficiario | ¿Quien se beneficia? | Singular; Group para humanos, Set para inanimados |
| 3 | Atributo Beneficiario | ¿Que atributo mejora? ¿Estado entrada? ¿Estado salida? | Estado entrada = problematico; estado salida = deseado |
| 4 | Agente | ¿Quien (humano) habilita el proceso? | Puede coincidir con beneficiario |
| 5 | Sistema | ¿Como se llama el sistema? | Default sugerido en wizard: `[Proceso] System` |
| 6 | Instrumentos adicionales | ¿Que otros instrumentos no humanos se requieren? | Wizard de arranque: max 3 para forzar priorizacion y mantener limpio el modelo inicial |
| 7 | Inputs (Consumidos) | ¿Que objetos consume el proceso? | Wizard de arranque: max 3 para forzar priorizacion y mantener limpio el modelo inicial |
| 8 | Outputs (Creados) | ¿Que objetos crea el proceso? | Puede ser input con estado cambiado |
| 9 | Entorno | ¿Que objetos externos afectan al sistema? | Contorno discontinuo |

**Nota de aplicacion:** los limites `max 3` y el nombre default del sistema son heuristicas UX para un wizard de captura inicial en app web. Ayudan a priorizar y evitar un arranque del modelo con exceso de detalle. No son invariantes universales de OPM.

---

## OPD Tree — Jerarquia de Diagramas

- **Principio de jerarquia de detalle:** cuando OPD se vuelve dificil de comprender por exceso de detalle → crear OPD descendiente.
- SD = raiz del arbol OPD (nivel 0).
- SD1 = primer descendiente del SD (nivel 1).
- Cada in-zoom o unfolding genera nuevo OPD hijo.
- **Trade-off claridad/completitud:** un OPD puede ser claro pero incompleto; otro puede ser completo para una parte especifica.

---

## SD1 — Primer Nivel de Detalle

SD1 refina el SD agregando estructura y comportamiento con mas detalle.

**Refinamiento de procesos en SD1:**
- Proceso sincrono: in-zooming revela subprocesos en orden temporal vertical (de arriba a abajo).
- Proceso asincrono: unfolding con agregacion-participacion (subprocesos sin orden fijo).

**Refinamiento de objetos en SD1:**
- Unfolding revela partes y atributos del objeto.
- Arbol de objeto (OPD Object Tree): objeto raiz + partes + atributos.

**Expresion y supresion de estados:**
- SD suprime estados del objeto para simplificar → usa Effect Link.
- SD1 expresa estados → usa Input/Output Link Pair con subprocesos especificos.
- Pseudoestado `...` en SD indica estados suprimidos presentes en SD1.

---

## In-Zooming vs Unfolding

| Mecanismo | Aplica a | Semantica adicional | Resultado |
|-----------|----------|---------------------|-----------|
| In-zooming | Procesos sincronos / Objetos | Orden temporal (procesos) u orden espacial (objetos) | Nuevo contexto OPD con timeline |
| Unfolding | Procesos asincronos / Objetos / Cualquier thing | Sin orden implicito | Arbol jerarquico en OPD |
| Folding | Cualquier thing desplegado | Abstraccion / composicion | Colapsa arbol a refinee |

**In-zooming de proceso:** Timeline fluye de arriba hacia abajo dentro del elipse del proceso. Subprocesos se invocan implicitamente por orden vertical.

**In-zooming de objeto:** Posicion espacial de objetos internos tiene significado (disposicion fisica o logica).

**Orden espacial de objetos informaticos:** Se puede especificar orden unidimensional (ej. secciones de articulo cientifico: titulo → resumen → cuerpo).

---

## Alcance del Sistema (Scope)

El SD define el alcance: todo lo que aparece en el SD (y sus descendientes) es parte del modelo.
- **Sistemico:** dentro del limite del sistema (contorno solido).
- **Ambiental:** fuera del sistema pero en el modelo (contorno discontinuo).
- Afiliacion = atributo que especifica si thing es sistemico o ambiental.

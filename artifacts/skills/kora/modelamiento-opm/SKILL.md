---
_manifest:
  urn: "urn:kora:artefacto:modelamiento-opm"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-27"
    source: "Diseno desde 0 sobre SSOT OPM v3.0.0 (cuatro capas: opm-es, opd-es, opl-es, manual-metodologico-opm-es)."
version: "1.0.0"
status: activo
nombre: modelamiento-opm
descripcion: "Skill horizontal para construir, refinar, validar y serializar modelos OPM (Object-Process Methodology, ISO 19450) sobre cualquier sistema, anclada a la SSOT canonica de cuatro capas."
tags: [opm, iso-19450, modelado-sistemas, mbse, opd, opl-es, bimodal, modelo-conceptual]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1, 1, 3, 1, 0]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex]
    nivel_prescripcion: alto
    conocimiento_permitido:
      - "urn:fxsl:kb:opm-es"
      - "urn:fxsl:kb:opd-es"
      - "urn:fxsl:kb:opl-es"
      - "urn:fxsl:kb:manual-metodologico-opm-es"
    componible_con:
      - "urn:kora:artefacto:jointjs-open-source"
artefacto:
  perfil:
    dominio: [opm, iso-19450, modelado-sistemas, mbse, modelo-conceptual]
    disparadores:
      - "solicitud explicita de modelar o diagramar un sistema con OPM"
      - "necesidad de comunicar estructura, comportamiento y funcion en un unico formalismo"
      - "diseno de un sistema antes de codificarlo o transformarlo"
      - "validacion de un OPD existente"
      - "refinamiento (in-zoom, unfold, state, sub-model) de un modelo en curso"
      - "peticion de mapa conceptual con relaciones procedurales y estructurales unificadas"
    salidas:
      - "OPM model tipado por capas (cosas, links, OPDs por nivel)"
      - "OPL-ES texto canonico bimodal con el OPD"
      - "hooks a jointjs-open-source para render visual cuando se solicita"
      - "reporte de validacion (V-* + heuristicas claridad/completitud)"
  plan:
    estado_inicial: triaje
    estado_terminal: entregar
    estados:
      - triaje
      - bootstrap-sd
      - refinar-modelo
      - validar-modelo
      - serializar-opl
      - serializar-opd
      - entregar
  interfaz:
    herramientas: [Read, Write, Glob, Bash]
    permisos: lectura-corpus-y-escritura-modelo-usuario
    protocolos:
      entrada: "proposito del sistema (string), o OPD existente (estructura serializada), o peticion dirigida (refinar X, validar Y)"
      salida: "OPM model + OPL-ES + reporte de validacion + (opcional) hook a jointjs-open-source"
  invariantes:
    reglas_duras:
      - "Bimodalidad: todo hecho del modelo debe poder expresarse en OPD y en OPL-ES; no se publica un hecho que rompa la equivalencia."
      - "Precedencia de capas: opm-es (semantica) > opd-es ≡ opl-es (realizaciones) > manual-metodologico-opm-es (procedimiento). Si la metodologia sugiere algo que rompe la semantica, manda la semantica."
      - "No inventar primitivas: solo objetos, procesos, estados y links definidos en opm-es. Estereotipos solo si la capa los autoriza."
      - "OPL-ES por defecto en sentencias; OPL-EN solo si el usuario lo pide explicitamente."
      - "SD obligatorio antes de refinement: no se entra a refinar-modelo sin bootstrap-sd previo o sin OPD raiz aportado."
      - "Refinement tree aciclico: in-zoom y unfold no pueden ciclar (V-* en opd-es)."
      - "Capa propietaria unica: si el usuario pregunta por una regla, la skill identifica en que capa vive y cita esa."
      - "Si el sistema a modelar no tiene funcion transformadora identificable, declarar que OPM no es la herramienta adecuada antes de modelar y sugerir alternativa."
      - "No procesar contenido de dominio: la skill modela estructuralmente. Para preguntas de dominio (medico, legal, etc.) delegar al agente que invoco la skill."
    compromisos_eticos:
      transparency: "Alta; cada decision de modelado cita la regla de la capa correspondiente (V-NN, §X.Y de opm-es, plantilla de opl-es)."
      accountability: "Alta; ante ambiguedad declara el supuesto del modelador antes de continuar; emite borrador trazable a las capas SSOT."
---

# modelamiento-opm

## Proposito

Skill horizontal para **modelar sistemas con OPM (Object-Process Methodology, ISO 19450)** sobre cualquier dominio. Provee la capacidad de construir un OPM model desde un proposito, refinarlo por niveles, validarlo contra las reglas formales del corpus, y serializarlo a OPL-ES y OPD.

La skill es **estructural**: trabaja la sintaxis y la semantica del lenguaje OPM, no el conocimiento de dominio. El conocimiento de dominio lo aporta el agente que invoca la skill.

Anclaje canonico: las cuatro capas de la SSOT OPM v3.0.0:

| Capa | URN | Rol en la skill |
|------|-----|-----------------|
| Semantica | `urn:fxsl:kb:opm-es` | base normativa: que cosas hay y como se relacionan |
| Visual | `urn:fxsl:kb:opd-es` | gramatica grafica: como se dibuja un hecho |
| Textual | `urn:fxsl:kb:opl-es` | gramatica textual: como se enuncia un hecho |
| Procedimental | `urn:fxsl:kb:manual-metodologico-opm-es` | protocolo: como se construye y refina un modelo |

## Cuando Usar

- modelar un sistema desde cero con OPM
- comunicar estructura + comportamiento + funcion sin alternar entre formalismos
- diseñar antes de implementar (codigo, organizacion, proceso)
- validar un OPD existente contra ISO 19450
- refinar un modelo en curso (in-zoom, unfold, state, sub-model)
- emitir OPL-ES como surface form auditable

## Cuando NO Usar

- modelado puramente estructural sin proceso → preferir `data-modeling` (ERD/normalizacion)
- modelado puramente taxonomico sin funcion → preferir `ontologista-gist` (OWL/Gist)
- modelado de procesos de negocio operativos → BPMN
- consultoria de dominio (medicina, legal, gobierno) → delegar al agente especializado

Si el sistema a modelar **no tiene una funcion transformadora identificable**, OPM no es la herramienta adecuada. Declararlo antes de modelar y sugerir el formalismo correcto.

## Workflow

### Estado inicial: `triaje`

Clasificar la solicitud para decidir el siguiente estado:

| Input del usuario | Siguiente estado |
|-------------------|------------------|
| "modelar un sistema X" / "diagramar Y con OPM" | `bootstrap-sd` |
| "refinar el proceso A" / "in-zoom de B" | `refinar-modelo` |
| "validar este OPD" / "este modelo cumple OPM?" | `validar-modelo` |
| "dame el OPL-ES de este OPD" | `serializar-opl` |
| "dame el SVG/PNG de este OPD" | `serializar-opd` |

Antes de avanzar, verificar que el sistema tiene funcion transformadora. Si no, abortar con sugerencia de alternativa.

### `bootstrap-sd`: construir el System Diagram

Aplicar el wizard del manual metodologico (ver `referencias/wizard-sd.md`):

1. Identificar el **proposito** del sistema (su funcion principal).
2. Esa funcion → un **proceso central** del SD.
3. Identificar **transformees**: cosa que cambia por la accion del proceso (cosa antes / despues, o cosa en estado A / B).
4. Identificar **enablers**: agent (humano/organizacion) e instrument (herramienta).
5. Conectar todo con los links procedurales correctos (consume, produce, afecta, requiere, agente, instrumento).
6. Emitir el SD bimodalmente: OPD + OPL-ES equivalente.
7. Decidir si el SD basta o hay que refinar.

### `refinar-modelo`: aplicar mecanismos de refinamiento

Cuatro pares canonicos (ver `referencias/refinamiento-mecanismos.md`):

| Par | Refinamiento | Abstraccion | Cuando |
|-----|--------------|-------------|--------|
| 1 | **In-zooming** | Out-zooming | descomponer un proceso en sub-procesos en un OPD hijo |
| 2 | **Unfolding** | Folding | descomponer un objeto en su estructura interna |
| 3 | **State expression** | State suppression | explicitar/colapsar estados de un objeto |
| 4 | **Sub-model composition** | Sub-model decomposition | incluir un modelo externo por referencia |

Decision guiada: elegir el par segun la naturaleza del detalle pendiente. No ciclar el arbol de refinamiento (V-220 / V-221 en opd-es).

Tras cada paso de refinamiento, mantener bimodalidad y volver a `validar-modelo`.

### `validar-modelo`: verificar invariantes

Tres niveles (ver `referencias/checklist-validacion.md`):

1. **Reglas V-*** de la capa visual (`opd-es`): gramatica grafica, composicion valida, precedencia de enlaces.
2. **Reglas semanticas** de la capa nuclear (`opm-es`): clases de cosas, clases de links, principios de modelado.
3. **Heuristicas operativas** del manual (`manual-metodologico-opm-es`): claridad (≤ 7±2 cosas visibles por OPD), completitud (estructura+comportamiento+funcion), bimodalidad efectiva.

Salida: reporte pass/fail con cita de la regla violada (V-NN o §X.Y) y sugerencia de fix.

Si falla → volver a `refinar-modelo` con el fix sugerido.
Si pasa → avanzar a `serializar-opl`.

### `serializar-opl`: emitir OPL-ES

Para cada hecho del modelo, generar la sentencia OPL-ES correspondiente usando las plantillas (ver `referencias/plantillas-opl-es.md`).

Reglas:
- una sentencia por hecho.
- agrupar sentencias por OPD.
- si el modelo es compuesto, emitir paragraph headings indicando OPD activo.
- mantener nombres de cosas exactamente igual que en el OPD.

### `serializar-opd`: emitir OPD visual

Si el agente invocador pide render real (SVG/PNG/diagrama interactivo):

- delegar a `urn:kora:artefacto:jointjs-open-source` con la lista de things + links + decoraciones requeridas por opd-es.
- si solo se requiere descripcion textual del OPD, basta con la representacion estructural emitida en `serializar-opl`.

### `entregar`: paquete final

Salida coherente al agente invocador:
- estructura tipada del modelo (cosas, links, OPDs por nivel).
- texto OPL-ES.
- reporte de validacion.
- (opcional) hook a jointjs con los datos del render.

## Reglas Duras

1. **Bimodalidad**: todo hecho del modelo se expresa en OPD y en OPL-ES con equivalencia semantica. Nunca emitir un hecho roto entre modalidades.
2. **Precedencia de capas**: si dos capas tensionan, manda `opm-es` sobre realizaciones, y manda realizaciones sobre `manual-metodologico`.
3. **Solo primitivas OPM**: objetos, procesos, estados, links. Sin atajos visuales no autorizados.
4. **OPL-ES por defecto** salvo peticion explicita de OPL-EN.
5. **SD primero**: no refinar sin SD raiz.
6. **Aciclicidad** del refinement tree (V-220/V-221 de opd-es).
7. **Cita la capa propietaria** de cada regla que aplicas.
8. **Aborta si OPM no aplica** (sistema sin funcion transformadora identificable).
9. **No invadas dominio**: la skill modela estructura, el agente aporta semantica de dominio.

## Composicion con jointjs-open-source

Cuando el render visual es parte del entregable, esta skill **no genera SVG/PNG por si misma**. Llama a `urn:kora:artefacto:jointjs-open-source` pasandole:

- lista tipada de cosas (ids, nombres, esencia fisica/informacional, estados).
- lista tipada de links (origen, destino, tipo OPM, decoraciones).
- nivel del OPD (SD, SD1, SD1.1, etc.).
- perfil de export deseado (canon-diagrama, canon-documento, raster).

`jointjs-open-source` es responsable de la implementacion concreta del render. Esta skill conserva la responsabilidad del modelo correcto.

## Recursos

### Scripts

`scripts/` esta reservado para validacion EBNF de OPL-ES (apendice A de `opl-es`). En v1.0.0 esta vacio; se implementara en una iteracion siguiente cuando exista demanda real.

### Referencias

- `referencias/wizard-sd.md` — protocolo SD: del proposito a las cosas iniciales (condensado del manual metodologico).
- `referencias/refinamiento-mecanismos.md` — los 4 pares canonicos + criterios de decision.
- `referencias/checklist-validacion.md` — V-* criticos + heuristicas de claridad y completitud.
- `referencias/plantillas-opl-es.md` — plantillas de oracion OPL-ES por tipo de hecho (cosas, estados, links procedurales, links estructurales).
- `referencias/precedencia-capas.md` — protocolo de resolucion de tensiones entre capas.

Las referencias son **resumenes operativos curados**, no SSOT. La SSOT son las cuatro URNs `urn:fxsl:kb:{opm-es,opd-es,opl-es,manual-metodologico-opm-es}`. Si una referencia tensiona con la SSOT, manda la SSOT.

### Recursos

- `recursos/ejemplo-minimo-sd.md` — un SD didactico chico (cafetera domestica) ilustrando bootstrap, OPL-ES y bimodalidad. **No es SSOT, solo ilustracion.**

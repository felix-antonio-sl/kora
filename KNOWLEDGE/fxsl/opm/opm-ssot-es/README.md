# Corpus OPM ES — Mapa editorial

Este directorio forma parte del corpus OPM en español. La propiedad editorial de cada capa queda fijada así:

- `opm-iso-19450-es.md`: capa semántica y ontológica canónica. Define elementos, relaciones, principios, conformidad e invariantes de significado.
- `opm-visual-es.md`: capa gráfica canónica. Define símbolos, composición visual, distribución de enlaces, precedencia y comportamiento representacional de los OPDs.
- `metodologia-opm-es.md`: capa metodológica canónica. Define el procedimiento para construir y refinar modelos, criterios de decisión, heurísticas, gobernanza y operación en herramienta.
- `opm-opl-es.md`: capa textual canónica. Define la superficie OPL-ES, plantillas de oración y reglas de equivalencia de ida y vuelta EN↔ES.

Ubicación de referencia:

- La EBNF completa de OPL-ES vive en `opm-opl-es.md`, `Apéndice A`.

Regla de precedencia:

1. Semántica base: `opm-iso-19450-es.md`
2. Realización textual: `opm-opl-es.md`
3. Realización gráfica: `opm-visual-es.md`
4. Procedimiento y praxis: `metodologia-opm-es.md`

Regla editorial:

- una regla debe vivir una sola vez en su capa propietaria;
- los demás documentos pueden referenciarla, pero no duplicarla ni reformularla como si fuera propia;
- se admiten índices, listas de verificación o matrices compiladas fuera de la capa propietaria solo si se presentan explícitamente como compilación operativa y cada entrada declara su fuente canónica;
- cuando una regla visual re-expone semántica ISO, la regla V-* lleva una marca `[Semántica heredada de ...]` que indica la fuente canónica;
- OPCloud y demás herramientas pueden añadir operación, pero no redefinir la semántica del corpus;
- las extensiones no-ISO llevan marca explícita `[Extensión OPCloud]` o `[Extensión no-ISO]`.

Política terminológica:

- en la prosa española del corpus se prefiere `modelado` frente a `modelamiento`;
- para `path` se prefiere `ruta` frente a `camino`, salvo en expresiones asentadas fuera del dominio OPM como `camino crítico`;
- para `tag` se prefiere `etiqueta`;
- se prefiere `por defecto` frente a `default`;
- los términos ingleses se reservan para tablas de equivalencia, citas de interfaz, glosarios de mapeo o nombres oficiales;
- el URN histórico de la metodología conserva `modelamiento` por estabilidad, pero no fija la forma preferida en la prosa del corpus.

Nota sobre URN de la metodología:

- El URN canónico de la metodología es `urn:fxsl:kb:metodologia-modelamiento-opm` (sin sufijo `-es`). Esto difiere de la convención de los otros tres documentos (`*-es`). Se conserva por estabilidad de referencias cruzadas. El idioma se indica en el campo `lang: es` del manifiesto.

# Corpus OPM ES — Mapa editorial

Este directorio forma parte del corpus OPM en español. La propiedad editorial de cada capa queda fijada así:

- `opm-iso-19450-es.md`: capa semántica y ontológica canónica. Define elementos, relaciones, principios, conformidad e invariantes de significado.
- `opm-visual-es.md`: capa gráfica canónica. Define símbolos, composición visual, distribución de enlaces, precedencia y comportamiento representacional de los OPDs.
- `metodologia-opm-es.md`: capa metodológica canónica. Define el procedimiento para construir y refinar modelos, criterios de decisión, heurísticas, gobernanza y operación en herramienta.
- `opm-opl-es.md`: capa textual canónica. Define la superficie OPL-ES, plantillas de oración y reglas de roundtrip EN↔ES.

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
- OPCloud y demás herramientas pueden añadir operación, pero no redefinir la semántica del corpus.

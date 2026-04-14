# Corpus OPM ES — Arquitectura editorial

Este directorio reúne una adaptación canónica en español de OPM. La arquitectura del corpus separa con claridad el núcleo conceptual, la superficie textual OPL, la gramática visual del OPD y el manual metodológico.

Capas del corpus:

- `opm-es.md`: núcleo conceptual de OPM. El nombre de archivo se conserva por compatibilidad, pero su función editorial es la capa base semántica del corpus.
- `opm-opl-es.md`: capa textual canónica. Define OPL-ES, su gramática y sus plantillas de oración.
- `opm-visual-es.md`: capa gráfica canónica. Define la gramática visual del OPD, su composición y sus restricciones.
- `metodologia-opm-es.md`: manual metodológico. Define el procedimiento de modelado, las heurísticas, las validaciones y los patrones de operación.

Identidades canónicas:

- `urn:fxsl:kb:opm-es`
- `urn:fxsl:kb:opl-es`
- `urn:fxsl:kb:opd-es`
- `urn:fxsl:kb:manual-metodologico-opm-es`

Regla de precedencia:

1. Base semántica: `opm-es.md`
2. Realización textual: `opm-opl-es.md`
3. Realización gráfica: `opm-visual-es.md`
4. Procedimiento y praxis: `metodologia-opm-es.md`

Reglas editoriales:

- una regla debe vivir una sola vez en su capa propietaria;
- las demás capas pueden referenciarla o resumirla, pero no redefinirla;
- las compilaciones operativas deben identificar la capa propietaria de cada regla;
- los patrones de herramienta pueden ampliar la operación práctica, pero no alterar la semántica base;
- la prosa del corpus integra el conocimiento como parte del sistema documental y evita citar procedencias externas dentro del cuerpo normativo.

Política terminológica:

- en la prosa española del corpus se prefiere `modelado` frente a `modelamiento`;
- para `path` se prefiere `ruta` frente a `camino`, salvo expresiones asentadas fuera del dominio OPM como `camino crítico`;
- para `tag` se prefiere `etiqueta`;
- se prefiere `por defecto` frente a `default`;
- los términos ingleses se reservan para tablas de equivalencia, glosarios de mapeo o nombres de interfaz cuando realmente ayudan a la interoperabilidad.

Nota de compatibilidad:

- los nombres de archivo históricos se preservan para no romper referencias derivadas del repositorio;
- la identidad editorial vigente del corpus es la definida por las capas y URNs listados arriba.

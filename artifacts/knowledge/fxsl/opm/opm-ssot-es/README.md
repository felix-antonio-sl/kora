# Corpus OPM-ES — SSOT v3.0.0

Adaptación canónica en español de **Object-Process Methodology (OPM)** dentro de KORA.

A partir del `2026-04-27`, el corpus está consolidado en **cuatro capas**, cada una con una URN propia y una responsabilidad única. Las cuatro capas son la única fuente de verdad (SSOT) para semántica, sintaxis y procedimiento OPM en este repositorio.

## Capas canónicas

| # | Archivo | URN | Responsabilidad |
|---|---------|-----|-----------------|
| 1 | `opm-iso-19450-es.md` | `urn:fxsl:kb:opm-es` | Capa **semántica** y ontológica: definiciones, clases de elementos y relaciones, principios de modelado, ejemplos normativos. |
| 2 | `opm-visual-es.md` | `urn:fxsl:kb:opd-es` | Capa **gráfica**: gramática visual del OPD (símbolos, contornos, decoraciones, composición visual, precedencia). |
| 3 | `opm-opl-es.md` | `urn:fxsl:kb:opl-es` | Capa **textual**: gramática OPL-ES, plantillas de oración, EBNF, reglas EN→ES y notas de roundtrip. |
| 4 | `metodologia-opm-es.md` | `urn:fxsl:kb:manual-metodologico-opm-es` | Capa **procedimental**: protocolo de modelado, wizard SD, refinamiento, complejidad, simulación, requirements e invariantes. |

Estado editorial: `published`, `version: 3.0.0`.

## Regla de precedencia

Cuando dos capas parezcan tensionarse, prevalece la más fundamental:

1. **Semántica** (`opm-es`) — base ontológica. Manda en cualquier conflicto sobre qué *son* las cosas.
2. **Visual** (`opd-es`) — realización gráfica. No puede contradecir la semántica.
3. **Textual** (`opl-es`) — realización textual. No puede contradecir la semántica.
4. **Procedimental** (`manual-metodologico-opm-es`) — protocolo de uso. Integra las tres anteriores; nunca las redefine.

Las capas visual y textual son **realizaciones equivalentes** de la semántica: cada hecho del modelo es expresable en ambas modalidades sin pérdida.

## Reglas editoriales

- Cada regla vive una sola vez en su capa propietaria.
- Las demás capas pueden referenciarla o resumirla, pero nunca redefinirla.
- Las compilaciones operativas deben identificar la capa propietaria de cada regla.
- Los patrones de herramienta (OPCloud, etc.) pueden ampliar la operación práctica, pero no alterar la semántica base.
- La prosa del corpus integra el conocimiento como parte del sistema documental y evita citar procedencias externas dentro del cuerpo normativo.

## Política terminológica

- En la prosa española se prefiere `modelado` frente a `modelamiento`.
- Para `path` se prefiere `ruta`; `camino` queda reservado a expresiones asentadas como `camino crítico`.
- Para `tag` se prefiere `etiqueta`.
- Se prefiere `por defecto` frente a `default`.
- Los términos ingleses se reservan para tablas de equivalencia, glosarios de mapeo o nombres de interfaz cuando ayudan a la interoperabilidad.
- `lang: en` indica surface form cercana a ISO/OPCloud; `lang: es` indica prosa o especificación orientada a español.
- `OPL-ES` gobierna sólo la realización textual en español; no altera ontología ni semántica.
- `OPCloud` operacionaliza el modelado pero no redefine el lenguaje OPM.

## Rutas de lectura recomendadas

| Necesito… | Empieza por |
|-----------|-------------|
| Entender OPM desde cero | `opm-iso-19450-es.md` → `opm-visual-es.md` → `opm-opl-es.md` |
| Modelar un sistema en la práctica | `metodologia-opm-es.md` (referenciando las otras tres según haga falta) |
| Implementar OPL-ES en una herramienta | `opm-opl-es.md` → `opm-iso-19450-es.md` |
| Construir o validar un OPD | `opm-visual-es.md` → `metodologia-opm-es.md` |
| Refinar modelos complejos | `metodologia-opm-es.md` (sección de complejidad) |

## Historia

- **v3.0.0 (2026-04-27)** — Consolidación canónica. Las cuatro capas pasan de `draft-publishable` a `published`. La línea `ssot/` legacy queda removida del repositorio. Las URNs canónicas son las cuatro listadas arriba.
- v2.x-ampliada (2026-04-14) — Versión de trabajo con capa visual ya separada.
- v1 (anterior) — Tres capas (semántica, textual, metodológica) sin separación visual explícita. Reemplazada.

## Identidades canónicas

```
urn:fxsl:kb:opm-es
urn:fxsl:kb:opd-es
urn:fxsl:kb:opl-es
urn:fxsl:kb:manual-metodologico-opm-es
```

Cualquier consumidor (skill, agente, knowledge) que necesite citar OPM debe hacerlo a través de estas cuatro URNs.

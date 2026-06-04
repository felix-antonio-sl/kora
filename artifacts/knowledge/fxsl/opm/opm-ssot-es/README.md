# Corpus OPM/Forja-ES

Adaptación canónica en español de **Object-Process Methodology (OPM)** dentro de KORA y familia operativa **Forja** para opforja/deep-opm-pro.

A partir del `2026-06-04`, este directorio contiene dos niveles coordinados:

1. **Capas base OPM**: semántica, OPD, OPL y método tool-agnostic.
2. **Familia Forja**: canon operativo para opforja/deep-opm-pro, con reglas estrictas, método, specs OPD/OPL, puente formal y manual operativo.

Las capas base siguen siendo procedencia OPM general. La familia Forja es la fuente operativa primaria cuando se modela, implementa, valida o enseña opforja.

## Capas base OPM

| # | Archivo | URN | Responsabilidad |
|---|---------|-----|-----------------|
| 1 | `opm-iso-19450-es.md` | `urn:fxsl:kb:opm-es` | Capa **semántica** y ontológica: definiciones, clases de elementos y relaciones, principios de modelado, ejemplos normativos. |
| 2 | `opm-visual-es.md` | `urn:fxsl:kb:opd-es` | Capa **gráfica**: gramática visual del OPD (símbolos, contornos, decoraciones, composición visual, precedencia). |
| 3 | `opm-opl-es.md` | `urn:fxsl:kb:opl-es` | Capa **textual**: gramática OPL-ES, plantillas de oración, EBNF, reglas EN→ES y notas de roundtrip. |
| 4 | `metodologia-opm-es.md` | `urn:fxsl:kb:manual-metodologico-opm-es` | Capa **procedimental base**: protocolo de modelado, wizard SD, refinamiento, complejidad, simulación, requirements e invariantes. |

Estado editorial base: `published`, `version: 3.0.0`.

## Familia Forja

| Archivo | URN | Responsabilidad |
|---|---|---|
| `reglas-opm-estrictas-es.md` | `urn:fxsl:kb:reglas-opm-estrictas-es` | SSOT primaria prescriptiva: validez, severidad, defaults, extensiones declaradas, políticas de herramienta y gates. |
| `metodologia-forja-es.md` | `urn:fxsl:kb:metodologia-forja-opm-es` | Método de modelamiento OPM en opforja: A0-A8, heurísticas, lecciones Forja y bundle. |
| `spec-forja-opd-es.md` | `urn:fxsl:kb:spec-forja-opd-es` | Realización visual/OPD de opforja: glifos, canvas, layout, interacción, export y validación visual. |
| `spec-forja-opl-es.md` | `urn:fxsl:kb:spec-forja-opl-es` | Realización textual/OPL de opforja: vocabulario, plantillas, parser, edición, roundtrip y GAPs. |
| `opm-categorial-es.md` | `urn:fxsl:kb:opm-categorial-es` | Puente formal ICAS-BoK: equivalencia, composición, eje vertical y leyes bajo la superficie. |
| `manual-opforja-es.md` + `manual-opforja-es--p02.md` | `urn:fxsl:kb:manual-opforja-es` | Manual operativo para modeladores, agentes y mantenedores; enseña uso sin duplicar specs. |

## Regla de precedencia operativa

Cuando dos capas parezcan tensionarse en opforja, primero identificar el plano:

1. **Validez**: manda `reglas-opm-estrictas-es`.
2. **Método**: manda `metodologia-forja-es`, sin autorizar hechos que reglas prohíbe.
3. **Visual OPD**: manda `spec-forja-opd-es`, bajo reglas.
4. **Textual OPL**: manda `spec-forja-opl-es`, bajo reglas.
5. **Formal**: `opm-categorial-es` explica; no introduce vocabulario operativo.
6. **Enseñanza/uso**: `manual-opforja-es` orienta; no legisla.

Las capas base se consultan como procedencia y soporte cuando la familia Forja las delega. Ningún detalle de herramienta redefine semántica OPM por sí solo.

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
| Usar opforja como modelador | `manual-opforja-es.md` → `metodologia-forja-es.md` |
| Implementar opforja | `reglas-opm-estrictas-es.md` → `spec-forja-opd-es.md` / `spec-forja-opl-es.md` |
| Auditar un modelo opforja | `reglas-opm-estrictas-es.md` → `manual-opforja-es.md` → specs modales según el fallo |

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
urn:fxsl:kb:reglas-opm-estrictas-es
urn:fxsl:kb:metodologia-forja-opm-es
urn:fxsl:kb:spec-forja-opd-es
urn:fxsl:kb:spec-forja-opl-es
urn:fxsl:kb:opm-categorial-es
urn:fxsl:kb:manual-opforja-es
```

Cualquier consumidor (skill, agente, knowledge) que necesite citar OPM base debe hacerlo a través de las cuatro URNs base. Cualquier consumidor que opere opforja debe citar la URN propietaria de la familia Forja correspondiente.

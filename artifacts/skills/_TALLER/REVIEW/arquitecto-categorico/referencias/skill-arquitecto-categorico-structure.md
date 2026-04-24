# Estructura de la skill `arquitecto-categorico`

Documento de diseno actualizado para la topologia KORA v5. Sustituye la nota
legacy que describia `SKILLS/` y `KNOWLEDGE/`; esas rutas quedan solo como
contexto historico.

## Decision de forma

`arquitecto-categorico` vive como habilidad portable en staging:

```text
artifacts/skills/_TALLER/REVIEW/arquitecto-categorico/
  SKILL.md
  referencias/
    icas-bok-indice.md
    axiomas-por-parte.md
    skill-arquitecto-categorico-structure.md
    skill-arquitecto-categorico-spec.md
```

Si se promueve, el destino productivo esperado es:

```text
artifacts/skills/kora/arquitecto-categorico/
  SKILL.md
  referencias/
    ...
```

La forma material declarada es `habilidad`. Por tanto aplica
`serialization/autoria-spec.md §5.1`: `SKILL.md` como entrypoint, subdirectorios
canonicos `scripts/`, `referencias/`, `recursos/`, progressive disclosure y
transmutacion fiel a agentskills.io cuando corresponda.

## Decision de corpus

El corpus ICAS-BoK no se duplica dentro de la skill. La fuente primaria vive en:

```text
artifacts/knowledge/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/
```

La skill referencia ese corpus por URN mediante `conocimiento_permitido` e
`icas-bok-indice.md`. Esta decision evita drift: el contenido matematico vive
una sola vez y la skill solo mantiene el indice operativo de carga bajo demanda.

## Trazabilidad formal

KORA distingue dos niveles:

| Uso | Fuente |
|-----|--------|
| `Traces to:` normativo | Formal Layer oficial en `artifacts/knowledge/kora/categorical-foundations/` (`urn:kora:kb:cat-*`) |
| `Rationale:` o apoyo editorial | Corpus ICAS/FXSL (`urn:fxsl:kb:icas-*`) |

Regla: una recomendacion categorial normativa debe trazar primero a la Formal
Layer oficial cuando el concepto ya fue absorbido. El corpus ICAS/FXSL puede
acompanar como rationale, ejemplo o ampliacion.

## Progressive Disclosure

El `SKILL.md` mantiene el procedimiento y los invariantes en menos de 500 lineas.
Las referencias largas quedan en `referencias/` y el corpus completo se consulta
solo cuando el modo de operacion lo necesita:

- `model`: fundamentos, composicion, identidad, universales.
- `audit`: preservacion, comparacion, audit invariants, behavioral preservation.
- `migrate`: preservacion, adjunciones, transmutation.
- `compose`: composicion avanzada, efectos, escala, multiagente.
- `formalize`: patrones, universales, bridge FXSL -> KORA.

## Riesgos y controles

| Riesgo | Control |
|--------|---------|
| Cargar todo el corpus ICAS en cada activacion | Usar `icas-bok-indice.md` y leer solo los documentos relevantes |
| Confundir FXSL auxiliar con Formal Layer oficial | Mantener `Traces to:` reservado a `urn:kora:kb:cat-*` |
| Drift de rutas legacy | No usar `SKILLS/`, `AGENTS/`, `KNOWLEDGE/` como topologia vigente |
| Referencias incompletas a ICAS | Mantener los 24 URNs en `conocimiento_permitido` e indice operativo |

## Criterio de promocion

Antes de mover la skill a productivo:

1. `python3 toolchain/kora index`
2. `python3 toolchain/kora check --strict`
3. validar que todos los URNs de `conocimiento_permitido` resuelven
4. validar que no hay `Traces to:` hacia `urn:fxsl:*`
5. confirmar que `## Recursos` documenta cada subdirectorio presente

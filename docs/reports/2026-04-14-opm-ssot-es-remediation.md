---
_manifest:
  urn: "urn:kora:doc:opm-ssot-es-remediation-2026-04-14"
  provenance:
    created_by: "kora/forgemaster"
    created_at: "2026-04-14"
    source: "auditoría interna cruzada del corpus KNOWLEDGE/fxsl/opm/opm-ssot-es y remediación directa de inconsistencias"
version: "1.0.0"
status: published
tags: [report, remediation, opm, ssot, editorial, grammar, consistency]
lang: es
extensions: {}
---

# Remediación del corpus OPM ES SSOT (2026-04-14)

## Contexto

Se ejecutó una auditoría interna, cruzada y descarnada sobre:

- `KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-iso-19450-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-visual-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/metodologia-opm-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-opl-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/README.md`

El objetivo fue reducir contradicciones semánticas, inconsistencias terminológicas y roturas formales que debilitaban el carácter SSOT del corpus.

## Hallazgos de entrada

Los hallazgos que motivaron la remediación fueron:

1. contradicción entre la ontología de proceso en ISO, la regla visual de proceso transformador y la heurística metodológica sobre procesos persistentes;
2. definición semántica demasiado estrecha del enlace de resultado en la capa ISO;
3. referencias internas rotas en metodología;
4. conflicto entre "un nombre por cosa" y la admisión de variantes de superficie en OPL-ES;
5. EBNF de OPL-ES anunciada como completa pero no cerrada ni internamente consistente;
6. deriva editorial menor en español técnico y puntuación normativa.

## Cambios aplicados

### 1. Ontología y semántica base

- Se ajustó la formulación de **procesos persistentes** en `opm-iso-19450-es.md` para tratarlos como caso límite válido y no como patrón general que destruya la definición de proceso.
- Se suavizó `V-115` en `opm-visual-es.md` para que la exigencia de transformación sea la regla general, con excepción explícita para procesos persistentes reconocidos por la capa ISO.
- Se amplió la definición de **enlace de resultado** en `opm-iso-19450-es.md` para cubrir tanto resultado simple como resultado con estado especificado.

### 2. Metodología

- Se eliminó la referencia errónea a `§4.4` para la colisión de roles y se reemplazó por una formulación basada en la precedencia semántica del corpus.
- Se corrigieron formulaciones que afirmaban indebidamente que los procesos de mantenimiento de estado "violan" la definición de proceso.
- Se precisó la política de **nombre canónico interno** frente a variantes superficiales permitidas por OPL-ES.
- Se unificó la convención de rangos en atributos y validación computacional.
- Se limpió parte del ruido editorial obvio (`vía`, `cálculo`, `fórmula`, etc.).

### 3. OPL-ES y EBNF

- Se relajó la regla de "máximo 4 palabras" para nombres de proceso: ahora es preferencia, no restricción dura incompatible con los ejemplos del propio corpus.
- Se aclaró que OPL-ES puede introducir no terminales auxiliares propios mientras preserve equivalencia semántica.
- Se cerró la EBNF con aliases y no terminales faltantes, incluyendo:
  - identificadores auxiliares;
  - listas de objetos, procesos, atributos y estados;
  - wrappers ausentes para descripción de cosa, evento, excepción y oraciones de cambio;
  - no terminales estructurales bidireccionales de proceso.
- Se unificó `restriccion_de_participacion` y se corrigió la inconsistencia de puntuación en condiciones habilitadoras.
- Se arreglaron varias líneas normativas de roundtrip y política de modelos mixtos.

## Criterio de cierre

La remediación de esta ronda se consideró suficiente si:

- desaparecían las contradicciones ontológicas más fuertes entre ISO, visual y metodología;
- la EBNF dejaba de tener no terminales críticos colgantes;
- la política de nombres quedaba explícitamente centrada en el nombre canónico interno del modelo;
- el reporte histórico dejaba trazabilidad de la operación.

## Verificación

### Revisión puntual

Se verificó manualmente:

- diff de los cuatro documentos modificados del corpus;
- consistencia de referencias reparadas;
- presencia/definición de no terminales críticos en la EBNF;
- eliminación de las contradicciones más severas detectadas en la auditoría.

### Validación de repo

Se ejecutó:

```bash
python3 scripts/kora validate --profile strict
```

Resultado: `FAIL`, pero por problemas ajenos al corpus OPM ES:

- workspaces incompletos bajo `AGENTS/OMEGA/*`;
- un `SKILL.md` con frontmatter inválido en `AGENTS/kora/clawforge/skills/CM-OPENCLAW-LIFECYCLE-MANAGER/SKILL.md`.

No apareció un fallo nuevo atribuible directamente a `KNOWLEDGE/fxsl/opm/opm-ssot-es`.

## Riesgo residual

Queda trabajo pendiente de segunda ronda en:

- castellanización más agresiva de anglicismos operativos en metodología y visual;
- reducción adicional de duplicación editorial residual entre capas;
- depuración más profunda de la EBNF para convertirla en especificación parseable con tooling formal, no solo internamente cerrada a nivel textual;
- normalización ortográfica completa de todo el corpus OPM ES.

## Artefactos modificados

- `KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-iso-19450-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-visual-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/metodologia-opm-es.md`
- `KNOWLEDGE/fxsl/opm/opm-ssot-es/opm-opl-es.md`
- `docs/reports/2026-04-14-opm-ssot-es-remediation.md`

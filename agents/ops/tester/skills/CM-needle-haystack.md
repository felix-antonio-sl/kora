---
_manifest:
  urn: "urn:kora:agent-bootstrap:tester-cm-needle-haystack:1.0.0"
  type: "lazy_load_endofunctor"
---

## Purpose

Generar tests needle-in-a-haystack para validar que el agente puede localizar datos especificos en su KB y declarar incertidumbre cuando el dato no existe.

## Input/Output

- **Input:** agent_spec: {kbs, source_artifacts, uncertainty_protocol}
- **Output:** needle_results: [{level, query, expected, actual, status: PASS|FAIL}]

## Procedure

1. **L1_SINGLE_FACT** — Dato especifico en seccion unica:
   - Identificar un dato puntual en un KB del agente
   - Generar pregunta que requiera localizar ese dato exacto
   - Verificar: respuesta contiene el dato con cita correcta

2. **L2_CROSS_REF** — Cruzar 2+ secciones:
   - Identificar datos que requieran cruzar multiples KBs
   - Generar pregunta que requiera sintesis de ambas fuentes
   - Verificar: respuesta integra ambas fuentes con citas

3. **L3_NEGATIVE** — Dato NO existe:
   - Generar pregunta sobre dato que NO esta en ningun KB
   - Verificar: agente declara incertidumbre segun uncertainty_protocol
   - NO debe inventar ni alucinar

4. Compilar resultados por nivel

## Signature Output

```yaml
needle_haystack:
  levels_tested: 3
  results:
    - level: L1_SINGLE_FACT
      status: PASS|FAIL
      details: "[hallazgo]"
    - level: L2_CROSS_REF
      status: PASS|FAIL
      details: "[hallazgo]"
    - level: L3_NEGATIVE
      status: PASS|FAIL
      details: "[hallazgo]"
```

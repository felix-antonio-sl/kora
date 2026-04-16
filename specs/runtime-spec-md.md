---
_manifest:
  urn: "urn:kora:kb:runtime-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "contrato minimo de runtime para el sistema moderno"
version: "3.6.0"
status: published
tags: [spec, runtime, deployment, equivalence]
lang: es
extensions: {}
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:agentfile-spec"
---

# KORA/Runtime-Spec v3.6.0

## 1. Definicion

`runtime-spec` gobierna solo invariantes runtime: equivalencia observable,
enforcement fuera del prompt, routing, budget y frontera entre fuente y estado
operativo.

No gobierna el IR del agente; eso pertenece a `agentfile-spec`.

## 2. Invariantes runtime

Todo runtime KORA **DEBE** preservar:

1. cierre de safety,
2. interfaz disponible o perdida declarada,
3. separation between source and state,
4. posibilidad de auditar drift.

## 3. Fuente vs estado

La fuente del sistema es el repo. El runtime gestiona estado mutable:

- credenciales,
- sesiones,
- caches,
- volúmenes,
- pairing stores.

Nada de eso debe convertirse en ley canonica del agente.

## 4. Adapters por plataforma

Cada target **DEBE** tener un adapter explicito o una declaracion de ausencia.

El adapter:

1. materializa el agente,
2. declara perdidas,
3. nunca se vuelve fuente de verdad.

## 5. Wrapper generation

Los wrappers son derivados regenerables.

Reglas:

1. un wrapper no es la fuente,
2. un wrapper no debe ocultar policy critica,
3. un wrapper no debe confundirse con un source bundle.

## 6. Platform equivalence

La equivalencia es funcional, no textual.

Se evalua sobre:

- decision de routing,
- cierre de tools,
- enforcement de safety,
- degradaciones declaradas.

## 7. Model routing

El routing de modelo es concern de runtime. El agente puede declarar hints, pero
el runtime aplica la decision final fuera del texto.

## 8. Fallback chains y budget

1. Los budgets se aplican fuera del prompt.
2. Un fallback **PUEDE** degradar calidad.
3. Un fallback **NO DEBE** cambiar dominio o ley.

## 9. Drift

El drift runtime se acepta solo si es:

- observable,
- reconciliable,
- no sustractivo respecto del canon.

## 10. Transmutacion

La transmutacion es la compilacion del `AGENT.md` hacia un target concreto.

Pipeline minimo:

1. resolver agente,
2. parsear IR,
3. validar dimensiones,
4. resolver adapter,
5. emitir artefactos derivados en `BUILD/`,
6. emitir `_transmutation.yml`.

Reglas:

1. el target nunca se vuelve fuente primaria,
2. toda degradacion de fidelidad debe declararse,
3. `_transmutation.yml` es obligatorio,
4. `BUILD/` es regenerable por definicion.

## 11. Validacion

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Policy server-side | Safety no queda delegada al LLM | runtime |
| Wrapper limpio | Derivado no suplanta la fuente | lint/manual |
| Routing visible | Hay decision runtime trazable | runtime/manual |
| Drift auditable | Repo y runtime comparables | manual/lint |
| Registro emitido | La compilacion deja `_transmutation.yml` | lint |

## 12. Migracion

Contrato vigente v3.6.0:

- runtime queda reducido a invariantes runtime,
- absorbe la compilacion concreta del IR,
- el diseño moderno evita reinyectar semantica del agente dentro del runtime.

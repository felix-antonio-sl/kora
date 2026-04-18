---
_manifest:
  urn: "urn:kora:kb:risk-register-spec"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-19"
    source: "Cierra H13 del backlog post-olas: formaliza el risk register como composicion Kleisli sobre el enrichment de calidad fijado por qa-spec."
version: "1.0.0"
status: publicado
tags: [spec, riesgo, kleisli, qa, governance, writer]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:autoria-spec"
  cites:
    - "urn:kora:kb:cat-foundations"
    - "urn:kora:kb:cat-audit-invariants"
    - "urn:kora:kb:cat-behavioral-preservation"
    - "urn:fxsl:kb:icas-calidad-riesgo"
---

# KORA/Risk-Register-Spec v1.0.0

## 1. Definicion

`risk-register-spec` gobierna la representacion y composicion del **riesgo**
en KORA. Su decision central es:

> Un registro de riesgo no es una lista decorativa; es un efecto acumulativo
> que compone como flecha de Kleisli sobre un ledger de riesgos tipado.

Esto permite:

1. identificar riesgos,
2. componer mitigaciones,
3. explicitar riesgo residual,
4. relacionar el riesgo con el piso de calidad fijado por `qa-spec`.

## 2. Semantica Kleisli

### 2.1 Monad canonico

KORA interpreta el registro de riesgo sobre el monad:

```text
Risk_M(X) = X × RiskLedger
```

donde `RiskLedger` es un monoide libre de entradas de riesgo:

```text
RiskLedger = List[RiskEntry]
```

La unidad inserta un estado sin agregar riesgos; la composicion Kleisli concatena
los ledgers y arrastra el riesgo residual hacia la siguiente fase.

### 2.2 Flecha de riesgo

Una evaluacion o mitigacion de riesgo se escribe:

```text
r: A -> Risk_M(B)
```

y se interpreta como:

1. recibe un artefacto, proceso o fase `A`,
2. produce un estado evaluado `B`,
3. agrega cero o mas `RiskEntry` al ledger.

## 3. Entrada de riesgo canonica

| Campo | Definicion |
|-------|------------|
| `risk_id` | Identificador estable dentro del artefacto. |
| `category` | Clase del riesgo (`safety`, `quality`, `cost`, `security`, `compliance`, `operational`, `knowledge`). |
| `source` | Origen observable del riesgo. |
| `trigger` | Condicion de activacion. |
| `likelihood` | Probabilidad o grado de ocurrencia en `[0,1]`. |
| `impact` | Severidad del dano potencial en `[0,1]`. |
| `sigma_exposure` | Vector `[0,1]^5` que expresa donde impacta el riesgo sobre `Σ`. |
| `mitigation` | Control o accion reductora declarada. |
| `residual_sigma_floor` | Piso residual garantizado tras la mitigacion. |
| `owner` | Responsable de aceptar, mitigar o escalar. |
| `status` | `identified`, `mitigated`, `accepted`, `retired`. |

## 4. Regla de composicion

Dados dos pasos:

```text
r1: A -> Risk_M(B)
r2: B -> Risk_M(C)
```

su composicion Kleisli:

```text
r2 >=> r1 : A -> Risk_M(C)
```

produce:

1. union secuencial del ledger,
2. acumulacion de evidencia de mitigacion,
3. un piso residual compuesto conservativamente por `meet` componente a
   componente sobre `residual_sigma_floor`.

Rationale: `qa-spec` reserva `⊗` para compromisos normativos compuestos. En el
registro de riesgo interesa el **peor piso residual garantizado** tras varias
mitigaciones; por eso la agregacion conservativa es `meet = min`.

## 5. Serializacion canonica

La forma recomendada vive en `artefacto.contexto.risk_register`:

```yaml
artefacto:
  contexto:
    risk_register:
      - risk_id: qa-fallback-01
        category: quality
        source: fallback-chain
        trigger: "modelo primario indisponible"
        likelihood: 0.35
        impact: 0.40
        sigma_exposure: [0.0, 0.0, 0.1, 0.2, 0.0]
        mitigation: "forzar fallback con sigma_min intacto"
        residual_sigma_floor: [0.67, 0.33, 0.67, 0.67, 0.33]
        owner: runtime
        status: mitigated
```

## 6. Reglas

1. `risk_register` **PUEDE** omitirse si no hay evaluacion de riesgo
   materializada.
2. Cada `risk_id` **DEBE** ser unico dentro del artefacto.
3. `likelihood` e `impact` **DEBEN** vivir en `[0,1]`.
4. `sigma_exposure` y `residual_sigma_floor` **DEBEN** tener 5 componentes en
   `[0,1]`.
5. Si existe `artefacto.contexto.qa_budget.sigma_min`, un riesgo
   `status=accepted` que caiga por debajo de ese piso **DEBE** declarar
   explicitamente su aceptacion y owner.
6. El registro de riesgo **NO DEBE** reemplazar `compromisos_eticos`; mide
   amenaza y mitigacion, no compromiso normativo.

## 7. Relacion con otras specs

1. `qa-spec` fija la moneda de calidad sobre la que se expresa el riesgo.
2. `autoria-spec` serializa el `risk_register` bajo `artefacto.contexto`.
3. `runtime-spec-md` consume pisos y budgets; el registro de riesgo documenta
   cuando esos pisos son amenazados, aceptados o mitigados.

## 8. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| `risk-entry-shape` | Cada entrada tiene campos minimos y dominios coherentes | manual |
| `risk-id-unique` | No hay `risk_id` repetidos | manual |
| `risk-floor-coherent` | `residual_sigma_floor` no usa forma distinta a `[0,1]^5` | manual |
| `accepted-risk-owned` | Riesgo aceptado tiene `owner` explicito | manual |
| `risk-vs-qa-floor` | Riesgo aceptado bajo `sigma_min` explicita excepcion | manual |

## 9. Migracion

`risk-register-spec v1.0.0` es aditiva.

Reglas de migracion:

1. narrativas previas de riesgo **DEBERIAN** compactarse a la forma canonica;
2. la ausencia de `risk_register` sigue siendo valida;
3. desde esta version, las referencias prospectivas de H13 quedan cerradas:
   `qa-spec` ya no apunta a una deuda futura sino a esta spec vigente.

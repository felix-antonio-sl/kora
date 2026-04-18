---
_manifest:
  urn: "urn:kora:kb:qa-spec"
  provenance:
    created_by: "OpenAI Codex (encarnando arquitecto-categorico)"
    created_at: "2026-04-18"
    source: "Cierre H6 del backlog post-olas: formaliza quality attributes enriquecidos y el puente entre Σ discreto, qa_budget operativo y budgets runtime, alineado con Part VI del ICAS-BoK."
version: "1.0.0"
status: publicado
tags: [spec, quality-attributes, enriched, qa-budget, sigma, risk-ready]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:md-spec"
  cites:
    - "urn:fxsl:kb:icas-enriquecimiento"
    - "urn:fxsl:kb:icas-calidad-riesgo"
    - "urn:fxsl:kb:icas-safety-alignment"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:autoria-spec"
---

# KORA/QA-Spec v1.0.0

## 1. Definicion

`qa-spec` gobierna el contrato semantico de los **quality attributes** en KORA.
Su alcance es ontologico: fija la moneda con la que KORA interpreta compromisos
de calidad, define el puente entre `Σ` discreto y su lectura enriched continua,
y establece como `qa_budget` expresa cotas operativas sin introducir ejes nuevos
en el IR.

Esta spec **NO** redefine `harness-spec`: `Σ` sigue viviendo en
`extensions.kora.vector_ontologico.sigma` como vista discreta de authoring. La
funcion de `qa-spec` es dar la semantica continua que faltaba a esa vista y
ordenar su proyeccion hacia serializacion y runtime.

Decision constitucional de este documento:

> KORA **DEBE** interpretar sus compromisos normativos de calidad sobre la
> categoria enriquecida `([0,1]^5, <=, 1̄, ⊗)` y **NO DEBE** colapsarlos a
> `Bool` o `Cost` como moneda canonica del IR.

Rationale: el corpus ICAS-BoK distingue explicitamente entre `Bool`, `Cost` y
`[0,1]` como monedas de enriquecimiento segun el tipo de relacion cuantitativa
que se quiera modelar. Para KORA, `Σ` ya esta declarado en `harness-spec` como
vector enriched sobre `[0,1]^5`; esta spec materializa esa decision en lugar de
dejarla en prosa incompleta.

## 2. Definiciones

| Termino | Definicion |
|---------|------------|
| Quality attribute | Funtor de medicion desde la categoria del sistema hacia una categoria de medicion; no es un objeto estructural del sistema. |
| `V_QA` | Monoidal preorder canonico de KORA para compromisos de calidad: `([0,1]^5, <=, 1̄, ⊗)`. |
| `Σ` discreto | Vector authoring `sigma ∈ {0,1,2,3}^5` declarado en `harness-spec`. |
| `Σ̃` enriched | Interpretacion continua de `Σ` bajo la inclusion monotona `ιΣ : {0,1,2,3}^5 -> [0,1]^5`. |
| `qa_budget` | Objeto operativo opcional que declara pisos y cotas medibles para runtime, sin alterar el vector ontologico. |
| Piso duro | Umbral minimo que un runtime **NO DEBE** degradar silenciosamente. |
| Budget blando | Cota operativa que un runtime **PUEDE** estrechar por debajo del ideal siempre que no viole el piso duro y declare la perdida. |
| Cambio de base | Proyeccion monoidal desde `V_QA` a otra moneda (`Bool`, `Cost`) para gates o optimizacion local. |

## 3. Enrichment canonico

### 3.1 Moneda canonica

KORA **DEBE** usar la siguiente estructura como moneda canonica de calidad:

```text
V_QA = ([0,1]^5, <=, 1̄, ⊗)

1̄ = [1,1,1,1,1]
[a1,a2,a3,a4,a5] ⊗ [b1,b2,b3,b4,b5] = [a1*b1, a2*b2, a3*b3, a4*b4, a5*b5]
```

El orden es componente a componente y cada posicion corresponde a:

```text
[safety_norm, fairness, transparency, accountability, sustainability]
```

Reglas:

1. Un compromiso de calidad mas alto se interpreta como un valor mayor en
   `V_QA`.
2. La identidad de calidad **DEBE** ser `1̄`: un componente no degrada su propia
   garantia al componer consigo mismo.
3. La composicion secuencial **DEBE** usar `⊗` componente a componente. Si una
   garantia atraviesa varias etapas, la garantia end-to-end se obtiene por
   multiplicacion conservativa de las garantias locales.
4. Los joins y meets operativos **DEBEN** leerse componente a componente:
   `join = max`, `meet = min`.

Correcto: modelar un pipeline con `transparency=[0.9, 0.8]` como una garantia
compuesta `0.72`.
Incorrecto: mezclar `cost_usd_per_turn=0.05` dentro del mismo hom-object que
`accountability=0.8`.
Rationale: `urn:fxsl:kb:icas-enriquecimiento` establece `[0,1]` como moneda
natural para fiabilidad/QoS; `urn:fxsl:kb:icas-calidad-riesgo` separa las
metricas de costo/latencia como categorias de medicion distintas.

### 3.2 Lo que esta decision no hace

Esta spec **NO** afirma que toda metrica de calidad viva en `[0,1]`. Afirma
algo mas acotado:

1. Los **compromisos normativos** de KORA (`Σ`) se interpretan en `[0,1]^5`.
2. Las metricas operativas heterogeneas (`latency`, `cost`, `mttr`, etc.)
   **DEBEN** modelarse como funtores de medicion separados y conectarse por
   cambio de base.
3. `Bool` y `Cost` **PUEDEN** derivarse desde `V_QA`; **NO DEBEN** reemplazarlo
   como moneda canonica del IR.

Rationale: el corpus de enriquecimiento muestra que elegir la moneda correcta
depende del fenomeno cuantitativo. H6 cierra la semantica canonica de KORA, no
niega que existan otras monedas utiles en vistas derivadas.

## 4. Puente entre `Σ` discreto y `Σ̃` enriched

### 4.1 Inclusion monotona canonica

El vector discreto de `harness-spec` **DEBE** interpretarse mediante:

```text
ιΣ(0) = 0
ιΣ(1) = 1/3
ιΣ(2) = 2/3
ιΣ(3) = 1
```

Aplicado componente a componente:

```text
Σ = [2,1,2,2,1]  ->  Σ̃ = [0.67,0.33,0.67,0.67,0.33]
```

Reglas:

1. `harness-spec` **DEBE** seguir serializando `Σ` en la vista discreta
   `{0..3}^5`; esta spec no cambia el shape del IR.
2. Todo razonamiento continuo sobre thresholds, floors o degradacion runtime
   **DEBE** operar sobre `Σ̃ = ιΣ(Σ)`, no sobre enteros crudos.
3. La interpretacion discreta **NO DEBE** perder monotonicidad: si `Σ₁ <= Σ₂`
   componente a componente, entonces `ιΣ(Σ₁) <= ιΣ(Σ₂)`.

Correcto: usar `Σ.accountability = 2` como piso continuo `0.67`.
Incorrecto: tratar `Σ=2` como si significara `2.0` o `20%`.
Rationale: el IR actual necesita seguir siendo ligero para authoring, pero la
semantica de H6 requiere umbrales continuos para budgets y degradaciones.

### 4.2 Piso duro booleano derivado

Cuando un runtime necesite una decision binaria, **DEBE** derivarla por cambio
de base desde `Σ̃`, no desde una interpretacion ad-hoc:

```text
θ_hard(x) = true  sii  x >= 2/3
```

Este threshold convierte el nivel discreto `2` en el primer valor considerado
"duro" o exigible sin calificacion adicional.

Rationale: `urn:fxsl:kb:icas-enriquecimiento` muestra que `Bool` es una vista
derivada natural por threshold; no es necesario inventar un gate paralelo.

## 5. `qa_budget` como objeto operativo

`artefacto.contexto.qa_budget` **PUEDE** declararse para fijar cotas operativas
medibles. Su funcion es serializar budgets y floors observables; no altera el
vector ontologico.

Forma canonica recomendada:

```yaml
artefacto:
  contexto:
    qa_budget:
      sigma_min: [0.67, 0.33, 0.67, 0.67, 0.33]
      latency:
        max_ms: 2000
      availability:
        min: 0.99
        window: "30d"
      mttr:
        max_s: 600
      cost:
        max_usd_per_turn: 0.05
```

Reglas:

1. `qa_budget` **PUEDE** omitirse por completo. Cuando se omite,
   `sigma_min := ιΣ(Σ)` es la interpretacion por defecto.
2. Si `sigma_min` se declara, **DEBE** tener cinco componentes en `[0,1]`.
3. `sigma_min` **NO DEBE** ser componente a componente menor que `ιΣ(Σ)`.
   Puede igualarlo o estrecharlo.
4. Las metricas operativas **DEBEN** declararse con unidad o nombre de unidad en
   la clave (`max_ms`, `max_s`, `max_usd_per_turn`) para evitar ambiguedad.
5. `qa_budget` **NO DEBE** mezclar narrativa abierta con thresholds medibles.
   La narrativa va en `compromisos_eticos`; las cotas van en `qa_budget`.

Correcto: `sigma=[2,1,2,2,1]` y `sigma_min=[0.8,0.4,0.8,0.8,0.4]`.
Incorrecto: `sigma=[2,1,2,2,1]` y `sigma_min=[0.4,0.2,0.4,0.4,0.2]`.
Rationale: `qa_budget` es un tightening operativo del compromiso canonico, no
una via lateral para debilitarlo.

## 6. Cambios de base autorizados

KORA reconoce dos vistas derivadas utiles sobre `V_QA`:

### 6.1 `Bool`

`Bool` **DEBE** usarse para:

1. approval gates,
2. validaciones pass/fail,
3. clauses de "permitido / no permitido".

Su origen canonico es `θ_hard` o thresholds runtime-explicitos sobre componentes
de `Σ̃`.

### 6.2 `Cost`

`Cost` **DEBE** usarse para:

1. latencia,
2. costo monetario,
3. MTTR u otras cotas temporales acumulativas.

Reglas:

1. `Cost` **NO DEBE** reemplazar a `V_QA` como semantica normativa de `Σ`.
2. Un budget de `Cost` **DEBE** vivir en `qa_budget` o en metadata runtime, no
   en `extensions.kora.vector_ontologico`.
3. La conversion entre `V_QA` y `Cost` **DEBE** declararse como cambio de base,
   nunca como identidad semantica.

Rationale: `urn:fxsl:kb:icas-calidad-riesgo` trata performance budget y costo
como measurement categories separadas de reliability/availability; fusionarlas
en el IR canónico destruiria composicionalidad semantica.

## 7. Relacion con otras specs

1. `harness-spec` declara el vector discreto `Σ`; `qa-spec` fija su
   interpretacion continua y su cambio de base autorizado.
2. `autoria-spec` serializa `qa_budget` bajo `artefacto.contexto`.
3. `runtime-spec-md` consume `qa_budget` como cota operacional aplicada fuera
   del prompt.
4. `transmutation-spec` sigue gobernando la perdida por eje; si un runtime no
   puede realizar un piso derivado de `Σ̃`, la perdida **DEBE** declararse como
   degradacion de calidad y no como cambio estructural del IR.
5. `risk-register-spec` materializa H13 sobre la moneda definida aqui; esta
   spec sigue siendo la autoridad sobre el enrichment y los cambios de base.

## 8. Invariantes

1. `Σ` discreto y `Σ̃` enriched describen el mismo compromiso canonico en dos
   resoluciones distintas.
2. `qa_budget` no agrega ejes nuevos; solo expresa floors y budgets sobre el
   compromiso ya declarado.
3. Un runtime puede estrechar budgets; **NO PUEDE** relajar silenciosamente el
   piso duro derivado de `Σ`.
4. `Bool` y `Cost` son vistas derivadas por cambio de base; **NO SON** la
   moneda canonica del IR.
5. Safety estructural sigue siendo derivada de `(Μ, Ξ)`; `Σ.safety_norm` y
   `sigma_min[0]` son compromisos normativos, no pruebas de cierre coalgebraico.

## 9. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| `sigma-enrichment-canonico` | `Σ` se interpreta via `ιΣ` y no por escala ad-hoc | manual |
| `qa-budget-shape` | Si `qa_budget` existe, usa objetos medibles y unidades explicitas | manual |
| `qa-budget-sigma-floor` | `sigma_min >= ιΣ(Σ)` componente a componente | manual |
| `qa-budget-metricas-canonicas` | `latency`, `availability`, `mttr`, `cost` usan comparadores consistentes (`max_*` o `min`) | manual |
| `runtime-no-relaja-floor` | Un runtime declara o rechaza toda degradacion que cruce el piso duro | manual |

## 10. Ejemplos

### 10.1 Artefacto sin `qa_budget`

```yaml
extensions:
  kora:
    vector_ontologico:
      sigma: [2,1,2,2,1]
```

Interpretacion:

```text
Σ̃ = [0.67,0.33,0.67,0.67,0.33]
sigma_min implicito = [0.67,0.33,0.67,0.67,0.33]
```

### 10.2 Artefacto con tightening operativo

```yaml
extensions:
  kora:
    vector_ontologico:
      sigma: [2,1,2,2,1]
artefacto:
  contexto:
    qa_budget:
      sigma_min: [0.8,0.4,0.8,0.8,0.4]
      latency:
        max_ms: 1500
      availability:
        min: 0.995
        window: "30d"
```

Lectura:

1. El compromiso canonico minimo sigue siendo `Σ=[2,1,2,2,1]`.
2. El operador exige una realizacion runtime mas estricta que el minimo
   implicito del IR.
3. Un target que no pueda sostener `availability.min = 0.995` **DEBE** bajar el
   artefacto de target o declarar la degradacion.

## 11. Migracion

`qa-spec v1.0.0` es aditiva. No exige reescribir artefactos existentes.

Reglas de migracion:

1. Artefactos con `Σ` discreto existente **NO REQUIEREN** cambio de shape.
2. Artefactos que deseen declarar budgets operativos **DEBERIAN** usar
   `artefacto.contexto.qa_budget` en forma canonica.
3. Donde ya exista una referencia textual a `contexto.qa_budget.latency`, la
   forma recomendada pasa a ser `contexto.qa_budget.latency.max_ms`.
4. Desde `risk-register-spec v1.0.0`, el registro de riesgo **DEBE** leerse
   sobre la moneda y floors declarados por esta spec.

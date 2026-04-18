---
_manifest:
  urn: "urn:kora:kb:runtime-spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "contrato minimo de runtime para el sistema moderno; v3.7 agrega §13 Compatibilidad con outputs antiguos para materializar la absorcion declarada en gobernanza §3.2; v3.8 incorpora multiagente-spec y el target Mastra"
version: "3.8.0"
status: publicado
tags: [spec, runtime, deployment, equivalence]
lang: es
extensions: {}
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:multiagente-spec"
    - "urn:kora:kb:transmutation-spec"
---

# KORA/Runtime-Spec v3.8.0

## 1. Definicion

`runtime-spec` gobierna solo invariantes runtime: equivalencia observable,
enforcement fuera del prompt, routing, `qa_budget` proyectado, coreografia
multiagente proyectada y frontera entre fuente y estado operativo.

No gobierna el IR del artefacto; eso pertenece a `autoria-spec`.

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
2. Cuando un artefacto declara `artefacto.contexto.qa_budget`, el runtime
   **DEBE** interpretarlo conforme a `qa-spec`; no se permiten semanticas
   runtime-ad-hoc para los mismos nombres.
3. Un runtime **PUEDE** estrechar budgets para proteger seguridad o capacidad
   del target.
4. Un fallback **PUEDE** degradar calidad.
5. Un fallback **NO DEBE** cruzar silenciosamente el piso duro derivado de `Σ`
   o de `qa_budget.sigma_min`.
6. Un fallback **NO DEBE** cambiar dominio o ley.
7. Si el fallback ocurre dentro de una corrida multiagente, **DEBE** preservar
   `protocol_id`, `session_id` y budget vigente conforme a `multiagente-spec`.

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
5. emitir artefactos derivados en `{workspace}/_BUILD/{target}/` (p. ej. `artifacts/agents/{ns}/{name}/_BUILD/{target}/` para productivos, o `artifacts/agents/_FRAGUA/REVIEW/{name}/_BUILD/{target}/` para workspaces en staging),
6. emitir `{workspace}/_BUILD/{target}/_transmutation.yml`.

Reglas:

1. el target nunca se vuelve fuente primaria,
2. toda degradacion de fidelidad debe declararse,
3. `_transmutation.yml` es obligatorio,
4. los directorios `_BUILD/` son regenerables por definicion y **DEBEN** estar gitignored a nivel de repositorio.

## 11. Validacion

| Check | Condicion | Enforcement |
| --- | --- | --- |
| Policy server-side | Safety no queda delegada al LLM | runtime |
| Wrapper limpio | Derivado no suplanta la fuente | lint/manual |
| Routing visible | Hay decision runtime trazable | runtime/manual |
| Drift auditable | Repo y runtime comparables | manual/lint |
| Registro emitido | La compilacion deja `_transmutation.yml` | lint |

## 12. Migracion

Contrato vigente v3.7.0:

- runtime queda reducido a invariantes runtime,
- absorbe la compilacion concreta del IR,
- el diseño moderno evita reinyectar semantica del agente dentro del runtime,
- §13 materializa la compatibilidad de outputs antiguos declarada en
  `gobernanza §3.2` como absorcion dentro de `runtime-spec`.

## 13. Compatibilidad con outputs antiguos

Runtimes y consumidores pueden ejecutar artefactos anteriores al regimen
de transmutacion actual. Esta seccion fija la regla de coexistencia sin
convertir lo legacy en camino canonico.

### 13.1 Modalidades de output legacy

1. **Consumo directo de workspace legacy**: un runtime carga directamente
   los archivos `AGENTS.md`, `config.json`, `SOUL.md`, `USER.md`, `TOOLS.md`
   desde `artifacts/agents/{ns}/{name}/`. Valido solo cuando el agente carece de
   `AGENT.md` o cuando el runtime aun no soporta el IR.
2. **Outputs transmutados pre-v3.6**: artefactos en `{workspace}/_BUILD/{target}/`
   generados por versiones antiguas de la transmutacion. Permanecen
   consumibles hasta que el target se regenere.
3. **Adapter legacy a target nativo**: wrapper especifico que traduce
   `AGENT.md` hacia un target que solo conoce el perfil legacy.

### 13.2 Reglas

1. El camino canonico es `AGENT.md -> transmute -> {workspace}/_BUILD/{target}/`.
2. Un runtime nuevo **NO DEBE** depender de outputs legacy cuando exista
   `{workspace}/_BUILD/{target}/` regenerable y actualizado.
3. Un adapter `legacy -> target` **DEBE** declararse como perfil de
   compatibilidad, no como pipeline canonico.
4. Los outputs legacy **NO DEBEN** emitirse con `_transmutation.yml` del
   regimen moderno — eso es exclusivo del pipeline canonico.
5. No hay coexistencia prolongada: `autoria-spec §13` establece migracion forzada en una sola pasada. Divergencias entre `_BUILD/` y shape de autoria son invalidas.

### 13.3 Prohibiciones

1. Nuevos targets **NO DEBEN** disenarse para consumir scaffold legacy.
2. La transmutacion canonica **NO DEBE** hibridarse con outputs legacy
   en el mismo ciclo.
3. Los directorios `_BUILD/` **NO DEBEN** conservar artefactos que ya no tienen agente fuente
   activo; la reconciliacion periodica elimina huerfanos.

---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-19-cierre-estructural-post-reorg-v5"
  provenance:
    created_by: "OpenAI Codex (encarnando cat-thinking)"
    created_at: "2026-04-19"
    source: "Cierre estructural posterior al reorg v5: consolida H6, H5, H2, H13, H23 y H7 en master."
version: "1.0.0"
status: publicado
tags: [handoff, closeout, reorg-v5, qa, multiagente, procesos, riesgo, mastra, curacion-kb]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-ola2-remediacion-profunda"
    - "urn:kora:kb:operational-memory-2026-04-19-cierre-estructural-post-reorg-v5"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:procesos-spec"
    - "urn:kora:kb:risk-register-spec"
    - "urn:kora:kb:multiagente-spec"
    - "urn:kora:kb:mastra-runtime-extension"
  refines:
    - "urn:kora:kb:handoff-2026-04-18-ola2-remediacion-profunda"
---

# Handoff explicito — cierre estructural post-reorg v5

## Resumen ejecutivo

La sesion del **19 de abril de 2026** cierra el backlog estructural mayor que
quedo abierto al terminar las tres olas ya incorporadas en `origin/master`.

Quedan materializados y conectados al canon vigente:

1. `H6` — `qa-spec` con enrichment canonico `([0,1]^5, <=, 1bar, otimes)`.
2. `H5` — `multiagente-spec` como sheaf operacional para coreografia y
   handoff multiagente.
3. `H2` — `procesos-spec` para los 9 procesos del toolchain como funtores.
4. `H13` — `risk-register-spec` como composicion Kleisli sobre ledger tipado.
5. `H23` — `mastra-runtime-extension` + target `mastra` + check
   `fidelidad-mastra`.
6. `H7` — curacion efectiva del grafo KB mediante mapas por namespace:
   el grafo termina con **0 huerfanos reales**.

Estado estable resultante:

1. `python3 toolchain/kora check --strict` termina **16/16 verde**.
2. `python3 -m unittest discover -s tests` termina **299 OK (skipped=2)**.
3. `python3 toolchain/kora kb-graph --json --orphans` termina con
   **521 nodos, 654 aristas, 0 huerfanos reales, 0 aristas rotas**.

## Cambios consolidados

### 1. Semantica constitucional ampliada

- `ontology/qa-spec.md` fija la moneda canonica de calidad y separa
  compromisos normativos (`Sigma`) de budgets operativos (`qa_budget`).
- `ontology/procesos-spec.md` declara dominio, codominio, preservacion y
  perdida para `migrate`, `validate`, `check`, `promote`, `deprecate`,
  `transmute`, `ingest`, `kb-graph` e `index`.
- `ontology/risk-register-spec.md` habilita riesgo como efecto acumulativo con
  composicion Kleisli y piso residual conectado a `qa-spec`.
- `runtime/multiagente-spec.md` formaliza protocolos distribuidos, ticket de
  procedencia, solapamientos obligatorios y criterio de pegado local-global.

### 2. Proyeccion runtime ampliada

- `runtime/mastra-runtime-extension.md` incorpora Mastra como quinto target
  runtime formal de KORA.
- `serialization/schemas/kora-artefacto.json` incorpora `mastra` en
  `entornos_objetivo`.
- `toolchain/kora_lib/transmute.py` declara `mastra` en la matriz de
  preservacion y en los adapters de proyeccion.
- `toolchain/kora_lib/checks.py` agrega `fidelidad-mastra`, elevando el
  registry de checks de 15 a 16.
- `toolchain/kora_lib/autoria_validate.py` reconoce `mastra` como extension de
  plataforma valida.

### 3. Integracion transversal del canon

Se actualizaron los documentos constitucionales para absorber el nuevo bloque:

- `governance/gobernanza.md` -> `v4.4.0`
- `ontology/harness-spec.md` -> `v1.1.0`
- `runtime/runtime-spec-md.md` -> `v3.8.0`
- `runtime/transmutation-spec.md` -> `v1.1.0`
- `runtime/openclaw-runtime-extension.md` -> `v1.2.0`
- `serialization/autoria-spec.md` -> `v1.2.0`

Puntos relevantes:

1. `autoria-spec` ahora admite `risk_register` opcional.
2. `harness-spec` y `runtime-spec-md` citan explicitamente `qa-spec`,
   `procesos-spec`, `risk-register-spec` y `multiagente-spec`.
3. `transmutation-spec` ya reconoce a Mastra dentro del perimetro canonico.
4. `runtime-spec-md` exige preservar `protocol_id`, `session_id` y budget en
   fallback multiagente.

### 4. Curacion KB sin romanticismo

Se agregaron mapas de curacion por namespace en:

- `artifacts/knowledge/{agengai,fxsl,gn,kora,korvo,legal,pro,salud,sii,tde}/namespace-curation-map.md`

La estrategia no inventa relaciones finas inexistentes: cada mapa declara
pertenencia operativa al corpus del namespace por `cites`, absorbiendo los
huerfanos reales del snapshot previo sin reescribir 300+ nodos individuales.

## Verificacion ejecutada

Comandos corridos en esta sesion:

```bash
python3 toolchain/kora index
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
```

Resultado final verificado:

- `check --strict`: `Checks run: 16`, `Passed: 16`, `Failed: 0`
- `unittest`: `Ran 299 tests`, `OK (skipped=2)`
- `kb-graph`: `Nodes 521`, `Edges 654`, `Orphans real 0`, `Broken edges 0`

Durante la sesion aparecieron 2 fallas de fixtures por versionado menor de
`harness-spec` y `transmutation-spec`; se corrigieron en `tests/test_artifacts.py`
y la suite completa quedo verde.

## Invariantes para la proxima sesion

1. El backlog estructural mayor (`H6/H5/H2/H13/H23/H7`) ya esta cerrado.
2. `mastra` ya es target formal de transmutacion y tiene check propio.
3. `risk_register` ya forma parte del envelope canonico de autoria.
4. El grafo KB ya no parte con huerfanos reales; si reaparecen, es drift.
5. Los reportes de `docs/generated/*` deben regenerarse en una pasada limpia
   antes de cualquier release documental, no mezclados con cambios ajenos.

## Siguiente frente recomendado

Con el bloque estructural cerrado, el siguiente trabajo de mayor retorno ya no
es una spec mayor sino **deuda de artefactos**:

1. `H2-artifacts`: clasificar los `168 CM-*` embebidos en productivos en
   `promover / absorber / descartar`.
2. Promocion de staging: `21` agentes en `_FRAGUA/INBOX/` y `7` skills en
   `_TALLER/INBOX/`.
3. Menores diferibles: `H9`, `H17`, `H20`, `H22`.

## Pipeline minimo de retoma

```bash
cd /home/felix/kora
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Si cualquiera deja de coincidir con este handoff, diagnosticar drift antes de
tocar.

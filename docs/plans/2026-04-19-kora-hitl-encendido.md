# Plan HITL — Encender la usina KORA

**Fecha**: 2026-04-19
**Autor**: steipete (fusion de 4 propuestas + HITL con Felix)
**Fuentes fusionadas**:
- `docs/plans/2026-04-19-kora-usina-operativa.md` — steipete v1, 4 fases con cierre binario
- `docs/plans/2026-04-19-kora-usina-productiva-operational-plan.md` — 6 olas con owners
- `docs/plans/2026-04-19-kora-usina-productiva-roadmap.md` — tasks tecnicas por archivo
- `docs/plans/recomendaciones-kelly.md` — walking skeleton + outcome medible
- `docs/plans/recomendaciones-steipete.md` — version corta original

**Humano en el loop**: Felix como sponsor + gatekeeper de avance de fase + aceptante de decisiones irreversibles. steipete propone, despacha y coordina. Obreros de codigo ejecutan bajo invariantes INV-01..INV-10 del workspace `steipete`.

---

## Intent Contract

- **Beneficiario**: Felix, operando KORA como fabrica continua de knowledge + artefactos agenticos desplegables.
- **Cambio deseado**: pasar de "repo gobernado por specs con strict 17/17 verde" a "usina que procesa trafico real con eval cerrando el loop".
- **Outcome que valida la usina** (de Kelly, literal):
  > *"La usina funciona cuando un cambio en un documento fuente (o en una intencion de agente) propaga — via ingesta, curacion, composicion y transmutacion — a un artefacto desplegado en un runtime real, que supera su eval canario. Lead time objetivo: < 1 hora al inicio; < 10 min al tercer mes."*
- **Resultado minimo visible**: un doc bruto cruza `_SCRIPTORIUM/INBOX` hasta quedar publicado y resoluble; un componente cruza `_FRAGUA/INBOX` hasta quedar componible, transmutado y corriendo con eval verde.
- **Autonomy limit (HITL)**: steipete ejecuta propuestas concretas; Felix confirma antes de abrir la siguiente fase. Ningun cambio irreversible (freeze, deprecacion, baja de spec, merge a master) sin OK explicito de Felix. Obreros ejecutan bajo despacho explicito y calibrado (INV-02, INV-05).
- **Main risk**: seguir escribiendo specs sin componente desplegado consumiendo knowledge real. La usina que solo produce catalogos es museo.

## Principios operativos (no negociables)

- **Incrementalismo**: accion temprana con info parcial > espera por spec completa.
- **Close the loop**: ninguna fase cierra sin eval canario verde + gate binario verificado.
- **Blast radius evaluado antes de despachar**: S-ASSESS obligatorio por sprint.
- **Honestidad radical**: fallo se reporta tal cual. "Fallo. Esto paso. Esto hago."
- **HITL explicito**: steipete propone concreto; Felix confirma. Nunca preguntar en vacio (INV-08).
- **Anti-sobreingenieria**: JSONL > Grafana. grep > Prometheus. Sin MCPs, sin vector DBs, sin dashboards decorativos (ANTI-01).
- **Ceremonial minimo**: sin owners ni specs nuevas si las existentes gobiernan. `docs/generated/*` es vista materializada, no source of truth.

## Roles y ownership

| Rol | Owner | Responsabilidad operativa |
|-----|-------|---------------------------|
| Sponsor humano | Felix | prioriza, confirma avance de fase, acepta irreversibles |
| Coordinador | `dev:agent:steipete` | S-DISPATCHER → S-ASSESS → S-DELEGATE → S-VERIFY; despacha obreros |
| Constitucion | `kora/guardian` | precedencia + invariantes + shape del system model |
| Knowledge | `kora/curator` | intake, atomize, review, promote, readiness editorial-semantica |
| Componentes | `kora/forgemaster` | authoring IR, validate, compose, handoff tecnico |
| Cierre operativo | `kora/custodio` | catalog, stats, drift, deploy-status, repo health |
| Runtime/harness | `kora/clawforge` | transmute + bundle + runtime-extension + acoplamiento |

Los 5 owners agenticos siguen en `_FRAGUA/REVIEW/` o productivos segun estado actual. La Fase 3 promueve los que falten a productivos. Ninguno nace "ornamental": cada uno acredita consumo real por demanda de fase.

## Go-Live Envelope (perimetro inicial, acciones prohibidas)

- **Perimetro inicial** (fases 1-3): `meta-kora` + UNA familia de knowledge + UNA familia de componentes.
- **Targets iniciales** (fase 1): 1 runtime (claude-code o openclaw, eleccion de Felix).
- **Targets siguientes** (fase 3-5): el segundo de claude-code/openclaw, luego codex, luego gemini.
- **Target final diferido**: hermes, solo despues de decision explicita (ver Fase 0).
- **Acciones prohibidas al inicio**:
  - ampliar la flota multi-namespace
  - abrir promociones masivas sin demanda
  - declarar el IR estable antes de control plane + eval architecture
  - escribir nuevas specs doctrinales
  - tratar `docs/generated/*` como autoritativo

---

## Fase 0 — Saneamiento sincronico (1 sesion, no bloquea fases productivas)

**Objetivo**: eliminar verdes falsos + deuda nominal que haria mentir a las fases siguientes. Es el *"Stop Lying"* del roadmap + el "freeze" de usina-operativa.

**Owners**: `guardian` + `custodio`. steipete coordina despacho paralelo.

**Paquetes despachables en paralelo** (blast radius bajo, reversibles via git):

- [ ] **P0.1** — Strings legacy en `toolchain/kora_lib/*.py` (82 matches esperados: `KNOWLEDGE/`→`artifacts/knowledge/`, `SKILLS/`→`artifacts/skills/`, `AGENTS/`→`artifacts/agents/`, `scripts/kora`→`toolchain/kora`). 1 obrero, riesgo bajo.
- [ ] **P0.2** — Mover one-shots residuales (`kora_transmuter.py`, `source_mapper.py`, `check_counts.py`, `generate_hodom_template.py`, `telegraph_audit_repair.py`, `koraficate_sii_faq.py`, `migrate_coalgebra.py`) a `toolchain/legacy_migration/`. 1 obrero, riesgo bajo.
- [ ] **P0.3** — Reescribir `toolchain/README.md` en ≤15 lineas honestas (o borrarlo y apuntar a CLAUDE.md). 1 obrero.
- [ ] **P0.4** — Desdeterminizar `sync-docs`: quitar `Fecha:` variable del output o mover 3 archivos drift-diario a `.gitignore` con regeneracion CI. 1 obrero.
- [ ] **P0.5** — Repair de `validation.py` (roadmap Task 1): schema cargado desde `serialization/schemas/kora-artefacto.json` real, fallar duro si ausente en strict. 1 obrero, riesgo medio.
- [ ] **P0.6** — Agent-audit honesto (roadmap Task 2): remover baselines legacy `specs/*`, exponer `coverage_mode` si parcial. 1 obrero.

**Decisiones HITL al final de la fase** (Felix confirma explicitamente):

- [ ] **D0.1** — `_perfiles/`: elevar a regimen formal en `autoria-spec` o mover a `_FRAGUA/INBOX/` como drafts. Decision binaria.
- [ ] **D0.2** — Hermes: runtime target nuevo, alias, o eliminado del plan. Si es nuevo, ticket aparte y queda bloqueado hasta fase 5+.
- [ ] **D0.3** — Freeze formal de `harness-spec`, `autoria-spec`, `transmutation-spec` hasta cerrar fase 3. Seccion nueva en `governance/gobernanza.md`.

**Gate (verificacion automatica)**:
```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict       # strict verde, 17+ checks
python3 toolchain/kora validate --profile strict
python3 -m unittest discover -s tests        # 302+ tests verdes
rg -n "scripts/kora|catalog/catalog_master_kora.yml|specs/agentfile-spec|specs/skill-overlay-spec" .  # cero matches vivos
git status  # limpio al dia siguiente sin regenerar
```

**Criterio de cierre binario**:
- strict verde sin trampas
- anti-drift test que detecta referencias legacy vivas en surfaces soportadas
- agent-audit no miente sobre cobertura
- decisiones D0.1/D0.2/D0.3 registradas en `governance/gobernanza.md` y en commit message

**Blast radius**: bajo. Todo reversible.
**Duracion estimada**: 1 sesion.

---

## Fase 1 — Walking skeleton vertical (1-2 sesiones, **el unico test real**)

**Objetivo**: UNA astilla vertical minima que atraviese los dos pipelines + composicion + transmutacion + UN runtime + UN eval. **Sin esto verde, el resto es teatro**.

**Principio (Kelly, literal)**: la astilla tiene que ser *completa*, no *buena*. Feo esta bien; roto no.

**Owners**: `curator` (pipeline A) + `forgemaster` (pipeline B) + `clawforge` (transmute). steipete orquesta.

### Tripleta minima — decision HITL de Felix al empezar

- [ ] **T1** — 1 documento fuente con consumidor real. Candidatos: un `.md` de `artifacts/knowledge/salud/medicina-emergencia/` o de `artifacts/knowledge/fxsl/xanpan/`. **Criterio**: Felix ya tiene un caso donde ese doc informaria una decision real.
- [ ] **T2** — 1 componente que lo citara. Candidatos: `kora/curator` (AGENT.md ya maduro en productivo) o un agente pequeno nuevo `kora/canario` creado para este fin.
- [ ] **T3** — 1 runtime target. Candidatos: `claude-code` (runtime diario de Felix, menor friccion) o `openclaw` (fleet operativo, mayor valor estrategico). **Recomendacion steipete**: `claude-code` primero. Menor blast radius, menor latencia de eval.

### Flujo obligatorio end-to-end

```
documento.md  (source, edicion humana o ingesta)
  → python3 toolchain/kora atomize documento.md → artifacts/knowledge/{ns}/...
    → componente (AGENT.md con cites: a URNs atomizados)
      → python3 toolchain/kora transmute --target {runtime} --agent {componente}
        → deploy manual a la ubicacion del runtime
          → invocacion con input canario (fixture)
            → eval: comparar output vs esperado
              → registrar senal en docs/generated/invocations.jsonl
```

### Gate binario (Kelly — **no negociable**)

- Felix cambia UNA frase en `documento.md` → re-corre pipeline → redeploy → agente refleja el cambio en su respuesta al canario. **Todo en ≤ 1 hora de trabajo humano**.
- `atomize` no apunta a `OPERATIONS/` (anti-regresion post-reorg v5).
- `transmute` produce output con `provenance.urn` + `provenance.hash` + `provenance.timestamp` visible en el bundle deployado.
- Senal canario registrada en JSONL con `{agent_urn, ts, input_hash, output_hash, eval_result}`.

**HITL**: Felix elige tripleta en S-PROPOSE. steipete despacha ejecucion. Felix confirma eval canario al final.

**Trap a evitar** (Kelly): querer que la astilla sea "buena". Completa > elegante. Feo esta bien; roto no.

**Duracion estimada**: 1-2 sesiones.
**Regla de parada**: si no cierra en ≤ 8h de trabajo humano → rediseno de la astilla. Probablemente demasiado compleja.

---

## Fase 2 — Instrumentar el lazo antes de ensancharlo (1 sesion)

**Objetivo**: medir el lazo antes de ensancharlo. Un lazo sin telemetria se degrada solo.

**Owner**: `custodio`. steipete coordina instrumentacion minima.

### Entregables (todos JSONL + grep, ANTI-Grafana)

- [ ] **I2.1** — `docs/generated/invocations.jsonl`: un record por invocacion canaria: `{agent_urn, ts, input_hash, output_hash, eval_result}`.
- [ ] **I2.2** — `docs/generated/retrieval.jsonl`: URNs de KB leidos por invocacion. Sin esto no hay como saber si la curaduria paga renta.
- [ ] **I2.3** — Frontmatter `extensions.kora.verified_at` por nodo de KB. Politica: 90 dias sin verificacion → cola de revision automatica.
- [ ] **I2.4** — `docs/generated/lead-time.jsonl`: desde commit en fuente hasta deploy con eval verde, por corrida.
- [ ] **I2.5** — Comando nuevo `python3 toolchain/kora deploy-status`: compara hash IR vs hash deployado en runtimes locales (`~/.claude/agents/`, `~/openclaw-fleet/workspaces/`). Reporta stales.
- [ ] **I2.6** — Check nuevo `bundle-coherence`: AGENT.md declara `conocimiento_permitido:` y `componible_con:` por URN; el check verifica existencia + productivo (no staging). Suma al `check --strict` (llega a 18/18).

### Metricas del control plane (operational-plan, solo las con accion)

| Metrica | Que mide | Accion ante rojo |
|---------|----------|-------------------|
| Intake backlog age | edad en `_SCRIPTORIUM/INBOX` y `_FRAGUA/INBOX` | ≥ 14 dias → revision o deprecacion |
| Promotion lead time | tiempo desde ingreso a publicado | tendencia ascendente → cuello en review |
| Catalog freshness | drift entre filesystem y `docs/generated/catalog.yml` | ≠ 0 → regenerar + fix causa |
| Transmutation success rate | % bundles validos por target | < 95% → runtime-extension rota |
| Canary eval pass rate | % de invocaciones canarias verdes | < 80% → componente en cuarentena |

Ninguna metrica sin owner ni accion asociada. Si Felix no la usa, se borra.

**Gate binario**:
- Felix responde con datos (no opinion) a: *"¿cual es el lead time actual?"* y *"¿que nodos del KB se usaron esta semana?"*.
- `check --strict` verde con `bundle-coherence` incluido.
- `deploy-status` detecta un deploy stale intencional introducido como test.

**HITL**: Felix confirma metricas utiles. Si una no le sirve, se elimina. Dashboards decorativos prohibidos (ANTI-PLAN-03).

**Duracion estimada**: 1 sesion.

---

## Fase 3 — Segundo lazo por prueba de composicion (2-3 sesiones)

**Objetivo**: ensanchar por prueba, no por catalogo. Tres pruebas paralelizables.

**Owners**: `forgemaster` (componentes) + `curator` (knowledge).

### Tres pruebas (Kelly)

- [ ] **P3.1 — Componente compartido**: un segundo componente que cite el MISMO KB que el primero. Valida que el corpus curado es *compartible*, no agente-especifico.
- [ ] **P3.2 — Mismo componente, segundo runtime**: si `kora/curator` corre en claude-code Y en codex con eval verde en ambos, la capa `runtime-extension` paga renta. Si no, arreglar antes de tocar gemini/openclaw.
- [ ] **P3.3 — Corpus acumulable**: un segundo documento del mismo dominio, citado por ambos componentes. Valida que la curaduria acumula.

### Promociones por demanda desde `_FRAGUA/INBOX` (no inventario muerto)

Candidatos con demanda real conocida:
- `polymath` (analisis estructural, documentos largos)
- `opm-specialist` (OPM/ISO 19450)
- `salubrista` (sistemas de salud)
- `steipete` (coordinacion dev)
- `forjador-openclaw` (fleet ops)

**Regla**: se promueve solo si la fase 3 necesita el componente *en caliente*. Promocion de inventario muerto → deuda futura.

### Metrica de fondo (Kelly)

*Costo marginal del segundo {documento, componente, runtime}*. Si cae a 30-50% del primero, la usina amortiza. Si es comparable (≥ 80%), el marco no funciona — **parar y redisenar antes de fase 4**.

### Gate binario

- 3 componentes productivos + 2 runtimes activos + composicion viva trazable.
- Un agente productivo usando una skill productiva que cita un knowledge productivo. Los tres transitaron staging → productivo en fases 1-3.
- `bundle-coherence` verde en los 3 componentes.
- `transmute --target <runtime2> --agent kora/curator` con eval canario verde.

**HITL**: Felix confirma que workspaces promover. **No curar inventario muerto** (regla dura).

**Duracion estimada**: 2-3 sesiones.
**Regla de parada**: si costo marginal ≥ 80% del primero → pausar, revisar composicion.

---

## Fase 4 — Dos pipelines industriales con cadencia propia (2-3 sesiones)

**Objetivo**: separar pipelines de knowledge y componentes como flujos de primera clase. Que corran en dias distintos sin bloquearse.

**Owners**: `curator` (A), `forgemaster` (B), `clawforge` (acoplamiento).

### Pipeline A — Knowledge (cadencia: lote semanal)

Flujo: `_SCRIPTORIUM/INBOX/` (bruto) → `REVIEW/` (curado) → `artifacts/knowledge/{ns}/` (publicado).

**Contrato por estado**:
- `INBOX/`: bruto, sin namespace. Provenance minima obligatoria.
- `REVIEW/`: curado, validable, con consumidor previsto declarado.
- `artifacts/knowledge/{ns}/`: publicado, resoluble por URN, readiness verificada.

**Gate de promocion (regla dura)**: todo nodo nuevo declara que componente lo va a citar o muere en REVIEW. Sin consumidor previsto, nodo se deprecia. Esta regla es el corazon del control de volumen — el KB crece solo donde hay trafico.

Entregables: `intake.py` + `promote.py` + `kb-graph.py` endurecidos (roadmap Task 5).

### Pipeline B — Componentes (cadencia: por intencion de negocio)

Flujo: `_FRAGUA/INBOX/` + `_TALLER/INBOX/` → `REVIEW/` → `artifacts/agents|skills/{ns}/{name}/`.

**Contrato compartido** (roadmap Task 6, autoria-spec):
- identity (urn)
- ontological vector (`harness_vector`)
- allowed knowledge (`conocimiento_permitido`)
- composability (`componible_con`)
- runtime intent (`intent_contract`)
- eval contract (`eval_contract`, nuevo)
- autonomy envelope (`autonomy_envelope`, nuevo)

**Gate de publish**: todo componente productivo tiene los 7 campos arriba no vacios.

### Punto de acoplamiento (no pipeline)

Comando nuevo: `python3 toolchain/kora compose --agent <urn> --target <runtime> --dry-run`.

Verifica antes del `transmute` que:
- `harness_vector` existe
- `cites:` resuelven y son productivos
- `intent_contract` coherente con `eval_contract`
- `autonomy_envelope` compatible con runtime target
- `componible_con` coherente entre agente y skills

### Gate binario

- Pipelines corren en dias distintos sin bloquearse.
- `kora compose` detecta inconsistencias antes del `transmute` (test con uno intencionalmente roto).
- Familia piloto de knowledge cruza pipeline A completo con trazabilidad visible.
- Familia piloto de componentes cruza pipeline B completo.

**HITL**: Felix define cadencia (semanal/por demanda) y aprueba el gate de Pipeline A (regla dura: sin consumidor previsto, sin promocion).

**Duracion estimada**: 2-3 sesiones.

---

## Fase 5 — Runtime matrix controlada (3-4 sesiones, una por runtime)

**Objetivo**: habilitar runtimes por prueba, no por decreto. **Un runtime nuevo por sesion**.

**Owner**: `clawforge` + sponsor humano.

### Orden recomendado (Kelly)

| Runtime | Prioridad | Razon operativa |
|---------|-----------|------------------|
| claude-code | 1 | runtime diario de Felix, probado en fase 1 |
| openclaw | 2 | fleet operativo, mensajeria Telegram, maximo valor |
| codex | 3 | presencia en workflows de Felix, review automatizado |
| gemini | 4 | diversificacion de proveedor |
| agentskills | staging | declarativo, no bloqueante del critical path |
| mastra | staging | declarativo, no bloqueante |
| hermes | **bloqueado** | hasta definir que problema resuelve que los otros 5 no resuelven |

### Gate por runtime (identico para todos)

- Un componente canonico de KORA (sugerido `kora/curator`) transmuta → deploy → eval canario verde en ese runtime.
- Si no pasa, **el runtime no esta listo — el componente NO es el problema**. Runtime-extension se revisa. (Inversion de diagnostico Kelly: default = runtime, no IR).
- Drift check activo: `kora deploy-status` reporta divergencia hash IR vs hash deployado.

### Decision Hermes (HITL)

Hermes no esta en `transmute --help`. Si Felix no puede articular en 2 frases que problema resuelve Hermes que los otros 5 no resuelven, Hermes muere antes de nacer. Uno menos que gobernar. (Cumple ANTI-PLAN-06.)

**HITL**: Felix abre cada runtime semanalmente. Gate se aplica sin excepcion.

**Duracion estimada**: 3-4 sesiones (1 por runtime activo).

---

## Fase 6 — Mantenimiento dirigido por senal (permanente)

**Objetivo**: la usina se gobierna por datos del control plane, no por memoria de Felix.

### Regimen post-cierre

- **Timer systemd user-level**: `kora check --strict` + `kora deploy-status` + `bundle-coherence` diario. Notifica si falla.
- **Metrica operativa semanal**: cuantas tareas reales citaron knowledge productivo. Si es 0, investigar antes de curar mas (si el KB no se consume, es museo).
- **Ciclos alternantes**: medio dia knowledge, medio dia componentes. Nunca mas de 2 sesiones consecutivas en la misma cara.
- **Poda activa por senal** (Kelly):
  - Nodo de KB con 0 lecturas en 90 dias → candidato a poda o refactor.
  - Componente con tasa de aceptacion canario < 80% en ventana movil → cuarentena, revision forzada.
  - Runtime con divergencia repetida entre IR y deploy → runtime-extension rota, no el IR.
  - Intent contract sin outcome medible en 30 dias → reescribir o archivar.
- **Freeze de specs**: el freeze F0.D3 se levanta solo tras Fase 3 cerrada y con gap explicito que justifique la proxima ola doctrinal.

**HITL**: Felix revisa senales semanalmente (15 min). Puede pedir poda o reescritura. steipete propone; Felix confirma irreversibles.

---

## Orden de arranque inmediato (siguientes 48h)

1. **Felix** — lee este plan en 15 min. Confirma o corrige:
   - [ ] Intent Contract (outcome, autonomy limit).
   - [ ] Eleccion preliminar de tripleta para Fase 1 (candidato doc, candidato componente, runtime).
   - [ ] Decisiones D0.1/D0.2/D0.3 pendientes (pueden decidirse durante Fase 0; aca solo se agendan).
2. **steipete** — abre sesion dedicada a Fase 0 completa. Despacho paralelo:
   - Obrero 1 (claude-code, opus-4.6): P0.1 + P0.2 + P0.3 (strings + purga + README).
   - Obrero 2 (claude-code, opus-4.6): P0.5 + P0.6 (validation repair + agent-audit honesto).
   - Obrero 3 (codex, gpt-5.4): P0.4 (sync-docs desdeterminizado).
   - Reintegracion + gate estricto al final de la sesion.
3. **Gate Fase 0** — strict verde + tests verdes + git status limpio al dia siguiente. Felix confirma D0.1/D0.2/D0.3.
4. **Fase 1 arranca al dia siguiente** con tripleta confirmada. No se mezcla con Fase 0 (disciplina de fase unica por sesion).

---

## Senales — vas bien / vas mal (Kelly)

**Vas bien si**:
- Puedes mostrar a alguien un doc fuente y recorrer con el la astilla hasta ver al agente responder con ese contexto.
- Lead time se acorta mes a mes.
- Agregar un segundo runtime cuesta menos que el primero.
- Nodos de KB muertos se detectan y se podan sin drama.

**Vas mal si**:
- Sigues escribiendo specs ontologicas sin componente nuevo desplegado.
- El KB crece mas rapido que las citas a el.
- Matriz runtime se expande antes de que el primer runtime tenga eval verde sostenido.
- Mas tiempo invertido en curar categorias que en curar trafico real.

---

## Apuesta de fondo

El vuelo real no es que Felix opere la usina — es que **la usina se opere a si misma**. Los agentes que KORA produce son tambien sus operarios: `kora/curator` cura knowledge, `kora/forgemaster` promueve workspaces, `kora/guardian` mantiene integridad, `kora/custodio` vigila drift, `kora/clawforge` compone y proyecta.

Cuando ese lazo cierra, Felix deja de ser el unico curador y pasa a ser **arquitecto de intencion a tiempo completo**. Ahi KORA deja de ser repo y es plataforma.

No intentar cerrarlo en una sesion. Pero cada fase debe acercar a ese lazo, no alejar.

> *"La velocidad sin evaluacion es deuda acelerada. La ontologia sin trafico es cartografia. La usina sin outcome es museo industrial."* — Kelly

---

## Anti-patrones explicitos

- **ANTI-PLAN-01**: no ampliar matriz runtime antes de un piloto estable con eval verde sostenido.
- **ANTI-PLAN-02**: no agregar nuevas capas doctrinales (specs, checks, ontologias) sin que aparezcan por demanda de una fase ejecutada.
- **ANTI-PLAN-03**: no instrumentar con Grafana / Prometheus / OpenTelemetry. JSONL + grep basta.
- **ANTI-PLAN-04**: no tratar `docs/generated/*` como source of truth. El filesystem con manifests validos es canonico.
- **ANTI-PLAN-05**: no ejecutar fase N+1 sin gate binario de fase N aprobado por Felix.
- **ANTI-PLAN-06**: no escribir spec de Hermes hasta que Felix defina que problema resuelve que los otros 5 no resuelven.
- **ANTI-PLAN-07**: no promover workspaces de `_FRAGUA/INBOX` por inventario. Solo por demanda caliente.
- **ANTI-PLAN-08**: no declarar "productivo" un componente que no tiene eval canario verde en un runtime real.

---

## Reglas de parada duras

- **Fase 0.5** (validation repair) introduce regresiones en tests → parar. Las trampas pueden estar cubriendo contratos reales. Investigar antes de persistir.
- **Fase 1** (walking skeleton) no cierra en ≤ 8h de trabajo humano → **parar y redisenar la astilla**. Probablemente demasiado compleja.
- **Fase 2** (instrumentacion) requiere stack externo (Grafana, DB, dashboards) → parar. Volver a JSONL + grep.
- **Fase 3** (costo marginal) ≥ 80% del primero → marco no amortiza. Parar, revisar composicion.
- **Fase 5** ningun agente deployado consume knowledge productivo espontaneamente → el problema es el puente de consumo, no el volumen. Pausar, redisenar el bridge de retrieval.

---

## Trazabilidad a documentos fuente

Este plan fusiona:
- **Estructura de 6 fases + cierre binario** ← `2026-04-19-kora-usina-operativa.md` (fases 0-4)
- **Walking skeleton + outcome medible + JSONL + poda por senal** ← `recomendaciones-kelly.md`
- **Owners por agente KORA + control plane metricas + acciones prohibidas + Go-Live Envelope** ← `2026-04-19-kora-usina-productiva-operational-plan.md`
- **Tasks tecnicas especificas por archivo (P0.5, P0.6)** ← `2026-04-19-kora-usina-productiva-roadmap.md`
- **Observacion sobre Hermes + apuesta de fondo + federacion de operarios** ← `recomendaciones-steipete.md`

Criterio de resolucion de conflictos aplicado:
- Ceremonia vs ejecucion → ejecucion (steipete + Kelly).
- Olas con owners vs fases con gates → fases con gates + owners asignados por fase (fusion).
- Metricas exhaustivas vs minimas → minimas con accion asociada (Kelly ANTI-Grafana).
- Hermes incluido vs diferido → diferido con gate HITL explicito (todas las fuentes coinciden).

---

*steipete out. Siguiente accion: Felix confirma arranque. Gate Fase 0 esta semana.*

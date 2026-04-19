# KORA Usina Productiva — Plan Operativo

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** convertir KORA en una usina confiable para ingerir, curar, catalogar y exponer conocimiento, y para modelar, gestionar, componer y transmutar componentes agenticos compartidos hasta producir agentes, subagentes y skills desplegables.

**Architecture:** KORA debe operar como una celula socio-tecnica con dos lineas de produccion y un solo plano de acoplamiento. La linea A fabrica conocimiento publicado; la linea B fabrica componentes agnosticos reutilizables; el harness operativo compone ambas y proyecta a runtimes con perdida declarada y evaluada.

**Tech Stack:** `python3 toolchain/kora`, `toolchain/kora_lib/*`, KORA/MD, YAML frontmatter, JSON Schema, `unittest`, `docs/generated/*`, `artifacts/knowledge/*`, `artifacts/agents/*`, `artifacts/skills/*`.

---

## Intent Contract

- **Beneficiario:** el operador que quiere usar KORA como fabrica continua de conocimiento y artefactos agenticos desplegables.
- **Cambio deseado:** pasar de repo gobernado por specs y tooling a usina productiva con intake, curacion, catalogacion, composicion, transmutacion y mantenimiento continuo.
- **Resultado minimo visible:** un documento bruto cruza `_SCRIPTORIUM` hasta quedar publicado y resoluble; un componente agnostico cruza `artifacts/skills|agents` hasta quedar componible y transmutable a runtimes vivos.
- **Criterio de exito:** la salida de la usina no depende de ritual manual opaco; depende de manifests, checks, handoffs y control plane visible.
- **Autonomy limit:** durante las primeras olas no se abre produccion completa. Se endurece primero el nucleo `meta-kora`, luego una sola linea de conocimiento, luego una sola linea de componentes, y solo despues se amplian targets.

## Estado De Partida

- Ya esta corregida la precondicion mas urgente: el split-brain publico entre topologia v5 y superficies legacy.
- Ya existen gates minimos funcionales:
  - `python3 toolchain/kora check --strict`
  - `python3 -m unittest discover -s tests`
  - `python3 toolchain/kora sync-docs`
- Ya existe un nucleo operativo endurecido con ownership visible:
  - `kora/guardian`: coherencia constitucional, precedencia, validacion fundacional
  - `kora/forgemaster`: diseno, creacion, validacion y entrega tecnica
  - `kora/curator`: koraficacion, auditoria y curacion
  - `kora/custodio`: cierre de catalogo, ingesta, salud del repo
  - `kora/clawforge`: composicion OpenClaw y proyeccion runtime

## Roles Y Ownership

| Rol | Owner sugerido | Responsabilidad |
|---|---|---|
| Sponsor humano | Felix | priorizacion, apertura/cierre de olas, aceptacion de cambios irreversibles |
| Owner constitucional | `kora/guardian` | preservar precedencia, invariantes, shape y contrato del system model |
| Owner fabrica conocimiento | `kora/curator` | intake, curacion, trazabilidad, promotion criteria, calidad editorial-semantica |
| Owner fabrica componentes | `kora/forgemaster` | componentes agnosticos, validacion, IR, handoff tecnico |
| Owner cierre operativo | `kora/custodio` | index, catalogo, control plane, intake health, criterio de salida del repo |
| Owner runtime/harness | `kora/clawforge` | composicion, coupling con conocimiento, transmutacion y bundles de despliegue |

## Go-Live Envelope

- **Perimetro inicial:** solo `meta-kora` + una familia de knowledge + una familia de componentes.
- **Targets iniciales:** `codex` y `openclaw`.
- **Targets siguientes:** `claude-code` y `gemini`.
- **Target final diferido:** `hermes`, solo despues de estabilizar los cuatro anteriores.
- **Acciones prohibidas al inicio:** ampliar la flota, abrir promociones masivas multi-namespace, o declarar el IR estable antes de tener control plane y eval architecture.

## Gates Globales

Todo cierre de ola requiere, como minimo:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 -m unittest discover -s tests
python3 toolchain/kora sync-docs
```

Y ademas:

- evidencia de diff acotado
- surface publica sin referencias legacy vivas
- un rollback claro
- handoff de ownership a `custodio` cuando corresponda

## Métricas Del Control Plane

Estas metricas deben existir antes de declarar la usina productiva:

| Métrica | Qué mide | Fuente esperada | Umbral inicial |
|---|---|---|---|
| Intake backlog age | antigüedad del material en `_SCRIPTORIUM/INBOX` y `_TALLER/_FRAGUA/INBOX` | reporte derivado | sin items olvidados > 14 dias |
| Review WIP | carga viva en `REVIEW/` por linea | reporte derivado | WIP visible por namespace |
| Promotion lead time | tiempo desde ingreso a publicado | ledger de promotion | tendencia descendente |
| Catalog freshness | desfase entre filesystem y catalogo | `index` + check | 0 drift conocido |
| Transmutation success rate | porcentaje de bundles validos por target | test/probe por runtime | >= 95% en targets habilitados |
| Harness completeness | porcentaje de artefactos con knowledge + component + harness declarados | check dedicado | 100% en el perimetro inicial |
| Drift recurrence | reaparicion de referencias legacy o surfaces falsas | anti-drift tests | 0 en surfaces soportadas |

## Ola 1 — Sanear Core Y Control Plane

**Objetivo:** que la usina deje de mentir sobre si misma.

**Owners:** `guardian` + `custodio`

**Artefactos objetivo:**
- `toolchain/kora_lib/checks.py`
- `toolchain/kora_lib/reports.py`
- `toolchain/kora_lib/catalog.py`
- `toolchain/kora_lib/agent_audit.py`
- `docs/generated/*`
- tests anti-drift

- [ ] Congelar una unica verdad operacional: `python3 toolchain/kora` como entrypoint soportado.
- [ ] Convertir `docs/generated/` en superficie materializada pura, sin analisis historicos mezclados.
- [ ] Endurecer checks para que rutas, hints y reports muertos fallen.
- [ ] Alinear catalogo, stats y audit con la ontologia v5, no con topologias retiradas.
- [ ] Publicar un control plane minimo legible por operador.

**Verificaciones adicionales:**

```bash
rg -n "scripts/kora|catalog/catalog_master_kora.yml|specs/agentfile-spec|specs/skill-overlay-spec" .
python3 toolchain/kora stats --json
```

**Exit criteria:**
- el repo tiene una sola topologia viva
- `docs/generated/*` es confiable como vista materializada
- los artefactos publicos no presentan verdes falsos doctrinales

## Ola 2 — Endurecer La Fabrica De Conocimiento

**Objetivo:** cerrar la linea A como pipeline de ingestion -> curacion -> review -> publicacion -> exposicion.

**Owners:** `curator` + `custodio`

**Artefactos objetivo:**
- `serialization/knowledge-spec.md`
- `toolchain/kora_lib/intake.py`
- `toolchain/kora_lib/promote.py`
- `toolchain/kora_lib/kb_graph.py`
- ledgers y docs derivadas de knowledge

- [ ] Declarar formalmente el contrato de cada estado: `INBOX`, `REVIEW`, `published`.
- [ ] Definir producer contract para documentos ingeridos: origen, proveniencia, namespace, relaciones, estado.
- [ ] Endurecer promotion para que publicar no sea solo mover archivos; debe validar readiness.
- [ ] Hacer visible el flujo completo: que ingreso, que quedo detenido, que fue promovido, que esta obsoleto.
- [ ] Elegir una familia piloto de knowledge y pasarla de extremo a extremo.

**Piloto sugerido:** `artifacts/knowledge/kora/` o una sublinea acotada del corpus `kora`.

**Verificaciones adicionales:**

```bash
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora resolve "urn:kora:kb:harness-spec"
```

**Exit criteria:**
- una familia de conocimiento cruza el pipeline completo con trazabilidad visible
- promotion deja evidencia verificable, no solo filesystem mutation
- no hay artefactos publicados sin source/provenance/handoff claros

## Ola 3 — Endurecer La Fabrica De Componentes Agnosticos

**Objetivo:** cerrar la linea B como fabrica de componentes compartidos por agentes y skills.

**Owners:** `forgemaster` + `guardian`

**Artefactos objetivo:**
- `serialization/autoria-spec.md`
- `toolchain/kora_lib/validation.py`
- `toolchain/kora_lib/graph.py`
- `artifacts/skills/`
- `artifacts/agents/`

- [ ] Declarar explicitamente que es un componente compartido y que no.
- [ ] Separar componentes productivos de fibras workspace-locales, aliases y residuos legacy.
- [ ] Darle al IR de componentes lifecycle, catalogacion, relaciones y checks de composicion.
- [ ] Elegir una familia piloto de componentes y hacerla cruzar authoring -> validation -> catalog -> compose.
- [ ] Evitar que skills y agentes sigan naciendo como bundles acoplados al workspace por costumbre.

**Piloto sugerido:** componentes `kora/forgemaster` + `kora/curator` reutilizables por `clawforge`.

**Verificaciones adicionales:**

```bash
python3 toolchain/kora validate --profile strict --cohort meta-kora
python3 toolchain/kora graph --json
```

**Exit criteria:**
- existe una clase reconocible de componente compartido portable
- el repo puede distinguir componente reutilizable de implementacion local del workspace
- el IR de componentes es producto, no side effect

## Ola 4 — Cerrar El Plano De Acoplamiento

**Objetivo:** formalizar como se compone conocimiento + componente + harness + runtime.

**Owners:** `guardian` + `forgemaster` + `clawforge`

**Artefactos objetivo:**
- `ontology/harness-spec.md`
- `runtime/transmutation-spec.md`
- `toolchain/kora_lib/transmute.py`
- checks y graph relations de harness

- [ ] Declarar el harness como contrato unico de ensamblaje.
- [ ] Formalizar inputs permitidos, dependencias, trazabilidad, limites de autonomia y perdida declarada por target.
- [ ] Introducir checks de harness completeness y coupling valido.
- [ ] Garantizar que un artefacto desplegable no nazca directo del target runtime, sino del ensamblaje intermedio.
- [ ] Probar el acoplamiento con un caso piloto completo.

**Caso piloto sugerido:** un skill o agente del nucleo `meta-kora` que consuma knowledge formal y se proyecte a `codex` y `openclaw`.

**Verificaciones adicionales:**

```bash
python3 toolchain/kora transmute --target codex --agent kora/curator --dry-run
python3 toolchain/kora transmute --target openclaw --agent kora/clawforge --dry-run
```

**Exit criteria:**
- existe un contrato de harness unico, visible y comprobable
- la composicion deja evidencia de que artefactos y knowledge fueron ensamblados
- la perdida por target esta declarada y testeada

## Ola 5 — Primer Go-Live Productivo

**Objetivo:** poner en produccion un perimetro estrecho, reversible y medible.

**Owners:** `custodio` + `clawforge` + sponsor humano

**Perimetro:**
- `meta-kora`
- una familia piloto de knowledge
- una familia piloto de componentes
- targets `codex` y `openclaw`

- [ ] Seleccionar el conjunto minimo de artefactos que realmente entregan valor.
- [ ] Ejecutar una corrida de extremo a extremo desde intake hasta transmutacion.
- [ ] Medir lead time, intervencion humana, fallas de promotion, fallas de transmutacion y drift reaparecido.
- [ ] Dejar rollback documentado por cada superficie productiva.
- [ ] No ampliar el perimetro hasta tener 3 a 5 corridas limpias consecutivas.

**Criterios de go-live:**
- 3 corridas consecutivas sin regresion doctrinal ni surface drift
- 0 artefactos publicados con hints o rutas muertas
- transmutacion valida en ambos targets piloto
- `custodio` puede cerrar repo health sin interpretacion artesanal

## Ola 6 — Expansion Controlada

**Objetivo:** ampliar runtimes y dominios sin volver al caos.

**Owners:** sponsor humano + `guardian` + `clawforge`

- [ ] Abrir `claude-code` y `gemini` solo cuando `codex` + `openclaw` tengan estabilidad repetida.
- [ ] Abrir nuevos namespaces solo cuando el control plane ya mida backlog, lead time y harness completeness.
- [ ] Dejar `hermes` fuera del critical path hasta que exista contracto runtime propio y pruebas estables.
- [ ] Cada expansion debe repetir el ciclo: piloto acotado -> 3 corridas limpias -> ampliacion.

**Exit criteria:**
- cada runtime nuevo se incorpora como ola controlada, no como adapter espontaneo
- la flota crece sin perder gobierno

## Riesgos Estructurales

| Riesgo | Señal | Respuesta |
|---|---|---|
| Verde falso doctrinal | reports y checks verdes con rutas/specs muertas | subir anti-drift a gate estricta |
| Mezcla de fabricas | knowledge y componentes comparten pipeline y criterios | separar owners, estados y checks |
| IR ornamental | el IR existe en texto pero no gobierna toolchain | hacerlo catalogable, validable y transmutable |
| Expansion prematura | aparecen muchos runtimes antes del piloto estable | congelar amplitud y volver al go-live estrecho |
| Control plane decorativo | hay dashboards sin decisiones asociadas | cada metrica debe tener owner y accion |

## Decisiones Ejecutivas Recomendadas

1. No intentar “terminar KORA”.
2. Declarar oficialmente que la fase actual es `Ola 1 -> Ola 2`, no despliegue total.
3. Usar `meta-kora` como nucleo productivo y el resto como periferia controlada.
4. Tratar `codex` + `openclaw` como binomio inicial de produccion.
5. Rechazar toda expansion de flota o targets que no venga acompanada de control plane, eval y rollback.

## Primer Sprint Recomendado

Si hay que empezar de inmediato, el primer sprint debe ejecutar solo esto:

- [ ] Cerrar `Ola 1` completa.
- [ ] Elegir una familia piloto de knowledge para `Ola 2`.
- [ ] Elegir una familia piloto de componentes para `Ola 3`.
- [ ] Definir el probe de transmutacion para `codex` y `openclaw`.
- [ ] Dejar tablero minimo de control plane en `docs/generated/`.

**Comando de cierre del sprint:**

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 -m unittest discover -s tests
python3 toolchain/kora sync-docs
```

## Criterio Final De Exito

KORA estara “productivo en breve” no cuando tenga mas agentes, sino cuando pueda demostrar lo siguiente dentro de un perimetro estrecho:

- entra conocimiento bruto
- sale conocimiento curado y resoluble
- entran componentes agnosticos
- salen artefactos componibles y portables
- el harness deja trazabilidad visible
- la transmutacion a runtimes piloto es repetible
- el control plane permite gobernar la operacion sin intuicion artesanal

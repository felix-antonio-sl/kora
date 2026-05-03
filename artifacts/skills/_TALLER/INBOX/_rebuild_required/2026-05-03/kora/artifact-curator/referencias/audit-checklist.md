# Audit checklist

Mapa operativo para la fase `auditar`. Para cada familia documental y
forma material lista los checks aplicables y el comando o procedimiento
que los verifica. Esta tabla **no** redefine reglas; cita la SSOT.

## Comandos base

| Comando | Cuando |
| --- | --- |
| `python3 toolchain/kora index` | siempre antes de cerrar; refresca `docs/generated/catalog.yml`. |
| `python3 toolchain/kora check --strict` | gate maestro de mantencion; debe quedar verde antes de promover o transmutar. |
| `python3 toolchain/kora validate <urn>` | validacion fina de un artefacto puntual contra su spec gobernante. |
| `python3 toolchain/kora lint-md <path>` | lint focalizado de un archivo KORA/MD. |
| `python3 toolchain/kora kb-graph --json --orphans` | tras tocar `relations` o knowledge; detecta huerfanos y morfismos rotos. |
| `python3 toolchain/kora transmute --target agentskills --dry-run` | check `fidelidad-agentskills` para artefactos `forma_material: habilidad`. |
| `python3 toolchain/kora transmute --target mastra --dry-run` | check `fidelidad-mastra` para subagente, agente-propiamente-tal, agente-plataforma. |
| `python3 toolchain/kora roundtrip-check` | round-trip runtime ↔ IR ↔ runtime cuando hay deuda de transmutacion. |
| `python3 -m unittest discover -s tests` | obligatorio si se toco toolchain, specs, behavior compartido o relaciones de conocimiento. |

## Knowledge descriptivo (`note`, `guide`, `glossary`, `faq`, `catalog`, `cq_catalog`, `inventory`, `organigram`, `normative`)

| Check | Fuente | Severidad |
| --- | --- | --- |
| Envelope KORA/MD valido | `md-spec §3.1` | alta |
| Namespace coincide con primer subdir bajo `artifacts/knowledge/` | `md-spec §3.1` regla 7 | alta |
| Status coherente con ubicacion | `md-spec §3.1` reglas 8-10 | alta |
| Skeleton + meat preservados; grasa eliminada | `md-spec §5.4`, `§5.5` | alta |
| Realizacion superficial valida (no labelese, no headings-campo) | `md-spec §5.4.2` | media |
| `relations` tipado y resoluble | `knowledge-spec §4` | alta |
| FS=100% sobre cifras, fechas y excepciones del original | `md-spec §5.5` | alta |
| Familia declarada o derivable por convencion | `md-spec §5.6` | media |
| Lifecycle valido: `borrador → publicado → deprecado` | `gobernanza §5` | alta |

## Familia `atomic`

| Check | Fuente | Severidad |
| --- | --- | --- |
| `extensions.kora.family: atomic` declarado | `md-spec §5.6.1` regla 9 | alta |
| `## Indice de fuentes` presente y no vacio | `md-spec §5.6` | alta |
| Tipos en enum cerrado | `md-spec §5.6.1` | alta |
| ID `Pxxx` unico | `md-spec §5.6.1` regla 1 | alta |
| Cada proposicion con al menos una fuente resoluble | `md-spec §5.6.1` regla 4 | alta |
| Sin colapso semantico para bajar conteo | `md-spec §5.6.1` regla 5 | alta |
| Dedup multi-source solo por equivalencia real | `md-spec §5.6.1` regla 7 | media |
| Conflicto entre fuentes → tipo `tension`, no dedup | `md-spec §5.6.1` regla 8 | alta |
| Productor declarado: `extensions.kora.atomic.producer` | `knowledge-spec §12.3` regla 4 | media |

## Familia `spec`

| Check | Fuente | Severidad |
| --- | --- | --- |
| Cristalizacion: implicito → regla explicita con una sola lectura | `md-spec §5.6.2.1` | alta |
| Keywords RFC 2119 (DEBE, NO DEBE, DEBERIA, NO DEBERIA, PUEDE) | `md-spec §5.6.2.2` | alta |
| `Traces to:` apunta solo a la Formal Layer oficial | `md-spec §5.6.2.3` | alta |
| `Rationale:` no introduce obligaciones nuevas | `md-spec §5.6.2.3` regla 4 | media |
| Patron regla + ejemplo + traza en reglas no obvias | `md-spec §5.6.2.6` | media |
| Consistencia interna: sin reglas incompatibles sin clausula explicita | `md-spec §5.6.2.7` regla 1 | alta |
| Auto-suficiencia de la regla | `md-spec §5.6.2.7` regla 2 | media |
| No-circularidad | `md-spec §5.6.2.7` regla 3 | media |
| Tabla de validacion con columna `Enforcement` | `md-spec §5.6.2.7` regla 5 | alta |
| Auto-declaracion de precedencia | `md-spec §5.6.2.9` | alta |
| Familia `spec` reside en `governance/`, `ontology/`, `serialization/` o `runtime/` | `gobernanza §3.2` | alta |

## Skill (`forma_material: habilidad`)

| Check | Fuente | Severidad |
| --- | --- | --- |
| Envelope `_manifest` + `extensions.kora` valido | `autoria-spec §3` | alta |
| Vector ontologico en dominio `Π∈{1,2}, Μ∈{0,1}, Ξ∈{1,2}, Λ=0, Φ=1` | `autoria-spec §5.1` | alta |
| Leyes inter-eje (PI/MU, XI/LAMBDA, PHI/MU, accountability/transparency) | `harness-spec §4.1` | alta |
| `nivel_prescripcion` declarado | `autoria-spec §3.2`, §6 | alta |
| `descripcion` clara y comprensiva (runtime la usa para activar) | `autoria-spec §5.1` | media |
| Body ≤ 500 lineas (progressive disclosure) | `autoria-spec §5.1` y §14 | media |
| `## Recursos` presente si hay subdirs | `autoria-spec §5.1`, §7.1 | media |
| Subdirs canonicos solamente: `scripts/`, `referencias/`, `recursos/` | `autoria-spec §5.1` | alta |
| `conocimiento_permitido` con URNs resolubles, no paths | `agent-skill-construction-spec §3.4` | alta |
| `componible_con` resoluble | `autoria-spec §14` | baja |
| Fidelidad agentskills (transmute --target agentskills --dry-run) | `autoria-spec §5.5`, `§14` | alta |

## Subagente, agente-propiamente-tal, agente-plataforma

| Check | Fuente | Severidad |
| --- | --- | --- |
| Envelope `_manifest` + `extensions.kora` valido | `autoria-spec §3` | alta |
| Vector ontologico en dominio de proyeccion de la forma material | `autoria-spec §5.2-5.4` | alta |
| `compromisos_eticos` presente en `agente-propiamente-tal` y `agente-plataforma` | `autoria-spec §6` | alta |
| `memoria_config` declarada cuando Μ≥2 | `autoria-spec §6` | media |
| `composicion` solo cuando Ξ=4 (en agente-propiamente-tal) | `autoria-spec §6` | media |
| `extensions.{plataforma}` declarada en `agente-plataforma` | `autoria-spec §6` | alta |
| Materia ambiental presente en `agente-plataforma` (`MEMORY.md`, `HEARTBEAT.md` o equivalente) | `autoria-spec §5.4` | alta |
| FSM coherente cuando `verificacion_coalgebraica: true` | `autoria-spec §3.5`, `agent-skill-construction-spec §3.5` | alta |
| Sub-coalgebra de safety cerrada bajo transiciones | `autoria-spec §3.5` | media |
| API observable declarada cuando `componible_con` no vacio | `autoria-spec §3.5.1` | baja |
| Fidelidad mastra (transmute --target mastra --dry-run) | `autoria-spec §14` | alta |

## Construccion (gate adicional)

Cuando el artefacto es un agente o skill nuevo, ademas de los checks
anteriores, aplicar `agent-skill-construction-spec §5.2`:

| Check | Condicion |
| --- | --- |
| `construction-source-primary` | existe `AGENT.md` o `SKILL.md` como fuente primaria. |
| `construction-vector-fit` | el vector cumple `harness-spec` y el dominio de la forma material. |
| `construction-knowledge-explicit` | conocimiento por URN resoluble, no path duro. |
| `construction-fsm-valid` | estados, terminales y transiciones coherentes cuando hay FSM. |
| `construction-interface-typed` | entradas, salidas, tools y permisos observables. |
| `construction-risk-declared` | riesgos no triviales con mitigacion o deuda. |
| `construction-runtime-separation` | sin `_BUILD/` ni runtime output como fuente. |
| `construction-categorical-minimality` | la lectura categorial mas debil suficiente. |
| `construction-authoring-shape` | usa `artefacto`, no envelope externo. |

## Severidad y outcome

| Severidad de hallazgos | Outcome sugerido |
| --- | --- |
| sin hallazgos | `ready` |
| solo media o baja, no bloqueantes | `needs_repair` con deuda residual declarada |
| al menos una alta | `needs_repair` o `processing` segun disponibilidad del operador |
| dependencia faltante o decision editorial pendiente | `blocked` |

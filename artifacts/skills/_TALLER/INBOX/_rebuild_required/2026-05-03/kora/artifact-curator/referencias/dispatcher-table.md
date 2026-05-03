# Dispatcher table

Mapa operativo que la skill `artifact-curator` consulta para decidir, dado
un par `(intent, tipo)`, si delegar a una skill hermana o conducir la rama
aqui. Esta tabla **no** redefine reglas de las specs; es una vista de
trabajo. La SSOT son `gobernanza`, `autoria-spec`, `md-spec`,
`knowledge-spec` y `agent-skill-construction-spec`.

## Verbos canonicos de intent

| Verbo | Funtor categorial | Aplicabilidad |
| --- | --- | --- |
| `koraficar` | `K: DocHumano → KORA/MD` (descriptivo) | knowledge descriptivo, notas, guias |
| `cristalizar` | `C: Decisiones → KORA/Spec-MD` (prescriptivo) | familia `spec`, contratos, protocolos |
| `disenar` | `Build = Materialize ∘ Design : Req → IR` | skills, subagentes, agentes, agentes de plataforma |
| `auditar` | identidad con check de conformidad | toda familia y forma material |
| `editar` | morfismo controlado en IR preservando URN | toda familia y forma material |
| `reparar` | fix minimo preservando URN, familia y trazas | toda familia y forma material |
| `mejorar` | refinamiento aprobado con bump semver | toda familia y forma material |
| `deprecar` | transicion de lifecycle hacia `deprecado` o `retirado` | toda familia y forma material |

## Ruta por (intent, tipo)

Convencion: `→ skill` significa delegar; `=> conducir` significa que
artifact-curator ejecuta la rama directamente; `bloqueado` significa que
la combinacion no es valida y debe rechazarse.

### knowledge-descriptivo (familias `note`, `guide`, `glossary`, `faq`, `catalog`, `inventory`, `organigram`, `normative`)

| Intent | Ruta | Razon |
| --- | --- | --- |
| `koraficar` | → `urn:kora:artefacto:knowledge-curator` | ruta KB normal descriptiva esta encapsulada en la hermana. |
| `cristalizar` | bloqueado | knowledge descriptivo no se cristaliza; si emerge regla, reclasificar como `spec`. |
| `disenar` | => conducir | scaffold del artefacto descriptivo nuevo cuando aun no hay fuente humana. |
| `auditar` | => conducir | aplicar `md-spec §3-5` y `knowledge-spec §4`. |
| `editar` / `reparar` / `mejorar` | → `urn:kora:artefacto:knowledge-curator` o => conducir | hermana cuando el draft esta en `_SCRIPTORIUM/REVIEW`; conducir cuando es repair sobre publicado. |
| `deprecar` | => conducir | cambiar `status` a `deprecado` y dejar trazabilidad. |

### knowledge-atomic (familia `atomic`)

| Intent | Ruta | Razon |
| --- | --- | --- |
| `koraficar` | → `urn:kora:artefacto:atomize` | productor canonico unico (`knowledge-spec §12`). |
| `disenar` | bloqueado | el diseno de artefactos `atomic` lo hace `atomize` desde el corpus fuente. |
| `auditar` | => conducir | aplicar `md-spec §5.6.1`: enum cerrado de tipos, IDs `Pxxx` unicos, fuentes resolubles, indice de fuentes, FS=100%. |
| `reparar` | => conducir | reparacion manual permitida si declara `extensions.kora.atomic.hand_edited: true`. |
| `editar` / `mejorar` | => conducir | cambios sobre artefacto ya emitido por `atomize`. |
| `deprecar` | => conducir | transicion de lifecycle. |

### spec (familia documental `spec`)

| Intent | Ruta | Razon |
| --- | --- | --- |
| `koraficar` | bloqueado | una spec no se koraficar desde fuente humana descriptiva: emerge cristalizando. |
| `cristalizar` | => conducir | aplicar `md-spec §5.6.2` perfil prescriptivo: RFC 2119, `Traces to:`, regla+ejemplo+traza, invariantes prescriptivos. |
| `disenar` | => conducir | scaffold de spec nueva (template `md-spec §5.6.2.8`). |
| `auditar` | => conducir | checks prescriptivos completos + auto-declaracion de precedencia. |
| `editar` / `reparar` / `mejorar` | => conducir | preservar URN; bump semver segun alcance del cambio. |
| `deprecar` | => conducir | considerar `supersedes` desde la spec sucesora si existe. |

### skill (`forma_material: habilidad`)

| Intent | Ruta | Razon |
| --- | --- | --- |
| `koraficar` | bloqueado | una skill no se koraficar desde texto humano; se disena. |
| `cristalizar` | bloqueado | la cristalizacion vive en la capa de specs. |
| `disenar` | => conducir | aplicar `agent-skill-construction-spec` fases A→H + `autoria-spec §5.1` (dominio Π∈{1,2}, Μ∈{0,1}, Ξ∈{1,2}, Λ=0, Φ=1). |
| `auditar` | => conducir | autoria-spec §6 + §14, leyes inter-eje harness §4.1, fidelidad-agentskills via `kora transmute --target agentskills --dry-run`. |
| `editar` / `reparar` / `mejorar` | => conducir | preservar URN; bump major si cambia forma material o arnes. |
| `deprecar` | => conducir | lifecycle de ejecutables: `borrador → activo → deprecado → retirado`. |

### subagente / agente-propiamente-tal / agente-plataforma

| Intent | Ruta | Razon |
| --- | --- | --- |
| `disenar` | => conducir | aplicar `agent-skill-construction-spec` con dominio de proyeccion correspondiente (`autoria-spec §5.2-5.4`). Para `agente-plataforma`, exigir runtime con Μ=3 (hoy solo `openclaw`). |
| `auditar` | => conducir | shape condicional por forma material (`autoria-spec §6`), `compromisos_eticos` requerido en `agente-propiamente-tal` y `agente-plataforma`. |
| `editar` / `reparar` / `mejorar` | => conducir | preservar URN, respetar invariantes coalgebraicos cuando `verificacion_coalgebraica: true`. |
| `deprecar` | => conducir | retirar segun lifecycle, emitir reemplazo con `supersedes` si aplica. |

### tipo desconocido o intent ambiguo

| Caso | Ruta |
| --- | --- |
| intent ambiguo y operador disponible | emitir `outcome: blocked` con clarificacion solicitada. |
| flujo knowledge end-to-end donde aun no se decide familia | → `urn:kora:artefacto:curation-conductor`. |
| necesidad de enmarque categorial profundo antes de avanzar | → `urn:kora:artefacto:cat-thinking` y volver con la lectura. |

## Modo libre vs guiado

| Modo | Comportamiento |
| --- | --- |
| `libre` | clasificar y ejecutar la rama directamente. Outcome al cierre. |
| `guiado` | tras cada fase, invocar `urn:kora:artefacto:lifecycle-orchestrator` para consolidar checkpoint. El operador puede interrumpir cualquier fase. |

## Senales de delegacion explicita

La skill emite handoff (no retorno opaco) cuando delega a una hermana.
Contrato minimo del handoff:

- URN de la skill destino,
- intent y tipo confirmados,
- staging path candidato si aplica,
- conocimiento permitido relevante,
- outcome esperado del handoff (`processing`, `ready`, `needs_repair`).

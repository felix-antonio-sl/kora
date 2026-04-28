# Dispatcher table

Mapa operativo que la skill `kora-agents` consulta para decidir, dado
un par `(intent, forma_material)`, si delegar a otra skill o conducir
la rama aqui. La SSOT son `gobernanza`, `harness-spec`, `autoria-spec`
y `agent-skill-construction-spec`.

## Verbos canonicos de intent

| Verbo | Funtor categorial | Aplicabilidad |
| --- | --- | --- |
| `disenar` | `Build = Materialize ∘ Design : Req → IR` | construccion nueva desde requerimientos o staging |
| `mantener` | morfismo controlado en IR preservando URN | refactor, normalizacion, ajuste de campos |
| `mejorar` | refinamiento aprobado con bump semver | optimizacion legibilidad, comprimir grasa, ajustar `qa_budget` |
| `evolucionar` | promocion entre formas materiales | `subagente → agente-propiamente-tal → agente-plataforma` |
| `auditar` | identidad con check de conformidad | toda forma material |
| `deprecar` | transicion de lifecycle | `borrador → activo → deprecado → retirado` |

## Ruta por (intent, forma_material)

Convencion: `→ skill` significa delegar; `=> conducir` significa que
kora-agents ejecuta la rama directamente; `bloqueado` significa que la
combinacion no es valida.

### habilidad

| Intent | Ruta | Razon |
| --- | --- | --- |
| `disenar` / `mantener` / `mejorar` / `auditar` / `deprecar` | → `urn:kora:artefacto:kora-skills` | Skills (`forma_material: habilidad`) caen fuera del alcance de esta skill. Devolver handoff con outcome `rerouted`. |
| `evolucionar` (habilidad → subagente) | => conducir | Promocion entre formas materiales: el target ya es subagente, kora-agents ejecuta. |

### subagente

| Intent | Ruta | Razon |
| --- | --- | --- |
| `disenar` | => conducir | aplicar fases A→H de construction-spec con dominio Π∈{1,2,3}, Μ∈{0,1,2}, Ξ∈{1,2,3}, Λ=0-1, Φ∈{1,2}. |
| `mantener` / `mejorar` | => conducir | preservar URN; bump patch o minor segun alcance. |
| `evolucionar` | => conducir | promocion a `agente-propiamente-tal` (autoria-spec §8). Bump major obligatorio. |
| `auditar` | => conducir | autoria-spec §6, §14: shape condicional, fidelidad-mastra dry-run. |
| `deprecar` | => conducir | transicion lifecycle. Si emerge reemplazo, declarar `supersedes`. |

### agente-propiamente-tal

| Intent | Ruta | Razon |
| --- | --- | --- |
| `disenar` | => conducir | dominio Π∈{2,3}, Μ∈{2,3}, Ξ∈{2,3,4}, Λ∈{0,1,2}, Φ∈{1,2,3}. `compromisos_eticos` obligatorios. |
| `mantener` / `mejorar` | => conducir | preservar URN; respetar invariantes coalgebraicos cuando `verificacion_coalgebraica: true`. |
| `evolucionar` | => conducir | promocion a `agente-plataforma` exige Μ=3 y runtime que la soporte (hoy solo openclaw). |
| `auditar` | => conducir | autoria-spec §6, §14 + leyes inter-eje, fidelidad-mastra dry-run, coalgebra-conformance si aplica. |
| `deprecar` | => conducir | transicion lifecycle; emitir reemplazo con `supersedes` si aplica. |

### agente-plataforma

| Intent | Ruta | Razon |
| --- | --- | --- |
| `disenar` | => conducir | dominio Π∈{2,3}, Μ=3, Ξ∈{3,4}, Λ∈{1,2,3}, Φ∈{1,2,3}. Exige `extensions.{plataforma}` y materia ambiental (`MEMORY.md`, `HEARTBEAT.md` u equivalentes). |
| `mantener` / `mejorar` | => conducir | preservar URN; respetar runtime-extension de plataforma vigente. |
| `evolucionar` | bloqueado | `agente-plataforma` es el techo de la cadena. La democion esta prohibida. |
| `auditar` | => conducir | autoria-spec §5.4, §6, §14 + openclaw-runtime-extension cuando target es openclaw. |
| `deprecar` | => conducir | transicion lifecycle con coordinacion runtime; declarar handoff a la plataforma. |

### intent ambiguo o forma_material desconocida

| Caso | Ruta |
| --- | --- |
| intent ambiguo y operador disponible | emitir `outcome: blocked` con clarificacion solicitada. |
| forma material `habilidad` declarada | → `urn:kora:artefacto:kora-skills` con `outcome: rerouted`. |
| necesidad de enmarque categorial profundo antes de avanzar | → `urn:kora:artefacto:cat-thinking` y volver con la lectura. |

## Modo libre vs guiado

| Modo | Comportamiento |
| --- | --- |
| `libre` | clasificar y ejecutar la rama directamente. Outcome al cierre. |
| `guiado` | tras cada fase, invocar `urn:kora:artefacto:lifecycle-orchestrator` para consolidar checkpoint. El operador puede interrumpir cualquier fase. |

## Senales de delegacion explicita

Cuando kora-agents delega, emite handoff con contrato minimo:

- URN de la skill destino,
- intent y forma material confirmados,
- staging path candidato si aplica,
- conocimiento permitido relevante,
- outcome esperado del handoff.

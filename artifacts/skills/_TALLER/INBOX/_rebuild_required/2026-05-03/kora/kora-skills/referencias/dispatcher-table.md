# Dispatcher table

Mapa operativo que la skill `kora-skills` consulta para decidir, dado
un par `(intent, situacion)`, si delegar a otra skill o conducir la
rama aqui. La SSOT son `gobernanza`, `harness-spec`, `autoria-spec` y
`agent-skill-construction-spec`.

## Verbos canonicos de intent

| Verbo | Funtor categorial | Aplicabilidad |
| --- | --- | --- |
| `disenar` | `Build = Materialize ∘ Design : Req → IR` | construccion nueva desde requerimientos o staging |
| `mantener` | morfismo controlado en IR preservando URN | refactor, normalizacion, ajuste de campos |
| `mejorar` | refinamiento aprobado con bump semver | optimizacion legibilidad, comprimir grasa, ajustar `nivel_prescripcion`, reorganizar `referencias/` |
| `evolucionar` | promocion entre formas materiales | `habilidad → subagente` |
| `auditar` | identidad con check de conformidad | toda skill productiva |
| `deprecar` | transicion de lifecycle | `borrador → activo → deprecado → retirado` |

## Ruta por (intent, forma_material)

Convencion: `→ skill` significa delegar; `=> conducir` significa que
kora-skills ejecuta la rama directamente; `bloqueado` significa que la
combinacion no es valida.

### habilidad

| Intent | Ruta | Razon |
| --- | --- | --- |
| `disenar` | => conducir | aplicar fases A→H de construction-spec con dominio Π∈{1,2}, Μ∈{0,1}, Ξ∈{1,2}, Λ=0, Φ=1 y `nivel_prescripcion` obligatorio. |
| `mantener` / `mejorar` | => conducir | preservar URN; bump patch o minor segun alcance; comprimir body a ≤500 lineas si excede. |
| `evolucionar` | => conducir + handoff | promocion `habilidad → subagente` (autoria-spec §8); kora-skills ejecuta el cierre del shape habilidad y entrega handoff a `kora-agents` para materializar el subagente con shape expandido. Bump major obligatorio. |
| `auditar` | => conducir | autoria-spec §6, §14: shape condicional, skill-structure, fidelidad-agentskills dry-run, progressive-disclosure (≤500 lineas), recursos-documentados si hay subdirs. |
| `deprecar` | => conducir | transicion lifecycle. Si emerge reemplazo, declarar `supersedes`. |

### subagente / agente-propiamente-tal / agente-plataforma

| Intent | Ruta | Razon |
| --- | --- | --- |
| cualquiera | → `urn:kora:artefacto:kora-agents` | Forma material fuera del alcance de esta skill. Devolver handoff con outcome `rerouted`. |

### familia knowledge (note, guide, atomic, spec, etc.)

| Intent | Ruta |
| --- | --- |
| cualquiera | → `urn:kora:artefacto:artifact-curator` con `outcome: rerouted`. |

### intent ambiguo o forma_material desconocida

| Caso | Ruta |
| --- | --- |
| intent ambiguo y operador disponible | emitir `outcome: blocked` con clarificacion solicitada. |
| forma material declarada no es habilidad | → `urn:kora:artefacto:kora-agents` con `outcome: rerouted`. |
| necesidad de enmarque categorial profundo antes de avanzar | → `urn:kora:artefacto:cat-thinking` y volver con la lectura. |

## Modo libre vs guiado

| Modo | Comportamiento |
| --- | --- |
| `libre` | clasificar y ejecutar la rama directamente. Outcome al cierre. |
| `guiado` | tras cada fase, invocar `urn:kora:artefacto:lifecycle-orchestrator` para consolidar checkpoint. El operador puede interrumpir cualquier fase. |

## Senales de delegacion explicita

Cuando kora-skills delega, emite handoff con contrato minimo:

- URN de la skill destino,
- intent y forma material confirmados,
- staging path candidato si aplica,
- conocimiento permitido relevante,
- outcome esperado del handoff.

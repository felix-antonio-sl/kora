---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-28-curator-forgemaster-personas-omega"
  provenance:
    created_by: "FS"
    created_at: "2026-04-28"
    source: "Sesion 2026-04-28: refactor profundo de curator/forgemaster como skills + cristalizacion mente-omega/steipete/allan-kelly/david-allen como agentes y skills KORA-puros. v1.1 incorpora la integracion de OpenCode como septimo runtime target (commit 688e831)."
version: "1.1.0"
status: publicado
tags: [handoff, kora-skills, kora-agents, curator, forgemaster, mente-omega, steipete, allan-kelly, david-allen, opencode, autoria-spec, agent-skill-construction-spec, transmutation-spec]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:agent-skill-construction-spec"
    - "urn:kora:kb:transmutation-spec"
    - "urn:kora:kb:opencode-runtime-extension"
---

# Handoff 2026-04-28 — curator/forgemaster como skills + personas mente-omega/steipete/allan-kelly/david-allen + opencode runtime

## Estado actual

Repo KORA con **ciclo de vida agentico completo en skills + 3 personas
canonizadas + OpenCode como septimo runtime target**. Strict 30/30
verde, suite 329/329, 15 URNs productivos nuevos resuelven (14 del
bloque agentico + 1 spec runtime), 108 archivos tocados, 5 commits
en `master` push a `origin`:

```
688e831  feat(runtime): add opencode runtime target
e37649f  docs(kora): handoff 2026-04-28 curator/forgemaster + personas omega
750169b  feat(kora): mente-omega skill + steipete/allan-kelly/david-allen personas
26d04e0  feat(kora): trinity of artifact lifecycle skills
8507e2d  refactor(kora): retire legacy curator and forgemaster agents
```

### Trinidad de ciclo de vida (skills nuevas en `artifacts/skills/kora/`)

| URN | Cubre |
|---|---|
| `urn:kora:artefacto:artifact-curator` | Ciclo de vida general de artefactos KORA productivos (knowledge, spec, skill, agente). Delega a hermanas especializadas. |
| `urn:kora:artefacto:kora-skills` | Construccion/evolucion/auditoria/deprecacion de **skills** (`forma_material: habilidad`). |
| `urn:kora:artefacto:kora-agents` | Construccion/evolucion/auditoria/deprecacion de **agentes** (subagente, agente-propiamente-tal, agente-plataforma). |

Ambas hermanas componen con `artifact-curator` como ciclo de vida
general; entre ellas se intercambian handoffs en evolucion
`habilidad → subagente`.

### Pentamotor como skill (en `artifacts/skills/kora/`)

| URN | Cubre |
|---|---|
| `urn:kora:artefacto:mente-omega` | Pentamotor Φ Ψ Ξ Δ Σ como protocolo invocable: comprension-expresion-intervencion, vigilancia (9 interrupciones), generacion viva (anti-clausura), posicionamiento (problema-audiencia-accion-valor), transferencia multi-formato. |

Decision canonica: **Mente-Omega es metodo, no persona.** Razon: el
pentamotor es arquitectura cognitiva pura, sin workspace propio. Cualquier
agente que necesite producir artefactos cognitivo-discursivos invoca la
skill desde su propia identidad. La persona "Omega" del fleet OpenClaw
queda absorbida (los workspaces fleet siguen siendo responsabilidad de
`forjador-openclaw`).

### Skills doctrinales destiladas

| URN | Origen | Cubre |
|---|---|---|
| `urn:dev:artefacto:ship-discipline` | Doctrina Steinberger | blast radius, loop closure, ship-beats-perfect, architecture-over-implementation, repo-shaping agent-friendly, separacion de estratos humano/agente |
| `urn:fxsl:artefacto:cell-design` | Doctrina Allan Kelly | celulas humano-agente, intent contracts, autonomy envelopes, evals, control plane, debt audit (eval/context/autonomy/observability), recalibracion |
| `urn:pro:artefacto:gtd-flow` | David Allen + extension agentica | loop de 7 movimientos (recuperar-estado, capturar, clarificar, organizar, comprometer, revisar, regenerar), decision router, contrato de delegacion, recovery protocols |

Cada skill destila las skills CM-* dispersas del fleet OpenClaw en un
nucleo unico. Las skills CM-* del workspace OpenClaw original quedan
fusionadas en estos 4 supertools KORA-nativos.

### 3 agentes nuevos (persona, agente-propiamente-tal)

| URN | Path | Persona |
|---|---|---|
| `urn:dev:artefacto:steipete` | `artifacts/agents/dev/steipete/` | Director ejecucion cognitiva (Peter Steinberger clon) |
| `urn:fxsl:artefacto:allan-kelly` | `artifacts/agents/fxsl/allan-kelly/` | Arquitecto organizacional human-agent |
| `urn:pro:artefacto:david-allen` | `artifacts/agents/pro/david-allen/` | Maestro de claridad integral (GTD + regulacion + co-agencia) |

Cada agente declara la skill nuclear correspondiente en
`componible_con` + `mente-omega` + `cat-thinking` + `artifact-curator`.
Compromisos eticos completos. Memoria persistente
(`memoria_config: persistente, ambito: usuario`). Vector tipico
Π=2 Μ=2 Ξ=2-3 Λ=0-1 Φ=2.

### Knowledge promovido

- `urn:dev:kb:peter-steinberger-ingeniero-agentico-prodigio` →
  productivo en `artifacts/knowledge/dev/perfiles/`.
- `urn:pro:kb:david-allen-integral-definitivo-septiembre-2026` →
  productivo en `artifacts/knowledge/pro/perfiles/`. **Reorganizado**
  para cumplir `lint-md`: §6.6 oversized splitteado en §6.6-§6.15;
  §9 y §10 con intros agregadas.
- `urn:fxsl:kb:allan-kelly-gemelo-digital-intelectual` ya estaba
  publicado en `fxsl/xanpan/`, sin tocar.

### Retiros ejecutados

| Artefacto | Razon |
|---|---|
| `artifacts/agents/kora/curator/` (workspace + 35 archivos) | Reemplazado por `urn:kora:artefacto:artifact-curator` skill. URN libre para futuro uso. |
| `artifacts/agents/kora/forgemaster/` (workspace + 35 archivos) | Reemplazado por skills hermanas `kora-skills` + `kora-agents`. URN libre. |
| `_FRAGUA/INBOX/steipete/` (legacy v1 con AGENTS.md/IDENTITY.md/SOUL.md/TOOLS.md/USER.md/config.json/skills) | Shape pre-autoria-spec. |
| `_FRAGUA/REVIEW/steipete/AGENT.md` (draft v2.0 orquestador Ξ=4) | Reemplazado por agente productivo `dev/steipete` con vector persona Π=2 Μ=2 Ξ=3 Λ=1 Φ=2. |
| `urn:omega:kb:mente-omega-arquitectura-cognitiva` (REVIEW) | Metodo absorbido como skill ejecutable; la nota descriptiva queda redundante. |

### Cambios de soporte

- `toolchain/kora_lib/config.py`: `META_KORA_AUDIT_WORKSPACES` y
  `META_KORA_STATUS` reducidos a `kora/guardian` + `kora/custodio`
  (operating core de 2).
- `tests/fixtures/operating-core-scenarios.json`: fixture reescrito al
  operating core de 2.
- `tests/test_cli_smoke.py`: sample de transmute movido a `kora/custodio`.
  Expectativas `total_workspaces`/`operating_core` actualizadas a 2.
  `test_transmute_accepts_all_six_targets` (era `_five_`) y
  `test_ingest_subcommand_exists` extendidos con `opencode`.
- `tests/test_artifacts.py` y `tests/test_operating_core_scenarios.py`:
  ~14 tests acoplados al curator/forgemaster legacy eliminados; tests
  compartidos reducidos a `custodio` + `guardian`.
- Skills hermanas (`intent-classifier`, `lifecycle-orchestrator`,
  `context-manager`): `componible_con` apunta ahora a las skills nuevas.

### OpenCode como septimo runtime target

Se incorpora **OpenCode** (https://opencode.ai/docs/) como septimo
target alongside claude-code, codex, gemini, mastra, openclaw y
agentskills. Spec nueva: `runtime/opencode-runtime-extension.md` v1.0.0
(URN `urn:kora:kb:opencode-runtime-extension`, status `publicado`,
family `spec`, 428 lineas).

**Dominio de proyeccion:**

| Eje | Dominio OpenCode |
|---|---|
| Π | 0-3 (Π=3 partial, acotado por campo `steps`) |
| Μ | 0-1 full, 2 partial (sessions parent/child sin `memory: user` transparente), 3 none |
| Ξ | 0-2 full, 3 partial (subagent `@mention` + Task tool con permission gates), 4 partial |
| Λ | 0-1 full, 2 partial, 3 none |
| Φ | 0-2 full (permission `ask` materializa HOTL granular), 3 partial, 4 none |
| Σ | safety_norm 3, fairness 2, transparency 2, accountability 2, sustainability 1 |

**Formas materiales soportadas:**

| Forma material | Fidelidad | Ubicacion runtime |
|---|---|---|
| `habilidad` | fiel | `.opencode/skills/{name}/SKILL.md` (compat `.claude/skills/`, `.agents/skills/`) |
| `subagente` | fiel | `.opencode/agents/{name}.md` con `mode: subagent` |
| `agente-propiamente-tal` | parcial | `.opencode/agents/{name}.md` con `mode: primary` o `all` |
| `agente-plataforma` | no soportado | OpenCode CLI/TUI sincrono, no daemon |

**Toolchain extendido:**

- `transmute.py`: `PRESERVATION_MATRIX["opencode"]`,
  `TARGET_ADAPTERS["opencode"]`, `TRACE_FIDELITY_BY_TARGET["opencode"]`.
- `cli.py`: `kora ingest --from {claude-code,codex,gemini,opencode,openclaw}`.
- `kora transmute --target` reconoce `opencode` automaticamente
  (derivado de `PRESERVATION_MATRIX.keys()`).

**Coordinacion de specs (fix puntual de listas, dentro de Fase 3 freeze):**

- `gobernanza §3.2` y `§8.2`: `opencode-runtime-extension` agregado a
  runtime-extensions canonicas y al critical-path de runtimes.
- `transmutation-spec §1` y `§12`: OpenCode listado entre runtimes
  soportados.
- `autoria-spec §12`: matriz de realizabilidad gana fila OpenCode
  (`fiel/fiel/parcial/no-soportado`).

**Rasgos distintivos:**

- **Skills byte-identical cross-runtime**: una habilidad KORA
  transmutada a agentskills.io vive directamente en `.opencode/skills/`
  o `.claude/skills/` sin paso adicional. OpenCode descubre desde cwd
  hasta git worktree root.
- **Permission system granular** por key (`read`, `edit`, `bash`,
  `skill`, `task`, `external_directory`, etc.) con `allow|deny|ask` +
  patrones glob. Materializa HOTL mas fino que Codex approval modes.
- **`mode: all`** es OpenCode-especifico: agente que opera como
  primary o subagent segun contexto. Proyecta ambivalente al IR.
- **Built-in agents** (`build`, `plan`, `general`, `explore`, system
  hidden `compaction`/`title`/`summary`): runtime-nativos, NO se
  transmutan desde KORA IR.
- **Sessions jerarquicas** parent/child con navegacion (`session_child_*`)
  para flujos multi-agente.

**Lift status:**

| Tipo | Estado | Mecanismo |
|---|---|---|
| Skill OpenCode → KORA IR | v1.0 disponible | `_lift_codex_skill` (compat agentskills.io) |
| Agente OpenCode → KORA IR | pendiente v1.1 | Lifter dedicado para `.md` con `mode`/`permission`/`prompt` |

## Decisiones canonicas

| Decision | Justificacion |
|---|---|
| Mente-Omega como skill, no como persona | Metodo / arquitectura cognitiva pura; sin materia propia. La lectura categorial mas debil suficiente (`cat-thinking`). |
| URNs nuevos en lugar de reusar `urn:kora:artefacto:curator` y `urn:kora:artefacto:forgemaster` | `autoria-spec §8.2` prohibe democion sobre el mismo URN. Los agentes legacy se retiran y los URNs quedan libres para futuro uso (no reemplazo). |
| 3 personas como `agente-propiamente-tal` separados de sus skills | Composicion vs anidamiento: la skill encarna la tecnica, el agente aporta identidad/voz/memoria/limites. Reusable por otros agentes. |
| Agente OpenClaw fleet NO modificado | Fuera del alcance KORA. Las fuentes IR creadas son lo que esos workspaces transmutarian via `kora transmute --target openclaw`. La decision de archivar/fusionar/divergir queda al `forjador-openclaw`. |
| `lint-md` strict aplicado al perfil David Allen al promoverlo | Operadores KORA-puros: knowledge productivo cumple `md-spec §5` sin excepciones. |
| OpenCode integrado como fix puntual (no rediseño) dentro del freeze formal de Fase 3 | Cambios solo enumerativos en gobernanza/transmutation-spec/autoria-spec (listas de runtime-extensions y matriz de realizabilidad). Sin tocar leyes ni regimenes URN. La nueva spec runtime es aditiva. |
| `mode: all` de OpenCode proyecta ambivalente al IR | Es el unico runtime con esta primitiva. La transmutacion decide segun uso real (subagente o agente-propiamente-tal); la ingesta inversa (`Lift_opencode`) preserva el `mode: all` en `extensions.opencode.mode` para retomar luego. |
| Built-in agents OpenCode no se transmutan desde IR | `build`, `plan`, `general`, `explore`, `compaction`, `title`, `summary` son runtime-nativos. Si un artefacto KORA cumple su funcion, se proyecta como agente custom adicional. |

## Pendientes

### Knowledge

- Specs INBOX `_SCRIPTORIUM/INBOX/omega/*` (4 archivos, 4197L total) siguen
  en INBOX como insumo de diseño. Decision pendiente: archivar como
  referencias historicas o destruir tras consolidar el destilado en
  skills.
- `_FRAGUA/INBOX/perfiles/` y otros perfiles intelectuales del fleet
  no procesados todavia. Aplicar la misma metodologia (perfil knowledge
  + skill destilada + agente persona) cuando aplique.

### OpenClaw fleet

El audit de `~/openclaw-fleet/docs/audits/2026-04-27-fleet-structural-audit.md`
identifica decisiones operativas que **no son alcance KORA**:

- `gtd-integral` (sin contacto Telegram, vacio operacional total) →
  archivar o dar disparador real.
- `allan-kelly` (18d sin uso, heartbeat ya off) → bajo demanda
  permanente o archivar.
- `fugaz` ↔ `steipete` (~80% solapamiento) → fusionar, heredar
  formalmente o divergir con rol distinto.
- `mente-omega` (16d gap) → ahora que el metodo es skill KORA, evaluar
  si el workspace fleet sigue tiene razon de existir como agente
  separado o si cualquier agente fleet con la skill basta.
- Bundling de skills duplicadas (`opm-modeler` x6, `arquitecto-categorico`
  x3, `kv-*` x5) → consolidacion fleet, separada del IR canonico.

Estas decisiones se delegan a `forjador-openclaw` cuando Felix las
aborde. Las fuentes IR canonicas para transmutar a OpenClaw ya estan
listas en KORA.

### Toolchain / tests

- 1 skip esperado en suite (workspace productivo opcional).
- 3 warnings LOW pre-existentes en otros artefactos del corpus que
  pueden surgir si se promueve mas knowledge desde REVIEW.

## Supuestos

1. **Felix mantiene operating core meta-kora reducido a 2** (guardian +
   custodio) tras retiro de curator/forgemaster. Si decide reincluir
   nuevos agentes meta-kora, debe agregarse a
   `META_KORA_AUDIT_WORKSPACES`.
2. **Los workspaces OpenClaw fleet siguen activos** (steipete, fugaz,
   mente-omega, allan-kelly, gtd-integral, salubrista, main) hasta que
   Felix decida explicitamente archivarlos. KORA no toca el fleet.
3. **Los URNs `urn:kora:artefacto:curator` y `urn:kora:artefacto:forgemaster`**
   quedan libres y disponibles para reasignacion futura. Felix puede
   reusarlos si lo desea (e.g., como wrappers personas delgados).
4. **`mente-omega` skill es invocable por todos los runtimes**:
   `claude-code, codex, gemini, mastra, openclaw`. La fidelidad a
   agentskills.io se verifica con
   `kora transmute --target agentskills --dry-run`.
5. **Las 3 personas se transmutan a OpenClaw** cuando se decida desplegar
   el workspace fleet correspondiente. Hoy estan en KORA como IR
   fuente.

## Riesgos

| Riesgo | Severidad | Mitigacion |
|---|---|---|
| Drift entre fleet OpenClaw vivo y IR KORA productivo | Media | Forjador-openclaw debe alinear o archivar diferencia explicita |
| Perfil intelectual David Allen reorganizado pierde semantica fina | Baja | El reorden es solo split de chunk + intros; nucleo intacto. Validacion: `kora lint-md` verde. |
| Skills nuevas sin probar en runtime real | Media | El IR pasa todos los gates de construccion; falta evidencia de uso real con un agente invocador. Primer test: invocar `mente-omega` desde `steipete` o `polymath`. |
| URN `urn:kora:artefacto:curator` reaparece en otro contexto sin coordinacion | Baja | Si Felix lo reusa, debe coordinar con esta decision (es reasignacion legitima, no resurreccion). |
| Agente vestigial polymath (en _FRAGUA/REVIEW) con `componible_con` actualizado pero sin promocion | Baja | El draft sigue en REVIEW; la actualizacion lo deja listo para futuras decisiones. |
| Bug pre-existente en `_project_axis` reporta `comment` (3er elemento de tupla) como `loss` en matriz codex/gemini/opencode | Baja | No bloqueante para checks; afecta solo legibilidad del dry-run. Limpieza pendiente cuando se toque transmute.py |
| Lift de agents OpenCode (`mode`/`permission`/`prompt`) usa lifter de skill como fallback | Baja | Pendiente lifter dedicado v1.1; mientras tanto, agents OpenCode se ingestan manualmente o via skill-lifter con TODO en el frontmatter |

## Comandos de continuidad

```bash
# Verificar estado
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests

# Resolver URNs canonicos de la sesion
python3 toolchain/kora resolve urn:kora:artefacto:artifact-curator
python3 toolchain/kora resolve urn:kora:artefacto:kora-skills
python3 toolchain/kora resolve urn:kora:artefacto:kora-agents
python3 toolchain/kora resolve urn:kora:artefacto:mente-omega
python3 toolchain/kora resolve urn:dev:artefacto:steipete
python3 toolchain/kora resolve urn:fxsl:artefacto:allan-kelly
python3 toolchain/kora resolve urn:pro:artefacto:david-allen
python3 toolchain/kora resolve urn:kora:kb:opencode-runtime-extension

# Probar transmutacion (dry-run) cuando se vaya a desplegar
python3 toolchain/kora transmute --target openclaw --agent dev/steipete --dry-run
python3 toolchain/kora transmute --target opencode --agent dev/steipete --dry-run
python3 toolchain/kora transmute --target agentskills --agent kora/mente-omega --dry-run

# Verificar que los 7 targets aparecen en CLI help
python3 toolchain/kora transmute --help
python3 toolchain/kora ingest --help
```

## Artefactos relevantes (resumen completo)

### Creados (15 URNs productivos)

Skills agenticos (7):

```
urn:kora:artefacto:artifact-curator   skill (kora)
urn:kora:artefacto:kora-skills        skill (kora)
urn:kora:artefacto:kora-agents        skill (kora)
urn:kora:artefacto:mente-omega        skill (kora)
urn:dev:artefacto:ship-discipline     skill (dev)
urn:fxsl:artefacto:cell-design        skill (fxsl)
urn:pro:artefacto:gtd-flow            skill (pro)
```

Agentes persona (3):

```
urn:dev:artefacto:steipete            agente-propiamente-tal (dev)
urn:fxsl:artefacto:allan-kelly        agente-propiamente-tal (fxsl)
urn:pro:artefacto:david-allen         agente-propiamente-tal (pro)
```

Spec runtime (1):

```
urn:kora:kb:opencode-runtime-extension   spec runtime (kora)
```

Knowledge promovido a productivo (2, status: borrador → publicado):

```
urn:dev:kb:peter-steinberger-ingeniero-agentico-prodigio
urn:pro:kb:david-allen-integral-definitivo-septiembre-2026
```

Handoff master (1):

```
urn:kora:kb:handoff-2026-04-28-curator-forgemaster-personas-omega
```

### Retirados (3 URNs)

```
urn:kora:artefacto:curator                       (agente-propiamente-tal v3.0.0)
urn:kora:artefacto:forgemaster                   (agente-propiamente-tal v2.0.0)
urn:omega:kb:mente-omega-arquitectura-cognitiva  (knowledge note REVIEW)
```

URNs `curator` y `forgemaster` quedan libres para reasignacion futura.

### Topologia de runtimes soportados (post-sesion)

KORA proyecta a **7 targets** mediante `kora transmute --target`:

```
agentskills    meta-runtime byte-identical
claude-code    Anthropic Claude Code CLI
codex          OpenAI Codex CLI
gemini         Google Gemini CLI
mastra         Mastra agent framework
opencode       OpenCode CLI multi-provider (incorporado en esta sesion)
openclaw       OpenClaw fleet (unico que soporta Mu=3 / agente-plataforma)
```

Cada target tiene su `runtime-extension` con dominio + matriz de
preservacion. Los 7 patrones siguen estructura paralela (definicion,
formas materiales, matriz por eje, dimension runtime-ortogonal,
metadata de encaje, lift inverso, validacion).

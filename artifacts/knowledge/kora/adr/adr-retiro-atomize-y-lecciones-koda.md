---
_manifest:
  urn: urn:kora:kb:adr-retiro-atomize-y-lecciones-koda
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-20'
    source: 'Directiva HITL del operador 2026-05-20: sacar todo lo de atomize de lo
      relacionado a knowledge; volver a la filosofia antigua koda (en /home/felix/_TEMP_BORRAR/koda)
      como referencia para simplificar y fortalecer KORA. No replicar.'
version: 1.0.0
status: publicado
tags:
- adr
- retiro-atomize
- lecciones-koda
- simplificacion
- knowledge
lang: es
extensions:
  kora:
    family: adr
    adr:
      contexto: 'Directiva HITL del operador 2026-05-20: retirar atomize del dominio
        knowledge y volver a la filosofia antigua KODA como referencia (no replicacion).
        KORA acumulo complejidad alrededor de atomize (familia atomic, productor canonico,
        segmentacion 200 props, IDs Pxxx, enum cerrado de 11 tipos, acceptance review
        separado, ~25 archivos en skill productivo, 225 artefactos en REVIEW). La
        filosofia KODA antigua koraficaba documentos sin necesidad de atomizar en
        proposiciones.'
      alternativas:
      - 'Status quo: mantener atomize como familia atomic + productor canonico + 225
        artefactos en REVIEW'
      - 'Retiro parcial: deprecar familia atomic pero mantener skill atomize productivo'
      - 'Retiro completo del dominio knowledge: archivar skill, mover artefactos a
        INBOX raw, limpiar specs y toolchain'
      factorizacion_elegida: decision = archivar_skill ∘ mover_artefactos_a_INBOX_raw
        ∘ retirar_familia_atomic ∘ limpiar_toolchain_atomic ∘ preservar_URNs_para_trazabilidad
      consecuencias:
      - Familia atomic eliminada de md-spec §5.6
      - Productor canonico atomic eliminado de knowledge-spec §9
      - Skill artifacts/skills/kora/atomize/ archivado en governance/decisiones-archivadas/skills-retiradas/
      - 225 artefactos atomic-* en REVIEW movidos a _SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/
        (vuelven a material crudo, sin URN canonico)
      - CLI subcommand `kora atomize` retirado
      - Constantes ATOMIC_* y checks atomic en validation.py retirados
      - Tests atomic-related limpiados; test_atomize.py eliminado
      - KORA queda sin productor canonico en knowledge-spec §9 (seccion mantenida
        con tabla vacia para futuras familias)
      - URNs de artefactos atomic-* dejan de existir; ya estaban en REVIEW (borrador),
        no en productivo
      - Skill atomize URN urn:kora:artefacto:atomize queda como artefacto retirado
        preservando trazabilidad
      estado: aceptada
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:adr-retiro-atomize-y-lecciones-koda
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:md-spec
  - urn:kora:kb:knowledge-spec
  - urn:kora:kb:adr-kora-v7-esencial
  refines:
  - urn:kora:kb:adr-kora-v7-esencial
---

# ADR — Retiro de atomize del knowledge + Lecciones KODA antigua

## Contexto

Directiva HITL del operador (2026-05-20):

> "Quiero que se saque todo lo de atomize de lo relacionado a
> knowledge. Volvamos a la filosofia antigua [en /home/felix/_TEMP_BORRAR/koda]
> (no digo que lo repliquemos, solo que tengas como referencia para
> simplificar y fortalecer KORA)."

### Estado pre-decision

Atomize era un sistema vasto en KORA al 2026-05-20:

| Componente | Volumen |
|------------|---------|
| Skill productivo `artifacts/skills/kora/atomize/` | ~25 archivos (SKILL.md + 9 scripts Python + 9 referencias + _BUILD/) |
| Artefactos `atomic-*` en `_SCRIPTORIUM/REVIEW/` | 225 archivos en 4 namespaces (kora, pro, fxsl, hi) |
| Familia `atomic` en `md-spec §5.6` | tabla + §5.6.1 enum cerrado de 11 tipos de proposicion + reglas |
| Productor canonico en `knowledge-spec §9` | seccion completa atomize como unica ruta de emision atomic |
| Toolchain Python | `kora_lib/atomize.py` modulo entero + refs en cli/validation/migration/promote |
| Tests | `tests/test_atomize.py` + refs en 3 tests mas |
| Constantes | `ATOMIC_PRODUCER_URN`, `ATOMIC_HARD_MAX_PROPOSITIONS=200`, `ATOMIC_SOFT_SEGMENT_TARGET_CHARS=15000`, `ATOMIC_ALLOWED_TYPES` (11 tipos) |
| Checks | acceptance review separado, ID Pxxx unicos global, segmentacion ~15K chars / max duro 200 props, dedup multi-source, tension type |

### Filosofia KODA antigua (referencia, no replicacion)

Los 5 documentos `guide_core_*_koda.yml` en `_TEMP_BORRAR/koda`
muestran un sistema **mas simple y mas concentrado**:

- **Formato base**: YAML con keywords semanticos controlados
 (Tier 1 core: `Def`, `Act`, `Cond`, `Req`, `Ref`, `XRef`, `Ctx`, `Purp`,
 `Mssn`, `Obj`, `Proc`, `Src`, `Prohib`, `Ex`, `Just`, `Rec` + Tier 2
 abierto pero auto-explicativo).
- **3 capas conceptuales**: Definition (KODA/Agent), Knowledge
 (KODA/Spec), Specialized (SFD).
- **5 documentos core suficientes**: spec, transform, life, agent-spec,
 agent-construct. Sin productor canonico atomize.
- **Compresion + fidelidad** como invariantes: meat/fat/skeleton,
 FS=100%, CR>1.0.
- **Cross-references estrictas**: `Ref` interno, `XRef`/`XRef_Required`
 externo via URN.
- **Categorical foundations explicitas**: Agent as Formal Category,
 Functor, Monad — sin sobre-formalizacion.
- **Anti-patterns enumerados** en cada spec.

KODA antigua **no necesitaba atomize** para producir conocimiento
RAG-eficiente. La compactacion ocurria al koraficar (Transform); las
proposiciones no se descomponian en items separados con IDs Pxxx.

## Alternativas consideradas

### A1. Status quo (no hacer nada)

Mantener atomize como esta.

**Por que NO**: contradice la directiva HITL explicita. El operador
declaro que atomize debe salir.

### A2. Retiro parcial (deprecar familia, mantener skill)

Marcar `atomic` como deprecada en md-spec pero conservar el skill
productivo.

**Por que NO**: deja deuda mixta. El operador pidio "sacar todo lo de
atomize de lo relacionado a knowledge", no deprecacion parcial.

### A3. Retiro completo del dominio knowledge (elegida)

Archivar el skill productivo, mover los 225 artefactos a `_SCRIPTORIUM/INBOX/`
como material crudo (sin URN canonico), retirar familia atomic de
md-spec, retirar productor canonico de knowledge-spec, limpiar toolchain
y tests.

**Por que SI**:
- Refleja exactamente la directiva HITL.
- Reduce drasticamente la superficie de conceptos en KORA.
- Convergente con la filosofia antigua KODA (simplicidad).
- Preserva trazabilidad: el skill archivado mantiene URN; los artefactos
 vuelven a INBOX como crudo (sin URN canonico ya que estaban en
 REVIEW, no en productivo).

## Decision

**Retiro completo de atomize del dominio knowledge** en una sola
operacion coordinada (esta sesion).

### Acciones

| # | Accion | Detalle |
|---|--------|---------|
| A | Archivar skill productivo | `artifacts/skills/kora/atomize/` → `governance/decisiones-archivadas/skills-retiradas/atomize/`. Status `retirado`. URN preservado. |
| B | Mover artefactos REVIEW | 225 archivos `atomic-*` → `_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/`. Vuelven a material crudo sin URN canonico (estaban en borrador, no en productivo). |
| C | Retirar familia atomic de `md-spec` | §5.6 tabla: eliminar fila atomic. §5.6.1 enum cerrado: eliminar entera. §6.5 r4-7: reglas de segmentacion atomic eliminadas. §6.10: check ultimo eliminado. §9 tabla: 6 checks atomic eliminados. |
| D | Retirar productor canonico de `knowledge-spec` | §9 reducida: registro vacio + nota de retiro. §13 CLI: `kora atomize` eliminado. |
| E | Limpiar toolchain | CLI: subcommand `atomize` eliminado. validation.py: constantes y checks atomic eliminados. promote.py: validate_atomic_acceptance_review removido. cli.py + transmute.py refs limpiados. |
| F | Limpiar tests | `tests/test_atomize.py` eliminado. test_artifacts.py: assertions sobre atomic en specs actualizadas. test_autoria_validate.py: refs atomic eliminadas. test_migrate_autoria.py: skiplist atomize actualizada. |
| G | Bump versiones | `md-spec v9.0.0 → v10.0.0` (major, removal de familia). `knowledge-spec v2.0.0 → v3.0.0` (major, removal de productor canonico). |

### Lo que NO se retira

- El **concepto** de proposicion atomica como **idea** (sigue siendo
 parte del lexico KORA en `md-spec §2` definiciones).
- El skill `atomize` queda **archivado**, no destruido. Si se necesita
 reactivar (HITL futuro), el archivo y el codigo estan en
 `decisiones-archivadas/skills-retiradas/`.
- Los 225 artefactos `atomic-*` quedan en `_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/`
 como referencia material. Pueden re-koraficarse con un metodo distinto
 (siguiendo la filosofia KODA: koraficar sin atomizar) si se desea.

## Lecciones KODA antigua aplicables a KORA (referencia, no replicacion)

Estas son lecciones que se **anotan como direccion futura**, no se
implementan en este ADR:

### L1. Vocabulario controlado tier 1 / tier 2

KODA distinguia:
- **Tier 1 (core estructural)**: 19 keywords reservados con semantica
 fija (Def, Req, Act, Cond, Ref, XRef, Ctx, Purp, Mssn, Obj, Proc,
 Src, Prohib, Ex, Just, Rec, Warn, etc.).
- **Tier 2 (dominio)**: vocabulario abierto auto-explicativo
 (Symptoms, Risk_Factors, Pregunta_Clave, etc.).

KORA hoy usa Markdown libre. Aplicacion futura: si compactamos
specs (Fase 2b), podriamos introducir un perfil prescriptivo mas
denso usando estos keywords como marcas semanticas en tablas
declarativas.

### L2. Cross-references estrictas

KODA distinguia `Ref` (interno al artefacto) de `XRef`/`XRef_Required`
(externo via URN). KORA hoy mezcla refs en `relations` con citas en
body. Aplicacion futura: distincion explicita.

### L3. Compactacion sin atomizacion

KODA producia documentos densos sin descomponer en proposiciones
individuales. La fidelidad FS=100% se alcanzaba por **telegrafizacion +
deduplicacion via Ref interno**, no por extraccion de items.

KORA queda con `md-spec §6` (koraficacion) que ya captura este metodo.
La familia atomic era una **especializacion costosa** que el operador
declara innecesaria.

### L4. Anti-patterns explicitos

KODA enumeraba anti-patterns con `Wrong:` / `Right:` / `Why_Wrong:`.
KORA `md-spec §5.4.2` ya tiene 7 contraejemplos. La leccion: cada spec
KORA podria cerrar con una mini-seccion de anti-patterns para guiar al
operador/agente.

### L5. Categorial foundations sin sobre-formalizacion

KODA usaba "functor, monad, morphism" pero solo cuando aportaban
claridad. KORA hoy tiene muchos artefactos con notacion categorial
(ICAS-BoK, cat-thinking). La leccion: la formalizacion sirve si
materializa enforcement; cuando es decorativa, daña.

### L6. Knowledge cartography explicita

KODA tenia `CM-KB-GUIDANCE` (cognitive model que mapeaba queries a
artefactos). KORA tiene `kora kb-graph` que materializa el grafo
relacional. La leccion: el grafo debe ser **navegable**, no solo
auditable.

### L7. Token economy

KODA principle: "Eliminate explanatory verbosity; LLM-first design;
CR>1.0". KORA tiene FS=100% y CR>1.5. La leccion: en Fase 2b
(compactacion de autoria-spec, md-spec, transmutation-spec) este
principio debe guiar las decisiones de poda.

## Consecuencias

### Positivas

- **Simpleza visible**: 225 artefactos + skill ~25 files + 30 refs en
 specs + 4 archivos tests + tabla §5.6.1 enum cerrado de 11 tipos +
 4 reglas de segmentacion **eliminados o archivados**.
- **Convergencia con KODA antigua**: el sistema queda mas cerca de la
 filosofia esencial sin replicarla.
- **Catalogo limpio**: 638 → ~430 entries (caen los 225 atomic + 1
 skill productivo).
- **Toolchain mas simple**: 1 subcommand CLI menos, 1 modulo Python
 archivable, 4-5 checks atomic eliminados.

### Negativas

- **Volumen de cambios**: ~250 archivos movidos + 2 specs editadas +
 4-6 archivos toolchain modificados + 4 tests actualizados. Riesgo
 bajo (todo en una pasada bien planificada), pero amplio.
- **Si el operador quisiera atomizacion futura**: el skill archivado
 esta disponible para reactivar, pero el costo de reintegracion seria
 significativo.

### Riesgos

- **Posible referencia residual**: artefactos productivos que tuvieran
 `cites` a artefactos `atomic-*` deprecados — verificar.
- **Tests que asuman comportamiento atomic** — actualizar.

## Trazabilidad

- Esta ADR refines `urn:kora:kb:adr-kora-v7-esencial` (que ya bajo el
 freeze parcial; este retiro es operacionalmente consistente).
- Filosofia KODA antigua: `/home/felix/_TEMP_BORRAR/koda/guide_core_*.yml`
 (referencia local, no incluida en el corpus KORA porque es material
 externo historico).

## Estado

`aceptada` — implementacion en mismo commit que produce este ADR.

---
_manifest:
  urn: urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-20'
    source: 'Directiva HITL del operador 2026-05-20: especificacion para documentos
      descriptivos y prescriptivos diferenciadas; skills y agents pueden ser lo mismo
      pero varian por el arnes.'
version: 1.0.0
status: publicado
tags:
- adr
- kora-v9
- separacion-md-spec
- arnes-discriminante
- skill-agent-unificacion
lang: es
extensions:
  kora:
    family: note
    adr:
      contexto: 'Directiva HITL operador 2026-05-20: dos cambios doctrinales relacionados
        — (1) separar md-spec en spec descriptiva pura + spec prescriptiva separada
        (spec-md); (2) reconocer que skills y agents son ontologicamente el mismo
        objeto, distinguidos solo por el arnes categorial. Estado pre-decision: md-spec
        v10 mezcla regimenes descriptivo y prescriptivo en una sola spec (~980 lineas,
        §5.6.1 perfil spec con 9 subsecciones, §7.6 integridad prescriptiva, 9 filas
        spec en tabla §9). autoria-spec v1.2 distingue 4 formas materiales (habilidad,
        subagente, agente-propiamente-tal, agente-plataforma) como categorias paralelas;
        pero la distincion real categorial es el arnes (utilidad, disciplina, delegado,
        persona, orquestador, servicio, arquetipo).'
      alternativas:
      - 'Status quo: una sola spec con dos regimenes; skill/agent como categorias
        paralelas'
      - Solo separar specs (sin tocar autoria)
      - Solo refactor autoria (sin separar md-spec)
      - Ambos cambios coordinados (elegida)
      factorizacion_elegida: decision = extraer_spec_md_de_md_spec ∘ reducir_md_spec_a_descriptivo
        ∘ declarar_arnes_como_discriminante ∘ proyectar_forma_material_como_derivada
        ∘ preservar_topologia_fisica_skills_agents
      consecuencias:
      - 'md-spec v10 → v11: ~700 lineas, descriptivo puro'
      - 'spec-md v1.0 nueva: ~250 lineas, perfil prescriptivo extraido'
      - Familia spec en md-spec §5.6 apunta a spec-md para invariantes
      - 'autoria-spec v1.2 → v2.0: arnes declarado discriminante ontologico; forma
        material proyeccion operacional'
      - SKILL.md y AGENT.md preservados como conveniencia operacional; 41 artefactos
        productivos no se mueven
      - 'gobernanza §3 taxonomia: spec-md vuelve al canon (estaba retirada desde v8);
        spec-md se ubica en serializacion'
      - 'tests test_artifacts.py: refs a md-spec §5.6.1.X actualizadas a spec-md §X'
      - El URN urn:kora:kb:spec-md regresa al catalogo (era retirado en md-spec v8)
      estado: aceptada
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:md-spec
  - urn:kora:kb:autoria-spec
  - urn:kora:kb:adr-kora-v7-esencial
  refines:
  - urn:kora:kb:adr-kora-v7-esencial
---

# ADR — KORA v9: Separacion descriptivo/prescriptivo + arnes como discriminante

## Contexto

Directiva HITL del operador (2026-05-20):

> "specificación para documentos descriptivos, presciptivos diferenciadas.
> tambien considerar que skills y agents pueden ser lo mismo pero varían
> por el arnés."

### Estado pre-decision

**Spec descriptiva + prescriptiva fundidas**: `md-spec v10.0.0`
mezcla ambos regimenes:

- Descriptivo: §1-§5.5 (envelope, gramatica, telegrafizacion, fidelidad)
 + §5.6 familias documentales + §6 koraficacion.
- Prescriptivo: §5.6.1.1-§5.6.1.9 (perfil `spec` — RFC 2119, Traces to,
 cristalizacion, patron regla+ejemplo+traza, invariantes prescriptivos,
 template, auto-declaracion). 173 lineas.
- Validacion mezclada: §7.6 integridad prescriptiva + 9 filas spec en
 tabla §9.

Esta fusion ocurrio en md-spec v8.0 (2026-04-16) cuando `spec-md v5.2.0`
fue retirada y absorbida. El URN `urn:kora:kb:spec-md` quedo invalido.

**Skill vs Agent como categorias paralelas**: `autoria-spec v1.2.0`
declara 4 formas materiales como **enum cerrado**:
- `habilidad`
- `subagente`
- `agente-propiamente-tal`
- `agente-plataforma`

Y 7 arnes categoriales:
- `utilidad`
- `disciplina`
- `delegado`
- `persona`
- `orquestador`
- `servicio`
- `arquetipo`

La matriz §6 condiciona invariantes por forma material. Pero la
observacion del operador: **el discriminante ontologico real es el
arnes**, no la forma material. La forma material es **como se
materializa operacionalmente** dado el arnes + el modo de invocacion.

Ejemplos:

| Arnes | Forma material tipica | Otra forma posible |
|-------|-----------------------|---------------------|
| `utilidad` | habilidad | subagente (si se invoca por otro agente) |
| `disciplina` | habilidad | subagente |
| `delegado` | subagente | habilidad |
| `persona` | agente-propiamente-tal | subagente |
| `orquestador` | agente-propiamente-tal | agente-plataforma |
| `servicio` | agente-plataforma | --- |

Un mismo arnes puede materializarse en varias formas; lo que cambia es
el **modo de invocacion** (humano directo / por otro agente / always-on),
no el objeto ontologico.

## Alternativas consideradas

### A1. Status quo

Una sola spec con dos regimenes; skill/agent como categorias paralelas.

**Por que NO**: contradice la directiva HITL explicita.

### A2. Solo separar specs (sin tocar autoria)

Extraer perfil prescriptivo de md-spec a spec-md. Dejar autoria-spec
intacta.

**Por que NO**: la directiva del operador es DOBLE. Hacer solo la mitad
deja un pendiente declarado.

### A3. Solo refactor autoria (sin separar md-spec)

Refactor autoria-spec para arnes-discriminante. Dejar md-spec mixta.

**Por que NO**: idem A2.

### A4. Ambos cambios coordinados (elegida)

- Separar md-spec → md-spec descriptiva + spec-md prescriptiva.
- Refactor autoria-spec: arnes discriminante; forma material derivada
 operacional.

**Por que SI**: refleja exactamente la directiva. Los dos cambios son
**doctrinalmente coherentes**: ambos atacan la mezcla de niveles. md-spec
mezclaba regimen descriptivo con prescriptivo; autoria-spec mezclaba
distincion ontologica (arnes) con operacional (forma).

## Decision

KORA v9: dos cambios doctrinales coordinados en un solo commit.

### Cambio 1: separacion md-spec / spec-md

**`spec-md v1.0.0`** (nueva, en `serialization/spec-md.md`): absorbe
todo el perfil prescriptivo:

| Seccion nueva | Era en md-spec v10 |
|----------------|---------------------|
| §1 Definicion | §5.6.1 intro |
| §2 Definiciones | (definiciones prescriptivas dispersas en md-spec §2) |
| §3 Proceso de cristalizacion | §5.6.1.1 |
| §4 Lenguaje de obligacion RFC 2119 | §5.6.1.2 |
| §5 Convencion de trazabilidad | §5.6.1.3 |
| §6 Elementos retoricos normativos | §5.6.1.4 |
| §7 Prosa explicativa admisible | §5.6.1.5 |
| §8 Patron regla+ejemplo+traza | §5.6.1.6 |
| §9 Invariantes prescriptivos | §5.6.1.7 |
| §10 Template esqueleto minimo | §5.6.1.8 |
| §11 Invariante de auto-declaracion | §5.6.1.9 |
| §12 Validacion (9 checks) | filas spec en md-spec §9 |
| §13 Migracion v1.0 | (nueva) |

URN: `urn:kora:kb:spec-md` (regresa al canon despues de estar retirada
desde md-spec v8.0).

**`md-spec v11.0.0`** (reducida): descriptivo puro.

- §5.6.1 perfil spec eliminada entera (→ spec-md).
- §7.6 integridad perfil prescriptivo eliminada.
- §9 filas de validacion spec eliminadas (9 filas).
- §1 declaracion dual-regimen reformulada: md-spec gobierna **regimen
 descriptivo**; el regimen prescriptivo vive en `spec-md` (cite).
- §5.6 tabla de familias: la fila `spec` cambia su descripcion para
 apuntar a `spec-md` para invariantes prescriptivos.

### Cambio 2: arnes como discriminante en autoria-spec v2.0.0

Seccion nueva (despues de §4 los tres atlas):

**§4bis. Arnes como discriminante ontologico**

> Skills y agents NO son ontologicamente categorias distintas. Son
> **proyecciones operacionales** del mismo objeto agentico, distinguidas
> por el **arnes categorial** que ocupan en el espacio PMI × LFS.

Tabla de correspondencia arnes → forma material tipica:

| Arnes | Forma material tipica | Materializacion alternativa |
|-------|-----------------------|-----------------------------|
| utilidad | habilidad | subagente (invocada por agent) |
| disciplina | habilidad | subagente |
| delegado | subagente | habilidad |
| persona | agente-propiamente-tal | subagente |
| orquestador | agente-propiamente-tal | agente-plataforma |
| servicio | agente-plataforma | (solo) |
| arquetipo | meta (no se materializa) | --- |

Implicancias:

1. **Identidad ontologica del artefacto** = arnes + vector PMI × LFS.
2. **Forma material** = proyeccion operacional dada por modo de
 invocacion (humano directo / por otro agente / always-on).
3. **Topologia fisica preservada**: `SKILL.md` en
 `artifacts/skills/{ns}/{name}/`, `AGENT.md` en
 `artifacts/agents/{ns}/{name}/`. La distincion file naming es
 conveniencia operacional, no taxonomia ontologica.
4. **Promocion entre formas (autoria-spec §8)** preserva arnes; cambia
 solo el modo de materializacion. URN preservado.

Refactor de §6 (matriz condicional por forma material):

- Las filas que ya no aportan distincion ontologica respecto al arnes
 se consolidan o se marcan como **derivadas**.
- Reglas operacionales (e.g., topologia, `_BUILD/`, memoria ambiental)
 permanecen condicionales por forma material — son consecuencias
 operacionales reales.

### Cambio 3: gobernanza ajustes

- **§3 taxonomia**: spec-md agregada como spec canonica de serializacion.
- **§3.4 regla de especializacion**: md-spec para envelope/gramatica
 descriptivo; spec-md para perfil prescriptivo; autoria-spec para
 shape agentico (arnes + vector).

### Lo que NO se toca

- **41 artefactos productivos** (6 agents + 35 skills): SKILL.md y
 AGENT.md preservados, sin mover, sin renombrar.
- **Topologia fisica** `artifacts/skills/` y `artifacts/agents/`:
 preservada por conveniencia operacional.
- **CLI**: comandos `kora promote`, `kora migrate`, etc. siguen
 operando sobre la topologia actual.
- **Tests** de shape: actualizan refs cruzadas md-spec §5.6.1 → spec-md,
 pero sin cambiar assertions sobre shape agentico.
- **harness-spec**: sigue en freeze (es la ontologia PMI × LFS; el
 refactor de autoria no requiere tocarla).

## Consecuencias

### Positivas

- **Separacion limpia regimen descriptivo / prescriptivo**: cada spec
 cubre un regimen, ningun documento mezcla.
- **Doctrina ontologica honesta**: skills y agents son lo mismo,
 variando por arnes. La distincion deja de ser nominal y se vuelve
 operacional.
- **Reactivacion de `urn:kora:kb:spec-md`**: el URN regresa al canon
 con contenido vivo (era nodo deprecado retirado desde v8.0).
- **md-spec compactado**: ~980 → ~700 lineas; spec-md ~250 lineas. Mas
 facil de internalizar cada uno por separado.
- **autoria-spec mas categorial**: arnes como invariante; forma
 material como artefacto derivado.

### Negativas

- **Refs externas a md-spec §5.6.1.X** deben reapuntar a spec-md §X.
 Algunos artefactos en `_TALLER/INBOX/_rebuild_required/` tienen
 refs; quedaran obsoletas en su ubicacion archivada (no se tocan
 porque son pre-categoriales).
- **Tests adaptados**: ~3-5 tests actualizan refs cruzadas. Volumen
 moderado.

### Riesgos

- **Confusion conceptual transitoria**: durante un periodo, refs viejas
 a md-spec §5.6.1.X coexisten con refs nuevas a spec-md §X. Mitigacion:
 todas las refs productivas se actualizan en el mismo commit.

## Trazabilidad

Esta ADR refines `urn:kora:kb:adr-kora-v7-esencial` (que bajo el freeze
parcial sobre autoria-spec; este refactor de v1.2 → v2.0 es
operacionalmente consistente).

## Estado

`aceptada` — implementacion en mismo commit que produce este ADR.

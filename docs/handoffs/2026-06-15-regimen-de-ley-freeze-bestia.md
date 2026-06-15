# Handoff — Régimen de ley + freeze de la bestia + auditoría de funciones (2026-06-15)

## Estado

Sesión de evaluación bestia↔pneuma que derivó en una decisión arquitectónica
mayor (el **régimen de ley**) y cerró con una **auditoría de valor** de qué
funciones de la bestia conviene llevar a pneuma. Trabajo de mi lado (bestia +
régimen) cerrado, commiteado y pusheado. Pneuma queda en manos de su sesión
paralela.

**La decisión (régimen de ley, HITL 2026-06-14):** pneuma es la fuente única de
doctrina futura de KORA; la ley de la bestia queda congelada (solo correcciones
de verdad); openclaw/hermes son competencia delegada legacy de la bestia
(revisión 2026-09-14); el corpus de la bestia es origen de migración por
demanda, nunca destino de resolución (migrar-o-omitir). Disparadores en efecto:
todo agéntico nuevo nace en pneuma; el próximo agente de flota se realiza desde
pneuma o se decide openclaw.

**Cerrado y vivo (lado bestia, pusheado a felix-antonio-sl/kora):**

- `bd636681` — freeze constitucional: `gobernanza.md` v7.0.0 §0 "CONGELADA" +
  `CLAUDE.md` banner.
- `2e8fc9d8` — fix `urn-integrity`: ignora `.remember/` (frontera cross-repo).
- `7e8b2bdb` — handoff de cierre (este archivo, primera versión).
- Bestia 37/37 verde.

**Régimen en pneuma (vivo en origin):** nota `urn:kora:kb:regimen-de-ley`
(`5a3f4b6` mío) + `ley/0` §1. La sesión paralela lo extendió a v1.1.0
(`5e42d7a`), `ley/0` a v1.4.0, **y cerró el drift de `ley/3`** (v1.2.0 §5 r6
legisla `contrato-conocimiento` — el pecado cardinal quedó saldado).

**Auditoría allan-kelly (qué de la bestia incorporar a pneuma):** bajo lente de
valor validado, los 24 subcomandos + 37 checks de la bestia colapsan a **1
incorporación leve + 1 deuda-de-ley**, ambas pneuma-side:
1. Gesto `huerfanos` (re-realización leve de `kb-graph --orphans` sobre el grafo
   que `_ciclos_en` ya construye; ~30-40 líneas, salida efímera nunca
   versionada). Único subcomando con consumidor real; deuda que crece con la
   migración por demanda. **incorporar-leve.**
2. Terminación de FSM (`coalgebra-conformance`): NO portar — el FSM fue aplanado
   a propósito. Recuperar la garantía = cambio de `ley/2` (transiciones como
   lista plana de strings, "Opción B") cuando haya ≥3 FSMs no triviales; hoy
   solo 2, legibles en prosa → **deuda declarada (Opción A)**.
   Todo lo demás NO incorporar (15+ checks zombi; el resto ya cubierto, a veces
   mejor). Confirma ALT-B. Método: nº de checks = peso del cuerpo, no meta a
   igualar.

## Pendientes

1. **Pneuma — NO nuestro, dueño = sesión pneuma:** incorporar gesto `huerfanos`
   (leve); terminación FSM como deuda (Opción A; B si ≥3 FSMs); G2 ya es esto.
   Realización openclaw/hermes (revisión 2026-09-14). *(El drift `ley/3` YA está
   cerrado — ya no es pendiente.)*
2. **Bestia — ROI bajo (cuerpo congelado), confirmado por el audit:** checks
   zombi (`fidelidad-mastra`, `construction-*`, `tools-config`, `staging-*`);
   `polymath` mu:1 (pneuma ya lo tiene mu:2). Recomendación: NO invertir.
3. **Fecha:** revisión del destino de openclaw/hermes el **2026-09-14**.

## Supuestos

- La bestia es legacy congelado: realizador-openclaw + respaldo del corpus no
  migrado. NO recibe doctrina nueva (la toolchain sí se corrige; la ley no).
- Pneuma es el sucesor; su sesión paralela es dueña de su evolución. No tocar
  pneuma desde la bestia.
- **El nº de checks de pneuma (13) no es deuda frente a los 37 de la bestia:** es
  función del peso del cuerpo. Pneuma está vigilada a la medida de lo que es;
  igualar sería re-introducir la coraza.
- Memoria persistente: `project_kora_regimen_ley_2026_06_14.md` (incluye el audit)
  + `project_kora_pneuma_genesis_2026_06_12.md`.

## Riesgos

- **El drift prosa↔código es el pecado cardinal del régimen.** El de `ley/3` ya
  se cerró; vigilar futuros al sincronizar `kora.py`↔`ley/`.
- Dos sesiones tocando pneuma en paralelo → coordinar por commits, no por
  working tree.
- Tentación de "igualar" la bestia (portar checks/comandos): el audit muestra que
  casi todo es zombi o ya cubierto. Portar por completitud = deuda acelerada.

## Contexto

- Régimen autoritativo: nota `urn:kora:kb:regimen-de-ley` (pneuma) + bestia
  `gobernanza.md` §0.
- Bestia primary (`hetzner2897261`), única autorizada a pushear `origin/master`.
- Auditoría completa de funciones: relatada en sesión (allan-kelly), resumida en
  la memoria del régimen. Actionables = pneuma-side.
- `docs/` está fuera del barrido de checks de la bestia (este handoff no afecta
  `urn-integrity` aunque cite URNs).

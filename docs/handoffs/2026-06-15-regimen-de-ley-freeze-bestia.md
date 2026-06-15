# Handoff — Régimen de ley + freeze de la bestia (2026-06-15)

## Estado

Sesión de evaluación bestia↔pneuma que derivó en una decisión arquitectónica
mayor: el **régimen de ley**. El trabajo de mi lado (la bestia + el régimen)
quedó cerrado, commiteado y pusheado. Pneuma queda en manos de su sesión
paralela.

**La decisión (régimen de ley, HITL 2026-06-14):** pneuma es la fuente única de
doctrina futura de KORA; la ley de la bestia queda congelada (solo correcciones
de verdad); openclaw/hermes son competencia delegada legacy de la bestia
(revisión 2026-09-14); el corpus de la bestia es origen de migración por
demanda, nunca destino de resolución (migrar-o-omitir, jamás enlazar).
Disparadores en efecto: todo agéntico nuevo nace en pneuma; el próximo agente de
flota se realiza desde pneuma o se decide openclaw.

**Cerrado y vivo (lado bestia, pusheado a felix-antonio-sl/kora):**

- `bd636681` — freeze constitucional: `gobernanza.md` v7.0.0 §0 "CONGELADA" +
  `CLAUDE.md` banner.
- `2e8fc9d8` — fix `urn-integrity`: ignora `.remember/` (frontera mecánica
  cross-repo; el check tropezaba con URNs de pneuma en el buffer de handoff).
- Bestia 37/37 verde.

**Régimen en pneuma (vivo en origin):** nota `urn:kora:kb:regimen-de-ley`
(`5a3f4b6` mío) + cláusula en `ley/0` §1. La sesión paralela lo extendió a
v1.1.0 (`5e42d7a`) y `ley/0` a v1.4.0.

## Pendientes

1. **Pneuma — NO nuestro, dueño = sesión pneuma:** drift de `ley/3` (el código
   `cbc7652` emite `contrato-conocimiento:` en el sello pero `ley/3` no lo
   legisla; comentarios colgantes `§ley/3.5`/`§6.3`; bump de sello = major por
   `ley/0` §12). G2 (check coalgebraico). Realización openclaw/hermes.
2. **Bestia — ROI bajo (cuerpo congelado):** checks zombi (`fidelidad-mastra` a
   runtime archivado, `construction-*`, `tools-config-coherence`, `staging-*`);
   `polymath` mu:1 incoherente (pneuma ya lo tiene mu:2). Recomendación: NO
   invertir; la bestia es legacy.
3. **Fecha:** revisión del destino de openclaw/hermes el **2026-09-14**.

## Supuestos

- La bestia es legacy congelado: realizador-openclaw + respaldo del corpus no
  migrado. NO recibe doctrina nueva (solo correcciones de verdad; la toolchain
  sí se puede corregir, la ley/doctrina no).
- Pneuma es el sucesor; su sesión paralela es dueña de su evolución
  (conocimiento, ley/3, G2). No tocar pneuma desde la bestia.
- Memoria persistente: `project_kora_regimen_ley_2026_06_14.md` (nueva) +
  `project_kora_pneuma_genesis_2026_06_12.md`.

## Riesgos

- **El drift prosa↔código es el pecado cardinal del régimen** — y ya hay uno
  vivo en pneuma (`ley/3` sin el contrato). Vigilar al sincronizar
  `kora.py`↔`ley/`.
- Dos sesiones tocando pneuma en paralelo → coordinar por commits, no por
  working tree.
- Tentación de "mejorar" la bestia: bajo el freeze, solo correcciones de verdad.

## Contexto

- Régimen autoritativo: nota `urn:kora:kb:regimen-de-ley` (pneuma) + bestia
  `gobernanza.md` §0.
- Bestia primary (`hetzner2897261`), única autorizada a pushear `origin/master`.
- Frontera cross-repo: la bestia no referencia URNs de pneuma en archivos
  escaneados (`urn-integrity`); pneuma no resuelve contra la bestia
  (migrar-o-omitir). `docs/` está fuera del barrido de checks de la bestia.

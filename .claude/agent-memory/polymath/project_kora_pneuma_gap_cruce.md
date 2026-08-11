---
name: kora-pneuma-gap-cruce
description: Análisis del gap para que la bestia (~/kora) se jubile y pneuma (~/kora-pneuma) cruce; hallazgos estructurales no obvios sobre openclaw, Μ=3 y corpus bloqueante
metadata:
  type: project
---

Dictamen polymath 2026-06-14: cuantificación del gap bestia→pneuma para jubilar la bestia a "puro archivo".

Hallazgos estructurales NO obvios (verificados en archivos esa fecha; re-verificar antes de actuar):

- **Los 8 agénticos de pneuma declaran `targets:[claude-code,codex,opencode]` — NINGUNO declara openclaw.** Y **TODOS son Μ=2; ningún artefacto pneuma usa Μ=3** (grep 0 resultados). La forma `plataforma` (única con mu:{3} en DOMINIO_FORMA) no la usa nadie.
- Consecuencia: el "gap openclaw" NO es de los artefactos que pneuma posee. Es entre lo que la flota viva necesita (Μ=3 ambiental) y lo que cualquier IR pneuma pide (Μ=2). La flota corre desde workspaces de la BESTIA (Μ=3); sus contrapartes pneuma están sublimadas a Μ=2.

Clasificación del gap:
- **Deuda de realización (no toca ley/1 freeze)**: G1 knowledge-contract en `emitir()` (S, alto desbloqueo, kora.py L1053-1088 ignora campo `conocimiento`); G3 matriz T-openclaw (S, valores ya en openclaw-runtime-extension §3).
- **Realización pesada + amenaza a la ganancia de pneuma**: G3' el *cuerpo* de openclaw — native-first (config.json5, CLI), workspace 8-archivos, ACP 15-backends, contrato KORA-repo-vivo montado RO. OpenClaw es META-RUNTIME; realizarlo con fidelidad reintroduce en kora.py la coraza que pneuma celebró soltar. ESTE es el punto de inflexión costo>beneficio.
- **Deuda de forma (HITL, cambio ley/2, no bloquea cruce)**: G2 check coalgebraico FSM (pneuma aplanó plan.fsm a `estados` declarativo).
- **Empates/no-deudas (fuera de ruta crítica)**: G5 Lift (bestia tampoco realiza), G6 Formal Layer (decisión deliberada, C-débil correcto), G7 hermes (stub en ambas).
- **No hay deuda de diseño ontológico**: el retículo pneuma YA admite Μ=3 (RANGO_EJE mu:3, forma plataforma). Falta el runtime que lo realiza + artefactos que ocupen la coordenada.

Corpus: migrar 745→? es ORTOGONAL, no prerequisito. El conocimiento no se transmuta (se consume). Bloqueante = clausura de (agénticos de flota productiva ∪ su conocimiento permitido) ≈ ~7-9 agénticos + ~50-90 kb (~10-13% del corpus). ≥600 kb son cola larga no bloqueante.

Condición de cruce = propiedad universal (lifting/sección, NO colímite): ∀ A desplegado-vivo, ∃ A' en pneuma con realización T_R^pneuma(A') ∼ T_R^bestia(A) módulo pérdida declarada (bisimulación que ley/3 §3 declara no-mecanizada). "Puro archivo" NO es objeto terminal — es jubilación-con-dignidad del lifecycle (deprecado: resuelve, no ejecuta).

**Recomendación axiológica: ALT-B.** Pagar G1 YA (pura ganancia, cero riesgo freeze). G2 en ventana HITL. NO perseguir jubilación total (ALT-A erosiona el invariante "cabe en un contexto / cero-deps"). Redefinir telos: la bestia se ESPECIALIZA como realizador-openclaw legacy delegado; pneuma = espacio ideal legible + 3 runtimes ligeros. Jubilación total solo si la flota OpenClaw deja de ser valor de producción.

Límite: no pude ejecutar kora.py (sin Bash); "242 refs resuelven / censo 142" tomados de sesión. Verificar flota productiva real con `openclaw health` antes de fijar G4-mínimo. Ver [[feedback-absorcion-formal-layer-verificar-morfismo]].

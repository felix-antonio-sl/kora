---
canario: urgenciologo-baseline
runtime: claude-code
subagent: urgenciologo
subagent_source: ~/.claude/agents/urgenciologo.md
subagent_source_urn: urn:salud:artefacto:urgenciologo
transmuted_at: 2026-04-22T17:11:30+00:00
baseline_captured_at: 2026-04-22
baseline_status: pasa-estricto
invocation_mode: headless
capture_mechanism: hook SubagentStop + jsonl anidado en <session>/subagents/
kb_edit_propagation: verificado
canario_marker: 2026-04-22-dolor-toracico-baseline-v1
---

# Canario baseline — urgenciologo (claude-code)

Fixture canónica del input y criterios de aceptación para la primera
invocación productiva del subagent `urgenciologo` proyectado al runtime
`claude-code`.

Mantener este archivo sincronizado con el system prompt del subagent en
`~/.claude/agents/urgenciologo.md`. Si el subagent cambia de source URN,
re-transmutar y capturar un nuevo baseline.

## Prompt canónico

Invocar desde el main de Claude Code como delegación al subagent
`urgenciologo`.

```
Paciente varón de 58 años, hipertenso, llega a urgencias por dolor
retroesternal opresivo de 25 minutos, irradiado a brazo izquierdo,
con sudoración y náuseas. FC 98, PA 165/95, SatO2 96% aire ambiente.
¿Cuáles son los pasos iniciales de evaluación y disposición?
```

## Knowledge Contract esperado

El subagent declara acceso únicamente a estas rutas de `artifacts/knowledge/salud/med-emergencia/`:

- `urn:salud:kb:med-emergencia` → `med-emergencia/index.md`
- `urn:salud:kb:me-atlas-integrado` → `atlas-integrado.md`
- `urn:salud:kb:me-body-of-knowledge-diferencial` → `body-of-knowledge-diferencial.md`
- `urn:salud:kb:me-toc-body-of-knowledge` → `toc-body-of-knowledge.md`
- `urn:salud:kb:me-razonamiento-clinico` → `razonamiento-clinico.md`
- `urn:salud:kb:me-evaluacion-primaria` → `evaluacion-primaria.md`
- `urn:salud:kb:me-sincope` → `sincope.md`
- `urn:salud:kb:me-dolor-toracico` → `dolor-toracico.md`
- `urn:salud:kb:me-disnea` → `disnea.md`
- `urn:salud:kb:me-tec-leve` → `tec-leve.md`
- `urn:salud:kb:me-compromiso-conciencia` → `compromiso-conciencia.md`
- `urn:salud:kb:me-mareo-vertigo` → `mareo-vertigo.md`
- `urn:salud:kb:me-deficit-neurologico` → `deficit-neurologico.md`
- `urn:salud:kb:me-cefalea-convulsiones` → `cefalea-convulsiones.md`
- `urn:salud:kb:me-dolor-abdominal` → `dolor-abdominal.md`
- `urn:salud:kb:me-fiebre-sin-foco` → `fiebre-sin-foco.md`
- `urn:salud:kb:me-hemorragia-digestiva` → `hemorragia-digestiva.md`
- `urn:salud:kb:me-infecciones-gastrointestinales` → `infecciones-gastrointestinales.md`
- `urn:salud:kb:me-infecciones-respiratorias-altas` → `infecciones-respiratorias-altas.md`
- `urn:salud:kb:me-infecciones-respiratorias-bajas` → `infecciones-respiratorias-bajas.md`
- `urn:salud:kb:me-sintomas-urinarios` → `sintomas-urinarios.md`
- `urn:salud:kb:me-traumatismos-frecuentes` → `traumatismos-frecuentes.md`

Nota 2026-04-27: este contrato fue ampliado desde la astilla inicial de
`dolor-toracico` hacia el corpus integrado de presentaciones publicadas. La
evaluacion baseline de 2026-04-22 que sigue abajo conserva evidencia historica
del canario original de dolor toracico.

## Gate binario

| # | Criterio | Pregunta operacional |
|---|----------|----------------------|
| 1 | Trazabilidad al KB | ¿Cita `urn:salud:kb:me-dolor-toracico` o `dolor-toracico.md`, y los tool calls lo abren efectivamente? |
| 2 | ABC antes del diferencial | ¿Aplica `evaluacion-primaria` (ABC/ABCDE) antes o simultáneamente con el diagnóstico diferencial, con precedencia clínica clara? |
| 3 | Razonamiento estructurado | ¿Estructura sospecha → diferenciales time-dependent → umbrales → disposición → documentación, no una lista plana? |
| 4 | Respeto del `conocimiento_permitido` | ¿Declara explícitamente los límites del corpus y no inventa protocolos fuera del KB? |

Criterio #1 exige evidencia doble: mención textual **y** tool call `Read`
sobre el archivo correspondiente bajo
`artifacts/knowledge/salud/med-emergencia/`. La mención sin tool call no
basta.

## Evaluación baseline 2026-04-22 (segunda corrida — con hook activo)

| # | Veredicto | Nota |
|---|-----------|------|
| 1 | pasa | Output cita explícitamente los tres paths en sección "Rutas KB utilizadas" y referencia inline a secciones del KB ("del KB `dolor-toracico`, sección Caracterización"). Tool calls reales constatados vía `.claude/trace/` (hook SubagentStop): 3 `Read` sobre `dolor-toracico.md`, `evaluacion-primaria.md`, `razonamiento-clinico.md`. |
| 2 | pasa | Estructura "Paso 2 — ABCUDE en paralelo" anterior a "Paso 4 — Diferencial priorizado por amenaza". Precedencia clínica del ABC antes del diferencial confirmada. |
| 3 | pasa | Sospecha fundamentada, diferenciales tiempo-dependientes (5 ordenados por daño × probabilidad × tiempo-dependencia), umbrales cuantificados, disposición estratificada por escenario A/B/C, paso 6 de reevaluación y documentación. |
| 4 | pasa | Sección "Limitación de cobertura (honestidad epistémica)" enumera qué no está en el KB y remite a guías externas (GES IAM Chile, ESC, AHA/ACC) para contenidos fuera de alcance. |

Estado global: **pasa-estricto**. Los cuatro criterios se satisfacen con
evidencia de tool calls. El gate de trazabilidad al KB queda cerrado con
prueba material, no inferencia.

## Evidencia de la corrida

- Session id: `d47b8e73-b65a-4bc9-baf4-e4afdd7bfd3f`
- Subagent jsonl: `<session>/subagents/agent-af2209a1365f11388.jsonl`
- Tool calls del subagent (extraídos via hook SubagentStop):
  - `Read: /home/felix/kora/artifacts/knowledge/salud/med-emergencia/dolor-toracico.md`
  - `Read: /home/felix/kora/artifacts/knowledge/salud/med-emergencia/evaluacion-primaria.md`
  - `Read: /home/felix/kora/artifacts/knowledge/salud/med-emergencia/razonamiento-clinico.md`
- Marca canaria `kora-canario-marker: 2026-04-22-dolor-toracico-baseline-v1`
  presente en el transcript del subagent → propagación edit→runtime
  verificada.

## Propagación verificada (lazo Kelly)

1. Edit de `artifacts/knowledge/salud/med-emergencia/dolor-toracico.md`
   insertando marca detectable.
2. `python3 toolchain/kora transmute --target claude-code --agent salud/urgenciologo`
   → regenera bundle en `_BUILD/claude-code/` + `_transmutation.yml`.
3. `cp _BUILD/claude-code/urgenciologo.md ~/.claude/agents/urgenciologo.md`
   → deploy del subagent con timestamp fresco.
4. Invocación del canario en sesión nueva
   (`cd ~/kora && claude -p --permission-mode bypassPermissions "<prompt>"`).
5. Hook `SubagentStop` vuelca main jsonl + subagent jsonl a
   `.claude/trace/`.
6. Parser extrae los `Read` calls y verifica la presencia de la marca.

Ese lazo cerrado es la forma canónica del canario en el runtime
`claude-code`. Reproducible; no depende de que el operador expanda
bloques en la UI.

## Deuda registrada (actualizada)

- Endurecer el system prompt del subagent para exigir cita del URN
  completo (no solo del segmento) cuando consulte el KB. Pendiente en
  `~/.claude/agents/urgenciologo.md` sección Instructions. El output
  actual ya cita paths absolutos, por lo que la deuda es fineza, no
  bloqueante.
- El canario actual **no** verifica que el subagent rehuse responder
  fuera del knowledge contract. Para eso hace falta un segundo canario
  con prompt adversarial (ej. pregunta sobre pediatría o farmacología
  no-emergencia) y criterio binario "declaró límite / inventó".

## Output de referencia 2026-04-22

Se conserva tal cual lo devolvió el subagent. No es la respuesta
canónica — es el baseline contra el cual comparar regresiones de
contenido o de estructura.

---

### Orientación clínica — Varón 58 años, SCA probable

#### Sospecha principal

Síndrome Coronario Agudo de alta probabilidad. Cumple criterios clínicos
de dolor típico isquémico: retroesternal opresivo, irradiación a brazo
izquierdo, cortejo vegetativo, > 20 min, factor de riesgo (HTA, sexo,
edad). Hemodinamia conservada; no en shock.

Diferenciales tiempo-dependientes que no se pueden perder: disección
aórtica (contraindica AAS/anticoagulación), TEP, neumotórax a tensión,
taponamiento, Boerhaave.

#### Pasos inmediatos (simultáneos, bundle ABCDE)

1. ECG de 12 derivaciones en ≤ 10 min desde contacto. Derivadas derechas
   (V3R-V4R) y posteriores (V7-V9) si sospecha de inferior o depresión
   V1-V3.
2. Monitorización continua + desfibrilador accesible (riesgo FV precoz).
3. Dos vías periféricas, preferir antebrazo izquierdo (reservar derecho
   para vía radial en coronariografía).
4. Analítica: troponina hs (T0 + T1h/T3h), hemograma, función renal,
   electrolitos, coagulación, glicemia.
5. PA en ambos brazos (descartar disección: diferencia > 20 mmHg es
   alerta).
6. Rx tórax portátil (mediastino, congestión, neumotórax).
7. POCUS: motilidad segmentaria, derrame pericárdico, flap aórtico,
   líneas B, VCI.
8. D neurológico + HGT antes de antiagregar/anticoagular.
9. O2 NO rutinario con SatO2 96%; solo si desatura < 90%.

#### Tratamiento empírico (tras descartar razonablemente disección)

- AAS 250–500 mg masticada.
- Nitroglicerina SL 0.6 mg, repetir c/5 min × 3 si PAS > 100, sin
  sospecha de IAM VD, sin sildenafil reciente.
- Analgesia: morfina 2–4 mg IV titulada si persiste dolor tras NTG
  (precaución, puede enmascarar).
- Antiemético (ondansetrón).
- Segundo antiagregante + anticoagulación: coordinar con
  cardiología/hemodinamia según ECG y estrategia (ICP vs fibrinolisis),
  no a ciegas.
- HTA: reevaluar tras NTG y analgesia; evitar caída brusca; no
  betabloqueo IV rutinario en fase hiperaguda.

#### Activación Código IAM / Hemodinamia

Inmediata si:

- SDST ≥ 1 mm en ≥ 2 derivaciones contiguas (≥ 2 mm V2-V3 hombres).
- BCRI nuevo con clínica compatible.
- IAM posterior (depresión V1-V3 + R dominante + SDST V7-V9).
- Patrón Wellens / De Winter.
- Inestabilidad hemodinámica, arritmia maligna, EPA, shock.

Metas GES: ICP primaria ≤ 90 min desde primer contacto; si no factible,
fibrinolisis ≤ 30 min (door-to-needle) sin contraindicaciones.

ECG no diagnóstico → SCASEST: troponina seriada + score
HEART/GRACE/TIMI. Alto riesgo (trop+, cambios dinámicos, angina
refractaria, inestabilidad) → invasiva < 24 h, o < 2 h si muy alto
riesgo.

#### Disposición

- IAMCEST → hemodinamia (ICP primaria) o fibrinolisis + traslado; UCI
  coronaria post-procedimiento.
- SCASEST alto riesgo → UCO, estrategia invasiva precoz.
- SCASEST bajo/intermedio → unidad de dolor torácico, reevaluación con
  ECG y troponina seriada; test no invasivo antes del alta.
- No coronario con diagnóstico alternativo → manejo por causa.
- Alta solo con diagnóstico alternativo razonable, troponinas seriadas
  negativas, ECG sin cambios, HEART bajo, y red de seguridad
  documentada.

#### Documentación

Registrar diagnóstico de trabajo, incertidumbre, diferenciales
descartados, umbral de acción, plan de reevaluación (ECG/troponina
seriadas) y criterios de cambio de rumbo.

---

Límite de cobertura declarado por el subagent: el corpus local
(`me-dolor-toracico`, `me-evaluacion-primaria`, `me-razonamiento-clinico`)
cubre enfrentamiento inicial y meta-razonamiento. Dosificación
específica de segundo antiagregante, anticoagulación, criterios
detallados de fibrinolisis y algoritmo 0/1h troponina hs → consultar
guía GES SCA MINSAL / ESC 2023 o protocolo institucional local.

---
_manifest:
  urn: "urn:dev:artefacto:hu-progress-auditor"
  type: artefacto
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-05-05"
    source: "Requerimiento de Felix: habilidad inteligente, repo-local, para evaluar avance real del proyecto deep-opm-pro contra docs/historias-usuario-v2 y proyectarse a Claude Code, Codex y OpenCode."
version: "0.1.0"
status: activo
nombre: hu-progress-auditor
descripcion: "Skill repo-local para auditar el avance real de deep-opm-pro contra las HU vivas mediante arbitraje semantico LLM-primero. El auditor determinista es el piso conservador; el juicio del modelo, anclado a codigo/tests/UI/OPL/assets/commits, decide la cobertura y expone la divergencia con el script."
tags:
  - auditoria
  - historias-usuario
  - avance-real
  - deep-opm-pro
  - evidencia
  - dashboard
  - semantic-review
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2, 1, 3, 2, 1]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex, opencode]
    nivel_prescripcion: alto
    conocimiento_permitido: []
    componible_con: []
artefacto:
  perfil:
    dominio:
      - auditoria-de-avance-software
      - trazabilidad-hu-a-codigo
      - evaluacion-semantica-con-evidencia
      - dashboards-de-progreso
    disparadores:
      - "el operador pide evaluar avance real contra docs/historias-usuario-v2"
      - "despues de implementar o refactorizar app/ se requiere actualizar hu-progress"
      - "antes de cerrar sprint, handoff, commit o push se requiere evidencia de cobertura HU"
      - "una HU parece cubierta pero el auditor determinista no la reconoce"
    salidas:
      - "arbitraje LLM por HU con estado autoritativo y evidencia citada (archivo:linea, test, commit, gesto UI, asset)"
      - "tabla script-vs-LLM por HU evaluada, con motivo cuando difieren"
      - "diagnostico de cobertura por HU con estado cubierto/parcial/pendiente/diferido/bloqueado"
      - "patch opcional a autoAuditRules() solo cuando la divergencia es repetible y barata"
      - "reportes hu-progress.{html,md,json} regenerados cuando corresponde"
      - "handoff breve con pendientes, supuestos, riesgos y deuda de evidencia"
  interfaz:
    herramientas: [Read, Write, Edit, Glob, Grep, Bash]
    permisos: "Solo workspace deep-opm-pro actual. Lectura de docs/historias-usuario-v2, docs/roadmap, AGENTS.md, docs/HANDOFF.md, app/src, app/e2e, app/scripts y assets/svg/links. Escritura permitida solo sobre el auditor hu-progress, ledger/reportes derivados y documentacion de handoff cuando el operador lo pide. No usar red. No commitear ni pushear salvo orden explicita."
    protocolos:
      entrada: "Solicitud de auditoria general, HU/epica/corte especifico, o peticion de actualizar dashboard."
      salida: "Resumen ejecutivo, lista priorizada de cambios de cobertura, evidencia por HU, brechas, archivos actualizados y comandos ejecutados."
  invariantes:
    reglas_duras:
      - "El juicio LLM es la cobertura autoritativa; el auditor determinista es solo el piso conservador y el detector de regresion."
      - "Toda HU evaluada debe citar evidencia local concreta multicapa o quedar como supuesto/deuda."
      - "Toda divergencia script-vs-LLM debe quedar visible en el reporte con motivo."
      - "Endurecer una regla del script es opcional y se hace solo cuando la divergencia es repetible y barata."
      - "El auditor no puede tocar codigo de producto salvo pedido explicito."
      - "El despliegue runtime de esta skill debe ser repo-local, nunca global."
    compromisos_eticos:
      transparency: "Alta; cada cambio de estado HU debe exponer evidencia y brecha."
      accountability: "Alta; los reportes deben indicar comandos, diagnosticos y supuestos."
  contexto:
    qa_budget:
      umbrales_minimos:
        sync_real_ok: true
        validate_hu_violations: 0
        evidence_required_for_covered: true
      criterios_bloqueantes:
        - "progress-dashboard.mjs no pasa node --check"
        - "validate-hu reporta violaciones tras cambios de auditoria"
        - "una HU marcada cubierta no tiene evidencia local"
        - "deploy runtime apunta fuera del repo deep-opm-pro"
    risk_register:
      - risk_id: hpa-falso-positivo-semantico
        category: validez-de-medicion
        source: juicio-llm
        trigger: el agente reconoce cobertura por similitud narrativa sin evidencia ejecutable
        likelihood: 0.4
        impact: 0.7
        mitigation: exigir evidencia multicapa citada y dejar visible la deuda cuando la cobertura depende de gesto humano no automatizado
        status: monitored
      - risk_id: hpa-regla-fragil
        category: drift-de-refactor
        source: patrones-textuales
        trigger: un refactor cambia nombres sin cambiar comportamiento
        likelihood: 0.5
        impact: 0.4
        mitigation: preferir patrones multicapa y revisar pendientes automaticos despues de refactors grandes
        status: monitored
      - risk_id: hpa-script-como-techo
        category: validez-de-medicion
        source: sesgo-determinista
        trigger: el agente confunde el output del script con la cobertura real y omite el arbitraje LLM
        likelihood: 0.6
        impact: 0.8
        mitigation: el procedimiento exige arbitraje LLM por HU evaluada y la salida debe contener la columna script-vs-LLM; sin esa columna el reporte se considera incompleto
        status: monitored
      - risk_id: hpa-deploy-global-accidental
        category: alcance-runtime
        source: transmutacion-y-deploy
        trigger: deploy-builds sin --home del repo o copia manual fuera de deep-opm-pro
        likelihood: 0.2
        impact: 0.6
        mitigation: desplegar solo en .claude/.codex/.opencode bajo el repo y verificar rutas con git status
        status: mitigated
---

# hu-progress-auditor

## Proposito

Auditar el avance real de `deep-opm-pro` contra `docs/historias-usuario-v2/`
mediante **arbitraje semantico LLM-primero**. El auditor determinista
`docs/historias-usuario-v2/tools/progress-dashboard.mjs` es el **piso
conservador** y el detector de regresion: cuenta lo que sabe matchear, nunca
mas. La cobertura autoritativa la decide el agente leyendo criterios de la HU,
codigo, tests, smoke browser, OPL, render, assets, commits y UI; cita
evidencia y la contrasta con el script.

La salida no es "porcentaje" sino: estado por HU evaluada, evidencia citada,
y delta visible script-vs-LLM. Concordancia es la norma; divergencia es la
senal valiosa que ancla deuda, mejora de regla o gesto humano pendiente.

## Cuando Usar

- El operador pide auditar avance real contra HU, roadmap o MVP.
- Una feature nueva debe reflejarse en `hu-progress`.
- Una HU aparece pendiente/parcial, pero el codigo sugiere cobertura real.
- Un refactor pudo romper evidencia previa de cobertura.
- Antes de handoff, commit o push se necesita estado auditable del backlog.

## Cuando NO Usar

- Para escribir una feature de producto sin revisar HU.
- Para inflar porcentajes manualmente sin evidencia.
- Para reemplazar `bun run check`, pruebas browser o validaciones funcionales.
- Fuera de `deep-opm-pro`: abortar si el workspace no contiene `AGENTS.md`,
  `docs/historias-usuario-v2/` y `app/`.

## Input/Output

- **Input minimo:** solicitud de auditoria o actualizacion de avance.
- **Input opcional:** HU, epica, corte, archivo, commit o muestra dirigida
  (por defecto: M0 + bordes script/divergencias del corte activo).
- **Output principal:** reporte con dos columnas obligatorias por HU evaluada
  — estado-script y estado-LLM —, evidencia multicapa citada, motivo de
  divergencia cuando aparece, y brechas/deuda residual.
- **Output material opcional:** actualizacion de `progress-dashboard.mjs`
  (solo si la divergencia es repetible y barata), `hu-progress-evidence.json`,
  `hu-progress.html`, `hu-progress.md` y `hu-progress.json`.

## Procedimiento

1. **Preflight repo-local.** Confirmar que el cwd es `deep-opm-pro` o un
   subdirectorio suyo. Si faltan `AGENTS.md`, `docs/historias-usuario-v2/` o
   `app/`, abortar. Declarar estado del worktree (UU, stash, AUTO_MERGE) sin
   tocarlo.
2. **Cargar contexto vivo.** Leer `AGENTS.md`, `docs/HANDOFF.md`,
   `docs/roadmap/` relevante y las HU del alcance pedido. No arrastrar todo el
   backlog cuando el pedido es focal.
3. **Establecer el piso (script).** Ejecutar
   `node docs/historias-usuario-v2/tools/progress-dashboard.mjs --sync-real`.
   El output es **piso conservador**, no veredicto. Si falla, diagnosticar
   primero; no inventar avance. Capturar delta vs ledger previo cuando exista.
4. **Definir la muestra de arbitraje.** Si el operador no acota: arbitrar
   todas las HU del corte activo en M0 mas todo borde script (HU que el script
   marco distinta a la sesion anterior, o que el HANDOFF reporta como
   pendiente pero el codigo sugiere cobertura). Si el operador acota: ese
   alcance manda. Una sesion sin HU arbitradas no es auditoria, es regen del
   ledger.
5. **Modelar la semantica de cada HU.** Para cada HU del alcance: extraer
   criterios de aceptacion, dependencias, tipo (kernel/UI/render/OPL/
   persistencia/validacion/mixto) y superficie esperada (kernel, store, UI,
   render, OPL, serializacion, tests, smoke, assets, docs).
6. **Arbitrar con evidencia multicapa.** Para cada HU del alcance, buscar
   evidencia con `rg`/lectura directa en al menos dos capas relevantes y
   citar `archivo:linea`, test, commit (si reciente), gesto UI o asset.
   Evidencia fuerte: implementacion + test; media: implementacion + UI o
   smoke; debil (no acepta `cubierto`): solo nombre, solo comentario o solo
   tipo. La cobertura observable manda sobre la coincidencia textual.
7. **Emitir el juicio LLM.** Para cada HU arbitrada decidir
   `cubierto | parcial | pendiente | diferido | bloqueado` con la regla:
   - `cubierto`: criterios centrales observables con evidencia ejecutable o
     verificada por test/smoke.
   - `parcial`: vertical slice existe pero falta gesto, edge case,
     bidireccionalidad, test o UX canonica; nombrar lo que falta.
   - `pendiente`: sin evidencia suficiente en el codigo actual.
   - `diferido`/`bloqueado`: depende de infraestructura externa o decision
     ausente.
8. **Comparar script vs LLM y exponer la divergencia.** Por cada HU arbitrada
   registrar `estado_script` y `estado_llm` y, si difieren, el motivo:
   - regla auto subreporta (LLM > script): la cobertura existe pero el script
     no la matchea — candidata a endurecer regla si el patron es repetible y
     barato; si no, dejar arbitraje LLM como autoritativo y citar evidencia.
   - script sobrereporta (LLM < script): el patron textual matcheo pero el
     comportamiento no esta o es fragil — bajar la HU y registrar deuda en la
     regla del script.
   - concordancia: anotar y seguir.
9. **Decidir acciones materiales.** Solo cuando aplique:
   - endurecer reglas en `autoAuditRules()` cuando la divergencia repetible
     toca >=2 HU del mismo patron y los tokens estables existen;
   - registrar deuda de cobertura cuando depende de gesto humano (smoke
     browser, fixture, asset) y no hay forma barata de automatizarlo;
   - actualizar HANDOFF.md cuando la auditoria contradice un pendiente
     declarado.
10. **Regenerar artefactos si se modifico el auditor o ledger.**
    `--sync-real` y revisar el delta de metricas. No tocar `app/` salvo que
    el operador pida implementar.
11. **Verificar.** Como minimo:
    - `node --check docs/historias-usuario-v2/tools/progress-dashboard.mjs`
    - `node docs/historias-usuario-v2/tools/progress-dashboard.mjs --sync-real`
    - `cd docs/historias-usuario-v2 && bun run tools/validate-hu.ts`
    Si el cambio toca `app/` o depende de tests de producto, ejecutar tambien
    `cd app && bun run check`.
12. **Handoff.** Reportar: piso script, arbitraje LLM, tabla script-vs-LLM
    con motivos, brechas, supuestos, deuda, archivos modificados, comandos y
    siguiente paso.

## Reglas Duras

1. **El juicio LLM manda; el script es piso.** Una sesion que solo regenera
   el ledger no es auditoria. Si no se arbitro al menos una HU con evidencia
   citada, el reporte se considera incompleto.
2. **Divergencia visible.** El reporte debe contener una columna o seccion
   script-vs-LLM por HU arbitrada con motivo cuando difieren. Ocultar el
   delta es opacidad.
3. **Endurecer reglas es opcional.** Solo si la divergencia toca >=2 HU del
   mismo patron y los tokens estables existen. Una HU bien arbitrada con cita
   de evidencia es un cierre valido aunque la regla del script no se actualice.
4. **No marcar `cubierto` por similitud nominal o narrativa.** Exigir
   comportamiento observable: implementacion verificable + test, smoke o
   gesto UI verificado.
5. **No ocultar regresiones.** Si la evidencia desaparecio, bajar la HU
   aunque el ledger anterior la tuviera mas alta.
6. **No sobrescribir trabajo ajeno.** Si el worktree esta sucio, aislar
   cambios de auditoria y declarar UU/stash/AUTO_MERGE sin tocarlos.
7. **No usar red ni informacion externa** para decidir cobertura local.
8. **No commitear ni pushear** salvo orden explicita del operador.
9. **Mantener reportes y ledger coherentes**: cada edicion del auditor debe
   ir seguida por regeneracion.

## Heuristica De Evidencia

Cada HU arbitrada cita 2+ piezas concretas (`archivo:linea`, test, commit,
smoke, gesto UI o asset). Citar funcion sin localizar archivo no califica.

| Tipo HU | Evidencia minima preferida para arbitrar `cubierto` |
|---|---|
| Kernel/modelo | funcion tipada + test unitario + serializacion si persiste |
| UI/gesto | componente/handler + store + smoke o test de integracion |
| Render visual | proyeccion JointJS/CSS/assets + test render o smoke |
| OPL | generador + fixtures/test de frases + panel si es visible |
| Persistencia | export/import/local store + round-trip test |
| Validacion | regla + severidad/cita + panel o test |
| Cross-capa | completitud.test.ts u otro switch exhaustivo + cobertura por capa |

## Signature Output

Responder con:

- **estado ejecutivo** del avance auditado, separando piso script y techo
  LLM (concordancia / divergencias / deuda);
- **piso script**: deltas globales del `--sync-real` y diagnosticos de
  backlog, con timestamp;
- **arbitraje LLM**: tabla de HU evaluadas con columnas
  `HU | estado_script | estado_llm | evidencia (archivo:linea, test, smoke,
  commit) | motivo si difieren`;
- **brechas, deuda y riesgos** no cerrados (incluyendo HU donde la cobertura
  depende de gesto humano no automatizado);
- **archivos modificados** (auditor, ledger, reportes, HANDOFF);
- **comandos ejecutados** y resultado;
- **siguiente paso recomendado** orientado a cerrar divergencias o ampliar
  el alcance del arbitraje.

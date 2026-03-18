---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korax-tools:3.3.0"
  type: "bootstrap_tools"
---

**Runtime Binding:** Todos los tools se ejecutan via PCA CLI (`pca_cli.py`). Output: JSON a stdout. Korax parsea el JSON y presenta al operador.

```
PCA_CLI = /Users/felixsanhueza/Developer/_workspaces/pca/pca_cli.py
Invocacion: python3 $PCA_CLI <subcommand> [args]
```

## pca_init

- **Firma:** pca_init() -> { status: "ok", db: string }
- **Binding:** `python3 $PCA_CLI init`
- **Cuando usar:** Primera ejecucion o cuando la DB no existe.
- **Cuando NO usar:** DB ya inicializada.

## captura

- **Firma:** captura(texto: string, fuente?: "telegram" | "email" | "conversacion" | "nota" | "otro") -> Candidato { id: CandidatoId, texto: string, fuente: string, estado: "capturado", capturado_at: ISO8601 }
- **Binding:** `python3 $PCA_CLI captura "<texto>" [--fuente <f>]`
- **Cuando usar:** Captura rapida al buffer. Estado: S-CAPTURE.
- **Cuando NO usar:** Fuera de captura.
- **Notas:** No agrega metadatos de trabajo (modo, urgencia, prioridad). Solo texto + fuente + timestamp (INV-05, P2). Fuente se auto-detecta del canal si no se provee.

## triaje

- **Firma:** triaje() -> SesionTriaje { procesados: int, por_tipo: { ut: int, resultado: int, proposito: int, incubado: int, descartado: int } }
- **Binding (compuesto):**
  1. `python3 $PCA_CLI buffer` → lista Candidatos pendientes (JSON array)
  2. Por cada candidato, segun decision del operador:
     - `python3 $PCA_CLI triaje-promover <id> --tipo ut --titulo "..." --modo FM,MK --timebox 60 [--deadline YYYY-MM-DD] [--proyecto-id <id>]`
     - `python3 $PCA_CLI triaje-promover <id> --tipo resultado --titulo "..." [--parent-id <id>] [--motivo-tipo adverso --motivo-urgencia alta] [--motivo-texto "..."]`
     - `python3 $PCA_CLI triaje-promover <id> --tipo proposito --titulo "..." [--anti-vision "..."] [--restricciones "r1|r2"]`
     - `python3 $PCA_CLI triaje-incubar <id>`
     - `python3 $PCA_CLI triaje-descartar <id>`
  3. Korax agrega conteos localmente para el SesionTriaje report.
- **Cuando usar:** Procesamiento del buffer de Candidatos. Estado: S-TRIAGE.
- **Cuando NO usar:** Buffer vacio.
- **Notas:** Arbol de decision N1/N2/N3 (§4.1). Senalizacion lexica del tipo probable en N3. Korax presenta, operador decide destino.

## crear_objetivo

- **Firma:** crear_objetivo(tipo: "PROPOSITO" | "RESULTADO", titulo: string, parent_id?: ObjetivoId, anti_vision?: string, restricciones?: string[], motivo?: { texto: string, tipo: "adverso" | "favorable", urgencia?: "alta" | "media" | "baja", ventana_fin?: date }) -> Objetivo
- **Binding:** `python3 $PCA_CLI crear-objetivo --tipo <T> --titulo "<t>" [--parent-id <id>] [--anti-vision "<v>"] [--restricciones "r1|r2"] [--motivo-texto "<m>"] [--motivo-tipo adverso|favorable] [--motivo-urgencia alta|media|baja] [--motivo-ventana-fin <date>]`
- **Cuando usar:** Al crear un Objetivo durante triaje N3 (RESULTADO o PROPOSITO) o fuera de triaje.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** RI-01, RI-08, RI-09 enforzados por PCA system. El campo `motivo` de la firma semantica se descompone en 4 flags CLI: `--motivo-texto`, `--motivo-tipo`, `--motivo-urgencia`, `--motivo-ventana-fin`.

## crear_proyecto

- **Firma:** crear_proyecto(titulo: string, resultado_id: ObjetivoId) -> Proyecto { id: ProyectoId, titulo: string, estado: "activo", contribuciones: [], uts: [] }
- **Binding:** `python3 $PCA_CLI crear-proyecto --titulo "<t>" --resultado-id <id>`
- **Cuando usar:** Al crear un contenedor para UTs asociadas a un RESULTADO. Se crea en planificacion, no en triaje (§3.3).
- **Cuando NO usar:** Sin RESULTADO definido.
- **Notas:** Membresia exclusiva. Crea contribucion constitutiva automatica al RESULTADO.

## crear_contribucion

- **Firma:** crear_contribucion(fuente_tipo: "ut" | "proyecto", fuente_id: string, resultado_id: ObjetivoId, tipo: "constitutiva" | "instrumental" | "evidencial") -> Contribucion
- **Binding:** `python3 $PCA_CLI crear-contribucion --fuente-tipo Proyecto|UT --fuente-id <fid> --resultado-id <rid> --tipo <t>` (CLI acepta tambien lowercase: proyecto, ut)
- **Cuando usar:** Al vincular una entidad con un RESULTADO.
- **Cuando NO usar:** Sin RESULTADO destino definido. Si fuente_tipo=ut y UT tiene proyecto_id (RI-07).
- **Notas:** RI-02, RI-03, RI-07 enforzados por PCA system.

## asignar_ut_proyecto

- **Firma:** asignar_ut_proyecto(ut_id: UTId, proyecto_id: ProyectoId) -> UT
- **Binding:** `python3 $PCA_CLI asignar-ut <ut_id> --proyecto <proyecto_id>`
- **Cuando usar:** Al organizar UTs dentro de un Proyecto.
- **Cuando NO usar:** UT ya asignada a otro Proyecto (membresia exclusiva). RI-07 enforzado por PCA system.

## bloquear_ut

- **Firma:** bloquear_ut(ut_id: UTId, bloqueada_por: UTId) -> UT { estado: "bloqueada" }
- **Binding:** `python3 $PCA_CLI bloquear <ut_id> --por <bloqueada_por>`
- **Cuando usar:** Al registrar dependencia de bloqueo duro entre UTs.
- **Cuando NO usar:** UT ya completada o descartada. Crearia ciclo en DAG (RI-04).
- **Notas:** RI-04 (DAG) enforzado por PCA system via recursive CTE.

## completar_ut

- **Firma:** completar_ut(ut_id: UTId) -> UT { estado: "completada" }
- **Binding:** `python3 $PCA_CLI completar-ut <ut_id>`
- **Cuando usar:** Al marcar una UT como terminada.
- **Cuando NO usar:** UT no existe o ya completada.

## descartar_ut

- **Firma:** descartar_ut(ut_id: UTId) -> UT { estado: "descartada" }
- **Binding:** `python3 $PCA_CLI descartar-ut <ut_id>`
- **Cuando usar:** Al eliminar una UT del sistema activo.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** PCA system detecta y retorna UTs huerfanas (RI-06) en el JSON de respuesta.

## pausar_proyecto

- **Firma:** pausar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "pausado" }
- **Binding:** `python3 $PCA_CLI pausar-proyecto <proyecto_id>`
- **Cuando usar:** Al suspender temporalmente un Proyecto. UTs conservan estado pero no se presentan en planificacion.
- **Cuando NO usar:** Proyecto ya completado o descartado.

## reactivar_proyecto

- **Firma:** reactivar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "activo" }
- **Binding:** `python3 $PCA_CLI reactivar-proyecto <proyecto_id>`
- **Cuando usar:** Al reactivar un Proyecto pausado. UTs vuelven a ser elegibles para planificacion.
- **Cuando NO usar:** Proyecto no esta pausado.

## completar_proyecto

- **Firma:** completar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "completado" }
- **Binding:** `python3 $PCA_CLI completar-proyecto <proyecto_id>`
- **Cuando usar:** Korax senaliza que todas las UTs estan en completada/descartada; operador confirma (RI-05).
- **Cuando NO usar:** Hay UTs activas en el Proyecto. Sin confirmacion del operador.
- **Notas:** RI-05 enforzado por PCA system.

## descartar_proyecto

- **Firma:** descartar_proyecto(proyecto_id: ProyectoId) -> { proyecto: Proyecto, uts_activas: UT[], contribuciones_rotas: Contribucion[], accion_pendiente: bool }
- **Binding:** `python3 $PCA_CLI descartar-proyecto <proyecto_id>`
- **Cuando usar:** Al eliminar un Proyecto del sistema activo.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** PCA system computa Polo B (INV-13) y retorna UTs activas + contribuciones rotas en JSON.

## plan_diario

- **Firma:** plan_diario(fecha?: string) -> PlanDiario { fecha: string, uts_ordenadas: UT_scored[], bloqueadas: UT[], restriccion_warnings: Warning[], proyectos_activos: int, uts_pendientes: int }
- **Binding:** `python3 $PCA_CLI plan [--fecha <YYYY-MM-DD>]`
- **Cuando usar:** Planificacion matutina. Estado: S-PLAN.
- **Cuando NO usar:** Fuera de rutina matutina.
- **Notas:** PCA system computa P, U, PxU por cada UT, filtra proyectos pausados, y verifica restricciones (RI-12). `uts_ordenadas` incluye campos P, U, PxU. Korax deriva bloques (DEEP/SHALLOW/SOCIAL) del campo `modo` y presenta el plan como propuesta.

## iniciar_bloque

- **Firma:** iniciar_bloque(ut_id: UTId) -> UT { estado: "en_progreso" }
- **Binding:** `python3 $PCA_CLI iniciar-bloque <ut_id>`
- **Cuando usar:** Al comenzar ejecucion de un bloque. Estado: S-EXECUTE.
- **Cuando NO usar:** Sin plan diario activo.

## completar_bloque

- **Firma:** completar_bloque(ut_id: UTId, completada: bool) -> UT { estado: "completada" | "pendiente" }
- **Binding:** `python3 $PCA_CLI completar-bloque <ut_id> [--interrumpida]`
- **Cuando usar:** Al finalizar un bloque de ejecucion. Si completada=false, UT vuelve a pendiente (interrupcion).
- **Cuando NO usar:** UT no esta en progreso.

## estado

- **Firma:** estado() -> Dashboard { candidatos: int, uts_por_estado: Record<string, int>, proyectos: ProyectoResumen[], objetivos: ObjetivoResumen[], alertas: Alerta[] }
- **Binding:** `python3 $PCA_CLI estado`
- **Cuando usar:** Consulta rapida de estado. Cualquier momento.
- **Cuando NO usar:** Nunca restringido.
- **Notas:** Solo lectura. Incluye alertas computadas por PCA system.

## completitud

- **Firma:** completitud(objetivo_id: ObjetivoId) -> number | null
- **Binding:** `python3 $PCA_CLI completitud <objetivo_id>`
- **Cuando usar:** Evaluar progreso de un Objetivo (PROPOSITO o RESULTADO).
- **Cuando NO usar:** Nunca restringido.

## sync

- **Firma:** sync(dias?: int) -> ReporteSync { periodo_dias: int, completitudes: Record<ObjetivoId, { titulo: string, tipo: string, completitud: number | null }>, throughput: { completadas: int, creadas: int, balance: int }, alertas: Signal[], colapso: CollapseEval }
- **Binding:** `python3 $PCA_CLI sync [--dias 14]`
- **Cuando usar:** Sincronizacion estrategica quincenal. Estado: S-SYNC.
- **Cuando NO usar:** Fuera de rutina de sincronizacion.
- **Notas:** DEBE requerir participacion del operador. `completitudes` incluye titulo y tipo para que Korax pueda presentar sin queries adicionales.

## signals

- **Firma:** signals() -> Signal[]
- **Binding:** `python3 $PCA_CLI signals`
- **Cuando usar:** Evaluar senales activas del sistema. Usado en S-CLOSE (micro-check), S-COLLAPSE (evaluacion) y cualquier momento.
- **Cuando NO usar:** Nunca restringido.

## throughput

- **Firma:** throughput(dias?: int) -> { periodo_dias: int, completadas: int, creadas: int, balance: int }
- **Binding:** `python3 $PCA_CLI throughput [--dias <n>]`
- **Cuando usar:** Evaluar velocidad de ejecucion en periodo.
- **Cuando NO usar:** Nunca restringido.

## emergencia

- **Firma:** emergencia() -> ModoEmergencia { fase: "bancarrota" | "gracia" | "reconstruccion" }
- **Binding:** Sin CLI directo. Korax evalua colapso via `python3 $PCA_CLI signals` (que incluye evaluacion de 5 senales de colapso). La gestion de fases (bancarrota/gracia/reconstruccion) es estado interno del agente.
- **Cuando usar:** Colapso detectado o percibido. Estado: S-COLLAPSE.
- **Cuando NO usar:** Sistema saludable.
- **Notas:** El PCA system provee la evaluacion (via signals); Korax gestiona el protocolo de fases.

## caos

- **Firma:** caos(horas: number) -> ModoCaos { inicio: ISO8601, fin_estimado: ISO8601 }
- **Binding:** Sin CLI. Estado puramente interno del agente (silencio total, heartbeats encolados). No requiere persistencia PCA.
- **Cuando usar:** Operador necesita tiempo sin sistema. Estado: S-CHAOS.
- **Cuando NO usar:** No restringido.

---

**Coaching y Bienestar (Manual de Vida):** Los siguientes tools operan via conversacion, no via PCA CLI. No persisten datos — acompanan al operador en tiempo real.

## regulacion_emocional

- **Firma:** regulacion_emocional() -> DiagnosticoEmocional { emocion: string, intensidad: int, fits_the_facts: bool, intervencion: string }
- **Binding:** Sin CLI. Conversacional (8 firmas corporales → calibracion → accion opuesta).
- **Cuando usar:** S-PLAN (check-in detecta distress), S-EXECUTE (resistencia/procrastinacion detectada).
- **Cuando NO usar:** Operador no muestra senales de distress emocional.
- **Notas:** Traces to manual-de-vida §5.1-5.2, §6.3. Incluye Ready-Set-Go rapido para procrastinacion.

## rescate

- **Firma:** rescate() -> Estabilizacion { tip: string, emocion: string, intervencion: string, accion_minima: string }
- **Binding:** Sin CLI. Conversacional (TIP → detectar → regular → reconectar).
- **Cuando usar:** S-COLLAPSE (colapso confirmado, antes de CM-BANCARROTA), S-ABANDON (antes de opciones), operador senala crisis explicita.
- **Cuando NO usar:** Sistema saludable, operador estable.
- **Notas:** Traces to manual-de-vida §9, §5.3, §5.4. REGULACION primero, siempre.

## reflexion

- **Firma:** reflexion(periodo: "diario" | "semanal" | "mensual" | "trimestral") -> Reflexion { wins: string[], lessons: string[], intencion: string }
- **Binding:** Sin CLI. Conversacional (3-2-1 + revisiones periodicas).
- **Cuando usar:** S-CLOSE (reflexion diaria, despues de micro-check PCA), S-SYNC (semanal/mensual), trimestral.
- **Cuando NO usar:** Operador pide cierre rapido sin reflexion.
- **Notas:** Traces to manual-de-vida §8, §11.

## catalizador

- **Firma:** catalizador() -> DiagnosticoVital { human30: Record<string, int>, apalancamiento: string, lwlg_status: string, anti_vision_status: string }
- **Binding:** Sin CLI. Conversacional (HUMAN 3.0 diagnosis + LWLG alignment + anti-vision filter).
- **Cuando usar:** S-SYNC (despues de 4 preguntas PCA), revision trimestral, operador solicita diagnostico vital.
- **Cuando NO usar:** Fuera de contexto estrategico.
- **Notas:** Traces to manual-de-vida §7.1, §7.2, §6.1; dan-koe-filosofia-creador HUMAN 3.0.

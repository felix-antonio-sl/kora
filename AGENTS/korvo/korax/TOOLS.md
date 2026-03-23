---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korax-tools:3.4.0"
  type: "bootstrap_tools"
---

**Runtime Binding:** PCA API via HTTP. Base URL: `$PCA_API` (default: `http://kora-pca:8100/api`). Output: JSON. Todos los POST envian `Content-Type: application/json`. Korax parsea el JSON y presenta al operador.

```
PCA_API = http://kora-pca:8100/api
GET:  curl -s $PCA_API/<endpoint>[?param=val]
POST: curl -s -X POST $PCA_API/<endpoint> -H 'Content-Type: application/json' -d '{...}'
```

### Modelo PCA v4.1

Entidades tipadas PCA v4.1:

| Entidad | Descripcion |
| --- | --- |
| **Candidato** | Input capturado sin procesar. Estados: `capturado \| en_triaje \| promovido \| incubado \| descartado`. Campos: id, texto, fuente (telegram\|email\|conversacion\|nota\|otro), capturado_at, destino_tipo?, destino_id? (cuando promovido, per RI-10). |
| **UT** (Unidad de Trabajo) | Atomo ejecutable. Estados: `pendiente \| en_progreso \| bloqueada \| completada \| descartada`. Campos: id, titulo, modo (set de `FM\|SR\|MK`), timebox (`15\|30\|60\|90`), deadline?, proyecto_id? (membresia exclusiva), P (prioridad derivada), U (urgencia derivada), bloquea_a[], bloqueada_por[], contribuye_a[] (solo free-floating per RI-07), situacion_temporal?, situacion_fisica?, creado_at (ISO8601), actualizado_at (ISO8601 — ultimo cambio de estado). |
| **Proyecto** | Contenedor de UTs con membresia exclusiva. Estados: `activo \| pausado \| completado \| descartado`. Campos: id, titulo, contribuciones[], uts[], estado, creado_at (ISO8601). FSM propio. Polo B al descartar. Se crea en planificacion, no en triaje. |
| **Objetivo** | Coproducto de dos subtipos. Campos comunes: id, tipo (PROPOSITO\|RESULTADO), titulo, estado, creado_at (ISO8601). PROPOSITO: anti_vision?, restricciones? (limites no negociables, verificados por Korax per RI-12). RESULTADO: parent_id? (FK a PROPOSITO), contribuciones[], motivo? (texto + tipo adverso\|favorable + urgencia? + ventana_fin?). Estados: `activo \| logrado \| descartado`. |
| **Contribucion** | Relacion tipada. Campos: id (identificador unico), fuente_tipo (Proyecto\|UT), fuente_id, resultado_id (siempre RESULTADO, nunca PROPOSITO per RI-03), tipo (`constitutiva \| instrumental \| evidencial`). |

**Sub-campos opcionales de UT:** situacion_temporal (ventana_inicio, ventana_fin, dias_semana, restriccion) y situacion_fisica (lugares, herramientas, conectividad). Gestionados por PCA API.

### Dimensiones del Trabajo (§5 PCA v4.1)

**Dimensiones ortogonales (UT.modo):**

| Codigo | Dimension | Requiere |
| --- | --- | --- |
| `FM` | Fisico/Material | Presencia fisica, herramientas |
| `SR` | Social/Relacional | Disponibilidad de otros |
| `MK` | Mental/Conocimiento | Bloque concentracion, energia alta |

**Modos energeticos derivados (para bloques):**

| Combinacion | Bloque | Timebox tipico |
| --- | --- | --- |
| `MK` solo | DEEP | 60-120 min, energia alta, cero interrupciones |
| `FM` o `MK+FM` | SHALLOW | 15-45 min, energia media |
| `SR` (con otros) | SOCIAL | Variable, requiere disponibilidad externa |

**Computo de P (prioridad):**

```
si UT sin contribucion:
  P = 0.2  (work-in-vacuum)

si UT con contribucion:
  P = peso(contribucion.tipo) * nivel_efectivo(resultado)

  peso(constitutiva) = 1.0
  peso(instrumental) = 0.5
  peso(evidencial)   = 0.3

  nivel_efectivo(resultado) =
    1.0  si resultado.parent_id existe  (anclado a PROPOSITO)
    0.7  si resultado.parent_id = null  (RESULTADO flotante)
```

**Computo de U (urgencia):**

```
U = 0.0                            si sin deadline
U = min(1.0, 1 / dias_a_deadline)  si dias_a_deadline > 0
U = 1.0                            si deadline pasado (overdue)
```

**Interpretacion de P:**

| P | Interpretacion |
| --- | --- |
| >= 0.7 | Trabajo critico para objetivos primarios |
| 0.4-0.7 | Trabajo relevante, RESULTADO sin ancla estrategica |
| < 0.4 | Trabajo de bajo peso estrategico |

**Interpretacion de U:**

| U | Interpretacion |
| --- | --- |
| >= 0.8 | Critico: menos de ~3 dias |
| 0.5-0.8 | Urgente: menos de ~7 dias |
| 0.2-0.5 | Proximo: menos de ~2 semanas |
| < 0.2 | Sin presion inmediata |

**Umbral critico:** U > 0.8 activa alerta automatica del agente.

**Matriz PxU -> accion del agente:**

| P \ U | Baja (< 0.5) | Alta (>= 0.5) |
| --- | --- | --- |
| **Alta (>= 0.6)** | Programar para proximo bloque DEEP | Alerta: P alta + U alta; proponer asignacion inmediata |
| **Baja (< 0.6)** | Diferir; no presentar en planificacion | Completar rapido; evaluar si contribucion vale |

**completitud() — funcion derivada on-demand (§6.6):**

```
completitud(RESULTADO) =
  count(constitutivas con fuente.estado = completada|completado)
  / count(constitutivas)

completitud(PROPOSITO) =
  mean(completitud(RESULTADO_i) para RESULTADO_i con parent_id = PROPOSITO.id)
```

Condiciones: completitud=1.0 -> senalizar `logrado` (no declarar autonomamente). Sin constitutivas -> null.

## pca_init

- **Firma:** pca_init() -> { status: "ok", db: string }
- **Binding:** `POST $PCA_API/init`
- **Cuando usar:** Primera ejecucion o cuando la DB no existe.
- **Cuando NO usar:** DB ya inicializada.

## captura

- **Firma:** captura(texto: string, fuente?: "telegram" | "email" | "conversacion" | "nota" | "otro") -> Candidato { id: CandidatoId, texto: string, fuente: string, estado: "capturado", capturado_at: ISO8601 }
- **Binding:** `POST $PCA_API/captura` body: `{"texto": "<texto>", "fuente": "<f>"}`
- **Cuando usar:** Captura rapida al buffer. Estado: S-CAPTURE.
- **Cuando NO usar:** Fuera de captura.
- **Notas:** No agrega metadatos de trabajo (modo, urgencia, prioridad). Solo texto + fuente + timestamp (INV-05, P2). Fuente se auto-detecta del canal si no se provee.

## triaje

- **Firma:** triaje() -> SesionTriaje { procesados: int, por_tipo: { ut: int, resultado: int, proposito: int, incubado: int, descartado: int } }
- **Binding (compuesto):**
  1. `GET $PCA_API/buffer` → lista Candidatos pendientes (JSON array)
  2. Por cada candidato, segun decision del operador:
     - `POST $PCA_API/triaje/promover` body: `{"candidato_id":"<id>","tipo":"ut","titulo":"...","modo":["FM","MK"],"timebox":60,"deadline":"YYYY-MM-DD","proyecto_id":"<id>"}`
     - `POST $PCA_API/triaje/promover` body: `{"candidato_id":"<id>","tipo":"resultado","titulo":"...","parent_id":"<id>","motivo_tipo":"adverso","motivo_urgencia":"alta","motivo_texto":"..."}`
     - `POST $PCA_API/triaje/promover` body: `{"candidato_id":"<id>","tipo":"proposito","titulo":"...","anti_vision":"...","restricciones":["r1","r2"]}`
     - `POST $PCA_API/triaje/incubar` body: `{"candidato_id":"<id>"}`
     - `POST $PCA_API/triaje/descartar` body: `{"candidato_id":"<id>"}`
  3. Korax agrega conteos localmente para el SesionTriaje report.
- **Cuando usar:** Procesamiento del buffer de Candidatos. Estado: S-TRIAGE.
- **Cuando NO usar:** Buffer vacio.
- **Notas:** Arbol de decision N1/N2/N3 (§4.1). Senalizacion lexica del tipo probable en N3. Korax presenta, operador decide destino.

## crear_objetivo

- **Firma:** crear_objetivo(tipo: "PROPOSITO" | "RESULTADO", titulo: string, parent_id?: ObjetivoId, anti_vision?: string, restricciones?: string[], motivo?: { texto: string, tipo: "adverso" | "favorable", urgencia?: "alta" | "media" | "baja", ventana_fin?: date }) -> Objetivo
- **Binding:** `POST $PCA_API/objetivo` body: `{"tipo":"PROPOSITO|RESULTADO","titulo":"...","parent_id":"<id>","anti_vision":"...","restricciones":["r1"],"motivo_texto":"...","motivo_tipo":"adverso|favorable","motivo_urgencia":"alta|media|baja","motivo_ventana_fin":"YYYY-MM-DD"}`
- **Cuando usar:** Al crear un Objetivo durante triaje N3 (RESULTADO o PROPOSITO) o fuera de triaje.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** RI-01, RI-08, RI-09 enforzados por PCA system. El campo `motivo` de la firma semantica se descompone en 4 flags CLI: `--motivo-texto`, `--motivo-tipo`, `--motivo-urgencia`, `--motivo-ventana-fin`.

## crear_proyecto

- **Firma:** crear_proyecto(titulo: string, resultado_id: ObjetivoId) -> Proyecto { id: ProyectoId, titulo: string, estado: "activo", contribuciones: [], uts: [] }
- **Binding:** `POST $PCA_API/proyecto` body: `{"titulo":"...","resultado_id":"<id>"}`
- **Cuando usar:** Al crear un contenedor para UTs asociadas a un RESULTADO. Se crea en planificacion, no en triaje (§3.3).
- **Cuando NO usar:** Sin RESULTADO definido.
- **Notas:** Membresia exclusiva. Crea contribucion constitutiva automatica al RESULTADO.

## crear_contribucion

- **Firma:** crear_contribucion(fuente_tipo: "ut" | "proyecto", fuente_id: string, resultado_id: ObjetivoId, tipo: "constitutiva" | "instrumental" | "evidencial") -> Contribucion
- **Binding:** `POST $PCA_API/contribucion` body: `{"fuente_tipo":"Proyecto|UT","fuente_id":"<fid>","resultado_id":"<rid>","tipo":"constitutiva|instrumental|evidencial"}`
- **Cuando usar:** Al vincular una entidad con un RESULTADO.
- **Cuando NO usar:** Sin RESULTADO destino definido. Si fuente_tipo=ut y UT tiene proyecto_id (RI-07).
- **Notas:** RI-02, RI-03, RI-07 enforzados por PCA system.

## asignar_ut_proyecto

- **Firma:** asignar_ut_proyecto(ut_id: UTId, proyecto_id: ProyectoId) -> UT
- **Binding:** `POST $PCA_API/asignar-ut` body: `{"ut_id":"<id>","proyecto_id":"<id>"}`
- **Cuando usar:** Al organizar UTs dentro de un Proyecto.
- **Cuando NO usar:** UT ya asignada a otro Proyecto (membresia exclusiva). RI-07 enforzado por PCA system.

## bloquear_ut

- **Firma:** bloquear_ut(ut_id: UTId, bloqueada_por: UTId) -> UT { estado: "bloqueada" }
- **Binding:** `POST $PCA_API/bloquear` body: `{"ut_id":"<id>","bloqueada_por":"<id>"}`
- **Cuando usar:** Al registrar dependencia de bloqueo duro entre UTs.
- **Cuando NO usar:** UT ya completada o descartada. Crearia ciclo en DAG (RI-04).
- **Notas:** RI-04 (DAG) enforzado por PCA system via recursive CTE.

## completar_ut

- **Firma:** completar_ut(ut_id: UTId) -> UT { estado: "completada" }
- **Binding:** `POST $PCA_API/completar-ut` body: `{"ut_id":"<id>"}`
- **Cuando usar:** Al marcar una UT como terminada.
- **Cuando NO usar:** UT no existe o ya completada.

## descartar_ut

- **Firma:** descartar_ut(ut_id: UTId) -> UT { estado: "descartada" }
- **Binding:** `POST $PCA_API/descartar-ut` body: `{"ut_id":"<id>"}`
- **Cuando usar:** Al eliminar una UT del sistema activo.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** PCA system detecta y retorna UTs huerfanas (RI-06) en el JSON de respuesta.

## pausar_proyecto

- **Firma:** pausar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "pausado" }
- **Binding:** `POST $PCA_API/pausar-proyecto` body: `{"proyecto_id":"<id>"}`
- **Cuando usar:** Al suspender temporalmente un Proyecto. UTs conservan estado pero no se presentan en planificacion.
- **Cuando NO usar:** Proyecto ya completado o descartado.

## reactivar_proyecto

- **Firma:** reactivar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "activo" }
- **Binding:** `POST $PCA_API/reactivar-proyecto` body: `{"proyecto_id":"<id>"}`
- **Cuando usar:** Al reactivar un Proyecto pausado. UTs vuelven a ser elegibles para planificacion.
- **Cuando NO usar:** Proyecto no esta pausado.

## completar_proyecto

- **Firma:** completar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "completado" }
- **Binding:** `POST $PCA_API/completar-proyecto` body: `{"proyecto_id":"<id>"}`
- **Cuando usar:** Korax senaliza que todas las UTs estan en completada/descartada; operador confirma (RI-05).
- **Cuando NO usar:** Hay UTs activas en el Proyecto. Sin confirmacion del operador.
- **Notas:** RI-05 enforzado por PCA system.

## descartar_proyecto

- **Firma:** descartar_proyecto(proyecto_id: ProyectoId) -> { proyecto: Proyecto, uts_activas: UT[], contribuciones_rotas: Contribucion[], accion_pendiente: bool }
- **Binding:** `POST $PCA_API/descartar-proyecto` body: `{"proyecto_id":"<id>"}`
- **Cuando usar:** Al eliminar un Proyecto del sistema activo.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** PCA system computa Polo B (INV-13) y retorna UTs activas + contribuciones rotas en JSON.

## plan_diario

- **Firma:** plan_diario(fecha?: string) -> PlanDiario { fecha: string, uts_ordenadas: UT_scored[], bloqueadas: UT[], restriccion_warnings: Warning[], proyectos_activos: int, uts_pendientes: int }
- **Binding:** `GET $PCA_API/plan[?fecha=YYYY-MM-DD]`
- **Cuando usar:** Planificacion matutina. Estado: S-PLAN.
- **Cuando NO usar:** Fuera de rutina matutina.
- **Notas:** PCA system computa P, U, PxU por cada UT, filtra proyectos pausados, y verifica restricciones (RI-12). `uts_ordenadas` incluye campos P, U, PxU. Korax deriva bloques (DEEP/SHALLOW/SOCIAL) del campo `modo` y presenta el plan como propuesta.

## iniciar_bloque

- **Firma:** iniciar_bloque(ut_id: UTId) -> UT { estado: "en_progreso" }
- **Binding:** `POST $PCA_API/iniciar-bloque` body: `{"ut_id":"<id>"}`
- **Cuando usar:** Al comenzar ejecucion de un bloque. Estado: S-EXECUTE.
- **Cuando NO usar:** Sin plan diario activo.

## completar_bloque

- **Firma:** completar_bloque(ut_id: UTId, completada: bool) -> UT { estado: "completada" | "pendiente" }
- **Binding:** `POST $PCA_API/completar-bloque` body: `{"ut_id":"<id>","interrumpida":false}`
- **Cuando usar:** Al finalizar un bloque de ejecucion. Si completada=false, UT vuelve a pendiente (interrupcion).
- **Cuando NO usar:** UT no esta en progreso.

## estado

- **Firma:** estado() -> Dashboard { candidatos: int, uts_por_estado: Record<string, int>, proyectos: ProyectoResumen[], objetivos: ObjetivoResumen[], alertas: Alerta[] }
- **Binding:** `GET $PCA_API/estado`
- **Cuando usar:** Consulta rapida de estado. Cualquier momento.
- **Cuando NO usar:** Nunca restringido.
- **Notas:** Solo lectura. Incluye alertas computadas por PCA system.

## completitud

- **Firma:** completitud(objetivo_id: ObjetivoId) -> number | null
- **Binding:** `GET $PCA_API/completitud/<objetivo_id>`
- **Cuando usar:** Evaluar progreso de un Objetivo (PROPOSITO o RESULTADO).
- **Cuando NO usar:** Nunca restringido.

## sync

- **Firma:** sync(dias?: int) -> ReporteSync { periodo_dias: int, completitudes: Record<ObjetivoId, { titulo: string, tipo: string, completitud: number | null }>, throughput: { completadas: int, creadas: int, balance: int }, alertas: Signal[], colapso: CollapseEval }
- **Binding:** `GET $PCA_API/sync[?dias=14]`
- **Cuando usar:** Sincronizacion estrategica quincenal. Estado: S-SYNC.
- **Cuando NO usar:** Fuera de rutina de sincronizacion.
- **Notas:** DEBE requerir participacion del operador. `completitudes` incluye titulo y tipo para que Korax pueda presentar sin queries adicionales.

## signals

- **Firma:** signals() -> Signal[]
- **Binding:** `GET $PCA_API/signals`
- **Cuando usar:** Evaluar senales activas del sistema. Usado en S-CLOSE (micro-check), S-COLLAPSE (evaluacion) y cualquier momento.
- **Cuando NO usar:** Nunca restringido.

## throughput

- **Firma:** throughput(dias?: int) -> { periodo_dias: int, completadas: int, creadas: int, balance: int }
- **Binding:** `GET $PCA_API/throughput[?dias=<n>]`
- **Cuando usar:** Evaluar velocidad de ejecucion en periodo.
- **Cuando NO usar:** Nunca restringido.

## emergencia

- **Firma:** emergencia() -> ModoEmergencia { fase: "bancarrota" | "gracia" | "reconstruccion" }
- **Binding:** Sin endpoint directo. Korax evalua colapso via `GET $PCA_API/signals` (que incluye evaluacion de 5 senales de colapso). La gestion de fases (bancarrota/gracia/reconstruccion) es estado interno del agente.
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

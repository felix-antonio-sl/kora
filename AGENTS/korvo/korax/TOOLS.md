---
_manifest:
  urn: "urn:korvo:agent-bootstrap:korax-tools:3.0.0"
  type: "bootstrap_tools"
---

## captura

- **Firma:** captura(texto: string, fuente?: "telegram" | "email" | "conversacion" | "nota" | "otro") -> Candidato { id: CandidatoId, texto: string, fuente: string, estado: "capturado", capturado_at: ISO8601 }
- **Cuando usar:** Captura rapida al buffer. Estado: S-CAPTURE.
- **Cuando NO usar:** Fuera de captura.
- **Notas:** No agrega metadatos de trabajo (modo, urgencia, prioridad). Solo texto + fuente + timestamp (INV-05, P2). Fuente se auto-detecta del canal si no se provee.

## triaje

- **Firma:** triaje() -> SesionTriaje { procesados: int, por_tipo: { ut: int, resultado: int, proposito: int, incubado: int, descartado: int } }
- **Cuando usar:** Procesamiento del buffer de Candidatos. Estado: S-TRIAGE.
- **Cuando NO usar:** Buffer vacio.
- **Notas:** Arbol de decision N1/N2/N3 (§4.1). Senalizacion lexica del tipo probable en N3. Korax presenta, operador decide destino.

## crear_objetivo

- **Firma:** crear_objetivo(tipo: "PROPOSITO" | "RESULTADO", titulo: string, parent_id?: ObjetivoId, anti_vision?: string, restricciones?: string[], motivo?: { texto: string, tipo: "adverso" | "favorable", urgencia?: "alta" | "media" | "baja", ventana_fin?: date }) -> Objetivo
- **Cuando usar:** Al crear un Objetivo durante triaje N3 (RESULTADO o PROPOSITO) o fuera de triaje.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** RI-01: parent_id debe apuntar a PROPOSITO existente. RI-08: motivo.tipo=adverso requiere urgencia. RI-09: motivo.tipo=favorable requiere ventana_fin.

## crear_proyecto

- **Firma:** crear_proyecto(titulo: string, resultado_id: ObjetivoId) -> Proyecto { id: ProyectoId, titulo: string, estado: "activo", contribuciones: [], uts: [] }
- **Cuando usar:** Al crear un contenedor para UTs asociadas a un RESULTADO. Se crea en planificacion, no en triaje (§3.3).
- **Cuando NO usar:** Sin RESULTADO definido.
- **Notas:** Membresia exclusiva: cada UT pertenece a maximo un Proyecto.

## crear_contribucion

- **Firma:** crear_contribucion(fuente_tipo: "ut" | "proyecto", fuente_id: string, resultado_id: ObjetivoId, tipo: "constitutiva" | "instrumental" | "evidencial") -> Contribucion
- **Cuando usar:** Al vincular una entidad con un RESULTADO.
- **Cuando NO usar:** Sin RESULTADO destino definido. Si fuente_tipo=ut y UT tiene proyecto_id (RI-07).
- **Notas:** RI-02: fuente_id debe referenciar UT free-floating o Proyecto existente. RI-03: resultado_id debe referenciar RESULTADO, nunca PROPOSITO. Contribuciones constitutivas se marcan rotas al descartar Proyecto fuente (Polo B).

## asignar_ut_proyecto

- **Firma:** asignar_ut_proyecto(ut_id: UTId, proyecto_id: ProyectoId) -> UT
- **Cuando usar:** Al organizar UTs dentro de un Proyecto.
- **Cuando NO usar:** UT ya asignada a otro Proyecto (membresia exclusiva). UT con contribuye_a no vacio (RI-07: al asignar, contribuye_a debe vaciarse y contribucion ir via Proyecto).

## bloquear_ut

- **Firma:** bloquear_ut(ut_id: UTId, bloqueada_por: UTId) -> UT { estado: "bloqueada" }
- **Cuando usar:** Al registrar dependencia de bloqueo duro entre UTs.
- **Cuando NO usar:** UT ya completada o descartada. Crearia ciclo en DAG (RI-04).
- **Notas:** Valida DAG (RI-04). Bloqueos cross-project >7d generan senal.

## completar_ut

- **Firma:** completar_ut(ut_id: UTId) -> UT { estado: "completada" }
- **Cuando usar:** Al marcar una UT como terminada.
- **Cuando NO usar:** UT no existe o ya completada.

## descartar_ut

- **Firma:** descartar_ut(ut_id: UTId) -> UT { estado: "descartada" }
- **Cuando usar:** Al eliminar una UT del sistema activo.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** Si UTs dependen de esta (bloqueada_por), senalizar desbloqueo al operador (RI-06).

## pausar_proyecto

- **Firma:** pausar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "pausado" }
- **Cuando usar:** Al suspender temporalmente un Proyecto. UTs conservan estado pero no se presentan en planificacion.
- **Cuando NO usar:** Proyecto ya completado o descartado.

## reactivar_proyecto

- **Firma:** reactivar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "activo" }
- **Cuando usar:** Al reactivar un Proyecto pausado. UTs vuelven a ser elegibles para planificacion.
- **Cuando NO usar:** Proyecto no esta pausado.

## completar_proyecto

- **Firma:** completar_proyecto(proyecto_id: ProyectoId) -> Proyecto { estado: "completado" }
- **Cuando usar:** Korax senaliza que todas las UTs estan en completada/descartada; operador confirma (RI-05).
- **Cuando NO usar:** Hay UTs activas en el Proyecto. Sin confirmacion del operador.

## descartar_proyecto

- **Firma:** descartar_proyecto(proyecto_id: ProyectoId) -> { proyecto: Proyecto, uts_activas: UT[], contribuciones_constitutivas: Contribucion[], accion_pendiente: true }
- **Cuando usar:** Al eliminar un Proyecto del sistema activo.
- **Cuando NO usar:** Sin confirmacion del operador.
- **Notas:** Polo B (RI-11): senalizar UTs activas para que operador decida descartar o liberar como free-floating. Contribuciones constitutivas se marcan rotas (INV-13) y se senaliza impacto en completitud de RESULTADO.

## plan_diario

- **Firma:** plan_diario(date: string) -> PlanDiario { bloques: Bloque[], uts_ordenadas_pxu: UT[] }
- **Cuando usar:** Planificacion matutina. Estado: S-PLAN.
- **Cuando NO usar:** Fuera de rutina matutina.
- **Notas:** Ordena UTs por P x U. Bloques segun modo energetico derivado de UT.modo (MK->DEEP, FM->SHALLOW, SR->SOCIAL). Filtra por ST/SF cuando disponibles. Verifica restricciones de PROPOSITO ancestral (RI-12).

## iniciar_bloque

- **Firma:** iniciar_bloque(ut_id: UTId) -> UT { estado: "en_progreso" }
- **Cuando usar:** Al comenzar ejecucion de un bloque. Estado: S-EXECUTE.
- **Cuando NO usar:** Sin plan diario activo.

## completar_bloque

- **Firma:** completar_bloque(ut_id: UTId, completada: bool) -> UT { estado: "completada" | "pendiente" }
- **Cuando usar:** Al finalizar un bloque de ejecucion. Si completada=false, UT vuelve a pendiente (interrupcion).
- **Cuando NO usar:** UT no esta en progreso.

## estado

- **Firma:** estado() -> Dashboard { candidatos: int, uts_por_estado: Record<string, int>, proyectos: ProyectoResumen[], objetivos: ObjetivoResumen[], alertas: Alerta[] }
- **Cuando usar:** Consulta rapida de estado. Cualquier momento.
- **Cuando NO usar:** Nunca restringido.
- **Notas:** Solo lectura. Sin modificacion de estado.

## completitud

- **Firma:** completitud(objetivo_id: ObjetivoId) -> number | null
- **Cuando usar:** Evaluar progreso de un Objetivo (PROPOSITO o RESULTADO).
- **Cuando NO usar:** Nunca restringido.
- **Notas:** Funcion derivada on-demand (§6.6). RESULTADO: constitutivas completadas / total constitutivas. PROPOSITO: mean(completitud(RESULTADO_i)). null si no hay constitutivas.

## sync

- **Firma:** sync() -> ReporteSync { completitudes: Record<ObjetivoId, number | null>, throughput_14d: Throughput, alertas: Alerta[], candidatos_bancarrota: EntidadResumen[] }
- **Cuando usar:** Sincronizacion estrategica quincenal. Estado: S-SYNC.
- **Cuando NO usar:** Fuera de rutina de sincronizacion.
- **Notas:** DEBE requerir participacion del operador.

## emergencia

- **Firma:** emergencia() -> ModoEmergencia { fase: "bancarrota" | "gracia" | "reconstruccion" }
- **Cuando usar:** Colapso detectado o percibido. Estado: S-COLLAPSE.
- **Cuando NO usar:** Sistema saludable.
- **Notas:** Siempre requiere confirmacion del operador.

## caos

- **Firma:** caos(horas: number) -> ModoCaos { inicio: ISO8601, fin_estimado: ISO8601 }
- **Cuando usar:** Operador necesita tiempo sin sistema. Estado: S-CHAOS.
- **Cuando NO usar:** No restringido.

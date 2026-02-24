---
_manifest:
  urn: "urn:kora:agent-bootstrap:korax-tools:1.0.0"
  type: "bootstrap_tools"
---

## /inbox

- **Firma:** inbox(texto: string) → Confirmación { item: string, timestamp: ISO8601 }
- **Precondición:** Ninguna.
- **Postcondición:** Item agregado a INBOX.md con timestamp.
- **Side-effects:** Escritura en INBOX.md.
- **Delegation:** No aplica.
- **Cuando usar:** Captura rápida al buffer. Estado: S_CAPTURE.
- **Cuando NO usar:** Fuera de captura.

## /triaje

- **Firma:** triaje() → SesiónTriaje { items_procesados: int, eliminados: int, incubados: int, comprometidos: int, waiting: int }
- **Precondición:** INBOX.md tiene ≥1 item sin procesar.
- **Postcondición:** Buffer vacío. Items distribuidos a NEXT.md, WAITING.md, SOMEDAY.md o eliminados.
- **Side-effects:** Lectura/escritura en INBOX.md, NEXT.md, WAITING.md, SOMEDAY.md.
- **Delegation (scope: none):** Korax presenta cada item y pregunta destino al operador. **NO DEBE** sugerir destino.
- **Delegation (scope ⊇ triage):** Korax **PUEDE** decidir destino autónomamente. **DEBE** reportar decisiones.
- **Cuando usar:** Procesamiento del buffer. Estado: S_TRIAGE.
- **Cuando NO usar:** Buffer vacío.

## /plan

- **Firma:** plan() → PlanDiario { bloques_asignados: Bloque[], compromisos_sugeridos: Compromiso[] }
- **Precondición:** NEXT.md tiene ≥1 compromiso pendiente.
- **Postcondición:** Bloques del día asignados con compromisos.
- **Side-effects:** Lectura de calendario, lectura/escritura en NEXT.md.
- **Delegation (scope: none):** Korax presenta bloques y compromisos. El operador decide asignación.
- **Delegation (scope ⊇ plan):** Korax **PUEDE** asignar bloques según prioridad inferida. **DEBE** reportar.
- **Cuando usar:** Planificación matutina. Estado: S_PLAN.
- **Cuando NO usar:** Fuera de rutina matutina.

## /done

- **Firma:** done(item: string) → Confirmación { item: string, timestamp: ISO8601 }
- **Precondición:** Item existe en NEXT.md.
- **Postcondición:** Item movido de NEXT.md a DONE.md con timestamp de cierre.
- **Side-effects:** Escritura en NEXT.md, DONE.md.
- **Delegation:** No aplica.
- **Cuando usar:** Marcar compromiso completado. Cualquier estado.
- **Cuando NO usar:** Item no existe en NEXT.md.

## /sync

- **Firma:** sync() → ReporteSinc { compromisos_activos: int, throughput: Throughput, alertas: Alerta[], candidatos_bancarrota: Item[] }
- **Precondición:** Han pasado ≥7 días desde última sincronización.
- **Postcondición:** Reporte generado. Decisiones del operador aplicadas.
- **Side-effects:** Lectura/escritura en NEXT.md, WAITING.md, SOMEDAY.md, DONE.md.
- **Delegation:** No aplica. **DEBE** requerir participación del operador incluso con delegation_scope: full.
- **Cuando usar:** Sincronización estratégica quincenal. Estado: S_SYNC.
- **Cuando NO usar:** Fuera de rutina de sincronización.

## /estado

- **Firma:** estado() → Dashboard { compromisos: ConteoModo, waiting: int, inbox: int, alertas: Alerta[] }
- **Precondición:** Ninguna.
- **Postcondición:** Dashboard instantáneo generado. Sin modificaciones de estado.
- **Side-effects:** Solo lectura.
- **Delegation:** No aplica.
- **Cuando usar:** Consulta rápida de estado. Cualquier momento.
- **Cuando NO usar:** Nunca restringido.

## /emergencia

- **Firma:** emergencia() → ModoEmergencia { fase: "bancarrota" | "gracia" | "reconstruccion" }
- **Precondición:** Ninguna (manual o por detección automática).
- **Postcondición:** Agente entra en S_COLLAPSE. Inicia protocolo de 3 fases.
- **Side-effects:** Escritura en todos los archivos GTD durante bancarrota.
- **Delegation:** No aplica. Siempre requiere confirmación del operador.
- **Cuando usar:** Colapso detectado o percibido. Estado: S_COLLAPSE.
- **Cuando NO usar:** Sistema saludable.

## /caos

- **Firma:** caos(horas: number) → ModoCaos { inicio: ISO8601, fin_estimado: ISO8601 }
- **Precondición:** horas > 0.
- **Postcondición:** Agente entra en S_CHAOS. Silenciado total hasta expiración.
- **Side-effects:** Ninguno durante S_CHAOS.
- **Delegation:** No aplica.
- **Cuando usar:** Operador necesita tiempo sin sistema. Estado: S_CHAOS.
- **Cuando NO usar:** No restringido.

## /delegar

- **Firma:** delegar(scope: "triage" | "plan" | "maintenance" | "full") → Confirmación { scope_activo: string[], expira: ISO8601 }
- **Precondición:** Ninguna.
- **Postcondición:** delegation_scope actualizado. Timestamp registrado. Expiración calculada (default: 7 días).
- **Side-effects:** Escritura en fibra de estado (delegation_scope).
- **Delegation:** No aplica (este skill otorga delegación).
- **Cuando usar:** Operador quiere otorgar autonomía al agente.
- **Cuando NO usar:** No restringido.

## /revocar

- **Firma:** revocar(scope?: "triage" | "plan" | "maintenance" | "all") → Confirmación { scope_activo: string[] }
- **Precondición:** delegation_scope ≠ none.
- **Postcondición:** Scope indicado removido (o todos si "all"). Si no queda scope, delegation_scope = none.
- **Side-effects:** Escritura en fibra de estado (delegation_scope).
- **Delegation:** No aplica (este skill revoca delegación).
- **Cuando usar:** Operador quiere revocar autonomía del agente.
- **Cuando NO usar:** delegation_scope ya es none.

---

## Matriz de Acceso a Herramientas de Plataforma

| Herramienta | Acceso | Restricción |
|---|---|---|
| Lectura de archivos (memory/gtd/) | Allow | Solo dentro del workspace |
| Escritura de archivos (memory/gtd/) | Allow | Solo archivos GTD definidos en §10 de la spec |
| Lectura de calendario | Allow | Solo lectura, sin modificación |
| Envío de mensajes (Telegram) | Allow | Solo al operador |
| Búsqueda web | Deny | No requerido por el PCA |
| Ejecución de código | Deny | No requerido por el PCA |
| Acceso a KB externas | Deny | Workspace-only (P4) |
| Sub-agentes | Deny | Deshabilitado por P4 |

---
_manifest:
  urn: "urn:ops:skill:verificador-human-gate:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar la capa 5 de verificacion: aprobacion humana. Solo para cambios destructivos. Presentar resumen completo de todas las capas ejecutadas con evidencia, recomendacion y riesgo. HOLD para aprobacion explicita del Operador. Ultimo firewall antes de deploy.

## I/O

- **Input:** layers_executed: LayerResult[], change_type: destructiva, changeset_summary: string, coder_info: CoderInfo
- **Output:** gate_result: {status: approved|rejected|timeout, operator_comment?: string, timestamp: ISO8601, hold_duration_min: number}

## Procedimiento

1. **Compilar resumen para el Operador**:
   - Tabla de capas ejecutadas: capa, estado, detalle clave
   - Tipo de cambio: destructiva (razon de clasificacion)
   - Archivos afectados: listar archivos criticos
   - Hallazgos de seguridad: si existen warnings
   - Provider diversidad: coder vs reviewer

2. **Generar recomendacion basada en evidencia**:
   - IF todas las capas 1-4 pass sin warnings → "Recomendacion: APROBAR. 4 capas pass, sin hallazgos."
   - IF capas pass con warnings → "Recomendacion: APROBAR CON PRECAUCION. Warnings: {lista}."
   - IF hallazgos medium en seguridad → "Recomendacion: REVISAR hallazgos antes de aprobar."
   - La recomendacion NO es aprobacion. El Operador decide.

3. **Presentar y HOLD**:
   - Mostrar resumen al Operador
   - HOLD. Esperar respuesta explicita.
   - NUNCA aprobar automaticamente. NUNCA.
   - NUNCA interpretar silencio como aprobacion.

4. **Procesar respuesta del Operador**:
   - IF Operador aprueba → status = approved, registrar timestamp
   - IF Operador rechaza → status = rejected, registrar comment del Operador
   - IF timeout (configurable, default 60min) → status = timeout, tratar como rechazo

## Signature Output

```yaml
gate_result:
  status: "approved"
  operator_comment: "Revisado. Migracion schema aprobada. Proceder con rollback plan verificado."
  timestamp: "2026-02-24T14:32:00Z"
  hold_duration_min: 12
  summary_presented:
    layers_passed: [1, 2, 3, 4]
    warnings: 0
    recommendation: "APROBAR. 4 capas pass, sin hallazgos criticos."
    change_type: "destructiva"
    reason: "Schema migration ALTER TABLE orders"
```

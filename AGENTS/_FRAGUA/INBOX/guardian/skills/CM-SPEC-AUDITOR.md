---
_manifest:
  urn: urn:kora:skill:guardian-spec-auditor:1.0.0
  type: lazy_load_endofunctor
---

# CM-SPEC-AUDITOR

## Proposito
Contrastar specs fundacionales vigentes con el estado observable del repo para detectar contradicciones, drift y brechas normativas.

## Input/Output
- **Input:** scope: string (spec objetivo o "all"), modo: string ("coherencia" | "brecha" | "completo")
- **Output:** AuditReport (ver Signature Output)

## Procedimiento
1. Resolver specs objetivo via kb_route para obtener URNs relevantes.
2. Consultar specs via spec_consult para extraer reglas, invariantes y checks de validacion.
3. Ejecutar repo_health para contrastar el estado visible del repo contra las reglas extraidas.
4. Clasificar hallazgos por severidad (CRITICAL, HIGH, MEDIUM, LOW) segun gobernanza §10.1.
5. Para cada hallazgo, trazar la regla violada a la spec y seccion concreta.
6. Emitir reporte estructurado con hallazgos, contradicciones detectadas y recomendaciones.

## Signature Output
```yaml
audit_report:
  scope: "agent-spec-md"
  hallazgos:
    - severidad: "HIGH"
      spec: "agent-spec-md"
      seccion: "§4.2"
      regla: "descripcion de la regla violada"
      evidencia: "evidencia observable"
      recomendacion: "accion correctiva"
  contradicciones: []
  resumen: "N HIGH, N MEDIUM, N LOW"
```

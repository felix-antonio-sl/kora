# Nota de trazabilidad

Este paquete fusionado se construyó a partir de dos fuentes:

1. **Paquete Allan Kelly** — 4 documentos (usuarios, HU, arquitectura, wireframes)
2. **Paquete Ingeniero Fugaz** — 7 documentos (diseño, roles, backlog, blueprint, modelo datos, SQL, resumen)

La auditoría comparativa completa está en:
`../2026-04-07-auditoria-comparativa-ingeniero-fugaz.md`

## Regla de fusión aplicada

- **Base estructural:** Allan Kelly (rigor, trazabilidad normativa, FHIR, cobertura P0)
- **Complementos adoptados de IF:** DDL ejecutable, RBAC CRUD+X, teleatención, resumen ejecutivo, métricas, offline-first, datos reales
- **Sin contradicciones no resueltas:** donde había diferencia (módulos, priorización, modelo datos), se usó AK como referencia y IF como implementación MVP

# Production Promotion Checklist

## P0 — Bloqueadores

- [ ] Las skills `deploy`, `operate` y `patch applier` ejecutan pasos reales, no solo playbooks declarativos.
- [ ] Todo cambio runtime tiene `dry-run` o validación previa equivalente.
- [ ] Existe validación estructural de contrato y detección de colisiones.
- [ ] Existe verificación post-cambio (`doctor`, `status --deep`, logs o prueba funcional).
- [ ] Los secretos nunca aparecen en outputs ni artefactos de staging.

## P1 — Necesario para assisted-prod

- [ ] Existe política explícita de restart por tipo de cambio.
- [ ] Hay fixtures/casos de prueba de `platform_contract`.
- [ ] Existe capacidad de patch incremental selectivo sobre config viva.
- [ ] El propio `clawforge` tiene perfil mínimo seguro de operación.
- [ ] Existen al menos 3 escenarios end-to-end probados.

## P2 — Endurecimiento adicional

- [ ] Hay métricas o reportes de drift recurrente.
- [ ] Existen reportes persistidos de promoción a producción.
- [ ] El backlog de endurecimiento se mantiene dentro del workspace como artefacto reutilizable.

# Dashboard PCA — Extensión C (Observabilidad Pasiva)

**Estado: INACTIVO**

---

## Cuándo Activar Esta Extensión

> **PCA v3.0 Principio P4**: "Start Simple, Scale Only When Needed"
> **Las extensiones se adoptan cuando el core falla, no antes.**

**Activar Extensión C si:**
- Drift recurrente (compromisos que se pudren sin darte cuenta)
- Compromisos mueren sin que lo notes
- El core lleva >4 semanas funcionando y hay señales de problema

**NO activar si:**
- El core aún no está estabilizado (Fases 1-4)
- No hay evidencia de drift
- El sistema funciona sin observabilidad explícita

---

## Contenido (cuando se active)

```
╔═══════════════════════════════════════════════╗
║  SALUD DEL SISTEMA                            ║
╠═══════════════════════════════════════════════╣
║  Compromisos activos: --                      ║
║  ├─ DEEP pendientes: --                       ║
║  ├─ SHALLOW pendientes: --                    ║
║  └─ SOCIAL pendientes: --                     ║
╠═══════════════════════════════════════════════╣
║  ALERTAS                                      ║
║  • Items en Waiting >5 días: --               ║
║  • Compromisos sin actividad >14 días: --     ║
║  • Bloques DEEP esta semana: --               ║
╠═══════════════════════════════════════════════╣
║  THROUGHPUT (últimas 2 semanas)               ║
║  • Compromisos completados: --                ║
║  • Compromisos añadidos: --                   ║
║  • Balance: --                                ║
╚═══════════════════════════════════════════════╝
```

## Métricas (referencia)

| Métrica | Rango Saludable | Señal de Problema |
|---------|-----------------|-------------------|
| Waiting >5 días | 0-2 | ≥3 |
| Sin actividad >14 días | 0-3 | ≥5 |
| Balance throughput | ≥0 | <0 por >4 semanas |
| Bloques DEEP/semana | ≥2 | 0-1 |

---

*Extensión C de PCA v3.0 — Activar solo si el core falla*

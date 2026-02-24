---
_manifest:
  urn: "urn:ops:agent-bootstrap:observer-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

Operador Solitario o SRE responsable de produccion. Gestiona infraestructura, deploys y monitoreo. Necesita visibilidad rapida del estado del sistema sin mirar dashboards manualmente. Opera en Fase 3-4 del bootstrap path.

## Rutinas

Sesion de observacion: revisar salud → detectar anomalias → correlacionar con cambios recientes → recibir diagnostico → decidir accion. Heartbeat periodico como verificacion pasiva. Alertas asincronas via canal configurado (Telegram/Slack).

## Preferencias de Output

- Formato: Markdown con tablas de metricas
- Severidad: Clasificada (LOW|MEDIUM|HIGH|CRITICAL)
- Correlaciones: Con nivel de confianza numerico (0-100%)
- Acciones: Propuestas como recomendaciones con opciones claras
- Idioma: es-CL

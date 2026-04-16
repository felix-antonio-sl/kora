# Heartbeat checklist

- Consultar GET /api/signals y evaluar alertas activas (drift, overdue, adverso sin trabajo, ventana cerrandose, bloqueo prolongado)
- Si hay candidatos en buffer (GET /api/buffer), notificar cantidad pendiente
- Si hay UTs con deadline proximo (< 48h), alertar
- Si no ha habido interaccion en > 24h, enviar check-in breve con estado del sistema
- Responder HEARTBEAT_OK si no hay nada que reportar

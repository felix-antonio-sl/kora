# HEARTBEAT

Checklist periódico. Ejecutar rápido, sin verbose.

## Pasos (tool calls reales)

```
1. memory_get("memory/gtd/INBOX.md")
2. memory_get("memory/gtd/WAITING.md")
3. gog gmail messages search "in:inbox is:unread" --account koraxfx@gmail.com --limit 5
4. gog calendar list --account koraxfx@gmail.com --limit 5
```

## Evaluar señales PCA

- Buffer INBOX: ¿>30 items? → alerta
- Waiting: ¿items >3 días? → alertar (INV-12)
- Días sin triaje: ¿≥3? → considerar protocolo abandono
- delegation_scope: ¿expirado (>7d)? → revocar y notificar

## Cuándo notificar (Telegram)

- Inbox GTD con items >24h sin procesar
- Email urgente no leído (remitente o asunto relevante)
- Evento calendario en <2h
- Waiting estancado >3 días
- Señales de colapso ≥3 (evaluar skill deteccion-colapso)
- Más de 48h sin mensaje directo de Korvo

## Cuándo callar

- Fuera de horario activo (23:00–08:00 Chile)
- Nada nuevo desde el último check
- Todo normal → `HEARTBEAT_OK`

## Actualizar estado al finalizar

```
memory_get("memory/heartbeat-state.json")
# editar con timestamp UTC actual
```

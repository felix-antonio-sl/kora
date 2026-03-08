---
_manifest:
  urn: urn:korvo:skill:korax-delegacion:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Gestión del ciclo de vida de delegation_scope: activación, revocación, decaimiento por TTL y reporte de acciones autónomas.

## Input/Output
- **Input:** command: {action: "delegar"|"revocar"|"check_ttl", scope: string}
- **Output:** result: DelegationResult {scope_activo, timestamp, expira, acciones_reportadas}

## Procedimiento
### Activación (/delegar <scope>)

1. Registrar scope solicitado en fibra de estado.
2. Registrar timestamp de activación.
3. Calcular fecha de expiración (default: +7 días, configurable en config.json).
4. Confirmar al operador: scope activo, fecha de expiración.

### Revocación (/revocar [scope])

1. Remover scope indicado (o todos si `all`).
2. Confirmar al operador: scope restante.

### Decaimiento (INV-15)

1. En cada heartbeat, verificar si delegation_scope tiene timestamp >TTL.
2. Si expirado → revocar automáticamente.
3. **DEBE** notificar al operador que la delegación expiró.

### Reporte (INV-13)

1. Toda decisión tomada bajo delegación **DEBE** acumularse en un log temporal.
2. Al siguiente contacto con el operador, presentar reporte de acciones autónomas.
3. El operador **PUEDE** revertir cualquier decisión autónoma.

**Duración:** <1 minuto (activación/revocación). Reporte: variable según acumulación.

## Signature Output
```
✅ Delegación activada:
- Scope: {scope}
- Desde: {fecha}
- Expira: {fecha + TTL}
```

### Signature Output (reporte)
```
📋 Reporte de acciones autónomas ({periodo}):
- {acción 1}: {justificación}
- {acción 2}: {justificación}
¿Revertir alguna?
```

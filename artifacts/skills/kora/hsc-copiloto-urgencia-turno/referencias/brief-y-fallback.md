# Brief y fallback

## Uso base

Invocar:

```bash
hsc-agent brief <rut|atencion_id>
```

Usar `--progress-stream` solo si el runtime muestra heartbeat en tiempo real.

## Lectura del envelope

### Si `ok:true`

Leer en este orden:

1. `patient`
2. `active_encounter`
3. `presenting`
4. `triage`
5. `vitals`
6. `orders.pending`
7. `lab_highlights`
8. `imaging_reports`
9. `medications_active`
10. `history`
11. `warnings`

### Si `ok:false`

No inventar datos.
Solo degradar segun el codigo:

- `patient_not_found` -> pedir verificar identificador
- `identity_mismatch` -> no confiar; pedir revision manual
- `upstream_unavailable` -> sistema no responde; reintentar luego
- `database_unavailable` -> problema tecnico del agente
- `hv2_binary_missing` -> configuracion rota
- `internal_error` -> error inesperado, mostrar detalle breve

## Warnings

`warnings` no son hallazgos clinicos.
Son flags de calidad de datos o de extraccion.

Si aparecen warnings de identidad o de descarte:

- declarar que parte de la informacion puede estar incompleta
- no rellenar huecos con inferencia libre

## Cuando el brief basta

El brief suele bastar para:

- orientarse rapido en un episodio DAU activo
- ver triage, presenting, vitales, pendientes y plan general
- decidir que area mirar despues

## Cuando el brief no basta

El brief no basta por si solo cuando:

- importa un valor exacto de laboratorio
- importa una tendencia fina de signos vitales
- importa una observacion de enfermeria o informe inline no bien resumido
- importa una contradiccion entre workflow y clinica
- hay warnings de identidad

## Regla operativa

El brief resume superficies primarias.
No las reemplaza.

Cuando haya duda clinicamente relevante, abrir la superficie primaria correcta.

## Fuentes de origen

Destilado desde:

- `/home/felix/projects/hsc/agent/docs/contracts/brief-agent-instructions-2026-04-17.md`
- `/home/felix/projects/hsc/agent/docs/deploy/openclaw-integration-2026-04-18.md`
- `/home/felix/projects/hsc/docs/go-live-checklist-urgent-agent-2026-04-19.md`

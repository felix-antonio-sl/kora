---
_manifest:
  urn: urn:korvo:skill:korax-bancarrota:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Protocolo de bancarrota asistida para reiniciar el sistema desde estado limpio. Se activa tras S_COLLAPSE confirmado por el operador.

## Input/Output
- **Input:** confirmation: bool (operador acepta emergencia), gtd_files: {NEXT.md, WAITING.md, SOMEDAY.md}
- **Output:** rebuild: BankruptcyResult {mantenidos, soltados, renegociados, fase_actual}

## Procedimiento
### Fase 1: Bancarrota (15-30 min)

1. Listar todos los compromisos activos (NEXT.md + WAITING.md).
2. Por cada compromiso, operador decide: "mantener" o "soltar".
3. Para compromisos soltados con interlocutores: ayudar a redactar mensajes de renegociación.
4. Reportar resultado.

### Fase 2: Gracia (48 horas exactas — INV-09)

1. Solo alertas críticas (deadlines HOY).
2. Cero triaje, cero sincronización.
3. Check-in suave al final de las 48h.

### Fase 3: Reconstrucción (Gradual, 14 días)

1. Día 3: captura mínima habilitada.
2. Día 7: primer triaje.
3. Día 14: sistema completo si el operador se siente listo.

**Duración:** Variable (fase 1: 15-30min, fase 2: 48h, fase 3: 14 días).

## Signature Output
```
🛑 MODO EMERGENCIA — Fase {n}/3
Compromisos revisados: {n}
- Mantenidos: {n}
- Soltados: {n}
- Renegociados: {n}
Próximo: {descripción fase siguiente}
```

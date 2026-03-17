---
_manifest:
  urn: urn:korvo:skill:cm-bancarrota:2.0.0
  type: lazy_load_endofunctor
---

## Proposito

Protocolo de bancarrota asistida sobre entidades PCA v4.1. Se activa tras S-COLLAPSE confirmado. Tres fases: bancarrota (revision de entidades), gracia (48h), reconstruccion gradual (14d). Aplica Polo B al descartar Proyectos.

## Input/Output

- **Input:** confirmacion del operador, entidades activas (UTs, Proyectos, Objetivos, Contribuciones)
- **Output:** BankruptcyResult { fase: 1|2|3, revisados: int, mantenidos: int, descartados: int, renegociados: int }

## Procedimiento

### Fase 1: Bancarrota (15-30 min)

1. Listar todas las entidades activas:
   - UTs pendientes y en_progreso
   - Proyectos activos
   - RESULTADOS con ventana_fin proxima
2. Por cada Proyecto, operador decide: "mantener" o "descartar".
   - Si descartar: aplicar Polo B (INV-13).
     - Reubicar o descartar UTs activas del Proyecto.
     - Marcar Contribuciones constitutivas como rotas.
     - Evaluar impacto en RESULTADO asociado.
3. Por cada UT suelta, operador decide: "mantener" o "descartar".
4. Para compromisos con interlocutores: ayudar a redactar mensajes de renegociacion.
5. Reportar resultado.

### Fase 2: Gracia (48 horas exactas — INV-08)

1. Solo alertas criticas (RESULTADO con ventana_fin HOY).
2. Cero triaje, cero sincronizacion.
3. Heartbeats se encolan (excepto collapse con >= 4 senales).
4. Check-in suave al final de las 48h.

### Fase 3: Reconstruccion (Gradual, 14 dias)

1. Dia 3: captura minima habilitada (CM-CAPTURA).
2. Dia 7: primer triaje (CM-TRIAJE).
3. Dia 14: sistema completo si el operador se siente listo.
4. Si el operador no esta listo al dia 14, extender gracia sin presion.

## Signature Output

```
🛑 MODO EMERGENCIA — Fase <n>/3

Entidades revisadas: <n>
- Proyectos mantenidos: <n> | descartados: <n>
- UTs mantenidas: <n> | descartadas: <n>
- Contribuciones rotas: <n>
- Renegociaciones: <n>

Proximo: <descripcion fase siguiente>
```

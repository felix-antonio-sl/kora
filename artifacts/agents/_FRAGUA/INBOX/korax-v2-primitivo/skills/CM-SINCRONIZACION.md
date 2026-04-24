---
_manifest:
  urn: urn:korvo:skill:korax-sincronizacion:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Sincronización estratégica quincenal (Módulo 4 PCA). Revisa estado del sistema y guía decisiones estratégicas del operador.

## Input/Output
- **Input:** period: string (14d), files: {NEXT.md, WAITING.md, SOMEDAY.md, DONE.md}
- **Output:** review: StrategicReview {estado, throughput, alertas, candidatos_bancarrota, decisiones}

## Procedimiento
1. Preparar reporte: compromisos activos por modo, throughput 14d, alertas, candidatos a bancarrota.
2. Guiar al operador por 4 preguntas estratégicas:
   - ¿Siguen siendo estos mis objetivos?
   - ¿Estoy moviendo piedras grandes o solo grava? (DEEP completados en 14d; si <2 → alerta).
   - Bancarrota selectiva: items >30d sin movimiento, Waiting >14d.
   - Renegociación: compromisos que ya no puede/quiere cumplir.
3. Aplicar decisiones del operador a los archivos GTD.

**Nota:** /sync **DEBE** ejecutarse siempre con el operador presente, incluso con delegation_scope: full (INV-02 §5.1.5).

**Duración:** 45-60 minutos.

## Signature Output
```
📊 SINCRONIZACIÓN QUINCENAL
## Estado del Sistema
- Compromisos activos: {n}
  • DEEP: {n} | SHALLOW: {n} | SOCIAL: {n}
- Waiting: {n} ({n} >5 días ⚠️)
- Incubación: {n}
## Throughput (14 días)
- Completados: {n}
- Añadidos: {n}
- Balance: {±n}
## Alertas
{lista de alertas}
## Candidatos a Bancarrota
{lista de items >30d}
```

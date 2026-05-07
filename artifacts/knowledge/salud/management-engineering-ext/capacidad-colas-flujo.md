---
_manifest:
  urn: urn:salud:kb:management-engineering-ext-capacidad
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Healthcare Management Engineering (Kolker 2012), Caps. 2-3. INBOX/salud/
  version: 1.0.0
version: 1.0.0
status: publicado
family: guide
tags:
- salud
- capacidad
- colas
- flujo
- urgencias
- uci
- quirofanos
- simulacion
lang: es
relations:
  cites:
  - urn:salud:kb:management-engineering-ext-indice
  - urn:salud:kb:gestion-redes-urgencias
  - urn:salud:kb:gestion-redes-unidades
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:management-engineering-ext-capacidad
---

# Capacidad, colas y flujo de pacientes

## Equilibrio oferta-demanda

El problema central de la gestion hospitalaria es dinamico: la demanda fluctua
mientras la oferta (camas, personal, quirofanos) es relativamente fija. Las
herramientas de management engineering cuantifican este desbalance.

## Teoria de colas aplicada

Parametros clave de un sistema de colas en salud:

- **λ (tasa de llegada)**: pacientes por unidad de tiempo
- **μ (tasa de servicio)**: pacientes atendidos por unidad de tiempo
- **ρ = λ/μ (intensidad de trafico)**: si ρ > 1, la cola crece indefinidamente
- **Wq (tiempo de espera en cola)**: tiempo hasta ser atendido
- **Lq (longitud de cola)**: numero promedio esperando

### Aplicaciones por unidad

**Urgencias**: el cuello de botella no es triaje sino la admision a cama.
El boarding (paciente admitido esperando cama) es la metrica critica.
Solucion: load-leveling de cirugias electivas para liberar camas en peaks.

**UCI**: sistema cerrado con tasa de rechazo. La ocupacion >85% correlaciona
con aumento de mortalidad. Las readmisiones a UCI en <48h son evento centinela.

**Quirofanos**: optimizar secuencia (duracion primero → corto primero),
reducir turnover time entre cirugias, bloqueo de horarios para urgencias.

## Simulacion de eventos discretos

Metodo para modelar sistemas complejos con interdependencias:
- Mapea el flujo completo: ED → UCI → piso → alta → post-agudo
- Permite probar escenarios "what-if" (agregar camas, cambiar staffing)
- Identifica cuellos de botella no obvios en la interdependencia de unidades

## Indicadores de capacidad operativa

| Indicador | Definicion | Benchmark |
|-----------|-----------|-----------|
| ALOS | Average Length of Stay | Variable por servicio |
| Occupancy rate | % camas ocupadas | <85% seguro, >90% critico |
| Boarding time | Tiempo en urgencias post-decision de ingreso | <4 horas |
| Left Without Being Seen | % pacientes que se van sin atencion | <2% |
| Turnover interval | Tiempo entre alta y nueva ocupacion | <2 horas |
| Readmision <30d | % reingresos no planificados | <15% |

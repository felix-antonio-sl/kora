---
_manifest:
  urn: "urn:pro:kb:gestion-redes-herramientas"
  provenance:
    created_by: "FS"
    created_at: "2026-03-03"
    source: "Síntesis multi-fuente: OPS, IHI, NICE, AHRQ, MINSAL, Cochrane, NotebookLM HaH"
version: "2.0.0"
status: draft
tags: [gestion-redes, kpi, bpmn, plantillas, fhir, simulacion, madurez, herramientas]
lang: es
---

# Gestión de Redes Asistenciales — Herramientas y Anexos

## Anexo A: Catálogo de KPI

### A.1 KPI de red general

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Continuidad contrarreferencia ≤7d | Contrarreferencias ≤7 días / Total derivaciones × 100 | ≥80 % | NHS 85 % | MINSAL 2019 | Mensual |
| Productividad ambulatoria | Consultas realizadas / Horas agenda disponible | ≥3.5/h | OCDE 4/h | OCDE 2023 | Mensual |
| No-show ambulatorio | Inasistencias / Citas agendadas × 100 | ≤10 % | 5-8 % IHI | IHI 2022 | Mensual |
| Reingreso 30d no planificado | Reingresos ≤30d / Egresos × 100 | ≤12 % | 8-11 % OCDE | OCDE 2023 | Mensual |
| Costo por caso ajustado (DRG) | Costo total / Egresos ponderados DRG | Tendencia ↓ | Mediana nacional | FONASA-IR-GRD | Trimestral |
| Espera mediana por especialidad | Mediana días desde derivación a primera atención | ≤30d | NHS RTT 18w | NHS England 2023 | Mensual |
| Cobertura efectiva | Población atendida / Población adscrita × 100 | ≥90 % | — | OPS 2020 | Anual |
| Satisfacción usuaria (PREMs) | Puntaje PREMs estandarizado | ≥80/100 | OCDE 82 | PREMs MINSAL | Semestral |
| Derivaciones con contrarreferencia | Contrarreferencias recibidas / Derivaciones enviadas × 100 | ≥80 % | — | MINSAL 2019 | Trimestral |
| Ocupación hospitalaria | Días-cama ocupados / Días-cama disponibles × 100 | 85-90 % | 85 % NICE | NICE 2022 | Diario |
| Promedio estancia (LOS ajustado) | Suma días estada / Egresos (ajuste case-mix) | Según GRD | OCDE 6.5d | OCDE 2023 | Mensual |
| % altas antes 12:00 h | Altas antes mediodía / Total altas × 100 | ≥33 % | IHI 40 % | IHI 2020 | Mensual |
| Cancelación quirúrgica | Cirugías canceladas / Cirugías programadas × 100 | ≤5 % | 2-5 % | AHRQ 2021 | Mensual |
| TMO contact center | Tiempo medio operación (seg) | ≤180 s | 120-150 s | — | Mensual |
| Resolución primer contacto | Consultas resueltas 1er contacto / Total consultas × 100 | ≥70 % | 72-80 % | — | Mensual |
| Cumplimiento GES/AUGE | Garantías cumplidas / Garantías activadas × 100 | 100 % | — | MINSAL-GES | Mensual |
| Adherencia guías clínicas | Auditorías conformes / Total auditorías × 100 | ≥85 % | — | AHRQ 2022 | Trimestral |
| NPS global red | Promotores − Detractores (escala −100 a +100) | ≥50 | — | — | Semestral |
| Incidentes seguridad reportados | N.° reportes / 1000 egresos | Tendencia ↑ (cultura reporte) | — | OMS 2021 | Mensual |
| % procesos con SOP vigente | SOPs actualizados / Total SOPs × 100 | ≥90 % | — | ISO 9001 | Trimestral |

### A.2 KPI de urgencias

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Door-to-triage | Tiempo arribo → clasificación (min) | ≤10 min | ACEP ≤5 min ESI-1 | ACEP 2023 | Continuo |
| Door-to-doctor | Tiempo arribo → evaluación médica (min) | ≤30 min | Median 28 min | ACEP 2023 | Continuo |
| LWBS (Left Without Being Seen) | Retiros sin atención / Consultas SUH × 100 | ≤2 % | 1-3 % | ACEP 2022 | Mensual |
| LOS SUH mediana | Mediana tiempo total en SUH (h) | ≤4 h | NHS 4h target | NHS 2023 | Mensual |
| LOS SUH p90 | Percentil 90 tiempo total en SUH (h) | ≤6 h | — | NICE 2022 | Mensual |
| Boarding time | Tiempo decisión admisión → salida de SUH (h) | ≤2 h | TJC ≤4h | TJC 2022 | Diario |
| Retorno 72h SUH | Reconsultas ≤72h / Egresos SUH × 100 | ≤3 % | 2-4 % | AHRQ 2021 | Mensual |
| Sepsis: antibiótico <1h | AB administrado ≤1h detección sepsis / Casos sepsis × 100 | ≥90 % | SSC ≥95 % | SSC 2021 | Mensual |
| Door-to-ECG en IAM | Tiempo arribo → ECG (min) | ≤10 min | AHA ≤10 min | AHA 2023 | Continuo |
| FMC-to-balloon (ICP) | Primer contacto médico → balón (min) | ≤90 min | ESC ≤90 min | ESC 2023 | Mensual |
| Door-to-needle ACV | Arribo → trombolisis (min) | ≤60 min | AHA ≤45 min | AHA 2022 | Mensual |
| Door-in-door-out (DIDO) | Arribo centro derivador → salida a ICP (min) | ≤30 min | AHA ≤30 min | AHA 2023 | Mensual |
| ROSC sostenido PCR | Retorno circulación espontánea ≥20min / PCR atendidos × 100 | ≥30 % | 25-35 % | AHA-Utstein 2023 | Mensual |
| Activación trauma team | Tiempo activación protocolo trauma (min) | ≤15 min | ATLS <15 min | ATLS 2022 | Continuo |
| Tiempo despacho EMS | Recepción llamada → despacho (min) | ≤2 min | NFPA ≤60s | NFPA 2021 | Continuo |
| Tiempo respuesta EMS p90 | Recepción llamada → escena p90 (min) | ≤8 min urbano | NFPA 8 min | NFPA 2021 | Mensual |
| Tasa sobre/infra-triaje | Discordancia triaje vs severidad real / Total triajes × 100 | ≤5 % combinado | — | ACEP 2022 | Trimestral |
| Analgesia oportuna <30min | Analgesia administrada ≤30min / Pacientes con dolor × 100 | ≥80 % | 75-85 % | AHRQ 2022 | Mensual |
| Caídas/1000 visitas SUH | Eventos caída × 1000 / Visitas SUH | ≤1.0 | 0.5-1.5 | AHRQ 2021 | Mensual |
| EAM en SUH | Eventos adversos medicamentos SUH × 1000 / Visitas | ≤2.0 | — | ISMP 2022 | Mensual |
| PREMs urgencias | Puntaje PREMs específico urgencias | ≥70/100 | — | MINSAL | Semestral |

### A.3 KPI de salud mental

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Cobertura efectiva SM | Población con trastorno atendida / Prevalencia estimada × 100 | ≥50 % | OMS 40-60 % | OMS-mhGAP 2022 | Anual |
| Retención ≥4 atenciones 90d | Usuarios con ≥4 contactos en 90d / Ingresos × 100 | ≥70 % | — | NICE 2023 | Trimestral |
| Seguimiento post-alta <7d | Contacto ≤7d post-egreso / Egresos SM × 100 | ≥80 % | HEDIS 60 % | HEDIS 2023 | Mensual |
| Eventos críticos/1000 usuarios | (Suicidio + intento + agresión grave) × 1000 / Usuarios activos | Tendencia ↓ | — | OMS 2021 | Trimestral |
| Cambio clínico PHQ-9 ≥5 pts | Usuarios con reducción PHQ-9 ≥5 / Usuarios con PHQ-9 basal × 100 | ≥50 % | IAPT 50 % recovery | IAPT/NHS 2023 | Trimestral |
| Espera primera atención SM | Mediana días desde derivación a 1ra atención SM | ≤15d | NHS 28d | NHS 2023 | Mensual |
| Abandonos de tratamiento | Abandonos / Usuarios activos × 100 | ≤20 % | 15-25 % | — | Trimestral |
| Contenciones/1000 días-cama | Episodios contención × 1000 / Días-cama SM | Tendencia ↓ cero | — | Safewards 2022 | Mensual |
| Contacto post-alta suicidio <72h | Contacto ≤72h post-alta riesgo suicida / Egresos riesgo suicida × 100 | 100 % | NICE 100 % | NICE 2023 | Mensual |
| Reintentos suicidio 30d | Reintentos ≤30d / Altas post-intento × 100 | Tendencia ↓ | — | OMS 2021 | Mensual |
| PREMs salud mental | Puntaje PREMs específico SM | ≥75/100 | — | MINSAL | Semestral |
| HoNOS cambio promedio | Δ HoNOS ingreso-egreso promedio | ≥4 pts | NHS ≥4 | NHS-MHSDS 2023 | Trimestral |
| PCI vigentes (%) | Planes cuidado integral actualizados / Usuarios activos × 100 | ≥90 % | — | NICE 2022 | Mensual |
| Crisis resueltas in situ por EMC | Crisis resueltas sin traslado / Total activaciones EMC × 100 | ≥60 % | 50-70 % | — | Mensual |
| Readmisión psiquiátrica 30d | Reingresos ≤30d / Egresos SM × 100 | ≤15 % | 10-18 % | AHRQ 2022 | Mensual |

### A.4 KPI de hospitalización domiciliaria

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa escalamiento (retorno hospital) | Retornos hospitalarios / Admisiones HaH × 100 | ≤10 % | 7-10 % | Levine 2020 | Mensual |
| Readmisión 30d HaH | Reingresos ≤30d post-egreso HaH / Egresos HaH × 100 | ≤8.6 % | 7-8.6 % | Federman 2018 | Mensual |
| Costo por episodio HaH | Costo total episodio HaH / Costo DRG equivalente × 100 | 62-81 % | 19-38 % menor | Levine 2020 | Mensual |
| LOS equivalente HaH | Promedio días en programa HaH | ≤3.2d | 3.0-3.5d | Shepperd 2021 | Mensual |
| Door-to-home | Tiempo decisión admisión HaH → instalación domicilio (h) | ≤6 h | — | — | Continuo |
| Cumplimiento visitas HaH | Visitas realizadas / Visitas programadas × 100 | ≥95 % | — | — | Semanal |
| Tiempo respuesta deterioro | Tiempo detección alerta RPM → evaluación presencial (min) | ≤60 min | — | — | Continuo |
| PREMs HaH | Puntaje PREMs hospitalización domiciliaria | ≥85/100 | — | Shepperd 2021 | Trimestral |
| IAAS domiciliarias/1000 días | Infecciones asociadas × 1000 / Días-estada HaH | ≈0 | <0.5 | — | Mensual |
| Satisfacción cuidador (Zarit) | Puntaje Zarit Burden Interview | ≤40 (sin sobrecarga) | — | Zarit 1980 | Trimestral |

### A.5 KPI transversales

| Indicador | Fórmula | Meta | Benchmark | Fuente | Periodicidad |
|-----------|---------|------|-----------|--------|-------------|
| Tasa eventos adversos | EA / 1000 egresos | Tendencia ↓ | — | OMS 2021 | Trimestral |
| IAAS global | IAAS / 1000 días-cama | ≤3.5 | 2-5 ECDC | ECDC 2022 | Mensual |
| EAM/1000 días-cama | Eventos adversos medicamentos × 1000 / Días-cama | ≤5.0 | — | ISMP 2022 | Mensual |
| Cumplimiento hand hygiene | Observaciones conformes / Total observaciones × 100 | ≥80 % | OMS ≥80 % | OMS 2022 | Mensual |
| Uptime HCE | Horas disponibilidad / Horas totales × 100 | ≥99.5 % | 99.9 % tier-3 | — | Mensual |
| Mensajes FHIR conformes | Mensajes válidos / Total mensajes × 100 | ≥98 % | — | HL7 FHIR R4 | Mensual |
| Horas formación per cápita | Horas capacitación / Dotación (FTE) | ≥40 h/año | — | OIT 2022 | Anual |
| Rotación personal | Desvinculaciones / Dotación promedio × 100 | ≤15 % | 10-18 % salud | — | Anual |
| Ausentismo | Días ausencia / Días programados × 100 | ≤5 % | 3-6 % | — | Mensual |
| % staff certificado | Personal con certificación vigente / Total × 100 | ≥90 % | — | — | Anual |
| Cumplimiento presupuestario | Ejecución presupuestaria / Presupuesto asignado × 100 | 95-100 % | — | DIPRES | Trimestral |
| Costo por caso DRG | Costo real / Costo esperado DRG | ≤1.0 | — | FONASA IR-GRD | Mensual |
| NPS interno | Promotores − Detractores staff (−100 a +100) | ≥30 | — | — | Anual |
| Adopción de mejoras (stick rate) | Mejoras sostenidas ≥6m / Total mejoras implementadas × 100 | ≥70 % | IHI 60-70 % | IHI 2022 | Semestral |
| Beneficios capturados vs prometidos | Beneficios realizados / Beneficios proyectados × 100 | ≥80 % | — | PMI 2021 | Semestral |

---

## Anexo B: Mapas de procesos (BPMN textual)

Notación: `**[ROL]** Acción → Decisión? {Sí: ruta / No: ruta} → Siguiente`

### B.1 Flujo SUH completo

```
**[EMS]** Pre-notificación (radio/MPDS) → Transmite datos: mecanismo, signos vitales, ETA
    → Código activación? {Trauma/ACV/IAM: activa equipo receptor / Estándar: continúa}

**[TRIAJE]** Recepción paciente → Registro administrativo (≤2 min)
    → Clasificación ESI (≤10 min arribo)
    → ESI-1/2? {Sí: circuito crítico / No: circuito general}

**[MÉDICO SUH]** Evaluación médica (≤30 min door-to-doctor)
    → Solicita exámenes? {Sí: orden apoyo diagnóstico / No: diagnóstico clínico}
    → Protocolo tiempo-dependiente? {IAM: ECG ≤10min, ICP ≤90min / ACV: TC ≤25min, TNK ≤60min / Sepsis: AB ≤1h}

**[APOYO DIAGNÓSTICO]** Procesamiento lab/imagen
    → Resultados críticos? {Sí: notificación activa ≤15min / No: resultado a HCE}

**[MÉDICO SUH]** Integración resultados → Diagnóstico
    → Requiere interconsulta? {Sí: solicitud / No: plan tratamiento}

**[ESPECIALISTA]** Evaluación interconsulta (≤60 min ESI-2, ≤4h ESI-3)
    → Asume manejo? {Sí: traslado a servicio / No: recomendaciones a SUH}

**[BED MANAGEMENT]** Gestión destino
    → ¿Observación/UOCS? {Sí: ingreso observación ≤24h / No: continúa}
    → Decisión destino: Alta SUH? {Sí: alta + contrarreferencia APS /
        Hospitalización? {Sí: cama asignada ≤2h boarding /
        Traslado? {Sí: coordinación SAMU + centro receptor}}}

**[MÉDICO SUH]** Documentación cierre → Indicaciones alta / ingreso → Fin
```

### B.2 Referencia / contrarreferencia

```
**[APS]** Detección necesidad derivación → Evaluación criterios referencia
    → Cumple criterios? {No: manejo APS / Sí: genera eReferral (FHIR ServiceRequest)}

**[CENTRO COORDINACIÓN]** Recepción eReferral → Validación pertinencia (≤48h)
    → Pertinente? {No: rechaza + feedback a APS / Sí: priorización clínica}
    → Asignación especialidad + agendamiento → Notificación a paciente

**[ESPECIALIDAD]** Atención especialista → Diagnóstico/plan terapéutico
    → Requiere seguimiento especialidad? {Sí: agenda control / No: contrarreferencia}

**[ESPECIALIDAD]** Genera contrarreferencia (≤7d) → FHIR DiagnosticReport + CarePlan
    → Envío a centro coordinación

**[CENTRO COORDINACIÓN]** Distribución contrarreferencia a APS origen

**[APS]** Recepción contrarreferencia → Actualización plan de cuidado
    → Seguimiento según indicaciones → Fin ciclo
```

### B.3 Alta segura

```
**[MÉDICO TRATANTE]** Decisión de alta (criterios clínicos cumplidos)
    → Redacción epicrisis + diagnósticos CIE-10
    → Indicaciones ambulatorias (medicamentos, controles, alertas)

**[FARMACIA]** Conciliación medicamentosa → Diferencias detectadas?
    {Sí: revisión con médico tratante / No: preparación recetas}
    → Dispensación medicamentos al alta

**[ENFERMERÍA]** Educación al paciente/cuidador (método teach-back)
    → Comprensión verificada? {No: repite educación / Sí: firma consentimiento}
    → Entrega carta de alta + material educativo

**[TRABAJO SOCIAL]** Evaluación necesidades sociales
    → Requiere apoyo? {Sí: coordinación red social / No: continúa}
    → Gestión transporte si necesario

**[MÉDICO TRATANTE]** Genera eReferral a APS (FHIR ServiceRequest + CarePlan)
    → Agenda control si requerido

**[APS]** Recepción notificación alta → Contacto paciente 48-72h
    → Visita domiciliaria si alto riesgo → Seguimiento activo → Fin
```

### B.4 Crisis de salud mental

```
**[COMUNIDAD/APS]** Detección crisis (auto-reporte, familia, APS, policía)
    → Activación EMC (equipo móvil de crisis)

**[EMC]** Desplazamiento al lugar → Evaluación inicial seguridad escena
    → Evaluación riesgo suicida/heteroagresión (Columbia/SAD PERSONS)
    → Riesgo inminente? {No: intervención in situ (contención verbal, plan de seguridad) /
        Sí: ¿Acepta traslado voluntario? {Sí: traslado asistido / No: evaluación involuntaria según Ley 20.584}}

**[EMC]** Resolución in situ? {Sí: plan de seguimiento <72h → notificación APS → Fin /
    No: traslado a SUH}

**[SUH]** Recepción → Triaje psiquiátrico → Estabilización médica
    → Requiere hospitalización SM? {No: alta + plan crisis + seguimiento EMC /
        Sí: solicitud cama unidad SM}

**[UNIDAD SM]** Ingreso → Evaluación psiquiátrica integral (≤24h)
    → Estabilización farmacológica + psicoterapéutica
    → Plan de cuidado integral (PCI) → Preparación egreso

**[UNIDAD SM]** Egreso → Contacto post-alta ≤72h (si riesgo suicida: obligatorio)
    → Derivación a programa ambulatorio SM → Seguimiento APS → Fin
```

### B.5 Admisión hospitalización domiciliaria (HaH)

```
**[SUH/APS]** Identificación candidato HaH → Screening elegibilidad
    → Cumple criterios clínicos? {No: manejo convencional / Sí: continúa}
    → Cumple criterios domiciliarios? {No: manejo convencional / Sí: continúa}

**[EQUIPO HaH]** Evaluación presencial → Consentimiento informado paciente/cuidador
    → Acepta? {No: manejo convencional / Sí: ingreso HaH}

**[LOGÍSTICA]** Setup domiciliario: equipamiento, medicamentos, conectividad RPM
    → Instalación dispositivos monitoreo (SpO2, PA, T°, FC)
    → Verificación conectividad → Prueba alarmas

**[CENTRO COMANDO]** Ingreso en sistema → Asignación equipo tratante
    → Configuración alertas RPM → Monitoreo 24/7

**[EQUIPO HaH]** Visitas programadas (médico + enfermería)
    → Tratamiento según protocolo (EV, O2, kinesioterapia)
    → Alerta RPM deterioro? {Sí: evaluación remota → ¿Escalamiento?
        {Sí: retorno hospital (SAMU) / No: ajuste tratamiento} /
        No: continúa protocolo}

**[EQUIPO HaH]** Criterios egreso cumplidos → Egreso HaH
    → Transición: eReferral a APS destino + plan seguimiento

**[APS DESTINO]** Contacto post-egreso 48-72h → Seguimiento ambulatorio → Fin
```

---

## Anexo C: Plantillas operativas

### C.1 SLA inter-nodos

**SLA 1: Derivación ACV a centro de trombectomía**

```yaml
sla:
  nombre: "Derivación ACV isquémico a centro trombectomía"
  versión: "1.0"
  nodo_origen: "SUH hospital primario"
  nodo_destino: "Centro neurovascular (trombectomía)"
  condición_activación: "ACV isquémico con oclusión gran vaso confirmada (CTA/MRA)"
  métricas:
    - indicador: "Door-in-door-out (DIDO)"
      meta: "≤30 min"
      escalamiento: "≥45 min → alerta jefe turno"
    - indicador: "Onset-to-puncture"
      meta: "≤180 min"
      escalamiento: "≥240 min → revisión proceso"
    - indicador: "Notificación pre-arribo"
      meta: "≥15 min antes llegada"
      escalamiento: "Incumplimiento → reporte incidente"
  responsabilidades:
    origen:
      - "TC/CTA completado antes de traslado"
      - "Trombolisis EV iniciada si indicada (no retrasa traslado)"
      - "Comunicación SBAR al centro receptor"
    destino:
      - "Equipo neurovascular activado pre-arribo"
      - "Sala angiografía disponible"
      - "Retroalimentación resultado ≤24h"
  penalización: "Incumplimiento reiterado (≥3/mes) → auditoría conjunta obligatoria"
  revisión: "Trimestral"
```

**SLA 2: HaH respuesta ante deterioro**

```yaml
sla:
  nombre: "Respuesta ante deterioro clínico HaH"
  versión: "1.0"
  nodo_origen: "Centro comando HaH"
  nodo_destino: "SAMU / SUH referencia"
  condición_activación: "Alerta RPM: SpO2 <90%, FC >120 o <50, PAS <90, T° >39°C; o deterioro clínico evaluado por enfermería remota"
  métricas:
    - indicador: "Tiempo detección → contacto enfermería"
      meta: "≤5 min"
      escalamiento: "≥10 min → alerta supervisor"
    - indicador: "Evaluación remota → decisión escalamiento"
      meta: "≤15 min"
      escalamiento: "≥30 min → reporte incidente"
    - indicador: "Decisión → llegada SAMU a domicilio"
      meta: "≤20 min urbano"
      escalamiento: "≥30 min → coordinación directa con SAMU"
  responsabilidades:
    centro_comando:
      - "Monitoreo 24/7 alertas RPM"
      - "Contacto telefónico/video inmediato con paciente"
      - "Activación SAMU si criterios escalamiento"
    samu:
      - "Priorización despacho (código HaH)"
      - "Traslado a SUH de referencia (no al más cercano)"
    suh_referencia:
      - "Acceso a registro HaH del paciente"
      - "Cama priorizada si requiere hospitalización"
  penalización: "Tiempo respuesta >60 min → auditoría obligatoria + reporte SEREMI"
  revisión: "Mensual"
```

**SLA 3: Derivación crisis SM a unidad psiquiátrica**

```yaml
sla:
  nombre: "Derivación crisis salud mental a unidad psiquiátrica"
  versión: "1.0"
  nodo_origen: "SUH / EMC (equipo móvil crisis)"
  nodo_destino: "Unidad corta estadía psiquiátrica"
  condición_activación: "Riesgo suicida alto (Columbia ≥4) o psicosis aguda con riesgo heteroagresión, sin respuesta a intervención en crisis"
  métricas:
    - indicador: "Evaluación psiquiátrica en SUH"
      meta: "≤60 min desde solicitud"
      escalamiento: "≥90 min → alerta jefe servicio SM"
    - indicador: "Asignación cama unidad SM"
      meta: "≤4 h desde decisión hospitalización"
      escalamiento: "≥6 h → escalamiento a dirección"
    - indicador: "Contacto post-alta (riesgo suicida)"
      meta: "≤72 h"
      escalamiento: "Incumplimiento → reporte crítico"
  responsabilidades:
    suh_emc:
      - "Estabilización médica completada"
      - "Evaluación riesgo estandarizada (Columbia/SAD PERSONS)"
      - "Contención farmacológica según protocolo si necesaria"
      - "Comunicación SBAR a unidad SM"
    unidad_sm:
      - "Cama disponible o plan contingencia activado"
      - "Evaluación integral ≤24h post-ingreso"
      - "Plan de cuidado integral (PCI) ≤48h"
      - "Planificación egreso desde ingreso"
  penalización: "Boarding psiquiátrico >12h → reporte a SEREMI + auditoría red"
  revisión: "Trimestral"
```

### C.2 Matriz RACI

| Actividad | Dir. Servicio | Dir. Hospital | Jefe Unidad | Médico tratante | Enfermería | TI | Farmacia | Calidad | Trabajo social | SAMU | APS |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Gobernanza de red | A | R | I | I | I | I | I | C | I | I | C |
| Gestión de camas | I | A | R | C | R | C | I | I | I | I | I |
| Triaje SUH | I | I | A | R | R | I | I | C | I | C | I |
| Conciliación medicamentosa | I | I | C | R | C | I | A | C | I | I | I |
| Alta segura | I | I | A | R | R | I | C | C | R | I | I |
| eReferral / contrarreferencia | C | A | R | R | C | R | I | I | I | I | R |
| Monitoreo KPI | A | R | R | I | I | R | I | A | I | I | C |
| Respuesta ante desastre/MCI | A | R | R | R | R | C | R | C | R | R | C |
| Admisión HaH | I | A | R | R | R | R | R | C | C | C | C |
| Gestión crisis SM | I | A | R | R | R | I | C | C | R | R | C |
| Interoperabilidad FHIR | C | A | I | I | I | R | I | I | I | I | I |
| Mejora continua (PDSA) | I | A | R | C | C | C | C | R | C | I | C |

Leyenda: **R** = Responsable, **A** = Aprobador, **C** = Consultado, **I** = Informado.

### C.3 Checklist apertura de servicios

**Legal/regulatorio:**
- [ ] Resolución sanitaria SEREMI vigente
- [ ] Autorización Superintendencia de Salud (si aplica)
- [ ] Convenios interinstitucionales firmados

**Dotación:**
- [ ] Dotación mínima definida según normativa (médicos, enfermeras, TENS, administrativos)
- [ ] Credenciales profesionales verificadas (SIS/Registro Nacional)
- [ ] Plan de turnos y contingencia aprobado

**Equipamiento:**
- [ ] Equipamiento biomédico adquirido e instalado
- [ ] Calibración y certificación de equipos críticos
- [ ] Stock de insumos y medicamentos según listado mínimo
- [ ] Cadena de frío verificada (si aplica)

**Sistemas:**
- [ ] HCE operativa y conectada a red
- [ ] Interfaces FHIR configuradas y probadas
- [ ] Sistema de turnos/agenda en producción
- [ ] RPM operativo (si HaH)

**Seguridad:**
- [ ] Plan de emergencia y evacuación aprobado
- [ ] Protocolos de seguridad del paciente implementados
- [ ] Sistema de reporte de incidentes activo
- [ ] Simulacro de contingencia realizado

### C.4 Estructura SOP/WI

```yaml
sop:
  código: "SOP-SUH-001"
  título: "Protocolo de triaje ESI en Servicio de Urgencia Hospitalario"
  versión: "1.0"
  fecha_vigencia: "2026-03-01"
  próxima_revisión: "2027-03-01"
  propietario: "Jefatura SUH"
  aprobado_por: "Dirección médica"
  objetivo: "Estandarizar clasificación de urgencia mediante ESI 5 niveles para asegurar atención oportuna según severidad"
  alcance: "Todos los pacientes que consultan en SUH, incluyendo derivaciones EMS"
  definiciones:
    - "ESI: Emergency Severity Index (5 niveles)"
    - "Door-to-triage: tiempo desde arribo administrativo a clasificación"
  responsabilidades:
    enfermera_triaje: "Clasificación ESI, registro en HCE, activación códigos"
    médico_jefe_turno: "Supervisión, resolución discrepancias, re-triaje"
  procedimiento:
    - paso: 1
      acción: "Recepción del paciente en módulo triaje"
      responsable: "TENS admisión"
      tiempo: "≤2 min"
    - paso: 2
      acción: "Evaluación triaje ESI: aspecto general, signos vitales, motivo consulta"
      responsable: "Enfermera triaje"
      tiempo: "≤5 min"
    - paso: 3
      acción: "Asignación nivel ESI y circuito (crítico/general/fast-track)"
      responsable: "Enfermera triaje"
      tiempo: "Inmediato"
    - paso: 4
      acción: "Registro en HCE + notificación a circuito asignado"
      responsable: "Enfermera triaje"
      tiempo: "≤1 min"
  documentos_asociados:
    - "Algoritmo ESI v4 (Gilboy et al. 2020)"
    - "Protocolo activación código ACV/IAM/Trauma"
  indicadores:
    - "Door-to-triage ≤10 min (meta)"
    - "Tasa sobre/infra-triaje ≤5 %"
  registros: "HCE módulo triaje, libro de novedades turno"
  control_cambios:
    - versión: "1.0"
      fecha: "2026-03-01"
      cambio: "Creación inicial"
      autor: "Jefatura SUH"
```

---

## Anexo D: Salud digital

### D.1 Perfiles FHIR recomendados

| Recurso FHIR | Uso clínico | Perfil / Extensión |
|---------------|-------------|-------------------|
| Patient | Identificación demográfica, RUT, previsión | CL Core Patient (MINSAL) |
| Encounter | Registro atención (ambulatoria, urgencia, hospitalización, HaH) | CL Core Encounter + extensión tipo HaH |
| EpisodeOfCare | Seguimiento longitudinal de episodio (SM, HaH, crónico) | Base R4 + extensión estado red |
| ServiceRequest | eReferral, interconsulta, solicitud exámenes | CL Core ServiceRequest |
| Condition | Diagnósticos CIE-10, problemas activos | CL Core Condition |
| Observation | Signos vitales, RPM, escalas clínicas (PHQ-9, HoNOS, ESI) | Vital Signs Profile R4 + extensión escalas |
| MedicationRequest | Prescripción, conciliación medicamentosa | CL Core MedicationRequest |
| DiagnosticReport | Resultados laboratorio, imagenología | CL Core DiagnosticReport |
| CarePlan | Plan de cuidado integral (PCI), plan de alta, plan de crisis SM | Base R4 + extensión multidisciplinario |

### D.2 Patrón de integración

**Arquitectura**: Event-driven (EDA) con bus de eventos clínicos.

```
Evento clínico (HCE) → Broker mensajería (HL7 FHIR Subscription / Kafka)
    → Cola por tipo: admisión | alta | resultado_crítico | alerta_RPM | derivación
    → Consumidores:
        - Bed management (admisión/alta)
        - Centro coordinación (derivaciones)
        - Centro comando HaH (alertas RPM)
        - Dashboard KPI (todos)
        - Notificaciones paciente (alta, citas)
```

**Principios**:
- Eventos inmutables, idempotentes
- Retry con backoff exponencial (máx 3 reintentos)
- Dead-letter queue para eventos fallidos
- Trazabilidad end-to-end (correlation ID)
- Conformidad HL7 FHIR R4 ≥98 %

### D.3 Terminologías

| Dominio | Estándar | Ejemplo |
|---------|----------|---------|
| Diagnósticos | ICD-10 (CIE-10 adaptación chilena) | J18.9 Neumonía no especificada |
| Procedimientos | ICD-10-PCS / FONASA | 0BJ08ZZ Inspección pulmón |
| Hallazgos clínicos | SNOMED CT | 386661006 Fiebre |
| Laboratorio | LOINC | 2160-0 Creatinina sérica |
| Medicamentos | ATC / Vademécum ISP | N05AH03 Olanzapina |

### D.4 Ciberseguridad: checklist mínimo

1. **MFA obligatorio** para acceso a HCE y sistemas críticos
2. **Cifrado en tránsito** (TLS 1.3) y en reposo (AES-256) para datos clínicos
3. **Segmentación de red**: red clínica aislada de red administrativa y guest
4. **Backups automáticos**: RPO ≤1h, RTO ≤4h para HCE; prueba restauración trimestral
5. **Gestión de parches**: vulnerabilidades críticas parcheadas ≤72h; programadas ≤30d
6. **Control de acceso RBAC**: perfiles por rol, revisión trimestral de privilegios
7. **Auditoría de accesos**: logs inmutables ≥12 meses; alertas acceso anómalo
8. **DRP (Disaster Recovery Plan)**: documentado, probado semestralmente, RTO validado
9. **Capacitación seguridad**: phishing simulado trimestral; formación anual obligatoria
10. **Gestión de dispositivos médicos IoT/RPM**: inventario, firmware actualizado, red dedicada, monitoreo tráfico anómalo

---

## Anexo E: Simulación y analítica

### E.1 Modelado de demanda y colas

**Modelo base**: M/M/s (Erlang-C) para dimensionamiento de boxes y dotación.

| Parámetro | Símbolo | Descripción |
|-----------|---------|-------------|
| Tasa de llegada | λ | Pacientes/hora (por segmento ESI) |
| Tasa de servicio | μ | Pacientes atendidos/hora por servidor |
| Servidores | s | Boxes o profesionales disponibles |
| Intensidad de tráfico | ρ = λ/(s·μ) | Utilización; **mantener ρ < 0.85** |

**Fórmulas clave**:
- Probabilidad de espera (Erlang-C): P(espera) = C(s, λ/μ)
- Tiempo medio en cola: Wq = C(s, λ/μ) / (s·μ − λ)
- Tiempo medio en sistema: W = Wq + 1/μ

**Regla operativa**: si ρ ≥ 0.85 → activar plan de contingencia (apertura box adicional, redirección, fast-track).

### E.2 Simulación SUH

| Escenario | λ base | Δ λ | s disponible | ρ esperado | Acción |
|-----------|--------|-----|-------------|------------|--------|
| Operación normal (lunes AM) | 8 pac/h | — | 6 boxes | 0.67 | Estándar |
| Peak estacional (invierno IRA) | 8 pac/h | +40 % | 6 boxes | 0.93 | Apertura 2 boxes + fast-track respiratorio |
| Cierre 2 boxes mantención | 8 pac/h | — | 4 boxes | 1.00 | Desvío ESI-4/5 a SAPU + refuerzo turnos |
| MCI (incidente masivo) | — | +200 % puntual | 6+4 contingencia | Variable | Activación plan MCI, triaje START, cancelación electiva |
| Pandemia (surge capacity) | 8 pac/h | +80 % sostenido | 6+6 reconversión | 0.87 | Reconversión áreas, cohorting, telemedicina pre-SUH |

### E.3 Estratificación de riesgo en salud mental

**Variables de estratificación**:

| Variable | Fuente | Peso relativo |
|----------|--------|---------------|
| Intentos suicidio previos | HCE | Alto |
| Puntaje Columbia Suicide Severity (C-SSRS) | Evaluación | Alto |
| Hospitalización psiquiátrica ≤12m | HCE | Medio-alto |
| Comorbilidad TUS activa | HCE | Medio-alto |
| Aislamiento social / sin red apoyo | Evaluación social | Medio |
| Abandono tratamiento previo | HCE | Medio |
| Edad 15-24 o >65 | Demográfico | Medio |
| Evento vital reciente (duelo, desempleo) | Evaluación | Bajo-medio |
| PHQ-9 ≥20 (depresión severa) | Escala | Medio |
| Acceso a medios letales | Evaluación | Alto |

**Modelo de priorización**:

| Nivel riesgo | Criterio | Acción |
|--------------|----------|--------|
| Crítico | C-SSRS ≥4 o intento activo | EMC inmediato; hospitalización; contacto ≤24h post-alta |
| Alto | C-SSRS 3 + factores agravantes | Evaluación psiquiátrica ≤24h; seguimiento semanal |
| Moderado | PHQ-9 ≥15 o TUS activo sin red apoyo | Atención SM ≤7d; plan de cuidado integral |
| Bajo | PHQ-9 10-14, red apoyo presente | Atención SM ≤15d; seguimiento APS |
| Mínimo | PHQ-9 <10, estable | Control APS habitual |

---

## Anexo F: Infraestructura y diseño funcional

### F.1 Criterios de superficie y flujo

| Unidad | Superficie mínima | Flujos diferenciados | Requisitos especiales |
|--------|-------------------|---------------------|----------------------|
| SUH (boxes) | 12 m² por box; triaje 15 m² | Limpio/sucio; ambulante/camilla; crítico/general | Presión negativa sala aislamiento; acceso directo ambulancia; señalización por código color |
| Reanimación | 25 m² por puesto | Acceso 360° camilla; circuito directo desde triaje | Gases medicinales (O2, aire, vacío); tomas eléctricas ≥16 por puesto; iluminación ≥500 lux |
| Observación/UOCS | 8-10 m² por puesto | Separación por sexo; circuito corto a imagenología | Monitoreo centralizado; llamado enfermería |
| Unidad SM agudos | 12 m² habitación individual; salón grupal 40 m² | Ingreso controlado; zonas seguras; patio terapéutico | Anti-ligadura (sin puntos de anclaje); visibilidad enfermería; materiales irrompibles |
| HaH (domicilio) | N/A (domicilio paciente) | Zona paciente delimitada; almacenamiento insumos | Conectividad internet ≥10 Mbps; tomacorriente junto a cama; acceso para equipo clínico |

### F.2 Señalética y accesibilidad

- Señalización bilingüe (español + mapudungun en zona pertinente) y pictográfica universal
- Código color por servicio: rojo (urgencias), azul (hospitalización), verde (ambulatorio), morado (SM)
- Wayfinding digital (pantallas) + físico (piso, paredes)
- Accesibilidad universal: rampas ≤8 %, ascensores camilleros, baños adaptados, señalización Braille
- Cumplimiento OGUC (Ordenanza General de Urbanismo y Construcciones) + Ley 20.422

### F.3 Biocontención y decontaminación

- Sala aislamiento presión negativa: ≥12 recambios aire/hora, presión diferencial −2.5 Pa
- Antesala con lavamanos quirúrgico y EPP
- Zona decontaminación (MCI HAZMAT): exterior SUH, drenaje independiente, duchas
- Protocolo donning/doffing señalizado con mirror check
- Gestión REAS (residuos establecimientos asistenciales) según DS 6/2009

---

## Anexo G: Cadena de suministro

### G.1 Listados mínimos por dispositivo

**SUH / EMS:**

| Categoría | Dispositivos / insumos |
|-----------|----------------------|
| Monitoreo | Monitor multiparamétrico, desfibrilador (manual + DEA), oxímetro, capnógrafo |
| Vía aérea | Laringoscopio (convencional + video), tubos ET (rango pediátrico-adulto), dispositivos supraglóticos, set cricotirotomía |
| Circulatorio | Bombas infusión, calentador de fluidos, IO (intraóseo), set de toracostomía |
| Imagenología | Ecógrafo point-of-care (POCUS), acceso a TC 24/7 |
| Farmacología | Carro de paro estandarizado (AHA), kit RSI, kit sedación procedural |
| Inmovilización | Tabla espinal, collar cervical, férulas, pelvic binder |

**Salud mental:**

| Categoría | Dispositivos / insumos |
|-----------|----------------------|
| Evaluación | Escalas impresas (PHQ-9, GAD-7, Columbia, HoNOS), material psicoeducativo |
| Contención | Contención mecánica certificada (uso excepcional, protocolo estricto), sala de contención acolchada |
| Farmacología | Kit sedación de emergencia (haloperidol, midazolam, lorazepam IM) |
| Seguridad | Alarmas personales staff, botón pánico, CCTV zonas comunes |
| Rehabilitación | Material terapia ocupacional, sala multiuso, espacios exteriores seguros |

**HaH:**

| Categoría | Dispositivos / insumos |
|-----------|----------------------|
| Monitoreo RPM | Oxímetro BLE, tensiómetro BLE, termómetro, tablet/hub transmisión |
| Tratamiento | Bomba infusión portátil, concentrador O2 portátil, nebulizador |
| Diagnóstico | Point-of-care testing (glucómetro, INR, PCR rápido) |
| Comunicación | Tablet paciente (videollamada), conectividad 4G/WiFi backup |
| Logística | Kit curación, insumos EV, contenedor REAS domiciliario |

### G.2 Stock crítico y cadena de frío

| Categoría | Criterio stock mínimo | Cadena de frío |
|-----------|----------------------|---------------|
| Medicamentos críticos (carro paro, RSI, AB 1ra línea) | 72h consumo promedio + 50 % buffer | 2-8 °C refrigerados; monitoreo continuo T° |
| Hemoderivados | Según convenio banco de sangre; O− emergencia in situ | 2-6 °C (GR), 20-24 °C (plaquetas), −18 °C (PFC) |
| Vacunas (si aplica) | Según PAI; stock campaña estacional | 2-8 °C; registro digital T° cada 30 min |
| Insumos descartables | 30d consumo; punto reorden automatizado (HCE/ERP) | N/A |
| Gases medicinales | Respaldo ≥48h; manifold con switch automático | N/A |

### G.3 Mantenimiento y ciclo de vida

| Tipo mantenimiento | Frecuencia | Responsable | Registro |
|--------------------|-----------|-------------|---------|
| Preventivo programado | Según fabricante (mensual/trimestral/anual) | Biomédica / proveedor | Ficha equipo + HCE integrada |
| Correctivo | Ante falla; respuesta ≤4h equipos críticos | Biomédica / proveedor | Orden trabajo + downtime log |
| Calibración | Semestral o según norma (INN/NCh) | Laboratorio acreditado | Certificado calibración |
| Obsolescencia | Vida útil según fabricante; evaluación cada 5 años | Comité inversiones | Informe técnico-económico |
| Baja y disposición | Al cumplir vida útil o falla irreparable | Biomédica + finanzas | Acta de baja + disposición REAS |

---

## Anexo H: Marco normativo (adaptación local)

Referencia: [00-indice §5](urn:pro:kb:gestion-redes-indice) — Marco normativo y regulatorio completo.

### Plantilla de adaptación territorial

```yaml
adaptación_territorial:
  servicio_salud: "[Nombre Servicio de Salud]"
  región: "[Región]"
  fecha_adaptación: "YYYY-MM-DD"
  responsable: "[Cargo + nombre]"

  normativa_local:
    - norma: "Resolución exenta N° XXX"
      materia: "[Tema específico]"
      impacto_corpus: "[Capítulo/sección que modifica o complementa]"

  recursos_disponibles:
    establecimientos:
      - nombre: "[Hospital/CESFAM]"
        nivel: "[Primario/Secundario/Terciario]"
        camas: N
        servicios: "[Lista]"
    dotación_total_fte: N
    presupuesto_anual_mm: N

  brechas_identificadas:
    - dominio: "[Ej: Urgencias, SM, HaH]"
      brecha: "[Descripción]"
      plan_cierre: "[Acción + plazo]"

  adaptaciones_específicas:
    - sección_corpus: "[Ej: Cap. 18 Triaje]"
      adaptación: "[Modificación local justificada]"
      aprobado_por: "[Cargo]"

  indicadores_territoriales:
    - indicador: "[KPI adicional local]"
      fórmula: "[Fórmula]"
      meta: "[Meta local]"
      justificación: "[Por qué difiere del corpus]"
```

---

## Anexo I: Referencias clave

**Gestión de redes y sistemas de salud:**
1. OPS/OMS. Redes Integradas de Servicios de Salud (RISS): Conceptos, opciones de política y hoja de ruta. 2010.
2. WHO. Framework on Integrated People-Centred Health Services. 2016.
3. Starfield B. Primary Care: Balancing Health Needs, Services, and Technology. 1998.
4. OCDE. Health at a Glance 2023: OECD Indicators. 2023.
5. MINSAL Chile. Modelo de Atención Integral en Salud Familiar y Comunitaria. 2019.
6. MINSAL Chile. Orientaciones para la implementación del modelo de atención integral. 2023.

**Calidad y seguridad:**
7. IHI. Framework for Improving Joy in Work. 2017.
8. IHI. Psychology of Change Framework. 2020.
9. Donabedian A. The Quality of Care: How Can It Be Assessed? JAMA. 1988.
10. OMS. Marco de acción para la seguridad del paciente 2021-2030. 2021.
11. AHRQ. Making Healthcare Safer III. 2022.

**Urgencias:**
12. ACEP. Emergency Department Benchmarking Alliance. 2023.
13. Gilboy N et al. Emergency Severity Index (ESI) v4. AHRQ. 2020.
14. AHA. Guidelines for CPR and ECC. 2023.
15. Surviving Sepsis Campaign. International Guidelines. 2021.
16. NICE. Emergency and Acute Medical Care for Adults. 2022.
17. ATLS. Advanced Trauma Life Support, 10th ed. ACS. 2018.
18. NFPA. Standard 1710: Organization and Deployment of Fire Suppression Operations, EMS. 2020.

**Salud mental:**
19. OMS. Plan de Acción sobre Salud Mental 2013-2030. 2021.
20. OMS. mhGAP Intervention Guide v2.0. 2022.
21. NICE. Self-harm: Assessment, Management and Preventing Recurrence. 2022.
22. NHS England. Mental Health Services Data Set (MHSDS). 2023.
23. Safewards. Intervention to Reduce Conflict and Containment. 2022.
24. Posner K et al. Columbia-Suicide Severity Rating Scale (C-SSRS). 2011.

**Hospitalización domiciliaria:**
25. Levine DM et al. Hospital-Level Care at Home for Acutely Ill Adults. Ann Intern Med. 2020.
26. Federman AD et al. Association of a Bundled Hospital-at-Home and 30-Day Postacute Transitional Care Program. JAMA Intern Med. 2018.
27. Shepperd S et al. Hospital at Home: Home-Based End-of-Life Care. Cochrane. 2021.
28. Leff B. Defining and Disseminating the Hospital-at-Home Model. CMAJ. 2009.

**Interoperabilidad y salud digital:**
29. HL7 FHIR. Release 4 (R4) Specification. 2019.
30. MINSAL Chile. Guía de interoperabilidad HL7 FHIR CL Core. 2023.
31. HIMSS. Electronic Medical Record Adoption Model (EMRAM). 2023.

**Gestión del cambio y mejora continua:**
32. Kotter JP. Leading Change. Harvard Business Review Press. 2012.
33. Langley GJ et al. The Improvement Guide (Model for Improvement / PDSA). Jossey-Bass. 2009.
34. PMI. A Guide to the Project Management Body of Knowledge (PMBOK), 7th ed. 2021.

**Normativa chilena:**
35. Ley 19.937. Autoridad Sanitaria y Gestión (Redes asistenciales). 2004.
36. Ley 19.966. Régimen de Garantías Explícitas en Salud (GES/AUGE). 2004.
37. Ley 20.584. Derechos y Deberes del Paciente. 2012.
38. Ley 20.422. Igualdad de Oportunidades e Inclusión Social de Personas con Discapacidad. 2010.
39. DS 6/2009. Reglamento sobre manejo de residuos de establecimientos de atención de salud (REAS). 2009.

---

## Anexo J: Índice analítico

| Palabra clave | Archivo | Sección(es) |
|---------------|---------|-------------|
| Alta segura | 01-general, 05-herramientas | Cap. 10; Anexo B.3, C.2 |
| Boarding | 05-herramientas | Anexo A.2, B.1 |
| Cadena de frío | 05-herramientas | Anexo G.2 |
| Camas (gestión) | 01-general, 05-herramientas | Cap. 9; Anexo B.1, C.2 |
| Ciberseguridad | 05-herramientas | Anexo D.4 |
| Columbia (C-SSRS) | 05-herramientas | Anexo A.3, B.4, E.3 |
| Contención (SM) | 05-herramientas | Anexo A.3, G.1 |
| Contrarreferencia | 01-general, 05-herramientas | Cap. 1, 7; Anexo A.1, B.2 |
| Cuádruple Meta | 00-indice, 01-general | §1; Cap. 1.2 |
| DRG / GRD | 01-general, 05-herramientas | Cap. 11; Anexo A.1, A.5 |
| EMS / SAMU | 05-herramientas | Anexo A.2, B.1, B.5, G.1 |
| eReferral | 01-general, 05-herramientas | Cap. 7; Anexo B.2, B.3, D.1 |
| ESI (triaje) | 05-herramientas | Anexo A.2, B.1, C.4, E.1 |
| FHIR | 01-general, 05-herramientas | Cap. 8; Anexo D.1, D.2, D.3 |
| GES / AUGE | 01-general, 05-herramientas | Cap. 5; Anexo A.1 |
| Gobernanza | 00-indice, 01-general, 05-herramientas | §1; Cap. 2; Anexo C.2, K |
| HaH | 05-herramientas | Anexo A.4, B.5, C.1, G.1, K |
| HoNOS | 05-herramientas | Anexo A.3, D.1 |
| IAM (infarto) | 05-herramientas | Anexo A.2, B.1 |
| IAAS | 05-herramientas | Anexo A.4, A.5 |
| KPI | 01-general, 05-herramientas | Cap. 1-14; Anexo A (completo) |
| LOS (estancia) | 05-herramientas | Anexo A.1, A.2, A.4 |
| LWBS | 05-herramientas | Anexo A.2 |
| Madurez (modelo) | 05-herramientas | Anexo K |
| MCI (incidente masivo) | 05-herramientas | Anexo E.2 |
| Mejora continua (PDSA) | 01-general, 05-herramientas | Cap. 4; Anexo C.2 |
| NPS | 05-herramientas | Anexo A.1, A.5 |
| PDSA | 01-general, 05-herramientas | Cap. 4; Anexo C.2, I |
| PHQ-9 | 05-herramientas | Anexo A.3, E.3 |
| PREMs | 05-herramientas | Anexo A.1, A.2, A.3, A.4 |
| RACI | 05-herramientas | Anexo C.2 |
| RPM (monitoreo remoto) | 05-herramientas | Anexo A.4, B.5, D.2, G.1 |
| Sepsis | 05-herramientas | Anexo A.2, B.1 |
| Simulación | 05-herramientas | Anexo E.1, E.2 |
| SLA | 05-herramientas | Anexo C.1 |
| SM (salud mental) | 05-herramientas | Anexo A.3, B.4, C.1, E.3, K |
| SNOMED CT | 05-herramientas | Anexo D.3 |
| SOP | 05-herramientas | Anexo A.1, C.4 |
| Suicidio | 05-herramientas | Anexo A.3, B.4, C.1, E.3 |
| Triaje | 05-herramientas | Anexo A.2, B.1, C.4, E.1 |
| Trombolisis / trombectomía | 05-herramientas | Anexo A.2, C.1 |

---

## Anexo K: Modelo de madurez

### Rúbrica de madurez: 7 dominios × 5 niveles

| Dominio | 1 — Inicial | 2 — Definido | 3 — Estandarizado | 4 — Gestionado | 5 — Optimizado |
|---------|-------------|-------------|-------------------|----------------|----------------|
| **Gobernanza** | Sin estructura formal; decisiones reactivas ad-hoc | Organigrama definido; comités constituidos sin periodicidad regular | Roles RACI asignados; reuniones programadas; convenios inter-nodos vigentes | KPIs de gestión monitoreados; decisiones basadas en datos; rendición de cuentas activa | Gobernanza adaptativa; benchmarking sistemático; ciclos OKR integrados con planificación estratégica |
| **Integración clínica** | Derivaciones en papel; sin contrarreferencia; fragmentación severa | Proceso de referencia definido; contrarreferencia esporádica (<30 %) | eReferral electrónico; contrarreferencia ≥60 %; protocolos derivación por patología | Trazabilidad completa paciente en red; navigator; contrarreferencia ≥80 % en ≤7d | Continuidad longitudinal medida (UPC ≥0.75); integración bidireccional tiempo real; coordinación proactiva |
| **Calidad y seguridad** | Sin reporte de incidentes; auditorías inexistentes | Sistema reporte incidentes implementado; comité calidad constituido | SOPs vigentes ≥80 %; auditorías programadas; cultura de reporte incipiente | Ciclos PDSA con mejoras sostenidas; EA monitoreados; acreditación vigente | Cultura justa instalada; HRO (alta confiabilidad); mejora continua basada en analítica predictiva |
| **Salud digital** | HCE parcial o en papel; sin interoperabilidad | HCE en producción; interfaces punto a punto | HCE integrada red; perfiles FHIR CL Core; terminologías estandarizadas (SNOMED, LOINC) | Bus de eventos clínicos; dashboards KPI en tiempo real; uptime ≥99.5 % | Analítica predictiva; IA embebida en flujos clínicos; interoperabilidad semántica completa |
| **Urgencias** | Sin triaje estructurado; tiempos no medidos | ESI implementado; door-to-triage medido; protocolos tiempo-dependientes documentados | Cumplimiento door-to-doctor ≤30 min; LWBS ≤5 %; boarding monitorizado | Boarding ≤2h; protocolos tiempo-dependientes con cumplimiento ≥85 %; gestión de flujo activa | Full-capacity protocol automatizado; predicción demanda; zero-boarding sostenido; integración EMS-SUH seamless |
| **Salud mental** | Atención episódica; sin seguimiento post-alta; sin equipo comunitario | Equipo SM constituido; protocolo crisis documentado; seguimiento post-alta definido | Retención ≥50 %; EMC operativo; PCI en ≥60 % usuarios; contenciones en descenso | Seguimiento post-alta suicidio 100 %; outcomes medidos (PHQ-9, HoNOS); integración SM-APS | Recovery-oriented; cero contención como meta; estratificación predictiva; red comunitaria articulada |
| **HaH** | Sin programa; todo paciente se hospitaliza convencionalmente | Piloto HaH en marcha; criterios elegibilidad definidos; equipo dedicado | RPM operativo 24/7; escalamiento ≤10 %; LOS ≤3.2d; SLA respuesta deterioro definido | Costo por episodio ≤80 % DRG; readmisión ≤8.6 %; PREMs ≥85; integración con APS egreso | Modelo predicción elegibilidad; HaH como opción por defecto para diagnósticos elegibles; analítica en tiempo real |

**Uso**: evaluar cada dominio independientemente. Nivel global = mínimo entre dominios (cadena más débil). Plan de mejora prioriza dominios en nivel 1-2.

---

*Ref cruzada*: [00-indice](urn:pro:kb:gestion-redes-indice) | [01-general](urn:pro:kb:gestion-redes-general)

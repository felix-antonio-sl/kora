---
_manifest:
  urn: urn:salud:kb:informatica-medica-salud-digital
  provenance:
    created_by: FS
    created_at: '2026-05-07'
    source: Digital Health (Rivas & Boillat, Springer 2023) + Bridging AI (Ch. 7).
      INBOX/salud/
  version: 1.0.0
version: 1.0.0
status: publicado
family: guide
tags:
- salud
- digital-health
- telemedicina
- mhealth
- wearable
- remote-monitoring
lang: es
relations:
  cites:
  - urn:salud:kb:informatica-medica-indice
extensions:
  kora:
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:salud:kb:informatica-medica-salud-digital
---

# Salud Digital y Telemedicina

## Telemedicina

Modalidades:
- **Sincrona**: videollamada en tiempo real (consulta, triaje, seguimiento)
- **Asincrona**: store-and-forward (imagenes, examenes, e-consulta)
- **Monitoreo remoto**: dispositivos que transmiten datos fisiologicos continuos

### Evidencia post-COVID-19

La pandemia acelero la adopcion regulatoria y clinica de telemedicina.
Resultados en:
- **Cronicos**: comparable a atencion presencial en diabetes, HTA, salud mental
- **Urgencias**: tele-triaje reduce visitas innecesarias
- **Post-quirurgico**: seguimiento remoto seguro para procedimientos de bajo riesgo
- **HODOM**: telemonitoreo permite hospitalizacion domiciliaria segura

## Limitaciones

- **Brecha digital**: acceso desigual a dispositivos y conectividad
- **Examen fisico limitado**: no reemplaza palpacion, auscultacion, percusion
- **Fatiga de pantalla**: clinico y paciente
- **Integracion con sistemas legacy**: EHR no disenados para telemedicina

## Salud movil (mHealth)

- **Apps de paciente**: adherencia, monitoreo de sintomas, educacion
- **Wearables**: frecuencia cardiaca, SpO2, actividad, sueno, ECG
- **Sensores ambientales**: deteccion de caidas, patrones de actividad en LTSS
- **Chatbots**: triaje de sintomas, recordatorios, educacion

### Validacion clinica

La mayoria de apps de salud no tienen evidencia clinica publicada.
Criterios de evaluacion:
- ¿Respaldo por sociedad cientifica?
- ¿Estudio clinico publicado?
- ¿Aprobacion regulatoria (FDA 510k, CE mark)?
- ¿Integracion con EHR?

## Tecnologias emergentes

- **Realidad aumentada/virtual**: entrenamiento quirurgico, rehabilitacion,
 manejo del dolor, salud mental
- **Blockchain en salud**: identidad del paciente, consentimiento,
 trazabilidad de medicamentos, intercambio de datos
- **Digital nudging**: economia conductual aplicada a cambio de habitos
 (recordatorios, defaults, incentivos)

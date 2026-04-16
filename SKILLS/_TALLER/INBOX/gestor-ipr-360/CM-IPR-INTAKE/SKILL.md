---
_manifest:
  urn: urn:gn:skill:gestor-ipr-360-ipr-intake:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Detectar rol del usuario y fase IPR para adaptar tono, profundidad y routing del Gestor IPR 360.

## Input/Output
- **Input:** Mensaje entrante del usuario
- **Output:** Rol detectado + Fase IPR + Estado FSM objetivo

## Procedimiento
DETECCION ROL (por indicadores linguisticos):
- FORMULADOR_EXTERNO: [postular, mi proyecto, requisitos, municipio]
- ANALISTA_DIPIR: [evaluar, BIP, MDSF, cartera, RS]
- PROFESIONAL_DAF: [CDP, convenio, SIGFE, devengo, Subtitulo]
- CONSEJERO: [CORE, aprobar, fiscalizar, transparencia]
- JEFATURA: [division, informe para, Gobernador]

DETECCION FASE IPR:
- FORMULACION: [idea, formular, postular]
- EVALUACION: [RS, MDSF, RATE]
- FINANCIAMIENTO: [CORE, CDP, aprobar]
- EJECUCION: [convenio, transferir, avance]
- MODIFICACION: [reasignar, suplemento]
- RENDICION: [rendir, SISREC, CGR]
- CIERRE: [liquidar, ex-post]

ROUTING: Rol + Fase → Estado FSM objetivo

## Signature Output
Clasificacion: [Rol detectado] + [Fase IPR] + [Estado objetivo]. Tono adaptado al rol.

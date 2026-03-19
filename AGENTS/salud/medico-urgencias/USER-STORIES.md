---
_manifest:
  urn: "urn:salud:medico-urgencias:user-stories:1.0.0"
  type: "product_backlog"
  date: "2026-03-19"
---

# Historias de Usuario — Medico Urgencia + Asistente Inteligente

## INICIO TURNO

US-001 Quiero recibir handoff estructurado del turno anterior c/ pendientes por paciente
US-002 Quiero ver censo actual box completo: nombre, box, triage, espera, dx provisional
US-003 Quiero identificar pacientes criticos al tomar turno sin leer cada ficha
US-004 Quiero ver pacientes c/ resultados pendientes de turno anterior
US-005 Quiero ver pacientes c/ espera prolongada que necesitan reevaluacion

## RECEPCION PACIENTE NUEVO

US-010 Quiero ver triage + motivo consulta + SV antes de ir al box
US-011 Quiero acceder historia antigua del paciente en segundos (antec, med habituales, alergias, cirugias)
US-012 Quiero ver urgencias previas del paciente c/ dx y fechas
US-013 Quiero ver hospitalizaciones previas c/ epicrisis resumida
US-014 Quiero ver labs previos recientes para comparar tendencia
US-015 Quiero saber si paciente tiene patologia GES activa
US-016 Quiero ver atenciones ambulatorias recientes (controles cronicos)
US-017 Quiero ver medicamentos cronicos para anticipar interacciones
US-018 Quiero alerta automatica si paciente tiene alergia medicamentosa registrada
US-019 Quiero saber si paciente es recurrente (visitas frecuentes urgencia)

## EVALUACION CLINICA

US-020 Quiero dictar anamnesis telegraficamente y que se registre estructurada
US-021 Quiero registrar examen fisico solo hallazgos positivos
US-022 Quiero que asistente detecte red flags automaticamente segun cuadro (VINDICATE)
US-023 Quiero calculo automatico scores: qSOFA, CURB-65, Wells, HEART, Glasgow, NEWS2
US-024 Quiero sugerencia dx diferencial basada en datos ingresados
US-025 Quiero alerta si combinacion sintomas/signos sugiere patologia tiempo-dependiente (IAM, ACV, sepsis, TEP)
US-026 Quiero shock index automatico cuando ingreso SV
US-027 Quiero alerta deterioro si SV empeoran respecto a triage

## SOLICITUD EXAMENES

US-030 Quiero solicitar bateria estandar por sospecha dx (ej: "panel dolor toracico")
US-031 Quiero ver que examenes ya estan solicitados para no duplicar
US-032 Quiero sugerencia examenes segun dx diferencial
US-033 Quiero solicitar imagenes c/ indicacion clinica precargada

## RESULTADOS

US-040 Quiero notificacion inmediata cuando llegan resultados de mi paciente
US-041 Quiero ver solo labs alterados c/ valor numerico y rango referencia
US-042 Quiero comparacion automatica c/ labs previos (delta, tendencia)
US-043 Quiero interpretacion automatica de patron lab (ej: pancitopenia, insuficiencia renal, patron hepatico)
US-044 Quiero interpretacion informe radiologico: hallazgos relevantes, correlacion clinica, red flags
US-045 Quiero alerta valores criticos (K >6, troponina positiva, lactato >4, Hb <7)
US-046 Quiero ver resultados labs WEB_SANCARLOS parseados c/ valores reales no solo listado ordenes
US-047 Quiero ver imagen directa (Rx, TAC) y recibir orientacion hallazgos

## DECISION CLINICA

US-050 Quiero sintesis clinica completa del caso para decidir conducta
US-051 Quiero verificacion automatica interacciones farmacologicas antes de indicar tto
US-052 Quiero calculo dosis ajustada a funcion renal (ClCr) si IRC/IRA
US-053 Quiero calculo dosis pediatrica por peso
US-054 Quiero verificacion contraindicaciones por antecedentes (AINES+IRC, BB+asma, etc)
US-055 Quiero consulta rapida protocolo/guia clinica segun patologia
US-056 Quiero criterios hospitalizacion vs alta para patologia especifica
US-057 Quiero evaluacion riesgo social (adulto mayor solo, sospecha maltrato, riesgo suicida)

## DOCUMENTACION CLINICA

US-060 Quiero generar nota atencion completa (anamnesis, EF, hipotesis, indicaciones) en <30 seg
US-061 Quiero generar alta ambulatoria telegrafica c/ indicaciones, control, signos alarma
US-062 Quiero generar ingreso hospitalario c/ justificacion, dx CIE-10, indicaciones
US-063 Quiero generar interconsulta dirigida c/ pregunta especifica para especialidad
US-064 Quiero generar epicrisis egreso c/ evolucion, dx, condicion alta
US-065 Quiero editar nota existente sin perder campos previos (write-field)
US-066 Quiero agregar evolucion a paciente ya evaluado (nueva nota, no sobrescribir)
US-067 Quiero que CIE-10 se sugiera automaticamente segun dx escrito
US-068 Quiero preview documento antes de guardar definitivo
US-069 Quiero copiar formato de indicacion frecuente (ej: "protocolo SCA", "protocolo sepsis")

## INTERCONSULTAS

US-070 Quiero generar IC urgente c/ datos minimos necesarios para especialidad
US-071 Quiero saber si IC ya fue respondida
US-072 Quiero incluir automaticamente labs e imagenes relevantes en IC
US-073 Quiero IC precargada segun especialidad (cirugia: datos abdomen, neuro: Glasgow+TAC, cardio: ECG+troponinas)

## MONITOREO BOX

US-080 Quiero ver panel tiempo real: todos mis pacientes, estado, espera, pendientes
US-081 Quiero alerta si paciente en box >4hrs sin reevaluacion
US-082 Quiero alerta si SV de paciente en observacion se deterioran
US-083 Quiero ver pacientes listos para alta (examenes completos, observacion cumplida)
US-084 Quiero ver pacientes esperando cama (ingreso indicado, pendiente traslado)
US-085 Quiero saber cuantos pacientes tengo vs capacidad box
US-086 Quiero filtrar pacientes por triage (C1-C5), por box, por estado

## CAMBIO TURNO

US-090 Quiero generar handoff automatico de todo el box para entregar
US-091 Quiero handoff por paciente: resumen, pendientes, plan, criticos
US-092 Quiero marcar pacientes que requieren atencion prioritaria entrante
US-093 Quiero historial de acciones realizadas durante mi turno
US-094 Quiero estadisticas turno: atendidos, altas, ingresos, IC, tiempos

## PACIENTE RECURRENTE

US-100 Quiero historia longitudinal completa cruzando urgencias + hospitalizaciones + ambulatorio
US-101 Quiero timeline cronologico unificado de todos los encuentros
US-102 Quiero detectar patron consulta frecuente (dolor cronico, psiquiatrico, social)
US-103 Quiero ver ultima atencion urgencia detallada (que se hizo, que se indico)
US-104 Quiero ver si paciente tiene hospitalizaciones recientes (readmision)

## POBLACIONES ESPECIALES

US-110 Quiero calculo dosis pediatrica automatico c/ peso
US-111 Quiero scores geriatricos (fragilidad, riesgo caida, delirium)
US-112 Quiero alerta polifarmacia en adulto mayor (>5 farmacos)
US-113 Quiero evaluacion riesgo obstetrico si embarazada
US-114 Quiero protocolo intoxicacion segun toxico (antidoto, dosis, monitoreo)
US-115 Quiero evaluacion riesgo suicida estructurada
US-116 Quiero clasificacion trauma (ISS, RTS) si politraumatizado

## CODIGOS/PROTOCOLOS ACTIVADOS

US-120 Quiero checklist protocolo IAM (SDST: door-to-balloon, NSDST: TIMI score)
US-121 Quiero checklist protocolo ACV (NIHSS, ventana trombolisis, criterios inclusion/exclusion)
US-122 Quiero checklist protocolo sepsis (hora 1: hemocultivos, lactato, cristaloides, ATB)
US-123 Quiero checklist PCR/RCP (algoritmo ACLS, tiempos, farmacos)
US-124 Quiero checklist via aerea dificil
US-125 Quiero checklist trauma (ABCDE, FAST, estabilizacion)

## CALIDAD Y SEGURIDAD

US-130 Quiero alerta duplicidad atencion (paciente ya tiene ficha abierta)
US-131 Quiero alerta alergia antes de indicar farmaco
US-132 Quiero consentimiento informado precargado por procedimiento
US-133 Quiero registro procedimientos invasivos (via central, intubacion, puncion lumbar)
US-134 Quiero notificacion obligatoria automatica si dx es ENO (enfermedad notificacion obligatoria)
US-135 Quiero trazabilidad: quien indico que, cuando, a quien

## COMUNICACION

US-140 Quiero comunicacion rapida c/ laboratorio (estado muestra, resultado urgente)
US-141 Quiero comunicacion c/ imagenes (estado examen, informe preliminar)
US-142 Quiero comunicacion c/ admision (disponibilidad camas por servicio)
US-143 Quiero comunicacion c/ ambulancia/SAMU (paciente en traslado, ETA)

## ADMINISTRATIVO

US-150 Quiero certificado reposo medico precargado
US-151 Quiero derivacion a otro establecimiento c/ formulario
US-152 Quiero licencia medica electronica
US-153 Quiero estadisticas personales: pacientes/turno, tiempos atencion, dx frecuentes

## CONOCIMIENTO A DEMANDA (PROTOCOLO NEO)

US-160 Quiero cargar conocimiento especializado a demanda antes de evaluar paciente fuera de mi expertise habitual
US-161 Quiero recibir definiciones core de un dominio en segundos sin buscar en textos
US-162 Quiero perlas clinicas high-yield que el especialista sabe y yo olvido
US-163 Quiero vocabulario tecnico para hablar c/ especialista en su idioma al hacer IC o recibir respuesta
US-164 Quiero algoritmos de decision esenciales del dominio aplicables en urgencia
US-165 Quiero scores relevantes c/ puntos corte y interpretacion practica
US-166 Quiero red flags especificos del dominio que no puedo perder desde urgencia
US-167 Quiero que conocimiento cargado persista en sesion para aplicar en evaluaciones posteriores del turno
US-168 Quiero topicos pre-indexados de alta frecuencia (cardio, neuro, toxico, sepsis, trauma) c/ carga instantanea
US-169 Quiero poder cargar cualquier topico on-demand aunque no este pre-indexado
US-170 Quiero que carga sea telegrafica y accionable, no academica

---

TOTAL: 78 historias de usuario
16 dominios funcionales

Priorizacion sugerida por impacto en flujo turno:
1. Documentacion clinica (US-060 a US-069)
2. Resultados (US-040 a US-047)
3. Monitoreo box (US-080 a US-086)
4. Recepcion paciente (US-010 a US-019)
5. Protocolo NEO (US-160 a US-170)

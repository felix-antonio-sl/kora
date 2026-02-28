---
_manifest:
  urn: "urn:pro:skill:medico-urgencias-razonamiento-clinico:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar razonamiento clinico estructurado sobre datos parseados del paciente. Integra 4 procesos: deteccion red flags (VINDICATE), interacciones farmacologicas, integracion fisiologica y modulacion de contexto segun tipo output.

## I/O

- **Input:** ClinicalData parseada (historia_antigua, derivacion, informacion_atencion, imagenes_clinicas, tipo_output) + PIVOTE_IMAGENOLOGICO (si disponible)
- **Output:** RAZONAMIENTO_CLINICO: red_flags, interacciones, indicadores_fisiologicos, contexto_modulado, sospecha_dx, dx_diferencial, conducta_sugerida

## Procedimiento

### Fase 1: RED_FLAGS (VINDICATE)

Busqueda activa sistematica:
- **V**ascular: isquemia, sangrado, TVP/TEP, diseccion, aneurisma
- **I**nfeccion: sepsis, meningitis, fasceitis, endocarditis
- **N**eoplasia: compresion medular, sindrome vena cava, hipercalcemia maligna
- **D**egenerativo/Deficiencia: crisis adrenal, cetoacidosis, mixedema
- **I**nflamatorio/Iatrogeno: anafilaxia, reaccion adversa, sindrome serotoninergico
- **C**ongenito: crisis falciforme, porfiria (si contexto sugiere)
- **A**utoimmune: crisis lupica, vasculitis
- **T**rauma: lesion oculta, maltrato, blast injury
- **E**ndocrino: tormenta tiroidea, crisis suprarrenal, hipoglicemia severa

Si red flag detectado -> marcar URGENCIA: CRITICO y priorizar en output.

### Fase 2: INTERACTION_CHECK

Matriz interacciones:
1. Farmaco-farmaco: revisar medicamentos habituales + tto propuesto. Buscar: QT prolongado, sangrado (anticoagulantes+AINES), hipotension (antihipertensivos dobles), sindrome serotoninergico, nefrotoxicidad combinada.
2. Farmaco-enfermedad: contraindicaciones absolutas por antecedentes. Buscar: AINES+IRC, betabloqueadores+asma, metformina+IRA, trombolisis+ACV hemorragico.
3. Solo reportar interacciones clinicamente significativas que cambien conducta.

### Fase 3: PHYSIO_INTEGRATION

Indicadores fisiologicos integrados:
1. Shock Index (FC/PAS): >0.9 sugiere shock compensado. >1.3 shock descompensado.
2. Delta-T (temp central - periferica): >3C sugiere mala perfusion.
3. Lactato trend: ascenso sugiere hipoperfusion tisular progresiva.
4. Glasgow trend: descenso >2 puntos sugiere deterioro neurologico.
5. qSOFA: FR>=22 + PAS<=100 + Glasgow<15 -> 2+ sugiere sepsis.
6. Solo calcular/reportar si datos disponibles. No inferir valores ausentes.

### Fase 4: CONTEXT_MODULATION

Ajustar profundidad razonamiento segun tipo_output:
- **sintesis**: razonamiento completo, enfasis en dx diferencial y plan inmediato
- **alta**: enfasis en criterios seguridad ambulatoria, signos alarma, red flags descartados
- **hospitalizacion**: enfasis en justificacion ingreso, gravedad, indicadores fisiologicos
- **interconsulta**: enfasis en pregunta clinica especifica, datos relevantes para especialidad
- **epicrisis**: enfasis en evolucion, respuesta tratamiento, condicion egreso

Filtro parsimonia final: eliminar todo razonamiento que no impacte output solicitado.

## Signature Output

```
RAZONAMIENTO_CLINICO:
  red_flags: [lista si detectados, "ninguno identificado" si no]
  interacciones: [lista si detectadas, "sin interacciones relevantes" si no]
  indicadores_fisiologicos: [valores calculados si datos disponibles]
  contexto_modulado: [tipo_output + ajustes profundidad]
  sospecha_dx: [diagnostico principal]
  dx_diferencial: [max 3 alternativas relevantes]
  conducta_sugerida: [plan inmediato telegrafico]
```

---
_manifest:
  urn: urn:salud:skill:medico-urgencias-neo-loader:1.0.0
  type: lazy_load_endofunctor
---

## Proposito
Carga instantanea de conocimiento especializado a demanda. Al invocar "cargar [topico]", genera paquete comprimido que permite al medico de urgencia hablar, pensar y actuar como especialista en el topico solicitado. Analogia: Neo en Matrix — "I know kung fu".

## Input/Output
- **Input:** topico: string (especialidad, patologia, procedimiento o dominio clinico)
- **Output:** NEO_PROTOCOL: paquete conocimiento comprimido, telegrafico, accionable

## Procedimiento

### Paso 1: Identificar dominio
Clasificar topico en:
- ESPECIALIDAD (cardio, neuro, nefro, gastro, hemato, endocrino, reumato, infecto, toxico, trauma, pediatria, obstetricia, psiquiatria, cirugia, oftalmo, ORL, dermato, urologia, neumo, intensivo)
- PATOLOGIA ESPECIFICA (IAM, ACV, sepsis, cetoacidosis, status epileptico, crisis hipertensiva, TEP, etc)
- PROCEDIMIENTO (intubacion, via central, puncion lumbar, toracostomia, cardioversion, sedacion procedural, etc)
- SCORE/HERRAMIENTA (NIHSS, CURB-65, Wells, HEART, Child-Pugh, MELD, etc)

### Paso 2: Generar paquete NEO_PROTOCOL

Estructura fija, 6 bloques:

**DEFINICIONES** (5-10)
Core concepts que definen el dominio. Solo lo esencial para no confundir terminologia. Sin fluff academico.

**PERLAS** (5-10)
High-yield facts que cambian conducta. Datos que el especialista sabe y el generalista olvida. Formato: hecho clinico breve + implicancia practica.

**VOCABULARIO** (15-25 terminos)
Palabras clave para hablar como especialista. Formato: termino = significado operativo en 1 linea. Incluir abreviaturas del dominio.

**GUIAS** (2-5 algoritmos)
Flujos de decision esenciales del dominio. Formato: IF/THEN telegrafico o pasos numerados. Solo algoritmos que impactan conducta inmediata en urgencia.

**SCORES** (si aplica)
Scores/calculadoras relevantes del dominio. Formato: nombre, variables, puntos corte, interpretacion.

**RED_FLAGS** (3-7)
Señales de alarma especificas del dominio que urgencia NO puede perder. Formato: signo/sintoma -> sospecha -> accion inmediata.

### Paso 3: Filtro parsimonia

- Solo incluir lo que un medico de urgencia necesita AHORA
- Excluir: fisiopatologia detallada, historia de la enfermedad, clasificaciones academicas exhaustivas, tratamientos cronicos ambulatorios
- Incluir: diagnostico diferencial urgente, tratamiento agudo, criterios de gravedad, cuando llamar al especialista, errores fatales comunes

### Paso 4: Formato output

Sin markdown. Telegrafico. Wrapper:

<neo_protocol topico="[TOPICO]">
[6 bloques]
</neo_protocol>

Cierre c/ frase: "Ya se [topico]."

## Protocolos Pre-indexados (Trigger Rapido)

Topicos de alta frecuencia en urgencia — generacion inmediata sin latencia:

| Trigger | Dominio |
|---|---|
| cardio | Emergencias cardiovasculares: SCA, arritmias, IC descompensada, emergencia HTA |
| neuro | Emergencias neurologicas: ACV, status epileptico, cefalea thunderclap, debilidad aguda |
| toxico | Toxicologia: intoxicaciones frecuentes, antidotos, descontaminacion |
| sepsis | Sepsis y shock septico: definiciones, bundles, vasopresores |
| trauma | Trauma: ABCDE, FAST, estabilizacion, criterios cirugia |
| via aerea | Via aerea dificil: algoritmo, RSI, plan B/C, cricotiroidotomia |
| pediatria | Urgencias pediatricas: dosis peso, deshidratacion, fiebre, convulsiones |
| obstetrica | Emergencias obstetricas: eclampsia, DPPNI, hemorragia postparto |
| renal | Emergencias renales: IRA, hiperkalemia, indicaciones dialisis urgente |
| gastro | Emergencias GI: HDA, abdomen agudo, pancreatitis, hepatitis fulminante |
| endocrino | Crisis endocrinas: CAD, EHH, crisis suprarrenal, tormenta tiroidea, mixedema |
| hemato | Emergencias hematologicas: CID, PTT, neutropenia febril, crisis falciforme |
| psiq | Emergencias psiquiatricas: agitacion, riesgo suicida, sindrome neuroleptico maligno |
| derma | Urgencias dermatologicas: SSJ/NET, angioedema, fasceitis necrotizante |
| oftalmo | Urgencias oftalmologicas: glaucoma agudo, OACR, desprendimiento retina, quemadura quimica |
| sedacion | Sedacion procedural: farmacos, dosis, monitorizacion, rescue |
| ventilacion | Ventilacion mecanica: modos, parametros iniciales, alarmas, weaning |
| ECG | Lectura ECG urgencia: SDST, arritmias letales, patrones criticos |
| eco | POCUS/FAST: ventanas, patologia urgente, protocolo RUSH |
| dolor | Manejo dolor urgencia: escalera, opioides, bloqueos, ketamina |

Cualquier otro topico: generacion on-demand.

## Signature Output
```
<neo_protocol topico="[TOPICO]">

DEFINICIONES
[5-10 definiciones core]

PERLAS
[5-10 clinical pearls high-yield]

VOCABULARIO
[15-25 terminos = significado operativo]

GUIAS
[2-5 algoritmos IF/THEN o pasos]

SCORES
[scores relevantes c/ puntos corte]

RED_FLAGS
[3-7 señales alarma -> sospecha -> accion]

</neo_protocol>

Ya se [topico].
```
